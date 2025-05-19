---
title: Semantic Classification
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
# **Purpose**

> 📘 The Semantic Classification API allows point of sales to retrieve end customer participations classifications based on predefined categories and sentiment analysis. It supports retrieving classification schemes and categorised feedback.

# **Dependency Notice**

This API depends on the **Responses API**. Before querying the **Semantic Classification API**, you must first retrieve responses IDs using the **Responses API**. More details can be found [here](/docs/a-response-at-once).

# **Scheme API**

## **Description**

**GET /customers/{customer}/api/semantic/scheme**

Retrieves your semantic classification scheme.

## **Request Example**

```sh Curl
curl --location 'https://app.goodays.co/customers/{customer}/api/semantic/scheme' \
--header 'Authorization: Token <YOUR_TOKEN>' \
--header 'Content-Type: application/json'
```

### **Response Example**

```json
{
    "data": {
        "id": "a1b2c3d4-e5f6-1a2b-3c4d-5e6f7a8b9c0d",
        "name": "Restaurant By Goodays",
        "categories": [
            {
                "id": "a1b2c3d4e5",
                "name": "Confort et ambiance",
                "subcategories": [
                    {
                        "id": "m1n2p3q4r5",
                        "name": "Ambiance générale",
                        "parent": "a1b2c3d4e5"
                    },
                    {
                        "id": "m1n2p3q4r5",
                        "name": "Confort du mobilier",
                        "parent": "a1b2c3d4e5"
                    }
                ]
            }
        ]
    }
}
```

***

# **Classification API**

## **Description**

**GET /customers/{customer}/semantic/classification**

Retrieves categorized end customer feedback and associated sentiment analysis.

### **Query Parameters**

[block:parameters]
{
  "data": {
    "h-0": "**Parameter**",
    "h-1": "**Description**",
    "0-0": "`items_per_page`",
    "0-1": "(Optional) Pagination, 20 by default up to 100 results.",
    "1-0": "`scheme`",
    "1-1": "(Optional) Scheme ID. Defaults to the active scheme.",
    "2-0": "`start_date`",
    "2-1": "(Required if no `responses` or `month`)  \nStart of calculation period.  Format: `YYYY-MM-DDThh:mm:ss`",
    "3-0": "`end_date`",
    "3-1": "(Required if no `responses` or `month`)  \nEnd of calculation period. Format: `YYYY-MM-DDThh:mm:ss`",
    "4-0": "`month`",
    "4-1": "(Optional) Filter by month. Format: `YYYY-MM`",
    "5-0": "`place`",
    "5-1": "(Optional) Filter by point of sales ID.",
    "6-0": "`places`",
    "6-1": "(Optional) List of point of sales IDs (comma-separated).",
    "7-0": "`level`",
    "7-1": "(Optional) Filter by level ID.",
    "8-0": "`levels`",
    "8-1": "(Optional) List of level IDs (comma-separated).",
    "9-0": "`categories`",
    "9-1": "(Optional) Filter by category IDs (comma-separated).",
    "10-0": "`responses`",
    "10-1": "(Optional) Filter by response IDs (comma-separated)."
  },
  "cols": 2,
  "rows": 11,
  "align": [
    null,
    null
  ]
}
[/block]


## **Request Example**

```sh Curl
curl --location 'https://app.goodays.co/customers/{customer}/api/semantic/classifications? \
   start_date=2025-01-01& \
   end_date=2025-01-02' \
--header 'Authorization: Token <YOUR_TOKEN>'
```

## **Response Example**

```json
{
    "count": 313,
    "next": "https://app.goodays.co/{customer}/api/semantic/classifications?start_date=2025-01-01&end_date=2025-01-02&page=2",
    "previous": null,
    "results": [
        {
            "response": "k1l2m3n4o5",
            "category": {
                "id": "m1n2p3q4r5",
                "name": "Ambiance générale",
                "parent": "a1b2c3d4e5"
            },
            "sentiment": "positive"
        },
        {
            "response": "k1l2m3n4o5",
            "category": {
                "id": "m1n2p3q4r5",
                "name": "Confort du mobilier",
                "parent": "a1b2c3d4e5"
            },
            "sentiment": "negative"
        },
        {
            "response": "r1s2t3u4v5",
            "category": {
                "id": "m1n2p3q4r5",
                "name": "Confort du mobilier",
                "parent": "a1b2c3d4e5"
            },
            "sentiment": "positive"
        }
    ]
}
```

# **Error Handling**

If no query parameters (`start_date`, `end_date`, `responses`, or `month`) are provided, the API returns:

```json
[
    "Either 'responses', 'month', or 'start_date' and 'end_date' must be provided."
]
```

***

# **Example Use Case**

## **Scenario**

You want to extract feedback data related to a specific category `m1n2p3q4r5` for a given point of sales `t1u2v3w4x5` within the period from January 1, 2025, to January 2, 2025, for integration into your datalake.

## **Steps**

1. The client calls the following API request:
   ```sh
   curl --location 'https://app.goodays.co/customers/{customer}/api/semantic/classifications?\
      start_date=2025-01-01& \
      end_date=2025-01-02& \
      place=t1u2v3w4x5& \
      categories=m1n2p3q4r5' \
   --header 'Authorization: Token <YOUR_TOKEN>'
   ```
2. The API returns only feedback related to the category **"Ambiance générale"** at the specified point of sales for the requested date range.
3. You integrate the returned data into your datalake.

## **Response Example**

```json
{
    "count": 4,
    "next": null,
    "previous": null,
    "results": [
        {
            "response": "k1l2m3n4o5",
            "category": {
                "id": "m1n2p3q4r5",
                "name": "Ambiance générale",
                "parent": "a1b2c3d4e5"
            },
            "sentiment": "negative"
        },
        {
            "response": "r1s2t3u4v5",
            "category": {
                "id": "m1n2p3q4r5",
                "name": "Ambiance générale",
                "parent": "a1b2c3d4e5"
            },
            "sentiment": "positive"
        },
        {
            "response": "d1e2f3g4h5",
            "category": {
                "id": "m1n2p3q4r5",
                "name": "Ambiance générale",
                "parent": "a1b2c3d4e5"
            },
            "sentiment": "positive"
        },
        {
            "response": "d1e2f3u4v5",
            "category": {
                "id": "m1n2p3q4r5",
                "name": "Ambiance générale",
                "parent": "a1b2c3d4e5"
            },
            "sentiment": "positive"
        }
    ]
} 
```