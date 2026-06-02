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
- [freenginx](https://freenginx.org/) - Community fork of NGINX maintained by long-time NGINX core developer Maxim Dounin.
- [NGINX Plus](https://www.nginx.com/products/nginx/) - Commercial NGINX with live activity monitoring, dynamic config and JWT/SAML auth, by F5.
- [openresty](https://github.com/openresty/openresty) - Dynamic web platform based on NGINX and LuaJIT, bundling many modules out of the box.
- [tengine](https://github.com/alibaba/tengine) - Alibaba's NGINX fork with dynamic upstream, request-trace and additional optimisations.

## Packaging and distribution

- [extras.getpagespeed.com](https://extras.getpagespeed.com/) - Production-grade RPM and DEB repository with 130+ NGINX modules across all major distributions. ⭐
- [docker-nginx](https://github.com/nginxinc/docker-nginx) - Official NGINX Docker images.
- [lastversion](https://github.com/dvershinin/lastversion) - Find and download the latest release of any project on GitHub / GitLab / SourceForge / PyPI / Hg / official sites. ⭐
- [nginx.org Linux packages](https://nginx.org/en/linux_packages.html) - Official NGINX binary packages for Debian, Ubuntu, RHEL/CentOS, Amazon Linux, SLES.

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

- [nginx-acme](https://github.com/nginx/nginx-acme) - Automatic certificate management (ACMEv2) module for NGINX, by F5/NGINX Inc. 📦
- [ModSecurity-nginx](https://github.com/SpiderLabs/ModSecurity-nginx) - ModSecurity v3 connector for NGINX. 📦
- [naxsi](https://github.com/dvershinin/naxsi) - Open-source positive-model WAF for NGINX. 📦 ⭐
- [ngx_security_headers](https://github.com/GetPageSpeed/ngx_security_headers) - Sends modern security headers (CSP, X-Frame-Options, Referrer-Policy) and strips insecure ones. 📦 ⭐
- [ngx_waf](https://github.com/ADD-SP/ngx_waf) - High-performance, ModSecurity-compatible WAF module for NGINX. 📦

## Authentication

- [auth-pam](https://nginx-extras.getpagespeed.com/modules/auth-pam/) - PAM authentication dynamic module for NGINX. 📦 ⭐
- [nginx-auth-ldap](https://github.com/dvershinin/nginx-auth-ldap) - LDAP Authentication module for NGINX. 📦 ⭐
- [nginx-http-auth-digest](https://github.com/atomx/nginx-http-auth-digest) - Digest Authentication for NGINX. 📦
- [nginx-http-auth-totp](https://github.com/61131/nginx-http-auth-totp) - Time-based one-time password (TOTP) HTTP authentication for NGINX. 📦
- [nginx-http-shibboleth](https://github.com/nginx-shib/nginx-http-shibboleth) - Shibboleth auth-request module for SAML SSO. 📦
- [nginx-jwt-module](https://github.com/max-lt/nginx-jwt-module) - Check for a valid JWT and proxy to upstream (max-lt/nginx-jwt-module). 📦
- [nginx-ntlm-module](https://github.com/dvershinin/nginx-ntlm-module) - NTLM NGINX Module. 📦 ⭐
- [nginx-secure-token-module](https://github.com/kaltura/nginx-secure-token-module) - Generates CDN tokens (cookie or query-string) for signed URL delivery (by Kaltura). 📦
- [nginx_phantom_token_module](https://github.com/curityio/nginx_phantom_token_module) - Introspects phantom access tokens per RFC 7662 and forwards a JWT to the upstream. 📦
- [ngx-http-auth-jwt-module](https://github.com/TeslaGov/ngx-http-auth-jwt-module) - JWT validation module (TeslaGov fork). 📦
- [ngx_aws_auth](https://github.com/anomalizer/ngx_aws_auth) - Proxy to authenticated AWS services (S3 and friends). 📦
- [ngx_http_auth_hash_module](https://github.com/dvershinin/ngx_http_auth_hash_module) - Secure link hash authentication. 📦 ⭐
- [ngx_http_auth_radius_module](https://github.com/dvershinin/ngx_http_auth_radius_module) - HTTP authentication via RADIUS protocol. 📦 ⭐
- [ngx_http_hmac_secure_link_module](https://github.com/nginx-modules/ngx_http_hmac_secure_link_module) - HMAC secure link module with OpenSSL hashes (alternative to the core ngx_http_secure_link). 📦
- [pta](https://github.com/iij/pta) - Period-of-Time Authentication, restricts access to a window in time. 📦
- [spnego-http-auth](https://nginx-extras.getpagespeed.com/modules/spnego-http-auth/) - SPNEGO/Kerberos HTTP authentication. 📦 ⭐

## Bot mitigation

- [nginx-length-hiding-filter-module](https://github.com/nulab/nginx-length-hiding-filter-module) - Appends a random-length string to HTML responses to defeat BREACH/CRIME-class attacks. 📦
- [ngx_bot_verifier](https://github.com/repsheet/ngx_bot_verifier) - Verifies good-bot identity by reverse-DNS (Googlebot, Bingbot and friends). 📦 ⭐
- [ngx_cookie_limit_req_module](https://github.com/dvershinin/ngx_cookie_limit_req_module) - Limits request rate per malicious forged cookie. 📦 ⭐
- [ngx_http_captcha_module](https://github.com/RekGRpth/ngx_http_captcha_module) - Native CAPTCHA generation and validation in NGINX. 📦
- [ngx_http_js_challenge_module](https://github.com/dvershinin/ngx_http_js_challenge_module) - Proof-of-work JavaScript challenge for anti-DDoS, similar to Cloudflare's. 📦 ⭐
- [testcookie-nginx-module](https://github.com/dvershinin/testcookie-nginx-module) - Cookie-based challenge/response for low-effort bot mitigation. 📦 ⭐

## Caching and compression

- [cache-purge](https://nginx-extras.getpagespeed.com/modules/cache-purge/) - Purge content from FastCGI, proxy, SCGI and uWSGI caches by URL. 📦 ⭐
- [ngx_brotli](https://github.com/GetPageSpeed/ngx_brotli) - Brotli compression module (GetPageSpeed fork of google/ngx_brotli with regular releases). 📦 ⭐
- [compression-vary](https://nginx-extras.getpagespeed.com/modules/compression-vary/) - Enhanced Vary header handling for compression, emits the right Vary without duplicates. 📦 ⭐
- [immutable](https://nginx-extras.getpagespeed.com/modules/immutable/) - Marks public assets with Cache-Control: immutable so browsers stop revalidating fingerprinted files. 📦 ⭐
- [ngx_dynamic_etag](https://github.com/dvershinin/ngx_dynamic_etag) - Adds correct ETag headers to dynamic responses, enabling 304s on proxied content. 📦 ⭐
- [ngx_http_compression_normalize_module](https://github.com/dvershinin/ngx_http_compression_normalize_module) - Parses and normalizes the Accept-Encoding header so caches see one canonical form. 📦 ⭐
- [ngx_http_unzstd_filter_module](https://github.com/dvershinin/ngx_http_unzstd_filter_module) - Decompresses Zstd-encoded upstream responses for clients that don't support Zstd. 📦 ⭐
- [ngx_slowfs_cache](https://github.com/dvershinin/ngx_slowfs_cache) - Caches static files served from slow filesystems. 📦 ⭐
- [ngx_unbrotli](https://github.com/dvershinin/ngx_unbrotli) - Decompresses Brotli-encoded upstream responses for clients that don't support Brotli. 📦 ⭐
- [sorted-args](https://nginx-extras.getpagespeed.com/modules/sorted-args/) - Normalizes query-string parameter order to dramatically improve cache hit rates. 📦 ⭐
- [srcache-nginx-module](https://github.com/dvershinin/srcache-nginx-module) - Transparent subrequest-based caching for arbitrary NGINX locations. 📦 ⭐
- [zstd-nginx-module](https://github.com/tokers/zstd-nginx-module) - Zstandard compression module for NGINX (by tokers). 📦

## Headers, cookies and response filters

- [headers-more-nginx-module](https://github.com/dvershinin/headers-more-nginx-module) - Set, add and clear arbitrary input and output headers, far more capable than ngx_headers. 📦 ⭐
- [cookie-flag](https://nginx-extras.getpagespeed.com/modules/cookie-flag/) - Sets HttpOnly, Secure and SameSite flags on cookies set by upstream. 📦 ⭐
- [device-type](https://nginx-extras.getpagespeed.com/modules/device-type/) - Comprehensive device detection at the NGINX edge, classifies requests by device class. 📦 ⭐
- [internal-redirect](https://nginx-extras.getpagespeed.com/modules/internal-redirect/) - Performs an internal redirect to a specified URI without a client round-trip. 📦 ⭐
- [nginx-http-concat](https://github.com/dvershinin/nginx-http-concat) - Concatenates CSS and JS files referenced via ?<file>,<file>,..., Alibaba pattern. 📦 ⭐
- [nginx_accept_language_module](https://github.com/dvershinin/nginx_accept_language_module) - Parses Accept-Language and picks the best supported locale into a variable. 📦 ⭐
- [ngx-fancyindex](https://github.com/dvershinin/ngx-fancyindex) - Fancy autoindex listings (HTML5, sortable, themeable) replacing the bare-bones core directory listing. 📦 ⭐
- [ngx_http_loop_detect_module](https://github.com/dvershinin/ngx_http_loop_detect_module) - Honours the CDN-Loop header to break runaway proxy loops. 📦 ⭐
- [ngx_http_request_cookies_filter_module](https://github.com/dvershinin/ngx_http_request_cookies_filter_module) - Fine-grained control over which cookies reach the upstream. 📦 ⭐
- [ngx_http_rewrite_status_filter_module](https://github.com/dvershinin/ngx_http_rewrite_status_filter_module) - Rewrite the response status code (turn 502 into 503 and friends). 📦 ⭐
- [ngx_http_server_redirect_module](https://github.com/dvershinin/ngx_http_server_redirect_module) - Redirect the server_name within the same request. 📦 ⭐
- [ngx_http_substitutions_filter_module](https://github.com/dvershinin/ngx_http_substitutions_filter_module) - Regex and fixed-string substitutions in response bodies. 📦 ⭐
- [ngx_http_trim_filter_module](https://github.com/dvershinin/ngx_http_trim_filter_module) - Whitespace and comment trimming filter for HTML, CSS and JS responses. 📦 ⭐
- [xss-nginx-module](https://github.com/dvershinin/xss-nginx-module) - Native cross-site AJAX (JSONP) support without going through Lua. 📦 ⭐

## Streaming, media and image processing

- [nginx-rtmp-module](https://github.com/dvershinin/nginx-rtmp-module) - RTMP media streaming server based on the historical nginx-rtmp-module. 📦 ⭐
- [f4fhds](https://github.com/GetPageSpeed/f4fhds) - HTTP Dynamic Streaming (HDS) f4f fragment handler (Adobe legacy). 📦 ⭐
- [immerse](https://nginx-extras.getpagespeed.com/modules/immerse/) - Modern-image-format filter: transparent WebP and AVIF delivery based on Accept. 📦 ⭐
- [ipscrub](https://github.com/masonicboom/ipscrub) - Anonymizes client IP addresses in access logs (k-anonymity-style). 📦
- [markdown](https://nginx-extras.getpagespeed.com/modules/markdown/) - Renders Markdown files to HTML on the fly. 📦 ⭐
- [media-framework](https://github.com/kaltura/media-framework) - Kaltura Media Framework shared module, HTTP API, events, persistence and Lua interop. 📦
- [mod_zip](https://github.com/dvershinin/mod_zip) - Assembles ZIP archives on the fly from a manifest of upstream URLs. 📦 ⭐
- [modjpeg-nginx](https://github.com/ioppermann/modjpeg-nginx) - JPEG filter for overlays, logos and watermarks on JPEGs in flight. 📦
- [nchan](https://github.com/slact/nchan) - Scalable pub/sub server inside NGINX: HTTP, WebSocket, Server-Sent Events and long-polling. 📦
- [nginx-http-flv-module](https://github.com/winshining/nginx-http-flv-module) - HTTP-FLV streaming on top of nginx-rtmp-module. 📦
- [nginx-push-stream-module](https://github.com/wandenberg/nginx-push-stream-module) - HTTP push (Comet, EventSource, long-polling, WebSocket) as a pure-NGINX pub/sub stream. 📦
- [nginx-srt-module](https://github.com/kaltura/nginx-srt-module) - Haivision SRT (Secure Reliable Transport) TCP gateway module. 📦
- [nginx-ts-module](https://github.com/arut/nginx-ts-module) - MPEG-TS live streaming module. 📦
- [nginx-vod-module](https://github.com/kaltura/nginx-vod-module) - On-the-fly MP4 repackager to DASH, HDS, HLS and MSS (by Kaltura). 📦
- [ngx_http_html_sanitize_module](https://github.com/dvershinin/ngx_http_html_sanitize_module) - HTML5 sanitizer based on Google Gumbo, whitelisted elements, attributes and CSS. 📦 ⭐
- [ngx_http_untar_module](https://github.com/ajax16384/ngx_http_untar_module) - Serves file content directly out of tar archives. 📦
- [ngx_small_light](https://github.com/dvershinin/ngx_small_light) - Dynamic image transformation (resize, crop, rotate, watermark). 📦 ⭐
- [ngx_webp](https://github.com/dvershinin/ngx_webp) - On-the-fly WebP conversion of JPEG and PNG responses. 📦 ⭐

## Logging and observability

- [nginx-module-vts](https://github.com/vozlt/nginx-module-vts) - Virtual-host traffic status module, Prometheus / JSON / HTML real-time stats. 📦
- [graphite-nginx-module](https://github.com/mailru/graphite-nginx-module) - Send per-location stats directly to Graphite. 📦
- [log-zmq](https://nginx-extras.getpagespeed.com/modules/log-zmq/) - Stream access logs over ZeroMQ for centralized collection. 📦 ⭐
- [nginx-module-stream-sts](https://github.com/vozlt/nginx-module-stream-sts) - Stream server traffic status core module (companion to sts). 📦
- [nginx-module-sts](https://github.com/vozlt/nginx-module-sts) - Stream server traffic status, same idea as VTS but for the stream {} block. 📦
- [nginx-otel](https://github.com/nginxinc/nginx-otel) - Official OpenTelemetry tracing exporter module for NGINX. 📦
- [nginx-statsd](https://github.com/dvershinin/nginx-statsd) - Send NGINX metrics to a StatsD collector. 📦 ⭐
- [ngx-sqlite-log](https://github.com/GetPageSpeed/ngx-sqlite-log) - SQLite-backed access log, queryable logs without a separate pipeline. 📦 ⭐
- [ngx_http_error_log_write_module](https://github.com/dvershinin/ngx_http_error_log_write_module) - Conditionally emit error-log entries from configuration. 📦 ⭐
- [ngx_http_log_var_set_module](https://github.com/dvershinin/ngx_http_log_var_set_module) - Set NGINX variables right before the access log writes, late-stage log enrichment. 📦 ⭐
- [ngx_http_pipelog_module](https://github.com/pandax381/ngx_http_pipelog_module) - Pipe access logs to an external program (analytics, alerting, archival). 📦
- [ngx_http_upstream_log_module](https://github.com/dvershinin/ngx_http_upstream_log_module) - Writes upstream-side request logs separate from the client-side access log. 📦 ⭐
- [traffic-accounting-nginx-module](https://github.com/dvershinin/traffic-accounting-nginx-module) - Real-time incoming/outgoing traffic counters per zone. 📦 ⭐

## Lua and OpenResty ecosystem

- [lua-nginx-module](https://github.com/openresty/lua-nginx-module) - Embed the power of LuaJIT into NGINX's HTTP request lifecycle. 📦
- [array-var-nginx-module](https://github.com/openresty/array-var-nginx-module) - Array-typed variables for the OpenResty stack. 📦
- [echo-nginx-module](https://github.com/openresty/echo-nginx-module) - Echo, sleep, time and exec directives for the content phase. 📦
- [encrypted-session-nginx-module](https://github.com/openresty/encrypted-session-nginx-module) - Encrypt and decrypt NGINX variable values, for sessionless session cookies. 📦
- [lua-upstream-nginx-module](https://github.com/openresty/lua-upstream-nginx-module) - Lua API for controlling NGINX upstreams at runtime. 📦
- [memc-nginx-module](https://github.com/openresty/memc-nginx-module) - Extended memcached upstream module (full memcached command set, not just GET). 📦
- [nginx-eval-module](https://github.com/openresty/nginx-eval-module) - Evaluate memcached or proxy response into a variable. 📦
- [ngx_devel_kit](https://github.com/vision5/ngx_devel_kit) - Nginx Devel Kit, generic toolkit that many third-party modules depend on. 📦
- [ngx_wasm_module](https://github.com/GetPageSpeed/ngx_wasm_module) - Proxy-Wasm (WebAssembly) support for NGINX, powered by wasmtime. 📦 ⭐
- [njs](https://github.com/nginx/njs) - Official JavaScript scripting in NGINX (subset of ES5 + extensions). 📦
- [redis2-nginx-module](https://github.com/openresty/redis2-nginx-module) - Native upstream for the Redis 2.0+ protocol, full pipelining. 📦
- [set-misc-nginx-module](https://github.com/openresty/set-misc-nginx-module) - Provides set_xxx directives (md5, sha1, base64, hex, escape, quote) for the rewrite phase. 📦
- [stream-lua-nginx-module](https://github.com/GetPageSpeed/stream-lua-nginx-module) - Embed LuaJIT into NGINX's stream {} (TCP/UDP) processing. 📦 ⭐

## Performance and optimization

- [incubator-pagespeed-ngx](https://github.com/apache/incubator-pagespeed-ngx) - Apache mod_pagespeed for NGINX, automatic CSS/JS/image optimization at the edge. 📦
- [nginx-link-function](https://github.com/Taymindis/nginx-link-function) - Dlopen application code straight into NGINX request handling for ultra-low-latency endpoints. 📦
- [nginx-sxg-module](https://github.com/google/nginx-sxg-module) - Signed HTTP Exchange (SXG) support, prefetch with original-origin attribution. 📦
- [passenger](https://github.com/phusion/passenger) - Phusion Passenger application server module, runs Ruby/Python/Node apps inside NGINX. 📦
- [tuning](https://nginx-extras.getpagespeed.com/modules/tuning/) - Observes real traffic patterns and proposes data-driven NGINX tuning. 📦 ⭐

## Upstreams, rate limiting and access control

- [ipset-access](https://nginx-extras.getpagespeed.com/modules/ipset-access/) - Zero-latency IP allow/deny using Linux kernel ipsets. 📦 ⭐
- [nftset-access](https://nginx-extras.getpagespeed.com/modules/nftset-access/) - Zero-latency IP allow/deny using Linux kernel nftables sets. 📦 ⭐
- [nginx-combined-upstreams-module](https://github.com/lyokha/nginx-combined-upstreams-module) - Adds add_upstream and combine_server_singlets directives for upstream composition. 📦
- [nginx-module-sysguard](https://github.com/dvershinin/nginx-module-sysguard) - Sheds load when system CPU, memory or RT exceeds thresholds. 📦 ⭐
- [nginx-sticky-module-ng](https://github.com/dvershinin/nginx-sticky-module-ng) - Sticky-cookie session affinity load balancer. 📦 ⭐
- [nginx-stream-upsync-module](https://github.com/xiaokai-wang/nginx-stream-upsync-module) - Sync stream {} upstreams from Consul or etcd. 📦
- [nginx-upload-module](https://github.com/fdintino/nginx-upload-module) - Streams multipart/form-data uploads straight to disk before passing metadata upstream. 📦
- [nginx-upload-progress-module](https://github.com/masterzen/nginx-upload-progress-module) - Real-time upload progress tracking for browser UIs. 📦
- [nginx-upstream-fair](https://github.com/itoffshore/nginx-upstream-fair) - Fair load-balancer based on number of in-flight requests per backend. 📦
- [nginx-upsync-module](https://github.com/weibocom/nginx-upsync-module) - Sync HTTP upstreams from Consul or etcd without reloading NGINX. 📦
- [ngx_dynamic_limit_req_module](https://github.com/limithit/ngx_dynamic_limit_req_module) - Dynamically locks an IP after threshold and releases it after a configurable window. 📦
- [ngx_http_access_control_module](https://github.com/dvershinin/ngx_http_access_control_module) - Advanced access control by NGINX variables (beyond allow / deny by IP). 📦 ⭐
- [ngx_http_delay_module](https://github.com/dvershinin/ngx_http_delay_module) - Insert a configurable delay before responding, useful for shaping or tarpitting. 📦 ⭐
- [ngx_http_limit_traffic_ratefilter_module](https://github.com/dvershinin/ngx_http_limit_traffic_ratefilter_module) - Rate-limit traffic by arbitrary NGINX variables (e.g. per token, per geo). 📦 ⭐
- [ngx_upstream_jdomain](https://github.com/nicholaschiasson/ngx_upstream_jdomain) - Async DNS resolution for upstream backends, survives DNS-only backends. 📦
- [rate-limit-nginx-module](https://github.com/weserv/rate-limit-nginx-module) - Redis-backed cluster-wide rate limiting. 📦

## Variables, JSON and extensibility

- [form-input-nginx-module](https://github.com/calio/form-input-nginx-module) - Parses application/x-www-form-urlencoded request bodies into variables. 📦
- [iconv-nginx-module](https://github.com/calio/iconv-nginx-module) - Character-set conversion of request and response bodies via libiconv. 📦
- [nginx-json-var-module](https://github.com/dvershinin/nginx-json-var-module) - Group variable expressions as a JSON value for clean logging. 📦 ⭐
- [nginx-keyval](https://github.com/kjdev/nginx-keyval) - Key-value store backed module, variables sourced from disk-backed KV pairs. 📦
- [nginx-let-module](https://github.com/dvershinin/nginx-let-module) - Arithmetic and string expressions in the rewrite phase. 📦 ⭐
- [ngx_http_json_module](https://github.com/dvershinin/ngx_http_json_module) - Dumps a $json variable into a string. 📦 ⭐
- [ngx_http_label_module](https://github.com/dvershinin/ngx_http_label_module) - Define global key-value labels for dynamic configuration. 📦 ⭐
- [ngx_http_var_module](https://github.com/dvershinin/ngx_http_var_module) - Dynamically assign variables via predefined functions (math, string, hash). 📦 ⭐
- [ngx_postgres](https://github.com/dvershinin/ngx_postgres) - Direct PostgreSQL upstream, no PHP / app layer needed for read-heavy paths. 📦 ⭐

## Networking and protocols

- [nginx-cgi](https://github.com/pjincz/nginx-cgi) - Run classic CGI scripts under NGINX. 📦
- [nginx-dav-ext-module](https://github.com/arut/nginx-dav-ext-module) - Adds PROPFIND, OPTIONS, LOCK and UNLOCK to NGINX's core WebDAV. 📦
- [Nginx-DOH-Module](https://github.com/dvershinin/Nginx-DOH-Module) - Serve DNS-over-HTTPS responses straight from NGINX. 📦 ⭐
- [nginx_ajp_module](https://github.com/dvershinin/nginx_ajp_module) - Apache AJP13 protocol upstream (talk to Tomcat / JBoss natively). 📦 ⭐
- [ngx_coolkit](https://github.com/dvershinin/ngx_coolkit) - Collection of small NGINX utilities, encoding, time helpers, IP utilities. 📦 ⭐
- [ngx_http_geoip2_module](https://github.com/leev/ngx_http_geoip2_module) - MaxMind GeoIP2 lookups into NGINX variables. 📦
- [ngx_http_proxy_connect_module](https://github.com/dvershinin/ngx_http_proxy_connect_module) - Adds HTTP CONNECT (forward-proxy) support to NGINX. 📦 ⭐
- [rdns](https://nginx-extras.getpagespeed.com/modules/rdns/) - Reverse-DNS lookup of the client IP into NGINX variables. 📦 ⭐

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
