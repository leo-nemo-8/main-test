---
title: Solicitation nation
excerpt: ''
deprecated: false
hidden: false
metadata:
  title: ''
  description: ''
  robots: index
next:
  description: ''
  pages:
    - type: link
      title: Solicitation API Reference
      url: /reference/solicitations_list
---
The **Solicitation API** is the perfect tool to get in touch with your customers. By email or SMS, send your surveys on a regular basis or right after an interaction! Who says "real time"?

> 👍 Going further
>
> Consult the [API Reference](/reference/solicitations_list) for more.

> 📘 Feel stucked?
>
> Need help with an error? Head to [Troubleshooting and errors](/docs/errors) for more information.

# Key Concepts

The Solicitation API is based on 2 main usages: send and retrieve solicitations.

You can send a solicitation with just a simple POST request. Once the solicitation sent, you can retrieve it by sending a GET request and monitor its status (sent, opened, ...).

Solicitations can be sent one by one or in bulk. These two technics allow to manage your solicitations at your own rhythm.\
If you are able to perform a request after each payment for example, the single solicitation endpoint is the best fit.\
On the other hand, if you create a program that sends a lot of solicitations at a given time, the bulk option is your best choice.

# Let's try!

## Send a single solicitation

Let's say you want to get your customers' feedback right after they purchased something on your website. On your success page, you simply have to send a POST request to the Solicitation API to get in touch with your end customer!

1. Create the payload.

```json
{
   "sender":"Your name <no-reply@subdomain>|Your name",
   "survey":"{survey-id}",
   "type":"email|sms",
   "place":"{place-id}",
   "lang":"{lang}",
   "recipient":"{end customer email|end customer phone number}",
   "context":{
      "first_name":"{end customer first name}",
      "last_name":"{end customer last name}",
      "phone":"{end customer phone}",
      "email":"{end customer email}",
      "crm_id":"{end customer CRM ID}",
      "custom_parameter_1":"{value}",
      "custom_parameter_2":"{value}",
      "custom_parameter_n":"{value}"
   }
}
```

> 📘 Sender Formatting
>
> If you send an email the format must be "Your name [no-reply@yourdomain.com](mailto:no-reply@yourdomain.com)".\
> For SMS the format must be a label of maximum 11 characters containing only numbers, spaces and/or letters without accents.

> 📘 The lang parameter
>
> `lang` is optional. It sets the language of the solicitation (email or SMS). When it is not provided, the language of the point of sale is used.
>
> When sending several solicitations at once, `lang` is set for each item of `data`.
>
> Accepted values: `ar`, `ca`, `cs`, `da`, `de`, `de-at`, `el`, `en`, `es`, `fi`, `fr`, `hrv`, `hu`, `hy`, `it`, `ja`, `ko`, `nb`, `nl`, `pl`, `pt`, `pt-br`, `ro`, `ru`, `sk`, `sl`, `sq`, `sv`, `tr`, `zh-hans`, `zh-hant`, `ka`, `ind`.

> 📘 Recipient's phone number format
>
> We recommend using the [E.164](https://www.twilio.com/docs/glossary/what-e164) standard.
>
> E.164 numbers are formatted `[+] [country code] [subscriber number including area code]` and can have a maximum of fifteen digits.
>
> An example of a French phone number in the E.164 format is : *+33612345678*
>
> *For your information, a Goodays script normalizes the received phone numbers to the E.164 format. This means that formats such as 0033 or 06 (for French phone numbers) will be transformed in +33xxxxxxxxx.*
>
> :warning: *Be careful though, as normalization is not guaranteed in 100% of cases, especially in border areas. A French number is valid as an Italian or Belgian number, but it's 3 different people behind, impossible to know which one it is without a country code.*

> 🚧 Marketing Pressure
>
> The Solicitation API doesn't support marketing pressure: it sends each request regardless of whether the end customer has already been solicited.\
> It's your responsibility to set up this marketing pressure on your side.

2. Use the endpoint url `https://api.goodays.co/v2/solicitations` with the POST verb.

3. *Et voilà!* Now you can send a GET request to see this new solicitation and keep track of its status' evolutions!

## Send several solicitations at once

With this endpoint, you will be able to send up to 1000 solicitations at a time!

1. Create the payload.

```json
{
   "sender":"Your name <no-reply@subdomain>|Your name",
   "survey":"{survey-id}",
   "type":"email|sms",
   "place":"{place-id}",
   "data":[
      {
         "recipient":"{end customer email|end customer phone number}",
         "lang":"{lang}",
         "context":{
            "first_name":"{end customer first name}",
            "last_name":"{end customer last name}",
            "email":"{end customer email}",
            "phone":"{end customer phone}",
            "crm_id":"{end customer CRM ID}",
            "custom_parameter_1":"{value}",
            "custom_parameter_2":"{value}",
            "custom_parameter_n":"{value}"
         }
      },
      {
         "recipient":"{end customer email|end customer phone number}",
         "lang":"{lang}",
         "context":{
            "first_name":"{end customer first name}",
            "last_name":"{end customer last name}",
            "email":"{end customer email}",
            "phone":"{end customer phone}",
            "crm_id":"{end customer CRM ID}",
            "custom_parameter_1":"{value}",
            "custom_parameter_2":"{value}",
            "custom_parameter_n":"{value}"
         }
      }
   ]
}
```

> 📘 Sender Formatting
>
> If you send an email the format must be "Your name [no-reply@yourdomain.com](mailto:no-reply@yourdomain.com)".\
> For SMS the format must be a label of maximum 11 characters containing only numbers, spaces and/or letters without accents.

> 📘 Recipient's phone number format
>
> We recommend using the [E.164](https://www.twilio.com/docs/glossary/what-e164) standard.
>
> E.164 numbers are formatted `[+] [country code] [subscriber number including area code]` and can have a maximum of fifteen digits.
>
> An example of a French phone number in the E.164 format is : *+33612345678*
>
> *For your information, a Goodays script normalizes the received phone numbers to the E.164 format. This means that formats such as 0033 or 06 (for French phone numbers) will be transformed in +33xxxxxxxxx.*
>
> :warning: *Be careful though, as normalization is not guaranteed in 100% of cases, especially in border areas. A French number is valid as an Italian or Belgian number, but it's 3 different people behind, impossible to know which one it is without a country code.*

2. Use the endpoint url `https://api.goodays.co/v2/solicitations/bulk` with the POST verb.

3. And as usual, you can send a GET request at `https://api.goodays.co/v2/solicitations` to see these new solicitations.

## Retrieve the "place-id"

* Use the Place ID returned by the endpoint [/places](ref:places_list), or directly your external ID.

## Retrieve the "survey-id"

1. Call the endpoint url `https://api.goodays.co/v2/surveys` to obtain the ID corresponding to the right survey.
2. Then the "id" attribute is the answer.

## Check the required (or not) custom parameters in the "context" part

1. Call the endpoint url `https://api.goodays.co/v2/configuration` to get the list of your custom parameters
2. "required" tells you which custom parameter is mandatory or not

# Solicitation statuses

A solicitation can have different status in its lifespan. The `status` field of [/solicitations/{id}](ref:solicitations_read) returns the latest one. Here are the possibilities 

<Table align={["left","left"]}>
  <thead>
    <tr>
      <th>
        Status
      </th>

      <th>
        Meaning
      </th>
    </tr>
  </thead>

  <tbody>
    <tr>
      <td>
        `unknown`
      </td>

      <td>
        No status is available yet for this solicitation.
      </td>
    </tr>

    <tr>
      <td>
        `queued`
      </td>

      <td>
        The solicitation is waiting to be send.
      </td>
    </tr>

    <tr>
      <td>
        `dispatching`
      </td>

      <td>
        The solicitation is being sent.
      </td>
    </tr>

    <tr>
      <td>
        `sent`
      </td>

      <td>
        The solicitation has been sent.
      </td>
    </tr>

    <tr>
      <td>
        `delivered`
      </td>

      <td>
        The email or SMS has reached the inbox of the recipient.
      </td>
    </tr>

    <tr>
      <td>
        `undelivered`
      </td>

      <td>
        The following reasons may explain this status :  

        * Email was rejected by the recipient's server
        * The email address does not exist
        * Emails can be marked as spam by the recipient for various reasons
        * An email was sent to a recipient who is on a suppression list
      </td>
    </tr>

    <tr>
      <td>
        `failed`
      </td>

      <td>
        The email can not been send due to an internal error.
      </td>
    </tr>

    <tr>
      <td>
        `opened`
      </td>

      <td>
        The recipient opened the email.
      </td>
    </tr>

    <tr>
      <td>
        `clicked`
      </td>

      <td>
        The recipient clicked on a link in the email.
      </td>
    </tr>

    <tr>
      <td>
        `reported as spam`
      </td>

      <td>
        The recipient reported the email as "Spam".
      </td>
    </tr>

    <tr>
      <td>
        `unsubscribed`
      </td>

      <td>
        The recipient unsubscribed. It will not be possible to send new emails to this recipient.
      </td>
    </tr>
  </tbody>
</Table>

## Retrieve sending IDs

1. Call the endpoint url `https://api.goodays.co/v2/solicitations/` without GET parameter.
2. In return you get the list of emails sent.
3. Save the "id" parameter of each emails you want a status.

You can filter this list with the following GET parameters:

| GET parameter | Description |
| :------------ | :---------- |
| **type** | Type of solicitation: `email` or `sms`. |
| **recipient** | Email address or phone number of the recipient. |
| **place** | Point of sale: Place ID from [/places](ref:places_list), or your external ID. |
| **partner_id** | Point of sale: your external ID. |

Example: `https://api.goodays.co/v2/solicitations?type=sms`

## Check sending status

1. Call the endpoint url `https://api.goodays.co/v2/solicitations/:solicitation_id` with the GET parameter "solicitation\_id" filled in with the email ID previously retrieved .
2. In return you will get the status of your shipment.

# Ready to start?

For an overview of how our APIs work, check out the [Get started page](doc:getting-started). If you're ready to use the Solicitation API, you can use your API token to make direct requests.
