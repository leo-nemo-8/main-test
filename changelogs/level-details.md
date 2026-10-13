---
title: Level category, status and creation date
author: Jean-Christophe Camus
date: "2019-07-15"
type: Added
hidden: false
---

Levels (your hierarchical or geographical organisation) now expose:

- `category_id` (in `GET /levels` and `GET /levels/{id}`) and `category` (in `GET /levels/{id}`): the category of the level, for example region or business unit. Use `category_id` with the `by_level_category` parameter of the Metrics API;
- `is_active` (in `GET /levels/{id}`): whether the level is active.

Since October 10, 2019, `GET /levels/{id}` also returns `created_date`, the creation date of the level.
