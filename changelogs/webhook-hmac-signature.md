---
title: Signed webhooks (HMAC-SHA256)
author: Jean-Christophe Camus
date: "2020-10-08"
type: Added
hidden: false
---

Webhooks can now be signed, so you can make sure that the requests you receive come from Goodays.

When a secret key is configured on your subscription, each webhook request includes an `X-HMAC-SHA256` header containing `hex(HMAC-SHA256(secret_key, raw_request_body))`. Compute the same signature on your side and compare it with the header. Without a secret key, the header is not sent.

To set up a secret key, contact your Goodays technical contact. See [Securing your webhook](doc:create-your-interface#securing-your-webhook) for details.
