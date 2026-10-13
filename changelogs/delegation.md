---
title: Delegation to your Customer Service
author: Jean-Christophe Camus
date: "2019-12-12"
type: Added
hidden: false
---

When a local manager does not know how to answer an end customer, they can now delegate the participation to your Customer Service:

- a new `delegated` webhook event is sent when a participation is delegated;
- participations include `delegated_to` (the point of sale the handling was delegated to) and `attached_messages` (the additional messages exchanged on the same conversation, such as private messages).

Webhooks are only sent for the events your subscription lists: contact your Goodays contact to receive `delegated`. See [Converse API](doc:create-your-interface) for details.
