---
title: Keeping up with API changes
excerpt: How the Goodays API evolves and how to follow its changes
deprecated: false
hidden: false
metadata:
  title: ''
  description: ''
  robots: index
next:
  description: ''
---
The Goodays API evolves regularly to bring you new data and new features. This page explains how these changes are made and how your technical teams can follow them.

# How the API evolves

The Goodays API evolves **on the same version**, by adding new elements:

* new attributes in the existing responses (for example a new date or a new indicator);
* new optional parameters or filters;
* new endpoints or new webhook events.

These additions enrich the data you receive without changing the way you call the API or the business rules behind it. They are designed to be **transparent for your existing integrations**: no action is required on your side, and the documentation is updated at the same time.

> 📘 Best practice: ignore unknown attributes
>
> As for any REST/JSON integration, your client should ignore the attributes it does not know, instead of failing on them. Make sure your JSON deserialisation and any schema validation you use do not expect a closed list of fields.

If an evolution could not be made in such a backward-compatible way, a new version of the API would be offered, so that the integrations of our active clients keep working.

# The changelog

Every evolution of the API is listed in the [Announcements](https://apidocs.goodays.co/changelog) section of this documentation, with its date, its type (added, improved, fixed...) and a link to the related documentation.

As additions do not require any action, we do not send a specific notification for each of them. The changelog is the place to keep track of them at your own pace.

# Get notified automatically with RSS

The changelog is also available as an RSS feed:

```
https://apidocs.goodays.co/changelog.rss
```

You can subscribe to this feed with any tool that reads RSS, so that your teams are notified as soon as a new entry is published. For example:

* an RSS reader;
* your team chat tool (most of them can post the new entries of an RSS feed in a channel);
* an RSS-to-email service, to receive each new entry by email.

> 👍 Any question?
>
> If an evolution raises a question for your integration, contact your Goodays technical contact.
