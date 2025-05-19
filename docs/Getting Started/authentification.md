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
To use the Goodays APIs, you need to pass your personal access token in the Authorization header of your requests.

## Access Token

Access tokens are long strings of random characters that look something like this: `943af478d3ff3d4d760020c11af102b79c440513`.  
Your access token is unique to you. We use it to identify you and make sure that only you can access your resources.

## Get your token

An access token is unique and belongs to an individual client. If you don't have your access token, you can ask for yours by contacting your account manager.

## Authentication format

Now that you have your access token, you can perform requests.  
Each request to an API have to contain the access token in the Authorization header.  
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
| 403              | Invalid authentication credentials | The provided access token is invalid.     | Check if the provided token matches the token sent by Goodays. |

> ❗️ Privacy
> 
> Anyone with your access token can read, update and delete your resources, so keep your token **safe**! Also, don't commit to source control with your access token in your code — use a placeholder like ACCESS_TOKEN instead.