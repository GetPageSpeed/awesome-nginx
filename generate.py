#!/usr/bin/env python3
"""Generate the body of README.md for awesome-nginx.

Reads:
  - categories.yml                            (curation + ordering)
  - $NGINX_EXTRAS_DIR/modules/**/*.yml        (packaged-module catalog)
  - $NGINX_EXTRAS_DIR/discovered.db.json      (GitHub-discovered modules)

Writes:
  - the body between <!-- BEGIN GENERATED --> / <!-- END GENERATED -->
    markers in README.md.

Flags:
  --check  Exit 1 if README would change (CI drift check). No write.
"""

from __future__ import annotations

import argparse
import json
import os
import re
import sys
import urllib.error
import urllib.request
from concurrent.futures import ThreadPoolExecutor
from pathlib import Path

import yaml

REPO_ROOT = Path(__file__).resolve().parent
README_PATH = REPO_ROOT / "README.md"
CATEGORIES_PATH = REPO_ROOT / "categories.yml"
LINK_CACHE_PATH = REPO_ROOT / ".link-cache.json"
BEGIN_MARKER = "<!-- BEGIN GENERATED -->"
END_MARKER = "<!-- END GENERATED -->"

DEFAULT_NGINX_EXTRAS = Path.home() / "Projects" / "nginx-extras"

# Hard denylist — never emit a URL pointing at these repos, even if probing
# would somehow report 200 (e.g. transient redirect). These are the GetPageSpeed
# packaging-infra repos that are private by policy.
PRIVATE_REPO_DENYLIST = {
    "getpagespeed/rpmbuilder",
    "getpagespeed/debbuilder",
    "getpagespeed/buildstrap",
    "getpagespeed/getpagespeed-extras-release",
    "getpagespeed/nginx-extras",
    "getpagespeed/nginx-extras-docs",
}


def load_nginx_extras(extras_dir: Path) -> dict[str, dict]:
    """Return {handle: {repo, summary, plan}} for every modules/**/*.yml."""
    out: dict[str, dict] = {}
    modules_root = extras_dir / "modules"
    if not modules_root.is_dir():
        sys.exit(f"nginx-extras modules dir not found: {modules_root}")
    for path in sorted(modules_root.rglob("*.yml")):
        handle = path.stem
        try:
            data = yaml.safe_load(path.read_text())
        except Exception as exc:
            print(f"warning: failed to parse {path}: {exc}", file=sys.stderr)
            continue
        if not isinstance(data, dict):
            continue
        out[handle] = {
            "repo": (data.get("repo") or "").strip(),
            "summary": (data.get("summary") or "").strip(),
            "plan": data.get("plan", ""),
        }
    return out


def load_discovered(extras_dir: Path) -> dict[str, dict]:
    """Return discovered.db.json keyed by 'owner/repo'."""
    path = extras_dir / "discovered.db.json"
    if not path.is_file():
        return {}
    return json.loads(path.read_text())


def load_categories() -> dict:
    data = yaml.safe_load(CATEGORIES_PATH.read_text())
    if not isinstance(data, dict):
        sys.exit("categories.yml did not parse to a mapping")
    return data


def github_url(repo: str) -> str:
    return f"https://github.com/{repo}"


def docs_url(handle: str) -> str:
    """nginx-extras-docs deep link for a packaged module handle."""
    return f"https://nginx-extras.getpagespeed.com/modules/{handle}/"


def is_gps_repo(repo: str) -> bool:
    if not repo:
        return False
    owner = repo.split("/", 1)[0].lower()
    return owner in {"getpagespeed", "dvershinin"}


def normalize_description(text: str) -> str:
    """Single line, ends in a period (awesome-lint requirement)."""
    text = (text or "").strip()
    text = text.split("\n", 1)[0].strip()
    text = re.sub(r"\s+", " ", text)
    if not text:
        return text
    if text[-1] not in ".!?":
        text += "."
    return text


def render_entry(entry: dict) -> str:
    """Render one bullet."""
    label = entry["label"]
    url = entry["url"]
    desc = normalize_description(entry["description"])
    badges = []
    if entry.get("gps_packaged"):
        badges.append("📦")
    if entry.get("original_by_gps"):
        badges.append("⭐")
    badge_str = (" " + " ".join(badges)) if badges else ""
    base = f"- [{label}]({url}) - {desc}{badge_str}"
    return base


def sort_key(entry: dict) -> tuple:
    pin = entry.get("pin")
    pin = pin if isinstance(pin, int) else 9999
    return (pin, entry["label"].lower())


def build_entries(
    cats: dict,
    extras: dict[str, dict],
    discovered: dict[str, dict],
) -> dict[str, list[dict]]:
    """Group all entries by category name. Each entry is dict with rendering data."""
    by_cat: dict[str, list[dict]] = {c: [] for c in cats["categories_order"]}

    # nginx-extras-packaged modules
    nginx_extras_map = cats.get("nginx_extras") or {}
    seen_repos: set[str] = set()
    for handle, conf in nginx_extras_map.items():
        if handle not in extras:
            print(f"warning: handle '{handle}' in categories.yml not found in nginx-extras", file=sys.stderr)
            continue
        category = conf.get("category")
        if category not in by_cat:
            sys.exit(f"unknown category '{category}' for handle '{handle}'")
        meta = extras[handle]
        repo = meta["repo"]
        desc = conf.get("description") or meta.get("summary") or ""
        if conf.get("link"):
            url = conf["link"]
        elif repo:
            url = github_url(repo)
        else:
            url = docs_url(handle)
        label = conf.get("label") or (repo.split("/", 1)[-1] if repo else handle)
        by_cat[category].append({
            "label": label,
            "url": url,
            "description": desc,
            "handle": handle,
            "gps_packaged": True,
            "original_by_gps": is_gps_repo(repo),
            "pin": conf.get("pin"),
            "repo": repo,
        })
        if repo:
            seen_repos.add(repo.lower())

    # extras (not in nginx-extras)
    for ent in cats.get("extras") or []:
        category = ent.get("category")
        if category not in by_cat:
            sys.exit(f"unknown category '{category}' for extras entry {ent}")
        if "repo" in ent:
            repo = ent["repo"]
            url = github_url(repo)
            label = ent.get("title") or repo.split("/", 1)[-1]
            original_by_gps = ent.get("original_by_gps", is_gps_repo(repo))
            if repo.lower() in seen_repos:
                continue
            seen_repos.add(repo.lower())
        elif "url" in ent:
            url = ent["url"]
            label = ent["title"]
            original_by_gps = ent.get("original_by_gps", False)
        else:
            sys.exit(f"extras entry needs 'repo' or 'url': {ent}")
        by_cat[category].append({
            "label": label,
            "url": url,
            "description": ent.get("description", ""),
            "handle": None,
            "gps_packaged": ent.get("gps_packaged", False),
            "original_by_gps": original_by_gps,
            "pin": ent.get("pin"),
            "repo": ent.get("repo"),
        })

    # honourable mentions — auto-pull desc + stars from discovered.db.json
    for ent in cats.get("honourable") or []:
        category = ent.get("category", "Honourable mentions")
        if category not in by_cat:
            sys.exit(f"unknown category '{category}' for honourable entry {ent}")
        repo = ent["repo"]
        meta = discovered.get(repo, {})
        desc = ent.get("description") or meta.get("description") or "NGINX module."
        stars = meta.get("stars")
        if stars:
            desc = f"{normalize_description(desc).rstrip('.')} ({stars:,}★)"
        by_cat[category].append({
            "label": repo.split("/", 1)[-1],
            "url": github_url(repo),
            "description": desc,
            "handle": None,
            "gps_packaged": False,
            "original_by_gps": is_gps_repo(repo),
            "pin": ent.get("pin"),
            "repo": repo,
        })

    for cat in by_cat:
        by_cat[cat].sort(key=sort_key)
    return by_cat


def anchor(heading: str) -> str:
    """GitHub-style heading anchor: lowercase, non-word → -, collapse runs."""
    slug = heading.lower()
    slug = re.sub(r"[^\w\- ]", "", slug)
    slug = slug.replace(" ", "-")
    return slug


def render_body(by_cat: dict[str, list[dict]], order: list[str]) -> str:
    populated = [c for c in order if by_cat.get(c)]
    blocks: list[str] = ["## Contents\n"]
    for cat in populated:
        blocks.append(f"- [{cat}](#{anchor(cat)})")
    blocks.append("")
    for cat in populated:
        blocks.append(f"## {cat}\n")
        for e in by_cat[cat]:
            blocks.append(render_entry(e))
        blocks.append("")
    return "\n".join(blocks).rstrip() + "\n"


def splice_readme(body: str) -> str:
    current = README_PATH.read_text() if README_PATH.is_file() else ""
    if BEGIN_MARKER not in current or END_MARKER not in current:
        sys.exit(f"README.md is missing {BEGIN_MARKER} / {END_MARKER} markers")
    pre = current.split(BEGIN_MARKER, 1)[0]
    post = current.split(END_MARKER, 1)[1]
    return f"{pre}{BEGIN_MARKER}\n\n{body}\n{END_MARKER}{post}"


def load_link_cache() -> dict:
    if LINK_CACHE_PATH.is_file():
        try:
            return json.loads(LINK_CACHE_PATH.read_text())
        except Exception:
            return {}
    return {}


def save_link_cache(cache: dict) -> None:
    LINK_CACHE_PATH.write_text(json.dumps(cache, indent=2, sort_keys=True) + "\n")


def probe_url(url: str) -> int:
    """HEAD request; returns HTTP status (0 on connection error)."""
    try:
        req = urllib.request.Request(
            url,
            method="HEAD",
            headers={"User-Agent": "awesome-nginx-probe/1 (+https://github.com/GetPageSpeed/awesome-nginx)"},
        )
        with urllib.request.urlopen(req, timeout=15) as r:
            return r.status
    except urllib.error.HTTPError as e:
        # Some sites (notably github.com on HEAD) sometimes return 4xx for HEAD
        # but 200 on GET. Retry once with GET to avoid false negatives.
        if e.code in (403, 405, 429):
            try:
                req2 = urllib.request.Request(
                    url,
                    method="GET",
                    headers={"User-Agent": "awesome-nginx-probe/1"},
                )
                with urllib.request.urlopen(req2, timeout=15) as r:
                    return r.status
            except urllib.error.HTTPError as e2:
                return e2.code
            except Exception:
                return 0
        return e.code
    except Exception:
        return 0


def audit_links(by_cat: dict, refresh: bool) -> tuple[list, dict]:
    """Probe every emitted URL. Return (bad_entries, updated_cache).

    bad_entries: list of (status, url, label, category) for non-200 or denylisted.
    """
    cache = load_link_cache()
    all_entries = [(cat, e) for cat, entries in by_cat.items() for e in entries]

    # Denylist check first (no network needed)
    bad: list[tuple] = []
    for cat, e in all_entries:
        repo = (e.get("repo") or "").lower()
        if repo and repo in PRIVATE_REPO_DENYLIST:
            bad.append(("DENYLIST", e["url"], e["label"], cat))

    # URLs to probe (skip those already cached fresh unless --refresh)
    urls_to_probe = []
    for cat, e in all_entries:
        url = e["url"]
        if url in cache and not refresh:
            continue
        urls_to_probe.append(url)
    urls_to_probe = sorted(set(urls_to_probe))

    if urls_to_probe:
        print(f"Probing {len(urls_to_probe)} URLs...", file=sys.stderr)
        with ThreadPoolExecutor(max_workers=8) as ex:
            for url, status in zip(urls_to_probe, ex.map(probe_url, urls_to_probe)):
                cache[url] = status

    for cat, e in all_entries:
        url = e["url"]
        status = cache.get(url, 0)
        if status != 200 and status not in (206, 429):
            # Skip duplicates already flagged by denylist
            if any(b[1] == url for b in bad):
                continue
            bad.append((status, url, e["label"], cat))

    return bad, cache


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--check", action="store_true", help="Exit 1 if README would change.")
    parser.add_argument("--no-probe", action="store_true", help="Skip the URL probe (use cache if present, otherwise no check).")
    parser.add_argument("--refresh-probe", action="store_true", help="Re-probe every URL ignoring the cache.")
    parser.add_argument(
        "--extras-dir",
        type=Path,
        default=Path(os.environ.get("NGINX_EXTRAS_DIR", DEFAULT_NGINX_EXTRAS)),
        help="Path to a checkout of GetPageSpeed/nginx-extras.",
    )
    args = parser.parse_args()

    cats = load_categories()
    extras = load_nginx_extras(args.extras_dir)
    discovered = load_discovered(args.extras_dir)

    by_cat = build_entries(cats, extras, discovered)

    # URL audit — fail-fast so we never emit a README with bad/private links.
    if not args.no_probe:
        bad, cache = audit_links(by_cat, refresh=args.refresh_probe)
        save_link_cache(cache)
        if bad:
            print("\nERROR: the following entries link to URLs that are private, dead, or unreachable:", file=sys.stderr)
            for status, url, label, cat in bad:
                print(f"  [{status}] [{cat}] {label}: {url}", file=sys.stderr)
            print("\nFix `categories.yml` (use the public docs page, the canonical upstream, or drop the entry).", file=sys.stderr)
            return 2

    body = render_body(by_cat, cats["categories_order"])
    new_readme = splice_readme(body)

    current = README_PATH.read_text() if README_PATH.is_file() else ""
    if args.check:
        if current != new_readme:
            print("README.md is out of sync with categories.yml — run `python generate.py`.", file=sys.stderr)
            return 1
        return 0

    if current != new_readme:
        README_PATH.write_text(new_readme)
        print(f"Wrote {README_PATH}")
    else:
        print("README.md already up to date.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
