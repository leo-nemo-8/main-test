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
      title: Response API reference
      url: https://apidocs.goodays.co/reference/responses_list
---
You are using a dedicated Customer Service tool to reply to all or part of your customers' feedback? You use Goodays to collect customer feedback? Then you are on the right page!

The **Converse API** allows you to process Goodays participations, and reply to them, from a dedicated external tool, in JSON format, by setting up webhooks with your third-party integration.

> 👍 Going further
>
> Consult the [Response API](/reference#response) and [API events](/reference#events) for more.

> 📘 Feel stucked?
>
> Need help with an error? Head to [Troubleshooting and errors](/docs/errors) for more information.

# Why use Converse API

* Enable you to manage the participations collected by Goodays outside its back office:

* In the case of partial delegation from the points of sale to the Customer Service Department  
  E.g.: a pro user of a point of sale has the possibility of delegating a participation for processing by Customer Service.

* In the case of total delegation to remote Customer Service  
  E.g.: Customer Service operates from a Salesforce-type tool.

# Key Concepts

The Converse API allows you to manage the participations collected by Goodays outside its back office.

We can send, through webhook, the participation to your third-party tool and retrieve the replies from your Customer Service to send them directly to your end customers.

# For what purposes?

## Partial delegation to Remote Customer Service

In this solution, the remote Customer Service replies from its third-party tool only to the participations that are within its perimeter. The other participations are processed by the pro users of the points of sale.

<Image align="center" alt="Partial delegation to Remote Customer Service" border={false} caption="Partial delegation to Remote Customer Service" src="https://files.readme.io/723ca20-image.png" />

## Total delegation to Remote Customer Service

In this solution, the remote Customer Service replies from its third-party tool to all the participations collected by Goodays.

<Image align="center" alt="Total delegation to Remote Customer Service" border={false} caption="Total delegation to Remote Customer Service" src="https://files.readme.io/3ed9350-image.png" />

# How to - Basics

## Receive events from Goodays

With each new end customer participation or new message to the Customer Service, the Goodays webhook calls the specific endpoint provided by you.

<Image border={false} src="https://files.readme.io/2dbda95-image.png" />

You have to set up, by your side, one endpoint to managed all these events triggered by the different hooks:

* A "response" handler to deal with a new participation of an end customer.

<Callout icon="📘" theme="info">
  It is the first exchange with the end customer, it contains the verbatim of the end customer, the answers to the questions as well as the personal data and the custom parameters collected.
</Callout>

* A "message" handler to manage a possible private message from the end customer after the Customer Service reply.

<Callout icon="📘" theme="info">
  Once Customer Service has replied to the end customer's participation, the end customer can continue the exchange through a "private message" visible only to the end customer and the Customer Service.
</Callout>

* A "delegate" handler, only needed for the partial delegation mode, to deal with the delegation of a participation from a point of sale to the Customer Service.

<Callout icon="📘" theme="info">
  If a pro user considers that they cannot reply to a participation, they can delegate it to Customer Service.
</Callout>

The Converse API will send event to your endpoint every time these actions are triggered.

## Send actions from the Customer Service to the end customer

<Image border={false} src="https://files.readme.io/2137d4d-image.png" />

The actions that Customer Service can perform on a participation are:

* Reply to the end customer participation:

The main functionality: Customer Service simply replies to the end customer by text.

* Mark the participation as handled by a phone call (with the optional addition of a private note):

If your Customer Service processes a participation directly by phone, this will close the thread on the Goodays side. It is also possible to add a "private note" to summarize the phone exchange between Customer Service and the end customer.

* Mark the participation as closed without reply:

If your Customer Service considers that a participation does not require a reply or telephone processing, it is possible to close the thread directly on the Goodays side.

* Mark the participation as spam:

If your Customer Service considers that a participation is a spam, they can report it to Goodays.

* Reply to a private message from the end customer

If the end customer has replied to your first reply, Customer Service can reply in turn.

# How to - Expert

## Receive events from Goodays

As said before you have to set up the endpoint allowing Goodays to send you the participations and private messages of your end customers.

Once your endpoint is up and running, you must provide us its URL so we can set up the webhook.

> 🚧 Data transcoding
>
> No data transcoding is done on the webhook side by Goodays. Any next transformation job you might have to do after is taken for granted.

> 📘 Samples
>
> You can obtain samples corresponding to your configuration by calling the "[events](ref:events)" endpoint.

### Securing your webhook

Or how to make sure that you only receive data from Goodays?

To allow you to make sure that requests come from Goodays, we recommend that you verify the signature sent in the header of your endpoint.

By default, Goodays is compatible with the HMAC standard and the SHA256 hash algorithm.

If a secret key is configured, we will systematically include the following header in each webhook request:

```
X-HMAC-SHA256
```

This header contains a signature generated from:

* the `secret key` agreed beforehand with your Goodays project contact;
* the raw `body` of the API call.

The signature is calculated as:

```
hex(HMAC-SHA256(secret_key, raw_request_body))
```

You must then calculate the same signature on your side and compare it with the value received in the `X-HMAC-SHA256` header.

If no `secret key` is defined, we do not add this header.

> 🚧
>
> ### Important
>
> The signature must be calculated from the raw HTTP request body, exactly as received by your endpoint, before any JSON parsing.
>
> Do not calculate the signature from:
>
> * a parsed JSON object;
> * a re-serialized JSON payload;
> * a pretty-printed JSON payload;
> * a payload with sorted keys;
> * a payload where spaces or line breaks have changed;
> * a payload where Unicode escapes have been transformed.
>
> Even a small change in the body changes the signature.

Python example:

```
import hmac
import hashlib

def verify_goodays_signature(secret_key, raw_request_body, received_signature):
    expected_signature = hmac.new(
        secret_key.encode("utf-8"),
        raw_request_body,
        hashlib.sha256,
    ).hexdigest()

    return hmac.compare_digest(expected_signature, received_signature)
```

Example usage:

```
raw_request_body = request.body
received_signature = request.headers.get("X-HMAC-SHA256")

is_valid = verify_goodays_signature(
    secret_key,
    raw_request_body,
    received_signature,
)
```

Node.js / Express example:

```
const crypto = require("crypto");
const express = require("express");

const app = express();

app.use(express.json({
  verify: (req, res, buf) => {
    req.rawBody = buf;
  }
}));

app.post("/goodays/webhook", (req, res) => {
  const secretKey = process.env.GOODAYS_WEBHOOK_SECRET;
  const receivedSignature = req.header("X-HMAC-SHA256");

  const expectedSignature = crypto
    .createHmac("sha256", secretKey)
    .update(req.rawBody)
    .digest("hex");

  if (!receivedSignature || expectedSignature !== receivedSignature) {
    return res.status(401).send("Invalid signature");
  }

  return res.status(200).send("OK");
});
```

Salesforce Apex example:

```
Blob mac = Crypto.generateMac(
    'HmacSHA256',
    RestContext.request.requestBody,
    Blob.valueOf(secretKey)
);

String expectedSignature = EncodingUtil.convertToHex(mac).toLowerCase();
String receivedSignature = RestContext.request.headers.get('X-HMAC-SHA256');

Boolean isValid = expectedSignature.equalsIgnoreCase(receivedSignature);
```

In Apex, use `RestContext.request.requestBody` directly. Do not deserialize the JSON before calculating the signature.

Example:

* The *secret key* is `Goodays`
* The body is:

JSON

```
{
    "event_type": "response"
}
```

Then we will add in the header of each call:

Header

```
X-HMAC-SHA256 = bcf95bdaa6dae4e97a44eb8d65273d3c5459f9a258b68c26f10d6cc69b359b51
```

> 📘
>
> The content of the parameter `X-HMAC-SHA256` will therefore change with each request.

### Receive a "response" from an end customer

This event is triggered when an end customer sends a [participation](ref:events_sample_response).

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
                "sms": false,
                "custom": false
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
| survey         | The survey answered by the end customer                                                  |
| answers        | The end customer's answers to the survey                                                        |
| message        | The end customer's verbatim                                                                     |
| attachment     | Contains a web link to the resource shared by the end customer: image or document               |
| user           | Information on the end customer                                                                 |
| context        | Custom parameters provided by our common client to describe the context of the participation    |
| place          | Point of sale information                                                                       |
| state          | Thread status: open, closed or spam                                                             |
| actions        | The only possible actions on the participation: reply, spam, close and call                     |

### Receive a "message" from an end customer

This event is triggered when an end customer sends a [private message](ref:events_sample_message) in a conversation with you. This event can only occur after this end customer sent a participation and you replied to it.

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
                "sms": false,
                "custom": false
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
| reply             | Contains the Customer Service reply to the participation of the end customer               |
| attached_messages | The list of past exchanges in the thread between the end customer and the Customer Service |
| message           | The private message of the end customer to Customer Service                                |

### Receive a "delegation" from a pro user

This event is triggered when a pro user of a point of sale faces a question they don't know how to reply to. They can "ask for help" and [delegate the participation](ref:events_sample_delegated) to the Customer Service.

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
                "sms": false,
                "custom": false
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
| delegated_to   | Contains the information of the point of sale to which the participation is delegated. Here: Customer Service |

## Send actions from the Customer Service to the end customer

Two Goodays endpoints allow you to process an end customer's participation or private message:

<Image align="center" alt="Main use case: processing of end customer's participation" border={false} caption="Main use case: processing of end customer's participation" src="https://files.readme.io/5a3361e-image.png" />

<Image align="center" alt="Secondary use case: processing of end customer's private message" border={false} caption="Secondary use case: processing of end customer's private message" src="https://files.readme.io/3d5a486-image.png" />

> ❗️ The Goodays back office management rules apply.
>
> The possible actions for each participation or message are listed in the "actions" attribute. Please use them.
>
> E.g.:
>
> * you cannot send a message without having processed the initial participation previously
> * you cannot put in spam if a participation is already processed.

> 🚧 Process each participation or message
>
> To allow a good management of the statistics it is very important to process each participation of an end customer (even with a "closed without reply").

The different possibilities are:

### Reply to the end customer participation

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
> The "user" attribute is the ID of the pro user who performs the action. You can obtain it with the Users API: `/users?email={pro user email}`.  
> It is optional: when it is missing, the action is attributed to the pro user of your API token.

> 📘 "remark_type" attribute
>
> The "remark_type" is mandatory when the participation is an external review that has not been typed yet.  
> E.g.: a Google review.
>
> The possible values are:
>
> * Praise
> * Question
> * Idea
> * Problem
>
> If you can't implement Google reviews typing then you should always push `Message` value.  
> i.e. `"remark_type": "Message"`

### Reply to the end customer private message

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

### Mark the participation as handled by a phone call (with optional addition of a rating and a private note)

With [`/responses/{response-id}/call`](ref:responses_call):

```json Sample reply by call
{
  "user": "1a2b3c4",
  "rating": 5,
  "note": "The conversation with the End Customer was good, it's a misunderstanding."
}
```

> 📘 "note" and "rating" attributes
>
> The "note" and "rating" attributes are optional:
>
> * The "note" attribute is a free text: a private note about the call with the end customer (e.g. more context about the dissatisfaction of the end customer).
> * The "rating" attribute is an integer from 1 to 5: it lets Customer Service rate the call with the end customer.

### Mark the participation as closed without reply

With [`/responses/{response-id}/close`](ref:responses_close):

```json Sample reply without reply
{
  "user": "1a2b3c4",
  "remark_type": "Problem"
}
```

### Mark the participation as spam

With [`/responses/{response-id}/spam`](ref:responses_spam):

```json Sample reply as spam
{
  "user": "1a2b3c4"
}
```

# Use cases

## Customer Service handles the participation of an end customer

Let's imagine that an operator in your Customer Service has received a participation from an end customer via the Goodays webhook. We are in the "public message" section: the verbatim of the end customer and the operator's reply could possibly be published on the site of our common client.

### Receive the participation

As a preliminary, we have sent the end customer's participation to your endpoint "response":

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
                "sms": false,
                "custom": false
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

### Process the participation

> 🚧 You need to process each participation sent
>
> It is important to provide Goodays with a processing status for each participation provided.  
> The reply rate and processing time are part of the KPIs monitored by our common client.

Here are, in concrete terms, the possible actions on your side:

* Your operator can directly call the end customer, after that action you must notify Goodays to mark the participation as completed:

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

* **OR** your operator can reply with a text message:

```curl Reply
curl --location --request PUT 'https://api.goodays.co/v2/responses/646RjJ5Z49/reply' \
--header 'Content-Type: application/json' \
--header 'Authorization: 1234abcd1234abcd1234abcd1234abcd' \
--data-raw '{
  "user": "1a2b3c4",
  "content": "Dear Customer, thank you for your feedback. We are sorry for the inconvenience. What information you were looking for? Regards,"
}'
```

* **OR**, if your operator judges that the participation does not require a reply, they can close it without any exchange with the end customer:

```curl Close without reply
curl --location --request PUT 'https://api.goodays.co/v2/responses/vdOpL1NJ74l/close' \
--header 'Content-Type: application/json' \
--header 'Authorization: 1234abcd1234abcd1234abcd1234abcd' \
--data-raw '{
  "user": "1a2b3c4"
}'
```

* **OR**, if your operator deems that the participation is spam, please report it to us:

```curl Spam
curl --location --request PUT 'https://api.goodays.co/v2/responses/vdOpL1NJ74l/spam' \
--header 'Content-Type: application/json' \
--header 'Authorization: 1234abcd1234abcd1234abcd1234abcd' \
--data-raw '{
  "user": "1a2b3c4"
}'
```

## The end customer replies to Customer Service

Let's imagine that, following the operator's reply, the end customer replies in turn: we then enter the "private message" section. The rest of the exchange will remain between you and the end customer

### Receive the message from the end customer

As a preliminary, we have sent the end customer's message to your endpoint "message":

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
                "sms": false,
                "custom": false
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
> It is important to provide Goodays with a processing status for each message provided.  
> Even if no reply is needed.

Here are, in concrete terms, the possible actions on your side:

* Your operator can reply with a text message:

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

The end customer and Customer Service can continue to exchange in "private message" mode until a new participation from the end customer arrives.

> 📘 Loop message and new participation
>
> If a new participation from the end customer arrives we get out of the loop message.

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
                "sms": false,
                "custom": false
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

## The pro user delegates the participation of an end customer to the Customer Service

It is possible that a participation from an end customer cannot be processed by the pro users of the point of sale, in which case it is possible to delegate the participation (and possible private messages) to Customer Service.  
In this case the participation is moved from its point of sale directly to the Customer Service. The pro users of the point of sale no longer have access to this participation.

> 📘 Possible actions after a pro user delegation
>
> Once the delegation has been made by the pro user, the actions are the same as in the chapter "[Customer Service handles the participation of an end customer](#customer-service-handles-the-participation-of-an-end-customer)".

Then, we send the participation to your endpoint "response" with the "event_type" on "delegated":

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
                "sms": false,
                "custom": false
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