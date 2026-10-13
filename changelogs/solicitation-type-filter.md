---
title: Filter solicitations by type
author: Jean-Christophe Camus
date: "2020-02-13"
type: Added
hidden: false
---

`GET /solicitations` now accepts a `type` filter to list only email or SMS solicitations: `GET /solicitations?type=email` or `GET /solicitations?type=sms`.
