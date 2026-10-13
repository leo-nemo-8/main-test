---
title: Empty results for users without an active point of sale
author: Jean-Christophe Camus
date: "2026-08-03"
type: Improved
hidden: false
---

If the user of your API token has no active point of sale, list endpoints (responses, places, surveys, solicitations, dashboard...) now return an empty result straight away, instead of running the full query.

If you get unexpected empty results, check that the user attached to your token still has at least one active point of sale. Metrics (`stats`) endpoints are not affected.
