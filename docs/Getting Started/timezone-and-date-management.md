---
title: Timezone And Date Management
excerpt: ''
deprecated: false
hidden: false
metadata:
  title: ''
  description: ''
  robots: noindex
next:
  description: ''
---
An important zoom on the date format: Goodays uses the [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) standard for its date formats.

> 📘 Date and time in UTC
>
> We accept the following format for our `start_date` and `end_date` attribute :
>
> * 2021-11-16T15:40:09+00:00
> * 2021-11-16T15:40:09Z
> * 20211116T154009Z

This means that it is recommended to specify the timezone used in the date formats that you push to us:

* For a UTC+0 format you can add `Z`or `-00:00` to your date
* For a different UTC format you can add, for example, `-02:00` or `+02:00` depending on the timezone you want to use

```curl
curl --location --request GET 'https://api.goodays.co/v2/responses/bulk? \
	start_date=2019-07-09T00:00:00Z \
  &end_date=2019-07-10T00:00:00Z' \
--header 'Content-Type: application/json' \
--header 'Authorization: {access-token}'
```

Or for a `+02:00` timezone

```curl
curl --location --request GET 'https://api.goodays.co/v2/responses/bulk? \
	start_date=2019-07-09T00%3A00%3A00%2B02%3A00 \
  &end_date=2019-07-10T00%3A00%3A00%2B02%3A00' \
--header 'Content-Type: application/json' \
--header 'Authorization: {access-token}'
```

> 📘 Url encode
>
> We recommend to Url encode the value of each date. Especially if you use the `+` character.

# Metrics API: how dates and timezones are applied

> 📘 Which date is used?
>
> Metrics (`/stats/nps`, `/stats/ces`, `/stats/satisfaction`, `/stats/remarks`, `/stats/surveys`, `/stats/dissatisfaction`) are always attached to the **date the end customer submitted the participation**, never to the date it was processed by a pro user.

## Timezone used for `by=day`, `month`, `quarter`, `year`

When you aggregate by a time period, days (and months, quarters, years) are cut using the timezone of your `begin` parameter:

* If `begin` contains a timezone (e.g. `2026-09-01T00:00:00+02:00` or `2026-09-01T00:00:00Z`), this timezone is used.
* If `begin` is not provided, or has no timezone, **Europe/Paris** is used, the same as in the Goodays back office.

For example, with the default timezone, a participation received on September 5th at 11:30 pm (Paris time) is counted in the September 5th bucket.

> 🚧 Fixed offsets and daylight saving time
>
> A fixed offset such as `+02:00` does not follow daylight saving time changes. After the switch to winter time, your daily buckets will be shifted by one hour compared to the back office. To get the same figures as the back office, omit the timezone or use Europe/Paris times.

# Metrics API: data freshness and recalculation

Statistics are **not frozen day by day**: they are recalculated on each call, based on the current state of the participations.

* When a participation is processed later (e.g. `pending` on September 5th, answered on September 6th), it **stays attached to September 5th** and only its status changes (`pending` → `text`, `call`, `ignored` or `spam`). The statistics of September 5th evolve; the action does not appear in September 6th.
* There is **no date after which a day's statistics become final**: they can change as long as the participations of that day evolve (processing, reply, requalification…).
* A modification is usually reflected in the API **between 15 minutes and one hour**, depending on the type of participation.

> 👍 Best practice for BI integrations
>
> If you store Goodays statistics incrementally, re-import a rolling period (for example the last 30 to 60 days) on a regular basis rather than considering a past day as final.
