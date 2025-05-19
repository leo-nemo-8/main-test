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
 - the users
 - the places.

For these two resources, you can add, update and delete informations.
[block:api-header]
{
  "title": "Managing the users"
}
[/block]
These functionalities are incredibly useful when there is a lot of movement among your collaborators. New employees, employees moving from one place to another or employees leaving the company may create a huge load of work to maintain your user base.
The following endpoints help you maintaining this user base in the Critizr scope.

## Create a new user

The endpoint is ```https://api.critizr.com/v2/users``` with the ```POST``` HTTP verb.
The following field are available to create the user : 
  * email
  * first_name
  * last_name
  * activate_notifications
  * places
  * read_only
  * phone

The payload may look like this : 
[block:code]
{
  "codes": [
    {
      "code": "{\n    \"email\": \"arnaud.lancelot@critizr.com\",\n    \"first_name\": \"Arnaud\",\n    \"last_name\": \"Lancelot\",\n    \"phone\": \"0123456789\",\n    \"activate_notifications\": true,\n    \"places\" : [{place-id}, {place-id}, ...],\n    \"read_only\": false\n}",
      "language": "json"
    }
  ]
}
[/block]
## Update a user

The endpoint is ```https://api.critizr.com/v2/users/{user-id}``` with the ```PATCH``` HTTP verb.
The following field are available to update the user : 
   * places
  * is_readonly
[block:callout]
{
  "type": "danger",
  "body": "If you made a mistake in critical fields such as ```email```, ```first_name``` or ```last_name```, the easiest way is to delete the user and create an other one.",
  "title": "Critical fields"
}
[/block]
The payload may look like this : 
[block:code]
{
  "codes": [
    {
      "code": "{\n    \"places\" : [{place-id}, {place-id}, ...],\n    \"is_readonly\": true\n}",
      "language": "json"
    }
  ]
}
[/block]
## Remove a user

The endpoint is ```https://api.critizr.com/v2/users/{user-id}``` with the ```DELETE``` HTTP verb.
[block:api-header]
{
  "title": "Managing the places"
}
[/block]
Places shouldn't experience as much changes as the users. Still, it is useful to be able to create, alter or remove a place from your scope.

## Create a place

The endpoint is ```https://api.critizr.com/v2/places``` with the ```POST``` HTTP verb.
The following field are available to create the place : 
  * name
  * partner_id (as your internal store code)
  * universe
  * lang
  * street
  * postal_code
  * city
  * latitude
  * longitude
  * phone
  * surveys
  * levels
  * users

Some fields require information that you can found with the help of other endpoints : 
  * universes refers to the endpoint [```/universes```](ref:levels-1)
  * surveys refers to the endpoint [```/surveys```](ref:surveys-1) 
  * levels refers to the endpoint [```/levels```](ref:levels-1) 
  * users refers to the endpoint [```/users```](ref:users-1) 

The payload may look like this :
[block:code]
{
  "codes": [
    {
      "code": "{\n    \"name\": \"My Shop\",\n    \"partner_id\": \"123ABC\",\n    \"universe\": \"my_universe\",\n    \"lang\": \"fr\",\n    \"street\": \"221b Baker St\",\n    \"postal_code\": \"NW1 6XE\",\n    \"city\": \"London\",\n    \"latitude\": 51.523659,\n    \"longitude\": -0.158541,\n    \"phone\": \"+442072243688\",\n    \"surveys\": [{survey-id}, {survey-id}, ...],\n    \"levels\": [{level-id}, {level-id}, ...],\n    \"users\": [{user-id}, {user-id}, ...]\n}",
      "language": "json"
    }
  ]
}
[/block]
## Update a place

The endpoint is ```https://api.critizr.com/v2/places/{place-id}``` with the ```PATCH``` HTTP verb.
The following field are available to update the place : 
  * name
  * lang
  * street
  * postal_code
  * city
  * latitude
  * longitude
  * phone
  * surveys
  * levels
  * users
[block:callout]
{
  "type": "danger",
  "title": "Surveys update",
  "body": "It is possible to add new surveys to a place. However, you can not remove an existing survey from a place by using the API."
}
[/block]
The payload may look like this :
[block:code]
{
  "codes": [
    {
      "code": "{\n  \t\"name\": \"My Shop\",\n    \"lang\": \"fr\",\n    \"street\": \"221b Baker St\",\n    \"postal_code\": \"NW1 6XE\",\n    \"city\": \"London\",\n    \"latitude\": 51.523659,\n    \"longitude\": -0.158541,\n    \"phone\": \"+442072243688\",\n    \"surveys\": [{survey-id}, {survey-id}, ...],\n    \"levels\": [{level-id}, {level-id}, ...],\n    \"users\": [{user-id}, {user-id}, ...]\n}",
      "language": "json"
    }
  ]
}
[/block]
## Remove a place

The endpoint is ```https://api.critizr.com/v2/places/{place-id}``` with the ```DELETE``` HTTP verb.
[block:api-header]
{
  "title": "Key takeaways"
}
[/block]
- Managing your users and places in real time is possible by API.
- Some informations require using other endpoints. Feel free to take a look at the [complete API reference](/reference).
[block:callout]
{
  "type": "info",
  "title": "PUT vs PATCH",
  "body": "If you are not familiar with the difference between these two HTTP verbs and their implication, head to [this article](/docs/explore-the-core#section-updating-resources) !"
}
[/block]