---
title: Inbox
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
> 📘 What's that?
>
> The Inbox is where a Goodays user receives all the feedback from end customers to process.
>
> The elements to be processed are distinguished into two attributes:
>
> * dissatisfaction alerts
> * messages

<Image border={false} src="https://files.readme.io/9bfb75a-Product_Messagerie_1.png" title="Product Messagerie (1).png" />

# How do I get my inbox metrics?

With [/dashboard](ref:dashboard):

```curl
curl --location --request GET 'https://api.goodays.co/v2/dashboard' \
--header 'Authorization: 1234abcd1234abcd1234abcd1234abcd'
```

```json
{
    "pending_alert": 1,
    "pending_reply": 2
}
```

The return will always contain:

| Attribute         | Description                              |
| :---------------- | :--------------------------------------- |
| **pending_alert** | Number of dissatisfaction alerts pending |
| **pending_reply** | Number of verbatims awaiting processing  |

> 📘 Total items awaiting processing?
>
> To get the total number of items waiting to be processed, the two attributes `alert` and `awaiting_reply` must be added together.

# Add some filters

It is possible to add GET parameters to refine the calculation of the score over a Goodays user perimeter or an establishment.

## GET parameters

To retrieve the number of items waiting to be processed it is possible to combine the following GET parameters:

<Table align={["left","left"]}>
  <thead>
    <tr>
      <th>
        GET parameters
      </th>

      <th>
        Description
      </th>
    </tr>
  </thead>

  <tbody>
    <tr>
      <td>
        **level**
      </td>

      <td>
        Filter on a level.  
        _It is necessary to indicate the ID of the establishment from the endpoint[/levels](ref:levels_list)._
      </td>
    </tr>

    <tr>
      <td>
        **pro_user**
      </td>

      <td>
        Filter on the perimeter of a Goodays user.  
        _Format : email url encoded_  
        Ex: [_yul.brenner@coolrunnings.com_](mailto:_yul.brenner@coolrunnings.com_) will become _yul.brenner%40coolrunnings.com_
      </td>
    </tr>
  </tbody>
</Table>

# Use cases

Here are some examples to show you the possibilities of this endpoint.

## For one Goodays user

I have to use the following parameters :

* pro_user

```curl Inbox call
curl --location --request GET 'https://api.goodays.co/v2/dashboard? \
	pro_user=yul.brenner%40coolrunnings.com' \
--header 'Authorization: 1234abcd1234abcd1234abcd1234abcd'
```

```json Inbox
{
    "pending_alert": 0,
    "pending_reply": 3
}
```

<br />
