---
title: Anonymisation option for participations
author: Jean-Christophe Camus
date: "2026-03-17"
type: Added
hidden: false
---

An anonymisation option is now available on API tokens. When it is enabled on your token, participations returned by `GET /responses/{id}` and `GET /responses/bulk` are anonymised:

- the respondent's `email`, `first_name` and `last_name` are returned as `null`;
- `email`, `phone`, `first_name` and `last_name` are returned as `null` in `context`;
- `crm_id` and the other context fields are kept, so you can still reconcile participations with your own systems.

Since April 2026, the option also applies to external reviews (Google, etc.). Since July 2026, the names and emails of the people who took part in the conversation, including your own users, are also returned as `null` on anonymised participations.

The option is enabled per token. Contact your Goodays contact to activate it.
