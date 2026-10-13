---
title: Handle participations from your own tools with the Converse API
author: Jean-Christophe Camus
date: "2019-10-29"
type: Added
hidden: false
---

You can now handle end customer participations directly from your Customer Service tool:

- `PUT /responses/{id}/reply`: reply to the end customer;
- `PUT /responses/{id}/message`: send a private message in the conversation;
- `PUT /responses/{id}/call`: mark the participation as handled by a phone call;
- `PUT /responses/{id}/close`: close it without reply;
- `PUT /responses/{id}/spam`: mark it as spam.

The actions available for a participation are listed in its `actions` attribute, and the same management rules as in the Goodays back office apply.

See [Converse API](doc:create-your-interface) for details.
