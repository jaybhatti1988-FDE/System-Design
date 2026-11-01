# 24. Authentication and authorization (OAuth2, JWT, sessions)?

> Part A: Fundamentals

**Answer:** Sessions: server-side state, easy revocation. JWT: signed stateless token; short expiry + refresh tokens; revocation is hard. OAuth2/OIDC: delegated access via authorization code flow (+PKCE). Authorization via RBAC/ABAC, enforced at gateway and service.

```mermaid
flowchart LR
    n0["User"]
    n1["IdP login"]
    n2["Auth code"]
    n3["Access token"]
    n4["API verifies signature"]
    n0 --> n1
    n1 --> n2
    n2 --> n3
    n3 --> n4
```

---
[⬆ Back to index](../../README.md#-question-index)
