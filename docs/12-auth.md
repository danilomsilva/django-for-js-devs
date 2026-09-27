# Chapter 12 — Auth

## TL;DR

- Django ships two auth mechanisms out of the box: session auth (cookie-based, what the admin uses) and token auth (header-based, what a React SPA typically uses).
- DRF returns **403**, not 401, when no credentials are presented and no scheme issued a challenge — a common surprise coming from JWT-based setups.
- This chapter covers DRF's built-in `TokenAuthentication`; JWT (a more common real-world choice for SPAs) is mentioned as the "also" option and is a good next step once this clicks.

## The mental model

Ok, we can now validate and shape data (chapter 11) — but so far, every endpoint has been open to anyone. Real APIs need to know who's asking. Let's look at how a request carries identity through Django, and how that identity reaches your view.

```mermaid
flowchart LR
    Req[Request with Authorization header] --> AuthClass["Authentication class\n(Session or Token)"]
    AuthClass -->|valid| SetUser[request.user is set]
    AuthClass -->|invalid/missing| Anon[request.user is AnonymousUser]
    SetUser --> View[Your view]
    Anon --> View
```

Authentication only answers "who is this?" — it doesn't decide whether they're *allowed* to do something. That's permissions, covered next in chapter 13. `whoami` in this chapter only requires *being* someone; it doesn't check *what* that someone can do.

## If you know JS: Passport.js / Auth.js

| Passport.js / Auth.js | Django / DRF |
|---|---|
| A "strategy" (local, JWT, OAuth...) | An "authentication class" (`SessionAuthentication`, `TokenAuthentication`, or a JWT package) |
| `req.user` after a strategy succeeds | `request.user` after a DRF authentication class succeeds |
| Session cookie (`express-session`) | Django's built-in session framework — same idea, already wired in |
| A JWT you issue and the client sends in `Authorization: Bearer <token>` | DRF's opaque token (`Authorization: Token <token>`) works similarly; JWT packages exist too (see "go deeper") |
| Multiple strategies can be tried in order | Multiple `DEFAULT_AUTHENTICATION_CLASSES` are tried in order — first one that succeeds wins |

The biggest conceptual overlap: both systems separate "verify who this is" (authentication) from "wire that identity onto the request object" — `req.user` and `request.user` play the same role.

## The Django way

[`examples/config/settings.py`](../examples/config/settings.py) enables two authentication classes:

```python
REST_FRAMEWORK = {
    "DEFAULT_AUTHENTICATION_CLASSES": [
        "rest_framework.authentication.SessionAuthentication",
        "rest_framework.authentication.TokenAuthentication",
    ],
}
```

**Session auth** is what the Django admin already uses (chapter 8) — log in via a form, get a session cookie, every subsequent request is tied to that session. Good for a same-site setup; not ideal for a decoupled React SPA on a different origin.

**Token auth** is the one you'll actually use from a React app talking to a separately-hosted API. `rest_framework.authtoken` (added to `INSTALLED_APPS`) gives every user an opaque token they send as a header:

```
Authorization: Token 9944b09199c62bcf9418ad846dd0e4bbdfc6ee4
```

Get a token by posting credentials to the endpoint DRF provides:

```python
# examples/greetings/urls.py
path("auth/token/", obtain_auth_token, name="obtain-token"),
```

```bash
curl -X POST http://127.0.0.1:8000/api/auth/token/ \
  -d "username=alice&password=s3cret"
# {"token": "9944b09199c62bcf9418ad846dd0e4bbdfc6ee4"}
```

From React (or any client), that token then goes on every request:

```js
fetch("/api/whoami/", {
  headers: { Authorization: `Token ${token}` },
});
```

**A protected endpoint** — [`examples/greetings/views.py`](../examples/greetings/views.py)'s `whoami`:

```python
@api_view(["GET"])
@permission_classes([IsAuthenticated])
def whoami(request):
    return Response({"username": request.user.username})
```

[`examples/greetings/tests.py`](../examples/greetings/tests.py) covers all three states: no credentials (`test_whoami_requires_authentication`, expects 403), a valid token (`test_whoami_with_token`), and obtaining a token in the first place (`test_obtain_token_endpoint`).

## Gotchas for JS devs

- **403, not 401, for missing credentials** — DRF returns 401 only when an authentication scheme issues a "challenge" (like `WWW-Authenticate`); `SessionAuthentication` doesn't, so with no valid credentials at all, you get 403 "Forbidden" rather than the 401 "Unauthorized" you might expect coming from a typical JWT setup. `test_whoami_requires_authentication` in `examples/` asserts exactly this.
- DRF's built-in token never expires and isn't a JWT — it's an opaque, permanent string until you delete/rotate it. Fine for learning and small internal tools; most production SPA setups reach for JWT (via `djangorestframework-simplejwt`, not covered in `examples/` yet) or `django-allauth`/similar for anything user-facing at scale.
- CSRF only applies to session-authenticated, cookie-based requests — token-authenticated requests are exempt, since the token itself (not a cookie) proves identity. If you switch a React app from token to session-cookie auth, you'll need to start handling CSRF tokens on writes.

## Check yourself

1. Why does `test_whoami_requires_authentication` expect a 403, not a 401?

   <details><summary>Answer</summary>DRF returns 401 only when an authentication class issues an actual challenge header. <code>SessionAuthentication</code> doesn't, so with no credentials at all, DRF falls back to 403.</details>

2. What's the practical difference between session auth and token auth for a React SPA hosted on a different origin than the API?

   <details><summary>Answer</summary>Session auth relies on a cookie, which is awkward across origins (cross-site cookie rules, CSRF handling). Token auth sends an explicit <code>Authorization</code> header per request, which works cleanly across origins without cookie complications.</details>

## Go deeper (when you need it)

- [DRF docs — authentication](https://www.django-rest-framework.org/api-guide/authentication/)
- [djangorestframework-simplejwt](https://django-rest-framework-simplejwt.readthedocs.io/) (JWT auth, a common production choice not covered in `examples/` yet)
- [Passport.js](https://www.passportjs.org/)

## Further reading & credits

- [DRF docs — authentication](https://www.django-rest-framework.org/api-guide/authentication/) — Encode OSS, BSD-3-Clause.
- [Passport.js docs](https://www.passportjs.org/) — MIT.
