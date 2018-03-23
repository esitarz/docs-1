---
title: Spending Accounts
date: 2018-03-23
category: API Reference
tags: Me And My Stuff
slug: MeSpendingAccounts
---
"Me" is a container for read-only endpoints that return a filtered view
of things that the current buyer user is allowed to see, i.e. things
that they are assigned to either directly or as a member of a buyer
organization or user group. It also provides ways for a user to update
or change their own information.

---
## Get a list of spending accounts visible to this user
### `GET` `v1/me/spendingAccounts`

| Parameters      | Description                    |
|------------------|---------------------------------|
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
{'Sample': '{\r\n  "Meta": {\r\n    "Page": 1,\r\n    "PageSize": 20,\r\n    "TotalCount": 25,\r\n    "TotalPages": 2,\r\n    "ItemRange": [\r\n      1,\r\n      20\r\n    ]\r\n  },\r\n  "Items": [\r\n    {\r\n      "ID": "",\r\n      "Name": "",\r\n      "Balance": 0,\r\n      "AllowAsPaymentMethod": false,\r\n      "RedemptionCode": "",\r\n      "StartDate": "2018-03-21T23:00:00+00:00",\r\n      "EndDate": "2018-03-21T23:00:00+00:00",\r\n      "xp": {}\r\n    }\r\n  ]\r\n}', 'Fields': [{'Name': 'ID', 'Type': 'string', 'Description': 'ID of the spending account.', 'Required': False}, {'Name': 'Name', 'Type': 'string', 'Description': 'Name of the spending account.', 'Required': True}, {'Name': 'Balance', 'Type': 'float', 'Description': 'Balance of the spending account.', 'Required': True}, {'Name': 'AllowAsPaymentMethod', 'Type': 'boolean', 'Description': 'Allow as payment method of the spending account.', 'Required': False}, {'Name': 'RedemptionCode', 'Type': 'string', 'Description': 'If specified, matching code must be provided on redemption in order for the transaction to be successful. Most commonly used to implement Gift Cards.', 'Required': False}, {'Name': 'StartDate', 'Type': 'date', 'Description': 'Start date of the spending account.', 'Required': False}, {'Name': 'EndDate', 'Type': 'date', 'Description': 'End date of the spending account.', 'Required': False}, {'Name': 'xp', 'Type': 'object', 'Description': 'Container for extended (custom) properties of the spending account.', 'Required': False}]}## Get a single spending account
### `GET` `v1/me/spendingaccounts/{spendingAccountID}`

| Parameters      | Description                    |
|------------------|---------------------------------|
| Name            | spendingAccountID              |
| Type            | string                         |
| Description     | ID of the spending account.    |
| Required        | True                           |

 **Requestbody**: 
None
 **Responsestatus**: `200`

 **Responsebody**: 
{'Sample': '{\r\n  "ID": "",\r\n  "Name": "",\r\n  "Balance": 0,\r\n  "AllowAsPaymentMethod": false,\r\n  "RedemptionCode": "",\r\n  "StartDate": "2018-03-21T23:00:00+00:00",\r\n  "EndDate": "2018-03-21T23:00:00+00:00",\r\n  "xp": {}\r\n}', 'Fields': [{'Name': 'ID', 'Type': 'string', 'Description': 'ID of the spending account.', 'Required': False}, {'Name': 'Name', 'Type': 'string', 'Description': 'Name of the spending account.', 'Required': True}, {'Name': 'Balance', 'Type': 'float', 'Description': 'Balance of the spending account.', 'Required': True}, {'Name': 'AllowAsPaymentMethod', 'Type': 'boolean', 'Description': 'Allow as payment method of the spending account.', 'Required': False}, {'Name': 'RedemptionCode', 'Type': 'string', 'Description': 'If specified, matching code must be provided on redemption in order for the transaction to be successful. Most commonly used to implement Gift Cards.', 'Required': False}, {'Name': 'StartDate', 'Type': 'date', 'Description': 'Start date of the spending account.', 'Required': False}, {'Name': 'EndDate', 'Type': 'date', 'Description': 'End date of the spending account.', 'Required': False}, {'Name': 'xp', 'Type': 'object', 'Description': 'Container for extended (custom) properties of the spending account.', 'Required': False}]}