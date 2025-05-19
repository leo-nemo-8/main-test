---
title: Become a collection source
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
The Collect API will allow you to become your own collection source by allowing you to send us the collected entries from your own tools!

![](https://files.readme.io/a2dc0e4-Collect_reviews.png "Collect reviews.png")

> 👍 Going further
> 
> Consult the [API Collect](/reference#responses_collect) for more.

> 📘 Feel stucked?
> 
> Need help with an error? Head to [Troubleshooting and errors](/docs/errors) for more information.

# Presentation

The Collect API allows you to push the collected responses on your side from your own tools, all in real time!  
Our recommendation is to create participation on the Goodays side as soon as you collect it from your tool. This allows the local manager not to lose time on the processing of the customer feedback.

This is very effective if you are using an application, kiosk or terminal that would not be compatible with the SDKs provided by default by Goodays.

![](https://files.readme.io/23f7c68-Capture_decran_2020-10-01_a_15.56.06.png "Capture d’écran 2020-10-01 à 15.56.06.png")

> ❗️ 
> 
> The survey used is in Goodays format and must respect the **response** formatting rules.

# How to push the responses from my end customer

## Push a response

In order to complete the payload to post a response you must first recover the following Goodays data:

- the **structure** ID of the **[survey](become-a-collection-source#the-survey-part)**
- the **question** IDs of the **[survey](become-a-collection-source#the-survey-part)**
- the **[establishment](become-a-collection-source#the-point-of-sales-part)** ID
- the **[Custom parameters](become-a-collection-source#the-customer-parameters-part)**

And, of course, the data related to the end customer.

You now have all the information you need to post a response to Goodays!  
For this you must use the [API Collect](/reference#responses_collect).

> ❗️ Unique Response
> 
> Be careful to push only one response per end customer's participation: the Collect API records each call you made without deduplication.

For our example, we will send the answer to the survey with the following information (see [prepare the data](become-a-collection-source#prepare-the-data) chapter):

- End customer (the "_user_") : **Mr Miyagi**
- Establishment (the "_place_") : **VÉLO Antibes** (ID : _ABC123_)
- Survey : **post_visit** (ID : _mrY4WLpx9w_)
- Custom Parameters : **Order date** (key : _ordr_dt_)

Description of the payload:

[block:parameters]
{
  "data": {
    "h-0": "Attribut",
    "h-1": "Description",
    "h-2": "Mandatory",
    "0-0": "**date**",
    "0-1": "Date of response from the end customer  \n  \nFormat: 2020-08-07T01:29:30.034195+02:00",
    "0-2": "**Yes**",
    "1-0": "**user**",
    "1-1": "Contains the data of the end customer:  \n  \n- _email_\n- _first_name_\n- _last_name_\n- _phone_\n- _crm_id_",
    "1-2": "See [The customer parameters part](become-a-collection-source#the-customer-parameters-part).",
    "2-0": "**context**",
    "2-1": "The Custom Parameters",
    "2-2": "See [The customer parameters part](become-a-collection-source#the-customer-parameters-part).",
    "3-0": "**place**",
    "3-1": "The establishment ID  \n_Enter your establishment code directly here_",
    "3-2": "**Yes**",
    "4-0": "**survey**",
    "4-1": "The survey ID  \n  \nSee [The survey part](become-a-collection-source#the-survey-part).",
    "4-2": "**Yes**",
    "5-0": "**answers** ",
    "5-1": "List of answers to survey questions.  \n  \nSee [The survey part](become-a-collection-source#the-survey-part).  \n  \nNote: An end customer is not forced to answer all questions, you can send a survey that is not completed in its totality.",
    "5-2": "**Yes**",
    "6-0": "**message**",
    "6-1": "Text message from the end customer:  \n  \n- _created_date_ : format \"2020-08-07T01:29:30.034195+02:00\"\n\n- _type_: \"Idea\", \"Praise\", \"Problem\", \"Question\" or \"NoType\" if no category exists\n\n- _content_: text messageNotes:\n\n- A text message cannot be sent without a survey\n\n- A text message must have all his attributes filled in",
    "6-2": "**No**",
    "7-0": "**medium**",
    "7-1": "Source of feedback collection.  \n  \nHere are the most used mediums:  \n  \n- transactional email: `TE`\n- transactional SMS: `TS`\n- mobile: `MOB`_The value differs according to your collection perimeter: please ask your Goodays technical contact for this information if it does not match the examples above._",
    "7-2": "**Yes**",
    "8-0": "**collect_uid**",
    "8-1": "Allows the management of the **unique participation**.  \n  \nThe `collect_uid` parameter is used to identify the participation in a unique way. This can be a string, a number, a date... You can, for example, concatenate an order ID, a reservation ID, a basket ID... with a timestamp. The most important thing is that this value must be unique.  \n  \nIf the value of the `collect_uid` already exists then a `409 error` is returned and the response is not recorded.  \n  \n_This parameter is not mandatory but strongly recommended._",
    "8-2": "**No**"
  },
  "cols": 3,
  "rows": 9,
  "align": [
    "left",
    "left",
    "left"
  ]
}
[/block]


The API Call:

```curl
curl --location --request POST 'https://api.goodays.co/v2/responses/collect' \
--header 'Content-Type: application/json' \
--header 'Authorization: 1234abcd1234abcd1234abcd1234abcd' \
--data-raw '{
  "date": "2020-08-07T01:29:30.034195+02:00",
  "user": {
    "email": "kesuke@miyagi.com",
    "first_name": "Kesuke",
    "last_name": "Miyagi",
    "phone": "+33123456789",
    "crm_id": ""
  },
  "context": {
    "ordr_dt": "2020-08-06"
  },
  "place": "kvdAqqMYdj",
  "survey": "mrY4WLpx9w",
  "answers": [
    {"question": "rY4WDG1px9", "value": 5},
    {"question": "ap4Mzm1vx2", "value": 3},
    {"question": "9v8XaO1Xd3", "value": [
                            "Welcome / friendliness",
                            "Availability"]
                            },
    {"question": "5gd0vbRYxL", "value": 2},
    {"question": "OD82OVbJdW", "value": ["Tastes too bland"]},
    {"question": "Qr43JKNjdV", "value": 5},
    {"question": "MexGzQOn4K", "value": 10}
    ],
  "message": {
    "created_date": "2020-09-25T16:13:09.799615+02:00",
    "type": "Praise",
    "content": "I really appreciated my experience with your counselor."
  },
  "medium": "terminal",
  "collect_uid": "16814802001BC123"
}'
```

If the answer has been recorded, you will get a "_201: created_" back in the header.  
If not, an error will be returned in the endpoint return, for example:

```json
{
    "survey": [
        "No resource found for the given value."
    ]
}
```

## Prepare the data

### The survey part

Request the following endpoint : [`/surveys`](ref:surveys_list).

```curl
curl --location --request GET 'https://api.goodays.co/v2/surveys' \
--header 'Content-Type: application/json' \
--header 'Authorization: 1234abcd1234abcd1234abcd1234abcd'
```

You will obtain something like this: 

```json
"next": null,
    "previous": null,
    "results": [
        {
            "id": "mrY4WLpx9w",
            "slug": "post_visit",
            "label": "Post Visite",
            "enabled": true,
            "detail_url": "https://api.goodays.co/v2/surveys/mrY4WLpx9w"
        },
        {
            "id": "kegxKlZ8oY",
            "slug": "sollicited_new_customer",
            "label": "Email - Post-achat Magasin 1er achat",
            "enabled": true,
            "detail_url": "https://api.goodays.co/v2/surveys/kegxKlZ8oY"
        },
        {
            "id": "LAEd7lD493",
            "slug": "spontaneous",
            "label": "Spontané",
            "enabled": true,
            "detail_url": "https://api.goodays.co/v2/surveys/LAEd7lD493"
        }
    ]
}
```

Take the id corresponding to the survey you wish to push responses to.  
Request the following endpoint : [`/surveys`](ref:surveys_list) with the "id" as parameter:

```curl surveys_read call
curl --location --request GET 'https://api.goodays.co/v2/surveys/mrY4WLpx9w' \
--header 'Content-Type: application/json' \
--header 'Authorization: 1234abcd1234abcd1234abcd1234abcd'
```

You will obtain something like this:

```json
{
    "id": "mrY4WLpx9w",
    "slug": "restaurant-experience",
    "label": "Restaurant Experience",
    "enabled": true,
    "questions": [
        {
            "id": "rY4WDG1px9",
            "position": 1,
            "title": "Are you generally satisfied with your restaurant experience?",
            "enabled": true,
            "type": "stars",
            "enabled_at": "2019-04-04T17:50:06.349126+02:00",
            "disabled_at": null,
            "options": {},
            "sub_questions": []
        },
        {
            "id": "ap4Mzm1vx2",
            "position": 2,
            "title": "What did you think of the quality of service throughout your meal?",
            "enabled": true,
            "type": "stars",
            "enabled_at": "2019-04-04T17:50:06.416521+02:00",
            "disabled_at": null,
            "options": {},
            "sub_questions": [
                {
                    "id": "9v8XaO1Xd3",
                    "sub_id": 1,
                    "triggers": [
                        1,
                        2,
                        3
                    ],
                    "title": "What can we improve?",
                    "enabled": true,
                    "type": "multiple_answers",
                    "enabled_at": "2019-04-04T17:50:06.465984+02:00",
                    "disabled_at": null,
                    "options": {
                        "choices": [
                            "Welcome / friendliness",
                            "Availability",
                            "Politeness",
                            "Tips",
                            "Errors in the dishes served",
                            "Unsatisfied requests",
                            "Slow service",
                            "Something else."
                        ]
                    }
                }
            ]
        },
        {
            "id": "5gd0vbRYxL",
            "position": 3,
            "title": "Was your meal tasty?",
            "enabled": true,
            "type": "stars",
            "enabled_at": "2019-04-04T17:50:06.507387+02:00",
            "disabled_at": null,
            "options": {},
            "sub_questions": [
                {
                    "id": "OD82OVbJdW",
                    "sub_id": 1,
                    "triggers": [
                        1,
                        2,
                        3
                    ],
                    "title": "What can we improve?",
                    "enabled": true,
                    "type": "multiple_answers",
                    "enabled_at": "2019-04-04T17:50:06.548106+02:00",
                    "disabled_at": null,
                    "options": {
                        "choices": [
                            "Tastes too bland",
                            "Seasoning",
                            "Problem cooking meat",
                            "Warmth of the dishes",
                            "Freshness of the products",
                            "Originality of taste",
                            "Something else."
                        ]
                    }
                }
            ]
        },
        {
            "id": "Qr43JKNjdV",
            "position": 4,
            "title": "How do you judge the quality/price ratio of your dish?",
            "enabled": true,
            "type": "stars",
            "enabled_at": "2019-04-04T17:50:06.586386+02:00",
            "disabled_at": null,
            "options": {},
            "sub_questions": [
                {
                    "id": "k6xmZ1vK8j",
                    "sub_id": 1,
                    "triggers": [
                        1,
                        2,
                        3
                    ],
                    "title": "What can we improve?",
                    "enabled": true,
                    "type": "multiple_answers",
                    "enabled_at": "2019-04-04T17:50:06.630313+02:00",
                    "disabled_at": null,
                    "options": {
                        "choices": [
                            "Portion size",
                            "Quality of the meat",
                            "Quality of other products",
                            "Something else."
                        ]
                    }
                }
            ]
        },
        {
            "id": "DYdkw7N3dM",
            "position": 5,
            "title": "Have you visited us before?",
            "enabled": true,
            "type": "yesno",
            "enabled_at": "2024-11-21T15:19:50.945499+01:00",
            "disabled_at": null,
            "options": {},
            "sub_questions": []
        },
        {
            "id": "MexGzQOn4K",
            "position": 6,
            "title": "Would you recommend Buffalo Grill to others?",
            "enabled": true,
            "type": "nps",
            "enabled_at": "2019-04-04T17:50:06.674478+02:00",
            "disabled_at": null,
            "options": {
                "alert_limit": 6
            },
            "sub_questions": []
        }
    ],
    "places": "https://api.critizr.com/v2/surveys/kQvdJyo8Dg/places",
    "responses": "https://api.critizr.com/v2/surveys/kQvdJyo8Dg/responses"
}
```

That's it, you have the structure of the survey! 

> 👍 Types of questions
> 
> All of these answer type are compatible with the Collect API :
> 
> - `nps`
> - `csat`
> - `stars`
> - `choices`
> - `multiple_answers`
> - `text`
> - `yes/no`

### The customer parameters part

Request the following endpoint : [`/configuration`](ref:configuration_list).

```curl
curl --location --request GET 'https://api.goodays.co/v2/configuration' \
--header 'Content-Type: application/json' \
--header 'Authorization: 1234abcd1234abcd1234abcd1234abcd'
```

You will obtain something like this:

```json
{
    "custom_parameters": [
        {
            "key": "first_name",
            "label": "First name",
            "required": false,
            "use_in_stats": true
        },
        {
            "key": "email",
            "label": "Email",
            "required": false,
            "use_in_stats": true
        },
        {
            "key": "phone",
            "label": "Phone",
            "required": false,
            "use_in_stats": false
        },
        {
            "key": "last_name",
            "label": "Last name",
            "required": false,
            "use_in_stats": false
        },
        {
            "key": "crm_id",
            "label": "ID Client",
            "required": false,
            "use_in_stats": false
        },
        {
            "key": "ordr_dt",
            "label": "Order date",
            "required": false,
            "use_in_stats": false
        },
        {
            "key": "advsr",
            "label": "Adivsor seen",
            "required": false,
            "use_in_stats": true
        }
    ]
}
```

> 🚧 What Custom Parameters do I have to use?
> 
> To find out if a Custom Parameter is mandatory you have to look at the attribute "required ". If it is at "true" then the attribute must be in the payload of the API call.

> 🚧 And for the "user"?
> 
> For the `user` object: if a value is optional you must leave the attribute with an empty value.
> 
> But the `email` and `first_name` is always mandatory: if you don't have it you must be don't push the `user` object.

# Examples

## Send survey scores only

```curl
curl --location --request POST 'https://api.goodays.co/v2/responses/collect' \
--header 'Content-Type: application/json' \
--header 'Authorization: 1234abcd1234abcd1234abcd1234abcd' \
--data-raw '{
  "date": "2020-08-07T01:29:30.034195+02:00",
  "user": {
    "email": "kesuke@miyagi.com",
    "first_name": "Kesuke",
    "last_name": "Miyagi",
    "phone": "+33123456789",
    "crm_id": "012ABC789"
  },
  "context": {
    "ordr_dt": "2020-08-06"
  },
  "place": "ABC123",
  "survey": "mrY4WLpx9w",
  "answers": [
    {"question": "rY4WDG1px9", "value": 5},
    {"question": "ap4Mzm1vx2", "value": 3},
    {"question": "9v8XaO1Xd3", "value": [
                            "Welcome / friendliness",
                            "Availability"]
                            },
    {"question": "5gd0vbRYxL", "value": 2},
    {"question": "OD82OVbJdW", "value": ["Tastes too bland"]},
    {"question": "Qr43JKNjdV", "value": 5},
    {"question": "Qr43JKNjdV", "value": 1},
    {"question": "DYdkw7N3dM", "value": 1} //0 for no, 1 for yes
    ],
  "medium": "terminal",
  "collect_uid": "16814802001BC123"
}'
```

## Send a partially completed survey

```curl
curl --location --request POST 'https://api.goodays.co/v2/responses/collect' \
--header 'Content-Type: application/json' \
--header 'Authorization: 1234abcd1234abcd1234abcd1234abcd' \
--data-raw '{
  "date": "2020-08-07T01:29:30.034195+02:00",
  "user": {
    "email": "kesuke@miyagi.com",
    "first_name": "Kesuke",
    "last_name": "Miyagi",
    "phone": "+33123456789",
    "crm_id": "012ABC789"
  },
  "context": {
    "ordr_dt": "2020-08-06"
  },
  "place": "ABC123",
  "survey": "mrY4WLpx9w",
  "answers": [
    {"question": "rY4WDG1px9", "value": 5},
    {"question": "ap4Mzm1vx2", "value": 3}
    ],
  "medium": "terminal",
  "collect_uid": "16814802001BC123"
}'
```