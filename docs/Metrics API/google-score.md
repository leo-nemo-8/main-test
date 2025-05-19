---
title: Google Score
excerpt: ''
deprecated: false
hidden: false
metadata:
  title: ''
  description: ''
  robots: index
next:
  description: ''
---
> 📘 What's that
> 
> The **Google Score** is a rating assigned by Google to local establishment on Google My Business (GMB), based on end customer reviews and ratings. This score reflects end customer satisfaction and can influence the business’s online visibility and reputation.

> 👍 Going further
> 
> Consult the general [Metrics API documentation](/docs/exploit-the-full-potential-of-your-data) for more.

[block:image]
{
  "images": [
    {
      "image": [
        "https://files.readme.io/7b3725c-Connect-4.png",
        "",
        ""
      ],
      "align": "center",
      "sizing": "500px"
    }
  ]
}
[/block]


# How do I get my Google Score?

With [/stats/google_score](ref:stats_google_score_list):

```json Google Score call
curl --location --request GET 'https://api.goodays.co/v2/stats/google_score' \
--header 'Content-Type: application/json' \
--header 'Authorization: 1234abcd1234abcd1234abcd1234abcd'
```

> 📘 By default, Google Score and other data are returned for the current month.

```json Sample Google Score
{
    "data": [
        {
            "key": null,
            "description": null,
            "public_rating": 4.06,
            "public_rating_count": 177135,
            "places_count": 70,
            "monthly_rating": 4.23,
            "monthly_rating_count": 2510,
            "action_phone_count": 23916,
            "action_website_count": 34752,
            "itinerary_count": 17254,
            "views_count": 394184,
            "rating_distribution": [
                {
                    "value": 1,
                    "count": 166
                },
                {
                    "value": 2,
                    "count": 118
                },
                {
                    "value": 3,
                    "count": 192
                },
                {
                    "value": 4,
                    "count": 542
                },
                {
                    "value": 5,
                    "count": 1492
                }
            ]
        }
    ]
}
```

And the return will always contain:

[block:parameters]
{
  "data": {
    "h-0": "Attribute",
    "h-1": "Description",
    "0-0": "**key**",
    "0-1": "Distribution key ID.",
    "1-0": "**description**",
    "1-1": "Description of the distribution key.",
    "2-0": "**public_rating**",
    "2-1": "Google Public Score at the time of the requested month.  \n_(current month by default)_  \n  \n:information_source: This is the score displayed by Google on the establishment's page (on the day of the query if the month is current or on the last day of the month requested).  \n  \n:bulb: If `places_count` is greater than 1, then this is the average Google Score for all the establishments in the query scope.",
    "3-0": "**public_rating_count**",
    "3-1": "Number of participations at the time of the requested month.  \n_(current month by default)_  \n  \n:information_source: This is the total number of reviews displayed on the establishment page (on the day of the request if the month is current or on the last day of the month requested).",
    "4-0": "**places_count**",
    "4-1": "Number of establishment(s) taken into account when calculating the Google Public Score.  \n_(all by default)_",
    "5-0": "**monthly_rating**",
    "5-1": "Monthly Google Score for the requested month.  \n_(current month by default)_  \n  \n:information_source: This is the average of Google ratings collected between the first and last day of the month requested.",
    "6-0": "**monthly_rating_count**",
    "6-1": "Number of participations collected between the first and last day over the requested month.  \n_(current month by default)_",
    "7-0": "**action_phone_count**",
    "7-1": "Number of calls generated between the first and last day via the Google Business Profile over the requested month.  \n_(current month by default)_",
    "8-0": "**action_website_count**",
    "8-1": "Amount of traffic generated between the first and last day by the Google Business Profile over the requested month  \n_(current month by default)_",
    "9-0": "**itinerary_count**",
    "9-1": "Number of times this button was used between the first and last day over the requested month.  \n_(current month by default)_",
    "10-0": "**views_count**",
    "10-1": "Number of times the Google Score has been viewed between the first and last day over the requested month.  \n_(current month by default)_",
    "11-0": "**rating_distribution**",
    "11-1": "Evolution of the number of received reviews between the first and last day over the requested month.  \n_(current month by default)_"
  },
  "cols": 2,
  "rows": 12,
  "align": [
    "left",
    "left"
  ]
}
[/block]


> 📘 Zoom on "key" and "description" attribute
> 
> This attributes are only filled in when "by" or "by_level_category" is used.  
> Otherwise they have the value `null`.

# Add some filters

It is possible to add GET parameters to refine the calculation of the Google Score over a defined month, an establishment...

## GET parameters

To calculate a Google Score, it is possible to combine the following GET parameters:

[block:parameters]
{
  "data": {
    "h-0": "GET parameters",
    "h-1": "Description",
    "0-0": "**month**",
    "0-1": "Month for the calculation period.  \n_Format : YYYY-MM_",
    "1-0": "**place**",
    "1-1": "Filter on an establishment.  \n_It is necessary to indicate the ID of the establishment from the endpoint [/places](ref:places_list) _",
    "2-0": "**places**",
    "2-1": "Filter on an establishment list.  \n_Format : Establishment IDs separated by commas_",
    "3-0": "**level**",
    "3-1": "Filter on a level.  \n_It is necessary to indicate the ID of the establishment from the endpoint [/levels](ref:levels_list) _",
    "4-0": "**levels**",
    "4-1": "Filter on a level list.  \n_Format : Level IDs separated by commas_",
    "5-0": "**by**",
    "5-1": "Group calculations by.  \nSee chapter [by](google-score#by) ",
    "6-0": "**by_level_category**",
    "6-1": "Group calculations by level category.  \nSee chapter [by Level Category](google-score#by-level-category) "
  },
  "cols": 2,
  "rows": 7,
  "align": [
    "left",
    "left"
  ]
}
[/block]


## Group calculations

The two "by" parameters allow you to retrieve a list of results aggregated according to the value selected in the input.

> 📘 Combine the "by" or not combine the "by" ?
> 
> You can combine several other GET parameters with a "by" but you can not combine the filters "by" and "by_level_category" in a single request. Only one aggregation parameter is allowed.

Here are the 2 possibilities:

### By

Calculate the Google Score by grouping elements and return a list.

The distribution of the calculation can be by : "month", "place".

See "[By establishment over the month of May 2024](google-score#by-establishment-over-the-month-of-may-2024)" or [By month for one level](google-score#by-month-for-one-level) use cases.

### By Level Category

Calculate the Google Score by level category and return a list.

The categories represent your hierarchical or geographical organization depending on your Goodays configuration.

From these categories you can calculate the Google Score distributed by region, business unit, brand, etc.

The category ID to be used is returned by the endpoint [/levels](ref:levels_list), in the "category_id" attribute.

See "[By level category](google-score#by-level-category-1)" use case.

# Use cases

Here are some examples to show you the possibilities of this endpoint. This is obviously not exhaustive, it's up to you to have fun to find the right parameter arrangements :)

## By establishment over the month of May 2024

I have to use the following parameters:

- month : the month of May 2024
- by : group calculation by "place"

```curl Google Score call
curl --location --request GET 'https://api.goodays.co/v2/stats/google_score? \
   month=2024-05 \
   &by=place' \
--header 'Content-Type: application/json' \
--header 'Authorization: 1234abcd1234abcd1234abcd1234abcd'
```

```json Google Score by place on the month of May 2024
{
    "data": [
        {
            "key": "Qr43Y5Wo8V",
            "description": "Style Haguenau (Haguenau) - 001",
            "public_rating": 3.99,
            "public_rating_count": 543,
            "places_count": 1,
            "monthly_rating": 3.75,
            "monthly_rating_count": 32,
            "action_phone_count": 757,
            "action_website_count": 6050,
            "itinerary_count": 2273,
            "views_count": 1034,
            "rating_distribution": [
                {
                    "value": 1,
                    "count": 6
                },
                {
                    "value": 2,
                    "count": 3
                },
                {
                    "value": 3,
                    "count": 3
                },
                {
                    "value": 4,
                    "count": 1
                },
                {
                    "value": 5,
                    "count": 19
                }
            ]
        },
        {
            "key": "MexGwlEXxK",
            "description": "Style Colmar (Colmar) - 002",
            "public_rating": 3.96,
            "public_rating_count": 428,
            "places_count": 1,
            "monthly_rating": 4.16,
            "monthly_rating_count": 31,
            "action_phone_count": 857,
            "action_website_count": 5691,
            "itinerary_count": 1728,
            "views_count": 7892,
            "rating_distribution": [
                {
                    "value": 1,
                    "count": 2
                },
                {
                    "value": 2,
                    "count": 3
                },
                {
                    "value": 3,
                    "count": 4
                },
                {
                    "value": 4,
                    "count": 1
                },
                {
                    "value": 5,
                    "count": 21
                }
            ]
        },
        {
            "key": "KQ4ekDyg8e",
            "description": "Style Mulhouse (Mulhouse) - 003",
            "public_rating": 3.97,
            "public_rating_count": 76,
            "places_count": 1,
            "monthly_rating": 3.66,
            "monthly_rating_count": 29,
            "action_phone_count": 890,
            "action_website_count": 474,
            "itinerary_count": 1575,
            "views_count": 1600,
            "rating_distribution": [
                {
                    "value": 1,
                    "count": 6
                },
                {
                    "value": 2,
                    "count": 4
                },
                {
                    "value": 3,
                    "count": 1
                },
                {
                    "value": 4,
                    "count": 1
                },
                {
                    "value": 5,
                    "count": 17
                }
            ]
        }
    ]
}
```

> 📘 Zoom on "by" parameter
> 
> Here the "by" distributes the calculation by establishment. The attribute "key" contains the ID of the establishment and the "description" its name.

## By month for one level

I have to use the following parameters :

- level : level ID
- by : "month"

_Hypothesis: in our configuration the level ID "bQdPk9M89r" corresponds to our level "Greater London"_

```curl Google Score call
curl --location --request GET 'https://api.goodays.co/v2/stats/google_score? \
  level=bQdPk9M89r \
  &by=month' \
--header 'Content-Type: application/json' \
--header 'Authorization: 1234abcd1234abcd1234abcd1234abcd'
```

```json Google Score by month for one level
{
    "data": [
        {
            "key": "2024-03",
            "description": "2024-03",
            "public_rating": 3.95,
            "public_rating_count": 4427,
            "places_count": 1,
            "monthly_rating": 3.6,
            "monthly_rating_count": 42,
            "action_phone_count": 1548,
            "action_website_count": 8210,
            "itinerary_count": 18592,
            "views_count": 179935,
            "rating_distribution": [
                {
                    "value": 1,
                    "count": 8
                },
                {
                    "value": 2,
                    "count": 4
                },
                {
                    "value": 3,
                    "count": 4
                },
                {
                    "value": 4,
                    "count": 7
                },
                {
                    "value": 5,
                    "count": 19
                }
            ]
        },
        {
            "key": "2024-04",
            "description": "2024-04",
            "public_rating": 3.96,
            "public_rating_count": 4470,
            "places_count": 1,
            "monthly_rating": 4.26,
            "monthly_rating_count": 43,
            "action_phone_count": 3768,
            "action_website_count": 4277,
            "itinerary_count": 12220,
            "views_count": 304021,
            "rating_distribution": [
                {
                    "value": 1,
                    "count": 5
                },
                {
                    "value": 2,
                    "count": 2
                },
                {
                    "value": 3,
                    "count": 3
                },
                {
                    "value": 4,
                    "count": 0
                },
                {
                    "value": 5,
                    "count": 33
                }
            ]
        },
        {
            "key": "2024-05",
            "description": "2024-05",
            "public_rating": 3.96,
            "public_rating_count": 4501,
            "places_count": 1,
            "monthly_rating": 4.16,
            "monthly_rating_count": 31,
            "action_phone_count": 2901,
            "action_website_count": 3766,
            "itinerary_count": 12057,
            "views_count": 171853,
            "rating_distribution": [
                {
                    "value": 1,
                    "count": 3
                },
                {
                    "value": 2,
                    "count": 1
                },
                {
                    "value": 3,
                    "count": 4
                },
                {
                    "value": 4,
                    "count": 3
                },
                {
                    "value": 5,
                    "count": 20
                }
            ]
        }
    ]
}
```

> 📘 Zoom on "by" parameter
> 
> The attributes "key" and "description" both contain the relevant year and month.

## By level category

I have to use the following parameters:

- by_level_category : "2"

_Hypothesis: in our configuration the level category "2" corresponds to our level "regions"._

```curl Google Score call
curl --location --request GET 'https://api.goodays.co/v2/stats/google_score? \
  by_level_category=2' \
--header 'Content-Type: application/json' \
--header 'Authorization: 1234abcd1234abcd1234abcd1234abcd'
```

```json Google Score by level category
{
    "data": [
        {
            "key": "AEd7RrD893",
            "description": "East Midlands",
            "public_rating": 3.98,
            "public_rating_count": 81606,
            "places_count": 18,
            "monthly_rating": 4.0,
            "monthly_rating_count": 551,
            "action_phone_count": 38894,
            "action_website_count": 74268,
            "itinerary_count": 118659,
            "views_count": 2533490,
            "rating_distribution": [
                {
                    "value": 1,
                    "count": 49
                },
                {
                    "value": 2,
                    "count": 62
                },
                {
                    "value": 3,
                    "count": 57
                },
                {
                    "value": 4,
                    "count": 57
                },
                {
                    "value": 5,
                    "count": 326
                }
            ]
        },
        {
            "key": "rY4WkQk49w",
            "description": "West Midlands",
            "public_rating": 3.98,
            "public_rating_count": 90568,
            "places_count": 20,
            "monthly_rating": 3.94,
            "monthly_rating_count": 623,
            "action_phone_count": 42002,
            "action_website_count": 76763,
            "itinerary_count": 188640,
            "views_count": 3319740,
            "rating_distribution": [
                {
                    "value": 1,
                    "count": 59
                },
                {
                    "value": 2,
                    "count": 77
                },
                {
                    "value": 3,
                    "count": 68
                },
                {
                    "value": 4,
                    "count": 57
                },
                {
                    "value": 5,
                    "count": 362
                }
            ]
        },
        {
            "key": "9v8XRlZ43o",
            "description": "Yorkshire and the Humber",
            "public_rating": 3.99,
            "public_rating_count": 77038,
            "places_count": 17,
            "monthly_rating": 3.97,
            "monthly_rating_count": 543,
            "action_phone_count": 32274,
            "action_website_count": 58795,
            "itinerary_count": 175455,
            "views_count": 2402351,
            "rating_distribution": [
                {
                    "value": 1,
                    "count": 54
                },
                {
                    "value": 2,
                    "count": 63
                },
                {
                    "value": 3,
                    "count": 53
                },
                {
                    "value": 4,
                    "count": 46
                },
                {
                    "value": 5,
                    "count": 327
                }
            ]
        }
    ]
}
```

> 📘 Zoom on "by_level_category" parameter
> 
> Here the "by_level_category" distributes the calculation by level category. The attribute "key" contains the ID of the level and the "description" the level name.