
# PeeringDB Root Cause Analyses for Release 2.67

---

## 2.67.1 — Production outage (2026-02-25)

**Impact:** PeeringDB pods entered crash loop, causing service degradation for ~20 minutes.

**Timeline:**

- Karpenter initiated node consolidation and forcefully evicted redis-0 (the Redis Sentinel master).
- redis-0's EBS volume hit a multi-attach error — EBS is single-attach, so the volume couldn't mount on the new node while still attached to the old one.
- redis-0 was down for ~13 minutes waiting for the volume to detach and reattach.
- During this window, Sentinel on redis-1/redis-2 could not resolve redis-0's DNS, and failover did not complete cleanly.
- PeeringDB pods lost Redis connectivity, causing `RedisNegativeCacheMiddleware` to generate unhandled exceptions.
- Because `RedisNegativeCacheMiddleware` runs before `PDBSessionMiddleware` in the middleware stack, the session was never initialized on the request.
- Django's `CsrfViewMiddleware` (with `CSRF_USE_SESSIONS=True`) then failed with `ImproperlyConfigured: request.session is not set`.
- This caused `/healthcheck` to return HTTP 500, failing all liveness and readiness probes.
- Kubernetes restarted pods, creating a cascading restart loop.

**Root causes:**

1. **EBS storage for Redis:** Single-attach volumes cause long rescheduling delays during node consolidation.
2. **Middleware ordering:** `RedisNegativeCacheMiddleware` ran before `PDBSessionMiddleware`, so a Redis failure prevented session initialization, which cascaded into CSRF failures on every request including healthchecks.

**Fixes:**

1. **App fix ([PR #1905](https://github.com/peeringdb/peeringdb/pull/1905)):** Reorders middleware so session middleware runs before the Redis-dependent negative cache middleware; adds try/except around Redis cache calls; adds `DJANGO_REDIS_IGNORE_EXCEPTIONS` setting.
2. **Infra fix (planned):** Switch Redis storage from EBS to EFS (multi-attach, no AZ lock) to eliminate volume rescheduling delays.

---

## 2.76.2 — OOM crash loop and rate limiting (2026-02-26)

**Impact:** Pods entered OOM crash loop due to two concurrent issues compounding each other.

**Root causes:**

1. **Bot scan traffic spike:** A surge of bot scans drove memory usage high enough to trigger OOM kills on web pods.
2. **Healthcheck rate limiting:** Healthcheck requests were being counted against the web page rate limiter. Under normal conditions this was invisible, but combined with the OOM-induced pod restarts, pods couldn't pass healthchecks fast enough to stabilize — creating a crash cycle.
3. **OAuth OIDC key permissions:** Separately, after the OIDC signing key was moved to a Kubernetes secret, file permissions were incorrect, breaking OAuth authentication.

**Fixes:**

1. **Rate limiter fix ([PR #1909](https://github.com/peeringdb/peeringdb/pull/1909)):** Exempt healthcheck endpoints from web page rate limiting.
2. **OIDC fix:** Corrected permissions on the OIDC key within the Kubernetes secret mount.

---

## 2.76.3 — Third-party library relink (2026-02-28)

**Impact:** None. Unrelated to the release itself.

**Root cause:** A third-party library dependency needed to be relinked.

**Fix:** Relinked the library. No functional changes.

---

## 2.76.4 — Outbound email failure (2026-03-02)

**Impact:** Email sending was broken following the migration from local postfix relays to external SMTP.

**Root cause:** Sent emails included an erroneous `Return-Path: <>` header that the external SMTP provider rejected or mishandled. This header was a leftover from the local postfix relay configuration where it was either ignored or handled differently.

**Fix:** Removed the erroneous `Return-Path: <>` header from outbound emails.
