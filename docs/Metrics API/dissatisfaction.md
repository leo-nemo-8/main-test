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

<Image align="center" border={false} width="smart" src="https://files.readme.io/124eeb3-Product_synthesis.png" />

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

<Table align={["left","left"]}>
  <thead>
    <tr>
      <th>
        Attribute
      </th>

      <th>
        Description
      </th>
    </tr>
  </thead>

  <tbody>
    <tr>
      <td>
        **key**
      </td>

      <td>
        Distribution key ID.
      </td>
    </tr>

    <tr>
      <td>
        **description**
      </td>

      <td>
        Description of the distribution key.
      </td>
    </tr>

    <tr>
      <td>
        **count**
      </td>

      <td>
        Total number of responses that triggered a dissatisfaction alert.
      </td>
    </tr>

    <tr>
      <td>
        **percentage**
      </td>

      <td>
        Percentage of total volume of responses received.
      </td>
    </tr>

    <tr>
      <td>
        **pending**
      </td>

      <td>
        * **count**: total number of dissatisfaction alert in `pending` status
        * **percentage**: Percentage of dissatisfaction alert with this status
      </td>
    </tr>

    <tr>
      <td>
        **spam**
      </td>

      <td>
        * **count**: total number of dissatisfaction alert in `spam` status
        * **percentage**: Percentage of dissatisfaction alert with this status
      </td>
    </tr>

    <tr>
      <td>
        **ignored**
      </td>

      <td>
        * **count**: total number of dissatisfaction alert in `ignored` status
        * **percentage**: Percentage of dissatisfaction alert with this status
      </td>
    </tr>

    <tr>
      <td>
        **call**
      </td>

      <td>
        * **count**: total number of dissatisfaction alert in `call` status
        * **percentage**: Percentage of dissatisfaction alerts with this status
      </td>
    </tr>

    <tr>
      <td>
        **text**
      </td>

      <td>
        * **count**: total number of dissatisfaction alert in `pending` status
        * **percentage**: Percentage of dissatisfaction alert with this status
      </td>
    </tr>
  </tbody>
</Table>

> 📘 Status
>
> Responses (with or without a dissatisfaction alert) can have different statuses:
>
> * **pending**: the processing of the response has been put on hold by the Local Manager.
> * **spam**: response was spammed by the Local Manager.
> * **ignored**: response was ignored by the Local Manager.
> * **call**: the response was processed by a call to the End Customer by the Local Manager.
> * **text**: the processing of the participation was written to the End User by the Local Manager.

> 📘 Zoom on "key" and "description" attribute
>
> These attributes are only filled in when filters "by", "by_context" or "by_level_category" are used.  
> Otherwise they have the value `null`.

# Add some filters

It is possible to add GET parameters to refine the calculation of the dissatisfaction results over a defined period, an establishment...

## GET parameters

To filter the dissatisfaction results, it is possible to combine the following GET parameters:

<Table align={["left","left"]}>
  <thead>
    <tr>
      <th>
        GET parameters
      </th>

      <th>
        Description
      </th>
    </tr>
  </thead>

  <tbody>
    <tr>
      <td>
        **begin**
      </td>

      <td>
        Start date of the calculation period.  
        _Format : YYYY-MM-DDThh:mm:ssZ_  
        See [this page](doc:timezone-management) for the timezone management.
      </td>
    </tr>

    <tr>
      <td>
        **end**
      </td>

      <td>
        End date of the calculation period.  
        _Format : YYYY-MM-DDThh:mm:ssZ_  
        See [this page](doc:timezone-management) for the timezone management.
      </td>
    </tr>

    <tr>
      <td>
        **place**
      </td>

      <td>
        Filter on an establishment.  
        _It is necessary to indicate the ID of the establishment from the endpoint[/places](ref:places_list)_
      </td>
    </tr>

    <tr>
      <td>
        **places**
      </td>

      <td>
        Filter on an establishment list.  
        _Format : Establishment IDs separated by commas_
      </td>
    </tr>

    <tr>
      <td>
        **level**
      </td>

      <td>
        Filter on a level.  
        _It is necessary to indicate the ID of the establishment from the endpoint[/levels](ref:levels_list)_
      </td>
    </tr>

    <tr>
      <td>
        **levels**
      </td>

      <td>
        Filter on a level list.  
        _Format : Level IDs separated by commas_
      </td>
    </tr>

    <tr>
      <td>
        **survey**
      </td>

      <td>
        filter on a survey.  
        _It is necessary to indicate the ID of the question from the endpoint[/surveys](ref:surveys_list)_
      </td>
    </tr>

    <tr>
      <td>
        **question**
      </td>

      <td>
        Filter on a question.  
        _It is necessary to indicate the ID of the question from the endpoint[/surveys](ref:surveys_list)_
      </td>
    </tr>

    <tr>
      <td>
        **nps**
      </td>

      <td>
        Filter on nps category : "detractor", "passive", "promoter".
      </td>
    </tr>

    <tr>
      <td>
        **remark_type**
      </td>

      <td>
        Filter on remark type : "Idea", "Message",  "Praise", "Problem", "Question".
      </td>
    </tr>

    <tr>
      <td>
        **source**
      </td>

      <td>
        Filter on source : "email", "facebook", "google", "sms", "tripadvisor", "widget", "wifi".
      </td>
    </tr>

    <tr>
      <td>
        **by**
      </td>

      <td>
        Group calculations by.  
        See chapter [by](dissatisfaction#by)
      </td>
    </tr>

    <tr>
      <td>
        **by_context**
      </td>

      <td>
        Group calculations by Additional Information.  
        See chapter [by Context](dissatisfaction#by-context)
      </td>
    </tr>

    <tr>
      <td>
        **by_level_category**
      </td>

      <td>
        Group calculations by level category.  
        See chapter [by Level Category](dissatisfaction#by-level-category)
      </td>
    </tr>
  </tbody>
</Table>

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

* begin : the first date of the month of May
* end_date : the last date of the month of May
* by : end calculation by "place"

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

* source : "email"
* level : level ID
* by : "month"

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

* by_context : "advisor"

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

* by_level_category : "2"

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
