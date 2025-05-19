---
title: Troubleshooting and errors
excerpt: >-
  There is nothing more frustrating than having an error and not knowing what it
  means.
deprecated: false
hidden: false
metadata:
  title: ''
  description: ''
  robots: noindex
next:
  description: ''
---
In this section, we will cover the most common errors and how to avoid them. 

## Basic principle

As convention at Goodays, we decide to use the HTTP Codes at their fullest.\
For the most common errors, we send back the most relevant HTTP Code.\
In case of complex errors, we will send an HTTP error code and a payload with a detailed message.

## Authorization

If your request causes an authentication error, the response will contain an error object. The error object includes information to help you resolve the problem.

The information included in the error object varies depending on the error, but all error objects include a code, which is a short, readable key to help you identify the error. Here are the Authentication error codes:

| HTTP Status Code | Message                            | Meaning                                   | Potential Solution                                             |
| :--------------- | :--------------------------------- | :---------------------------------------- | :------------------------------------------------------------- |
| 401              | No API key found in request        | The `Authorization` header doesn't exist. | Please add the `Authorization` header in your request.         |
| 403              | Invalid authentication credentials | The provided access token is invalid.     | Check if the provided token matches the token sent by Goodays. |

## Rate Limits

We implement a rate limit policy for our endpoints. Abuses will trigger these limitations.

| HTTP Status Code | Message                 | Meaning                                            | Potential Solution                                  |
| :--------------- | :---------------------- | :------------------------------------------------- | :-------------------------------------------------- |
| 429              | API rate limit exceeded | The rate limit for this endpoint has been reached. | Wait before trying to request this ressource again. |

## Common errors

| HTTP Status Code | Message               | Meaning                                                                                         |
| :--------------- | :-------------------- | :---------------------------------------------------------------------------------------------- |
| 400              | Bad request           | Make sure you use the correct url syntax.                                                       |
| 403              | Forbidden             | The resource you are trying to read is inaccessible.                                            |
| 404              | Not found             | You are trying to read a resource that doesn't exist. Make sure you use the correct url syntax. |
| 405              | Method Not Allowed    | There should be a mistake between the endpoint and the HTTP verb used.                          |
| 5XX              | Internal Server Error | An error occurred with our API.                                                                 |
