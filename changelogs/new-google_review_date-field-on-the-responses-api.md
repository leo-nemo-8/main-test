---
title: New google_review_date field on the Responses API
author: Jean-Christophe Camus
date: "2026-09-10"
type: Added
hidden: false
---

We added an optional `google_review_date` field to participations returned by the Responses API (list and detail).

- For participations coming from Google My Business, it contains the date the review was last modified on Google, as returned by Google. For a review that was never edited, this is the date it was posted.
- For any other source, it is `null`.

This is an additive change: no existing field was removed or modified, and no change is required on the way you call the API. As a general good practice for REST/JSON integrations, make sure your client ignores attributes it does not know about.

See [Participation retrieval](doc:a-response-at-once) for details.
