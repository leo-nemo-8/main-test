---
title: Legacy retrieval
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
You are moving to Goodays and your previous partner collected ratings, verbatims, end customer data and custom parameters. You can import this history into Goodays, so that your statistics and KPIs keep their continuity.

Each past participation is sent with one API call. Historical participations only feed your statistics: they never enter the Inbox, raise no alert and send no notification (see [Live or historical import](doc:live-vs-historical-import)).

## Before you start

* **Map your data.** Your legacy data will rarely match the Goodays format as is: match each legacy survey and question with a Goodays survey and question, and each legacy point of sale with a Goodays point of sale. This page assumes this transformation is done.
* **Plan for volume.** The import is simple but can take time for a large history. Send a `collect_uid` with each participation so that you can resume an interrupted import safely.
* **Test first.** Import a small sample, check it with your Goodays project contact, then send the rest.

## How to import your history

Call the [/responses/historical](ref:responses_historical) endpoint with the `POST` method and the correct payload.  
This payload contains the list of all the answers of a participation and, if any, the verbatim of the end customer. In order to create the list of answers, you need to get the surveys and their questions, to match the Goodays questions with the legacy answers.

> 📘 `/responses` is now `/responses/historical`
>
> The endpoint has a new, more explicit name: `POST /responses/historical`. It takes exactly the same payload and behaves the same way. If you already use `POST /responses`, nothing changes for you: it remains available and works as before.

1. Get the surveys  
   Request the following endpoint: [/surveys](ref:surveys_list).  
   You will obtain something like this:

```json
{
    "next": "{next-cursor}",
    "previous": "{previous-cursor}",
    "results": [
        {
            "id": "{survey-id}",
            "slug": "post-purchase",
            "label": "Post Purchase",
            "enabled": true,
            "detail_url": "https://api.goodays.co/v2/surveys/{survey-id}"
        },
        {
            "id": "{survey-id}",
            "slug": "post-appointment",
            "label": "Post Appointment",
            "enabled": true,
            "detail_url": "https://api.goodays.co/v2/surveys/{survey-id}"
        }
    ]
}
```

2. For each survey, get the attached questions  
   Request the following endpoint: [/surveys/{survey-id}](ref:surveys_read) with a survey ID retrieved from the previous request.

Below, an example of the API response:

```json
{
    "id": "{survey-id}",
    "slug": "post-purchase",
    "label": "Post Purchase",
    "enabled": true,
    "questions": [
        {
            "id": "{question-id}",
            "position": 1,
            "title": "Are you **satisfied** with your purchase in our store ?",
            "enabled": true,
            "type": "stars",
            "enabled_at": "2018-01-18T02:22:22.157859+01:00",
            "disabled_at": null,
            "options": {},
            "sub_questions": []
        },
        {
            "id": "{question-id}",
            "position": 2,
            "title": "Please rate  **the welcome and sympathy** of our team",
            "enabled": true,
            "type": "stars",
            "enabled_at": "2018-01-18T02:22:22.802779+01:00",
            "disabled_at": null,
            "options": {},
            "sub_questions": []
        }
    ],
    "places": "https://api.goodays.co/v2/surveys/{survey-id}/places"
}
```

Now that you have retrieved the surveys ids and the questions ids, you can generate the payload to insert your legacy participations in Goodays.

3. Create payloads  
   The payload you need to generate looks like the one below:

```json
{
    "place": "{place-id}",
    "date": "{date-of-the-participation}",
    "survey": "{survey-id}",
    "answers": [
        {
            "value": 10,
            "question": "{question-id}"
        },
        {
            "value": 5,
            "question": "{question-id}"
        }
    ],
    "user": {
        "email": "mikey@goonies.com",
        "first_name": "Mikey",
        "last_name": "Walsh",
        "phone": "0123456789",
        "crm_id": "{crm-id}"
    },
    "context": {
        "{custom-parameter-key}": "{custom-parameter-value}"
    },
    "message": {
        "created_date": "{date-of-the-participation}",
        "type": "Praise",
        "content": "{verbatim-of-the-end-customer}"
    },
    "medium": "{medium}",
    "collect_uid": "{your-unique-participation-id}"
}
```

> ❗️ Participation date
>
> You should fill the `date` field with the date where the participation actually took place!

> 📘 Custom parameters
>
> The `context` part contains your custom parameters. To obtain their list, request the following endpoint : [`/configuration`](ref:configuration_list).

> 📘 Verbatim
>
> The `message` part is optional. It contains the verbatim of the end customer, with its remark type (`Idea`, `Praise`, `Problem`, `Question` or `NoType`). A verbatim cannot be sent without the `user` object. See [Become a collection source](doc:become-a-collection-source) for the details of each field.

> 📘 Answer values
>
> The expected `value` format depends on the question type: see [Surveys & Question Types](doc:surveys-question-types). For example, a Yes/No question takes `1` for yes and `0` for no.

4. Send the request  
   Once your payload is properly built, you can call the endpoint `/responses/historical` with the `POST` method.  
   Don't forget to add your payload!

```curl
curl --location --request POST 'https://api.goodays.co/v2/responses/historical' \
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
  "medium": "TE",
  "collect_uid": "16814802001BC123"
}'
```

If your payload is valid, you will get a "_201: created_" back in the header.  
If not, an error will be returned in the response of the call, for example:

```json
{
    "survey": [
        "No resource found for the given value."
    ]
}
```

> ❗️ Unique participation
>
> The `collect_uid` parameter identifies the participation in a unique way. This can be a string, a number, a date... You can, for example, concatenate an order ID, a reservation ID, a basket ID... with a timestamp. The most important thing is that this value must be unique.
>
> If the value of the `collect_uid` already exists, a `409` error is returned and the participation is not recorded.
>
> This parameter is not mandatory but strongly recommended: it lets you send the same file again safely if an import is interrupted.

> 🚧 A "201" does not mean the participation is created yet
>
> Historical participations are queued and created a few minutes later. Your payload is checked when you send it (format, point of sale, survey, questions, `collect_uid`) and any error is returned right away. The "201" then confirms that the participation has been accepted in the queue, not that it is already created.

![Historical import in four steps: send the payload to /responses/historical, it is checked right away and errors are sent back, then it is queued and a 201 is returned, and the participation is created later: check it with a GET request.](https://files.readme.io/1c7a6159419710b3cacea9933457252d9cf085a564fb108c10f2588b2e1fafe6-historical-import-timeline.png)

5. Check if everything is ok  
   A few minutes after your import, every participation you created with this method can be retrieved by calling the [/responses](ref:responses_list) endpoint with the `GET` method. You can add filters to this request to obtain the results for an end customer, a point of sale or a survey.  
   Then you can retrieve each participation to check that it matches your expectations.