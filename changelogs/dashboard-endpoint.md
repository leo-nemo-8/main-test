---
title: New dashboard endpoint
author: Jean-Christophe Camus
date: "2023-02-09"
type: Added
hidden: false
---

We added `GET /dashboard`, which returns the counters of what is waiting for your teams:

- `pending_alert`: dissatisfaction alerts waiting to be handled;
- `pending_reply`: verbatims waiting to be processed.

Results can be filtered by `place`, `level` or `pro_user`.

See [Inbox](doc:inbox) for details.
