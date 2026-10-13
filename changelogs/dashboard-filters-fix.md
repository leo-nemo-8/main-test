---
title: Dashboard filters fixed
author: Jean-Christophe Camus
date: "2026-09-29"
type: Fixed
hidden: false
---

On `GET /dashboard`:

- the `place` filter now works with the Goodays point of sale identifier as well as with your own code (`external_id`);
- the `place` and `level` filters now also apply to the `pending_chat` counter.

See [Inbox](doc:inbox) for details.
