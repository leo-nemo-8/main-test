---
title: Surveys & Question Types Deep Dive
excerpt: From Resource Management to Structural Logic
deprecated: false
hidden: false
metadata:
  robots: index
---
As established in the **Core API** overview, surveys are one of the four essential pillars of the Goodays environment. While the Core API provides the endpoints necessary to consult and list your survey resources, this section explores the internal logic and data formats that power them.

A Goodays survey is a dynamic tool designed to capture the nuances of the end customer experience. It can range from a single satisfaction question to a complex, multi-path journey using "Mother-Daughter" conditional logic. Understanding these structures is critical for several key technical workflows:

* **Interpreting Data:** Correcty parsing the JSON results returned by the Response API.
* **Pushing Feedback:** Formatting the `answers` array correctly when using the Collect API to import external data.
* **Data Analysis:** Understanding how specific question types (like NPS or Stars) contribute to the calculated values in the Metrics API.

The following guide details every question type available in Goodays and how their data is structured in both the survey definition and the user's response.

***

# Survey Question Types & Structures

Goodays surveys are highly customizable and support a wide variety of question formats—ranging from simple text inputs to complex, conditional logic (mother-daughter questions).

When querying the [Response API](/doc/) understanding the `type` of question and its configuration in the `options` object is crucial for properly parsing the response data.

***

## Core Question Object Structure

Before diving into specific types, it's important to understand the basic structure of a question in the Goodays Survey API. Each question object contains standard metadata:

```json
{
    "id": "nlxDYWQJ8M",
    "position": 1,
    "title": "How would you rate your overall experience at Jurassic Park?",
    "enabled": true,
    "type": "stars",
    "enabled_at": "2026-03-11T17:09:21.776819+01:00",
    "disabled_at": null,
    "options": {},
    "sub_questions": []
}
```

* `type`: Defines the format of the question (e.g., `stars`, `text`, `nps`).
* `options`: A configuration object containing type-specific parameters (e.g., alert limit, skippable flags).
* `sub_questions`: An array containing conditional "daughter" questions that are triggered based on the end user's answer.

***

## Supported Question Types

Here is a detailed breakdown of all available question `type` values, including how they are configured in the survey definition and how the user's answer is formatted in the Response API payload.

### 1. Stars Rating (`stars`)

Used for standard 1-to-5 star rating scales.

* **Configuration:** The `options` object can include an `alert_limit` (e.g., 2).
* **Response Payload:** The `value` is an **Integer** representing the number of stars selected.

**Response Example:**

```json
{
    "value": 2,
    "question": {
        "id": "nlxDYWQJ8M",
        "title": "How would you rate your overall experience at Jurassic Park?",
        "type": "stars"
    }
}
```

### 2. End Customer Satisfaction (`csat`)

A metric used to measure user satisfaction, often represented visually as a scale (e.g., 1 to 5).

* **Configuration:** The `options` object can include an `alert_limit` (e.g., 2).
* **Response Payload:** The `value` is an **Integer**.

**Response Example:**

```json
{
    "value": 2,
    "question": {
        "id": "yLdLYQpm4j",
        "title": "How satisfied were you with the organization and flow of your visit to Jurassic Park?",
        "type": "csat"
    }
}
```

### 3. Net Promoter Score (`nps`)

Used to measure end customer loyalty. It asks how likely the end customer is to recommend the business on a scale of 0 to 10.

* **Configuration:** The `options` object can include an `alert_limit` (e.g., 2).
* **Response Payload:** The `value` is an **Integer** (0-10).

**Response Example:**

```json
{
    "value": 4,
    "question": {
        "id": "Q54E5XpK4y",
        "title": "How likely are you to recommend Jurassic Park to a friend or family member?",
        "type": "nps"
    }
}
```

### 4. Open-ended Text (`text`)

A free-form text input field for end customers to leave verbatim feedback.

* **Configuration:** Typically uses an empty options object (unless configured as skippable).
* **Response Payload:** The `value` is a **String**.

**Response Example:**

```json
{
    "value": "More raptor !",
    "question": {
        "id": "Zmxo3QWqxj",
        "title": "What could we improve to make your next visit to Jurassic Park even better?",
        "type": "text"
    }
}
```

### 5. Single Choice (`choices`)

A list of options where the user can only select **one** answer.

* **Configuration:** The `options` object contains an array of `choices` (Strings).
* **Response Payload:** The `value` is a **String** exactly matching the chosen option.

**Survey Configuration Example:**

```json
"options": {
    "choices": [
        "The T-Rex encounter",
        "The raptor zone",
        "The dinosaur safari tour"
    ]
}
```

**Response Example:**

```json
{
    "value": "The raptor zone",
    "question": {
        "id": "k6xmwOvKdj",
        "title": "What was the highlight of your visit to Jurassic Park?",
        "type": "choices"
    }
}
```

### 6. Multiple Choice (`multiple_answers`)

A list of options where the user can select **one or more** answers.

* **Configuration:** The `options` object contains an array of available `choices`.
* **Response Payload:** The `value` is an **Array of Strings**, containing all selected options.

**Survey Configuration Example:**

```json
"options": {
    "choices": [
        "Waiting time was too long",
        "The park was difficult to navigate",
        "Staff assistance was not sufficient"
    ]
}
```

**Response Example:**

```json
{
    "value": [
        "Some attractions were unavailable",
        "Staff assistance was not sufficient"
    ],
    "question": {
        "id": "pe8NzlDM8j",
        "title": "What was the main issue during your visit?",
        "type": "multiple_answers"
    }
}

```

### 7. Emoji Sentiment (`emoji`)

A visual scale using emojis instead of numbers to capture sentiment.

* **Configuration:** The `options` object contains an array of `labels` corresponding to the emojis.
* **Response Payload:** The `value` is a **String** matching the label of the selected emoji.

**Survey Configuration Example:**

```json
"options": {
    "labels": [
        "Not impressed at all",
        "Slightly impressed",
        "Quite impressed",
        "Very impressed"
    ]
}

```

**Response Example:**

```json
{
    "value": "Very impressed",
    "question": {
        "id": "bJdY1E6OdR",
        "title": "How did you feel when you saw the dinosaurs for the first time?",
        "type": "emoji"
    }
}

```

### 8. Boolean Yes/No (`yesno`)

A simple binary choice.

* **Configuration:** Usually empty `options`.
* **Response Payload:** The `value` is a **String** representing the user's localized choice (e.g., "Oui", "Non", "Yes", "No").

**Response Example:**

```json
{
    "value": "Non",
    "question": {
        "id": "ELxjqVoV4K",
        "title": "Did you feel safe during your visit to Jurassic Park?",
        "type": "yesno"
    }
}

```

***

## Advanced Behaviors

### Conditional Logic (Mother-Daughter Questions)

Goodays supports nested conditional questions. In the survey structure, a "Mother" question will contain a `sub_questions` array. Each "Daughter" question inside this array includes a `triggers` array.

The daughter question is only displayed to the end customer if their answer to the mother question matches one of the values in the `triggers` array.

**Example Logic:**
If a user gives a low CSAT score (1 or 2), we want to ask what went wrong. If they give a high score (4 or 5), we want to ask what worked best.

```json
{
    "id": "yLdLYQpm4j",
    "title": "How satisfied were you with the organization and flow of your visit?",
    "type": "csat",
    "sub_questions": [
        {
            "id": "pe8NzlDM8j",
            "triggers": [1, 2],
            "title": "What was the main issue during your visit?",
            "type": "multiple_answers"
        },
        {
            "id": "158yQm678w",
            "triggers": [4, 5],
            "title": "What worked best during your visit?",
            "type": "multiple_answers"
        }
    ]
}

```

_Note: In the Response API payload, if a daughter question is triggered and answered, it will appear in the flat `answers` array alongside the mother question._

### Skippable Questions

Any question type can be configured as optional. This is defined in the options object of the question by adding a boolean flag and an optional custom label.

```json
"options": {
    "skippable_label": "Skip this question",
    "skippable": true
}

```

If an end customer skips a question, it will simply not appear in the `answers` array of their response payload.

### Handling Alerts (`alert_triggered`)

Score-based questions—specifically **Stars Rating (`stars`)**, **End Customer Satisfaction (`csat`)**, and **Net Promoter Score (`nps`)**—can be configured with an `alert_limit` in their `options` object.

If an and customer submits a score that is **equal to or lower than** this limit, it triggers an alert.

In the Response API payload, this is represented by the `alert_triggered` boolean located at the **root** of the response object (not inside the individual answer).

**Example of a response triggering an alert:**
Here, the customer gave a CSAT score of 2, which hit the alert limit threshold.

```json
{
    "id": "6xmpPLON4j",
    "created_date": "2026-03-12T10:59:52.108239+01:00",
    "answers": [
        {
            "value": 2,
            "question": {
                "id": "yLdLYQpm4j",
                "title": "How satisfied were you with the organization and flow of your visit to Jurassic Park?",
                "type": "csat"
            }
        }
    ],
    "state": "open",
    "alert_triggered": true
}

```

***

## Appendix: Complete JSON Examples

For reference, here are complete JSON payloads illustrating a full survey structure configuration and the corresponding Response API output.

### 1. Complete Survey Structure Example

This JSON represents a full survey configuration, including various question types and mother-daughter logic.

```json
{
    "id": "yLdLGNm8j1",
    "slug": "jp_post_visit",
    "label": "Jurassic Park - Post Visit",
    "enabled": true,
    "questions": [
        {
            "id": "nlxDYWQJ8M",
            "position": 1,
            "title": "How would you rate your overall experience at Jurassic Park?",
            "enabled": true,
            "type": "stars",
            "enabled_at": "2026-03-11T17:09:21.776819+01:00",
            "disabled_at": null,
            "options": {},
            "sub_questions": [
                {
                    "id": "Qe4Z1qMndp",
                    "triggers": [4, 5],
                    "title": "What made your experience memorable?",
                    "enabled": true,
                    "type": "multiple_answers",
                    "enabled_at": "2026-03-11T17:09:21.782354+01:00",
                    "disabled_at": null,
                    "options": {
                        "choices": [
                            "The realism of the dinosaurs",
                            "The excitement of the visit",
                            "The immersive environment",
                            "The quality of the attractions"
                        ]
                    }
                }
            ]
        },
        {
            "id": "yLdLYQpm4j",
            "position": 2,
            "title": "How satisfied were you with the organization and flow of your visit to Jurassic Park?",
            "enabled": true,
            "type": "csat",
            "enabled_at": "2026-03-11T17:09:21.785423+01:00",
            "disabled_at": null,
            "options": {},
            "sub_questions": [
                {
                    "id": "pe8NzlDM8j",
                    "triggers": [1, 2],
                    "title": "What was the main issue during your visit?",
                    "enabled": true,
                    "type": "multiple_answers",
                    "enabled_at": "2026-03-11T17:09:21.788652+01:00",
                    "disabled_at": null,
                    "options": {
                        "choices": [
                            "Waiting time was too long",
                            "The park was difficult to navigate",
                            "Staff assistance was not sufficient",
                            "Some attractions were unavailable",
                            "The visit felt disorganized"
                        ],
                        "skippable_label": "Skip this question",
                        "skippable": true
                    }
                },
                {
                    "id": "158yQm678w",
                    "triggers": [4, 5],
                    "title": "What worked best during your visit?",
                    "enabled": true,
                    "type": "multiple_answers",
                    "enabled_at": "2026-03-11T17:09:21.791675+01:00",
                    "disabled_at": null,
                    "options": {
                        "choices": [
                            "Smooth visitor flow",
                            "Clear directions and signage",
                            "Friendly and helpful staff",
                            "Good attraction availability",
                            "Well-organized experience"
                        ],
                        "skippable_label": "Skip this question",
                        "skippable": true
                    }
                }
            ]
        },
        {
            "id": "bJdY1E6OdR",
            "position": 3,
            "title": "How did you feel when you saw the dinosaurs for the first time?",
            "enabled": true,
            "type": "emoji",
            "enabled_at": "2026-03-11T17:09:21.794878+01:00",
            "disabled_at": null,
            "options": {
                "labels": [
                    "Not impressed at all",
                    "Slightly impressed",
                    "Quite impressed",
                    "Very impressed"
                ]
            },
            "sub_questions": []
        },
        {
            "id": "ELxjqVoV4K",
            "position": 4,
            "title": "Did you feel safe during your visit to Jurassic Park?",
            "enabled": true,
            "type": "yesno",
            "enabled_at": "2026-03-11T17:09:21.797788+01:00",
            "disabled_at": null,
            "options": {},
            "sub_questions": []
        },
        {
            "id": "k6xmwOvKdj",
            "position": 5,
            "title": "What was the highlight of your visit to Jurassic Park?",
            "enabled": true,
            "type": "choices",
            "enabled_at": "2026-03-11T17:09:21.800797+01:00",
            "disabled_at": null,
            "options": {
                "choices": [
                    "The T-Rex encounter",
                    "The raptor zone",
                    "The dinosaur safari tour"
                ]
            },
            "sub_questions": []
        },
        {
            "id": "OJ85go5n4w",
            "position": 6,
            "title": "Which parts of your Jurassic Park visit did you enjoy the most?",
            "enabled": true,
            "type": "multiple_answers",
            "enabled_at": "2026-03-11T17:09:21.803983+01:00",
            "disabled_at": null,
            "options": {
                "choices": [
                    "Seeing the dinosaurs up close",
                    "The guided tour",
                    "The interactive attractions",
                    "The gift shop",
                    "The live shows or demonstrations",
                    "The adventure and excitement"
                ]
            },
            "sub_questions": []
        },
        {
            "id": "Zmxo3QWqxj",
            "position": 7,
            "title": "What could we improve to make your next visit to Jurassic Park even better?",
            "enabled": true,
            "type": "text",
            "enabled_at": "2026-03-11T17:09:21.806988+01:00",
            "disabled_at": null,
            "options": {
                "skippable_label": "Skip this question",
                "skippable": true
            },
            "sub_questions": []
        },
        {
            "id": "Q54E5XpK4y",
            "position": 8,
            "title": "How likely are you to recommend Jurassic Park to a friend or family member?",
            "enabled": true,
            "type": "nps",
            "enabled_at": "2026-03-11T17:09:21.810043+01:00",
            "disabled_at": null,
            "options": {
                "alert_limit": 6
            },
            "sub_questions": []
        }
    ],
    "places": "https://api.goodays.co/v2/surveys/yLdLGNm8j1/places",
    "responses": "https://api.goodays.co/v2/surveys/yLdLGNm8j1/responses"
}

```

### 2. Complete Response API Payload Example

This JSON shows the output returned by the Response API. This single, comprehensive example demonstrates:

* An `alert_triggered` status (due to a low CSAT score of 2).
* A mother-daughter conditional question (the low CSAT score triggered the "main issue" question).
* Included metadata (`message`, `user`, `context`, and `place` blocks).

```json
{
    "next": null,
    "previous": null,
    "results": [
        {
            "id": "6xmpPLON4j",
            "token": "f1f1056a9fac71ca44f7a0267f1833dc5540f1ea0a6d48590ca18d24b69b8b39",
            "created_date": "2026-03-12T10:59:52.108239+01:00",
            "updated_date": "2026-03-12T10:59:52.243673+01:00",
            "source": "widget",
            "survey": {
                "id": "yLdLGNm8j1",
                "slug": "jp_post_visit",
                "label": "Jurassic Park - Post Visit",
                "enabled": true,
                "detail_url": "https://api.goodays.co/v2/surveys/yLdLGNm8j1"
            },
            "answers": [
                {
                    "id": "D82bQgWW38",
                    "value": 2,
                    "question": {
                        "id": "nlxDYWQJ8M",
                        "title": "How would you rate your overall experience at Jurassic Park?",
                        "type": "stars",
                        "enabled": true
                    }
                },
                {
                    "id": "Ed7k21bnLd",
                    "value": 2,
                    "question": {
                        "id": "yLdLYQpm4j",
                        "title": "How satisfied were you with the organization and flow of your visit to Jurassic Park?",
                        "type": "csat",
                        "enabled": true
                    }
                },
                {
                    "id": "Y4WJMZb0Jd",
                    "value": [
                        "Some attractions were unavailable",
                        "Waiting time was too long"
                    ],
                    "question": {
                        "id": "pe8NzlDM8j",
                        "title": "What was the main issue during your visit?",
                        "type": "multiple_answers",
                        "enabled": true
                    }
                },
                {
                    "id": "vdOp5zbjM4",
                    "value": "Non",
                    "question": {
                        "id": "ELxjqVoV4K",
                        "title": "Did you feel safe during your visit to Jurassic Park?",
                        "type": "yesno",
                        "enabled": true
                    }
                },
                {
                    "id": "mxomv9GaNd",
                    "value": 4,
                    "question": {
                        "id": "Q54E5XpK4y",
                        "title": "How likely are you to recommend Jurassic Park to a friend or family member?",
                        "type": "nps",
                        "enabled": true
                    }
                }
            ],
            "message": {
                "id": "vdANkQ1W4j",
                "created_date": "2026-03-12T11:00:48.653910+01:00",
                "type": "Problem",
                "content": "The waiting time for the T-Rex enclosure was unacceptable, and the staff seemed overwhelmed.",
                "attachment": null,
                "sender": {
                    "email": "dr.grant@example.com",
                    "first_name": "Alan",
                    "last_name": "Grant"
                }
            },
            "reply": null,
            "user": {
                "email": "dr.grant@example.com",
                "first_name": "Alan",
                "last_name": "Grant",
                "opt_in": {
                    "newsletter": false,
                    "email": true,
                    "sms": false,
                    "custom": false
                }
            },
            "context": {
                "email": "dr.grant@example.com",
                "phone": "0600000000",
                "crm_id": "VIP-9932",
                "cz_tag": "jp_post_visit",
                "last_name": "Grant",
                "first_name": "Alan"
            },
            "place": {
                "id": "EexqBnL58Y",
                "partner_id": "park-isla-nublar",
                "name": "Jurassic Park - Isla Nublar",
                "enabled": true,
                "detail_url": "https://api.goodays.co/v2/places/EexqBnL58Y"
            },
            "delegated_to": null,
            "attached_messages": [],
            "state": "open",
            "thread": "y8VZ06lL8G",
            "actions": {
                "reply": "https://api.goodays.co/api/v2/responses/6xmpPLON4j/reply",
                "spam": "https://api.goodays.co/api/v2/responses/6xmpPLON4j/spam",
                "close": "https://api.goodays.co/api/v2/responses/6xmpPLON4j/close"
            },
            "alert_triggered": true
        }
    ]
}

```
