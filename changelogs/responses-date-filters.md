---
title: Filter participations by date
author: Jean-Christophe Camus
date: "2021-01-20"
type: Added
hidden: false
---

The Responses API now accepts `start_date` and `end_date` to retrieve the participations of a given period (`start_date` included, `end_date` excluded).

By default the period applies to `created_date`. Add `date_field=updated_date` to apply it to the last update date instead, and retrieve every participation modified over the period, not only those created.

See [Participation retrieval](doc:a-response-at-once#choose-the-date-to-filter) for details.
