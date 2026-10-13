---
title: The email filter now applies to the respondent's email
author: Jean-Christophe Camus
date: "2025-07-28"
type: Improved
hidden: false
---

The `email` filter of the Responses API (`GET /responses?email=...`) now looks for the email of the respondent, returned in `user.email`, instead of the email sent in the participation `context`.

Participations without an identified respondent are therefore no longer returned by this filter, even if their `context` contains the requested email.
