---
title: Customer-Satisfaction Score
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
> The Customer-Satisfaction score is an average calculated on the basis of the customers’ answers to all the star questions from the published surveys.
> 
> That score can then be analyzed over any period of time or the focus can be narrowed to any given survey, the NPS, a particular establishment, or any other analysis filter you wish to apply.

> 👍 Going further
> 
> Consult the [general Metrics API documentation](/docs/exploit-the-full-potential-of-your-data) for more.

[block:image]
{
  "images": [
    {
      "image": [
        "https://files.readme.io/2252ad3-CSAT.png",
        "CSAT.png",
        1024
      ],
      "align": "center",
      "sizing": "smart"
    }
  ]
}
[/block]


# How do I get my Customer-Satisfaction score?

With [/stats/satisfaction](ref:stats_satisfaction_list):

```curl Satisfaction call
curl --location --request GET 'https://api.goodays.co/v2/stats/satisfaction' \
--header 'Content-Type: application/json' \
--header 'Authorization: 1234abcd1234abcd1234abcd1234abcd'
```

```json Sample Satisfaction
{
    "data": [
        {
            "key": null,
            "description": null,
            "average": 4.415842247536645,
            "ratings_count": 4745,
            "responses_count": 1760
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
    "2-0": "**average** ",
    "2-1": "Average score over the requested period.",
    "3-0": "**ratings_count** ",
    "3-1": "Number of responses to \"star\" questions observed over the requested periods.  \nThere may be several \"star\" questions per response.",
    "4-0": "**responses_count**",
    "4-1": "Number of participations in the selection over the requested period."
  },
  "cols": 2,
  "rows": 5,
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

To calculate a Customer-Satisfaction Score, it is possible to combine the following GET parameters:

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
    "2-1": "Filter on an establishment.  \n_It is necessary to indicate the ID of the establishment from the endpoint [/places](ref:places_read)_",
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
    "11-1": "Group calculations by.  \nSee chapter [by](customer-satisfaction-score#by)",
    "12-0": "**by_context** ",
    "12-1": "Group calculations by Additional Information.  \nSee chapter [by Context](customer-satisfaction-score#by-context)",
    "13-0": "**by_level_category** ",
    "13-1": "Group calculations by level category.  \nSee chapter [by Level Category](customer-satisfaction-score#by-level-category)"
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
> The examples listed for the "source" parameter are not exhaustive. To obtain an exhaustive list, the endpoint [/stats/satisfaction](ref:stats_satisfaction_list) must be called by indicating an unexpected value. In return the error message will list all possible values.

## Group calculations

The three "by" parameters allow you to retrieve a list of results aggregated according to the value selected in the input.

> 📘 Combine the "by" or not combine the "by" ?
> 
> You can combine several other GET parameters with a "by" but you can not combine the filters "by", "by_context" and "by_level_category" in a single request. Only one aggregation parameter is allowed.

Here are the 3 possibilities :

### By

Calculate the Customer-Satisfaction score by grouping elements and return a list.

The distribution of the calculation can be by : "day", "month", "nps_category", "place", "quarter", "remark_type", "source", "survey", "year".

See "[By establishment over the month of May 2020](customer-satisfaction-score#by-establishment-over-the-month-of-may-2020)" or [By month for one level and a specific source](customer-satisfaction-score#by-month-for-one-level-and-a-specific-source) use cases.

### By Context

Calculate the Customer-Satisfaction score for each value of the "Additional Information" passed as a parameter and returns a list.

"Additional Information" is additional data attached to a response to give a better understanding about the context.

The list of "Additional Information" available depends on your Goodays configuration and can be retrieved by the endpoint [configuration](ref:configuration_list). The only 'Additional Information" usable with this parameter are the one with the field _"use_in_stats" = true_.

See "[By context of the purchase amount](customer-satisfaction-score#by-context-of-the-purchase-amount)" use case.

### By Level Category

Calculate the Customer-Satisfaction score by level category and return a list.

The categories represent your hierarchical or geographical organization depending on your Goodays configuration.

From these categories, you can calculate the customer satisfaction score distributed by region, business unit, brand, etc.

The category ID to be used is returned by the endpoint [/levels](ref:levels_list-1), in the "category_id" attribute.

See "[By level category](customer-satisfaction-score#by-level-category-1)" use case.

# Use cases

Here are some examples to show you the possibilities of this endpoint. This is obviously not exhaustive, it's up to you to have fun to find the right parameter arrangements :)

## By establishment over the month of May 2020

I have to use the following parameters :

- begin : the first date of the month of May
- end : the last date of the month of May
- by : group calculation by "place"

```curl
curl --location --request GET 'https://api.goodays.co/v2/stats/satisfaction? \
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
            "key": "bwdQ661e4Q",
            "description": "VÉLO Chambéry (Chambéry) - velo-chambery",
            "average": 4.159793343117506,
            "ratings_count": 24818,
            "responses_count": 7585
        },
        {
            "key": "bQdPLrmwd9",
            "description": "VÉLO Berlin (Berlin) - velo-berlin",
            "average": 3.802727568394556,
            "ratings_count": 19633,
            "responses_count": 3352
        },
        {
            "key": "My4lvMpK8R",
            "description": "VÉLO London (London) - velo-london",
            "average": 4.499930739652768,
            "ratings_count": 1572,
            "responses_count": 270
        },
        {
            "key": "egxK551kdo",
            "description": "VÉLO Brest (Brest) - velo-brest",
            "average": 4.1271768709984595,
            "ratings_count": 3280,
            "responses_count": 567
        },
        {
            "key": "yLdLD9NKdj",
            "description": "VÉLO Glasgow (Glasgow) - velo-glasgow",
            "average": 4.1271768709984595,
            "ratings_count": 2817,
            "responses_count": 496
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

```curl Satisfaction call
curl --location --request GET 'https://api.goodays.co/v2/stats/satisfaction? \
email=max.guevara@angel.com' \
--header 'Content-Type: application/json' \
--header 'Authorization: 1234abcd1234abcd1234abcd1234abcd'
```

```json Customer-Satisfaction Score by place for one End Customer
{
    "data": [
        {
            "key": null,
            "description": null,
            "average": 3.5136054421768708,
            "ratings_count": 71,
            "responses_count": 12
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

```curl Satisfaction call
curl --location --request GET 'https://api.goodays.co/v2/stats/satisfaction? \
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
            "key": "2020-01",
            "description": "2020-01",
            "average": 4.067802221803097,
            "ratings_count": 4332,
            "responses_count": 649
        },
        {
            "key": "2020-02",
            "description": "2020-02",
            "average": 4.1641412359309324,
            "ratings_count": 1456,
            "responses_count": 233
        },
        {
            "key": "2020-03",
            "description": "2020-03",
            "average": 4.216741811186759,
            "ratings_count": 423,
            "responses_count": 64
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

_Hypothesis: additional informations exist in your configuration and is present in every response._ 

```curl Satisfaction call
curl --location --request GET 'https://api.goodays.co/v2/stats/satisfaction?by_context=price' \
--header 'Content-Type: application/json' \
--header 'Authorization: 1234abcd1234abcd1234abcd1234abcd'
```

```json Customer-Satisfaction Score by month for one one level and a specific source
{
    "data": [
        {
            "key": "3Q54E78yD9",
            "description": "Entre 500 et 1000€",
            "average": 3.3475125435071256,
            "ratings_count": 876,
            "responses_count": 326
        },
        {
            "key": "lZmxo9dj6G",
            "description": "Entre 200 et 500€",
            "average": 3.2930732905697893,
            "ratings_count": 473,
            "responses_count": 176
        },
        {
            "key": "NEexq5xYzW",
            "description": "Supérieur à 1000€",
            "average": 4.446379198143904,
            "ratings_count": 457,
            "responses_count": 155
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

\_Hypothesis: in our configuration the level category "2" corresponds to our level "\_regions\*".

```curl Satisfaction call
curl --location --request GET 'https://api.goodays.co/v2/stats/satisfaction?by_level_category=5' \
--header 'Content-Type: application/json' \
--header 'Authorization: 1234abcd1234abcd1234abcd1234abcd'
```

```json Customer-Satisfaction Score by level category
{
    "data": [
        {
            "key": "1P8Blka4jX",
            "description": "France",
            "average": 3.475416518244089,
            "ratings_count": 10799,
            "responses_count": 3345
        },
        {
            "key": "pe8N9zNxjK",
            "description": "Deutschland",
            "average": 3.3621418112980908,
            "ratings_count": 1240,
            "responses_count": 455
        },
        {
            "key": "158y1QN8wN",
            "description": "United Kingdom",
            "average": 3.4691652415222634,
            "ratings_count": 608,
            "responses_count": 229
        },
        {
            "key": "Qr43jwjdVY",
            "description": "United Kingdom",
            "average": 3.8333333333333335,
            "ratings_count": 21,
            "responses_count": 7
        }
    ]
}
```

> 📘 Zoom on "by_level_category" parameter
> 
> Here the "by_level_category" distributes the calculation by level category. The attribute "key" contains the ID of the level and the "description" the level name.