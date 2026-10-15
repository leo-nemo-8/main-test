---
title: Remark types
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
> The remark type is the category of the verbatim left by the end customer: **Idea**, **Praise**, **Problem** or **Question**.
>
> The exchanges between a pro user and the end customer after the first verbatim are typed as "Message".

> 👍 Going further
>
> Consult the [general Metrics API documentation](/docs/exploit-the-full-potential-of-your-data) for more.

<Image border={false} src="https://files.readme.io/ec4c833-Constructive_Conversations.png" title="Constructive Conversations.png" />

# How do I get my remark type metrics?

With [/stats/remarks](ref:stats_remarks_list):

```curl Remarks call
curl --location --request GET 'https://api.goodays.co/v2/stats/remarks' \
--header 'Content-Type: application/json' \
--header 'Authorization: 1234abcd1234abcd1234abcd1234abcd'
```

```json Sample Remarks
{
    "data": [
        {
            "key": null,
            "description": null,
            "count": 150397,
            "Idea": {
                "count": 36094,
                "percentage": 23.999148919193868
            },
            "Praise": {
                "count": 80626,
                "percentage": 53.60878209006829
            },
            "Problem": {
                "count": 28532,
                "percentage": 18.971123094210657
            },
            "Question": {
                "count": 4734,
                "percentage": 3.147669168932891
            },
            "Message": {
                "count": 411,
                "percentage": 0.27327672759430044
            }
        }
    ]
}
```

By default the calculation of the score is done "since always".  
And the return will always contain:

| Attribute       | Description                                                                                                                             |
| :-------------- | :-------------------------------------------------------------------------------------------------------------------------------------- |
| **key**         | Distribution key ID.                                                                                                                    |
| **description** | Description of the distribution key.                                                                                                    |
| **count**       | Number of participations in the selection over the requested period.                                                                    |
| **Idea**        | Participations with a verbatim of type "Idea".                                                                                         |
| **Praise**      | Participations with a verbatim of type "Praise".                                                                                       |
| **Problem**     | Participations with a verbatim of type "Problem".                                                                                      |
| **Question**    | Participations with a verbatim of type "Question".                                                                                     |
| **Message**     | Exchanges between a pro user and the end customer after the first verbatim.   |
| **count**       | Number of participations for the remark type observed over the requested periods for the Idea, Praise, Problem, Question or Message.     |
| **percentage**  | Percentage of participations for the remark type observed over the requested periods for the Idea, Praise, Problem, Question or Message. |

> 📘 Zoom on "key" and "description" attribute
>
> This attributes are Only filled in when "by", "by_context" or "by_level_category" is used.  
> Otherwise they have the value `null`.

# Add some filters

It is possible to add GET parameters to refine the calculation of the score over a defined period, a point of sale...

## GET parameters

To calculate remark type metrics it is possible to combine the following GET parameters:

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
        Filter on a point of sale.  
        _It is necessary to indicate the Place ID from the endpoint [/places](ref:places_list)._
      </td>
    </tr>

    <tr>
      <td>
        **places**
      </td>

      <td>
        Filter on a list of points of sale.  
        _Format : Place IDs separated by commas._
      </td>
    </tr>

    <tr>
      <td>
        **level**
      </td>

      <td>
        Filter on a level.  
        _It is necessary to indicate the ID of the level from the endpoint [/levels](ref:levels_list)._
      </td>
    </tr>

    <tr>
      <td>
        **levels**
      </td>

      <td>
        Filter on a level list.  
        _Format : Level IDs separated by commas._
      </td>
    </tr>

    <tr>
      <td>
        **survey**
      </td>

      <td>
        filter on a survey.  
        _It is necessary to indicate the ID of the question from the endpoint[/surveys](ref:surveys_list)._
      </td>
    </tr>

    <tr>
      <td>
        **question**
      </td>

      <td>
        Filter on a question.  
        _It is necessary to indicate the ID of the question from the endpoint[/surveys](ref:surveys_list)._
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
        **context_**
      </td>

      <td>
        Filter on a value of a custom parameter.  
        _To construct this parameter you need to concatenate the prefix`context_`and one of the`key` attribute returned by the endpoint [/configuration](ref:configuration_list)._

        See the :information_source: block below.
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
        See chapter [by](remarks#by).
      </td>
    </tr>

    <tr>
      <td>
        **by_context**
      </td>

      <td>
        Group calculations by custom parameter.  
        See chapter [by Context](remarks#by-context).
      </td>
    </tr>

    <tr>
      <td>
        **by_level_category**
      </td>

      <td>
        Group calculations by level category.  
        See chapter [by Level Category](remarks#by-level-category).
      </td>
    </tr>
  </tbody>
</Table>

> 📘 Get an updated list of values for the "context_" parameter
>
> A custom parameter is additional data attached to a participation to describe its context (order date, purchase amount, advisor...).
>
> The list of your custom parameters depends on your Goodays configuration and can be retrieved by the endpoint [configuration](ref:configuration_list). Only the custom parameters with the field _"use_in_stats" = true_ can be used with this parameter.
>
> See "[By context of the purchase amount](remarks#by-context-of-the-purchase-amount)" use case.

> 📘 Get an updated list of values for the "source" parameter
>
> The examples listed for the "source" parameter are not exhaustive. To obtain an exhaustive list, the endpoint [/stats/remarks](ref:stats_remarks_list) must be called by indicating an unexpected value. In return the error message will list all possible values.

## Group calculations

The three "by" parameters allow you to retrieve a list of results aggregated according to the value selected in the input.

> 📘 Combine the "by" or not combine the "by" ?
>
> You can combine several other GET parameters with a "by" but you can not combine the filters "by", "by_context" and "by_level_category" in a single request. Only one aggregation parameter is allowed.

Here are the 3 possibilities :

### By

Calculate the remark type metrics by grouping elements and return a list.

The distribution of the calculation can be by : "day", "month", "nps_category", "place", "quarter", "remark_type", "source", "survey", "year".

See "[By point of sale over the month of May 2020](remarks#by-point-of-sale-over-the-month-of-may-2020)" or [By month for one level and a specific source](remarks#by-month-for-one-level-and-a-specific-source) use cases.

### By Context

Calculate the remark type metrics for each value of the custom parameter passed as a parameter and return a list.

A custom parameter is additional data attached to a participation to describe its context (order date, purchase amount, advisor...).

The list of your custom parameters depends on your Goodays configuration and can be retrieved by the endpoint [configuration](ref:configuration_list). Only the custom parameters with the field _"use_in_stats" = true_ can be used with this parameter.

See "[By context of the purchase amount](remarks#by-context-of-the-purchase-amount)" use case.

### By Level Category

Calculate the remark type metrics by level category and return a list.

The categories represent your hierarchical or geographical organization depending on your Goodays configuration.

From these categories, you can calculate the remark type metrics distributed by region, business unit, brand, etc.

The category ID to be used is returned by the endpoint [/levels](ref:levels_list), in the "category_id" attribute.

See "[By level category](remarks#by-level-category-1)" use case.

# Use cases

Here are some examples to show you the possibilities of this endpoint. This is obviously not exhaustive, it's up to you to have fun to find the right parameter arrangements :)

## By point of sale over the month of May 2020

I have to use the following parameters :

* begin : the first date of the month of May
* end : the last date of the month of May
* by : group calculation by "place"

```curl Remarks call
curl --location --request GET 'https://api.goodays.co/v2/stats/remarks? \
   begin=2020-05-01T00:00:00Z \
   &end=2020-05-31T23:59:00Z \
   &by=place' \
--header 'Content-Type: application/json' \
--header 'Authorization: 1234abcd1234abcd1234abcd1234abcd'
```

```json Remarks by place on the last month
{
    "data": [
        {
            "key": "bwdQ661e4Q",
            "description": "VÉLO Chambéry (Chambéry) - velo-chambery",
            "count": 150397,
            "Idea": {
                "count": 36094,
                "percentage": 23.999148919193868
            },
            "Praise": {
                "count": 80626,
                "percentage": 53.60878209006829
            },
            "Problem": {
                "count": 28532,
                "percentage": 18.971123094210657
            },
            "Question": {
                "count": 4734,
                "percentage": 3.147669168932891
            },
            "Message": {
                "count": 411,
                "percentage": 0.27327672759430044
            }
        },
        {
            "key": "bQdPLrmwd9",
            "description": "VÉLO Berlin (Berlin) - velo-berlin",
            "count": 150397,
            "Idea": {
                "count": 36094,
                "percentage": 23.999148919193868
            },
            "Praise": {
                "count": 80626,
                "percentage": 53.60878209006829
            },
            "Problem": {
                "count": 28532,
                "percentage": 18.971123094210657
            },
            "Question": {
                "count": 4734,
                "percentage": 3.147669168932891
            },
            "Message": {
                "count": 411,
                "percentage": 0.27327672759430044
            }
        },
        {
            "key": "My4lvMpK8R",
            "description": "VÉLO London (London) - velo-london",
            "count": 150397,
            "Idea": {
                "count": 36094,
                "percentage": 23.999148919193868
            },
            "Praise": {
                "count": 80626,
                "percentage": 53.60878209006829
            },
            "Problem": {
                "count": 28532,
                "percentage": 18.971123094210657
            },
            "Question": {
                "count": 4734,
                "percentage": 3.147669168932891
            },
            "Message": {
                "count": 411,
                "percentage": 0.27327672759430044
            }
        }
    ]
}
```

> 📘 Zoom on "by" parameter
>
> Here the "by" distributes the calculation by point of sale. The attribute "key" contains the Place ID of the point of sale and the "description" its name.

## For one end customer

I have to use the following parameters :

* email

**Tips :** you can add the parameter "by" with the value "place" to get a distribution of this end customer's scores by point of sale.

```curl Remarks call
curl --location --request GET 'https://api.goodays.co/v2/stats/remarks? \
email=max.guevara@angel.com' \
--header 'Content-Type: application/json' \
--header 'Authorization: 1234abcd1234abcd1234abcd1234abcd'
```

```json Remarks
{
    "data": [
        {
            "key": null,
            "description": null,
            "count": 6,
            "Idea": {
                "count": 0,
                "percentage": 0
            },
            "Praise": {
                "count": 1,
                "percentage": 20
            },
            "Problem": {
                "count": 2,
                "percentage": 40
            },
            "Question": {
                "count": 0,
                "percentage": 0
            },
            "Message": {
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

## For one custom parameter

I have to use the following parameters :

* context_ : "context_service"

_Hypothesis: in our configuration we have a "Service" custom parameter with a `service` key_

```curl
curl --location --request GET 'https://api.goodays.co/v2/stats/remarks? /
	context_service=vegetables' \
--header 'Content-Type: application/json' \
--header 'Authorization: 1234abcd1234abcd1234abcd1234abcd'
```

```json
{
    "data": [
        {
            "key": null,
            "description": null,
            "count": 8379,
            "Idea": {
                "count": 771,
                "percentage": 9.201575366988902
            },
            "Message": {
                "count": 0,
                "percentage": null
            },
            "Praise": {
                "count": 4725,
                "percentage": 56.390977443609025
            },
            "Problem": {
                "count": 2596,
                "percentage": 30.98221744838286
            },
            "Question": {
                "count": 287,
                "percentage": 3.4252297410192147
            }
        }
    ]
}
```

If the value is not known an error is returned:

```curl
curl --location --request GET 'https://api.goodays.co/v2/stats/remarks? /
	context_service=vegetables' \
--header 'Content-Type: application/json' \
--header 'Authorization: 1234abcd1234abcd1234abcd1234abcd'
```

```json
{
    "context value": "Unhandled value vege for parameter context_service"
}
```

## By month for one level and a specific source

I have to use the following parameters :

* source : "email"
* level : level ID
* by : "month"

_Hypothesis: in our configuration the level ID "Yqxzp5Ad2J" corresponds to your level "South France"_

```curl Remarks call
curl --location --request GET 'https://api.goodays.co/v2/stats/remarks? \
source=email \
&level=Yqxzp5Ad2J \
&by=month' \
--header 'Content-Type: application/json' \
--header 'Authorization: 1234abcd1234abcd1234abcd1234abcd'
```

```json Remarks by month for one one level and a specific source
{
    "data": [
        {
            "key": "2020-04",
            "description": "2020-04",
            "count": 150397,
            "Idea": {
                "count": 36094,
                "percentage": 23.999148919193868
            },
            "Praise": {
                "count": 80626,
                "percentage": 53.60878209006829
            },
            "Problem": {
                "count": 28532,
                "percentage": 18.971123094210657
            },
            "Question": {
                "count": 4734,
                "percentage": 3.147669168932891
            },
            "Message": {
                "count": 411,
                "percentage": 0.27327672759430044
            }
        },
        {
            "key": "2020-05",
            "description": "2020-05",
            "count": 150397,
            "Idea": {
                "count": 36094,
                "percentage": 23.999148919193868
            },
            "Praise": {
                "count": 80626,
                "percentage": 53.60878209006829
            },
            "Problem": {
                "count": 28532,
                "percentage": 18.971123094210657
            },
            "Question": {
                "count": 4734,
                "percentage": 3.147669168932891
            },
            "Message": {
                "count": 411,
                "percentage": 0.27327672759430044
            }
        },
        {
            "key": "2020-06",
            "description": "2020-06",
            "count": 150397,
            "Idea": {
                "count": 36094,
                "percentage": 23.999148919193868
            },
            "Praise": {
                "count": 80626,
                "percentage": 53.60878209006829
            },
            "Problem": {
                "count": 28532,
                "percentage": 18.971123094210657
            },
            "Question": {
                "count": 4734,
                "percentage": 3.147669168932891
            },
            "Message": {
                "count": 411,
                "percentage": 0.27327672759430044
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

* by_context : "price"

_Hypothesis: the custom parameter exists in your configuration and is present in every participation._

```curl Remarks
curl --location --request GET 'https://api.goodays.co/v2/stats/remarks?by_context=price' \
--header 'Content-Type: application/json' \
--header 'Authorization: 1234abcd1234abcd1234abcd1234abcd'
```

```json Remarks by month for one one level and a specific source
{
    "data": [
        {
            "key": "3Q54E78yD9",
            "description": "Entre 500 et 1000€",
            "count": 150397,
            "Idea": {
                "count": 36094,
                "percentage": 23.999148919193868
            },
            "Praise": {
                "count": 80626,
                "percentage": 53.60878209006829
            },
            "Problem": {
                "count": 28532,
                "percentage": 18.971123094210657
            },
            "Question": {
                "count": 4734,
                "percentage": 3.147669168932891
            },
            "Message": {
                "count": 411,
                "percentage": 0.27327672759430044
            }
        },
        {
            "key": "lZmxo9dj6G",
            "description": "Entre 200 et 500€",
            "count": 150397,
            "Idea": {
                "count": 36094,
                "percentage": 23.999148919193868
            },
            "Praise": {
                "count": 80626,
                "percentage": 53.60878209006829
            },
            "Problem": {
                "count": 28532,
                "percentage": 18.971123094210657
            },
            "Question": {
                "count": 4734,
                "percentage": 3.147669168932891
            },
            "Message": {
                "count": 411,
                "percentage": 0.27327672759430044
            }
        },
        {
            "key": "NEexq5xYzW",
            "description": "Supérieur à 1000€",
            "count": 150397,
            "Idea": {
                "count": 36094,
                "percentage": 23.999148919193868
            },
            "Praise": {
                "count": 80626,
                "percentage": 53.60878209006829
            },
            "Problem": {
                "count": 28532,
                "percentage": 18.971123094210657
            },
            "Question": {
                "count": 4734,
                "percentage": 3.147669168932891
            },
            "Message": {
                "count": 411,
                "percentage": 0.27327672759430044
            }
        }
    ]
}
```

> 📘 Zoom on "by_context" parameter
>
> Here the "by_context" distributes the calculation by custom parameter "price". The attribute "key" contains the ID of the custom parameter value and the "description" its name.

## By level category

I have to use the following parameters :

* by_level_category : "2"

_Hypothesis: in our configuration the level category "2" corresponds to your regions._

```curl Remarks call
curl --location --request GET 'https://api.goodays.co/v2/stats/remarks?by_level_category=2' \
--header 'Content-Type: application/json' \
--header 'Authorization: 1234abcd1234abcd1234abcd1234abcd'
```

```json Remarks by level category
{
    "data": [
        {
            "key": "LAEd7rX893",
            "description": "Bretagne",
            "count": 150397,
            "Idea": {
                "count": 36094,
                "percentage": 23.999148919193868
            },
            "Praise": {
                "count": 80626,
                "percentage": 53.60878209006829
            },
            "Problem": {
                "count": 28532,
                "percentage": 18.971123094210657
            },
            "Question": {
                "count": 4734,
                "percentage": 3.147669168932891
            },
            "Message": {
                "count": 411,
                "percentage": 0.27327672759430044
            }
        },
        {
            "key": "ELxjpqAdKg",
            "description": "Berlin",
            "count": 150397,
            "Idea": {
                "count": 36094,
                "percentage": 23.999148919193868
            },
            "Praise": {
                "count": 80626,
                "percentage": 53.60878209006829
            },
            "Problem": {
                "count": 28532,
                "percentage": 18.971123094210657
            },
            "Question": {
                "count": 4734,
                "percentage": 3.147669168932891
            },
            "Message": {
                "count": 411,
                "percentage": 0.27327672759430044
            }
        },
        {
            "key": "OKQ4eXAdeW",
            "description": "Provence-Alpes-Côte d'Azur",
            "count": 150397,
            "Idea": {
                "count": 36094,
                "percentage": 23.999148919193868
            },
            "Praise": {
                "count": 80626,
                "percentage": 53.60878209006829
            },
            "Problem": {
                "count": 28532,
                "percentage": 18.971123094210657
            },
            "Question": {
                "count": 4734,
                "percentage": 3.147669168932891
            },
            "Message": {
                "count": 411,
                "percentage": 0.27327672759430044
            }
        }
    ]
}
```

> 📘 Zoom on "by_level_category" parameter
>
> Here the "by_level_category" distributes the calculation by level category. The attribute "key" contains the ID of the level and the "description" the level name.
