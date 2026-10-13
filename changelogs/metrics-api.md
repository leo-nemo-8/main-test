---
title: New Metrics API
author: Jean-Christophe Camus
date: "2020-01-29"
type: Added
hidden: false
---

The new Metrics API lets you retrieve the statistics calculated by Goodays, with the same filters as in the back office:

- `GET /stats/nps`: Net Promoter Score;
- `GET /stats/satisfaction`: customer satisfaction score;
- `GET /stats/relationship`: customer relationship score (reply rate, reply time, reply quality);
- `GET /stats/remarks`: distribution of remarks by type;
- `GET /stats/surveys/{id}`: results of a survey, question by question.

Results can be filtered by period, point of sale, level or survey, and grouped by day, month, point of sale and more.

See [Exploit the full potential of your data!](doc:exploit-the-full-potential-of-your-data) for details.
