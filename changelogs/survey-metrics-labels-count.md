---
title: Answer labels and response count in survey metrics
author: Jean-Christophe Camus
date: "2020-08-03"
type: Added
hidden: false
---

`GET /stats/surveys/{id}` now returns, for each question:

- `count`: the total number of responses to the question;
- in each item of `answers`, a `value` field with the wording of the answer (for example the label of a choice, or "Oui" / "Non" for a Yes/No question), alongside its `count` and `percentage`.

See [Surveys](doc:surveys) for details.
