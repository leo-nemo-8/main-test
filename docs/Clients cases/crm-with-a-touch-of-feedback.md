---
title: CRM with a touch of Customer Experience
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
Let's say you use a CRM tool. Let's also say that you are well aware that customer experience is a must-have to understand your customers. If not, head to this [amazing white book](https://business.critizr.com/ebook-10-convictions-pour-la-relation-client?hsCtaTracking=17abeb06-bbdf-482a-9db5-5e9c45834578%7Cd930c7c2-5da0-4429-bbe8-f6bb9db4052e) and if you are still not convinced, please read [this one](https://business.critizr.com/en/blog/why-is-customer-feedback-important-for-marketing-purposes).

## Why use Goodays to enrich your CRM ?

Customer feedback is an amazing source of knowledge. It will not only provide valuable KPI about how your brand is perceived by your customers but it will also help you gather valuable informations about your customers' experience on more precise levels and even *verbatims*.\
These elements allow a general analysis on your brand and how you do things but they can also be used under the scope of one customer.\
With Goodays API, you will be able to add a whole new context facet for your customers. You will not only be aware of their purchases but also how they judge their experiences within your stores or online!

All these new informations may be extremely valuable when : 

* you have to **discuss with a customer** by email or on the phone
* you want to **create marketing campaigns** given one or more Customer Experience indicators
* you want to **analyse your customers' database** under the filter of Customer Experience indicators

## How to - Basics

The process is pretty straightforward.\
First, you have to retrieve the responses for the period you need.\
Then, you need to get the details of each response.\
Finally, you can use the answers to update your CRM profiles.

## Key takeaways

* Customer Experience is an important part of the customer knowledge.
* Customer Experience should be a part of your CRM.
* Customer Experience data could be valuable for customer management, marketing and analysis.
* Technical integration is simple as pie.

## How to - Expert

1. Retrieve every customer responses for a user

2. Request the following endpoint : `/responses`

3. Add the parameter `email` to only retrieve the responses for a user. We **strongly** recommend to url encode the email address to avoid any disturbances.

4. Perform the request that should look like this : `https://api.goodays.co/v2/responses?email=arnaud.lancelot%40goodays.co`

At this point, you will get an array of responses. By convention, we only send the 20 first results and the [pagination system](/docs/navigation-through-the-resources) to get the others.

Here is an example of what the API responds : 

```json
{
    "next": "https://api.goodays.co/v2/responses?cursor=cD0yMDE4LTEyLTEyKzA2JTNBMTclM0ExMi40MDI5MzMlMkIwMCUzQTAw",
    "previous": null,
    "results": [
        {
            "id": "{response-id}",
            "created_date": "2018-12-12T09:03:13.441327+01:00",
            "updated_date": "2018-12-12T09:04:13.305446+01:00",
            "has_answers": false,
            "has_message": true,
            "detail_url": "https://api.goodays.co/v2/responses/{response-id}"
        },
        {
            "id": "{response-id}",
            "created_date": "2018-12-12T09:01:47.562677+01:00",
            "updated_date": "2018-12-12T09:01:47.590289+01:00",
            "has_answers": true,
            "has_message": true,
            "detail_url": "https://api.goodays.co/v2/responses/{response-id}"
        },
        ...
    ]
}
```

2. For each response, get the details

Request the following endpoint : `/responses/{response-id}` with a response-id retrieved from the previous requests.

Below, an example of the response : 

```json
{
    "id": "gxKrrlok4o",
    "created_date": "2019-02-05T17:50:55.656496+01:00",
    "updated_date": "2019-02-05T17:50:55.685946+01:00",
    "source": "email",
    "survey": {
        "id": "{survey-id}",
        "slug": "post-purchase",
        "label": "Post Purchase",
        "enabled": true,
        "detail_url": "https://api.goodays.co/v2/surveys/{survey-id}"
    },
    "answers": [
        {
            "id": "{answer-id}",
            "value": "yes",
            "question": {
                "id": "{question-id}",
                "title": "Did you enjoy your time in our store ?",
                "type": "yesno",
                "enabled": true
            }
        },
        {
            "id": "{answer-id}",
            "created_date": "2019-02-05T17:50:55.635353+01:00",
            "value": 10,
            "question": {
                "id": "{question-id}",
                "title": "**Would you recommend** this place to your friends ?",
                "type": "nps",
                "enabled": true
            }
        },
        ...
    ],
    "message": null,
    "reply": null,
    "user": {
        "email": "arnaud.lancelot@goodays.co",
        "first_name": "Arnaud",
        "last_name": "Lancelot"
    },
    "context": {
        "frequency": "...",
        "rfm": "..."
    },
    "place": {
        ... place details
    }
}
```

You can use the answers to the survey or some context informations to enrich your customers profile.

> 📘 Need to retrieve hundreds of responses at once?
>
> Don't panic!\
> There is the [bulk mode](/reference#responses_bulk) which allows you to retrieve responses 20 by 20 (the paging is not customizable here). The GET parameters are the same as described above.
