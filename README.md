# Awesome NGINX [![Awesome](https://awesome.re/badge.svg)](https://awesome.re)

> Production-grade NGINX modules, tools, distributions and learning resources, curated by GetPageSpeed.

Every entry is something we run in production, package as an RPM or DEB, or built ourselves. Hobbyware, abandoned forks and proof-of-concept malware are left out by design.

- 📦 marks an entry we package as an RPM and DEB, installable in seconds on RHEL, Alma, Rocky, Amazon Linux, Fedora, Ubuntu, Debian and SLES.
- ⭐ marks an entry authored under the GetPageSpeed or @dvershinin GitHub accounts.

<!-- BEGIN GENERATED -->

## Contents

- [Distributions and forks](#distributions-and-forks)
- [Packaging and distribution](#packaging-and-distribution)
- [Configuration and tooling](#configuration-and-tooling)
- [Security and WAF](#security-and-waf)
- [Authentication](#authentication)
- [Bot mitigation](#bot-mitigation)
- [Caching and compression](#caching-and-compression)
- [Headers, cookies and response filters](#headers-cookies-and-response-filters)
- [Streaming, media and image processing](#streaming-media-and-image-processing)
- [Logging and observability](#logging-and-observability)
- [Lua and OpenResty ecosystem](#lua-and-openresty-ecosystem)
- [Performance and optimization](#performance-and-optimization)
- [Upstreams, rate limiting and access control](#upstreams-rate-limiting-and-access-control)
- [Variables, JSON and extensibility](#variables-json-and-extensibility)
- [Networking and protocols](#networking-and-protocols)
- [Documentation and learning](#documentation-and-learning)
- [Honourable mentions](#honourable-mentions)

## Distributions and forks

- [nginx](https://github.com/nginx/nginx) - Official NGINX source repository, mirrored from the canonical Mercurial.
- [angie](https://github.com/webserver-llc/angie) - Modern NGINX fork by ex-NGINX core engineers, adds ACME, HTTP/3, observability.
- [freenginx](https://github.com/freenginx/freenginx) - Community fork of NGINX maintained by long-time NGINX core developer Maxim Dounin.
- [NGINX Plus](https://www.nginx.com/products/nginx/) - Commercial NGINX with live activity monitoring, dynamic config and JWT/SAML auth, by F5.
- [openresty](https://github.com/openresty/openresty) - Dynamic web platform based on NGINX and LuaJIT, bundling many modules out of the box.
- [tengine](https://github.com/alibaba/tengine) - Alibaba's NGINX fork with dynamic upstream, request-trace and additional optimisations.

## Packaging and distribution

- [extras.getpagespeed.com](https://extras.getpagespeed.com/) - Production-grade RPM and DEB repository with 130+ NGINX modules across all major distributions. ⭐
- [buildstrap](https://github.com/GetPageSpeed/buildstrap) - Bootstraps CircleCI configs for the RPM/DEB build matrix. ⭐
- [debbuilder](https://github.com/GetPageSpeed/debbuilder) - Debian/Ubuntu equivalent of rpmbuilder. ⭐
- [docker-nginx](https://github.com/nginxinc/docker-nginx) - Official NGINX Docker images.
- [getpagespeed-extras-release](https://github.com/GetPageSpeed/getpagespeed-extras-release) - YUM/DNF release RPM that wires up the GetPageSpeed extras repository. ⭐
- [lastversion](https://github.com/dvershinin/lastversion) - Find and download the latest release of any project on GitHub / GitLab / SourceForge / PyPI / Hg / official sites. ⭐
- [nginx-extras](https://github.com/GetPageSpeed/nginx-extras) - Source of every module YAML packaged by extras.getpagespeed.com, submit a YAML, get a build. ⭐
- [nginx-extras-docs](https://github.com/GetPageSpeed/nginx-extras-docs) - Auto-generated documentation site at nginx-extras.getpagespeed.com. ⭐
- [nginx.org Linux packages](https://nginx.org/en/linux_packages.html) - Official NGINX binary packages for Debian, Ubuntu, RHEL/CentOS, Amazon Linux, SLES.
- [rpmbuilder](https://github.com/GetPageSpeed/rpmbuilder) - Containerised RPM build harness, same tool that powers extras.getpagespeed.com. ⭐

## Configuration and tooling

- [gixy](https://github.com/dvershinin/gixy) - Static analyzer that catches alias-traversal, SSRF, host-header attacks and other NGINX config footguns. ⭐
- [crossplane](https://github.com/dvershinin/crossplane) - Convert NGINX configs to and from JSON, fork of the NGINX Amplify tool with fixes. ⭐
- [gixy-jetbrains](https://github.com/GetPageSpeed/gixy-jetbrains) - JetBrains IDE plugin surfacing gixy findings inline. ⭐
- [Mozilla SSL Configuration Generator](https://ssl-config.mozilla.org/) - Mozilla-maintained generator for the TLS / cipher configuration block.
- [nginx-honeypot](https://github.com/dvershinin/nginx-honeypot) - Run an NGINX honeypot to capture and study attacker behaviour. ⭐
- [nginxconfig.io](https://github.com/valentinxxx/nginxconfig.io) - Online NGINX config generator with sensible TLS, performance and security defaults.
- [nginxpwner](https://github.com/dvershinin/nginxpwner) - Look for common NGINX misconfigurations and exploitable patterns. ⭐
- [ngxtop](https://github.com/GetPageSpeed/ngxtop) - Real-time NGINX top, like `top` for your traffic. ⭐
- [off-by-slash](https://github.com/dvershinin/off-by-slash) - Detect alias-traversal misconfigurations (the trailing-slash class of bugs). ⭐

## Security and WAF

- [nginx-acme](https://github.com/nginx/nginx-acme) - Automatic certificate management (ACMEv2) module for NGINX, by F5/NGINX Inc. [📦](https://nginx-extras.getpagespeed.com/modules/acme/)
- [ModSecurity-nginx](https://github.com/SpiderLabs/ModSecurity-nginx) - ModSecurity v3 connector for NGINX. [📦](https://nginx-extras.getpagespeed.com/modules/security/)
- [naxsi](https://github.com/dvershinin/naxsi) - Open-source positive-model WAF for NGINX. [📦](https://nginx-extras.getpagespeed.com/modules/naxsi/) ⭐
- [ngx_security_headers](https://github.com/GetPageSpeed/ngx_security_headers) - Sends modern security headers (CSP, X-Frame-Options, Referrer-Policy) and strips insecure ones. [📦](https://nginx-extras.getpagespeed.com/modules/security-headers/) ⭐
- [ngx_waf](https://github.com/ADD-SP/ngx_waf) - High-performance, ModSecurity-compatible WAF module for NGINX. [📦](https://nginx-extras.getpagespeed.com/modules/waf/)

## Authentication

- [nginx-auth-ldap](https://github.com/dvershinin/nginx-auth-ldap) - LDAP Authentication module for NGINX. [📦](https://nginx-extras.getpagespeed.com/modules/auth-ldap/) ⭐
- [nginx-http-auth-digest](https://github.com/atomx/nginx-http-auth-digest) - Digest Authentication for NGINX. [📦](https://nginx-extras.getpagespeed.com/modules/auth-digest/)
- [nginx-http-auth-totp](https://github.com/61131/nginx-http-auth-totp) - Time-based one-time password (TOTP) HTTP authentication for NGINX. [📦](https://nginx-extras.getpagespeed.com/modules/auth-totp/)
- [nginx-http-shibboleth](https://github.com/nginx-shib/nginx-http-shibboleth) - Shibboleth auth-request module for SAML SSO. [📦](https://nginx-extras.getpagespeed.com/modules/shibboleth/)
- [nginx-jwt-module](https://github.com/max-lt/nginx-jwt-module) - Check for a valid JWT and proxy to upstream (max-lt/nginx-jwt-module). [📦](https://nginx-extras.getpagespeed.com/modules/jwt/)
- [nginx-ntlm-module](https://github.com/dvershinin/nginx-ntlm-module) - NTLM NGINX Module. [📦](https://nginx-extras.getpagespeed.com/modules/ntlm/) ⭐
- [nginx-secure-token-module](https://github.com/kaltura/nginx-secure-token-module) - Generates CDN tokens (cookie or query-string) for signed URL delivery (by Kaltura). [📦](https://nginx-extras.getpagespeed.com/modules/secure-token/)
- [nginx_phantom_token_module](https://github.com/curityio/nginx_phantom_token_module) - Introspects phantom access tokens per RFC 7662 and forwards a JWT to the upstream. [📦](https://nginx-extras.getpagespeed.com/modules/phantom-token/)
- [ngx-http-auth-jwt-module](https://github.com/TeslaGov/ngx-http-auth-jwt-module) - JWT validation module (TeslaGov fork). [📦](https://nginx-extras.getpagespeed.com/modules/teslagov-jwt/)
- [ngx_aws_auth](https://github.com/anomalizer/ngx_aws_auth) - Proxy to authenticated AWS services (S3 and friends). [📦](https://nginx-extras.getpagespeed.com/modules/aws-auth/)
- [ngx_http_auth_hash_module](https://github.com/dvershinin/ngx_http_auth_hash_module) - Secure link hash authentication. [📦](https://nginx-extras.getpagespeed.com/modules/auth-hash/) ⭐
- [ngx_http_auth_pam_module](https://github.com/GetPageSpeed/ngx_http_auth_pam_module) - PAM authentication dynamic module for NGINX. [📦](https://nginx-extras.getpagespeed.com/modules/auth-pam/) ⭐
- [ngx_http_auth_radius_module](https://github.com/dvershinin/ngx_http_auth_radius_module) - HTTP authentication via RADIUS protocol. [📦](https://nginx-extras.getpagespeed.com/modules/auth-radius/) ⭐
- [ngx_http_auth_spnego](https://github.com/GetPageSpeed/ngx_http_auth_spnego) - SPNEGO/Kerberos HTTP authentication. [📦](https://nginx-extras.getpagespeed.com/modules/spnego-http-auth/) ⭐
- [ngx_http_hmac_secure_link_module](https://github.com/nginx-modules/ngx_http_hmac_secure_link_module) - HMAC secure link module with OpenSSL hashes (alternative to the core ngx_http_secure_link). [📦](https://nginx-extras.getpagespeed.com/modules/hmac-secure-link/)
- [pta](https://github.com/iij/pta) - Period-of-Time Authentication, restricts access to a window in time. [📦](https://nginx-extras.getpagespeed.com/modules/pta/)

## Bot mitigation

- [nginx-length-hiding-filter-module](https://github.com/nulab/nginx-length-hiding-filter-module) - Appends a random-length string to HTML responses to defeat BREACH/CRIME-class attacks. [📦](https://nginx-extras.getpagespeed.com/modules/length-hiding/)
- [ngx_bot_verifier](https://github.com/dvershinin/ngx_bot_verifier) - Verifies good-bot identity by reverse-DNS (Googlebot, Bingbot and friends). [📦](https://nginx-extras.getpagespeed.com/modules/bot-verifier/) ⭐
- [ngx_cookie_limit_req_module](https://github.com/dvershinin/ngx_cookie_limit_req_module) - Limits request rate per malicious forged cookie. [📦](https://nginx-extras.getpagespeed.com/modules/cookie-limit/) ⭐
- [ngx_http_captcha_module](https://github.com/RekGRpth/ngx_http_captcha_module) - Native CAPTCHA generation and validation in NGINX. [📦](https://nginx-extras.getpagespeed.com/modules/captcha/)
- [ngx_http_js_challenge_module](https://github.com/dvershinin/ngx_http_js_challenge_module) - Proof-of-work JavaScript challenge for anti-DDoS, similar to Cloudflare's. [📦](https://nginx-extras.getpagespeed.com/modules/js-challenge/) ⭐
- [testcookie-nginx-module](https://github.com/dvershinin/testcookie-nginx-module) - Cookie-based challenge/response for low-effort bot mitigation. [📦](https://nginx-extras.getpagespeed.com/modules/testcookie/) ⭐

## Caching and compression

- [ngx_brotli](https://github.com/GetPageSpeed/ngx_brotli) - Brotli compression module (GetPageSpeed fork of google/ngx_brotli with regular releases). [📦](https://nginx-extras.getpagespeed.com/modules/brotli/) ⭐
- [ngx_cache_purge](https://github.com/GetPageSpeed/ngx_cache_purge) - Purge content from FastCGI, proxy, SCGI and uWSGI caches by URL. [📦](https://nginx-extras.getpagespeed.com/modules/cache-purge/) ⭐
- [ngx_dynamic_etag](https://github.com/dvershinin/ngx_dynamic_etag) - Adds correct ETag headers to dynamic responses, enabling 304s on proxied content. [📦](https://nginx-extras.getpagespeed.com/modules/dynamic-etag/) ⭐
- [ngx_http_compression_normalize_module](https://github.com/dvershinin/ngx_http_compression_normalize_module) - Parses and normalizes the Accept-Encoding header so caches see one canonical form. [📦](https://nginx-extras.getpagespeed.com/modules/compression-normalize/) ⭐
- [ngx_http_compression_vary_filter_module](https://github.com/GetPageSpeed/ngx_http_compression_vary_filter_module) - Enhanced Vary header handling for compression, emits the right Vary without duplicates. [📦](https://nginx-extras.getpagespeed.com/modules/compression-vary/) ⭐
- [ngx_http_sorted_args](https://github.com/GetPageSpeed/ngx_http_sorted_args) - Normalizes query-string parameter order to dramatically improve cache hit rates. [📦](https://nginx-extras.getpagespeed.com/modules/sorted-args/) ⭐
- [ngx_http_unzstd_filter_module](https://github.com/dvershinin/ngx_http_unzstd_filter_module) - Decompresses Zstd-encoded upstream responses for clients that don't support Zstd. [📦](https://nginx-extras.getpagespeed.com/modules/unzstd/) ⭐
- [ngx_immutable](https://github.com/GetPageSpeed/ngx_immutable) - Marks public assets with Cache-Control: immutable so browsers stop revalidating fingerprinted files. [📦](https://nginx-extras.getpagespeed.com/modules/immutable/) ⭐
- [ngx_slowfs_cache](https://github.com/dvershinin/ngx_slowfs_cache) - Caches static files served from slow filesystems. [📦](https://nginx-extras.getpagespeed.com/modules/slowfs/) ⭐
- [ngx_unbrotli](https://github.com/dvershinin/ngx_unbrotli) - Decompresses Brotli-encoded upstream responses for clients that don't support Brotli. [📦](https://nginx-extras.getpagespeed.com/modules/unbrotli/) ⭐
- [srcache-nginx-module](https://github.com/dvershinin/srcache-nginx-module) - Transparent subrequest-based caching for arbitrary NGINX locations. [📦](https://nginx-extras.getpagespeed.com/modules/srcache/) ⭐
- [zstd-nginx-module](https://github.com/tokers/zstd-nginx-module) - Zstandard compression module for NGINX (by tokers). [📦](https://nginx-extras.getpagespeed.com/modules/zstd/)

## Headers, cookies and response filters

- [headers-more-nginx-module](https://github.com/dvershinin/headers-more-nginx-module) - Set, add and clear arbitrary input and output headers, far more capable than ngx_headers. [📦](https://nginx-extras.getpagespeed.com/modules/headers-more/) ⭐
- [nginx-http-concat](https://github.com/dvershinin/nginx-http-concat) - Concatenates CSS and JS files referenced via ?<file>,<file>,..., Alibaba pattern. [📦](https://nginx-extras.getpagespeed.com/modules/concat/) ⭐
- [nginx_accept_language_module](https://github.com/dvershinin/nginx_accept_language_module) - Parses Accept-Language and picks the best supported locale into a variable. [📦](https://nginx-extras.getpagespeed.com/modules/accept-language/) ⭐
- [ngx-fancyindex](https://github.com/dvershinin/ngx-fancyindex) - Fancy autoindex listings (HTML5, sortable, themeable) replacing the bare-bones core directory listing. [📦](https://nginx-extras.getpagespeed.com/modules/fancyindex/) ⭐
- [ngx_http_cookie_flag](https://github.com/GetPageSpeed/ngx_http_cookie_flag) - Sets HttpOnly, Secure and SameSite flags on cookies set by upstream. [📦](https://nginx-extras.getpagespeed.com/modules/cookie-flag/) ⭐
- [ngx_http_device_type_module](https://github.com/GetPageSpeed/ngx_http_device_type_module) - Comprehensive device detection at the NGINX edge, classifies requests by device class. [📦](https://nginx-extras.getpagespeed.com/modules/device-type/) ⭐
- [ngx_http_internal_redirect_module](https://github.com/GetPageSpeed/ngx_http_internal_redirect_module) - Performs an internal redirect to a specified URI without a client round-trip. [📦](https://nginx-extras.getpagespeed.com/modules/internal-redirect/) ⭐
- [ngx_http_loop_detect_module](https://github.com/dvershinin/ngx_http_loop_detect_module) - Honours the CDN-Loop header to break runaway proxy loops. [📦](https://nginx-extras.getpagespeed.com/modules/loop-detect/) ⭐
- [ngx_http_request_cookies_filter_module](https://github.com/dvershinin/ngx_http_request_cookies_filter_module) - Fine-grained control over which cookies reach the upstream. [📦](https://nginx-extras.getpagespeed.com/modules/request-cookies-filter/) ⭐
- [ngx_http_rewrite_status_filter_module](https://github.com/dvershinin/ngx_http_rewrite_status_filter_module) - Rewrite the response status code (turn 502 into 503 and friends). [📦](https://nginx-extras.getpagespeed.com/modules/rewrite-status/) ⭐
- [ngx_http_server_redirect_module](https://github.com/dvershinin/ngx_http_server_redirect_module) - Redirect the server_name within the same request. [📦](https://nginx-extras.getpagespeed.com/modules/server-redirect/) ⭐
- [ngx_http_substitutions_filter_module](https://github.com/dvershinin/ngx_http_substitutions_filter_module) - Regex and fixed-string substitutions in response bodies. [📦](https://nginx-extras.getpagespeed.com/modules/substitutions/) ⭐
- [ngx_http_trim_filter_module](https://github.com/dvershinin/ngx_http_trim_filter_module) - Whitespace and comment trimming filter for HTML, CSS and JS responses. [📦](https://nginx-extras.getpagespeed.com/modules/trim/) ⭐
- [xss-nginx-module](https://github.com/dvershinin/xss-nginx-module) - Native cross-site AJAX (JSONP) support without going through Lua. [📦](https://nginx-extras.getpagespeed.com/modules/xss/) ⭐

## Streaming, media and image processing

- [nginx-rtmp-module](https://github.com/dvershinin/nginx-rtmp-module) - RTMP media streaming server based on the historical nginx-rtmp-module. [📦](https://nginx-extras.getpagespeed.com/modules/rtmp/) ⭐
- [f4fhds](https://github.com/GetPageSpeed/f4fhds) - HTTP Dynamic Streaming (HDS) f4f fragment handler (Adobe legacy). [📦](https://nginx-extras.getpagespeed.com/modules/f4fhds/) ⭐
- [ipscrub](https://github.com/masonicboom/ipscrub) - Anonymizes client IP addresses in access logs (k-anonymity-style). [📦](https://nginx-extras.getpagespeed.com/modules/ipscrub/)
- [media-framework](https://github.com/kaltura/media-framework) - Kaltura Media Framework shared module, HTTP API, events, persistence and Lua interop. [📦](https://nginx-extras.getpagespeed.com/modules/live-common/)
- [mod_zip](https://github.com/dvershinin/mod_zip) - Assembles ZIP archives on the fly from a manifest of upstream URLs. [📦](https://nginx-extras.getpagespeed.com/modules/zip/) ⭐
- [modjpeg-nginx](https://github.com/ioppermann/modjpeg-nginx) - JPEG filter for overlays, logos and watermarks on JPEGs in flight. [📦](https://nginx-extras.getpagespeed.com/modules/jpeg/)
- [nchan](https://github.com/slact/nchan) - Scalable pub/sub server inside NGINX: HTTP, WebSocket, Server-Sent Events and long-polling. [📦](https://nginx-extras.getpagespeed.com/modules/nchan/)
- [nginx-http-flv-module](https://github.com/winshining/nginx-http-flv-module) - HTTP-FLV streaming on top of nginx-rtmp-module. [📦](https://nginx-extras.getpagespeed.com/modules/flv/)
- [nginx-push-stream-module](https://github.com/wandenberg/nginx-push-stream-module) - HTTP push (Comet, EventSource, long-polling, WebSocket) as a pure-NGINX pub/sub stream. [📦](https://nginx-extras.getpagespeed.com/modules/push-stream/)
- [nginx-srt-module](https://github.com/kaltura/nginx-srt-module) - Haivision SRT (Secure Reliable Transport) TCP gateway module. [📦](https://nginx-extras.getpagespeed.com/modules/srt/)
- [nginx-ts-module](https://github.com/arut/nginx-ts-module) - MPEG-TS live streaming module. [📦](https://nginx-extras.getpagespeed.com/modules/ts/)
- [nginx-vod-module](https://github.com/kaltura/nginx-vod-module) - On-the-fly MP4 repackager to DASH, HDS, HLS and MSS (by Kaltura). [📦](https://nginx-extras.getpagespeed.com/modules/vod/)
- [ngx_http_html_sanitize_module](https://github.com/dvershinin/ngx_http_html_sanitize_module) - HTML5 sanitizer based on Google Gumbo, whitelisted elements, attributes and CSS. [📦](https://nginx-extras.getpagespeed.com/modules/html-sanitize/) ⭐
- [ngx_http_untar_module](https://github.com/ajax16384/ngx_http_untar_module) - Serves file content directly out of tar archives. [📦](https://nginx-extras.getpagespeed.com/modules/untar/)
- [ngx_immerse](https://github.com/GetPageSpeed/ngx_immerse) - Modern-image-format filter: transparent WebP and AVIF delivery based on Accept. [📦](https://nginx-extras.getpagespeed.com/modules/immerse/) ⭐
- [ngx_markdown_filter_module](https://github.com/GetPageSpeed/ngx_markdown_filter_module) - Renders Markdown files to HTML on the fly. [📦](https://nginx-extras.getpagespeed.com/modules/markdown/) ⭐
- [ngx_small_light](https://github.com/dvershinin/ngx_small_light) - Dynamic image transformation (resize, crop, rotate, watermark). [📦](https://nginx-extras.getpagespeed.com/modules/small-light/) ⭐
- [ngx_webp](https://github.com/dvershinin/ngx_webp) - On-the-fly WebP conversion of JPEG and PNG responses. [📦](https://nginx-extras.getpagespeed.com/modules/webp/) ⭐

## Logging and observability

- [nginx-module-vts](https://github.com/vozlt/nginx-module-vts) - Virtual-host traffic status module, Prometheus / JSON / HTML real-time stats. [📦](https://nginx-extras.getpagespeed.com/modules/vts/)
- [graphite-nginx-module](https://github.com/mailru/graphite-nginx-module) - Send per-location stats directly to Graphite. [📦](https://nginx-extras.getpagespeed.com/modules/graphite/)
- [nginx-log-zmq](https://github.com/dvershinin/nginx-log-zmq) - Stream access logs over ZeroMQ for centralized collection. [📦](https://nginx-extras.getpagespeed.com/modules/log-zmq/) ⭐
- [nginx-module-stream-sts](https://github.com/vozlt/nginx-module-stream-sts) - Stream server traffic status core module (companion to sts). [📦](https://nginx-extras.getpagespeed.com/modules/stream-sts/)
- [nginx-module-sts](https://github.com/vozlt/nginx-module-sts) - Stream server traffic status, same idea as VTS but for the stream {} block. [📦](https://nginx-extras.getpagespeed.com/modules/sts/)
- [nginx-otel](https://github.com/nginxinc/nginx-otel) - Official OpenTelemetry tracing exporter module for NGINX. [📦](https://nginx-extras.getpagespeed.com/modules/otel/)
- [nginx-statsd](https://github.com/dvershinin/nginx-statsd) - Send NGINX metrics to a StatsD collector. [📦](https://nginx-extras.getpagespeed.com/modules/statsd/) ⭐
- [ngx-sqlite-log](https://github.com/GetPageSpeed/ngx-sqlite-log) - SQLite-backed access log, queryable logs without a separate pipeline. [📦](https://nginx-extras.getpagespeed.com/modules/log-sqlite/) ⭐
- [ngx_http_error_log_write_module](https://github.com/dvershinin/ngx_http_error_log_write_module) - Conditionally emit error-log entries from configuration. [📦](https://nginx-extras.getpagespeed.com/modules/error-log-write/) ⭐
- [ngx_http_log_var_set_module](https://github.com/dvershinin/ngx_http_log_var_set_module) - Set NGINX variables right before the access log writes, late-stage log enrichment. [📦](https://nginx-extras.getpagespeed.com/modules/log-var-set/) ⭐
- [ngx_http_pipelog_module](https://github.com/pandax381/ngx_http_pipelog_module) - Pipe access logs to an external program (analytics, alerting, archival). [📦](https://nginx-extras.getpagespeed.com/modules/pipelog/)
- [ngx_http_upstream_log_module](https://github.com/dvershinin/ngx_http_upstream_log_module) - Writes upstream-side request logs separate from the client-side access log. [📦](https://nginx-extras.getpagespeed.com/modules/upstream-log/) ⭐
- [traffic-accounting-nginx-module](https://github.com/dvershinin/traffic-accounting-nginx-module) - Real-time incoming/outgoing traffic counters per zone. [📦](https://nginx-extras.getpagespeed.com/modules/traffic-accounting/) ⭐

## Lua and OpenResty ecosystem

- [lua-nginx-module](https://github.com/openresty/lua-nginx-module) - Embed the power of LuaJIT into NGINX's HTTP request lifecycle. [📦](https://nginx-extras.getpagespeed.com/modules/lua/)
- [array-var-nginx-module](https://github.com/openresty/array-var-nginx-module) - Array-typed variables for the OpenResty stack. [📦](https://nginx-extras.getpagespeed.com/modules/array-var/)
- [echo-nginx-module](https://github.com/openresty/echo-nginx-module) - echo, sleep, time and exec directives for the content phase. [📦](https://nginx-extras.getpagespeed.com/modules/echo/)
- [encrypted-session-nginx-module](https://github.com/openresty/encrypted-session-nginx-module) - Encrypt and decrypt NGINX variable values, for sessionless session cookies. [📦](https://nginx-extras.getpagespeed.com/modules/encrypted-session/)
- [lua-upstream-nginx-module](https://github.com/openresty/lua-upstream-nginx-module) - Lua API for controlling NGINX upstreams at runtime. [📦](https://nginx-extras.getpagespeed.com/modules/lua-upstream/)
- [memc-nginx-module](https://github.com/openresty/memc-nginx-module) - Extended memcached upstream module (full memcached command set, not just GET). [📦](https://nginx-extras.getpagespeed.com/modules/memc/)
- [nginx-eval-module](https://github.com/openresty/nginx-eval-module) - Evaluate memcached or proxy response into a variable. [📦](https://nginx-extras.getpagespeed.com/modules/eval/)
- [ngx_devel_kit](https://github.com/vision5/ngx_devel_kit) - Nginx Devel Kit, generic toolkit that many third-party modules depend on. [📦](https://nginx-extras.getpagespeed.com/modules/ndk/)
- [ngx_wasm_module](https://github.com/GetPageSpeed/ngx_wasm_module) - Proxy-Wasm (WebAssembly) support for NGINX, powered by wasmtime. [📦](https://nginx-extras.getpagespeed.com/modules/wasm-wasmtime/) ⭐
- [njs](https://github.com/nginx/njs) - Official JavaScript scripting in NGINX (subset of ES5 + extensions). [📦](https://nginx-extras.getpagespeed.com/modules/njs/)
- [redis2-nginx-module](https://github.com/openresty/redis2-nginx-module) - Native upstream for the Redis 2.0+ protocol, full pipelining. [📦](https://nginx-extras.getpagespeed.com/modules/redis2/)
- [set-misc-nginx-module](https://github.com/openresty/set-misc-nginx-module) - set_xxx directives, md5, sha1, base64, hex, escape, quote, for the rewrite phase. [📦](https://nginx-extras.getpagespeed.com/modules/set-misc/)
- [stream-lua-nginx-module](https://github.com/GetPageSpeed/stream-lua-nginx-module) - Embed LuaJIT into NGINX's stream {} (TCP/UDP) processing. [📦](https://nginx-extras.getpagespeed.com/modules/stream-lua/) ⭐

## Performance and optimization

- [incubator-pagespeed-ngx](https://github.com/apache/incubator-pagespeed-ngx) - Apache mod_pagespeed for NGINX, automatic CSS/JS/image optimization at the edge. [📦](https://nginx-extras.getpagespeed.com/modules/pagespeed/)
- [nginx-link-function](https://github.com/Taymindis/nginx-link-function) - Dlopen application code straight into NGINX request handling for ultra-low-latency endpoints. [📦](https://nginx-extras.getpagespeed.com/modules/link/)
- [nginx-sxg-module](https://github.com/google/nginx-sxg-module) - Signed HTTP Exchange (SXG) support, prefetch with original-origin attribution. [📦](https://nginx-extras.getpagespeed.com/modules/sxg/)
- [ngx_http_tuning](https://github.com/GetPageSpeed/ngx_http_tuning) - Observes real traffic patterns and proposes data-driven NGINX tuning. [📦](https://nginx-extras.getpagespeed.com/modules/tuning/) ⭐
- [passenger](https://github.com/phusion/passenger) - Phusion Passenger application server module, runs Ruby/Python/Node apps inside NGINX. [📦](https://nginx-extras.getpagespeed.com/modules/passenger/)

## Upstreams, rate limiting and access control

- [nginx-combined-upstreams-module](https://github.com/lyokha/nginx-combined-upstreams-module) - add_upstream / combine_server_singlets directives for upstream composition. [📦](https://nginx-extras.getpagespeed.com/modules/combined-upstreams/)
- [nginx-module-sysguard](https://github.com/dvershinin/nginx-module-sysguard) - Sheds load when system CPU, memory or RT exceeds thresholds. [📦](https://nginx-extras.getpagespeed.com/modules/sysguard/) ⭐
- [nginx-sticky-module-ng](https://github.com/dvershinin/nginx-sticky-module-ng) - Sticky-cookie session affinity load balancer. [📦](https://nginx-extras.getpagespeed.com/modules/sticky/) ⭐
- [nginx-stream-upsync-module](https://github.com/xiaokai-wang/nginx-stream-upsync-module) - Sync stream {} upstreams from Consul or etcd. [📦](https://nginx-extras.getpagespeed.com/modules/stream-upsync/)
- [nginx-upload-module](https://github.com/fdintino/nginx-upload-module) - Streams multipart/form-data uploads straight to disk before passing metadata upstream. [📦](https://nginx-extras.getpagespeed.com/modules/upload/)
- [nginx-upload-progress-module](https://github.com/masterzen/nginx-upload-progress-module) - Real-time upload progress tracking for browser UIs. [📦](https://nginx-extras.getpagespeed.com/modules/upload-progress/)
- [nginx-upstream-fair](https://github.com/itoffshore/nginx-upstream-fair) - Fair load-balancer based on number of in-flight requests per backend. [📦](https://nginx-extras.getpagespeed.com/modules/upstream-fair/)
- [nginx-upsync-module](https://github.com/weibocom/nginx-upsync-module) - Sync HTTP upstreams from Consul or etcd without reloading NGINX. [📦](https://nginx-extras.getpagespeed.com/modules/upsync/)
- [ngx_dynamic_limit_req_module](https://github.com/limithit/ngx_dynamic_limit_req_module) - Dynamically locks an IP after threshold and releases it after a configurable window. [📦](https://nginx-extras.getpagespeed.com/modules/dynamic-limit-req/)
- [ngx_http_access_control_module](https://github.com/dvershinin/ngx_http_access_control_module) - Advanced access control by NGINX variables (beyond allow / deny by IP). [📦](https://nginx-extras.getpagespeed.com/modules/access-control/) ⭐
- [ngx_http_delay_module](https://github.com/dvershinin/ngx_http_delay_module) - Insert a configurable delay before responding, useful for shaping or tarpitting. [📦](https://nginx-extras.getpagespeed.com/modules/delay/) ⭐
- [ngx_http_limit_traffic_ratefilter_module](https://github.com/dvershinin/ngx_http_limit_traffic_ratefilter_module) - Rate-limit traffic by arbitrary NGINX variables (e.g. per token, per geo). [📦](https://nginx-extras.getpagespeed.com/modules/limit-traffic-rate/) ⭐
- [ngx_ipset_access_module](https://github.com/GetPageSpeed/ngx_ipset_access_module) - Zero-latency IP allow/deny using Linux kernel ipsets. [📦](https://nginx-extras.getpagespeed.com/modules/ipset-access/) ⭐
- [ngx_nftset_access_module](https://github.com/GetPageSpeed/ngx_nftset_access_module) - Zero-latency IP allow/deny using Linux kernel nftables sets. [📦](https://nginx-extras.getpagespeed.com/modules/nftset-access/) ⭐
- [ngx_upstream_jdomain](https://github.com/nicholaschiasson/ngx_upstream_jdomain) - Async DNS resolution for upstream backends, survives DNS-only backends. [📦](https://nginx-extras.getpagespeed.com/modules/upstream-jdomain/)
- [rate-limit-nginx-module](https://github.com/weserv/rate-limit-nginx-module) - Redis-backed cluster-wide rate limiting. [📦](https://nginx-extras.getpagespeed.com/modules/redis-rate-limit/)

## Variables, JSON and extensibility

- [form-input-nginx-module](https://github.com/calio/form-input-nginx-module) - Parses application/x-www-form-urlencoded request bodies into variables. [📦](https://nginx-extras.getpagespeed.com/modules/form-input/)
- [iconv-nginx-module](https://github.com/calio/iconv-nginx-module) - Character-set conversion of request and response bodies via libiconv. [📦](https://nginx-extras.getpagespeed.com/modules/iconv/)
- [nginx-json-var-module](https://github.com/dvershinin/nginx-json-var-module) - Group variable expressions as a JSON value for clean logging. [📦](https://nginx-extras.getpagespeed.com/modules/json-var/) ⭐
- [nginx-keyval](https://github.com/kjdev/nginx-keyval) - Key-value store backed module, variables sourced from disk-backed KV pairs. [📦](https://nginx-extras.getpagespeed.com/modules/keyval/)
- [nginx-let-module](https://github.com/dvershinin/nginx-let-module) - Arithmetic and string expressions in the rewrite phase. [📦](https://nginx-extras.getpagespeed.com/modules/let/) ⭐
- [ngx_http_json_module](https://github.com/dvershinin/ngx_http_json_module) - Dumps a $json variable into a string. [📦](https://nginx-extras.getpagespeed.com/modules/json/) ⭐
- [ngx_http_label_module](https://github.com/dvershinin/ngx_http_label_module) - Define global key-value labels for dynamic configuration. [📦](https://nginx-extras.getpagespeed.com/modules/label/) ⭐
- [ngx_http_var_module](https://github.com/dvershinin/ngx_http_var_module) - Dynamically assign variables via predefined functions (math, string, hash). [📦](https://nginx-extras.getpagespeed.com/modules/var/) ⭐
- [ngx_postgres](https://github.com/dvershinin/ngx_postgres) - Direct PostgreSQL upstream, no PHP / app layer needed for read-heavy paths. [📦](https://nginx-extras.getpagespeed.com/modules/postgres/) ⭐

## Networking and protocols

- [nginx-cgi](https://github.com/pjincz/nginx-cgi) - Run classic CGI scripts under NGINX. [📦](https://nginx-extras.getpagespeed.com/modules/cgi/)
- [nginx-dav-ext-module](https://github.com/arut/nginx-dav-ext-module) - Adds PROPFIND, OPTIONS, LOCK and UNLOCK to NGINX's core WebDAV. [📦](https://nginx-extras.getpagespeed.com/modules/dav-ext/)
- [Nginx-DOH-Module](https://github.com/dvershinin/Nginx-DOH-Module) - Serve DNS-over-HTTPS responses straight from NGINX. [📦](https://nginx-extras.getpagespeed.com/modules/doh/) ⭐
- [nginx_ajp_module](https://github.com/dvershinin/nginx_ajp_module) - Apache AJP13 protocol upstream (talk to Tomcat / JBoss natively). [📦](https://nginx-extras.getpagespeed.com/modules/ajp/) ⭐
- [ngx_coolkit](https://github.com/dvershinin/ngx_coolkit) - Collection of small NGINX utilities, encoding, time helpers, IP utilities. [📦](https://nginx-extras.getpagespeed.com/modules/coolkit/) ⭐
- [ngx_http_geoip2_module](https://github.com/leev/ngx_http_geoip2_module) - MaxMind GeoIP2 lookups into NGINX variables. [📦](https://nginx-extras.getpagespeed.com/modules/geoip2/)
- [ngx_http_proxy_connect_module](https://github.com/dvershinin/ngx_http_proxy_connect_module) - Adds HTTP CONNECT (forward-proxy) support to NGINX. [📦](https://nginx-extras.getpagespeed.com/modules/proxy-connect/) ⭐
- [ngx_http_rdns](https://github.com/GetPageSpeed/ngx_http_rdns) - Reverse-DNS lookup of the client IP into NGINX variables. [📦](https://nginx-extras.getpagespeed.com/modules/rdns/) ⭐

## Documentation and learning

- [nginx-extras.getpagespeed.com](https://nginx-extras.getpagespeed.com/) - Reference docs for every packaged NGINX module: installation, directives, examples. ⭐
- [awesome-nginx](https://github.com/agile6v/awesome-nginx) - Long-running broad awesome-list of NGINX projects.
- [awesome-nginx-security](https://github.com/wallarm/awesome-nginx-security) - Awesome list scoped to NGINX security: talks, WAFs, configuration analyzers.
- [GetPageSpeed blog](https://www.getpagespeed.com/) - Deep dives on NGINX tuning, modules and packaging from the engineering team behind this list. ⭐
- [h5bp/server-configs-nginx](https://github.com/h5bp/server-configs-nginx) - Boilerplate server configs (cache headers, MIME types, security headers) from HTML5 Boilerplate.
- [nginx-admins-handbook](https://github.com/trimstray/nginx-admins-handbook) - Exhaustive admin handbook covering performance, security, hardening and debugging.
- [nginx-resources](https://github.com/fcambus/nginx-resources) - Curated collection of NGINX articles, books and tutorials.
- [nginx-tuning](https://github.com/denji/nginx-tuning) - Tuning cheat-sheet for high-traffic NGINX deployments.
- [nginx101.com](https://nginx101.com/) - Practical NGINX articles for the long tail of operator questions. ⭐
- [Official NGINX documentation](https://nginx.org/en/docs/) - The authoritative directive and module reference.

## Honourable mentions

- [nginx-ct](https://github.com/grahamedgecombe/nginx-ct) - Certificate Transparency support, embeds SCTs into TLS handshakes (175★).
- [nginx-gridfs](https://github.com/mdirolf/nginx-gridfs) - Serve files directly from MongoDB GridFS (792★).
- [nginx-haskell-module](https://github.com/lyokha/nginx-haskell-module) - Embed Haskell handlers, asynchronous tasks and services into NGINX (161★).
- [nginx-http-user-agent](https://github.com/alibaba/nginx-http-user-agent) - Match browsers and crawlers by User-Agent, Alibaba's pattern (162★).
- [nginx-python-module](https://github.com/arut/nginx-python-module) - Embed Python into NGINX request handling (139★).
- [nginx-ssl-fingerprint](https://github.com/phuslu/nginx-ssl-fingerprint) - High-performance JA3 and HTTP/2 fingerprinting (198★).
- [nginx-ssl-ja3](https://github.com/fooinha/nginx-ssl-ja3) - TLS JA3 fingerprinting for bot and abuse detection (216★).
- [nginx-video-thumbextractor-module](https://github.com/wandenberg/nginx-video-thumbextractor-module) - Extract thumbnails from video files on the fly (208★).
- [nginx_upstream_module](https://github.com/tarantool/nginx_upstream_module) - Native Tarantool upstream (REST, JSON, WebSockets, load balancing) (173★).
- [ngx-php](https://github.com/rryqszq4/ngx-php) - Embedded PHP 7/8 scripting inside an NGINX module (693★).
- [ngx_dynamic_upstream](https://github.com/cubicdaiya/ngx_dynamic_upstream) - Add, remove and modify upstream servers without reloading NGINX (515★).
- [ngx_healthcheck_module](https://github.com/zhouchangxun/ngx_healthcheck_module) - Active healthchecks for upstream servers in both http and stream contexts (282★).
- [ngx_http_consul_backend_module](https://github.com/hashicorp/ngx_http_consul_backend_module) - Set upstream backends directly from a Consul service catalog (155★).
- [ngx_kafka_module](https://github.com/brg-liuwei/ngx_kafka_module) - Posts request bodies to a Kafka cluster, handy for log fan-out (176★).
- [ngx_wasm_module](https://github.com/Kong/ngx_wasm_module) - Kong's NGINX plus WebAssembly runtime (126★).
- [socks-nginx-module](https://github.com/dannote/socks-nginx-module) - Adds SOCKS5 support to ngx_http_proxy_module (201★).
- [wasm-nginx-module](https://github.com/api7/wasm-nginx-module) - Run WebAssembly modules inside OpenResty / NGINX (alternative to wasmtime) (200★).

<!-- END GENERATED -->

## Contributing

Contributions welcome. See the [contribution guidelines](CONTRIBUTING.md).
