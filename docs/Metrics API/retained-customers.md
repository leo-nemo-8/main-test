---
title: Retained Customers
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
> A Retained Customer is a customer who has expressed dissatisfaction and has been identified as "at risk". After the local manager's response, this customer indicated that he was satisfied with the treatment of his dissatisfaction and considered returning to the place. The local manager's action thus prevented this customer from churn.

> 👍 Going further
>
> Consult the [general Metrics API documentation](/docs/exploit-the-full-potential-of-your-data) for more.

<Image align="center" width="smart" src="https://files.readme.io/4b2692c-ChurnReduction0.5x.png" />

# How do I get my Retained Customers metrics?

With [/stats/stats\_retained\_customers\_list](ref:retained_customers):

```curl Satisfaction call
curl --location --request GET 'https://api.goodays.co/v2/stats/retained_customers' \
--header 'Content-Type: application/json' \
--header 'Authorization: 1234abcd1234abcd1234abcd1234abcd'
```

```json Sample Satisfaction
{
    "data": [
        {
            "key": null,
            "description": null,
            "retained_customers_count": 80,
            "retained_customers_percentage": 66.66666666666666,
            "customers_responding_count": 120
        }
    ]
}
```

By default the calculation of the score is done "since always".\
And the return will always contain:

| Attribute                           | Description                                                                                                                         |
| :---------------------------------- | :---------------------------------------------------------------------------------------------------------------------------------- |
| **key**                             | Distribution key ID.                                                                                                                |
| **description**                     | Description of the distribution key.                                                                                                |
| **retained\_customers\_count**      | Total number of End Customers who are satisfied with the Local Manager's response and planned to return to the place.               |
| **retained\_customers\_percentage** | Percentage of total number of End Customers who are satisfied with the Local Manager's response and planned to return to the place. |
| **customers\_responding\_count**    | Total number of End Customers responding to the question about coming back to the place                                             |

> 📘 Zoom on "key" and "description" attribute
>
> This attributes are only filled in when "by", "by\_context" or "by\_level\_category" is used.\
> Otherwise they have the value `null`.

# Add some filters

It is possible to add GET parameters to refine the calculation of the dissatisfaction results over a defined period, a place...

## GET parameters

To filter the Retain Customers results, it is possible to combine the following GET parameters:

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
        Start date of the calculation period.\
        *Format : YYYY-MM-DDThh:mm:ssZ*\
        See [this page](doc:timezone-management) for the timezone management.
      </td>
    </tr>

    <tr>
      <td>
        **end**
      </td>

      <td>
        End date of the calculation period.\
        *Format : YYYY-MM-DDThh:mm:ssZ*\
        See [this page](doc:timezone-management) for the timezone management.
      </td>
    </tr>

    <tr>
      <td>
        **place** 
      </td>

      <td>
        Filter on an establishment.\
        *It is necessary to indicate the ID of the establishment from the endpoint[/places](ref:places_list)*
      </td>
    </tr>

    <tr>
      <td>
        **places** 
      </td>

      <td>
        Filter on an establishment list.\
        *Format : Establishment IDs separated by commas*
      </td>
    </tr>

    <tr>
      <td>
        **level** 
      </td>

      <td>
        Filter on a level.\
        *It is necessary to indicate the ID of the establishment from the endpoint[/levels](ref:levels_list)*
      </td>
    </tr>

    <tr>
      <td>
        **levels** 
      </td>

      <td>
        Filter on a level list.\
        *Format : Level IDs separated by commas*
      </td>
    </tr>

    <tr>
      <td>
        **survey**
      </td>

      <td>
        filter on a survey.\
        *It is necessary to indicate the ID of the question from the endpoint[/surveys](ref:surveys_list)*
      </td>
    </tr>

    <tr>
      <td>
        **question** 
      </td>

      <td>
        Filter on a question.\
        *It is necessary to indicate the ID of the question from the endpoint[/surveys](ref:surveys_list)*
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
        **remark\_type** 
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
        Filter on source : "critizr", "email", "facebook", "google", "sms", "tripadvisor", "widget", "wifi".
      </td>
    </tr>

    <tr>
      <td>
        **by** 
      </td>

      <td>
        Group calculations by.\
        See chapter [by](dissatisfaction#by)
      </td>
    </tr>

    <tr>
      <td>
        **by\_context** 
      </td>

      <td>
        Group calculations by Additional Information.\
        See chapter [by Context](dissatisfaction#by-context)
      </td>
    </tr>

    <tr>
      <td>
        **by\_level\_category** 
      </td>

      <td>
        Group calculations by level category.\
        See chapter [by Level Category](dissatisfaction#by-level-category)
      </td>
    </tr>
  </tbody>
</Table>

> 📘 Get an updated list of values for the "source" parameter
>
> The examples listed for the "source" parameter are not exhaustive. To obtain an exhaustive list, the endpoint [/stats/retained-customers](ref:dissatisfaction) must be called by indicating an unexpected value. In return the error message will list all possible values.

## Group calculations

The three "by" parameters allow you to retrieve a list of results aggregated according to the value selected in the input.

> 📘 Combine the "by" or not combine the "by" ?
>
> You can combine several other GET parameters with a "by" but you can not combine the filters "by", "by\_context" and "by\_level\_category" in a single request. Only one aggregation parameter is allowed.

Here are the 3 possibilities :

### By

Refine the calculation of the Retained Customers results by grouping elements and return a list.

The distribution of the calculation can be by : "day", "month", "nps\_category", "place", "quarter", "remark\_type", "source", "survey", "year".

See "[By establishment over the month of May 2020](retained-customers#by-establishment-over-the-month-of-may-2020)" or [By month for one level and a specific source](retained-customers#by-month-for-one-level-and-a-specific-source) use cases.

### By Context

Refine the calculation of the Retained Customers results for each value of the "Additional Information" passed as a parameter and returns a list.

"Additional Information" is additional data attached to a response to give a better understanding about the context.

The list of "Additional Information" available depends on your Goodays configuration and can be retrieved by the endpoint [configuration](ref:configuration_list). The only 'Additional Information" usable with this parameter are the one with the field *"use\_in\_stats" = true*.

See "[By context of the purchase amount](dissatisfaction#by-context-of-the-purchase-amount)" use case.

### By Level Category

Refine the calculation of the Retained Customers results by level category and return a list.

The categories represent your hierarchical or geographical organization depending on your Goodays configuration.

From these categories, you can calculate the customer satisfaction score distributed by region, business unit, brand, etc.

The category ID to be used is returned by the endpoint [/levels](ref:levels_list), in the "category\_id" attribute.

See "[By level category](retained-customers#by-level-category-1)" use case.

# Use cases

Here are some examples to show you the possibilities of this endpoint. This is obviously not exhaustive, it's up to you to have fun to find the right parameter arrangements :)

## By establishment over the month of May 2020

I have to use the following parameters :

* begin : the first date of the month of May
* end : the last date of the month of May
* by : group calculation by "place"

```curl
curl --location --request GET 'https://api.goodays.co/v2/stats/retained-customers? \
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
            "key": "mj8133D64R",
            "description": "VÉLO Annecy (Annecy) - velo-annecy",
            "retained_customers_count": 2,
            "retained_customers_percentage": 50.0,
            "customers_responding_count": 4
        },
        {
            "key": "qz4RZZM94r",
            "description": "VÉLO Aix-en-Provence (Aix-en-Provence) - velo-aix-en-provence",
            "retained_customers_count": 2,
            "retained_customers_percentage": 50.0,
            "customers_responding_count": 4
        }
    ]
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

*Hypothesis: in our configuration the level ID "Yqxzp5Ad2J" corresponds to our level "South France"*

```curl Satisfaction call
curl --location --request GET 'https://api.goodays.co/v2/stats/retained_customers? \
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
            "description": "2021-07",
            "retained_customers_count": 4,
            "retained_customers_percentage": 36.36363636363637,
            "customers_responding_count": 11
        },
        {
            "key": "2021-08",
            "description": "2021-08",
            "retained_customers_count": 6,
            "retained_customers_percentage": 75.0,
            "customers_responding_count": 8
        },
        {
            "key": "2021-09",
            "description": "2021-09",
            "retained_customers_count": 8,
            "retained_customers_percentage": 80.0,
            "customers_responding_count": 10
        },
        {
            "key": "2021-10",
            "description": "2021-10",
            "retained_customers_count": 7,
            "retained_customers_percentage": 46.666666666666664,
            "customers_responding_count": 15
        },
        {
            "key": "2021-11",
            "description": "2021-11",
            "retained_customers_count": 3,
            "retained_customers_percentage": 50.0,
            "customers_responding_count": 6
        }
    ]
}
```

> 📘 Zoom on "by" parameter
>
> The attributes "key" and "description" both contain the relevant year and month.

## By context of the purchase amount

I have to use the following parameters :

* by\_context : "advisor"

*Hypothesis: additional informations exist in your configuration and is present in every response.* 

```curl Satisfaction call
curl --location --request GET 'https://api.goodays.co/v2/stats/retained-customers?by_context=advisor' \
--header 'Content-Type: application/json' \
--header 'Authorization: 1234abcd1234abcd1234abcd1234abcd'
```

```json Customer-Satisfaction Score by month for one one level and a specific source
{
    "data": [
        {
            "key": "ryLdLpdj1e",
            "description": "Nizar",
            "retained_customers_count": 60,
            "retained_customers_percentage": 61.855670103092784,
            "customers_responding_count": 97
        },
        {
            "key": "ap4MPA1wd2",
            "description": "Jeanne",
            "retained_customers_count": 12,
            "retained_customers_percentage": 92.3076923076923,
            "customers_responding_count": 13
        },
        {
            "key": "BQe4Zoxprb",
            "description": "Clémence",
            "retained_customers_count": 1,
            "retained_customers_percentage": 100.0,
            "customers_responding_count": 1
        }
    ]
}
```

> 📘 Zoom on "by\_context" parameter
>
> Here the "by\_context" distributes the calculation by additional information "price". The attribute "key" contains the ID of the additional information and the "description" its name.

## By level category

I have to use the following parameters :

* by\_level\_category : "2"

\_Hypothesis: in our configuration the level category "2" refers to our level "\_regions\*".

```curl Satisfaction call
curl --location --request GET 'https://api.goodays.co/v2/stats/retained-customers?by_level_category=5' \
--header 'Content-Type: application/json' \
--header 'Authorization: 1234abcd1234abcd1234abcd1234abcd'
```

```json Customer-Satisfaction Score by level category
{
    "data": [
        {
            "key": "ryLdLpdj1e",
            "description": "France",
            "retained_customers_count": 60,
            "retained_customers_percentage": 61.855670103092784,
            "customers_responding_count": 97
        },
        {
            "key": "ap4MPA1wd2",
            "description": "Germany",
            "retained_customers_count": 12,
            "retained_customers_percentage": 92.3076923076923,
            "customers_responding_count": 13
        },
        {
            "key": "BQe4Zoxprb",
            "description": "United Kingdom",
            "retained_customers_count": 1,
            "retained_customers_percentage": 100.0,
            "customers_responding_count": 1
        }
    ]
}
```

> 📘 Zoom on "by\_level\_category" parameter
>
> Here the "by\_level\_category" distributes the calculation by level category. The attribute "key" contains the ID of the level and the "description" the level name.
