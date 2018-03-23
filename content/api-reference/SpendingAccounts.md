---
title: Spending Accounts
date: 2018-03-23
category: API Reference
tags: Buyers
slug: SpendingAccounts
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

## Get a single spending account
### `GET` `v1/buyers/{buyerID}/spendingaccounts/{spendingAccountID}`

| Parameters      | Description                    |
|------------------|---------------------------------|
| Name            | buyerID                        |
| Type            | string                         |
| Description     | ID of the buyer.               |
| Required        | True                           |
| Name            | spendingAccountID              |
| Type            | string                         |
| Description     | ID of the spending account.    |
| Required        | True                           |

 **Requestbody**: 
None
 **Responsestatus**: `200`

 **Responsebody**: 
{'Sample': '{\r\n  "ID": "",\r\n  "Name": "",\r\n  "Balance": 0,\r\n  "AllowAsPaymentMethod": false,\r\n  "RedemptionCode": "",\r\n  "StartDate": "2018-03-21T23:00:00+00:00",\r\n  "EndDate": "2018-03-21T23:00:00+00:00",\r\n  "xp": {}\r\n}', 'Fields': [{'Name': 'ID', 'Type': 'string', 'Description': 'ID of the spending account.', 'Required': False}, {'Name': 'Name', 'Type': 'string', 'Description': 'Name of the spending account.', 'Required': True}, {'Name': 'Balance', 'Type': 'float', 'Description': 'Balance of the spending account.', 'Required': True}, {'Name': 'AllowAsPaymentMethod', 'Type': 'boolean', 'Description': 'Allow as payment method of the spending account.', 'Required': False}, {'Name': 'RedemptionCode', 'Type': 'string', 'Description': 'If specified, matching code must be provided on redemption in order for the transaction to be successful. Most commonly used to implement Gift Cards.', 'Required': False}, {'Name': 'StartDate', 'Type': 'date', 'Description': 'Start date of the spending account.', 'Required': False}, {'Name': 'EndDate', 'Type': 'date', 'Description': 'End date of the spending account.', 'Required': False}, {'Name': 'xp', 'Type': 'object', 'Description': 'Container for extended (custom) properties of the spending account.', 'Required': False}]}
## Get a list of spending accounts
### `GET` `v1/buyers/{buyerID}/spendingaccounts`

| Parameters      | Description                    |
|------------------|---------------------------------|
| Name            | buyerID                        |
| Type            | string                         |
| Description     | ID of the buyer.               |
| Required        | True                           |
| Name            | search                         |
| Type            | string                         |
| Description     | Word or phrase to search for.  |
| Required        | False                          |
| Name            | searchOn                       |
| Type            | string                         |
| Description     | Comma-delimited list of fields to search on. |
| Required        | False                          |
| Name            | sortBy                         |
| Type            | string                         |
| Description     | Comma-delimited list of fields to sort by. |
| Required        | False                          |
| Name            | page                           |
| Type            | integer                        |
| Description     | Page of results to return. Default: 1 |
| Required        | False                          |
| Name            | pageSize                       |
| Type            | integer                        |
| Description     | Number of results to return per page. Default: 20, max: 100. |
| Required        | False                          |
| Name            | filters                        |
| Type            | object                         |
| Description     | Any additional key/value pairs passed in the query string are interpretted as filters. Valid keys are top-level properties of the returned model or 'xp.???' |
| Required        | False                          |

 **Requestbody**: 
None
 **Responsestatus**: `200`

 **Responsebody**: 
{'Sample': '{\r\n  "Meta": {\r\n    "Page": 1,\r\n    "PageSize": 20,\r\n    "TotalCount": 25,\r\n    "TotalPages": 2,\r\n    "ItemRange": [\r\n      1,\r\n      20\r\n    ]\r\n  },\r\n  "Items": [\r\n    {\r\n      "ID": "",\r\n      "Name": "",\r\n      "Balance": 0,\r\n      "AllowAsPaymentMethod": false,\r\n      "RedemptionCode": "",\r\n      "StartDate": "2018-03-21T23:00:00+00:00",\r\n      "EndDate": "2018-03-21T23:00:00+00:00",\r\n      "xp": {}\r\n    }\r\n  ]\r\n}', 'Fields': [{'Name': 'ID', 'Type': 'string', 'Description': 'ID of the spending account.', 'Required': False}, {'Name': 'Name', 'Type': 'string', 'Description': 'Name of the spending account.', 'Required': True}, {'Name': 'Balance', 'Type': 'float', 'Description': 'Balance of the spending account.', 'Required': True}, {'Name': 'AllowAsPaymentMethod', 'Type': 'boolean', 'Description': 'Allow as payment method of the spending account.', 'Required': False}, {'Name': 'RedemptionCode', 'Type': 'string', 'Description': 'If specified, matching code must be provided on redemption in order for the transaction to be successful. Most commonly used to implement Gift Cards.', 'Required': False}, {'Name': 'StartDate', 'Type': 'date', 'Description': 'Start date of the spending account.', 'Required': False}, {'Name': 'EndDate', 'Type': 'date', 'Description': 'End date of the spending account.', 'Required': False}, {'Name': 'xp', 'Type': 'object', 'Description': 'Container for extended (custom) properties of the spending account.', 'Required': False}]}
## Create a new spending account
### `POST` `v1/buyers/{buyerID}/spendingaccounts`

| Parameters      | Description                    |
|------------------|---------------------------------|
| Name            | buyerID                        |
| Type            | string                         |
| Description     | ID of the buyer.               |
| Required        | True                           |

 **Requestbody**: 
{'Sample': '{\r\n  "ID": "",\r\n  "Name": "",\r\n  "Balance": 0,\r\n  "AllowAsPaymentMethod": false,\r\n  "RedemptionCode": "",\r\n  "StartDate": "2018-03-21T23:00:00+00:00",\r\n  "EndDate": "2018-03-21T23:00:00+00:00",\r\n  "xp": {}\r\n}', 'Fields': [{'Name': 'ID', 'Type': 'string', 'Description': 'ID of the spending account. Can only contain characters Aa-Zz, 0-9, -, and _. Searchable: priority level 1. Sortable: priority level 2.', 'Required': False}, {'Name': 'Name', 'Type': 'string', 'Description': 'Name of the spending account. Required. Max length 100 characters. Searchable: priority level 2. Sortable: priority level 1.', 'Required': True}, {'Name': 'Balance', 'Type': 'float', 'Description': 'Balance of the spending account. Required.', 'Required': True}, {'Name': 'AllowAsPaymentMethod', 'Type': 'boolean', 'Description': 'Allow as payment method of the spending account.', 'Required': False}, {'Name': 'RedemptionCode', 'Type': 'string', 'Description': 'If specified, matching code must be provided on redemption in order for the transaction to be successful. Most commonly used to implement Gift Cards.', 'Required': False}, {'Name': 'StartDate', 'Type': 'date', 'Description': 'Start date of the spending account.', 'Required': False}, {'Name': 'EndDate', 'Type': 'date', 'Description': 'End date of the spending account.', 'Required': False}, {'Name': 'xp', 'Type': 'object', 'Description': 'Container for extended (custom) properties of the spending account.', 'Required': False}]}
 **Responsestatus**: `201`

 **Responsebody**: 
{'Sample': '{\r\n  "ID": "",\r\n  "Name": "",\r\n  "Balance": 0,\r\n  "AllowAsPaymentMethod": false,\r\n  "RedemptionCode": "",\r\n  "StartDate": "2018-03-21T23:00:00+00:00",\r\n  "EndDate": "2018-03-21T23:00:00+00:00",\r\n  "xp": {}\r\n}', 'Fields': [{'Name': 'ID', 'Type': 'string', 'Description': 'ID of the spending account.', 'Required': False}, {'Name': 'Name', 'Type': 'string', 'Description': 'Name of the spending account.', 'Required': True}, {'Name': 'Balance', 'Type': 'float', 'Description': 'Balance of the spending account.', 'Required': True}, {'Name': 'AllowAsPaymentMethod', 'Type': 'boolean', 'Description': 'Allow as payment method of the spending account.', 'Required': False}, {'Name': 'RedemptionCode', 'Type': 'string', 'Description': 'If specified, matching code must be provided on redemption in order for the transaction to be successful. Most commonly used to implement Gift Cards.', 'Required': False}, {'Name': 'StartDate', 'Type': 'date', 'Description': 'Start date of the spending account.', 'Required': False}, {'Name': 'EndDate', 'Type': 'date', 'Description': 'End date of the spending account.', 'Required': False}, {'Name': 'xp', 'Type': 'object', 'Description': 'Container for extended (custom) properties of the spending account.', 'Required': False}]}
## Create or update a spending account
### `PUT` `v1/buyers/{buyerID}/spendingaccounts/{spendingAccountID}`

| Parameters      | Description                    |
|------------------|---------------------------------|
| Name            | buyerID                        |
| Type            | string                         |
| Description     | ID of the buyer.               |
| Required        | True                           |
| Name            | spendingAccountID              |
| Type            | string                         |
| Description     | ID of the spending account.    |
| Required        | True                           |

 **Requestbody**: 
{'Sample': '{\r\n  "ID": "",\r\n  "Name": "",\r\n  "Balance": 0,\r\n  "AllowAsPaymentMethod": false,\r\n  "RedemptionCode": "",\r\n  "StartDate": "2018-03-21T23:00:00+00:00",\r\n  "EndDate": "2018-03-21T23:00:00+00:00",\r\n  "xp": {}\r\n}', 'Fields': [{'Name': 'ID', 'Type': 'string', 'Description': 'ID of the spending account. Can only contain characters Aa-Zz, 0-9, -, and _. Searchable: priority level 1. Sortable: priority level 2.', 'Required': False}, {'Name': 'Name', 'Type': 'string', 'Description': 'Name of the spending account. Required. Max length 100 characters. Searchable: priority level 2. Sortable: priority level 1.', 'Required': True}, {'Name': 'Balance', 'Type': 'float', 'Description': 'Balance of the spending account. Required.', 'Required': True}, {'Name': 'AllowAsPaymentMethod', 'Type': 'boolean', 'Description': 'Allow as payment method of the spending account.', 'Required': False}, {'Name': 'RedemptionCode', 'Type': 'string', 'Description': 'If specified, matching code must be provided on redemption in order for the transaction to be successful. Most commonly used to implement Gift Cards.', 'Required': False}, {'Name': 'StartDate', 'Type': 'date', 'Description': 'Start date of the spending account.', 'Required': False}, {'Name': 'EndDate', 'Type': 'date', 'Description': 'End date of the spending account.', 'Required': False}, {'Name': 'xp', 'Type': 'object', 'Description': 'Container for extended (custom) properties of the spending account.', 'Required': False}]}
 **Responsestatus**: `200`

 **Responsebody**: 
{'Sample': '{\r\n  "ID": "",\r\n  "Name": "",\r\n  "Balance": 0,\r\n  "AllowAsPaymentMethod": false,\r\n  "RedemptionCode": "",\r\n  "StartDate": "2018-03-21T23:00:00+00:00",\r\n  "EndDate": "2018-03-21T23:00:00+00:00",\r\n  "xp": {}\r\n}', 'Fields': [{'Name': 'ID', 'Type': 'string', 'Description': 'ID of the spending account.', 'Required': False}, {'Name': 'Name', 'Type': 'string', 'Description': 'Name of the spending account.', 'Required': True}, {'Name': 'Balance', 'Type': 'float', 'Description': 'Balance of the spending account.', 'Required': True}, {'Name': 'AllowAsPaymentMethod', 'Type': 'boolean', 'Description': 'Allow as payment method of the spending account.', 'Required': False}, {'Name': 'RedemptionCode', 'Type': 'string', 'Description': 'If specified, matching code must be provided on redemption in order for the transaction to be successful. Most commonly used to implement Gift Cards.', 'Required': False}, {'Name': 'StartDate', 'Type': 'date', 'Description': 'Start date of the spending account.', 'Required': False}, {'Name': 'EndDate', 'Type': 'date', 'Description': 'End date of the spending account.', 'Required': False}, {'Name': 'xp', 'Type': 'object', 'Description': 'Container for extended (custom) properties of the spending account.', 'Required': False}]}
## Delete a spending account
### `DELETE` `v1/buyers/{buyerID}/spendingaccounts/{spendingAccountID}`

| Parameters      | Description                    |
|------------------|---------------------------------|
| Name            | buyerID                        |
| Type            | string                         |
| Description     | ID of the buyer.               |
| Required        | True                           |
| Name            | spendingAccountID              |
| Type            | string                         |
| Description     | ID of the spending account.    |
| Required        | True                           |

 **Requestbody**: 
None
 **Responsestatus**: `204`

 **Responsebody**: 
None
## Partially update a spending account
### `PATCH` `v1/buyers/{buyerID}/spendingaccounts/{spendingAccountID}`

| Parameters      | Description                    |
|------------------|---------------------------------|
| Name            | buyerID                        |
| Type            | string                         |
| Description     | ID of the buyer.               |
| Required        | True                           |
| Name            | spendingAccountID              |
| Type            | string                         |
| Description     | ID of the spending account.    |
| Required        | True                           |

 **Requestbody**: 
{'Sample': '{\r\n  "ID": "",\r\n  "Name": "",\r\n  "Balance": 0,\r\n  "AllowAsPaymentMethod": false,\r\n  "RedemptionCode": "",\r\n  "StartDate": "2018-03-21T23:00:00+00:00",\r\n  "EndDate": "2018-03-21T23:00:00+00:00",\r\n  "xp": {}\r\n}', 'Fields': [{'Name': 'ID', 'Type': 'string', 'Description': 'ID of the spending account. Can only contain characters Aa-Zz, 0-9, -, and _. Searchable: priority level 1. Sortable: priority level 2.', 'Required': False}, {'Name': 'Name', 'Type': 'string', 'Description': 'Name of the spending account. Required. Max length 100 characters. Searchable: priority level 2. Sortable: priority level 1.', 'Required': True}, {'Name': 'Balance', 'Type': 'float', 'Description': 'Balance of the spending account. Required.', 'Required': True}, {'Name': 'AllowAsPaymentMethod', 'Type': 'boolean', 'Description': 'Allow as payment method of the spending account.', 'Required': False}, {'Name': 'RedemptionCode', 'Type': 'string', 'Description': 'If specified, matching code must be provided on redemption in order for the transaction to be successful. Most commonly used to implement Gift Cards.', 'Required': False}, {'Name': 'StartDate', 'Type': 'date', 'Description': 'Start date of the spending account.', 'Required': False}, {'Name': 'EndDate', 'Type': 'date', 'Description': 'End date of the spending account.', 'Required': False}, {'Name': 'xp', 'Type': 'object', 'Description': 'Container for extended (custom) properties of the spending account.', 'Required': False}]}
 **Responsestatus**: `200`

 **Responsebody**: 
{'Sample': '{\r\n  "ID": "",\r\n  "Name": "",\r\n  "Balance": 0,\r\n  "AllowAsPaymentMethod": false,\r\n  "RedemptionCode": "",\r\n  "StartDate": "2018-03-21T23:00:00+00:00",\r\n  "EndDate": "2018-03-21T23:00:00+00:00",\r\n  "xp": {}\r\n}', 'Fields': [{'Name': 'ID', 'Type': 'string', 'Description': 'ID of the spending account.', 'Required': False}, {'Name': 'Name', 'Type': 'string', 'Description': 'Name of the spending account.', 'Required': True}, {'Name': 'Balance', 'Type': 'float', 'Description': 'Balance of the spending account.', 'Required': True}, {'Name': 'AllowAsPaymentMethod', 'Type': 'boolean', 'Description': 'Allow as payment method of the spending account.', 'Required': False}, {'Name': 'RedemptionCode', 'Type': 'string', 'Description': 'If specified, matching code must be provided on redemption in order for the transaction to be successful. Most commonly used to implement Gift Cards.', 'Required': False}, {'Name': 'StartDate', 'Type': 'date', 'Description': 'Start date of the spending account.', 'Required': False}, {'Name': 'EndDate', 'Type': 'date', 'Description': 'End date of the spending account.', 'Required': False}, {'Name': 'xp', 'Type': 'object', 'Description': 'Container for extended (custom) properties of the spending account.', 'Required': False}]}
## Get a list of spending account assignments
### `GET` `v1/buyers/{buyerID}/spendingaccounts/assignments`

| Parameters      | Description                    |
|------------------|---------------------------------|
| Name            | buyerID                        |
| Type            | string                         |
| Description     | ID of the buyer.               |
| Required        | True                           |
| Name            | spendingAccountID              |
| Type            | string                         |
| Description     | ID of the spending account.    |
| Required        | False                          |
| Name            | userID                         |
| Type            | string                         |
| Description     | ID of the user.                |
| Required        | False                          |
| Name            | userGroupID                    |
| Type            | string                         |
| Description     | ID of the user group.          |
| Required        | False                          |
| Name            | level                          |
| Type            | string                         |
| Description     | Level of the spending account assignment. Possible values: User, Group, Company. |
| Required        | False                          |
| Name            | page                           |
| Type            | integer                        |
| Description     | Page of results to return. Default: 1 |
| Required        | False                          |
| Name            | pageSize                       |
| Type            | integer                        |
| Description     | Number of results to return per page. Default: 20, max: 100. |
| Required        | False                          |

 **Requestbody**: 
None
 **Responsestatus**: `200`

 **Responsebody**: 
{'Sample': '{\r\n  "Meta": {\r\n    "Page": 1,\r\n    "PageSize": 20,\r\n    "TotalCount": 25,\r\n    "TotalPages": 2,\r\n    "ItemRange": [\r\n      1,\r\n      20\r\n    ]\r\n  },\r\n  "Items": [\r\n    {\r\n      "SpendingAccountID": "",\r\n      "UserID": "",\r\n      "UserGroupID": "",\r\n      "AllowExceed": false\r\n    }\r\n  ]\r\n}', 'Fields': [{'Name': 'SpendingAccountID', 'Type': 'string', 'Description': 'ID of the spending account.', 'Required': True}, {'Name': 'UserID', 'Type': 'string', 'Description': 'ID of the user.', 'Required': False}, {'Name': 'UserGroupID', 'Type': 'string', 'Description': 'ID of the user group.', 'Required': False}, {'Name': 'AllowExceed', 'Type': 'boolean', 'Description': 'Allow exceed of the spending account assignment.', 'Required': False}]}
## Save a spending account assignment
### `POST` `v1/buyers/{buyerID}/spendingaccounts/assignments`

| Parameters      | Description                    |
|------------------|---------------------------------|
| Name            | buyerID                        |
| Type            | string                         |
| Description     | ID of the buyer.               |
| Required        | True                           |

 **Requestbody**: 
{'Sample': '{\r\n  "SpendingAccountID": "",\r\n  "UserID": "",\r\n  "UserGroupID": "",\r\n  "AllowExceed": false\r\n}', 'Fields': [{'Name': 'SpendingAccountID', 'Type': 'string', 'Description': 'ID of the spending account. Required. Sortable: priority level 1.', 'Required': True}, {'Name': 'UserID', 'Type': 'string', 'Description': 'ID of the user. Sortable: priority level 2.', 'Required': False}, {'Name': 'UserGroupID', 'Type': 'string', 'Description': 'ID of the user group. Sortable: priority level 3.', 'Required': False}, {'Name': 'AllowExceed', 'Type': 'boolean', 'Description': 'Allow exceed of the spending account assignment.', 'Required': False}]}
 **Responsestatus**: `204`

 **Responsebody**: 
None
## Delete a spending account assignment
### `DELETE` `v1/buyers/{buyerID}/spendingaccounts/{spendingAccountID}/assignments`

| Parameters      | Description                    |
|------------------|---------------------------------|
| Name            | buyerID                        |
| Type            | string                         |
| Description     | ID of the buyer.               |
| Required        | True                           |
| Name            | spendingAccountID              |
| Type            | string                         |
| Description     | ID of the spending account.    |
| Required        | True                           |
| Name            | userID                         |
| Type            | string                         |
| Description     | ID of the user.                |
| Required        | False                          |
| Name            | userGroupID                    |
| Type            | string                         |
| Description     | ID of the user group.          |
| Required        | False                          |

 **Requestbody**: 
None
 **Responsestatus**: `204`

 **Responsebody**: 
None