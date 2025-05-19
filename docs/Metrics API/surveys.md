---
title: Surveys
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
> 📘 What's that?
> 
> Each survey is different and depends on your configuration : it can be composed of different answer type (stars, nps, multiple choices...).
> 
> _Please go to [/stats/survey](ref:stats_surveys_list) to obtain the detail of your survey configuration._

> 👍 Going further
> 
> Consult the [general Metrics API documentation](/docs/exploit-the-full-potential-of-your-data) for more.

![](https://files.readme.io/119cee5-Question.png "Question.png")

# How do I get my Survey metrics?

With [/stats/survey](ref:stats_surveys_list) 

```curl Survey call
curl --location --request GET 'https://api.goodays.co/v2/stats/surveys/5gd0vbRYxL' \
--header 'Content-Type: application/json' \
--header 'Authorization: 1234abcd1234abcd1234abcd1234abcd'
```

```json Sample Surveys Score
{
    "data": [
        {
            "key": "yLdLYMKp4j",
            "description": "Did you easily find the products you were looking for?",
            "count": 35,
            "average": 3.6965811965811968,
            "answers": [
                {
                    "count": 1,
                    "percentage": 2.857142857142857,
                    "value": 1
                },
                {
                    "count": 4,
                    "percentage": 11.428571428571429,
                    "value": 2
                },
                {
                    "count": 7,
                    "percentage": 20.0,
                    "value": 3
                },
                {
                    "count": 17,
                    "percentage": 48.57142857142857,
                    "value": 4
                },
                {
                    "count": 6,
                    "percentage": 17.142857142857142,
                    "value": 5
                }
            ]
        },
        {
            "key": "bJdY1MKqdR",
            "description": "What should we improve to fully satisfy you?",
            "count": 35,
          	"average": 3.8098290598290596,
            "answers": [
                {
                    "count": 1,
                    "percentage": 2.857142857142857,
                    "value": "The reception"
                },
                {
                    "count": 3,
                    "percentage": 8.571428571428571,
                    "value": "Advice"
                },
                {
                    "count": 5,
                    "percentage": 14.285714285714285,
                    "value": "Waiting at the checkout"
                },
                {
                    "count": 20,
                    "percentage": 57.14285714285714,
                    "value": "The products on offer"
                },
                {
                    "count": 6,
                    "percentage": 17.142857142857142,
                    "value": "Availability of counsellors"
                }
            ]
        },
        {
            "key": "ELxjqQmr4K",
            "description": "**Would you recommend** the VÉLO online store to your friends and family?",
            "count": 35,
            "average": 6.878205128205128,
            "answers": [
                {
                    "count": 0,
                    "percentage": 0.0,
                    "value": 0
                },
                {
                    "count": 1,
                    "percentage": 2.857142857142857,
                    "value": 1
                },
                {
                    "count": 5,
                    "percentage": 14.285714285714285,
                    "value": 2
                },
                {
                    "count": 2,
                    "percentage": 5.714285714285714,
                    "value": 3
                },
                {
                    "count": 1,
                    "percentage": 2.857142857142857,
                    "value": 4
                },
                {
                    "count": 1,
                    "percentage": 2.857142857142857,
                    "value": 5
                },
                {
                    "count": 0,
                    "percentage": 0.0,
                    "value": 6
                },
                {
                    "count": 8,
                    "percentage": 22.857142857142858,
                    "value": 7
                },
                {
                    "count": 6,
                    "percentage": 17.142857142857142,
                    "value": 8
                },
                {
                    "count": 7,
                    "percentage": 20.0,
                    "value": 9
                },
                {
                    "count": 4,
                    "percentage": 11.428571428571429,
                    "value": 10
                }
            ]
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
    "0-1": "Survey ID",
    "1-0": "**description** ",
    "1-1": "Description of the survey.",
    "2-0": "**count**",
    "2-1": "Number of responses.",
    "3-0": "**average** ",
    "3-1": "Average score",
    "4-0": "**answers**",
    "4-1": "List of questions related to the survey selected.  \nEach question lists the number of answers made on each answer option. The list is presented in the order of the choices proposed to the End Customer.  \nTo know the order of the choices of a survey it is necessary to use the endpoint [/stats/survey/{id}](ref:stats_surveys_read).",
    "5-0": "**count**",
    "5-1": "For each _answers_ : number of responses for the answer.",
    "6-0": "**percentage**",
    "6-1": "Percentage of responses for the answer.",
    "7-0": "**value**",
    "7-1": "Choice wording."
  },
  "cols": 2,
  "rows": 8,
  "align": [
    "left",
    "left"
  ]
}
[/block]


## parameters

| Parameter | Description |
| :-------- | :---------- |
| **id**    | Survey ID   |

# Add some filters

It is possible to add GET parameters to refine the calculation of the survey results over a defined period, an establishment...

## GET parameters

To filter the survey results, it is possible to combine the following GET parameters:

[block:parameters]
{
  "data": {
    "h-0": "GET parameters",
    "h-1": "Description",
    "0-0": "**begin**",
    "0-1": "Start date of the calculation period.  \n_Format : YYYY-MM-DDThh:mm:ssZ_  \nSee [this page](doc:timezone-management) for the timezone management.",
    "1-0": "**end**",
    "1-1": "End date of the calculation period.  \n_Format : YYYY-MM-DDThh:mm:ssZ_  \nSee [this page](doc:timezone-management) for the timezone management.",
    "2-0": "**place**",
    "2-1": "Filter on an establishment.  \n_It is necessary to indicate the ID of the establishment from the endpoint [/places](ref:places_list)_",
    "3-0": "**places**",
    "3-1": "Filter on an establishment list.  \n_Format : Establishment IDs separated by commas_",
    "4-0": "**level**",
    "4-1": "Filter on a level.  \n_It is necessary to indicate the ID of the establishment from the endpoint [/levels](ref:levels_list)_",
    "5-0": "**levels**",
    "5-1": "Filter on a level list.  \n_Format : Level IDs separated by commas_"
  },
  "cols": 2,
  "rows": 6,
  "align": [
    "left",
    "left"
  ]
}
[/block]


# Use cases

Here are some examples to show you the possibilities of this endpoint. This is obviously not exhaustive, it's up to you to have fun to find the right parameter arrangements :)

## For one establishment over the month of Octobre 2021

I have to use the following parameters :

- begin : the first date of the month of October
- end : the last date of the month of October
- place : the ID of the establishment

```curl
curl --location --request GET 'https://api.goodays.co/v2/stats/surveys/My4lvMpK8R? \
   begin=2021-10-01T00:00:00Z \
  &end=2021-10-31T00:00:00Z \
  &place=bwdQ661e4Q' \
--header 'Content-Type: application/json' \
--header 'Authorization: 1234abcd1234abcd1234abcd1234abcd'
```

```json
{
    "data": [
        {
            "key": "yLdLYMKp4j",
            "description": "Did you easily find the products you were looking for?",
            "count": 3,
            "average": 3.6666666666666665,
            "answers": [
                {
                    "count": 2,
                    "percentage": 66.66666666666666,
                    "value": 5
                },
                {
                    "count": 1,
                    "percentage": 33.33333333333333,
                    "value": 1
                }
            ]
        },
        {
            "key": "bJdY1MKqdR",
            "description": "What should we improve to fully satisfy you?",
            "count": 3,
            "average": 3.6666666666666665,
            "answers": [
                {
                    "count": 2,
                    "percentage": 66.66666666666666,
                    "value": 5
                },
                {
                    "count": 1,
                    "percentage": 33.33333333333333,
                    "value": 1
                }
            ]
        },
        {
            "key": "ELxjqQmr4K",
            "description": "**Would you recommend** the VÉLO online store to your friends and family?",
            "count": 3,
            "average": 9.0,
            "answers": [
                {
                    "count": 1,
                    "percentage": 33.33333333333333,
                    "value": 8
                },
                {
                    "count": 1,
                    "percentage": 33.33333333333333,
                    "value": 9
                },
                {
                    "count": 1,
                    "percentage": 33.33333333333333,
                    "value": 10
                }
            ]
        }
    ]
}
```

## For two levels

 have to use the following parameters :

- level : level ID

```curl
curl --location --request GET 'https://api.goodays.co/v2/stats/surveys/My4lvMpK8R? \
	levels=Yqxzp5Ad2J,bQdPLrmwd9' \
--header 'Content-Type: application/json' \
--header 'Authorization: 1234abcd1234abcd1234abcd1234abcd'
```

```json
{
    "data": [
        {
            "key": "yLdLYMKp4j",
            "description": "Did you easily find the products you were looking for?",
            "count": 66285,
            "average": 4.625870534172204,
            "answers": [
                {
                    "count": 53073,
                    "percentage": 80.06788866259335,
                    "value": 5
                },
                {
                    "count": 8495,
                    "percentage": 12.815870860677379,
                    "value": 4
                },
                {
                    "count": 2778,
                    "percentage": 4.190993437429283,
                    "value": 1
                },
                {
                    "count": 1215,
                    "percentage": 1.8329938900203666,
                    "value": 3
                },
                {
                    "count": 724,
                    "percentage": 1.0922531492796257,
                    "value": 2
                }
            ]
        },
        {
            "key": "bJdY1MKqdR",
            "description": "What should we improve to fully satisfy you?",
            "count": 60779,
            "average": 4.837596490103213,
            "answers": [
                {
                    "count": 53698,
                    "percentage": 88.34959443228747,
                    "value": 5
                },
                {
                    "count": 5860,
                    "percentage": 9.641488013952188,
                    "value": 4
                },
                {
                    "count": 558,
                    "percentage": 0.9180802579838431,
                    "value": 3
                },
                {
                    "count": 451,
                    "percentage": 0.7420326099475147,
                    "value": 1
                },
                {
                    "count": 212,
                    "percentage": 0.348804685828987,
                    "value": 2
                }
            ]
        },
        {
            "key": "ELxjqQmr4K",
            "description": "**Would you recommend** the VÉLO online store to your friends and family?",
            "count": 59159,
            "average": 9.444679569107018,
            "answers": [
                {
                    "count": 41945,
                    "percentage": 70.9021450666847,
                    "value": 10
                },
                {
                    "count": 10274,
                    "percentage": 17.366757382646767,
                    "value": 9
                },
                {
                    "count": 4581,
                    "percentage": 7.743538599367805,
                    "value": 8
                },
                {
                    "count": 1112,
                    "percentage": 1.8796801839111545,
                    "value": 7
                },
                {
                    "count": 340,
                    "percentage": 0.5747223583901012,
                    "value": 5
                },
                {
                    "count": 285,
                    "percentage": 0.48175256512111425,
                    "value": 6
                },
                {
                    "count": 263,
                    "percentage": 0.44456464781351945,
                    "value": 0
                },
                {
                    "count": 99,
                    "percentage": 0.16734562788417653,
                    "value": 3
                },
                {
                    "count": 95,
                    "percentage": 0.16058418837370475,
                    "value": 2
                },
                {
                    "count": 90,
                    "percentage": 0.15213238898561504,
                    "value": 1
                },
                {
                    "count": 75,
                    "percentage": 0.12677699082134586,
                    "value": 4
                }
            ]
        }
    ]
}
```