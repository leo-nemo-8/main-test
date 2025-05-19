---
title: Create your interface with your Remote Customer Service
excerpt: ''
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
      title: API response
      url: https://critizr.readme.io/reference#response
---
You are using a dedicated Customer Service tool to respond to all or part of your customers' feedback? You use Goodays to collect customer feedback? Then you are on the right page!

The **Converse API** allows you to delegate the response to Goodays participations from a dedicated external tool — in JSON format — with setting up webhooks on a third-party integrations.

> 👍 Going further
> 
> Consult the [Response API](/reference#response) and [API events](/reference#events) for more.

> 📘 Feel stucked?
> 
> Need help with an error? Head to [Troubleshooting and errors](/docs/errors) for more information.

# Why use Converse API

- Enable you to manage the participations collected by Goodays outside its Back Office:

- In the case of partial delegation from the local to the Customer Service Department  
  E.g.: the local has the possibility of delegating an End Customer's remark for processing by Customer Service.

- In the case of total delegation to remote Customer Service  
  E.g.: Customer Service operates from a Salesforce-type tool.

# Key Concepts

The Converse API allows you to manage the participations collected by Goodays outside its Back Office.

We can send, through webhook, the participation to your third-party tool and retrieve the answers from your Customer Service to send them directly to your End Customers.

# For what purposes?

## Partial delegation to Remote Customer Service

In this solution, the remote Customer Service responds only to customer participations that are within its perimeter from its third-party tool. Customer participations destined for the local area are answered by the local area.

[block:image]
{
  "images": [
    {
      "image": [
        "https://files.readme.io/723ca20-image.png",
        null,
        "Partial delegation to Remote Customer Service"
      ],
      "align": "center",
      "caption": "Partial delegation to Remote Customer Service"
    }
  ]
}
[/block]


## Total delegation to Remote Customer Service

In this solution, the Remote Customer Service answers to all customer participations collected by Goodays from its third party tools.

[block:image]
{
  "images": [
    {
      "image": [
        "https://files.readme.io/3ed9350-image.png",
        null,
        "Total delegation to Remote Customer Service"
      ],
      "align": "center",
      "caption": "Total delegation to Remote Customer Service"
    }
  ]
}
[/block]


# How to - Basics

## Receive events from Goodays

With each new End Customer participation or new message to the Customer Service, the Goodays webhook calls the specific endpoint provided by you.

![](https://files.readme.io/2dbda95-image.png)

You have to set up, by your side, one endpoint to managed all these events triggered by the different hooks:

- A "response" handler to deal with the End Customer verbatim.

> 📘 
> 
> It is the first exchange with the End Customer, it contains the verbatim of the customer, the answers to the questions as well as the personal and additional data collected.

- A "message" handler to manage a possible private message from the End Customer in response to the Customer Service response.

> 📘 
> 
> Once Customer Service has responded to the End Customer's verbatim, the End Customer can continue the exchange through a "private message" visible only to the End Customer and the Customer Service.

- A "delegate" handler, only needed for the partial delegation mode, to deal with the local delegation to the Customer Service.

> 📘 
> 
> If a local establishment considers that it cannot respond to an End Customer verbatim, it can delegate it to Customer Service.

The Converse API will send event to your endpoint every time these actions are triggered.

## Send actions from the Customer Service to the End Customer

![](https://files.readme.io/2137d4d-image.png)

The actions that Customer Service can perform on an End Customer return are:

- Reply to the End Customer participation:

The main functionality: Customer Service simply responds to the End Customer's return by text.

- Mark the End Customer's message as handled by a phone call (with the optional addition of a private note):

If your Customer Service processes a customer message directly by phone, this will close the thread on the Goodays side. It is also possible to add a "private note" to summarize the phone exchange between Customer Service and the End Customer.

- Mark the End Customer's message as closed without reply:

If your Customer Service considers that an End Customer return does not require answer or telephone processing, it is possible to close the thread directly on the Goodays side.

- Mark the customer's return as spam:

If your Customer Service considers that an End Customer's return is a spam, they can report it to Goodays.

- Reply to a private message from the end customer

If the end customer has replied to your first answer, Customer Service can respond in turn.

# How to - Expert

## Receive events from Goodays

As said before you have to set up the endpoint allowing Goodays to send you the entries and private messages of your End Customer.

Once your endpoint is up and running, you must provide us its URL so we can set up the webhook.

> 🚧 Data transcoding
> 
> No data transcoding is done on the webhook side by Goodays. Any next transformation job you might have to do after is taken for granted.

> 📘 Samples
> 
> You can obtain samples corresponding to your configuration by calling the "[events](ref:events)" endpoint.

### Securing your webhook

Or how to make sure that you only receive data from Goodays?

To allow you to make sure that responses come from Goodays we recommend that you implement an authentication in the header of your endpoint.

By default we are compatible with the HMAC standard and the SHA256 hash algorithm:

- If this option is chosen we will systematically include in the header `X-HMAC-SHA256` a signature containing the encrypted value generated from the `secret key` -_that we will have agreed upon beforehand (to be defined with your Goodays technical referent)_- and the `body` of the API call.  
  You must then verify that the value of the signature is correct to authenticate the response.

- If no _secret key_ is defined then we don't add anything in the header.

Example:

- The _secret key_ is `Goodays`
- The body is:

```json
{
    "event_type": "response"
}
```

Then we will add in the header of each call:

```cypher Header
X-HMAC-SHA256 = bcf95bdaa6dae4e97a44eb8d65273d3c5459f9a258b68c26f10d6cc69b359b51
```

> 📘 
> 
> The content of the parameter `X-HMAC-SHA256` will therefore change with each request.

### Receive a "response" from an End Customer

This event is triggered when an End Customer send a [response](ref:events_sample_response).

Here is an example of the payload received for this event:

```json Sample response
{
    "event_type": "response",
    "response": {
        "id": "vdOpL1NJ74l",
        "token": "1234abcd1234abcd1234abcd1234abcd",
        "created_date": "2020-02-05T10:20:39.810686+01:00",
        "updated_date": "2020-02-05T10:21:15.952136+01:00",
        "source": "email",
        "survey": {
            "id": "12AB34",
            "slug": "survey1",
            "label": "survey 1",
            "enabled": true,
            "detail_url": "https://api.goodays.co/v2/surveys/12AB34"
        },
        "answers": [
            {
                "id": "12AB34",
                "value": 5,
                "question": {
                    "id": "12AB34",
                    "title": "**Recommanderiez-vous** ce magasin à votre entourage ?",
                    "type": "nps",
                    "enabled": true
                }
            }
        ],
        "message": {
            "id": "12AB34",
            "created_date": "2020-02-05T10:20:39.810686+01:00",
            "type": "Problem",
            "content": "The seller needs to respond in a timely manner and respond to my needs. Often the information provided was incorrect or did not answer the query. We found this experience very frustrating.",
            "attachment": null,
            "sender": {
                "email": "chester.copperpot@astoria.com",
                "first_name": "Chester",
                "last_name": "COPPERPOT"
            }
        },
        "reply": null,
        "user": {
            "email": "chester.copperpot@astoria.com",
            "first_name": "Chester",
            "last_name": "COPPERPOT",
            "opt_in": {
                "newsletter": false,
                "email": false,
                "sms": false
            }
        },
        "context": {
            "email": "chester.copperpot@astoria.com",
            "extra": {
                "transaction_date": "2020-01-28"
            },
            "cz_tag": "survey1",
            "crm_id": "",
            "last_name": "COPPERPOT",
            "first_name": "Chester"
        },
        "place": {
            "id": "12AB34",
            "partner_id": "1234",
            "name": "place name",
            "enabled": true,
            "detail_url": "https://api.goodays.co/v2/places/12AB34"
        },
        "delegated_to": null,
        "attached_messages": [],
        "state": "open",
        "thread": "z4RjEyMP4r",
        "actions": {
            "reply": "https://api.goodays.co/api/v2/responses/vdOpL1NJ74l/reply",
            "spam": "https://api.goodays.co/api/v2/responses/vdOpL1NJ74l/spam",
            "close": "https://api.goodays.co/api/v2/responses/vdOpL1NJ74l/close",
            "call": "https://api.goodays.co/api/v2/responses/vdOpL1NJ74l/call"
        },
        "alert_triggered": false
    }
}
```

Focus on important attributes:

| Attribute name | Description                                                                                     |
| :------------- | :---------------------------------------------------------------------------------------------- |
| event_type     | The type of event that triggered the transmission: response, message, delegated                 |
| survey         | The questionnaire answered by the end customer                                                  |
| answers        | The final client's answers to the survey                                                        |
| message        | The end customer's verbatim                                                                     |
| attachment     | Contains a web link to the resource shared by the end customer: image or document               |
| user           | Information on the end customer                                                                 |
| context        | Additional data provided by our common client to provide context to the end customer's response |
| place          | Establishment information                                                                       |
| state          | Thread status: open, closed or pending                                                          |
| actions        | The only possible actions on the end customer response: reply, spam, close and call             |

### Receive a "message" from an End Customer

This event is triggered when an End Customer send a [private message](ref:events_sample_message) in a conversation with you. This event can only occur after this End Customer send a response and you replied to it.

Here is an example of the payload received for this event:

```json Sample message
{
    "event_type": "message",
    "response": {
        "id": "vdOpL1NJ74l",
        "token": "1234abcd1234abcd1234abcd1234abcd",
        "created_date": "2020-02-05T10:20:39.810686+01:00",
        "updated_date": "2020-02-05T10:20:39.810686+01:00",
        "source": "email",
        "survey": {
            "id": "12AB34",
            "slug": "survey1",
            "label": "survey 1",
            "enabled": true,
            "detail_url": "https://api.goodays.co/v2/surveys/12AB34"
        },
        "answers": [
            {
                "id": "12AB34",
                "value": 5,
                "question": {
                    "id": "12AB34",
                    "title": "Suite à votre dernière visite, recommanderiez-vous votre magasin /PLACE/ à votre entourage ?",
                    "type": "nps",
                    "enabled": true
                }
            }
        ],
        "message": {
            "id": "mxo1B0eGdj",
            "created_date": "2020-02-05T10:20:39.810686+01:00",
            "type": "Problem",
            "content": "The seller needs to respond in a timely manner and respond to my needs. Often the information provided was incorrect or did not answer the query. We found this experience very frustrating.",
            "attachment": null,
            "sender": {
                "email": "chester.copperpot@astoria.com",
                "first_name": "Chester",
                "last_name": "COPPERPOT"
            }
        },
        "reply": {
            "id": "54EjZ70lxy",
            "created_date": "2020-02-05T12:20:39.810686+01:00",
            "type": "text",
            "content": "Dear Customer, thank you for your feedback. We are sorry for the inconvenience. What information you were looking for? Regards,",
            "attachment": null,
            "sender": {
                 "email": "jennifer.parker@hillvalley.com",
                 "first_name": "Jennifer",
                 "last_name": "Parker"
            }
        },
        "user": {
            "email": "chester.copperpot@astoria.com",
            "first_name": "Chester",
            "last_name": "COPPERPOT",
            "opt_in": {
                "newsletter": false,
                "email": false,
                "sms": false
            }
        },
        "context": {
            "email": "chester.copperpot@astoria.com",
            "extra": {
                "transaction_date": "2020-01-28",
                "transaction_time": "17:47:00"
            },
            "cz_tag": "survey1",
    				"crm_id": "",
            "last_name": "COPPERPOT",
            "first_name": "Chester"
        },
        "place": {
            "id": "jdprBX2pxM",
            "partner_id": "1234",
            "name": "place name",
            "enabled": true,
            "detail_url": "https://api.goodays.co/v2/places/12AB34"
        },
        "delegated_to": null,
        "attached_messages": [
            {
                "id": "vdJmjjLk8D",
                "created_date": "2020-02-06T09:20:39.810686+01:00",
                "type": "Message",
                "content": "Thank you for your response. I need more information about your current backpack promotion: how long does it last?",
                "attachment": null,
                "sender": {
                    "email": "chester.copperpot@astoria.com",
                    "first_name": "Chester",
                    "last_name": "Copperpot"
                }
            },
            {
                "id": "54EjZ70lxy",
                "created_date": "2020-02-05T12:20:39.810686+01:00",
                "type": "Message",
                "content": "Dear Customer, thank you for your feedback. We are sorry for the inconvenience. What information you were looking for? Regards,",
                "attachment": null,
                "sender": {
                    "email": "jennifer.parker@hillvalley.com",
                    "first_name": "Jennifer",
                    "last_name": "Parker"
                }
            }
        ],
        "state": "closed",
        "thread": "12AB34",
        "actions": {
            "message": "https://api.goodays.co/api/v2/responses/vdOpL1NJ74l/message"
        },
        "alert_triggered": false
    },
    "message": {
        "id": "vdJmjjLk8D",
        "created_date": "2020-02-06T09:20:39.810686+01:00",
        "type": "Message",
        "content": "Thank you for your response. I need more information about your current backpack promotion: how long does it last?",
        "attachment": null,
        "sender": {
            "email": "chester.copperpot@astoria.com",
            "first_name": "Chester",
            "last_name": "COPPERPOT"
        }
    }
}
```

Focus on important new attributes:

| Attribute name    | Description                                                                                |
| :---------------- | :----------------------------------------------------------------------------------------- |
| reply             | Contains the Customer Service response to the verbatim of the end customer                 |
| attached_messages | The list of past exchanges in the thread between the end customer and the Customer Service |
| message           | The return (private message) of the end customer to Customer Service                       |

### Receive a "delegation" from a Local Manager

This event is triggered when a local user faces a question he doesn't know how to respond to. He can "ask for help" and [delegate the answer](ref:events_sample_delegated) to the Customer Service.

Here is an example of the payload received for this event:

```json Sample delegated
{
    "event_type": "delegated",
    "response": {
        "id": "vdOpL1NJ74l",
        "token": "1234abcd1234abcd1234abcd1234abcd",
        "created_date": "2020-01-29T14:07:04.765852+01:00",
        "updated_date": "2020-01-29T14:13:08.014586+01:00",
        "source": "email",
        "survey": {
            "id": "12AB34",
            "slug": "survey1",
            "label": "survey 1",
            "enabled": true,
            "detail_url": "https://api.goodays.co/v2/surveys/12AB34"
        },
        "answers": [
            {
                "id": "12AB34",
                "value": 5,
                "question": {
                    "id": "12AB34",
                    "title": "**Recommanderiez-vous** ce magasin à votre entourage ?",
                    "type": "nps",
                    "enabled": true
                }
            }
        ],
        "message": {
            "id": "mxo1B0eGdj",
            "created_date": "2020-01-29T14:13:07.913925+01:00",
            "type": "Problem",
            "content": "The seller needs to respond in a timely manner and respond to my needs. Often the information provided was incorrect or did not answer the query. We found this experience very frustrating.",
            "attachment": null,
            "sender": {
                "email": "chester.copperpot@astoria.com",
                "first_name": "Chester",
                "last_name": "COPPERPOT"
            }
        },
        "reply": null,
        "user": {
            "email": "chester.copperpot@astoria.com",
            "first_name": "Chester",
            "last_name": "COPPERPOT",
            "opt_in": {
                "newsletter": false,
                "email": false,
                "sms": false
            }
        },
        "context": {
            "email": "chester.copperpot@astoria.com",
            "phone": "",
            "crm_id": "12AB34",
            "extra": {
                "transaction_date": "2020-01-28",
                "title": "Mr"
            },
            "last_name": "COPPERPOT",
            "first_name": "Chester"
        },
        "place": {
            "id": "12AB34",
            "partner_id": "1234",
            "name": "place name",
            "enabled": true,
            "detail_url": "https://api.goodays.co/v2/places/12AB34"
        },
        "delegated_to": {
            "id": "ap4M7B1w82",
            "partner_id": "CustomerService",
            "name": "Customer Service",
            "enabled": true,
            "detail_url": "https://api.goodays.co/v2/places/ap4M7B1w82"
        },
        "attached_messages": [],
        "state": "open",
        "thread": "12AB34",
        "actions": {
            "reply": "https://api.goodays.co/api/v2/responses/12AB34/reply",
            "spam": "https://api.goodays.co/api/v2/responses/12AB34/spam",
            "close": "https://api.goodays.co/api/v2/responses/12AB34/close"
        },
        "alert_triggered": false
    }
}
```

Focus on important new attributes:

| Attribute name | Description                                                                                                       |
| :------------- | :---------------------------------------------------------------------------------------------------------------- |
| delegated_to   | Contains the information of the establishment to which the client's response is delegated. Here: Customer Service |

## Send actions from the Customer Service to the End Customer

Two Goodays endpoints allows you to process an End Customer's feedback or private message:

[block:image]
{
  "images": [
    {
      "image": [
        "https://files.readme.io/5a3361e-image.png",
        null,
        null
      ],
      "align": "center",
      "caption": "Main use case: processing of End Customer's feedback"
    }
  ]
}
[/block]


[block:image]
{
  "images": [
    {
      "image": [
        "https://files.readme.io/3d5a486-image.png",
        null,
        null
      ],
      "align": "center",
      "caption": "Secondary Use Case: processing of End Customer's response"
    }
  ]
}
[/block]


> ❗️ The Goodays Back Office management rules apply.
> 
> The possible actions for each response or message are listed in the "actions" attribute. Please use them.
> 
> E.g.:
> 
> - you cannot send a message without having processed the initial response previously
> - you cannot put in spam if an entry is already processed.

> 🚧 Process each End Customer response or message
> 
> To allow a good management of the response statistics it is very important to process each End Customer's return (even with a "closed without reply").

The different possibilities are:

### Reply to the End Customer feedback

With [`/responses/{response-id}/reply`](ref:responses_reply):

```json Sample reply
{
  "content": "Dear Customer, thank you for your feedback. We are sorry for the inconvenience. What information you were looking for? Regards,",
  "user": "1a2b3c4",
  "remark_type": "Problem"
}
```

> 📘 "user" attribute
> 
> The "user" attribute is your user ID that you can obtain with Users API: `/users?email={your email}`.  
> It is optional when you do processing on a response.

> 📘 "remark_type" attribute
> 
> The "remark_type" is mandatory when the initial response source is not Goodays.  
> E.g.: a Google feedback.
> 
> The possible values are:
> 
> - Praise
> - Question
> - Idea
> - Problem
> 
> If you can't implement Google reviews typing then you should always push `Message` value.  
> i.e. `"remark_type": "Message"`

### Reply to the End Customer private message

With [`/responses/{response-id}/message`](ref:responses_message):

```json Sample reply by message
{
  "user": "1a2b3c4",
  "content": "Dear customer, thank you for your interest in our range of backpacks: our promotion lasts until 19/03/2020. We hope to see you soon in our shop! Regards,"
}
```

Or for a Google message:

```json
{
  "user": "1a2b3c4",
  "content": "Dear customer, thank you for your interest in our range of backpacks: our promotion lasts until 19/03/2020. We hope to see you soon in our shop! Regards,",
  "remark_type": "Message"
}
```

### Mark the End Customer's return as handled by a phone call (with optional addition of a rating and a private note)

With [`/responses/{response-id}/call`](ref:responses_call):

```json Sample reply by call
{
  "user": "1a2b3c4",
  "rating": 5,
  "note": "The conversation with the End Customer was good, it's a misunderstanding."
}
```

> 📘 "note" and "rate" attribute
> 
> The "note" and "rate" attributes are facultative:
> 
> - The "note" attribute (0-5) permit to add some private note about the End Customer call (Eg: give more context about the dissatisfaction of the End Customer).
> - The "rate" gives the possibility to the Customer Service to rate the End Customer call.

### Mark the End Customer's return as closed without reply

With [`/responses/{response-id}/close`](ref:responses_close):

```json Sample reply without reply
{
  "user": "1a2b3c4",
  "remark_type": "Problem"
}
```

### Mark the customer's return as spam

With [`/responses/{response-id}/spam`](ref:responses_spam):

```json Sample reply as spam
{
  "user": "1a2b3c4"
}
```

# Use cases

## Customer Service handles the response of an End Customer

Let's imagine that an operator in your Customer Service has received a response from an End Customer via the Goodays webhook. We are in the "public message" section: the final End Customers remark and the operator's answer could possibly be published on the site of our common customer.

### Receive the response

As a preliminary, we have sent the End Customer's response to your endpoint "response":

```json Customer's response
{
    "event_type": "response",
    "response": {
        "id": "vdOpL1NJ74l",
        "token": "1234abcd1234abcd1234abcd1234abcd",
        "created_date": "2020-02-05T10:20:39.810686+01:00",
        "updated_date": "2020-02-05T10:21:15.952136+01:00",
        "source": "email",
        "survey": {
            "id": "12AB34",
            "slug": "survey1",
            "label": "survey 1",
            "enabled": true,
            "detail_url": "https://api.goodays.co/v2/surveys/12AB34"
        },
        "answers": [
            {
                "id": "12AB34",
                "value": 5,
                "question": {
                    "id": "12AB34",
                    "title": "**Recommanderiez-vous** ce magasin à votre entourage ?",
                    "type": "nps",
                    "enabled": true
                }
            }
        ],
        "message": {
            "id": "12AB34",
            "created_date": "2020-02-05T10:20:39.810686+01:00",
            "type": "Problem",
            "content": "The seller needs to respond in a timely manner and respond to my needs. Often the information provided was incorrect or did not answer the query. We found this experience very frustrating.",
            "attachment": null,
            "sender": {
                "email": "chester.copperpot@astoria.com",
                "first_name": "Chester",
                "last_name": "COPPERPOT"
            }
        },
        "reply": null,
        "user": {
            "email": "chester.copperpot@astoria.com",
            "first_name": "Chester",
            "last_name": "COPPERPOT",
            "opt_in": {
                "newsletter": false,
                "email": false,
                "sms": false
            }
        },
        "context": {
            "email": "chester.copperpot@astoria.com",
            "phone": "",
            "crm_id": "12AB34",
            "extra": {
                "transaction_date": "2020-01-28",
                "transaction_time": "17:47:00"
            },
            "last_name": "COPPERPOT",
            "first_name": "Chester"
        },
        "place": {
            "id": "12AB34",
            "partner_id": "1234",
            "name": "place name",
            "enabled": true,
            "detail_url": "https://api.goodays.co/v2/places/12AB34"
        },
        "delegated_to": null,
        "attached_messages": [],
        "state": "open",
        "thread": "z4RjEyMP4r",
        "actions": {
            "reply": "https://api.goodays.co/api/v2/responses/vdOpL1NJ74l/reply",
            "spam": "https://api.goodays.co/api/v2/responses/vdOpL1NJ74l/spam",
            "close": "https://api.goodays.co/api/v2/responses/vdOpL1NJ74l/close",
            "call": "https://api.goodays.co/api/v2/responses/vdOpL1NJ74l/call"
        },
        "alert_triggered": false
    }
}
```

### Process the response

> 🚧 You need to processed each response send
> 
> It is important to provide Goodays with a processing status for each response provided.  
> The reply rate and processing time are part of the KPIs monitored by our common customer.

Here are, in concrete terms, the possible actions on your side:

- Your operator can directly call the End Customer, after that action you must notify Goodays to mark response as completed:

```curl Call
curl --location --request PUT 'https://api.goodays.co/v2/responses/vdOpL1NJ74l/call' \
--header 'Content-Type: application/json' \
--header 'Authorization: 1234abcd1234abcd1234abcd1234abcd' \
--data-raw '{
  "user": "1a2b3c4",
  "rating": 5,
  "note": "The conversation with the End Customer was good, it'\''s a misunderstanding."
}'
```

- **OR** your operator can reply with a text message:

```curl Reply
curl --location --request PUT 'https://api.goodays.co/v2/responses/646RjJ5Z49/reply' \
--header 'Content-Type: application/json' \
--header 'Authorization: 1234abcd1234abcd1234abcd1234abcd' \
--data-raw '{
  "user": "1a2b3c4",
  "content": "Dear Customer, thank you for your feedback. We are sorry for the inconvenience. What information you were looking for? Regards,"
}'
```

- **OR**, if your operator judges that the task does not require an answer, he can close it without any exchange with the End Customer:

```curl Close without reply
curl --location --request PUT 'https://api.goodays.co/v2/responses/vdOpL1NJ74l/close' \
--header 'Content-Type: application/json' \
--header 'Authorization: 1234abcd1234abcd1234abcd1234abcd' \
--data-raw '{
  "user": "1a2b3c4"
}'
```

- **OR**, if your operator deems that the End Customer's response is spam, please report it to us:

```curl Spam
curl --location --request PUT 'https://api.goodays.co/v2/responses/vdOpL1NJ74l/spam' \
--header 'Content-Type: application/json' \
--header 'Authorization: 1234abcd1234abcd1234abcd1234abcd' \
--data-raw '{
  "user": "1a2b3c4"
}'
```

## The End Customer responds to Customer Service

Let's imagine that, following the operator's reply, the End Customer replies in turn: we then enter the "private message" section. The rest of the exchange will remain between you and the End Customer

### Receive the message from the End Customer

As a preliminary, we have sent the End Customer's message to your endpoint "message":

```json Customer's message
{
    "event_type": "message",
    "response": {
        "id": "vdOpL1NJ74l",
        "token": "1234abcd1234abcd1234abcd1234abcd",
        "created_date": "2020-02-05T10:20:39.810686+01:00",
        "updated_date": "2020-02-05T10:20:39.810686+01:00",
        "source": "email",
        "survey": {
            "id": "12AB34",
            "slug": "survey1",
            "label": "survey 1",
            "enabled": true,
            "detail_url": "https://api.goodays.co/v2/surveys/12AB34"
        },
        "answers": [
            {
                "id": "12AB34",
                "value": 5,
                "question": {
                    "id": "12AB34",
                    "title": "Suite à votre dernière visite, recommanderiez-vous votre magasin /PLACE/ à votre entourage ?",
                    "type": "nps",
                    "enabled": true
                }
            }
        ],
        "message": {
            "id": "mxo1B0eGdj",
            "created_date": "2020-02-05T10:20:39.810686+01:00",
            "type": "Problem",
            "content": "The seller needs to respond in a timely manner and respond to my needs. Often the information provided was incorrect or did not answer the query. We found this experience very frustrating.",
            "attachment": null,
            "sender": {
                "email": "chester.copperpot@astoria.com",
                "first_name": "Chester",
                "last_name": "COPPERPOT"
            }
        },
        "reply": {
            "id": "54EjZ70lxy",
            "created_date": "2020-02-05T12:20:39.810686+01:00",
            "type": "text",
            "content": "Dear Customer, thank you for your feedback. We are sorry for the inconvenience. What information you were looking for? Regards,",
            "attachment": null,
            "sender": {
                 "email": "jennifer.parker@hillvalley.com",
                 "first_name": "Jennifer",
                 "last_name": "Parker"
            }
        },
        "user": {
            "email": "chester.copperpot@astoria.com",
            "first_name": "Chester",
            "last_name": "COPPERPOT",
            "opt_in": {
                "newsletter": false,
                "email": false,
                "sms": false
            }
        },
        "context": {
            "email": "chester.copperpot@astoria.com",
            "extra": {
                "transaction_date": "2020-01-28",
                "transaction_time": "17:47:00"
            },
            "cz_tag": "survey1",
            "last_name": "COPPERPOT",
    				"crm_id": "",
            "first_name": "Chester"
        },
        "place": {
            "id": "jdprBX2pxM",
            "partner_id": "1234",
            "name": "place name",
            "enabled": true,
            "detail_url": "https://api.goodays.co/v2/places/12AB34"
        },
        "delegated_to": null,
        "attached_messages": [
            {
                "id": "vdJmjjLk8D",
                "created_date": "2020-02-06T09:20:39.810686+01:00",
                "type": "Message",
                "content": "Thank you for your response. I need more information about your current backpack promotion: how long does it last?",
                "attachment": null,
                "sender": {
                    "email": "chester.copperpot@astoria.com",
                    "first_name": "Chester",
                    "last_name": "Copperpot"
                }
            },
            {
                "id": "54EjZ70lxy",
                "created_date": "2020-02-05T12:20:39.810686+01:00",
                "type": "Message",
                "content": "Dear Customer, thank you for your feedback. We are sorry for the inconvenience. What information you were looking for? Regards,",
                "attachment": null,
                "sender": {
                    "email": "jennifer.parker@hillvalley.com",
                    "first_name": "Jennifer",
                    "last_name": "Parker"
                }
            }
        ],
        "state": "closed",
        "thread": "12AB34",
        "actions": {
            "message": "https://api.goodays.co/api/v2/responses/vdOpL1NJ74l/message"
        },
        "alert_triggered": false
    },
    "message": {
        "id": "vdJmjjLk8D",
        "created_date": "2020-02-06T09:20:39.810686+01:00",
        "type": "Message",
        "content": "Thank you for your response. I need more information about your current backpack promotion: how long does it last?",
        "attachment": null,
        "sender": {
            "email": "chester.copperpot@astoria.com",
            "first_name": "Chester",
            "last_name": "COPPERPOT"
        }
    }
}
```

### Process the message

> 🚧 Need to process the message
> 
> It is important to provide Goodays with a processing status for each response provided.  
> Even if no answer is needed.

Here are, in concrete terms, the possible actions on your side:

- Your operator can reply with a text message:

```curl Private message
curl --location --request PUT 'https://api.goodays.co/v2/responses/vdOpL1NJ74l/message' \
--header 'Content-Type: application/json' \
--header 'Authorization: 1234abcd1234abcd1234abcd1234abcd' \
--data-raw '{
  "user": "1a2b3c4",
  "content": "Dear customer, thank you for your interest in our range of backpacks: our promotion lasts until 19/03/2020. We hope to see you soon in our shop! Regards,"
}'
```

### The loop message

The End Customer and Customer Service can continue to exchange in "private message" mode until a new "response" from the End Customer arrives.

> 📘 Loop message and new response
> 
> If a new "response" from the End Customer arrives we get out of the loop message.

In this case, the payload sent to your endpoint "message" will look like this:

```json Customer's message
{
    "event_type": "message",
    "response": {
        "id": "vdOpL1NJ74l",
        "token": "1234abcd1234abcd1234abcd1234abcd",
        "created_date": "2020-02-05T10:20:39.810686+01:00",
        "updated_date": "2020-02-05T10:20:39.810686+01:00",
        "source": "email",
        "survey": {
            "id": "12AB34",
            "slug": "survey1",
            "label": "survey 1",
            "enabled": true,
            "detail_url": "https://api.goodays.co/v2/surveys/12AB34"
        },
        "answers": [
            {
                "id": "12AB34",
                "value": 5,
                "question": {
                    "id": "12AB34",
                    "title": "Suite à votre dernière visite, recommanderiez-vous votre magasin /PLACE/ à votre entourage ?",
                    "type": "nps",
                    "enabled": true
                }
            }
        ],
        "message": {
            "id": "mxo1B0eGdj",
            "created_date": "2020-02-05T10:20:39.810686+01:00",
            "type": "Problem",
            "content": "The seller needs to respond in a timely manner and respond to my needs. Often the information provided was incorrect or did not answer the query. We found this experience very frustrating.",
            "attachment": null,
            "sender": {
                "email": "chester.copperpot@astoria.com",
                "first_name": "Chester",
                "last_name": "COPPERPOT"
            }
        },
        "reply": {
            "id": "54EjZ70lxy",
            "created_date": "2020-02-05T12:20:39.810686+01:00",
            "type": "text",
            "content": "Dear Customer, thank you for your feedback. We are sorry for the inconvenience. What information you were looking for? Regards,",
            "attachment": null,
            "sender": {
                 "email": "jennifer.parker@hillvalley.com",
                 "first_name": "Jennifer",
                 "last_name": "Parker"
            }
        },
        "user": {
            "email": "chester.copperpot@astoria.com",
            "first_name": "Chester",
            "last_name": "COPPERPOT",
            "opt_in": {
                "newsletter": false,
                "email": false,
                "sms": false
            }
        },
        "context": {
            "email": "chester.copperpot@astoria.com",
            "extra": {
                "transaction_date": "2020-01-28",
                "transaction_time": "17:47:00"
            },
            "cz_tag": "survey1",
    				"crm_id": "",
            "last_name": "COPPERPOT",
            "first_name": "Chester"
        },
        "place": {
            "id": "jdprBX2pxM",
            "partner_id": "1234",
            "name": "place name",
            "enabled": true,
            "detail_url": "https://api.goodays.co/v2/places/12AB34"
        },
        "delegated_to": null,
        "attached_messages": [
            {
                "id": "exqmBvGmxY",
                "created_date": "2020-02-10T16:20:39.810686+01:00",
                "type": "Message",
                "content": "Thank you! See you soon 😊",
                "attachment": null,
                "sender": {
                    "email": "chester.copperpot@astoria.com",
                    "first_name": "Chester",
                    "last_name": "Copperpot"
                }
            },
            {
                "id": "LdLD59eedj",
                "created_date": "2020-02-06T13:33:39.810686+01:00",
                "type": "Message",
                "content": "Dear customer, thank you for your interest in our range of backpacks: our promotion lasts until 19/03/2020. We hope to see you soon in our shop! Regards,",
                "attachment": null,
                "sender": {
                    "email": "jennifer.parker@hillvalley.com",
                    "first_name": "Jennifer",
                    "last_name": "Parker"
                }
            },
            {
                "id": "vdJmjjLk8D",
                "created_date": "2020-02-06T09:20:39.810686+01:00",
                "type": "Message",
                "content": "Thank you for your response. I need more information about your current backpack promotion: how long does it last?",
                "attachment": null,
                "sender": {
                    "email": "chester.copperpot@astoria.com",
                    "first_name": "Chester",
                    "last_name": "Copperpot"
                }
            },
            {
                "id": "54EjZ70lxy",
                "created_date": "2020-02-05T12:20:39.810686+01:00",
                "type": "Message",
                "content": "Dear Customer, thank you for your feedback. We are sorry for the inconvenience. What information you were looking for? Regards,",
                "attachment": null,
                "sender": {
                    "email": "jennifer.parker@hillvalley.com",
                    "first_name": "Jennifer",
                    "last_name": "Parker"
                }
            }
        ],
        "state": "closed",
        "thread": "12AB34",
        "actions": {
            "message": "https://api.goodays.co/api/v2/responses/vdOpL1NJ74l/message"
        },
        "alert_triggered": false
    },
    "message": {
        "id": "exqmBvGmxY",
        "created_date": "2020-02-10T16:20:39.810686+01:00",
        "type": "Message",
        "content": "Thank you! See you soon 😊",
        "attachment": null,
        "sender": {
            "email": "chester.copperpot@astoria.com",
            "first_name": "Chester",
            "last_name": "COPPERPOT"
        }
    }
}
```

## The Local Manager delegate the response of an End Customer to the Customer Service

It is possible that a response from an End Customer cannot be processed by the Local Manager, in which case it is possible to delegate the End Customer's response (and possible private messages) to Customer Service.  
In this case the response is moved from his establishment directly to the Customer Service. The Local Manager no longer has access to this response.

> 📘 Possible actions after a Local Manager delegation
> 
> Once the delegation has been made by the Local Manager, the actions are the same as in the chapter "[Customer Service handles the response of an End Customer](#section-customer-service-handles-the-response-of-an-end-customer)".

Then, we send the response to your endpoint "response" with the "event_type" on "delegated":

```json Delegate the End Customer response
{
    "event_type": "delegated",
    "response": {
        "id": "vdOpL1NJ74l",
        "token": "1234abcd1234abcd1234abcd1234abcd",
        "created_date": "2020-01-29T14:07:04.765852+01:00",
        "updated_date": "2020-01-29T14:13:08.014586+01:00",
        "source": "email",
        "survey": {
            "id": "12AB34",
            "slug": "survey1",
            "label": "survey 1",
            "enabled": true,
            "detail_url": "https://api.goodays.co/v2/surveys/12AB34"
        },
        "answers": [
            {
                "id": "12AB34",
                "value": 5,
                "question": {
                    "id": "12AB34",
                    "title": "**Recommanderiez-vous** ce magasin à votre entourage ?",
                    "type": "nps",
                    "enabled": true
                }
            }
        ],
        "message": {
            "id": "mxo1B0eGdj",
            "created_date": "2020-01-29T14:13:07.913925+01:00",
            "type": "Problem",
            "content": "The seller needs to respond in a timely manner and respond to my needs. Often the information provided was incorrect or did not answer the query. We found this experience very frustrating.",
            "attachment": null,
            "sender": {
                "email": "chester.copperpot@astoria.com",
                "first_name": "Chester",
                "last_name": "COPPERPOT"
            }
        },
        "reply": null,
        "user": {
            "email": "chester.copperpot@astoria.com",
            "first_name": "Chester",
            "last_name": "COPPERPOT",
            "opt_in": {
                "newsletter": false,
                "email": false,
                "sms": false
            }
        },
        "context": {
            "email": "chester.copperpot@astoria.com",
            "extra": {
                "transaction_date": "2020-01-28",
                "transaction_time": "17:47:00"
            },
            "cz_tag": "survey1",
    				"crm_id": "",
            "last_name": "COPPERPOT",
            "first_name": "Chester"
        },
        "place": {
            "id": "12AB34",
            "partner_id": "1234",
            "name": "place name",
            "enabled": true,
            "detail_url": "https://api.goodays.cov2/places/12AB34"
        },
        "delegated_to": {
            "id": "ap4M7B1w82",
            "partner_id": "CustomerService",
            "name": "Customer Service",
            "enabled": true,
            "detail_url": "https://api.goodays.cov2/places/ap4M7B1w82"
        },
        "attached_messages": [],
        "state": "open",
        "thread": "12AB34",
        "actions": {
            "reply": "https://api.goodays.co/api/v2/responses/12AB34/reply",
            "spam": "https://api.goodays.co/api/v2/responses/12AB34/spam",
            "close": "https://api.goodays.coapi/v2/responses/12AB34/close"
        },
        "alert_triggered": false
    }
}
```