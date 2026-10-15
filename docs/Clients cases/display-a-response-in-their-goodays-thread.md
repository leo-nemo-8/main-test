---
title: Display a participation in the Goodays back office
excerpt: ''
deprecated: false
hidden: false
metadata:
  title: ''
  description: ''
  robots: index
next:
  description: ''
---
You retrieve participations with our [Response API](doc:a-response-at-once) and would like to link each of them to its thread in the Goodays back office?

For example:

* you display your end customers' participations in their CRM records,
* you have an internal dashboard that lists participations with certain filters.

**It can be done!**

## Retrieve the participation ID

The unique ID of each participation is the `id` attribute of each participation you retrieve through the API:

```json
{
    "id": "gxKrrlok4o",
    [...]
    "message": {
        "id": "TTT",
        "created_date": "2021-11-22T15:42:48.691040+01:00",
        "type": "Praise",
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

Once the participation `id` has been retrieved, simply call the `https://app.goodays.co/pro/open` url with the `response_id` parameter.

For example with the `id` "gxKrrlok4o":

```Text URL
https://app.goodays.co/pro/open?response_id=gxKrrlok4o
```

> 👍 Successfully display a participation
>
> For the participation to be displayed in the Goodays back office, three rules must be met:
>
> * the person who opens the link must be a pro user with access to the point of sale of the participation,
> * the `id` must correspond to an existing participation,
> * the participation must contain a verbatim OR have triggered a dissatisfaction alert.

> ❗️ In case of error
>
> If the message "The conversation can't be found on our servers." is displayed, check that the participation meets one of the following conditions:
>
> * its verbatim `message.content` is not `null`,
> * its `alert_triggered` attribute is `true`.
>
> And check that the pro user connected to the Goodays back office has access to the point of sale of this participation.
