---
title: Promotions
date: 2018-03-23
category: API Reference
tags: Orders And Fulfillment
slug: Promotions
---
Promotions are used to reduce the cost of a line item or an order.
Promotions can have redemption rules that can be applied for available
dates, occurences and value.
Promotions can be assigned to Products, Categories, Buyers, UserGroups
and Users for redemption.

---

## `GET` `v1/promotions/{promotionID}`
Get a single promotion

| Parameters      | Description                    |
|------------------|---------------------------------|


| Parameters      | Description                    |
|------------------|---------------------------------|
| Name            | promotionID                    |
| Type            | string                         |
| Description     | ID of the promotion.           |
| Required        | True                           |

## Requestbody
**Responsestatus**: `200`

## Responsebody
```
{'ID': '', 'Code': '', 'Name': '', 'RedemptionLimit': 0, 'RedemptionLimitPerUser': 0, 'RedemptionCount': 0, 'Description': '', 'FinePrint': '', 'StartDate': '2018-03-21T23:00:00+00:00', 'ExpirationDate': '2018-03-21T23:00:00+00:00', 'EligibleExpression': '', 'ValueExpression': '', 'CanCombine': False, 'xp': {}}
```


| Parameters      | Description                    |
|------------------|---------------------------------|
| Name            | ID                             |
| Type            | string                         |
| Description     | ID of the promotion.           |
| Required        | False                          |


| Parameters      | Description                    |
|------------------|---------------------------------|
| Name            | Code                           |
| Type            | string                         |
| Description     | Must be unique. Entered by buyer when adding promo to order. |
| Required        | True                           |


| Parameters      | Description                    |
|------------------|---------------------------------|
| Name            | Name                           |
| Type            | string                         |
| Description     | Name of the promotion.         |
| Required        | False                          |


| Parameters      | Description                    |
|------------------|---------------------------------|
| Name            | RedemptionLimit                |
| Type            | integer                        |
| Description     | Redemption limit of the promotion. |
| Required        | False                          |


| Parameters      | Description                    |
|------------------|---------------------------------|
| Name            | RedemptionLimitPerUser         |
| Type            | integer                        |
| Description     | Redemption limit per user of the promotion. |
| Required        | False                          |


| Parameters      | Description                    |
|------------------|---------------------------------|
| Name            | RedemptionCount                |
| Type            | integer                        |
| Description     | Redemption count of the promotion. |
| Required        | False                          |


| Parameters      | Description                    |
|------------------|---------------------------------|
| Name            | Description                    |
| Type            | string                         |
| Description     | Description of the promotion.  |
| Required        | False                          |


| Parameters      | Description                    |
|------------------|---------------------------------|
| Name            | FinePrint                      |
| Type            | string                         |
| Description     | Terms, conditions, and other legal jargon. |
| Required        | False                          |


| Parameters      | Description                    |
|------------------|---------------------------------|
| Name            | StartDate                      |
| Type            | date                           |
| Description     | Start date of the promotion.   |
| Required        | False                          |


| Parameters      | Description                    |
|------------------|---------------------------------|
| Name            | ExpirationDate                 |
| Type            | date                           |
| Description     | Expiration date of the promotion. |
| Required        | False                          |


| Parameters      | Description                    |
|------------------|---------------------------------|
| Name            | EligibleExpression             |
| Type            | string                         |
| Description     | Eligible expression of the promotion. |
| Required        | True                           |


| Parameters      | Description                    |
|------------------|---------------------------------|
| Name            | ValueExpression                |
| Type            | string                         |
| Description     | Value expression of the promotion. |
| Required        | True                           |


| Parameters      | Description                    |
|------------------|---------------------------------|
| Name            | CanCombine                     |
| Type            | boolean                        |
| Description     | Can combine of the promotion.  |
| Required        | False                          |


| Parameters      | Description                    |
|------------------|---------------------------------|
| Name            | xp                             |
| Type            | object                         |
| Description     | Container for extended (custom) properties of the promotion. |
| Required        | False                          |

## `GET` `v1/promotions`
Get a list of promotions

| Parameters      | Description                    |
|------------------|---------------------------------|


| Parameters      | Description                    |
|------------------|---------------------------------|
| Name            | search                         |
| Type            | string                         |
| Description     | Word or phrase to search for.  |
| Required        | False                          |


| Parameters      | Description                    |
|------------------|---------------------------------|
| Name            | searchOn                       |
| Type            | string                         |
| Description     | Comma-delimited list of fields to search on. |
| Required        | False                          |


| Parameters      | Description                    |
|------------------|---------------------------------|
| Name            | sortBy                         |
| Type            | string                         |
| Description     | Comma-delimited list of fields to sort by. |
| Required        | False                          |


| Parameters      | Description                    |
|------------------|---------------------------------|
| Name            | page                           |
| Type            | integer                        |
| Description     | Page of results to return. Default: 1 |
| Required        | False                          |


| Parameters      | Description                    |
|------------------|---------------------------------|
| Name            | pageSize                       |
| Type            | integer                        |
| Description     | Number of results to return per page. Default: 20, max: 100. |
| Required        | False                          |


| Parameters      | Description                    |
|------------------|---------------------------------|
| Name            | filters                        |
| Type            | object                         |
| Description     | Any additional key/value pairs passed in the query string are interpretted as filters. Valid keys are top-level properties of the returned model or 'xp.???' |
| Required        | False                          |

## Requestbody
**Responsestatus**: `200`

## Responsebody
```
{'Meta': {'Page': 1, 'PageSize': 20, 'TotalCount': 25, 'TotalPages': 2, 'ItemRange': [1, 20]}, 'Items': [{'ID': '', 'Code': '', 'Name': '', 'RedemptionLimit': 0, 'RedemptionLimitPerUser': 0, 'RedemptionCount': 0, 'Description': '', 'FinePrint': '', 'StartDate': '2018-03-21T23:00:00+00:00', 'ExpirationDate': '2018-03-21T23:00:00+00:00', 'EligibleExpression': '', 'ValueExpression': '', 'CanCombine': False, 'xp': {}}]}
```


| Parameters      | Description                    |
|------------------|---------------------------------|
| Name            | ID                             |
| Type            | string                         |
| Description     | ID of the promotion.           |
| Required        | False                          |


| Parameters      | Description                    |
|------------------|---------------------------------|
| Name            | Code                           |
| Type            | string                         |
| Description     | Must be unique. Entered by buyer when adding promo to order. |
| Required        | True                           |


| Parameters      | Description                    |
|------------------|---------------------------------|
| Name            | Name                           |
| Type            | string                         |
| Description     | Name of the promotion.         |
| Required        | False                          |


| Parameters      | Description                    |
|------------------|---------------------------------|
| Name            | RedemptionLimit                |
| Type            | integer                        |
| Description     | Redemption limit of the promotion. |
| Required        | False                          |


| Parameters      | Description                    |
|------------------|---------------------------------|
| Name            | RedemptionLimitPerUser         |
| Type            | integer                        |
| Description     | Redemption limit per user of the promotion. |
| Required        | False                          |


| Parameters      | Description                    |
|------------------|---------------------------------|
| Name            | RedemptionCount                |
| Type            | integer                        |
| Description     | Redemption count of the promotion. |
| Required        | False                          |


| Parameters      | Description                    |
|------------------|---------------------------------|
| Name            | Description                    |
| Type            | string                         |
| Description     | Description of the promotion.  |
| Required        | False                          |


| Parameters      | Description                    |
|------------------|---------------------------------|
| Name            | FinePrint                      |
| Type            | string                         |
| Description     | Terms, conditions, and other legal jargon. |
| Required        | False                          |


| Parameters      | Description                    |
|------------------|---------------------------------|
| Name            | StartDate                      |
| Type            | date                           |
| Description     | Start date of the promotion.   |
| Required        | False                          |


| Parameters      | Description                    |
|------------------|---------------------------------|
| Name            | ExpirationDate                 |
| Type            | date                           |
| Description     | Expiration date of the promotion. |
| Required        | False                          |


| Parameters      | Description                    |
|------------------|---------------------------------|
| Name            | EligibleExpression             |
| Type            | string                         |
| Description     | Eligible expression of the promotion. |
| Required        | True                           |


| Parameters      | Description                    |
|------------------|---------------------------------|
| Name            | ValueExpression                |
| Type            | string                         |
| Description     | Value expression of the promotion. |
| Required        | True                           |


| Parameters      | Description                    |
|------------------|---------------------------------|
| Name            | CanCombine                     |
| Type            | boolean                        |
| Description     | Can combine of the promotion.  |
| Required        | False                          |


| Parameters      | Description                    |
|------------------|---------------------------------|
| Name            | xp                             |
| Type            | object                         |
| Description     | Container for extended (custom) properties of the promotion. |
| Required        | False                          |

## `POST` `v1/promotions`
Create a new promotion
## Requestbody
```
{'ID': '', 'Code': '', 'Name': '', 'RedemptionLimit': 0, 'RedemptionLimitPerUser': 0, 'Description': '', 'FinePrint': '', 'StartDate': '2018-03-21T23:00:00+00:00', 'ExpirationDate': '2018-03-21T23:00:00+00:00', 'EligibleExpression': '', 'ValueExpression': '', 'CanCombine': False, 'xp': {}}
```

```
[{'Name': 'ID', 'Type': 'string', 'Description': 'ID of the promotion. Can only contain characters Aa-Zz, 0-9, -, and _. Searchable: priority level 1. Sortable: priority level 2.', 'Required': False}, {'Name': 'Code', 'Type': 'string', 'Description': 'Must be unique. Entered by buyer when adding promo to order.', 'Required': True}, {'Name': 'Name', 'Type': 'string', 'Description': 'Name of the promotion. Max length 100 characters. Searchable: priority level 2. Sortable: priority level 1.', 'Required': False}, {'Name': 'RedemptionLimit', 'Type': 'integer', 'Description': 'Redemption limit of the promotion.', 'Required': False}, {'Name': 'RedemptionLimitPerUser', 'Type': 'integer', 'Description': 'Redemption limit per user of the promotion.', 'Required': False}, {'Name': 'Description', 'Type': 'string', 'Description': 'Description of the promotion. Max length 2000 characters. Searchable: priority level 4.', 'Required': False}, {'Name': 'FinePrint', 'Type': 'string', 'Description': 'Terms, conditions, and other legal jargon.', 'Required': False}, {'Name': 'StartDate', 'Type': 'date', 'Description': 'Start date of the promotion. Sortable.', 'Required': False}, {'Name': 'ExpirationDate', 'Type': 'date', 'Description': 'Expiration date of the promotion. Sortable.', 'Required': False}, {'Name': 'EligibleExpression', 'Type': 'string', 'Description': 'Eligible expression of the promotion. Required. Max length 400 characters. Searchable: priority level 6. Sortable.', 'Required': True}, {'Name': 'ValueExpression', 'Type': 'string', 'Description': 'Value expression of the promotion. Required. Max length 400 characters. Searchable: priority level 7. Sortable.', 'Required': True}, {'Name': 'CanCombine', 'Type': 'boolean', 'Description': 'Can combine of the promotion. Sortable.', 'Required': False}, {'Name': 'xp', 'Type': 'object', 'Description': 'Container for extended (custom) properties of the promotion.', 'Required': False}]
```

**Responsestatus**: `201`

## Responsebody
```
{'ID': '', 'Code': '', 'Name': '', 'RedemptionLimit': 0, 'RedemptionLimitPerUser': 0, 'RedemptionCount': 0, 'Description': '', 'FinePrint': '', 'StartDate': '2018-03-21T23:00:00+00:00', 'ExpirationDate': '2018-03-21T23:00:00+00:00', 'EligibleExpression': '', 'ValueExpression': '', 'CanCombine': False, 'xp': {}}
```


| Parameters      | Description                    |
|------------------|---------------------------------|
| Name            | ID                             |
| Type            | string                         |
| Description     | ID of the promotion.           |
| Required        | False                          |


| Parameters      | Description                    |
|------------------|---------------------------------|
| Name            | Code                           |
| Type            | string                         |
| Description     | Must be unique. Entered by buyer when adding promo to order. |
| Required        | True                           |


| Parameters      | Description                    |
|------------------|---------------------------------|
| Name            | Name                           |
| Type            | string                         |
| Description     | Name of the promotion.         |
| Required        | False                          |


| Parameters      | Description                    |
|------------------|---------------------------------|
| Name            | RedemptionLimit                |
| Type            | integer                        |
| Description     | Redemption limit of the promotion. |
| Required        | False                          |


| Parameters      | Description                    |
|------------------|---------------------------------|
| Name            | RedemptionLimitPerUser         |
| Type            | integer                        |
| Description     | Redemption limit per user of the promotion. |
| Required        | False                          |


| Parameters      | Description                    |
|------------------|---------------------------------|
| Name            | RedemptionCount                |
| Type            | integer                        |
| Description     | Redemption count of the promotion. |
| Required        | False                          |


| Parameters      | Description                    |
|------------------|---------------------------------|
| Name            | Description                    |
| Type            | string                         |
| Description     | Description of the promotion.  |
| Required        | False                          |


| Parameters      | Description                    |
|------------------|---------------------------------|
| Name            | FinePrint                      |
| Type            | string                         |
| Description     | Terms, conditions, and other legal jargon. |
| Required        | False                          |


| Parameters      | Description                    |
|------------------|---------------------------------|
| Name            | StartDate                      |
| Type            | date                           |
| Description     | Start date of the promotion.   |
| Required        | False                          |


| Parameters      | Description                    |
|------------------|---------------------------------|
| Name            | ExpirationDate                 |
| Type            | date                           |
| Description     | Expiration date of the promotion. |
| Required        | False                          |


| Parameters      | Description                    |
|------------------|---------------------------------|
| Name            | EligibleExpression             |
| Type            | string                         |
| Description     | Eligible expression of the promotion. |
| Required        | True                           |


| Parameters      | Description                    |
|------------------|---------------------------------|
| Name            | ValueExpression                |
| Type            | string                         |
| Description     | Value expression of the promotion. |
| Required        | True                           |


| Parameters      | Description                    |
|------------------|---------------------------------|
| Name            | CanCombine                     |
| Type            | boolean                        |
| Description     | Can combine of the promotion.  |
| Required        | False                          |


| Parameters      | Description                    |
|------------------|---------------------------------|
| Name            | xp                             |
| Type            | object                         |
| Description     | Container for extended (custom) properties of the promotion. |
| Required        | False                          |

## `PUT` `v1/promotions/{promotionID}`
Create or update a promotion

| Parameters      | Description                    |
|------------------|---------------------------------|


| Parameters      | Description                    |
|------------------|---------------------------------|
| Name            | promotionID                    |
| Type            | string                         |
| Description     | ID of the promotion.           |
| Required        | True                           |

## Requestbody
```
{'ID': '', 'Code': '', 'Name': '', 'RedemptionLimit': 0, 'RedemptionLimitPerUser': 0, 'Description': '', 'FinePrint': '', 'StartDate': '2018-03-21T23:00:00+00:00', 'ExpirationDate': '2018-03-21T23:00:00+00:00', 'EligibleExpression': '', 'ValueExpression': '', 'CanCombine': False, 'xp': {}}
```

```
[{'Name': 'ID', 'Type': 'string', 'Description': 'ID of the promotion. Can only contain characters Aa-Zz, 0-9, -, and _. Searchable: priority level 1. Sortable: priority level 2.', 'Required': False}, {'Name': 'Code', 'Type': 'string', 'Description': 'Must be unique. Entered by buyer when adding promo to order.', 'Required': True}, {'Name': 'Name', 'Type': 'string', 'Description': 'Name of the promotion. Max length 100 characters. Searchable: priority level 2. Sortable: priority level 1.', 'Required': False}, {'Name': 'RedemptionLimit', 'Type': 'integer', 'Description': 'Redemption limit of the promotion.', 'Required': False}, {'Name': 'RedemptionLimitPerUser', 'Type': 'integer', 'Description': 'Redemption limit per user of the promotion.', 'Required': False}, {'Name': 'Description', 'Type': 'string', 'Description': 'Description of the promotion. Max length 2000 characters. Searchable: priority level 4.', 'Required': False}, {'Name': 'FinePrint', 'Type': 'string', 'Description': 'Terms, conditions, and other legal jargon.', 'Required': False}, {'Name': 'StartDate', 'Type': 'date', 'Description': 'Start date of the promotion. Sortable.', 'Required': False}, {'Name': 'ExpirationDate', 'Type': 'date', 'Description': 'Expiration date of the promotion. Sortable.', 'Required': False}, {'Name': 'EligibleExpression', 'Type': 'string', 'Description': 'Eligible expression of the promotion. Required. Max length 400 characters. Searchable: priority level 6. Sortable.', 'Required': True}, {'Name': 'ValueExpression', 'Type': 'string', 'Description': 'Value expression of the promotion. Required. Max length 400 characters. Searchable: priority level 7. Sortable.', 'Required': True}, {'Name': 'CanCombine', 'Type': 'boolean', 'Description': 'Can combine of the promotion. Sortable.', 'Required': False}, {'Name': 'xp', 'Type': 'object', 'Description': 'Container for extended (custom) properties of the promotion.', 'Required': False}]
```

**Responsestatus**: `200`

## Responsebody
```
{'ID': '', 'Code': '', 'Name': '', 'RedemptionLimit': 0, 'RedemptionLimitPerUser': 0, 'RedemptionCount': 0, 'Description': '', 'FinePrint': '', 'StartDate': '2018-03-21T23:00:00+00:00', 'ExpirationDate': '2018-03-21T23:00:00+00:00', 'EligibleExpression': '', 'ValueExpression': '', 'CanCombine': False, 'xp': {}}
```


| Parameters      | Description                    |
|------------------|---------------------------------|
| Name            | ID                             |
| Type            | string                         |
| Description     | ID of the promotion.           |
| Required        | False                          |


| Parameters      | Description                    |
|------------------|---------------------------------|
| Name            | Code                           |
| Type            | string                         |
| Description     | Must be unique. Entered by buyer when adding promo to order. |
| Required        | True                           |


| Parameters      | Description                    |
|------------------|---------------------------------|
| Name            | Name                           |
| Type            | string                         |
| Description     | Name of the promotion.         |
| Required        | False                          |


| Parameters      | Description                    |
|------------------|---------------------------------|
| Name            | RedemptionLimit                |
| Type            | integer                        |
| Description     | Redemption limit of the promotion. |
| Required        | False                          |


| Parameters      | Description                    |
|------------------|---------------------------------|
| Name            | RedemptionLimitPerUser         |
| Type            | integer                        |
| Description     | Redemption limit per user of the promotion. |
| Required        | False                          |


| Parameters      | Description                    |
|------------------|---------------------------------|
| Name            | RedemptionCount                |
| Type            | integer                        |
| Description     | Redemption count of the promotion. |
| Required        | False                          |


| Parameters      | Description                    |
|------------------|---------------------------------|
| Name            | Description                    |
| Type            | string                         |
| Description     | Description of the promotion.  |
| Required        | False                          |


| Parameters      | Description                    |
|------------------|---------------------------------|
| Name            | FinePrint                      |
| Type            | string                         |
| Description     | Terms, conditions, and other legal jargon. |
| Required        | False                          |


| Parameters      | Description                    |
|------------------|---------------------------------|
| Name            | StartDate                      |
| Type            | date                           |
| Description     | Start date of the promotion.   |
| Required        | False                          |


| Parameters      | Description                    |
|------------------|---------------------------------|
| Name            | ExpirationDate                 |
| Type            | date                           |
| Description     | Expiration date of the promotion. |
| Required        | False                          |


| Parameters      | Description                    |
|------------------|---------------------------------|
| Name            | EligibleExpression             |
| Type            | string                         |
| Description     | Eligible expression of the promotion. |
| Required        | True                           |


| Parameters      | Description                    |
|------------------|---------------------------------|
| Name            | ValueExpression                |
| Type            | string                         |
| Description     | Value expression of the promotion. |
| Required        | True                           |


| Parameters      | Description                    |
|------------------|---------------------------------|
| Name            | CanCombine                     |
| Type            | boolean                        |
| Description     | Can combine of the promotion.  |
| Required        | False                          |


| Parameters      | Description                    |
|------------------|---------------------------------|
| Name            | xp                             |
| Type            | object                         |
| Description     | Container for extended (custom) properties of the promotion. |
| Required        | False                          |

## `DELETE` `v1/promotions/{promotionID}`
Delete a promotion

| Parameters      | Description                    |
|------------------|---------------------------------|


| Parameters      | Description                    |
|------------------|---------------------------------|
| Name            | promotionID                    |
| Type            | string                         |
| Description     | ID of the promotion.           |
| Required        | True                           |

## Requestbody
**Responsestatus**: `204`

## Responsebody
## `PATCH` `v1/promotions/{promotionID}`
Partially update a promotion

| Parameters      | Description                    |
|------------------|---------------------------------|


| Parameters      | Description                    |
|------------------|---------------------------------|
| Name            | promotionID                    |
| Type            | string                         |
| Description     | ID of the promotion.           |
| Required        | True                           |

## Requestbody
```
{'ID': '', 'Code': '', 'Name': '', 'RedemptionLimit': 0, 'RedemptionLimitPerUser': 0, 'Description': '', 'FinePrint': '', 'StartDate': '2018-03-21T23:00:00+00:00', 'ExpirationDate': '2018-03-21T23:00:00+00:00', 'EligibleExpression': '', 'ValueExpression': '', 'CanCombine': False, 'xp': {}}
```

```
[{'Name': 'ID', 'Type': 'string', 'Description': 'ID of the promotion. Can only contain characters Aa-Zz, 0-9, -, and _. Searchable: priority level 1. Sortable: priority level 2.', 'Required': False}, {'Name': 'Code', 'Type': 'string', 'Description': 'Must be unique. Entered by buyer when adding promo to order.', 'Required': True}, {'Name': 'Name', 'Type': 'string', 'Description': 'Name of the promotion. Max length 100 characters. Searchable: priority level 2. Sortable: priority level 1.', 'Required': False}, {'Name': 'RedemptionLimit', 'Type': 'integer', 'Description': 'Redemption limit of the promotion.', 'Required': False}, {'Name': 'RedemptionLimitPerUser', 'Type': 'integer', 'Description': 'Redemption limit per user of the promotion.', 'Required': False}, {'Name': 'Description', 'Type': 'string', 'Description': 'Description of the promotion. Max length 2000 characters. Searchable: priority level 4.', 'Required': False}, {'Name': 'FinePrint', 'Type': 'string', 'Description': 'Terms, conditions, and other legal jargon.', 'Required': False}, {'Name': 'StartDate', 'Type': 'date', 'Description': 'Start date of the promotion. Sortable.', 'Required': False}, {'Name': 'ExpirationDate', 'Type': 'date', 'Description': 'Expiration date of the promotion. Sortable.', 'Required': False}, {'Name': 'EligibleExpression', 'Type': 'string', 'Description': 'Eligible expression of the promotion. Required. Max length 400 characters. Searchable: priority level 6. Sortable.', 'Required': True}, {'Name': 'ValueExpression', 'Type': 'string', 'Description': 'Value expression of the promotion. Required. Max length 400 characters. Searchable: priority level 7. Sortable.', 'Required': True}, {'Name': 'CanCombine', 'Type': 'boolean', 'Description': 'Can combine of the promotion. Sortable.', 'Required': False}, {'Name': 'xp', 'Type': 'object', 'Description': 'Container for extended (custom) properties of the promotion.', 'Required': False}]
```

**Responsestatus**: `200`

## Responsebody
```
{'ID': '', 'Code': '', 'Name': '', 'RedemptionLimit': 0, 'RedemptionLimitPerUser': 0, 'RedemptionCount': 0, 'Description': '', 'FinePrint': '', 'StartDate': '2018-03-21T23:00:00+00:00', 'ExpirationDate': '2018-03-21T23:00:00+00:00', 'EligibleExpression': '', 'ValueExpression': '', 'CanCombine': False, 'xp': {}}
```


| Parameters      | Description                    |
|------------------|---------------------------------|
| Name            | ID                             |
| Type            | string                         |
| Description     | ID of the promotion.           |
| Required        | False                          |


| Parameters      | Description                    |
|------------------|---------------------------------|
| Name            | Code                           |
| Type            | string                         |
| Description     | Must be unique. Entered by buyer when adding promo to order. |
| Required        | True                           |


| Parameters      | Description                    |
|------------------|---------------------------------|
| Name            | Name                           |
| Type            | string                         |
| Description     | Name of the promotion.         |
| Required        | False                          |


| Parameters      | Description                    |
|------------------|---------------------------------|
| Name            | RedemptionLimit                |
| Type            | integer                        |
| Description     | Redemption limit of the promotion. |
| Required        | False                          |


| Parameters      | Description                    |
|------------------|---------------------------------|
| Name            | RedemptionLimitPerUser         |
| Type            | integer                        |
| Description     | Redemption limit per user of the promotion. |
| Required        | False                          |


| Parameters      | Description                    |
|------------------|---------------------------------|
| Name            | RedemptionCount                |
| Type            | integer                        |
| Description     | Redemption count of the promotion. |
| Required        | False                          |


| Parameters      | Description                    |
|------------------|---------------------------------|
| Name            | Description                    |
| Type            | string                         |
| Description     | Description of the promotion.  |
| Required        | False                          |


| Parameters      | Description                    |
|------------------|---------------------------------|
| Name            | FinePrint                      |
| Type            | string                         |
| Description     | Terms, conditions, and other legal jargon. |
| Required        | False                          |


| Parameters      | Description                    |
|------------------|---------------------------------|
| Name            | StartDate                      |
| Type            | date                           |
| Description     | Start date of the promotion.   |
| Required        | False                          |


| Parameters      | Description                    |
|------------------|---------------------------------|
| Name            | ExpirationDate                 |
| Type            | date                           |
| Description     | Expiration date of the promotion. |
| Required        | False                          |


| Parameters      | Description                    |
|------------------|---------------------------------|
| Name            | EligibleExpression             |
| Type            | string                         |
| Description     | Eligible expression of the promotion. |
| Required        | True                           |


| Parameters      | Description                    |
|------------------|---------------------------------|
| Name            | ValueExpression                |
| Type            | string                         |
| Description     | Value expression of the promotion. |
| Required        | True                           |


| Parameters      | Description                    |
|------------------|---------------------------------|
| Name            | CanCombine                     |
| Type            | boolean                        |
| Description     | Can combine of the promotion.  |
| Required        | False                          |


| Parameters      | Description                    |
|------------------|---------------------------------|
| Name            | xp                             |
| Type            | object                         |
| Description     | Container for extended (custom) properties of the promotion. |
| Required        | False                          |

## `GET` `v1/promotions/assignments`
Get a list of promotion assignments

| Parameters      | Description                    |
|------------------|---------------------------------|


| Parameters      | Description                    |
|------------------|---------------------------------|
| Name            | buyerID                        |
| Type            | string                         |
| Description     | ID of the buyer.               |
| Required        | False                          |


| Parameters      | Description                    |
|------------------|---------------------------------|
| Name            | promotionID                    |
| Type            | string                         |
| Description     | ID of the promotion.           |
| Required        | False                          |


| Parameters      | Description                    |
|------------------|---------------------------------|
| Name            | userID                         |
| Type            | string                         |
| Description     | ID of the user.                |
| Required        | False                          |


| Parameters      | Description                    |
|------------------|---------------------------------|
| Name            | userGroupID                    |
| Type            | string                         |
| Description     | ID of the user group.          |
| Required        | False                          |


| Parameters      | Description                    |
|------------------|---------------------------------|
| Name            | level                          |
| Type            | string                         |
| Description     | Level of the promotion assignment. Possible values: User, Group, Company. |
| Required        | False                          |


| Parameters      | Description                    |
|------------------|---------------------------------|
| Name            | page                           |
| Type            | integer                        |
| Description     | Page of results to return. Default: 1 |
| Required        | False                          |


| Parameters      | Description                    |
|------------------|---------------------------------|
| Name            | pageSize                       |
| Type            | integer                        |
| Description     | Number of results to return per page. Default: 20, max: 100. |
| Required        | False                          |

## Requestbody
**Responsestatus**: `200`

## Responsebody
```
{'Meta': {'Page': 1, 'PageSize': 20, 'TotalCount': 25, 'TotalPages': 2, 'ItemRange': [1, 20]}, 'Items': [{'PromotionID': '', 'BuyerID': '', 'UserGroupID': ''}]}
```


| Parameters      | Description                    |
|------------------|---------------------------------|
| Name            | PromotionID                    |
| Type            | string                         |
| Description     | ID of the promotion.           |
| Required        | True                           |


| Parameters      | Description                    |
|------------------|---------------------------------|
| Name            | BuyerID                        |
| Type            | string                         |
| Description     | ID of the buyer.               |
| Required        | True                           |


| Parameters      | Description                    |
|------------------|---------------------------------|
| Name            | UserGroupID                    |
| Type            | string                         |
| Description     | ID of the user group.          |
| Required        | False                          |

## `POST` `v1/promotions/assignments`
Save a promotion assignment
## Requestbody
```
{'PromotionID': '', 'BuyerID': '', 'UserGroupID': ''}
```

```
[{'Name': 'PromotionID', 'Type': 'string', 'Description': 'ID of the promotion. Required. Sortable: priority level 1.', 'Required': True}, {'Name': 'BuyerID', 'Type': 'string', 'Description': 'ID of the buyer. Required. Sortable: priority level 2.', 'Required': True}, {'Name': 'UserGroupID', 'Type': 'string', 'Description': 'ID of the user group. Sortable: priority level 4.', 'Required': False}]
```

**Responsestatus**: `204`

## Responsebody
## `DELETE` `v1/promotions/{promotionID}/assignments`
Delete a promotion assignment

| Parameters      | Description                    |
|------------------|---------------------------------|


| Parameters      | Description                    |
|------------------|---------------------------------|
| Name            | promotionID                    |
| Type            | string                         |
| Description     | ID of the promotion.           |
| Required        | True                           |


| Parameters      | Description                    |
|------------------|---------------------------------|
| Name            | buyerID                        |
| Type            | string                         |
| Description     | ID of the buyer.               |
| Required        | True                           |


| Parameters      | Description                    |
|------------------|---------------------------------|
| Name            | userID                         |
| Type            | string                         |
| Description     | ID of the user.                |
| Required        | False                          |


| Parameters      | Description                    |
|------------------|---------------------------------|
| Name            | userGroupID                    |
| Type            | string                         |
| Description     | ID of the user group.          |
| Required        | False                          |

## Requestbody
**Responsestatus**: `204`

## Responsebody