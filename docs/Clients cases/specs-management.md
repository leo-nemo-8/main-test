---
title: Real time update on users and places
excerpt: ''
deprecated: false
hidden: true
metadata:
  title: ''
  description: ''
  robots: noindex
next:
  description: ''
---
Managing your technical perimeter from the Critizr APIs seems pretty obvious but it is worth explaining how it should be done.

The main purpose of these endpoints is to give you the opportunity to keep your scope identical between your system and Critizr's.

The main resources that need to be maintained are : 

* the users
* the places.

For these two resources, you can add, update and delete informations.

## Managing the users

These functionalities are incredibly useful when there is a lot of movement among your collaborators. New employees, employees moving from one place to another or employees leaving the company may create a huge load of work to maintain your user base.\
The following endpoints help you maintaining this user base in the Critizr scope.

## Create a new user

The endpoint is `https://api.critizr.com/v2/users` with the `POST` HTTP verb.\
The following field are available to create the user : 

* email
* first\_name
* last\_name
* activate\_notifications
* places
* read\_only
* phone

The payload may look like this : 

```json
{
    "email": "arnaud.lancelot@critizr.com",
    "first_name": "Arnaud",
    "last_name": "Lancelot",
    "phone": "0123456789",
    "activate_notifications": true,
    "places" : [{place-id}, {place-id}, ...],
    "read_only": false
}
```

## Update a user

The endpoint is `https://api.critizr.com/v2/users/{user-id}` with the `PATCH` HTTP verb.\
The following field are available to update the user : 

* places
* is\_readonly

> ❗️ Critical fields
>
> If you made a mistake in critical fields such as `email`, `first_name` or `last_name`, the easiest way is to delete the user and create an other one.

The payload may look like this : 

```json
{
    "places" : [{place-id}, {place-id}, ...],
    "is_readonly": true
}
```

## Remove a user

The endpoint is `https://api.critizr.com/v2/users/{user-id}` with the `DELETE` HTTP verb.

## Managing the places

Places shouldn't experience as much changes as the users. Still, it is useful to be able to create, alter or remove a place from your scope.

## Create a place

The endpoint is `https://api.critizr.com/v2/places` with the `POST` HTTP verb.\
The following field are available to create the place : 

* name
* partner\_id (as your internal store code)
* universe
* lang
* street
* postal\_code
* city
* latitude
* longitude
* phone
* surveys
* levels
* users

Some fields require information that you can found with the help of other endpoints : 

* universes refers to the endpoint [`/universes`](ref:levels-1)
* surveys refers to the endpoint [`/surveys`](ref:surveys-1) 
* levels refers to the endpoint [`/levels`](ref:levels-1) 
* users refers to the endpoint [`/users`](ref:users-1) 

The payload may look like this :

```json
{
    "name": "My Shop",
    "partner_id": "123ABC",
    "universe": "my_universe",
    "lang": "fr",
    "street": "221b Baker St",
    "postal_code": "NW1 6XE",
    "city": "London",
    "latitude": 51.523659,
    "longitude": -0.158541,
    "phone": "+442072243688",
    "surveys": [{survey-id}, {survey-id}, ...],
    "levels": [{level-id}, {level-id}, ...],
    "users": [{user-id}, {user-id}, ...]
}
```

## Update a place

The endpoint is `https://api.critizr.com/v2/places/{place-id}` with the `PATCH` HTTP verb.\
The following field are available to update the place : 

* name
* lang
* street
* postal\_code
* city
* latitude
* longitude
* phone
* surveys
* levels
* users

> ❗️ Surveys update
>
> It is possible to add new surveys to a place. However, you can not remove an existing survey from a place by using the API.

The payload may look like this :

```json
{
  	"name": "My Shop",
    "lang": "fr",
    "street": "221b Baker St",
    "postal_code": "NW1 6XE",
    "city": "London",
    "latitude": 51.523659,
    "longitude": -0.158541,
    "phone": "+442072243688",
    "surveys": [{survey-id}, {survey-id}, ...],
    "levels": [{level-id}, {level-id}, ...],
    "users": [{user-id}, {user-id}, ...]
}
```

## Remove a place

The endpoint is `https://api.critizr.com/v2/places/{place-id}` with the `DELETE` HTTP verb.

## Key takeaways

* Managing your users and places in real time is possible by API.
* Some informations require using other endpoints. Feel free to take a look at the [complete API reference](/reference).

> 📘 PUT vs PATCH
>
> If you are not familiar with the difference between these two HTTP verbs and their implication, head to [this article](/docs/explore-the-core#section-updating-resources) !
