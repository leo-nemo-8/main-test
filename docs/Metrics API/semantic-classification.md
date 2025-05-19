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

**GET /customers/\{customer}/api/semantic/scheme**

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

**GET /customers/\{customer}/semantic/classification**

Retrieves categorized end customer feedback and associated sentiment analysis.

### **Query Parameters**

<Table>
  <thead>
    <tr>
      <th>
        **Parameter**
      </th>

      <th>
        **Description**
      </th>
    </tr>
  </thead>

  <tbody>
    <tr>
      <td>
        `items_per_page`
      </td>

      <td>
        (Optional) Pagination, 20 by default up to 100 results.
      </td>
    </tr>

    <tr>
      <td>
        `scheme`
      </td>

      <td>
        (Optional) Scheme ID. Defaults to the active scheme.
      </td>
    </tr>

    <tr>
      <td>
        `start_date`
      </td>

      <td>
        (Required if no `responses` or `month`)\
        Start of calculation period.  Format: `YYYY-MM-DDThh:mm:ss`
      </td>
    </tr>

    <tr>
      <td>
        `end_date`
      </td>

      <td>
        (Required if no `responses` or `month`)\
        End of calculation period. Format: `YYYY-MM-DDThh:mm:ss`
      </td>
    </tr>

    <tr>
      <td>
        `month`
      </td>

      <td>
        (Optional) Filter by month. Format: `YYYY-MM`
      </td>
    </tr>

    <tr>
      <td>
        `place`
      </td>

      <td>
        (Optional) Filter by point of sales ID.
      </td>
    </tr>

    <tr>
      <td>
        `places`
      </td>

      <td>
        (Optional) List of point of sales IDs (comma-separated).
      </td>
    </tr>

    <tr>
      <td>
        `level`
      </td>

      <td>
        (Optional) Filter by level ID.
      </td>
    </tr>

    <tr>
      <td>
        `levels`
      </td>

      <td>
        (Optional) List of level IDs (comma-separated).
      </td>
    </tr>

    <tr>
      <td>
        `categories`
      </td>

      <td>
        (Optional) Filter by category IDs (comma-separated).
      </td>
    </tr>

    <tr>
      <td>
        `responses`
      </td>

      <td>
        (Optional) Filter by response IDs (comma-separated).
      </td>
    </tr>
  </tbody>
</Table>

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
