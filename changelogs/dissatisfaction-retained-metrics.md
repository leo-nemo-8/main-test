---
title: New dissatisfaction and retained customers metrics
author: Jean-Christophe Camus
date: "2021-09-30"
type: Added
hidden: false
---

Two new endpoints join the Metrics API:

- `GET /stats/dissatisfaction`: number of dissatisfaction alerts and how they were handled (`pending`, `call`, `text`, `ignored`, `spam`), with counts and percentages;
- `GET /stats/retained_customers`: number and percentage of retained customers, i.e. dissatisfied customers who, after your reply, said they were satisfied with how their issue was handled and would come back.

See [Dissatisfaction](doc:dissatisfaction) and [Retained customers](doc:retained-customers) for details.
