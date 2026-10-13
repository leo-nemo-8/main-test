---
title: Use your own point of sale code as place identifier
author: Jean-Christophe Camus
date: "2022-06-23"
type: Added
hidden: false
---

You can now identify a point of sale with your own code (`external_id`) instead of the Goodays identifier in:

- the `place` field of `POST /responses` and `POST /solicitations`;
- the `place` filter of `GET /responses`, `GET /solicitations` and `GET /dashboard`;
- the `/places/{place}/responses` routes.

The Goodays identifier still works everywhere. The `stats` endpoints only accept the Goodays identifier.
