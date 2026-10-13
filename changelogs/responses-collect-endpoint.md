---
title: New POST /responses/collect endpoint
author: Jean-Christophe Camus
date: "2020-09-18"
type: Added
hidden: false
---

We added `POST /responses/collect` to push the participations you collect through your own channels (kiosk, app, call center...) in real time.

It takes the same payload as `POST /responses`, but the participation is processed like any participation collected by Goodays: it appears in the Inbox and can trigger alerts. `POST /responses` remains dedicated to importing historical data, which only feeds your statistics.

See [Become a collection source](doc:become-a-collection-source) for details.
