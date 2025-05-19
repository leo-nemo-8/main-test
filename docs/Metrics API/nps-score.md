---
title: NPS - Net Promoter Score
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
> The NPS (**Net Promoter Score**) is an indicator calculated from a very specific question about the customer's **intention to recommend** you to others.
> 
> The question used in the survey is:  
> “Would you recommend this establishment to your friends and family?”  
> The answer is on a scale of 0 to 10.
> 
> The NPS is used to sort respondents into three main categories:
> 
> - “**DETRACTORS**”, who gave a score between 0 and 6
> - “**PASSIVES**”, who gave a score of 7 or 8
> - “**PROMOTERS**”, who gave a score of 9 or 10
> 
> _That score can then be analyzed over any period of time or the focus can be narrowed to any given survey, a particular POS or any other analysis filter you wish to apply._

> 👍 Going further
> 
> Consult the [general Metrics API documentation](/docs/exploit-the-full-potential-of-your-data) for more.

![](https://files.readme.io/ccdcc23-NPS.png "NPS.png")

# How do I get my NPS?

With [/stats/nps](ref:stats_nps_list):

```curl nps call
curl --location --request GET 'https://api.goodays.co/v2/stats/nps' \
--header 'Content-Type: application/json' \
--header 'Authorization: 1234abcd1234abcd1234abcd1234abcd'
```

```json Sample NPS
{
    "data": [
        {
            "key": null,
            "description": null,
            "count": 534522,
            "score": 50,
            "detractor": {
                "count": 52234,
                "percentage": 9.772095442283012
            },
            "passive": {
                "count": 160222,
                "percentage": 29.974818622994004
            },
            "promoter": {
                "count": 322066,
                "percentage": 60.25308593472298
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
    "2-1": "Number of participations in the selection over the requested period.",
    "3-0": "**score**",
    "3-1": "NPS Score  \nFormula: % promoters - % detractors",
    "4-0": "**detractor** ",
    "4-1": "End Customer who answered the ‘how likely are you to recommend this establishment to a friend or colleague?’ question with a score of 0 to 6.",
    "5-0": "**passive**",
    "5-1": "End Customer who answered the ‘how likely are you to recommend this establishment to a friend or colleague?’ question with a score of 7 or 8.",
    "6-0": "**promoter**",
    "6-1": "End Customer who answered the ‘how likely are you to recommend this establishment to a friend or colleague?’ question with a score of 9 or 10.",
    "7-0": "**count** ",
    "7-1": "Number of responses to \"NPS\" questions observed over the requested periods for the detractor, passive or promoter.",
    "8-0": "**percentage** ",
    "8-1": "Percentage of responses to \"NPS\" questions observed over the requested periods for the detractor, passive or promoter."
  },
  "cols": 2,
  "rows": 9,
  "align": [
    "left",
    "left"
  ]
}
[/block]


> 📘 Zoom on "key" and "description" attribute
> 
> This attributes are only filled in when "by", "by_context" or "by_level_category" is used.  
> Otherwise they have the value `null`.

# Add some filters

It is possible to add GET parameters to refine the calculation of the score over a defined period, an establishment...

## GET parameters

To calculate a NPS, it is possible to combine the following GET parameters:

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
    "11-1": "Group calculations by.  \nSee chapter [by](nps-score#by)",
    "12-0": "**by_context** ",
    "12-1": "Group calculations by Additional Information.  \nSee chapter [by Context](nps-score#by-context)",
    "13-0": "**by_level_category** ",
    "13-1": "Group calculations by level category.  \nSee chapter [by Level Category](nps-score#by-level-category)"
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
> The examples listed for the "source" parameter are not exhaustive. To obtain an exhaustive list, the endpoint [/stats/nps](ref:stats_nps_list) must be called by indicating an unexpected value. In return the error message will list all possible values.

## Group calculations

The three "by" parameters allow you to retrieve a list of results aggregated according to the value selected in the input.

> 📘 Combine the "by" or not combine the "by" ?
> 
> You can combine several other GET parameters with a "by" but you can not combine the filters "by", "by_context" and "by_level_category" in a single request. Only one aggregation parameter is allowed.

Here are the 3 possibilities:

### By

Calculate the NPS by grouping elements and return a list.

The distribution of the calculation can be by : "day", "month", "nps_category", "place", "quarter", "remark_type", "source", "survey", "year".

See "[By establishment over the month of May 2020](nps-score#by-establishment-over-the-month-of-may-2020)" or [By month for one level and a specific source](nps-score#by-month-for-one-level-and-a-specific-source) use cases.

### By Context

Calculate the NPS for each value of the "Additional Information" passed as a parameter and return a list.

"Additional Information" is data attached to a response to give a better understanding about the context.

The list of Additional Information available depends on your Goodays configuration and can be retrieved by the endpoint [configuration](ref:configuration_list). The only 'Additional Information" usable with this parameter are the one with the field  _"use_in_stats" = true_.

See "[By context of the purchase amount](nps-score#by-context-of-the-purchase-amount)" use case.

### By Level Category

Calculate the NPS by level category and return a list.

The categories represent your hierarchical or geographical organization depending on your Goodays configuration.

From these categories you can calculate the NPS distributed by region, business unit, brand, etc.

The category ID to be used is returned by the endpoint [/levels](ref:levels_list), in the "category_id" attribute.

See "[By level category](nps-score#by-level-category-1)" use case.

# Use cases

Here are some examples to show you the possibilities of this endpoint. This is obviously not exhaustive, it's up to you to have fun to find the right parameter arrangements :)

## By establishment over the month of May 2020

I have to use the following parameters :

- begin : the first date of the month of May
- end : the last date of the month of May
- by : group calculation by "place"

```curl NPS call
curl --location --request GET 'https://api.goodays.co/v2/stats/nps? \
   begin=2020-05-01T00:00:00Z \
   &end=2020-05-31T23:59:00Z \
   &by=place' \
--header 'Content-Type: application/json' \
--header 'Authorization: 1234abcd1234abcd1234abcd1234abcd'
```

```json NPS by place on the month of May 2020
{
    "data": [
        {
            "key": "egxK551kdo",
            "description": "VÉLO Brest (Brest)",
            "count": 14788,
            "score": 50,
            "detractor": {
                "count": 1474,
                "percentage": 9.967541249661888
            },
            "passive": {
                "count": 4423,
                "percentage": 29.909385988639436
            },
            "promoter": {
                "count": 8891,
                "percentage": 60.12307276169867
            }
        },
        {
            "key": "bQdPLrmwd9",
            "description": "VÉLO Chambéry (Chambéry) - velo-chambery",
            "count": 3835,
            "score": 52,
            "detractor": {
                "count": 454,
                "percentage": 11.83833116036506
            },
            "passive": {
                "count": 918,
                "percentage": 23.9374185136897
            },
            "promoter": {
                "count": 2463,
                "percentage": 64.22425032594525
            }
        }
    ]
}
```

> 📘 Zoom on "by" parameter
> 
> Here the "by" distributes the calculation by establishment. The attribute "key" contains the ID of the establishment and the "description" its name.

## For one End Customer

I have to use the following parameters:

- email

**Tips :** you can add the parameter "by" with the value "place" to get a distribution of this end-customer's scores by establishment.

```curl NPS call
curl --location --request GET 'https://api.goodays.co/v2/stats/nps? \
email=max.guevara@angel.com' \
--header 'Content-Type: application/json' \
--header 'Authorization: 1234abcd1234abcd1234abcd1234abcd'
```

```json NPS
{
    "data": [
        {
            "key": null,
            "description": null,
            "count": 5,
            "score": 20,
            "detractor": {
                "count": 2,
                "percentage": 40
            },
            "passive": {
                "count": 0,
                "percentage": 0.0
            },
            "promoter": {
                "count": 3,
                "percentage": 60
            }
        }
    ]
}
```

> 📘 Zoom on "by" parameter
> 
> Here there is no "by". The attribute "key" and "description" contains "null".

## By month for one level and a specific source

I have to use the following parameters :

- source : "email"
- level : level ID
- by : "month"

_Hypothesis: in our configuration the level ID "Yqxzp5Ad2J" corresponds to our level "South France"_

```curl NPS call
curl --location --request GET 'https://api.goodays.co/v2/stats/nps? \
source=email \
&level=Yqxzp5Ad2J \
&by=month' \
--header 'Content-Type: application/json' \
--header 'Authorization: 1234abcd1234abcd1234abcd1234abcd'
```

```json NPS by month for one one level and a specific source
{
    "data": [
        {
            "key": "2020-01",
            "description": "2020-01",
            "count": 611,
            "score": 47,
            "detractor": {
                "count": 85,
                "percentage": 13.911620294599016
            },
            "passive": {
                "count": 153,
                "percentage": 25.040916530278235
            },
            "promoter": {
                "count": 373,
                "percentage": 61.04746317512275
            }
        },
        {
            "key": "2020-02",
            "description": "2020-02",
            "count": 137,
            "score": 25,
            "detractor": {
                "count": 31,
                "percentage": 22.62773722627737
            },
            "passive": {
                "count": 41,
                "percentage": 29.927007299270077
            },
            "promoter": {
                "count": 65,
                "percentage": 47.44525547445255
            }
        },
        {
            "key": "2020-03",
            "description": "2020-03",
            "count": 156,
            "score": -1,
            "detractor": {
                "count": 59,
                "percentage": 37.82051282051282
            },
            "passive": {
                "count": 39,
                "percentage": 25.0
            },
            "promoter": {
                "count": 58,
                "percentage": 37.17948717948718
            }
        },
    ]
}
```

> 📘 Zoom on "by" parameter
> 
> The attributes "key" and "description" both contain the relevant year and month.

## By context of the purchase amount

I have to use the following parameters :

- by_context : "price"  
  \_Hypothesis: additional information exists in your configuration and is present in ever response._ 

```curl nps call
curl --location --request GET 'https://api.goodays.co/v2/stats/nps?by_context=price' \
--header 'Content-Type: application/json' \
--header 'Authorization: 1234abcd1234abcd1234abcd1234abcd'
```

```json NPS by month for one one level and a specific source
{
    "data": [
        {
            "key": "3Q54E78yD9",
            "description": "Entre 500 et 1000€",
            "count": 267,
            "score": -30,
            "detractor": {
                "count": 143,
                "percentage": 53.558052434456926
            },
            "passive": {
                "count": 61,
                "percentage": 22.846441947565545
            },
            "promoter": {
                "count": 63,
                "percentage": 23.595505617977526
            }
        },
        {
            "key": "lZmxo9dj6G",
            "description": "Entre 200 et 500€",
            "count": 156,
            "score": -1,
            "detractor": {
                "count": 59,
                "percentage": 37.82051282051282
            },
            "passive": {
                "count": 39,
                "percentage": 25.0
            },
            "promoter": {
                "count": 58,
                "percentage": 37.17948717948718
            }
        },
        {
            "key": "NEexq5xYzW",
            "description": "Supérieur à 1000€",
            "count": 137,
            "score": 25,
            "detractor": {
                "count": 31,
                "percentage": 22.62773722627737
            },
            "passive": {
                "count": 41,
                "percentage": 29.927007299270077
            },
            "promoter": {
                "count": 65,
                "percentage": 47.44525547445255
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

_Hypothesis: in our configuration the level category "2" corresponds to our level "regions"._

```curl nps call
curl --location --request GET 'https://api.goodays.co/v2/stats/nps? \
  by_level_category=2' \
--header 'Content-Type: application/json' \
--header 'Authorization: 1234abcd1234abcd1234abcd1234abcd'
```

```json NPS by level category
{
    "data": [
        {
            "key": "LAEd7rX893",
            "description": "Bretagne",
            "count": 331,
            "score": 6,
            "detractor": {
                "count": 109,
                "percentage": 32.93051359516616
            },
            "passive": {
                "count": 94,
                "percentage": 28.3987915407855
            },
            "promoter": {
                "count": 128,
                "percentage": 38.670694864048336
            }
        },
        {
            "key": "ELxjpqAdKg",
            "description": "Berlin - berlin",
            "count": 183,
            "score": -40,
            "detractor": {
                "count": 104,
                "percentage": 56.830601092896174
            },
            "passive": {
                "count": 49,
                "percentage": 26.775956284153008
            },
            "promoter": {
                "count": 30,
                "percentage": 16.39344262295082
            }
        },
        {
            "key": "OKQ4eXAdeW",
            "description": "Provence-Alpes-Côte d'Azur",
            "count": 483,
            "score": 5,
            "detractor": {
                "count": 134,
                "percentage": 27.74327122153209
            },
            "passive": {
                "count": 189,
                "percentage": 39.130434782608695
            },
            "promoter": {
                "count": 160,
                "percentage": 33.126293995859214
            }
        }
    ]
}
```

> 📘 Zoom on "by_level_category" parameter
> 
> Here the "by_level_category" distributes the calculation by level category. The attribute "key" contains the ID of the level and the "description" the level name.