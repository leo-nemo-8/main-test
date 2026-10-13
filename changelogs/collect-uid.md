---
title: Prevent duplicates with collect_uid
author: Jean-Christophe Camus
date: "2023-04-13"
type: Added
hidden: false
---

`POST /responses` now accepts an optional `collect_uid`: your own unique identifier for the participation. If a participation with the same `collect_uid` already exists for your account, the API returns `409 Conflict` instead of creating a duplicate.

See [Become a collection source](doc:become-a-collection-source) for details.
