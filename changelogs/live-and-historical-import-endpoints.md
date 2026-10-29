---
title: New endpoint names for live and historical imports
author: Jean-Christophe Camus
date: "2026-10-29"
type: Added
hidden: true
---

Sending participations to Goodays is now clearer, with two explicit endpoints:

- `POST /responses/live` sends a participation as soon as you collect it. It is created right away and processed like any participation collected by Goodays. It is the new name of `POST /responses/collect`.
- `POST /responses/historical` imports your past participations. They are queued, then only feed your statistics. It is the new name of `POST /responses`.

**Nothing changes for existing integrations**: `POST /responses/collect` and `POST /responses` remain available, take the same payload and behave exactly as before. You can switch to the new names whenever it suits you.

We also added a new possibility: a survey can now be set up so that its live participations only feed your statistics and analyses, without entering the Inbox, raising alerts or sending notifications. It is useful for content that nobody should reply to, such as call summaries. Ask your Goodays project contact to set it up.

See [Live or historical import](doc:live-vs-historical-import) and [Analyze the verbatims of your other channels](doc:analyze-verbatims-from-other-channels).
