---
title: Participation retrieval
excerpt: Access raw participation data in real-time
deprecated: false
hidden: false
metadata:
  title: ''
  description: ''
  robots: index
next:
  description: ''
  pages:
    - type: link
      title: Response API Reference
      url: /reference/responses_list
---
The **Response API** lets you access the data your surveys collect — on demand and in JSON format — without setting up webhooks or third-party integrations.

> 👍 Going further
>
> Consult the [API Reference](/reference/responses_list) for more.

> 📘 Feel stuck ?
>
> Need help with an error? Head to [Troubleshooting and errors](/docs/errors) for more information.

# Key Concepts

With the Response API, you send a GET request each time you want to retrieve your data.

The response includes all the submissions your surveys have received so far, in JSON format. You can also add query parameters to your requests so that responses include only submissions received after a certain date and time or within a certain date range. The [Response API reference](/reference/levels_responses_bulk) lists and describes all of the available query parameters.

The bulk mode allows you to retrieve responses 20 by 20 (the paging is customizable).

# Use query parameters to retrieve specific data

Suppose you expect thousands of responses on your surveys. To keep your Response API requests manageable, you decide to retrieve your survey's data once each day. In other words, you'll retrieve yesterday's data today, today's data tomorrow, and so on. Because you don't want to retrieve every response to your surveys, you'll use the `start_date` and `end_date` query parameters to narrow the scope of your request and limit the API response by date.

Use `start_date` and `end_date` query parameters to retrieve a date range.

Let's assume today is July 10, 2019, and you're going to retrieve the previous day's data. Here's the walkthrough:

1. You'll still use the `GET https://api.goodays.co/v2/responses/bulk` endpoint, but don't send your request yet!

2. Add the `start_date` query parameter to your request. The `start_date` parameter is a string that uses ISO 8601 format, Coordinated Universal Time (UTC), with "T" as a delimiter between the date and time. July 10, 2019 at 12:00 a.m. UTC is expressed as 2019-07-10T00:00:00. If you want to retrieve responses for yesterday, 2019-07-09, the value for your `start_date` query parameter would be 2019-07-09T00:00:00. This means your response will include responses received since 12:00 a.m. UTC on July 9, 2019.

3. Add the `end_date` query parameter to your request. The `end_date` parameter is also a string in the same format as the `start_date` parameter. The value for your `end_date` query parameter would be 2019-07-10T00:00:00. This means your response will include responses received up until 12:00 a.m. UTC on July 10, 2019.

Here's what the cURL request looks like:

```curl
curl --location --request GET 'https://api.goodays.co/v2/responses/bulk? \
	start_date=2019-07-09T00:00:00Z \
  &end_date=2019-07-10T00:00:00Z' \
--header 'Content-Type: application/json' \
--header 'Authorization: {access-token}'
```

Now, you can send your request. The response will include only the responses that were submitted yesterday, July 9, 2019. Like this sample:

```json
{
    "next": "https://api.goodays.co/v2/responses/bulk?cursor=cD0yMDE5LTA3LTA5KzE0JTNBNTklM0E0OS42NTM3NjAlMkIwMCUzQTAw&end_date=2019-07-10T00%3A00%3A00Z&start_date=2019-07-09T00%3A00%3A00Z",
    "previous": null,
    "results": [
        {
            "id": "gxKrrlok4o",
            "token": "936d44f4d5a9a95c63b3f0cc7d4642477a9f03836b5efadddd373d114e84c423",
            "created_date": "2019-07-09T17:48:36.222412+02:00",
            "updated_date": "2019-07-09T17:48:36.254510+02:00",
            "google_review_date": null,
            "source": "email",
            "survey": {
                "id": "QOJ85mb8wE",
                "slug": "post_purchase_pos",
                "label": "Post purchase point of sale",
                "enabled": true,
                "detail_url": "https://api.goodays.co/v2/surveys/QOJ85mb8wE"
            },
            "answers": [
                {
                    "id": "vdJrLvWQdD",
                    "value": 8,
                    "question": {
                        "id": "1vdOBYlA8l",
                        "title": "Would you recommend Style to your friends and family?",
                        "type": "nps",
                        "enabled": true
                    }
                },
                {
                    "id": "y8V20vN28G",
                    "value": 4,
                    "question": {
                        "id": "pe8NzypJ8j",
                        "title": "Are you satisfied with your checkout experience?",
                        "type": "stars",
                        "enabled": true
                    }
                }
            ],
            "message": {
                "id": "58yj9M7qdw",
                "created_date": "2019-07-09T17:48:36.222412+02:00",
                "type": "Problem",
                "content": "I like this shop!",
                "attachment": null,
                "sender": {
                    "email": "george.abitbol@classe.com",
                    "first_name": "George",
                    "last_name": "Abitbol"
                }
            },
            "reply": null,
            "user": {
                "email": "george.abitbol@classe.com",
                "first_name": "George",
                "last_name": "Abitbol",
                "opt_in": {
                    "newsletter": false,
                    "email": false,
                    "sms": false,
                    "custom": false
                }
            },
            "context": {
                "email": "george.abitbol@classe.com",
                "phone": "06123456789",
                "crm_id": "",
                "last_name": "Abitbol",
                "first_name": "George",
                "extra": {
                    "order_id": "12345",
                    "title": "Mademoiselle"
                }
            },
            "place": {
                "id": "5gd0Lz1XdL",
                "partner_id": "142",
                "name": "Style Aix-en-Provence",
                "enabled": true,
                "detail_url": "https://api.goodays.co/v2/places/5gd0Lz1XdL"
            },
            "delegated_to": null,
            "attached_messages": [],
            "state": "open",
            "thread": "6dn1GnXl8E",
            "actions": {
                "reply": "https://api.goodays.co/api/v2/responses/gxKrrlok4o/reply",
                "spam": "https://api.goodays.co/api/v2/responses/gxKrrlok4o/spam",
                "close": "https://api.goodays.co/api/v2/responses/gxKrrlok4o/close"
            },
            "alert_triggered": false
        },
        {
            "id": "p4MZZJJBx2",
            "token": "ceabc8599d95d926cf617b0fe420c6f975e3f3deb83ced454e22f8e43b87b1b1",
            "created_date": "2019-07-09T16:59:49.653760+02:00",
            "updated_date": "2019-07-09T16:59:49.685842+02:00",
            "google_review_date": "2019-07-09T14:32:10.000000+02:00",
            "source": "google",
            "survey": {
                "id": "9v8XR0X43o",
                "slug": "gmb",
                "label": "Google",
                "enabled": true,
                "detail_url": "https://api.goodays.co/v2/surveys/9v8XR0X43o"
            },
            "answers": [
                {
                    "id": "vdJrLvWQdD",
                    "value": 5,
                    "question": {
                        "id": "1vdOBYlA8l",
                        "title": "Google rating",
                        "type": "csat",
                        "enabled": true
                    }
                }
            ],
            "message": null,
            "reply": null,
            "user": null,
            "context": {},
            "place": {
                "id": "okxwBz5B4y",
                "partner_id": "049",
                "name": "Style Ajaccio",
                "enabled": true,
                "detail_url": "https://api.goodays.co/v2/places/okxwBz5B4y"
            },
            "delegated_to": null,
            "attached_messages": [],
            "state": "open",
            "thread": null,
            "actions": {},
            "alert_triggered": false
        }
    ]
}
```

> 📘 The `google_review_date` attribute
>
> `google_review_date` is the date the review was actually posted on the Google Business Profile, as returned by Google. It's populated only for participations where `source` is `google`; it's `null` for every other source.
>
> Use it instead of `created_date` / `updated_date` when you need dates consistent with Google-side reporting (e.g. to match daily/weekly counts against the Google Score API or the Google statistics screen in the back office), since `created_date` / `updated_date` reflect Goodays' own collection lifecycle, not Google's publication date.

> 📘 Parsing the `answers` array
>
> The structure of the objects inside the `answers` array depends entirely on the type of question asked (e.g., NPS, CSAT, multiple choice).
>
> To properly parse this data and understand advanced behaviors like conditional logic (mother-daughter questions) or alert triggers, please consult our dedicated guide: **[Survey Question Types & Structures](doc:surveys-question-types)**.

# Response attributes

Each object in the `results` array represents a single participation. Here are the attributes exposed on it:

<Table align={["left","left","left"]}>
  <thead>
    <tr>
      <th>
        Attribute
      </th>

      <th>
        Type
      </th>

      <th>
        Description
      </th>
    </tr>
  </thead>

  <tbody>
    <tr>
      <td>**id**</td>
      <td>string</td>
      <td>Unique identifier of the participation.</td>
    </tr>

    <tr>
      <td>**token**</td>
      <td>string</td>
      <td>Unique token of the participation.</td>
    </tr>

    <tr>
      <td>**created_date**</td>
      <td>datetime</td>
      <td>Date the participation was created in Goodays.</td>
    </tr>

    <tr>
      <td>**updated_date**</td>
      <td>datetime</td>
      <td>Date the participation was last updated (survey continued, manager replied...).</td>
    </tr>

    <tr>
      <td>**google_review_date**</td>
      <td>datetime, nullable</td>
      <td>Date the review was posted on the Google Business Profile, as returned by Google. Populated only when `source` is `google`; `null` for every other source.</td>
    </tr>

    <tr>
      <td>**source**</td>
      <td>string</td>
      <td>Collection channel: `email`, `sms`, `google`, `facebook`, `widget`, `tripadvisor`, `wifi`, `terminal`...</td>
    </tr>

    <tr>
      <td>**survey**</td>
      <td>object</td>
      <td>Survey the participation belongs to (`id`, `slug`, `label`, `enabled`, `detail_url`).</td>
    </tr>

    <tr>
      <td>**answers**</td>
      <td>array</td>
      <td>Answers given to the survey's questions. See [Survey Question Types & Structures](doc:surveys-question-types).</td>
    </tr>

    <tr>
      <td>**message**</td>
      <td>object, nullable</td>
      <td>Initial verbatim left by the end customer, if any.</td>
    </tr>

    <tr>
      <td>**reply**</td>
      <td>object, nullable</td>
      <td>Reply sent by the point of sale's manager, if any.</td>
    </tr>

    <tr>
      <td>**user**</td>
      <td>object, nullable</td>
      <td>End customer identity (`email`, `first_name`, `last_name`, `opt_in`).</td>
    </tr>

    <tr>
      <td>**context**</td>
      <td>object</td>
      <td>Extra data sent at collection time (`email`, `phone`, `crm_id`, `extra`...).</td>
    </tr>

    <tr>
      <td>**place**</td>
      <td>object</td>
      <td>Point of sale the participation is attached to (`id`, `partner_id`, `name`, `enabled`, `detail_url`).</td>
    </tr>

    <tr>
      <td>**delegated_to**</td>
      <td>object, nullable</td>
      <td>Point of sale the handling was delegated to, if any.</td>
    </tr>

    <tr>
      <td>**attached_messages**</td>
      <td>array</td>
      <td>Additional messages exchanged on the same thread.</td>
    </tr>

    <tr>
      <td>**state**</td>
      <td>string</td>
      <td>Current state of the participation: `open`, `closed` or `spam`.</td>
    </tr>

    <tr>
      <td>**thread**</td>
      <td>string, nullable</td>
      <td>Identifier of the conversation thread.</td>
    </tr>

    <tr>
      <td>**actions**</td>
      <td>object</td>
      <td>URLs of the actions currently available on the participation (`reply`, `spam`, `call`, `close`), depending on its state.</td>
    </tr>

    <tr>
      <td>**alert_triggered**</td>
      <td>boolean</td>
      <td>Whether the participation triggered an alert.</td>
    </tr>
  </tbody>
</Table>

# Add some filters

It is possible to add GET parameters to refine the response list over a defined period, a point of sales...

## GET parameters

To refine the result, it is possible to combine the following GET parameters:

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
        **start_date**
      </td>

      <td>
        Start date of the collection period.  
        _Format : YYYY-MM-DDThh:mm:ssZ_  
        See [this page](doc:timezone-and-date-management) for the timezone management.
      </td>
    </tr>

    <tr>
      <td>
        **end_date**
      </td>

      <td>
        End date of the collection period.  
        _Format : YYYY-MM-DDThh:mm:ssZ_  
        See [this page](doc:timezone-and-date-management) for the timezone management.
      </td>
    </tr>

    <tr>
      <td>
        **date_field**
      </td>

      <td>
        Choose the date on which the period filter should be set.  
        See chapter [Choose the date to filter](a-response-at-once#choose-the-date-to-filter)

        :bulb: _We recommend that you systematically use this parameter in your API calls with the value`updated_date` to retrieve all entries that have been modified over the requested `start_date` / `end_date` period, and not just those created._
      </td>
    </tr>

    <tr>
      <td>
        **place**
      </td>

      <td>
        Filter on a point of sales.  
        _Enter your establishment code directly here._
      </td>
    </tr>

    <tr>
      <td>
        **survey**
      </td>

      <td>
        Filter on a survey.  
        See chapter [Retrieve the "survey-id"](a-response-at-once#retrieve-the-survey-id)
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
        **email**
      </td>

      <td>
        Filter on an End Customer email.
      </td>
    </tr>

    <tr>
      <td>
        **crm_id**
      </td>

      <td>
        Filter on a CRM ID (aka End Customer ID).
      </td>
    </tr>

    <tr>
      <td>
        **first_name**
      </td>

      <td>
        Filter on first name of the End Customer.
      </td>
    </tr>

    <tr>
      <td>
        **last_name**
      </td>

      <td>
        Filter on last name of the End Customer.
      </td>
    </tr>

    <tr>
      <td>
        **phone**
      </td>

      <td>
        Filter on phone of the End Customer.
      </td>
    </tr>

    <tr>
      <td>
        **has_answers**
      </td>

      <td>
        Filter on responses that have a survey answered (completely or partially) by the End Customer.

        Possible values: `true` or `false`.
      </td>
    </tr>

    <tr>
      <td>
        **has_message**
      </td>

      <td>
        Filter on response that have an initial textual message from the End Customer.

        Possible values: `true` or `false`.
      </td>
    </tr>

    <tr>
      <td>
        **has_reply**
      </td>

      <td>
        Filter on response that have already been replied from the Local Manager.

        Possible values: `true` or `false`.
      </td>
    </tr>
  </tbody>
</Table>

## Retrieve the "survey-id"

1. Call the endpoint url `https://api.goodays.co/v2/surveys` to obtain the ID corresponding to the right survey.
2. Then the "id" attribute is the answer.

## Choose the date to filter

A response includes two dates:

* The `created_date`: the date the response was created
* The`updated_date`: the date the response was last updated because the client continued to complete the survey, the manager responded...

To define on which date to base the date filter you have to use the parameter GET `date_field` with the value `updated_date` or `created_date`.

This is important if you don't want to miss any updates from your end customers!

# Example of filters

Retrieve the end customer's responses with a verbatim that have been answered by the local manager on a specific point of sales and survey and the source is the website:

```curl
curl --location --request GET 'https://api.goodays.co/v2/responses/bulk \
   ?survey=gxKrrlok4o \
   &place=ABC123 \
   &has_message=true \
   &has_answers=true \
   &has_reply=true \
   &source=widget' \
--header 'Content-Type: application/json' \
--header 'Authorization: {access-token}'
```
