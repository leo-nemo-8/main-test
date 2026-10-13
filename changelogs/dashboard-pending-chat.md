---
title: New pending_chat counter on the dashboard endpoint
author: Jean-Christophe Camus
date: "2026-01-21"
type: Added
hidden: false
---

`GET /dashboard` now returns a `pending_chat` counter: the number of active chat conversations waiting for an answer from your teams.

This field is only returned for accounts where the chat feature is enabled.
