---
title: Explore the core
excerpt: ''
deprecated: false
hidden: false
metadata:
  title: ''
  description: ''
  robots: noindex
next:
  description: ''
---
Core API is a RESTful API that gives you some control over your levels, places, users and surveys.\
For example, you can :

* Consult your places
* Retrieve responses for a place

> 👍 Going further
>
> Consult the [API Reference](/reference) for more.

> 📘 Feel stucked ?
>
> Need help with an error? Head to [Troubleshooting and errors](/docs/errors) for more information.

# Key Concepts

The Core API involves four key concepts: levels, places, users, and surveys.

If you are not familiar with these concept, don't hesitate to consult the [Glossary](/docs/glossary)!

> 📘 Test points of sale
>
> Test points of sale are returned by [/places](ref:places_list), like your other points of sale. The API does not flag them as test points of sale: if you synchronise your points of sale from the API, ask your Goodays contact for the list of your test points of sale so you can exclude them.

# Functionalities

With the Core API, the following actions are available : 

* Consult levels
* Consult places
* [Add a response to a place](doc:become-a-collection-source)
* Consult surveys
* Consult users

# Restrictions by conviction

We consciously decided to restrain the capabilities of the API. Some informations and actions may have serious consequences and should remain under the supervision of the Goodays team.

# Ready to start?

For an overview of how our APIs work, check out the [Get started page](doc:getting-started). If you're ready to use the Core API, you can use your access token to make direct requests.
