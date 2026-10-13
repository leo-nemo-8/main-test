---
title: Solicitation status on the Solicitations API
author: Jean-Christophe Camus
date: "2025-04-17"
type: Added
hidden: false
---

`GET /solicitations/{id}` now returns a `status` field: the latest delivery status of the solicitation (for example `queued`, `sent`, `delivered`, `opened`, `clicked`, `failed`). It is `unknown` when no status is available yet.

See [Solicitation statuses](doc:solicitation-nation#solicitation-statuses) for the meaning of each status.
