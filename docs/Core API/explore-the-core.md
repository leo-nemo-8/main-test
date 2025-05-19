---
title: Explore the core (old => update place/user)
excerpt: ''
deprecated: false
hidden: true
metadata:
  title: ''
  description: ''
  robots: noindex
next:
  description: ''
  pages:
    - type: link
      title: Core API Reference
      url: https://critizr.readme.io/reference#levels
---
Core API is a RESTful API that gives you some control over your levels, places, users and surveys.\
For example, you can :

* Consult your places
* Retrieve responses for a place
* Add users to a place

> 👍 Going further
>
> Consult the [API Reference](/reference) for more.

> 📘 Feel stucked ?
>
> Need help with an error? Head to [Troubleshooting and errors](/docs/errors) for more information.

# Key Concepts

The Core API involves four key concepts: levels, places, users, and surveys.

If you are not familiar with these concept, don't hesitate to consult the [Glossary](/docs/glossary)!

# Functionalities

With the Core API, the following actions are available : 

* Consult, update and delete levels
* Consult, update and delete places
* Add a response, survey or user to a place
* Consult surveys
* Consult and delete users

# Restrictions by conviction

We consciously decided to restrain the capabilities of the API. Some informations and actions may have serious consequences and should remain under the supervision of the Critizr team.

# Updating resources

We built the Critizr's APIs by following the REST recommendations and best practices. This explain why there are two methods to update a resource.

## PUT

When using the `PUT` HTTP verb, the method expects to receive the entire resource containing the modifications. Each field is replaced by the payload's value.

## PATCH

When using the `PATCH`HTTP verb, you can only send the fields you want to update in the payload.

# Example

Imagine that you have to manage dozens of places and hundreds of employees. You probably already have tools and databases to help you add, update and remove says places, users or affect users to places.\
With the Core API, you simply have to get the user and the place you want to connect and proceed!

## Get the user

Here we will use the following GET endpoint : `https://api.critizr.com/v2/users`.\
The response is as follow :

```json
{
    "next": "https://api.critizr.com/v2/users?cursor=cD0xMTAwNTE1",
    "previous": null,
    "results": [
        {
            "id": "ABCD1234",
            "info": {
                "email": "arnaud.lancelot@critizr.com",
                "first_name": "Arnaud",
                "last_name": "Lancelot"
            },
            "places": "https://api.critizr.com/v2/users/ABCD1234/places"
        },
        ...
    ]
}
```

For the user Arnaud Lancelot, his ID is `ABCD1234`.

## Get the place

Next, we have to find the place on which we want to add Arnaud Lancelot.\
We will use the GET endpoint : `https://api.critizr.com/v2/places`.\
The response is as follow :

```json
{
    "next": "https://api.critizr.com/v2/places?cursor=cD0yMDE2LTA1LTE5KzE0JTNBMzMlM0E0Mi42MDkwMDclMkIwMCUzQTAw",
    "previous": null,
    "results": [
        {
            "id": "EFGH5678",
            "partner_id": "1234",
            "name": "Place",
            "enabled": true,
            "detail_url": "https://api.critizr.com/v2/places/EFGH5678"
        },
        ...
    ]
}
```

The place ID is `EFGH5678`.

## Assign the user to the place

With these two informations, we can simply assign the user to the place.\
We perform a `PATCH` request on the endpoint : `https://api.critizr.com/v2/places/{place-id}`. In our case, the `place-id` is `EFGH5678`.\
We will update the users of this place. So we will have to provide the full list of users for this place, including the new user `ABCD1234`.

Since we are using a `PATCH` request, we need to supply a payload like this :

```json
{
	"users": [..., "ABCD1234"]
}
```

A `204` response later, the matching is done !

We can check this association by perfoming a `GET` request on the following endpoint : `https://api.critizr.com/v2/users/ABCD1234/places`.

# Ready to start?

For an overview of how our APIs work, check out the [Get started page](doc:getting-started). If you're ready to use the Core API, you can use your access token to make direct requests.
