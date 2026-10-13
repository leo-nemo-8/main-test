---
title: Yes/No questions supported when collecting responses
author: Jean-Christophe Camus
date: "2024-12-19"
type: Added
hidden: false
---

`POST /responses` now accepts answers to Yes/No questions. Send `0` for no and `1` for yes; any other value returns a validation error.
