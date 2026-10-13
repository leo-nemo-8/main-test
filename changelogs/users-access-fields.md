---
title: New access fields on users
author: Jean-Christophe Camus
date: "2024-08-21"
type: Added
hidden: false
---

`GET /users` and `GET /users/{id}` now return the job and the access rights of each user:

- `function`: the user's job;
- `interface_moderation`: access to the moderation of the reviews published on your store displays;
- `interface_sollicitation`: access to the solicitation interface;
- `export_recherche`: access to the search export;
- `export_satisfaction`, `export_verbatim`, `export_transaction`: access to the satisfaction, verbatim and transaction exports.
