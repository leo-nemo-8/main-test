---
title: New Customer Effort Score (CES) metric
author: Jean-Christophe Camus
date: "2026-06-11"
type: Added
hidden: false
---

We added a new metrics endpoint, `GET /stats/ces`, for Customer Effort Score questions.

Each aggregated item returns:

- `avg`: the average effort score;
- `high_effort`, `moderate_effort`, `low_effort`: the number and percentage of answers in each effort band.

It supports the same filtering and grouping parameters as the other `stats` endpoints. The `ces` question type (scale from 1 to 7) is now part of the API schema.

See [CES - Customer Effort Score](doc:ces-score) for details.
