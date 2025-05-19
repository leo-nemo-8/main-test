---
title: Detractors solicitation
excerpt: ''
deprecated: false
hidden: true
metadata:
  title: ''
  description: ''
  robots: index
next:
  description: ''
---
Having happy customers is obviously a good thing and should be a real goal in your customer experience strategy. However, your customer base is probably not composed 100% by happy clients. As the NPS scale described, there is also some passives and some **detractors**.\
Even if having detractors seems to be the worst thing, it actually represents a huge lever !

According to the American Express 2017 Customer Service Barometer, "Americans tell an average of 15 people about a poor service experience, versus the 11 people they’ll tell about a good experience.". This statement should create a sense of urgency to deal with your detractors without waiting !\
There are several types of detractors. You can find the detail [in this article](https://business.critizr.com/blog/les-5-profils-de-consommateurs-insatisfaits).

The key insight here is that detractors usually experienced misunderstanding or felt deceived. Interacting to them right after they tell you about their insatisfaction is the perfect way to minimise their impact on other customers, fix their situation and move them from detractors to promoters.

## How to - Basics

The first steps are actually quite the same as the [article about CRM](docs/crm-with-a-touch-of-feedback).\
We still need to retrieve responses and get the details of each one to detect detractors.\
We now add a last step, the solicitation of these detractors.

## Key takeaways

* Having detractors is bad but ignoring them is worst!
* Reacting immediately after a detractor sent a review is an excellent way to turn this person in a promoter or at least to minimize his or her negative influence.
* Retrieving detractors can easily be done.
* Solicitations can be send one by one or in bluk.
* Some of our clients choose to create "detractors" surveys to to target those users.

## How to - Expert

1. Retrieve every customer responses for a user

2. Request the following endpoint : `/responses`

3. Add the parameter `start_date` and/or `end_date` to only retrieve the responses within this date range. For more information about the date filter, you should [read this article](doc:sense-the-response) .

4. Perform the request that should look like this : `https://api.critizr.com/v2/responses?start_date=2018-07-09T00%3A00%3A00&end_date=2018-07-10T00%3A00%3A00`

At this point, you will get an array of responses. By convention, we only send the 20 first results and the [pagination system](/docs:navigation-through-the-resources) to get the others.

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

2. For each response, get the details

Request the following endpoint : `/responses/{response-id}` with a response-id retrieved from the previous requests.

Below, an example of the response : 

```json
{
    "id": "gxKrrlok4o",
    "created_date": "2019-02-05T17:50:55.656496+01:00",
    "updated_date": "2019-02-05T17:50:55.685946+01:00",
    "source": "CU",
    "medium": "TE",
    "survey": {
        "id": "{survey-id}",
        "slug": "post-purchase",
        "label": "Post Purchase",
        "enabled": true,
        "detail_url": "https://api.critizr.com/v2/surveys/{survey-id}"
    },
    "answers": [
        {
            "id": "{answer-id}",
            "created_date": "2019-02-05T17:51:20.755242+01:00",
            "value": 10,
            "question_id": "{response-id}"
        },
        {
            "id": "{answer-id}",
            "created_date": "2019-02-05T17:50:55.635353+01:00",
            "value": 5,
            "question_id": "{response-id}"
        },
        ...
    ],
    "message": null,
    "reply": null,
    "user": {
        "email": "arnaud.lancelot@critizr.com",
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

With the details of the participation, you can get the value of the NPS question's answer and find out which customer is a detractor.

3. Send emails or sms to the detractors

Now that you retrieve the detractors among your respondents, you can send emails or sms to them.

> 📘 Sending mecanisms
>
> Critizr API lets you decide whether you send solicitations one by one or in bulk. The details of each mecanism will be presented below

1. Create the payloads\
   When you send solicitations one by one, the payload you have to generate looks like the one below :

```json
{
	"sender": "Critizr <no-reply@critizr.com>",
	"survey": "{survey-slug}",
	"type": "email|sms",
	"place": "{place-id}",
	"recipient": "XXXXX@critizr.com",
	"context": {
		"property": "value",
		"property": "value",
		...
	}
}
```

You can then send this payload to the following endpoint `https://api.critizr.com/v2/solicitations` with the `POST` HTTP verb.

For bulk sendings, the payload changes on the `recipient` field. It will now require an array of emails addresses. The payload should look like this :

```json
{
	"sender" : "Critizr <no-reply@critizr.com>",
	"survey" : "{survey-slug}",
	"type": "email|sms",
	"place" : "{place-id}",
	"recipient" : ["XXXXX@critizr.com", "YYYYYY@critizr.com", ...],
	"context": {
		"property": "value",
		"property": "value",
		...
	}
}
```

You can then send this payload to the following endpoint `https://api.critizr.com/v2/solicitations/bulk` with the `POST` HTTP verb.
