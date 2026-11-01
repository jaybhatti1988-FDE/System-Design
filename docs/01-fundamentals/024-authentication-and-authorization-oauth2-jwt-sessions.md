# 24. Authentication and authorization (OAuth2, JWT, sessions)?

> Part A: Fundamentals

**Answer:** Sessions: server-side state, easy revocation. JWT: signed stateless token; short expiry + refresh tokens; revocation is hard. OAuth2/OIDC: delegated access via authorization code flow (+PKCE). Authorization via RBAC/ABAC, enforced at gateway and service.

```
User -> IdP login -> auth code -> token -> API (verify signature)
```

---
[⬆ Back to index](../../README.md#-question-index)
