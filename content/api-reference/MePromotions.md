---
title: Promotions
date: 2018-03-23
category: API Reference
tags: Me And My Stuff
slug: MePromotions
---
"Me" is a container for read-only endpoints that return a filtered view
of things that the current buyer user is allowed to see, i.e. things
that they are assigned to either directly or as a member of a buyer
organization or user group. It also provides ways for a user to update
or change their own information.

---

## `GET` `v1/me/promotions`
Get a list of promotions visible to this user

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

## `GET` `v1/me/promotions/{promotionID}`
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
