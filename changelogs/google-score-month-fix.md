---
title: Google Score month filter fixed
author: Jean-Christophe Camus
date: "2026-03-24"
type: Fixed
hidden: false
---

On `GET /stats/google_score`, the `month` parameter now covers the whole requested month, from its first to its last day (up to today for the current month).

See [Google Score](doc:google-score) for details.
