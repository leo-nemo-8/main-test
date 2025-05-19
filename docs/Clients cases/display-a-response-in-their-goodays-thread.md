---
title: Display a response in their Goodays thread
excerpt: ''
deprecated: false
hidden: true
metadata:
  title: ''
  description: ''
  robots: index
next:
  description: ''
---
You retrieve responses from our [Response API ](a-response-at-once)and would like to be able to make a direct link between them and the Goodays Back Office?

For example:

- you can display your End Customers' responses in their CRM records,
- you have an internal dashboard that displays entries using certain filters.

**It can be done!**

## Retrieve the response ID

The unique ID of each response is the `id` attribute present for each response you have retrieved through our API:

```json
{
    "id": "gxKrrlok4o",
    [...]
    "message": {
        "id": "TTT",
        "created_date": "2021-11-22T15:42:48.691040+01:00",
        "type": "Problem",
        "content": "I like this shop!",
        "attachment": null,
        "sender": {
            "email": "sanka@coffie.jm",
            "first_name": "Sanka",
            "last_name": "Coffie"
        }
    },
    [...]
    "alert_triggered": false
}
```

## Build the URL to call

Once the response `id` has been retrieved, simply call the `https://app.goodays.co/pro/open` url with the `response_id` parameter.

For example with the `id` "gxKrrlok4o":

```Text URL
https://app.goodays.co/pro/open?response_id=gxKrrlok4
```

> 👍 Successfully display a response
> 
> For the response to be displayed successfully in the Goodays Back Office, it must satisfy three rules:
> 
> - the user must have a Goodays account AND the rights to display the response,
> - the `id` must correspond to an existing response,
> - the response must contain a verbatim OR have triggered a Dissatisfaction Alert.

> ❗️ In case of error
> 
> If the message "The conversation can't be found on our servers." verifies that the response meets one of the following conditions:
> 
> - the response has a verbatim `message.content` other than `null`
> - the response's `alert_triggered` attribute value is `true`
> 
> And, of course, the user connected to the Goodays Back Office has the right perimeter to access this response.