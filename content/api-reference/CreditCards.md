---
title: Credit Cards
date: 2018-03-23
category: API Reference
tags: Buyers
slug: CreditCards
---
Credit cards are used as a payment method for an order. A user may have
access to one or many credit cards for personal spend or group spending.
Credit Cards may be saved and assigned to members of an organization for
use during purchase.

---
## Get a single credit card
### `GET` `v1/buyers/{buyerID}/creditcards/{creditCardID}`

| Parameters      | Description                    |
|------------------|---------------------------------|
| Name            | buyerID                        |
| Type            | string                         |
| Description     | ID of the buyer.               |
| Required        | True                           |
| Name            | creditCardID                   |
| Type            | string                         |
| Description     | ID of the credit card.         |
| Required        | True                           |

 **Requestbody**: 
None
 **Responsestatus**: `200`

 **Responsebody**: 
{'Sample': '{\r\n  "ID": "",\r\n  "Token": "",\r\n  "DateCreated": "2018-03-21T23:00:00+00:00",\r\n  "CardType": "",\r\n  "PartialAccountNumber": "",\r\n  "CardholderName": "",\r\n  "ExpirationDate": "2018-03-21T23:00:00+00:00",\r\n  "xp": {}\r\n}', 'Fields': [{'Name': 'ID', 'Type': 'string', 'Description': 'ID of the credit card.', 'Required': False}, {'Name': 'Token', 'Type': 'string', 'Description': 'Token of the credit card.', 'Required': False}, {'Name': 'DateCreated', 'Type': 'date', 'Description': 'Date created of the credit card.', 'Required': False}, {'Name': 'CardType', 'Type': 'string', 'Description': 'Card type of the credit card.', 'Required': False}, {'Name': 'PartialAccountNumber', 'Type': 'string', 'Description': 'Partial account number of the credit card.', 'Required': False}, {'Name': 'CardholderName', 'Type': 'string', 'Description': 'Cardholder name of the credit card.', 'Required': False}, {'Name': 'ExpirationDate', 'Type': 'date', 'Description': 'Expiration date of the credit card.', 'Required': False}, {'Name': 'xp', 'Type': 'object', 'Description': 'Container for extended (custom) properties of the credit card.', 'Required': False}]}## Get a list of credit cards
### `GET` `v1/buyers/{buyerID}/creditcards`

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
{'Sample': '{\r\n  "Meta": {\r\n    "Page": 1,\r\n    "PageSize": 20,\r\n    "TotalCount": 25,\r\n    "TotalPages": 2,\r\n    "ItemRange": [\r\n      1,\r\n      20\r\n    ]\r\n  },\r\n  "Items": [\r\n    {\r\n      "ID": "",\r\n      "Token": "",\r\n      "DateCreated": "2018-03-21T23:00:00+00:00",\r\n      "CardType": "",\r\n      "PartialAccountNumber": "",\r\n      "CardholderName": "",\r\n      "ExpirationDate": "2018-03-21T23:00:00+00:00",\r\n      "xp": {}\r\n    }\r\n  ]\r\n}', 'Fields': [{'Name': 'ID', 'Type': 'string', 'Description': 'ID of the credit card.', 'Required': False}, {'Name': 'Token', 'Type': 'string', 'Description': 'Token of the credit card.', 'Required': False}, {'Name': 'DateCreated', 'Type': 'date', 'Description': 'Date created of the credit card.', 'Required': False}, {'Name': 'CardType', 'Type': 'string', 'Description': 'Card type of the credit card.', 'Required': False}, {'Name': 'PartialAccountNumber', 'Type': 'string', 'Description': 'Partial account number of the credit card.', 'Required': False}, {'Name': 'CardholderName', 'Type': 'string', 'Description': 'Cardholder name of the credit card.', 'Required': False}, {'Name': 'ExpirationDate', 'Type': 'date', 'Description': 'Expiration date of the credit card.', 'Required': False}, {'Name': 'xp', 'Type': 'object', 'Description': 'Container for extended (custom) properties of the credit card.', 'Required': False}]}## Create a new credit card
### `POST` `v1/buyers/{buyerID}/creditcards`

| Parameters      | Description                    |
|------------------|---------------------------------|
| Name            | buyerID                        |
| Type            | string                         |
| Description     | ID of the buyer.               |
| Required        | True                           |

 **Requestbody**: 
{'Sample': '{\r\n  "ID": "",\r\n  "Token": "",\r\n  "CardType": "",\r\n  "PartialAccountNumber": "",\r\n  "CardholderName": "",\r\n  "ExpirationDate": "2018-03-21T23:00:00+00:00",\r\n  "xp": {}\r\n}', 'Fields': [{'Name': 'ID', 'Type': 'string', 'Description': 'ID of the credit card. Can only contain characters Aa-Zz, 0-9, -, and _. Searchable: priority level 1. Sortable: priority level 1.', 'Required': False}, {'Name': 'Token', 'Type': 'string', 'Description': 'Token of the credit card.', 'Required': False}, {'Name': 'CardType', 'Type': 'string', 'Description': 'Card type of the credit card. Searchable: priority level 3. Sortable: priority level 3.', 'Required': False}, {'Name': 'PartialAccountNumber', 'Type': 'string', 'Description': 'Partial account number of the credit card. Max length 5 characters.', 'Required': False}, {'Name': 'CardholderName', 'Type': 'string', 'Description': 'Cardholder name of the credit card. Searchable: priority level 2. Sortable: priority level 2.', 'Required': False}, {'Name': 'ExpirationDate', 'Type': 'date', 'Description': 'Expiration date of the credit card. Searchable: priority level 4. Sortable: priority level 4.', 'Required': False}, {'Name': 'xp', 'Type': 'object', 'Description': 'Container for extended (custom) properties of the credit card.', 'Required': False}]}
 **Responsestatus**: `201`

 **Responsebody**: 
{'Sample': '{\r\n  "ID": "",\r\n  "Token": "",\r\n  "DateCreated": "2018-03-21T23:00:00+00:00",\r\n  "CardType": "",\r\n  "PartialAccountNumber": "",\r\n  "CardholderName": "",\r\n  "ExpirationDate": "2018-03-21T23:00:00+00:00",\r\n  "xp": {}\r\n}', 'Fields': [{'Name': 'ID', 'Type': 'string', 'Description': 'ID of the credit card.', 'Required': False}, {'Name': 'Token', 'Type': 'string', 'Description': 'Token of the credit card.', 'Required': False}, {'Name': 'DateCreated', 'Type': 'date', 'Description': 'Date created of the credit card.', 'Required': False}, {'Name': 'CardType', 'Type': 'string', 'Description': 'Card type of the credit card.', 'Required': False}, {'Name': 'PartialAccountNumber', 'Type': 'string', 'Description': 'Partial account number of the credit card.', 'Required': False}, {'Name': 'CardholderName', 'Type': 'string', 'Description': 'Cardholder name of the credit card.', 'Required': False}, {'Name': 'ExpirationDate', 'Type': 'date', 'Description': 'Expiration date of the credit card.', 'Required': False}, {'Name': 'xp', 'Type': 'object', 'Description': 'Container for extended (custom) properties of the credit card.', 'Required': False}]}## Create or update a credit card
### `PUT` `v1/buyers/{buyerID}/creditcards/{creditCardID}`

| Parameters      | Description                    |
|------------------|---------------------------------|
| Name            | buyerID                        |
| Type            | string                         |
| Description     | ID of the buyer.               |
| Required        | True                           |
| Name            | creditCardID                   |
| Type            | string                         |
| Description     | ID of the credit card.         |
| Required        | True                           |

 **Requestbody**: 
{'Sample': '{\r\n  "ID": "",\r\n  "Token": "",\r\n  "CardType": "",\r\n  "PartialAccountNumber": "",\r\n  "CardholderName": "",\r\n  "ExpirationDate": "2018-03-21T23:00:00+00:00",\r\n  "xp": {}\r\n}', 'Fields': [{'Name': 'ID', 'Type': 'string', 'Description': 'ID of the credit card. Can only contain characters Aa-Zz, 0-9, -, and _. Searchable: priority level 1. Sortable: priority level 1.', 'Required': False}, {'Name': 'Token', 'Type': 'string', 'Description': 'Token of the credit card.', 'Required': False}, {'Name': 'CardType', 'Type': 'string', 'Description': 'Card type of the credit card. Searchable: priority level 3. Sortable: priority level 3.', 'Required': False}, {'Name': 'PartialAccountNumber', 'Type': 'string', 'Description': 'Partial account number of the credit card. Max length 5 characters.', 'Required': False}, {'Name': 'CardholderName', 'Type': 'string', 'Description': 'Cardholder name of the credit card. Searchable: priority level 2. Sortable: priority level 2.', 'Required': False}, {'Name': 'ExpirationDate', 'Type': 'date', 'Description': 'Expiration date of the credit card. Searchable: priority level 4. Sortable: priority level 4.', 'Required': False}, {'Name': 'xp', 'Type': 'object', 'Description': 'Container for extended (custom) properties of the credit card.', 'Required': False}]}
 **Responsestatus**: `200`

 **Responsebody**: 
{'Sample': '{\r\n  "ID": "",\r\n  "Token": "",\r\n  "DateCreated": "2018-03-21T23:00:00+00:00",\r\n  "CardType": "",\r\n  "PartialAccountNumber": "",\r\n  "CardholderName": "",\r\n  "ExpirationDate": "2018-03-21T23:00:00+00:00",\r\n  "xp": {}\r\n}', 'Fields': [{'Name': 'ID', 'Type': 'string', 'Description': 'ID of the credit card.', 'Required': False}, {'Name': 'Token', 'Type': 'string', 'Description': 'Token of the credit card.', 'Required': False}, {'Name': 'DateCreated', 'Type': 'date', 'Description': 'Date created of the credit card.', 'Required': False}, {'Name': 'CardType', 'Type': 'string', 'Description': 'Card type of the credit card.', 'Required': False}, {'Name': 'PartialAccountNumber', 'Type': 'string', 'Description': 'Partial account number of the credit card.', 'Required': False}, {'Name': 'CardholderName', 'Type': 'string', 'Description': 'Cardholder name of the credit card.', 'Required': False}, {'Name': 'ExpirationDate', 'Type': 'date', 'Description': 'Expiration date of the credit card.', 'Required': False}, {'Name': 'xp', 'Type': 'object', 'Description': 'Container for extended (custom) properties of the credit card.', 'Required': False}]}## Delete a credit card
### `DELETE` `v1/buyers/{buyerID}/creditcards/{creditCardID}`

| Parameters      | Description                    |
|------------------|---------------------------------|
| Name            | buyerID                        |
| Type            | string                         |
| Description     | ID of the buyer.               |
| Required        | True                           |
| Name            | creditCardID                   |
| Type            | string                         |
| Description     | ID of the credit card.         |
| Required        | True                           |

 **Requestbody**: 
None
 **Responsestatus**: `204`

 **Responsebody**: 
None## Partially update a credit card
### `PATCH` `v1/buyers/{buyerID}/creditcards/{creditCardID}`

| Parameters      | Description                    |
|------------------|---------------------------------|
| Name            | buyerID                        |
| Type            | string                         |
| Description     | ID of the buyer.               |
| Required        | True                           |
| Name            | creditCardID                   |
| Type            | string                         |
| Description     | ID of the credit card.         |
| Required        | True                           |

 **Requestbody**: 
{'Sample': '{\r\n  "ID": "",\r\n  "Token": "",\r\n  "CardType": "",\r\n  "PartialAccountNumber": "",\r\n  "CardholderName": "",\r\n  "ExpirationDate": "2018-03-21T23:00:00+00:00",\r\n  "xp": {}\r\n}', 'Fields': [{'Name': 'ID', 'Type': 'string', 'Description': 'ID of the credit card. Can only contain characters Aa-Zz, 0-9, -, and _. Searchable: priority level 1. Sortable: priority level 1.', 'Required': False}, {'Name': 'Token', 'Type': 'string', 'Description': 'Token of the credit card.', 'Required': False}, {'Name': 'CardType', 'Type': 'string', 'Description': 'Card type of the credit card. Searchable: priority level 3. Sortable: priority level 3.', 'Required': False}, {'Name': 'PartialAccountNumber', 'Type': 'string', 'Description': 'Partial account number of the credit card. Max length 5 characters.', 'Required': False}, {'Name': 'CardholderName', 'Type': 'string', 'Description': 'Cardholder name of the credit card. Searchable: priority level 2. Sortable: priority level 2.', 'Required': False}, {'Name': 'ExpirationDate', 'Type': 'date', 'Description': 'Expiration date of the credit card. Searchable: priority level 4. Sortable: priority level 4.', 'Required': False}, {'Name': 'xp', 'Type': 'object', 'Description': 'Container for extended (custom) properties of the credit card.', 'Required': False}]}
 **Responsestatus**: `200`

 **Responsebody**: 
{'Sample': '{\r\n  "ID": "",\r\n  "Token": "",\r\n  "DateCreated": "2018-03-21T23:00:00+00:00",\r\n  "CardType": "",\r\n  "PartialAccountNumber": "",\r\n  "CardholderName": "",\r\n  "ExpirationDate": "2018-03-21T23:00:00+00:00",\r\n  "xp": {}\r\n}', 'Fields': [{'Name': 'ID', 'Type': 'string', 'Description': 'ID of the credit card.', 'Required': False}, {'Name': 'Token', 'Type': 'string', 'Description': 'Token of the credit card.', 'Required': False}, {'Name': 'DateCreated', 'Type': 'date', 'Description': 'Date created of the credit card.', 'Required': False}, {'Name': 'CardType', 'Type': 'string', 'Description': 'Card type of the credit card.', 'Required': False}, {'Name': 'PartialAccountNumber', 'Type': 'string', 'Description': 'Partial account number of the credit card.', 'Required': False}, {'Name': 'CardholderName', 'Type': 'string', 'Description': 'Cardholder name of the credit card.', 'Required': False}, {'Name': 'ExpirationDate', 'Type': 'date', 'Description': 'Expiration date of the credit card.', 'Required': False}, {'Name': 'xp', 'Type': 'object', 'Description': 'Container for extended (custom) properties of the credit card.', 'Required': False}]}## Get a list of credit card assignments
### `GET` `v1/buyers/{buyerID}/creditcards/assignments`

| Parameters      | Description                    |
|------------------|---------------------------------|
| Name            | buyerID                        |
| Type            | string                         |
| Description     | ID of the buyer.               |
| Required        | True                           |
| Name            | creditCardID                   |
| Type            | string                         |
| Description     | ID of the credit card.         |
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
| Description     | Level of the credit card assignment. Possible values: User, Group, Company. |
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
{'Sample': '{\r\n  "Meta": {\r\n    "Page": 1,\r\n    "PageSize": 20,\r\n    "TotalCount": 25,\r\n    "TotalPages": 2,\r\n    "ItemRange": [\r\n      1,\r\n      20\r\n    ]\r\n  },\r\n  "Items": [\r\n    {\r\n      "CreditCardID": "",\r\n      "UserID": "",\r\n      "UserGroupID": ""\r\n    }\r\n  ]\r\n}', 'Fields': [{'Name': 'CreditCardID', 'Type': 'string', 'Description': 'ID of the credit card.', 'Required': True}, {'Name': 'UserID', 'Type': 'string', 'Description': 'ID of the user.', 'Required': False}, {'Name': 'UserGroupID', 'Type': 'string', 'Description': 'ID of the user group.', 'Required': False}]}## Save a credit card assignment
### `POST` `v1/buyers/{buyerID}/creditcards/assignments`

| Parameters      | Description                    |
|------------------|---------------------------------|
| Name            | buyerID                        |
| Type            | string                         |
| Description     | ID of the buyer.               |
| Required        | True                           |

 **Requestbody**: 
{'Sample': '{\r\n  "CreditCardID": "",\r\n  "UserID": "",\r\n  "UserGroupID": ""\r\n}', 'Fields': [{'Name': 'CreditCardID', 'Type': 'string', 'Description': 'ID of the credit card. Required. Sortable: priority level 1.', 'Required': True}, {'Name': 'UserID', 'Type': 'string', 'Description': 'ID of the user. Sortable: priority level 2.', 'Required': False}, {'Name': 'UserGroupID', 'Type': 'string', 'Description': 'ID of the user group. Sortable: priority level 3.', 'Required': False}]}
 **Responsestatus**: `204`

 **Responsebody**: 
None## Delete a credit card assignment
### `DELETE` `v1/buyers/{buyerID}/creditcards/{creditCardID}/assignments`

| Parameters      | Description                    |
|------------------|---------------------------------|
| Name            | buyerID                        |
| Type            | string                         |
| Description     | ID of the buyer.               |
| Required        | True                           |
| Name            | creditCardID                   |
| Type            | string                         |
| Description     | ID of the credit card.         |
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