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
**Congratulations**! You made the decision to change your CX partner and chose Goodays!

Now that the decision has been made, the excitement shifts into questions and how-to meetings. You had a previous partner that collected ratings, user data and contextual information.  
These precious data hold not go to waste and you wonder if and how all these informations could be transmitted to Goodays.  
Well, another congratulations! You reach the right place to learn everything about legacy retrieval !

## Why are your legacy data worth salvation ?

This question already answers a previous one : Does your legacy data worth salvation? The answer is obviously "**Yes**"!  
We are in the Data Era so no information is too small or too "irrelevant" not to have its rightful place in your ecosystem.  
Plus, it probably took some time to gather all these informations.  
Lastly and more importantly, these data are still valuable for their original purpose. They provide a history and ensure continuity for the KPIs you are following.

## How to - Basics

The process is actually pretty simple. However, depending on the volume of your data, it may take some time.

The simple part is telling the Goodays API to create new responses based on your previous data. It is a simple API call providing every information you want to have in Goodays.

> 🚧 Warning
>
> One part of this process can be tricky : there is no guarantee that the format of your legacy data will match the Goodays specifications without any transformation. Please make sure you handle the format differencies properly.

## Key takeaways

In a word : Yes, your legacy data can be integrated to Goodays!  
The process is simple but an analysis have to happen to detect potential format mismatches.

## How to - Expert

> 📘 Disclaimer
>
> These steps only covers the part where you create valid new responses to Goodays. Any previous transformation job you might have to do before is taken for granted.

The retrieval simply requires to call the `/responses`endpoint with the `POST` method and the correct payload.  
This payload will contain the list of all the answers of a participation. In order to create this array, you will need to get the surveys and the questions attached to properly match the Goodays questions and the legacy answers.

1. Get the surveys and the questions for each  
   Request the following endpoint : `/surveys`.  
   You will obtain something like this :

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
   Request the following endpoint : `/surveys/{survey-id}` with a survey-id retrieved from the previous requests.

Below, an example of the response :

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

Now that you have retrieved the surveys ids and the questions ids, you can generate the payload to insert your legacy responses to Goodays.

3. Create payloads  
   The payload you need to generate looks like the one below :

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
        "email": "arnaud.lancelot@goodays.co",
        "first_name": "Arnaud",
        "last_name": "Lancelot",
        "phone": "0123456789",
        "crm_id": "{crm-id}"
    },
    "context": {
      	"additional_information_1": "additionnal information 1"
    },
    "medium" : "WEB"
}
```

> ❗️ Participation date
>
> You should fill the `date` field with the date where the participation actually took place!

> 📘 Context
>
> To obtain the value for the context part request the following endpoint : [`/configuration`](ref:configuration_list).

> 📘 Answer values
>
> The expected `value` format depends on the question type: see [Surveys & Question Types](doc:surveys-question-types). For example, a Yes/No question takes `1` for yes and `0` for no.

4. Send the request  
   Once your payload is properly build, you can call the endpoint `/responses`with the POST method.  
   Don't forget to had your previous payload!

```curl
curl --location --request POST 'https://api.goodays.co/v2/responses' \
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

If the answer has been recorded, you will get a "_201: created_" back in the header.  
If not, an error will be returned in the endpoint return, for example:

```json
{
    "survey": [
        "No resource found for the given value."
    ]
}
```

<Callout icon="❗️">


  Allows the management of the unique participation.

  The `collect_uid` parameter is used to identify the participation in a unique way. This can be a string, a number, a date... You can, for example, concatenate an order ID, a reservation ID, a basket ID... with a timestamp. The most important thing is that this value must be unique.

  If the value of the `collect_uid` already exists then a 409 error is returned and the response is not recorded.

  This parameter is not mandatory but strongly recommended.
</Callout>

##

4. Check if everything is ok  
   Every response you created with this method can be retrieved by call the endpoint `/responses` with the GET method. You can add filters to this request to obtain the results given a user, a place or a survey.  
   Then you can retrieve individual response to check if the responses match your expectations.
