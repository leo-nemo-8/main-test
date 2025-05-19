---
title: Dissatisfaction
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
> 📘 What's that?
> 
> A Dissatisfaction Alert is triggered if an End Customer gives a low score on a pre-defined survey question or leaves a problem remark.
> 
> Each Dissatisfaction Alert is highlighted in the Goodays Back Office and must be handled by the Local Manager by a call or message to the End Customer to understand their dissatisfaction.

> 👍 Going further
> 
> Consult the [general Metrics API documentation](/docs/exploit-the-full-potential-of-your-data) for more.

[block:image]
{
  "images": [
    {
      "image": [
        "https://files.readme.io/124eeb3-Product_synthesis.png",
        "Product synthesis.png",
        1024
      ],
      "align": "center",
      "sizing": "smart"
    }
  ]
}
[/block]


# How do I get my Dissatisfaction metrics?

With [/stats/dissatisfaction](ref:stats_dissatisfaction_list):

```curl Satisfaction call
curl --location --request GET 'https://api.goodays.co/v2/stats/dissatisfaction' \
--header 'Content-Type: application/json' \
--header 'Authorization: 1234abcd1234abcd1234abcd1234abcd'
```

```json Sample Satisfaction
{
    "data": [
        {
            "key": null,
            "description": null,
            "count": 996,
            "percentage": 2.86264478487052,
            "pending": {
                "count": 25,
                "percentage": 2.5100401606425704
            },
            "spam": {
                "count": 21,
                "percentage": 2.108433734939759
            },
            "ignored": {
                "count": 36,
                "percentage": 3.614457831325301
            },
            "call": {
                "count": 83,
                "percentage": 8.333333333333332
            },
            "text": {
                "count": 831,
                "percentage": 83.43373493975903
            }
        }
    ]
}
```

By default the calculation of the score is done "since always".  
And the return will always contain:

[block:parameters]
{
  "data": {
    "h-0": "Attribute",
    "h-1": "Description",
    "0-0": "**key** ",
    "0-1": "Distribution key ID.",
    "1-0": "**description** ",
    "1-1": "Description of the distribution key.",
    "2-0": "**count**",
    "2-1": "Total number of responses that triggered a dissatisfaction alert.",
    "3-0": "**percentage**",
    "3-1": "Percentage of total volume of responses received.",
    "4-0": "**pending**",
    "4-1": "**count**: total number of dissatisfaction alert in `pending` status  \n**percentage**: Percentage of dissatisfaction alert with this status",
    "5-0": "**spam**",
    "5-1": "**count**: total number of dissatisfaction alert in `spam` status  \n**percentage**: Percentage of dissatisfaction alert with this status",
    "6-0": "**ignored**",
    "6-1": "**count**: total number of dissatisfaction alert in `ignored` status  \n**percentage**: Percentage of dissatisfaction alert with this status",
    "7-0": "**call**",
    "7-1": "**count**: total number of dissatisfaction alert in `call` status  \n**percentage**: Percentage of dissatisfaction alerts with this status",
    "8-0": "**text**",
    "8-1": "**count**: total number of dissatisfaction alert in `pending` status  \n**percentage**: Percentage of dissatisfaction alert with this status"
  },
  "cols": 2,
  "rows": 9,
  "align": [
    "left",
    "left"
  ]
}
[/block]


> 📘 Status
> 
> Responses (with or without a dissatisfaction alert) can have different statuses:
> 
> - **pending**: the processing of the response has been put on hold by the Local Manager.
> - **spam**: response was spammed by the Local Manager.
> - **ignored**: response was ignored by the Local Manager.
> - **call**: the response was processed by a call to the End Customer by the Local Manager.
> - **text**: the processing of the participation was written to the End User by the Local Manager.

> 📘 Zoom on "key" and "description" attribute
> 
> These attributes are only filled in when filters "by", "by_context" or "by_level_category" are used.  
> Otherwise they have the value `null`.

# Add some filters

It is possible to add GET parameters to refine the calculation of the dissatisfaction results over a defined period, an establishment...

## GET parameters

To filter the dissatisfaction results, it is possible to combine the following GET parameters:

[block:parameters]
{
  "data": {
    "h-0": "GET parameters",
    "h-1": "Description",
    "0-0": "**begin**",
    "0-1": "Start date of the calculation period.  \n_Format : YYYY-MM-DDThh:mm:ssZ_  \nSee [this page](doc:timezone-management) for the timezone management.",
    "1-0": "**end**",
    "1-1": "End date of the calculation period.  \n_Format : YYYY-MM-DDThh:mm:ssZ_  \nSee [this page](doc:timezone-management) for the timezone management.",
    "2-0": "**place** ",
    "2-1": "Filter on an establishment.  \n_It is necessary to indicate the ID of the establishment from the endpoint [/places](ref:places_list)_",
    "3-0": "**places** ",
    "3-1": "Filter on an establishment list.  \n_Format : Establishment IDs separated by commas_",
    "4-0": "**level** ",
    "4-1": "Filter on a level.  \n_It is necessary to indicate the ID of the establishment from the endpoint [/levels](ref:levels_list)_",
    "5-0": "**levels** ",
    "5-1": "Filter on a level list.  \n_Format : Level IDs separated by commas_",
    "6-0": "**survey**",
    "6-1": "filter on a survey.  \n_It is necessary to indicate the ID of the question from the endpoint [/surveys](ref:surveys_list)_",
    "7-0": "**question** ",
    "7-1": "Filter on a question.  \n_It is necessary to indicate the ID of the question from the endpoint [/surveys](ref:surveys_list)_",
    "8-0": "**nps** ",
    "8-1": "Filter on nps category : \"detractor\", \"passive\", \"promoter\".",
    "9-0": "**remark_type** ",
    "9-1": "Filter on remark type : \"Idea\", \"Message\",  \"Praise\", \"Problem\", \"Question\".",
    "10-0": "**source** ",
    "10-1": "Filter on source : \"critizr\", \"email\", \"facebook\", \"google\", \"sms\", \"tripadvisor\", \"widget\", \"wifi\".",
    "11-0": "**by** ",
    "11-1": "Group calculations by.  \nSee chapter [by](dissatisfaction#by)",
    "12-0": "**by_context** ",
    "12-1": "Group calculations by Additional Information.  \nSee chapter [by Context](dissatisfaction#by-context)",
    "13-0": "**by_level_category** ",
    "13-1": "Group calculations by level category.  \nSee chapter [by Level Category](dissatisfaction#by-level-category)"
  },
  "cols": 2,
  "rows": 14,
  "align": [
    "left",
    "left"
  ]
}
[/block]


> 📘 Get an updated list of values for the "source" parameter
> 
> The examples listed for the "source" parameter are not exhaustive. To obtain an exhaustive list, the endpoint [/stats/dissatisfaction](ref:dissatisfaction) must be called by indicating an unexpected value. In return, the error message will list all possible values.

## Group calculations

The three "by" parameters allow you to retrieve a list of results aggregated according to the value selected in the input.

> 📘 Combine the "by" or not combine the "by" ?
> 
> You can combine several other GET parameters with an aggregation parameter but you can not combine the filters "by", "by_context" and "by_level_category" in a single request. Only one aggregation parameter is allowed.

Here are the 3 possibilities :

### By

Refine the calculation of the dissatisfaction results by grouping elements and return a list.

The distribution of the calculation can be by : "day", "month", "nps_category", "place", "quarter", "remark_type", "source", "survey", "year".

See "[By establishment over the month of May 2020](dissatisfaction#by-establishment-over-the-month-of-may-2020)" or [By month for one level and a specific source](dissatisfaction#by-month-for-one-level-and-a-specific-source) use cases.

### By Context

Refine the calculation of the dissatisfaction results for each value of the "Additional Information" passed as a parameter and returns a list.

"Additional Information" is additional data attached to a response to give a better understanding about the context.

The list of "Additional Information" available depends on your Goodays configuration and can be retrieved by the endpoint [configuration](ref:configuration_list). The only 'Additional Information" usable with this parameter are the one with the field _"use_in_stats" = true_.

See "[By context of the purchase amount](dissatisfaction#by-context-of-the-purchase-amount)" use case.

### By Level Category

Refine the calculation of the dissatisfaction results by level category and return a list.

The categories represent your hierarchical or geographical organization depending on your Goodays configuration.

From these categories, you can calculate the customer satisfaction score distributed by region, business unit, brand, etc.

The category ID to be used is returned by the endpoint [/levels](ref:levels_list), in the "category_id" attribute.

See "[By level category](dissatisfaction#by-level-category-1)" use case.

# Use cases

Here are some examples to show you the possibilities of this endpoint. This is obviously not exhaustive, it's up to you to have fun to find the right parameter arrangements :)

## By establishment over the month of May 2020

I have to use the following parameters :

- begin : the first date of the month of May
- end_date : the last date of the month of May
- by : end calculation by "place"

```curl
curl --location --request GET 'https://api.goodays.co/v2/stats/dissatisfaction? \
   begin=2020-05-01T00:00:00Z \
   &end=2020-05-31T23:59:00Z \
   &by=place' \
--header 'Content-Type: application/json' \
--header 'Authorization: 1234abcd1234abcd1234abcd1234abcd'
```

```json Customer-Satisfaction Score by place on the last month
{
    "data": [
        {
            "key": "OVdvjjo5dY",
            "description": "VÉLO Paris XVII (Paris) - velo-paris-xvii",
            "count": 334,
            "percentage": 27.69485903814262,
            "pending": {
                "count": 0,
                "percentage": 0
            },
            "spam": {
                "count": 0,
                "percentage": 0
            },
            "ignored": {
                "count": 0,
                "percentage": 0
            },
            "call": {
                "count": 7,
                "percentage": 2.095808383233533
            },
            "text": {
                "count": 327,
                "percentage": 97.90419161676647
            }
        },
        {
            "key": "yLdL5veY4j",
            "description": "La boutique du Vélo (Lille) - training-1",
            "count": 7,
            "percentage": 2.82258064516129,
            "pending": {
                "count": 0,
                "percentage": 0
            },
            "spam": {
                "count": 0,
                "percentage": 0
            },
            "ignored": {
                "count": 1,
                "percentage": 14.285714285714285
            },
            "call": {
                "count": 3,
                "percentage": 42.857142857142854
            },
            "text": {
                "count": 3,
                "percentage": 42.857142857142854
            }
        },
        {
            "key": "pe8NEvPLxj",
            "description": "Mon magasin Vélo (Lille) - training-2",
            "count": 6,
            "percentage": 5.3097345132743365,
            "pending": {
                "count": 0,
                "percentage": 0
            },
            "spam": {
                "count": 2,
                "percentage": 33.33333333333333
            },
            "ignored": {
                "count": 1,
                "percentage": 16.666666666666664
            },
            "call": {
                "count": 1,
                "percentage": 16.666666666666664
            },
            "text": {
                "count": 2,
                "percentage": 33.33333333333333
            }
        }
}
```

> 📘 Zoom on "by" parameter
> 
> Here the "by" distributes the calculation by establishment. The attribute "key" contains the ID of the institution and the "description" its name.

## By month for one level and a specific source

I have to use the following parameters :

- source : "email"
- level : level ID
- by : "month"

_Hypothesis: in our configuration the level ID "Yqxzp5Ad2J" corresponds to our level "South France"_

```curl Satisfaction call
curl --location --request GET 'https://api.goodays.co/v2/stats/dissatisfaction? \
source=email \
&level=Yqxzp5Ad2J \
&by=month' \
--header 'Content-Type: application/json' \
--header 'Authorization: 1234abcd1234abcd1234abcd1234abcd'
```

```json Customer-Satisfaction Score by month for one one level and a specific source
{
    "data": [
        {
            "key": "2021-07",
            "description": "2021-06",
            "count": 5,
            "percentage": 100.0,
            "pending": {
                "count": 3,
                "percentage": 60.0
            },
            "spam": {
                "count": 0,
                "percentage": 0
            },
            "ignored": {
                "count": 0,
                "percentage": 0
            },
            "call": {
                "count": 0,
                "percentage": 0
            },
            "text": {
                "count": 2,
                "percentage": 40.0
            }
        },
        {
            "key": "2021-08",
            "description": "2021-08",
            "count": 1,
            "percentage": 50.0,
            "pending": {
                "count": 0,
                "percentage": 0
            },
            "spam": {
                "count": 0,
                "percentage": 0
            },
            "ignored": {
                "count": 0,
                "percentage": 0
            },
            "call": {
                "count": 0,
                "percentage": 0
            },
            "text": {
                "count": 1,
                "percentage": 100.0
            }
        },
        {
            "key": "2021-09",
            "description": "2021-09",
            "count": 2,
            "percentage": 100.0,
            "pending": {
                "count": 0,
                "percentage": 0
            },
            "spam": {
                "count": 0,
                "percentage": 0
            },
            "ignored": {
                "count": 0,
                "percentage": 0
            },
            "call": {
                "count": 0,
                "percentage": 0
            },
            "text": {
                "count": 2,
                "percentage": 100.0
            }
        }
    ]
}
```

> 📘 Zoom on "by" parameter
> 
> The attributes "key" and "description" both contain the relevant year and month.

## By context of the purchase amount

I have to use the following parameters :

- by_context : "advisor"

_Hypothesis: additional information exists in your configuration and is present in every response._ 

```curl Satisfaction call
curl --location --request GET 'https://api.goodays.co/v2/stats/dissatisfaction?by_context=advisor' \
--header 'Content-Type: application/json' \
--header 'Authorization: 1234abcd1234abcd1234abcd1234abcd'
```

```json Customer-Satisfaction Score by month for one one level and a specific source
{
    "data": [
        {
            "key": "BQe4Zoxprb",
            "description": "Nizar",
            "count": 26,
            "percentage": 60.46511627906976,
            "pending": {
                "count": 0,
                "percentage": 0
            },
            "spam": {
                "count": 0,
                "percentage": 0
            },
            "ignored": {
                "count": 0,
                "percentage": 0
            },
            "call": {
                "count": 1,
                "percentage": 3.8461538461538463
            },
            "text": {
                "count": 25,
                "percentage": 96.15384615384616
            }
        },
        {
            "key": "1pe8NmxjKm",
            "description": "Jeanne",
            "count": 6,
            "percentage": 19.35483870967742,
            "pending": {
                "count": 0,
                "percentage": 0
            },
            "spam": {
                "count": 1,
                "percentage": 16.666666666666664
            },
            "ignored": {
                "count": 0,
                "percentage": 0
            },
            "call": {
                "count": 4,
                "percentage": 66.66666666666666
            },
            "text": {
                "count": 1,
                "percentage": 16.666666666666664
            }
        },
        {
            "key": "ryLdLpdj1e",
            "description": "Clémence",
            "count": 1,
            "percentage": 100.0,
            "pending": {
                "count": 0,
                "percentage": 0
            },
            "spam": {
                "count": 0,
                "percentage": 0
            },
            "ignored": {
                "count": 0,
                "percentage": 0
            },
            "call": {
                "count": 0,
                "percentage": 0
            },
            "text": {
                "count": 1,
                "percentage": 100.0
            }
        }
    ]
}
```

> 📘 Zoom on "by_context" parameter
> 
> Here the "by_context" distributes the calculation by additional information "price". The attribute "key" contains the ID of the additional information and the "description" its name.

## By level category

I have to use the following parameters :

- by_level_category : "2"

_Hypothesis: in our configuration the level category "2" refers to your regions._

```curl Satisfaction call
curl --location --request GET 'https://api.goodays.co/v2/stats/dissatisfaction?by_level_category=5' \
--header 'Content-Type: application/json' \
--header 'Authorization: 1234abcd1234abcd1234abcd1234abcd'
```

```json Customer-Satisfaction Score by level category
{
    "data": [
        {
            "key": "BQe4Zoxprb",
            "description": "France",
            "count": 26,
            "percentage": 60.46511627906976,
            "pending": {
                "count": 0,
                "percentage": 0
            },
            "spam": {
                "count": 0,
                "percentage": 0
            },
            "ignored": {
                "count": 0,
                "percentage": 0
            },
            "call": {
                "count": 1,
                "percentage": 3.8461538461538463
            },
            "text": {
                "count": 25,
                "percentage": 96.15384615384616
            }
        },
        {
            "key": "1pe8NmxjKm",
            "description": "Germany",
            "count": 6,
            "percentage": 19.35483870967742,
            "pending": {
                "count": 0,
                "percentage": 0
            },
            "spam": {
                "count": 1,
                "percentage": 16.666666666666664
            },
            "ignored": {
                "count": 0,
                "percentage": 0
            },
            "call": {
                "count": 4,
                "percentage": 66.66666666666666
            },
            "text": {
                "count": 1,
                "percentage": 16.666666666666664
            }
        },
        {
            "key": "ryLdLpdj1e",
            "description": "United Kingdom",
            "count": 1,
            "percentage": 100.0,
            "pending": {
                "count": 0,
                "percentage": 0
            },
            "spam": {
                "count": 0,
                "percentage": 0
            },
            "ignored": {
                "count": 0,
                "percentage": 0
            },
            "call": {
                "count": 0,
                "percentage": 0
            },
            "text": {
                "count": 1,
                "percentage": 100.0
            }
        }
    ]
}
```

> 📘 Zoom on "by_level_category" parameter
> 
> Here the "by_level_category" distributes the calculation by level category. The attribute "key" contains the ID of the level and the "description" the level name.