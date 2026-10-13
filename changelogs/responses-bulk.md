---
title: Retrieve participations in bulk with GET /responses/bulk
author: Jean-Christophe Camus
date: "2020-01-20"
type: Added
hidden: false
---

We added `GET /responses/bulk`, which returns participations with all their details (answers, verbatim, end customer, context, conversation...) in a single paginated call, instead of one call per participation.

It accepts the same filters as `GET /responses`, and is also available on `/places/{id}/responses/bulk`, `/levels/{id}/responses/bulk` and `/surveys/{id}/responses/bulk`.

See [Participation retrieval](doc:a-response-at-once) for details.
