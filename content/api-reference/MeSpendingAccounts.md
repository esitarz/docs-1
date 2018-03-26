---
title: Spending Accounts
date: 2018-03-26
category: API Reference
tags: Me And My Stuff
slug: Me-And-My-Stuff-MeSpendingAccounts
---
"Me" is a container for read-only endpoints that return a filtered view
of things that the current buyer user is allowed to see, i.e. things
that they are assigned to either directly or as a member of a buyer
organization or user group. It also provides ways for a user to update
or change their own information.

---

## `GET` `v1/me/spendingAccounts`
Get a list of spending accounts visible to this user

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
{'Meta': {'Page': 1, 'PageSize': 20, 'TotalCount': 25, 'TotalPages': 2, 'ItemRange': [1, 20]}, 'Items': [{'ID': '', 'Name': '', 'Balance': 0, 'AllowAsPaymentMethod': False, 'RedemptionCode': '', 'StartDate': '2018-03-21T23:00:00+00:00', 'EndDate': '2018-03-21T23:00:00+00:00', 'xp': {}}]}
```


| Parameters      | Description                    |
|------------------|---------------------------------|
| Name            | ID                             |
| Type            | string                         |
| Description     | ID of the spending account.    |
| Required        | False                          |


| Parameters      | Description                    |
|------------------|---------------------------------|
| Name            | Name                           |
| Type            | string                         |
| Description     | Name of the spending account.  |
| Required        | True                           |


| Parameters      | Description                    |
|------------------|---------------------------------|
| Name            | Balance                        |
| Type            | float                          |
| Description     | Balance of the spending account. |
| Required        | True                           |


| Parameters      | Description                    |
|------------------|---------------------------------|
| Name            | AllowAsPaymentMethod           |
| Type            | boolean                        |
| Description     | Allow as payment method of the spending account. |
| Required        | False                          |


| Parameters      | Description                    |
|------------------|---------------------------------|
| Name            | RedemptionCode                 |
| Type            | string                         |
| Description     | If specified, matching code must be provided on redemption in order for the transaction to be successful. Most commonly used to implement Gift Cards. |
| Required        | False                          |


| Parameters      | Description                    |
|------------------|---------------------------------|
| Name            | StartDate                      |
| Type            | date                           |
| Description     | Start date of the spending account. |
| Required        | False                          |


| Parameters      | Description                    |
|------------------|---------------------------------|
| Name            | EndDate                        |
| Type            | date                           |
| Description     | End date of the spending account. |
| Required        | False                          |


| Parameters      | Description                    |
|------------------|---------------------------------|
| Name            | xp                             |
| Type            | object                         |
| Description     | Container for extended (custom) properties of the spending account. |
| Required        | False                          |

## `GET` `v1/me/spendingaccounts/{spendingAccountID}`
Get a single spending account

| Parameters      | Description                    |
|------------------|---------------------------------|


| Parameters      | Description                    |
|------------------|---------------------------------|
| Name            | spendingAccountID              |
| Type            | string                         |
| Description     | ID of the spending account.    |
| Required        | True                           |

## Requestbody
**Responsestatus**: `200`

## Responsebody
```
{'ID': '', 'Name': '', 'Balance': 0, 'AllowAsPaymentMethod': False, 'RedemptionCode': '', 'StartDate': '2018-03-21T23:00:00+00:00', 'EndDate': '2018-03-21T23:00:00+00:00', 'xp': {}}
```


| Parameters      | Description                    |
|------------------|---------------------------------|
| Name            | ID                             |
| Type            | string                         |
| Description     | ID of the spending account.    |
| Required        | False                          |


| Parameters      | Description                    |
|------------------|---------------------------------|
| Name            | Name                           |
| Type            | string                         |
| Description     | Name of the spending account.  |
| Required        | True                           |


| Parameters      | Description                    |
|------------------|---------------------------------|
| Name            | Balance                        |
| Type            | float                          |
| Description     | Balance of the spending account. |
| Required        | True                           |


| Parameters      | Description                    |
|------------------|---------------------------------|
| Name            | AllowAsPaymentMethod           |
| Type            | boolean                        |
| Description     | Allow as payment method of the spending account. |
| Required        | False                          |


| Parameters      | Description                    |
|------------------|---------------------------------|
| Name            | RedemptionCode                 |
| Type            | string                         |
| Description     | If specified, matching code must be provided on redemption in order for the transaction to be successful. Most commonly used to implement Gift Cards. |
| Required        | False                          |


| Parameters      | Description                    |
|------------------|---------------------------------|
| Name            | StartDate                      |
| Type            | date                           |
| Description     | Start date of the spending account. |
| Required        | False                          |


| Parameters      | Description                    |
|------------------|---------------------------------|
| Name            | EndDate                        |
| Type            | date                           |
| Description     | End date of the spending account. |
| Required        | False                          |


| Parameters      | Description                    |
|------------------|---------------------------------|
| Name            | xp                             |
| Type            | object                         |
| Description     | Container for extended (custom) properties of the spending account. |
| Required        | False                          |
