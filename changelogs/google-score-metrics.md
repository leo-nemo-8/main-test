---
title: New Google Score metrics endpoint
author: Jean-Christophe Camus
date: "2024-05-22"
type: Added
hidden: false
---

We added `GET /stats/google_score`, to retrieve the Google Business Profile indicators of your points of sale, month by month:

- public rating and number of public reviews (`public_rating`, `public_rating_count`);
- monthly rating and number of reviews (`monthly_rating`, `monthly_rating_count`);
- rating distribution (`rating_distribution`);
- profile views, itinerary requests, phone calls and website clicks (`views_count`, `itinerary_count`, `action_phone_count`, `action_website_count`);
- number of points of sale taken into account (`places_count`).

Results are returned for the current month by default. Use `month` (format `YYYY-MM`) to choose another month, filter with `place`, `places`, `level` or `levels`, and group with `by` or `by_level_category`.

See [Google Score](doc:google-score) for details.
