---
title: Authentication
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
      slug: sorting-and-pagination
      title: Pagination and sorting
---
To use the Goodays APIs, you need to pass your API token in the Authorization header of your requests.

## API token

API tokens are long strings of random characters that look something like this: `943af478d3ff3d4d760020c11af102b79c440513`.\
Your API token is unique to you. We use it to identify you and make sure that only you can access your resources.

> 📘 Access scope
>
> Your API token is attached to a pro user. The API only returns the data of the points of sale this user has access to.
>
> If this user has no active point of sale, list endpoints (`responses`, `places`, `surveys`, `solicitations`, `dashboard`...) return an empty result. Metrics (`stats`) endpoints are not affected.

## Get your token

An API token is unique and belongs to one pro user of your organization. If you don't have your API token, you can ask for yours by contacting your Goodays project contact.

## Authentication format

Now that you have your API token, you can perform requests.\
Each request to an API have to contain the API token in the Authorization header.\
A typical request should look like this:

```curl
curl -X GET \
  https://api.goodays.co/v2/places \
  -H 'Authorization: {access-token}' \
  -H 'Content-Type: application/json'
```

## Errors

If your request causes an authentication error, the response will contain an error object. The error object includes information to help you resolve the problem.

The information included in the error object varies depending on the error, but all error objects include a code, which is a short, readable key to help you identify the error. Here are the Authentication error codes:

| HTTP Status Code | Message                            | Meaning                                   | Potential Solution                                             |
| :--------------- | :--------------------------------- | :---------------------------------------- | :------------------------------------------------------------- |
| 401              | No API key found in request        | The `Authorization` header doesn't exist. | Please add the `Authorization` header in your request.         |
| 403              | Invalid authentication credentials | The provided API token is invalid.     | Check if the provided token matches the token sent by Goodays. |

> ❗️ Privacy
>
> Anyone with your API token can read, update and delete your resources, so keep your token **safe**! Also, don't commit to source control with your API token in your code: use a placeholder like ACCESS\_TOKEN instead.
