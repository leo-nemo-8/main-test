---
title: Filter participations by source
author: Jean-Christophe Camus
date: "2024-07-04"
type: Added
hidden: false
---

The Responses API now accepts a `source` filter to retrieve participations collected through a given channel, for example `email`, `widget`, `wifi`, `plv`, `receipt`, `sms`, `terminal`, `sdk`, `facebook` or `google`.

Example: `GET /responses?source=email`

See [Participation retrieval](doc:a-response-at-once) for the full list of values.
