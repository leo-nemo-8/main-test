---
title: Last login date on users
author: Jean-Christophe Camus
date: "2019-11-13"
type: Added
hidden: false
---

`GET /users` and `GET /users/{id}` now return `last_login`: the date and time of the user's last login to Goodays (`null` if the user never logged in). You can use it, for example, to follow the adoption of Goodays by your teams.
