---
title: CES - Customer Effort Score
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
> The CES (**Customer Effort Score**) measures the **effort perceived by the end customer** during a key interaction: solving a problem, completing a procedure, using a digital journey, or ordering a product or service.
>
> The end customer is asked whether they agree with a statement, for example:  
> “It was easy to return my product.”  
> The answer is on a scale of 1 (_Strongly disagree_) to 7 (_Strongly agree_). A high score always means a low effort.
>
> The CES is used to sort answers into three effort levels:
>
> * “**HIGH EFFORT**”, for a score between 1 and 3
> * “**MODERATE EFFORT**”, for a score of 4 or 5
> * “**LOW EFFORT**”, for a score of 6 or 7
>
> _That score can then be analyzed over any period of time or the focus can be narrowed to any given survey, a particular POS or any other analysis filter you wish to apply._

> 👍 Going further
>
> Consult the [general Metrics API documentation](/docs/exploit-the-full-potential-of-your-data) for more.

# How do I get my CES?

With [/stats/ces](ref:stats_ces_list):

```curl ces call
curl --location --request GET 'https://api.goodays.co/v2/stats/ces' \
--header 'Content-Type: application/json' \
--header 'Authorization: 1234abcd1234abcd1234abcd1234abcd'
```

```json Sample CES
{
    "data": [
        {
            "key": null,
            "description": null,
            "count": 200,
            "avg": 5.6,
            "high_effort": {
                "count": 30,
                "percentage": 15.0
            },
            "moderate_effort": {
                "count": 40,
                "percentage": 20.0
            },
            "low_effort": {
                "count": 130,
                "percentage": 65.0
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
        Number of answers to "CES" questions in the selection over the requested period.  
        _This is a number of answers, not of participations: see below._
      </td>
    </tr>

    <tr>
      <td>
        **avg**
      </td>

      <td>
        Average CES score, out of 7.  
        Calculated on all the answers of the selection, not as an average of the averages of each establishment.
      </td>
    </tr>

    <tr>
      <td>
        **high_effort**
      </td>

      <td>
        Answers to "CES" questions with a score of 1 to 3.
      </td>
    </tr>

    <tr>
      <td>
        **moderate_effort**
      </td>

      <td>
        Answers to "CES" questions with a score of 4 or 5.
      </td>
    </tr>

    <tr>
      <td>
        **low_effort**
      </td>

      <td>
        Answers to "CES" questions with a score of 6 or 7.
      </td>
    </tr>

    <tr>
      <td>
        **count**
      </td>

      <td>
        Number of answers to "CES" questions observed over the requested period for the high, moderate or low effort level.
      </td>
    </tr>

    <tr>
      <td>
        **percentage**
      </td>

      <td>
        Percentage of answers to "CES" questions observed over the requested period for the high, moderate or low effort level.  
        `low_effort.percentage` is the main CES KPI displayed in Goodays: the % of customers who find the effort low.
      </td>
    </tr>
  </tbody>
</Table>

> 📘 Zoom on "key" and "description" attribute
>
> This attributes are only filled in when "by", "by_context" or "by_level_category" is used.  
> Otherwise they have the value `null`.

> 🚧 Answers, not participations
>
> Unlike the NPS, a survey can contain **several CES questions** (for example one on the website and one on Customer Service). The CES is therefore calculated on **answers**: a participation that contains two CES questions counts as two answers in `count` and in the effort levels.
>
> When your selection contains several CES questions, they are aggregated. To analyse one CES question on its own, use the `question` parameter.

# Add some filters

It is possible to add GET parameters to refine the calculation of the score over a defined period, an establishment...

## GET parameters

To calculate a CES, it is possible to combine the following GET parameters:

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
        See [this page](doc:timezone-and-date-management) for the timezone management.
      </td>
    </tr>

    <tr>
      <td>
        **end**
      </td>

      <td>
        End date of the calculation period.  
        _Format : YYYY-MM-DDThh:mm:ssZ_  
        See [this page](doc:timezone-and-date-management) for the timezone management.
      </td>
    </tr>

    <tr>
      <td>
        **place**
      </td>

      <td>
        Filter on an establishment.  
        _It is necessary to indicate the ID of the establishment from the endpoint [/places](ref:places_list)_
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
        _It is necessary to indicate the ID of the level from the endpoint [/levels](ref:levels_list)_
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
        Filter on a survey.  
        _It is necessary to indicate the ID of the survey from the endpoint [/surveys](ref:surveys_list)_
      </td>
    </tr>

    <tr>
      <td>
        **question**
      </td>

      <td>
        Filter on a question, for example to isolate one CES question.  
        _It is necessary to indicate the ID of the question from the endpoint [/surveys](ref:surveys_list)_
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
        Filter on source : "email", "sms", "widget", "wifi"...
      </td>
    </tr>

    <tr>
      <td>
        **by**
      </td>

      <td>
        Group calculations by.  
        See chapter [by](ces-score#by)
      </td>
    </tr>

    <tr>
      <td>
        **by_context**
      </td>

      <td>
        Group calculations by Additional Information.  
        See chapter [by Context](ces-score#by-context)
      </td>
    </tr>

    <tr>
      <td>
        **by_level_category**
      </td>

      <td>
        Group calculations by level category.  
        See chapter [by Level Category](ces-score#by-level-category)
      </td>
    </tr>
  </tbody>
</Table>

> 📘 Get an updated list of values for the "source" parameter
>
> The examples listed for the "source" parameter are not exhaustive. To obtain an exhaustive list, the endpoint [/stats/ces](ref:stats_ces_list) must be called by indicating an unexpected value. In return the error message will list all possible values.

## Group calculations

The three "by" parameters allow you to retrieve a list of results aggregated according to the value selected in the input.

> 📘 Combine the "by" or not combine the "by" ?
>
> You can combine several other GET parameters with a "by" but you can not combine the filters "by", "by_context" and "by_level_category" in a single request. Only one aggregation parameter is allowed.

Here are the 3 possibilities:

### By

Calculate the CES by grouping elements and return a list.

The distribution of the calculation can be by : "day", "month", "place", "quarter", "remark_type", "source", "survey", "year".

See "[By establishment over the month of May 2026](ces-score#by-establishment-over-the-month-of-may-2026)" use case.

### By Context

Calculate the CES for each value of the "Additional Information" passed as a parameter and return a list.

"Additional Information" is data attached to a response to give a better understanding about the context.

The list of Additional Information available depends on your Goodays configuration and can be retrieved by the endpoint [configuration](ref:configuration_list). The only 'Additional Information" usable with this parameter are the one with the field  _"use_in_stats" = true_.

### By Level Category

Calculate the CES by level category and return a list.

The categories represent your hierarchical or geographical organization depending on your Goodays configuration.

From these categories you can calculate the CES distributed by region, business unit, brand, etc.

The category ID to be used is returned by the endpoint [/levels](ref:levels_list), in the "category_id" attribute.

# Use cases

Here are some examples to show you the possibilities of this endpoint. This is obviously not exhaustive, it's up to you to have fun to find the right parameter arrangements :)

## By establishment over the month of May 2026

I have to use the following parameters :

* begin : the first date of the month of May
* end : the last date of the month of May
* by : group calculation by "place"

```curl CES call
curl --location --request GET 'https://api.goodays.co/v2/stats/ces? \
   begin=2026-05-01T00:00:00Z \
   &end=2026-05-31T23:59:00Z \
   &by=place' \
--header 'Content-Type: application/json' \
--header 'Authorization: 1234abcd1234abcd1234abcd1234abcd'
```

```json CES by place on the month of May 2026
{
    "data": [
        {
            "key": "egxK551kdo",
            "description": "VÉLO Brest (Brest)",
            "count": 120,
            "avg": 5.9,
            "high_effort": {
                "count": 12,
                "percentage": 10.0
            },
            "moderate_effort": {
                "count": 18,
                "percentage": 15.0
            },
            "low_effort": {
                "count": 90,
                "percentage": 75.0
            }
        },
        {
            "key": "bQdPLrmwd9",
            "description": "VÉLO Chambéry (Chambéry) - velo-chambery",
            "count": 80,
            "avg": 5.1,
            "high_effort": {
                "count": 18,
                "percentage": 22.5
            },
            "moderate_effort": {
                "count": 22,
                "percentage": 27.5
            },
            "low_effort": {
                "count": 40,
                "percentage": 50.0
            }
        }
    ]
}
```

> 📘 Zoom on "by" parameter
>
> Here the "by" distributes the calculation by establishment. The attribute "key" contains the ID of the establishment and the "description" its name.

## One CES question by month

A survey asks two CES questions: one about the website, one about Customer Service. I want the monthly CES of the Customer Service question only.

I have to use the following parameters :

* question : ID of the CES question
* by : "month"

_Hypothesis: in our configuration the question ID "Q54E5XpK4y" is our statement "I easily got the help I needed from Customer Service."_

```curl CES call
curl --location --request GET 'https://api.goodays.co/v2/stats/ces? \
question=Q54E5XpK4y \
&by=month' \
--header 'Content-Type: application/json' \
--header 'Authorization: 1234abcd1234abcd1234abcd1234abcd'
```

```json CES by month for one question
{
    "data": [
        {
            "key": "2026-07",
            "description": "2026-07",
            "count": 64,
            "avg": 4.8,
            "high_effort": {
                "count": 16,
                "percentage": 25.0
            },
            "moderate_effort": {
                "count": 16,
                "percentage": 25.0
            },
            "low_effort": {
                "count": 32,
                "percentage": 50.0
            }
        },
        {
            "key": "2026-08",
            "description": "2026-08",
            "count": 50,
            "avg": 5.3,
            "high_effort": {
                "count": 8,
                "percentage": 16.0
            },
            "moderate_effort": {
                "count": 12,
                "percentage": 24.0
            },
            "low_effort": {
                "count": 30,
                "percentage": 60.0
            }
        }
    ]
}
```

> 📘 Zoom on "by" parameter
>
> The attributes "key" and "description" both contain the relevant year and month.
