---
title: New google_review_date field on the Responses API
author: Jean-Christophe Camus
date: "2026-09-10"
type: Added
hidden: false
---

We added an optional `google_review_date` field to participations returned by the Responses API (list and detail).

- For participations coming from Google My Business, it contains the date of the review on Google, as reported by Google (its last update date).
- For any other source, it is `null`.

This is an additive change: no existing field was removed or modified, and no change is required on the way you call the API. As a general good practice for REST/JSON integrations, make sure your client ignores attributes it does not know about.
