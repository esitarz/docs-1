---
title: Spending Accounts
date: 2018-03-26
category: API Reference
tags: Buyers
slug: Buyers-SpendingAccounts
---
Spending Accounts are funds given to users by a managing entity and are
managed as part of a user's account. These funds are generally used as
"corporate dollars", "rewards dollars", or "gift cards".
They can be used to pay for all of or part of an order with parameters
that control account expiration, balance available, balance renewal,
user access and overdraft.
Multiple spending accounts can be assigned to a member of an
organization and applied to all transactions, but only one can be used
as a payment method.
When multiple Spending Accounts are used on a transaction each is
deducted individually.

---

## `GET` `v1/buyers/{buyerID}/spendingaccounts/{spendingAccountID}`
Get a single spending account

| Parameters      | Description                    |
|------------------|---------------------------------|


| Parameters      | Description                    |
|------------------|---------------------------------|
| Name            | buyerID                        |
| Type            | string                         |
| Description     | ID of the buyer.               |
| Required        | True                           |


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

## `GET` `v1/buyers/{buyerID}/spendingaccounts`
Get a list of spending accounts

| Parameters      | Description                    |
|------------------|---------------------------------|


| Parameters      | Description                    |
|------------------|---------------------------------|
| Name            | buyerID                        |
| Type            | string                         |
| Description     | ID of the buyer.               |
| Required        | True                           |


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

## `POST` `v1/buyers/{buyerID}/spendingaccounts`
Create a new spending account

| Parameters      | Description                    |
|------------------|---------------------------------|


| Parameters      | Description                    |
|------------------|---------------------------------|
| Name            | buyerID                        |
| Type            | string                         |
| Description     | ID of the buyer.               |
| Required        | True                           |

## Requestbody
```
{'ID': '', 'Name': '', 'Balance': 0, 'AllowAsPaymentMethod': False, 'RedemptionCode': '', 'StartDate': '2018-03-21T23:00:00+00:00', 'EndDate': '2018-03-21T23:00:00+00:00', 'xp': {}}
```

```
[{'Name': 'ID', 'Type': 'string', 'Description': 'ID of the spending account. Can only contain characters Aa-Zz, 0-9, -, and _. Searchable: priority level 1. Sortable: priority level 2.', 'Required': False}, {'Name': 'Name', 'Type': 'string', 'Description': 'Name of the spending account. Required. Max length 100 characters. Searchable: priority level 2. Sortable: priority level 1.', 'Required': True}, {'Name': 'Balance', 'Type': 'float', 'Description': 'Balance of the spending account. Required.', 'Required': True}, {'Name': 'AllowAsPaymentMethod', 'Type': 'boolean', 'Description': 'Allow as payment method of the spending account.', 'Required': False}, {'Name': 'RedemptionCode', 'Type': 'string', 'Description': 'If specified, matching code must be provided on redemption in order for the transaction to be successful. Most commonly used to implement Gift Cards.', 'Required': False}, {'Name': 'StartDate', 'Type': 'date', 'Description': 'Start date of the spending account.', 'Required': False}, {'Name': 'EndDate', 'Type': 'date', 'Description': 'End date of the spending account.', 'Required': False}, {'Name': 'xp', 'Type': 'object', 'Description': 'Container for extended (custom) properties of the spending account.', 'Required': False}]
```

**Responsestatus**: `201`

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

## `PUT` `v1/buyers/{buyerID}/spendingaccounts/{spendingAccountID}`
Create or update a spending account

| Parameters      | Description                    |
|------------------|---------------------------------|


| Parameters      | Description                    |
|------------------|---------------------------------|
| Name            | buyerID                        |
| Type            | string                         |
| Description     | ID of the buyer.               |
| Required        | True                           |


| Parameters      | Description                    |
|------------------|---------------------------------|
| Name            | spendingAccountID              |
| Type            | string                         |
| Description     | ID of the spending account.    |
| Required        | True                           |

## Requestbody
```
{'ID': '', 'Name': '', 'Balance': 0, 'AllowAsPaymentMethod': False, 'RedemptionCode': '', 'StartDate': '2018-03-21T23:00:00+00:00', 'EndDate': '2018-03-21T23:00:00+00:00', 'xp': {}}
```

```
[{'Name': 'ID', 'Type': 'string', 'Description': 'ID of the spending account. Can only contain characters Aa-Zz, 0-9, -, and _. Searchable: priority level 1. Sortable: priority level 2.', 'Required': False}, {'Name': 'Name', 'Type': 'string', 'Description': 'Name of the spending account. Required. Max length 100 characters. Searchable: priority level 2. Sortable: priority level 1.', 'Required': True}, {'Name': 'Balance', 'Type': 'float', 'Description': 'Balance of the spending account. Required.', 'Required': True}, {'Name': 'AllowAsPaymentMethod', 'Type': 'boolean', 'Description': 'Allow as payment method of the spending account.', 'Required': False}, {'Name': 'RedemptionCode', 'Type': 'string', 'Description': 'If specified, matching code must be provided on redemption in order for the transaction to be successful. Most commonly used to implement Gift Cards.', 'Required': False}, {'Name': 'StartDate', 'Type': 'date', 'Description': 'Start date of the spending account.', 'Required': False}, {'Name': 'EndDate', 'Type': 'date', 'Description': 'End date of the spending account.', 'Required': False}, {'Name': 'xp', 'Type': 'object', 'Description': 'Container for extended (custom) properties of the spending account.', 'Required': False}]
```

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

## `DELETE` `v1/buyers/{buyerID}/spendingaccounts/{spendingAccountID}`
Delete a spending account

| Parameters      | Description                    |
|------------------|---------------------------------|


| Parameters      | Description                    |
|------------------|---------------------------------|
| Name            | buyerID                        |
| Type            | string                         |
| Description     | ID of the buyer.               |
| Required        | True                           |


| Parameters      | Description                    |
|------------------|---------------------------------|
| Name            | spendingAccountID              |
| Type            | string                         |
| Description     | ID of the spending account.    |
| Required        | True                           |

## Requestbody
**Responsestatus**: `204`

## Responsebody
## `PATCH` `v1/buyers/{buyerID}/spendingaccounts/{spendingAccountID}`
Partially update a spending account

| Parameters      | Description                    |
|------------------|---------------------------------|


| Parameters      | Description                    |
|------------------|---------------------------------|
| Name            | buyerID                        |
| Type            | string                         |
| Description     | ID of the buyer.               |
| Required        | True                           |


| Parameters      | Description                    |
|------------------|---------------------------------|
| Name            | spendingAccountID              |
| Type            | string                         |
| Description     | ID of the spending account.    |
| Required        | True                           |

## Requestbody
```
{'ID': '', 'Name': '', 'Balance': 0, 'AllowAsPaymentMethod': False, 'RedemptionCode': '', 'StartDate': '2018-03-21T23:00:00+00:00', 'EndDate': '2018-03-21T23:00:00+00:00', 'xp': {}}
```

```
[{'Name': 'ID', 'Type': 'string', 'Description': 'ID of the spending account. Can only contain characters Aa-Zz, 0-9, -, and _. Searchable: priority level 1. Sortable: priority level 2.', 'Required': False}, {'Name': 'Name', 'Type': 'string', 'Description': 'Name of the spending account. Required. Max length 100 characters. Searchable: priority level 2. Sortable: priority level 1.', 'Required': True}, {'Name': 'Balance', 'Type': 'float', 'Description': 'Balance of the spending account. Required.', 'Required': True}, {'Name': 'AllowAsPaymentMethod', 'Type': 'boolean', 'Description': 'Allow as payment method of the spending account.', 'Required': False}, {'Name': 'RedemptionCode', 'Type': 'string', 'Description': 'If specified, matching code must be provided on redemption in order for the transaction to be successful. Most commonly used to implement Gift Cards.', 'Required': False}, {'Name': 'StartDate', 'Type': 'date', 'Description': 'Start date of the spending account.', 'Required': False}, {'Name': 'EndDate', 'Type': 'date', 'Description': 'End date of the spending account.', 'Required': False}, {'Name': 'xp', 'Type': 'object', 'Description': 'Container for extended (custom) properties of the spending account.', 'Required': False}]
```

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

## `GET` `v1/buyers/{buyerID}/spendingaccounts/assignments`
Get a list of spending account assignments

| Parameters      | Description                    |
|------------------|---------------------------------|


| Parameters      | Description                    |
|------------------|---------------------------------|
| Name            | buyerID                        |
| Type            | string                         |
| Description     | ID of the buyer.               |
| Required        | True                           |


| Parameters      | Description                    |
|------------------|---------------------------------|
| Name            | spendingAccountID              |
| Type            | string                         |
| Description     | ID of the spending account.    |
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
| Description     | Level of the spending account assignment. Possible values: User, Group, Company. |
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
{'Meta': {'Page': 1, 'PageSize': 20, 'TotalCount': 25, 'TotalPages': 2, 'ItemRange': [1, 20]}, 'Items': [{'SpendingAccountID': '', 'UserID': '', 'UserGroupID': '', 'AllowExceed': False}]}
```


| Parameters      | Description                    |
|------------------|---------------------------------|
| Name            | SpendingAccountID              |
| Type            | string                         |
| Description     | ID of the spending account.    |
| Required        | True                           |


| Parameters      | Description                    |
|------------------|---------------------------------|
| Name            | UserID                         |
| Type            | string                         |
| Description     | ID of the user.                |
| Required        | False                          |


| Parameters      | Description                    |
|------------------|---------------------------------|
| Name            | UserGroupID                    |
| Type            | string                         |
| Description     | ID of the user group.          |
| Required        | False                          |


| Parameters      | Description                    |
|------------------|---------------------------------|
| Name            | AllowExceed                    |
| Type            | boolean                        |
| Description     | Allow exceed of the spending account assignment. |
| Required        | False                          |

## `POST` `v1/buyers/{buyerID}/spendingaccounts/assignments`
Save a spending account assignment

| Parameters      | Description                    |
|------------------|---------------------------------|


| Parameters      | Description                    |
|------------------|---------------------------------|
| Name            | buyerID                        |
| Type            | string                         |
| Description     | ID of the buyer.               |
| Required        | True                           |

## Requestbody
```
{'SpendingAccountID': '', 'UserID': '', 'UserGroupID': '', 'AllowExceed': False}
```

```
[{'Name': 'SpendingAccountID', 'Type': 'string', 'Description': 'ID of the spending account. Required. Sortable: priority level 1.', 'Required': True}, {'Name': 'UserID', 'Type': 'string', 'Description': 'ID of the user. Sortable: priority level 2.', 'Required': False}, {'Name': 'UserGroupID', 'Type': 'string', 'Description': 'ID of the user group. Sortable: priority level 3.', 'Required': False}, {'Name': 'AllowExceed', 'Type': 'boolean', 'Description': 'Allow exceed of the spending account assignment.', 'Required': False}]
```

**Responsestatus**: `204`

## Responsebody
## `DELETE` `v1/buyers/{buyerID}/spendingaccounts/{spendingAccountID}/assignments`
Delete a spending account assignment

| Parameters      | Description                    |
|------------------|---------------------------------|


| Parameters      | Description                    |
|------------------|---------------------------------|
| Name            | buyerID                        |
| Type            | string                         |
| Description     | ID of the buyer.               |
| Required        | True                           |


| Parameters      | Description                    |
|------------------|---------------------------------|
| Name            | spendingAccountID              |
| Type            | string                         |
| Description     | ID of the spending account.    |
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