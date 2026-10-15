---
title: Pagination, sorting and filtering
excerpt: ''
deprecated: false
hidden: false
metadata:
  title: ''
  description: ''
  robots: noindex
next:
  description: ''
  pages:
    - type: basic
      slug: navigation-through-the-resources
      title: Navigation through the resources
    - type: basic
      slug: explore-the-core-2
      title: Explore the core
    - type: basic
      slug: solicitation-nation
      title: Solicitation nation
    - type: basic
      slug: a-response-at-once
      title: Participation retrieval
---
## Pagination

When you make an API request on an endpoint, you usually don't receive all of the results of that request in a single response. This is because some responses could contain thousands of objects so most responses are paginated by default.

## Number of results

For each "list" endpoint, the Goodays API sends **20 items**.

> 📘 page\_size
>
> The pagination is configurable using the "page\_size" parameter for up to 1000 results.

## Cursor-based Pagination

Cursor-based pagination is the most efficient method of paging and should always be used where possible. A cursor refers to a random string of characters which marks a specific item in a list of data. Unless this item is deleted, the cursor will always point to the same part of the list, but will be invalidated if an item is removed. Therefore, your app shouldn't store cursors and assume that they will be valid in the future.

When reading an endpoint that supports cursor pagination, you will see the following JSON response:

```json
{
    "next": "https://api.goodays.co/v2/{endpoint}?cursor=cD0yMDE4LTEyLTExKzA4JTNBMTAlM0E1My40ODE1NTclMkIwMCUzQTAw",
    "previous": "https://api.goodays.co/v2/{endpoint}?cursor=cD0yMDE4LTEyLTExKzExJTNBMDAlM0ExNy42NjYwNTYlMkIwMCUzQTAwJnI9MQ%3D%3D",
    "results": [
        ... actual data here
    ]
}
```

Each list request will respond with these 3 fields: 

* results
* next
* previous

### Results

The field `results` contains the actual data sent by the endpoint. It is an array of object. The schema of each object is specific of each endpoint and will be available in the [API Reference](/reference).

### Next

This field contains a url that will return the next page of data.\
This field might contain `null`. In this case, this is the last page of data and you can stop paging.

### Previous

This field contains a url that will return the previous page of data.\
This field might contain `null`. In this case, this is the first page of data.

> ❗️ Cursors consistency
>
> Don't store cursors. Cursors can quickly become invalid if items are added or deleted.

## Sorting

By default, search results are sorted by the best match available. You can change this to a specific field using the `sort` parameter.\
You can choose any of the fields' item to sort on. Refer to the [API Reference](/reference) for the resources' schema for each endpoint.

## Example

When you send a request to the [Response API](/reference#responses_list), you obtain a response like described below:

```json
{
    "next": "https://api.goodays.co/v2/responses?cursor=bz0yMA%3D%3D&sort=answers_count",
    "previous": null,
    "results": [
      	{
            "id": "{response-id}",
            "created_date": "2019-03-22T15:02:32.664353+01:00",
            "updated_date": "2019-03-22T15:02:32.664383+01:00",
            "has_answers": true,
            "has_message": false,
            "detail_url": "https://api.goodays.co/v2/responses/{response-id}"
        },
        {
            "id": "{response-id}",
            "created_date": "2019-03-22T15:00:11.357434+01:00",
            "updated_date": "2019-03-22T15:00:11.800730+01:00",
            "has_answers": true,
            "has_message": true,
            "detail_url": "https://api.goodays.co/v2/responses/{response-id}"
        },
        ...
    ]
}
```

Since each field can be used to sort the results, you can use the following fields: 

* id 
* created\_date
* updated\_date
* has\_answers
* has\_message
* detail\_url

If you want to sort the results by `created_date`, you simply have to add `sort=created_date` in the GET parameters of your query.

> 📘 Sort order
>
> You can add a hyphen to inverse the sort order: `sort=-created_date`

## Filtering

When you retrieve a list of resources, it could be pretty useful to only get the results you really want!\
This is where the filters come in handy!\
For every `GET` request that will respond with a list, filters will be available. The details of these filters are available in the [API Reference](/reference).

## Example

When you are retrieving a list of solicitations, you may want to only get the ones related to a particular point of sale. In this case, you can use the `place` filter, with the Place ID or your external ID.\
The request should look like this:

```curl
curl -X GET \
  'https://api.goodays.co/v2/solicitations?place={place-id}' \
  -H 'Authorization: {token}' \
  -H 'Content-Type: application/json' \
```

With this request, you only get the solicitations related to the point of sale you enter as a parameter.
