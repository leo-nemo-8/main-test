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

Solicitations can be sent one by one or in bulk. These two technics allow to manage your solicitations at your own rhythm.  
If you are able to perform a request after each payment for example, the single solicitation endpoint is the best fit.  
On the other hand, if you create a program that sends a lot of solicitations at a given time, the bulk option is your best choice.

# Let's try!

## Send a single solicitation

Let's say you want to get your customers' feedback right after they purchased something on your website. On your success page, you simply have to send a POST request to the Solicitation API to get in touch with your client!

1. Create the payload.

```json
{
   "sender":"Your name <no-reply@subdomain>|Your name",
   "survey":"{survey-id}",
   "type":"email|sms",
   "place":"{place-id}",
   "lang":"{lang ISO 639-1}",
   "recipient":"{client email|client phone number}",
   "context":{
      "first_name":"{client firstname}",
      "last_name":"{client lastname}",
      "phone":"{client phone}",
      "email":"{client email}",
      "crm_id":"{client crm ID}",
      "additional_information_1":"{valeur}",
      "additional_information_2":"{valeur}",
      "additional_information_n":"{valeur}"
   }
}
```

> 📘 Sender Formatting
> 
> If you send an email the format must be "Your name [no-reply@yourdomain.com](mailto:no-reply@yourdomain.com)".  
> For SMS the format must be a label of maximum 11 characters containing only numbers, spaces and/or letters without accents.

> 📘 Recipient's phone number format
> 
> We recommend using the [E.164](https://www.twilio.com/docs/glossary/what-e164) standard.
> 
> E.164 numbers are formatted `[+] [country code] [subscriber number including area code]` and can have a maximum of fifteen digits.
> 
> An example of a French phone number in the E.164 format is : _+33612345678_
> 
> _For your information, a Goodays script normalizes the received phone numbers to the E.164 format. This means that formats such as 0033 or 06 (for French phone numbers) will be transformed in +33xxxxxxxxx._
> 
> :warning: _Be careful though, as normalization is not guaranteed in 100% of cases, especially in border areas. A French number is valid as an Italian or Belgian number, but it's 3 different people behind, impossible to know which one it is without a country code._

> 🚧 Marketing Pressure
> 
> The Solicitation API doesn't support marketing pressure: it sends each request regardless of whether the end customer has already been solicited.  
> It's your responsibility to set up this marketing pressure on your side.

2. Use the endpoint url `https://api.goodays.co/v2/solicitations` with the POST verb.

3. _Et voilà!_ Now you can send a GET request to see this new solicitation and keep track of its status' evolutions!

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
         "recipient":"{client email|client phone number}",
         "lang":"{lang ISO 639-1}",
         "context":{
            "first_name":"{client name}",
            "last_name":"{client lastname}",
            "email":"{client email}",
            "phone":"{client phone}",
            "crm_id":"{client crm ID}",
            "additional_information_1":"{valeur}",
            "additional_information_2":"{valeur}",
            "additional_information_n":"{valeur}"
         }
      },
      {
         "recipient":"{client email|client phone number}",
         "lang":"{lang ISO 639-1}",
         "context":{
            "first_name":"{client name}",
            "last_name":"{client lastname}",
            "email":"{client email}",
            "phone":"{client phone}",
            "crm_id":"{client crm ID}",
            "additional_information_1":"{valeur}",
            "additional_information_2":"{valeur}",
            "additional_information_n":"{valeur}"
         }
      }
   ]
}
```

> 📘 Sender Formatting
> 
> If you send an email the format must be "Your name [no-reply@yourdomain.com](mailto:no-reply@yourdomain.com)".  
> For SMS the format must be a label of maximum 11 characters containing only numbers, spaces and/or letters without accents.

> 📘 Recipient's phone number format
> 
> We recommend using the [E.164](https://www.twilio.com/docs/glossary/what-e164) standard.
> 
> E.164 numbers are formatted `[+] [country code] [subscriber number including area code]` and can have a maximum of fifteen digits.
> 
> An example of a French phone number in the E.164 format is : _+33612345678_
> 
> _For your information, a Goodays script normalizes the received phone numbers to the E.164 format. This means that formats such as 0033 or 06 (for French phone numbers) will be transformed in +33xxxxxxxxx._
> 
> :warning: _Be careful though, as normalization is not guaranteed in 100% of cases, especially in border areas. A French number is valid as an Italian or Belgian number, but it's 3 different people behind, impossible to know which one it is without a country code._

2. Use the endpoint url `https://api.goodays.co/v2/solicitations/bulk` with the POST verb.

3. And as usual, you can send a GET request at `https://api.goodays.co/v2/solicitations` to see these new solicitations.

## Retrieve the "place-id"

- Enter your establishment code directly here

## Retrieve the "survey-id"

1. Call the endpoint url `https://api.goodays.co/v2/surveys` to obtain the ID corresponding to the right survey.
2. Then the "id" attribute is the answer.

## Check the required (or not) attribute in the "context" part

1. Call the endpoint url `https://api.goodays.co/v2/configuration` to get the attribute list
2. "required" tells you which attribute is mandatory or not

# Solicitation statuses

A solicitation can have different status in its lifespan. Here are the possibilities 

[block:parameters]
{
  "data": {
    "h-0": "Status",
    "h-1": "Meaning",
    "0-0": "Queued",
    "0-1": "The solicitation is waiting to be send.",
    "1-0": "Dispatching",
    "1-1": "The solicitation is being sent.",
    "2-0": "Sent",
    "2-1": "The solicitation has been sent.",
    "3-0": "Delivered",
    "3-1": "The email or SMS has reached the inbox of the recipient.",
    "4-0": "Undelivered",
    "4-1": "The following reasons may explain this status :  \n  \n- Email was rejected by the recipient's server\n- The email address does not exist\n- Emails can be marked as spam by the recipient for various reasons\n- An email was sent to a recipient who is on a suppression list",
    "5-0": "Failed",
    "5-1": "The email can not been send due to an internal error.",
    "6-0": "Opened",
    "6-1": "The recipient opened the email.",
    "7-0": "Clicked",
    "7-1": "The recipient clicked on a link in the email.",
    "8-0": "Reported",
    "8-1": "The recipient reported the email as \"Spam\".",
    "9-0": "Unsubscribed",
    "9-1": "The recipient unsubscribed. It will not be possible to send new emails to this recipient."
  },
  "cols": 2,
  "rows": 10,
  "align": [
    "left",
    "left"
  ]
}
[/block]


## Retrieve sending IDs

1. Call the endpoint url `https://api.goodays.co/v2/solicitations/` without GET parameter.
2. In return you get the list of emails sent.
3. Save the "id" parameter of each emails you want a status.

## Check sending status

1. Call the endpoint url `https://api.goodays.co/v2/solicitations/:solicitation_id` with the GET parameter "solicitation_id" filled in with the email ID previously retrieved .
2. In return you will get the status of your shipment.

# Ready to start?

For an overview of how our APIs work, check out the [Get started page](doc:getting-started). If you're ready to use the Solicitation API, you can use your access token to make direct requests.