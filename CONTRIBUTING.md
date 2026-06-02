# Contributing

Thanks for helping curate Awesome NGINX! This list aims for a high quality bar — every entry should be something you'd actually run in production or recommend to a colleague.

## Inclusion criteria

A module, tool, or resource belongs here if it meets **all** of these:

- It is **maintained** — commits within the last 24 months, or the project is feature-complete and still works against current nginx.
- It **builds against current nginx** (mainline or stable) on at least one mainstream Linux distro.
- It is **not malware** — no backdoors, webshells, trojans, RCE PoCs.
- It is **distinctive** — not a near-duplicate of an entry already in the list.
- The author would not be embarrassed for it to be the first entry someone reads in this category.

Discovery-only modules (those surfaced by [`nginx-extras/util/discover.py`](https://github.com/GetPageSpeed/nginx-extras/blob/master/util/discover.py) but not yet packaged) are welcome in the **Honourable mentions** section if they meet the bar above and have a meaningful star count.

## How to add an entry

This list is **generated**. Do not edit the section between `<!-- BEGIN GENERATED -->` and `<!-- END GENERATED -->` in `README.md` by hand — it will be overwritten.

1. Open `categories.yml`.
2. Add a new top-level key `<owner>/<repo>:` under the relevant category.
3. Fill the keys you need:
   - `category:` — one of the H2 sections (see existing entries for the canonical names).
   - `description:` — one-line, ends in a period. If omitted, the generator pulls from the `summary` field in the upstream `nginx-extras` YAML or from `discovered.db.json`.
   - `gps_packaged: true` — adds the 📦 badge. Only set when the module ships under `extras.getpagespeed.com`.
   - `original_by_gps: true` — adds the ⭐ marker. Only for modules / tools authored by GetPageSpeed or @dvershinin (not packaging-side mirror forks).
   - `pin:` — integer; lower pins float to the top of the category. Use sparingly, only when an entry is materially more important than its alphabetic neighbours.
4. Run `python generate.py`. Commit both `categories.yml` and the regenerated `README.md`.
5. Open a PR. CI runs `awesome-lint`, `lychee` link-check, and `python generate.py --check` (fails if the README is out of sync with `categories.yml`).

## Editorial style

- Descriptions are **terse** — one sentence, no marketing language.
- Use plain ASCII hyphens, not em-dashes.
- Every description ends in a period.
- Capitalize proper nouns (NGINX, ModSecurity, Lua) but keep module / package names exactly as they appear upstream (e.g. `ngx_brotli`, not `Ngx Brotli`).

## Removing an entry

If a project is abandoned, broken on current nginx, or has a security issue with no fix in sight, open a PR removing its key from `categories.yml`. Briefly justify in the PR body.
