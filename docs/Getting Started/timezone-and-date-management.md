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
