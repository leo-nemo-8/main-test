---
title: The response webhook is sent once the participation is fully processed
author: Jean-Christophe Camus
date: "2026-09-11"
type: Improved
hidden: false
---

The `response` webhook event is now sent as soon as Goodays has fully processed the participation (alerts, conversation, available actions), instead of after a fixed delay.

Its payload always reflects the final state of the participation, for example `alert_triggered` and `actions`.
