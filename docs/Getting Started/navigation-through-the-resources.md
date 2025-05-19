---
title: Navigation through the resources
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
For some endpoints, the Goodays API responds with links in the payload.  
It is the implementation of [HATEOAS principle](https://fr.wikipedia.org/wiki/HATEOAS).

## What is HATEOAS ?

HATEOAS stands for **H**ypermedia **a**s **t**he **E**ngine **o**f **A**pplication **S**tate.  
The basics of this principle is to allow a server to navigate through resources without having to be aware of the whole API schema.  
As a user browsing on a web page clicking from links to links, servers may discover resources by following the hypermedia links sent in the payload.

## Example

For this example, we will get a list of responses and use the hypermedia links to retrieve a single response.

## Get a list of responses

```curl
curl -X GET \
  'https://api.goodays.co/v2/responses' \
  -H 'Authorization: {access-token}' \
  -H 'Content-Type: application/json'
```

This request gets the following response :

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
            "has_message": false,
            "detail_url": "https://api.goodays.co/v2/responses/{response-id}"
        },
        ...
    ]
}
```

At this point, you should notice the `detail_url` field. It contains a url to retrieve the details of a specific response.  
Let's try this url!

## Get a specific response

```curl
curl -X GET \
'https://api.goodays.co/v2/responses/{response-id}' \
  -H 'Authorization: {access-token}' \
  -H 'Content-Type: application/json'
```

We get the full object of this specific response :

```json
{
    "id": "{response-id}",
    "created_date": "2018-12-12T09:03:13.441327+01:00",
    "updated_date": "2018-12-12T09:04:13.305446+01:00",
    "source": "CU",
    "survey": {
        "id": "{survey-id}",
        "slug": "post-visit",
        "label": "Sollicité",
        "enabled": true,
        "detail_url": "https://api.goodays.co/v2/surveys/{survey-id}"
    },
    "answers": [
        ... answers objects
    ],
    "message": {
        ... message details
    },
    "reply_type": "text",
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
        "id": "{place-id}",
        "partner_id": "{partner-id}",
        "name": "{place-name}",
        "enabled": true,
        "detail_url": "https://api.goodays.co/v2/places/{place-id}"
    },
    "state": "closed",
    "thread": "{thread-id}"
}
```

> 📘 Did you notice ?
> 
> In the response of the specific Response request, the fields `survey` and `place` also contain a `detail_url` field.  
> We could continue navigating to other resources !