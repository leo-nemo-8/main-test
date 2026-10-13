---
title: Reply details and has_reply filter on participations
author: Jean-Christophe Camus
date: "2019-08-30"
type: Added
hidden: false
---

- Participations now include a `reply` object with the reply sent to the end customer: its date, its content, its sender and its type (`text` for a written reply, `call` for a phone call). It is `null` when there is no reply yet.
- The Responses API accepts a new `has_reply` filter: `GET /responses?has_reply=false` lists the participations that have not been replied to yet.

See [Participation retrieval](doc:a-response-at-once) for details.
