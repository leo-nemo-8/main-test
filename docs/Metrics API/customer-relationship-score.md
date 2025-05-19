---
title: Customer-Relationship score
excerpt: ''
deprecated: false
hidden: false
metadata:
  title: customer-relationshio-score
  description: ''
  robots: index
next:
  description: ''
---
> 📘 What's that?
>
> The Customer-Relationship score is one of Goodays key performance indicators.
>
> This KPI takes three criteria into account:
>
> * **Reply rate:** Does the store respond to all these messages from customers?
> * **Reply time:** How long does it take for the store to respond to these messages?
> * **Reply quality:** Score given by your customers when they receive a response from the store.
>
> *The score displayed on the interface is updated in real time, and takes into account the messages received and processed during the month.*

> 👍 Going further
>
> Consult the [general Metrics API documentation](/docs/exploit-the-full-potential-of-your-data) for more.

<Image align="center" width="smart" src="https://files.readme.io/0485105-Customer_Relationship.png" />

# How do I get my Customer-Relationship score?

With [/stats/relationship](ref:stats_relationship_list):

```curl Relationship call
curl --location --request GET 'https://api.goodays.co/v2/stats/relationship' \
--header 'Content-Type: application/json' \
--header 'Authorization: 1234abcd1234abcd1234abcd1234abcd'
```

```json Sample Relationship
{
    "data": [
        {
            "key": null,
            "description": null,
            "reply_rate": 79.97107975717982,
            "reply_time": 182097,
            "reply_quality": 4,
            "customer_service_rating": 3.492065770743145
        }
    ]
}
```

By default the calculation of the score is done "since always".\
And the return will always contain:

| Attribute                     | Description                                                                                     |
| :---------------------------- | :---------------------------------------------------------------------------------------------- |
| **key**                       | Distribution key ID.                                                                            |
| **description**               | Description of the distribution key.                                                            |
| **reply\_rate**               | Average reply rate over the requested periods (in percentage).                                  |
| **reply\_time**               | Average reply time over the requested periods (in seconds).                                     |
| **reply\_quality**            | Average of the reply quality over the requested periods (on a scale from 1 to 5).               |
| **customer\_service\_rating** | Average of the Customer-Relationship score over the requested periods (on a scale from 1 to 5). |

> 📘 Zoom on "key" and "description" attribute
>
> This attributes are only filled in when "by", "by\_context" or "by\_level\_category" filters is used.\
> Otherwise they have the value `null`.

# Add some filters

It is possible to add GET parameters to refine the calculation of the score over a defined period, an establishment...

## GET parameters

To calculate a Customer-Relationship score it is possible to combine the following GET parameters:

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
        *Format : YYYY-MM-DDThh:mm:ss*\
        See [this page](doc:timezone-management) for the timezone management.
      </td>
    </tr>

    <tr>
      <td>
        **end**
      </td>

      <td>
        End date of the calculation period.\
        *Format : YYYY-MM-DDThh:mm:ss*\
        See [this page](doc:timezone-management) for the timezone management.
      </td>
    </tr>

    <tr>
      <td>
        **month** 
      </td>

      <td>
        Filter on a month.\
        **Format : YYYY-MM**
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
        *It is necessary to indicate the ID of the level from the endpoint[/levels](ref:levels_list)*
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
        **by** 
      </td>

      <td>
        Group calculations by.\
        See chapter [by](customer-relationship-score#by)
      </td>
    </tr>

    <tr>
      <td>
        **by\_level\_category** 
      </td>

      <td>
        Group calculations by level category.\
        See chapter [by Level Category](customer-relationship-score#by-level-category)
      </td>
    </tr>
  </tbody>
</Table>

## Group calculations

The two "by" parameters allow you to retrieve a list of results aggregated according to the value selected in the input.

> 📘 Combine the "by" or not combine the "by" ?
>
> You can combine several other GET parameters with a "by" but you can not combine the filters "by" and "by\_level\_category" in a single request. Only one aggregation parameter is allowed.

Here are the 2 possibilities :

### By

Calculate the Customer-Relationship score by grouping elements and return a list.

The distribution of the calculation can be by : "month" or "place".

See "[By establishment over the month of May 2020](customer-relationship-score#by-establishment-over-the-month-of-may-2020)" or [By month for one level and a specific source](customer-relationship-score#by-month-for-one-level-and-a-specific-source) use cases.

### By Level Category

Calculate the Customer-Relationship score by level category and return a list.

The categories represent your hierarchical or geographical organization depending on your Goodays configuration.

From these categories, you can calculate the Customer-Relationship score distributed by region, business unit, brand, etc.

The category ID to be used is returned by the endpoint [/levels](ref:levels_list), in the "category\_id" attribute.

See "[By level category](customer-relationship-score#by-level-category-1)" use case.

# Use cases

Here are some examples to show you the possibilities of this endpoint. This is obviously not exhaustive, it's up to you to have fun to find the right parameter arrangements :)

## By establishment over the month of May 2020

I have to use the following parameters :

* begin : the first date of the month of May
* end : the last date of the month of May
* by : group calculation by "place"

```curl Relationship call
curl --location --request GET 'https://api.goodays.co/v2/stats/relationship? \
   begin=2020-05-01T00:00:00Z \
   &end=2020-05-31T23:59:00Z \
   &by=place' \
--header 'Content-Type: application/json' \
--header 'Authorization: 1234abcd1234abcd1234abcd1234abcd'
```

```json Relationship call by place on the last month
{
    "data": [
        {
            "key": "bwdQ661e4Q",
            "description": "VÉLO Chambéry (Chambéry) - velo-chambery",
            "reply_rate": 92.94380936799226,
            "reply_time": 268754,
            "reply_quality": 4,
            "customer_service_rating": 3.8769743089322692
        },
        {
            "key": "bQdPLrmwd9",
            "description": "VÉLO Chambéry (Chambéry) - velo-chambery",
            "reply_rate": 90.31051211886935,
            "reply_time": 183065,
            "reply_quality": 3,
            "customer_service_rating": 2.813058822243302
        }
    ]
}
```

> 📘 Zoom on "by" parameter
>
> Here the "by" distributes the calculation by establishment. The attribute "key" contains the ID of the establishment and the "description" its name.

## By month for one level

I have to use the following parameters:

* level : level ID
* by : "month"

```curl Relationship call
curl --location --request GET 'https://api.goodays.co/v2/stats/relationship? \
level=Yqxzpde42J \
&by=month' \
--header 'Content-Type: application/json' \
--header 'Authorization: 1234abcd1234abcd1234abcd1234abcd'
```

```json Customer-Relationship score by month for one one level and a specific source
{
    "data": [
        {
            "key": "2020-02",
            "description": "2020-02",
            "reply_rate": 92.94380936799226,
            "reply_time": 268754,
            "reply_quality": 4,
            "customer_service_rating": 3.8769743089322692
        },
        {
            "key": "2020-03",
            "description": "2020-03",
            "reply_rate": 90.31051211886935,
            "reply_time": 183065,
            "reply_quality": 4,
            "customer_service_rating": 3.999658743540446
        },
        {
            "key": "2020-04",
            "description": "2020-04",
            "reply_rate": 0.0,
            "reply_time": null,
            "reply_quality": null,
            "customer_service_rating": 0.0
        },
        {
            "key": "2020-05",
            "description": "2020-05",
            "reply_rate": 89.02530811451099,
            "reply_time": 148004,
            "reply_quality": 4,
            "customer_service_rating": 3.813058822243302
        },
        {
            "key": "2020-06",
            "description": "2020-06",
            "reply_rate": 85.74929527000144,
            "reply_time": 123273,
            "reply_quality": 4,
            "customer_service_rating": 3.7839863476929843
        }
    ]
}
```

> 📘 Zoom on "by" parameter
>
> The attributes "key" and "description" both contain the relevant year and month.

## By level category

I have to use the following parameters :

* by\_level\_category : "9"

\_Hypothesis: in our configuration the level category "9" corresponds to our level "\_regions\*".

```curl Relationship call
curl --location --request GET 'https://api.goodays.co/v2/stats/relationship?by_level_category=9' \
--header 'Content-Type: application/json' \
--header 'Authorization: 1234abcd1234abcd1234abcd1234abcd'
```

```json Customer-Rlationship Score by level category
{
    "data": [
        {
            "key": "1P8Blka4jX",
            "description": "France",
            "reply_rate": 92.94380936799226,
            "reply_time": 268754,
            "reply_quality": 4,
            "customer_service_rating": 3.8769743089322692
        },
        {
            "key": "pe8N9zNxjK",
            "description": "Deutschland",
            "reply_rate": 92.94380936799226,
            "reply_time": 268754,
            "reply_quality": 4,
            "customer_service_rating": 3.8769743089322692
        },
        {
            "key": "158y1QN8wN",
            "description": "United Kingdom",
            "reply_rate": 92.94380936799226,
            "reply_time": 268754,
            "reply_quality": 4,
            "customer_service_rating": 3.8769743089322692
        }
    ]
}
```

> 📘 Zoom on "by\_level\_category" parameter
>
> Here the "by\_level\_category" distributes the calculation by level category. The attribute "key" contains the ID of the level and the "description" the level name.
