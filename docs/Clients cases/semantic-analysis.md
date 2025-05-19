---
title: Semantic analysis
excerpt: ''
deprecated: true
hidden: true
metadata:
  title: ''
  description: ''
  robots: noindex
next:
  description: ''
---
Knowing what your customers actually think is the Graal of Customer Experience. It feels like a superpower! Imagine being able to read your customers minds, to feel their frustration, anger, happiness, satisfaction, doubt or enthusiasm.\
We are not that far from this (expect maybe the "read the minds" part).\
If we are not able to know what your customers think, we may know what they say or write about you in the *verbatim* we collect. And with a touch of semantic analysis and analysis, all these *verbatim* will tell you what you want to know.

> ❗️ Disclaimer
>
> Goodays is a Customer Experience platform. Although it will allow you to gather *verbatim* (among other informations), it will not provide semantic analysis on its own.\
> We encourage you to work with a company specialized in semantic analysis and to use our API to provide this partner with your *verbatim*.

## How to - Basics

The process is pretty straightforward.\
In a nutshell, your semantic partner will request our API periodically and retrieve every *verbatim* your customers wrote.

## Key takeaways

* Semantic analysis works best with a lot of messages.
* *Verbatim* from Goodays are easily retrievable and usable for such analysis.
* Goodays **does not provide** a semantic feature. But we are more than happy to share your *verbatim* with your partners.

## How to - Expert

1. Retrieve every customer responses with a verbatim

⋅⋅1. Request the following endpoint : `/responses`\
⋅⋅2. Add the parameter `has_message=true` to only retrieve the responses with a *verbatim*\
⋅⋅3. Perform the request that should look like this : `https://api.critizr.com/v2/responses?has_message=true`

At this point, you will get an array of responses. By convention, we only send the 20 first results and the [pagination system](/docs/navigation-through-the-resources) to get the others.

Here is an example of what the API responds : 

```json
{
    "next": "https://api.critizr.com/v2/responses?cursor=cD0yMDE4LTEyLTEyKzA2JTNBMTclM0ExMi40MDI5MzMlMkIwMCUzQTAw",
    "previous": null,
    "results": [
        {
            "id": "{response-id}",
            "created_date": "2018-12-12T09:03:13.441327+01:00",
            "updated_date": "2018-12-12T09:04:13.305446+01:00",
            "answers_count": 8,
            "has_message": true,
            "detail_url": "https://api.critizr.com/v2/responses/{response-id}"
        },
        {
            "id": "{response-id}",
            "created_date": "2018-12-12T09:01:47.562677+01:00",
            "updated_date": "2018-12-12T09:01:47.590289+01:00",
            "answers_count": 3,
            "has_message": true,
            "detail_url": "https://api.critizr.com/v2/responses/{response-id}"
        },
        ...
    ]
}
```

2. For each response, get all the informations

Request the following endpoint : `/responses/{response-id}` with a response-id retrieved from the previous requests.

Below, an example of the response : 

```json
{
    "id": "{response-id}",
    "created_date": "2018-12-12T09:03:13.441327+01:00",
    "updated_date": "2018-12-12T09:04:13.305446+01:00",
		"medium": "email",
    "survey": {
        ... survey details
    },
    "answers": [
        ... answers objects
    ],
    "message": {
        "id": "{message-id}",
        "sent_at": "2019-02-04T14:45:32.547500+01:00",
        "transmitted_at": "2019-02-04T14:45:32.769123+01:00",
        "replied_at": null,
        "type": "Compliment",
        "content": "Very nice store",
        "attachement": null,
        "sender": {
            "email": "arnaud.lancelot@critizr.com",
            "first_name": "Arnaud",
            "last_name": "Lancelot"
        }
    },
    "reply": {
        ... reply details
    },
    "user": {
        ... user details
    },
    "context": {
        ... context details
    },
    "place": {
        ... place details
    }
}
```

With these two steps, you or your semantic partner can retrieve every *verbatim* your customers wrote. **Now your semantic analyses are fueled by Goodays!**
