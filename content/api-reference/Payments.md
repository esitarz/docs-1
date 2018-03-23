---
title: Payments
date: 2018-03-23
category: API Reference
tags: Orders And Fulfillment
slug: Payments
---

## Get a single payment
### `GET` `v1/orders/{direction}/{orderID}/payments/{paymentID}`

| Parameters      | Description                    |
|------------------|---------------------------------|
| Name            | direction                      |
| Type            | string                         |
| Description     | Direction of the order, from the current user's perspective. Possible values: incoming, outgoing. |
| Required        | True                           |
| Name            | orderID                        |
| Type            | string                         |
| Description     | ID of the order.               |
| Required        | True                           |
| Name            | paymentID                      |
| Type            | string                         |
| Description     | ID of the payment.             |
| Required        | True                           |

 **Requestbody**: 
None
 **Responsestatus**: `200`

 **Responsebody**: 
{'Sample': '{\r\n  "ID": "",\r\n  "Type": "PurchaseOrder",\r\n  "DateCreated": "2018-03-21T23:00:00+00:00",\r\n  "CreditCardID": "",\r\n  "SpendingAccountID": "",\r\n  "Description": "",\r\n  "Amount": 0,\r\n  "Accepted": false,\r\n  "xp": {},\r\n  "Transactions": [\r\n    {\r\n      "ID": "",\r\n      "Type": "",\r\n      "DateExecuted": "2018-03-21T23:00:00+00:00",\r\n      "Amount": 0,\r\n      "Succeeded": false,\r\n      "ResultCode": "",\r\n      "ResultMessage": "",\r\n      "xp": {}\r\n    }\r\n  ]\r\n}', 'Fields': [{'Name': 'ID', 'Type': 'string', 'Description': 'ID of the payment.', 'Required': False}, {'Name': 'Type', 'Type': 'string', 'Description': 'Type of the payment. Possible values: PurchaseOrder, CreditCard, SpendingAccount.', 'Required': False}, {'Name': 'DateCreated', 'Type': 'date', 'Description': 'Date created of the payment.', 'Required': False}, {'Name': 'CreditCardID', 'Type': 'string', 'Description': 'ID of the credit card.', 'Required': False}, {'Name': 'SpendingAccountID', 'Type': 'string', 'Description': 'ID of the spending account.', 'Required': False}, {'Name': 'Description', 'Type': 'string', 'Description': 'Description of the payment.', 'Required': False}, {'Name': 'Amount', 'Type': 'float', 'Description': 'If null, Payment applies to order total (or total of specific Line Items, if set), minus any other Payments where Amount is set.', 'Required': False}, {'Name': 'Accepted', 'Type': 'boolean', 'Description': 'Accepted of the payment.', 'Required': False}, {'Name': 'xp', 'Type': 'object', 'Description': 'Container for extended (custom) properties of the payment.', 'Required': False}, {'Name': 'Transactions', 'Type': 'array', 'Description': 'Transactions of the payment.', 'Required': False}]}## Get a list of payments
### `GET` `v1/orders/{direction}/{orderID}/payments`

| Parameters      | Description                    |
|------------------|---------------------------------|
| Name            | direction                      |
| Type            | string                         |
| Description     | Direction of the order, from the current user's perspective. Possible values: incoming, outgoing. |
| Required        | True                           |
| Name            | orderID                        |
| Type            | string                         |
| Description     | ID of the order.               |
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
{'Sample': '{\r\n  "Meta": {\r\n    "Page": 1,\r\n    "PageSize": 20,\r\n    "TotalCount": 25,\r\n    "TotalPages": 2,\r\n    "ItemRange": [\r\n      1,\r\n      20\r\n    ]\r\n  },\r\n  "Items": [\r\n    {\r\n      "ID": "",\r\n      "Type": "PurchaseOrder",\r\n      "DateCreated": "2018-03-21T23:00:00+00:00",\r\n      "CreditCardID": "",\r\n      "SpendingAccountID": "",\r\n      "Description": "",\r\n      "Amount": 0,\r\n      "Accepted": false,\r\n      "xp": {},\r\n      "Transactions": [\r\n        {\r\n          "ID": "",\r\n          "Type": "",\r\n          "DateExecuted": "2018-03-21T23:00:00+00:00",\r\n          "Amount": 0,\r\n          "Succeeded": false,\r\n          "ResultCode": "",\r\n          "ResultMessage": "",\r\n          "xp": {}\r\n        }\r\n      ]\r\n    }\r\n  ]\r\n}', 'Fields': [{'Name': 'ID', 'Type': 'string', 'Description': 'ID of the payment.', 'Required': False}, {'Name': 'Type', 'Type': 'string', 'Description': 'Type of the payment. Possible values: PurchaseOrder, CreditCard, SpendingAccount.', 'Required': False}, {'Name': 'DateCreated', 'Type': 'date', 'Description': 'Date created of the payment.', 'Required': False}, {'Name': 'CreditCardID', 'Type': 'string', 'Description': 'ID of the credit card.', 'Required': False}, {'Name': 'SpendingAccountID', 'Type': 'string', 'Description': 'ID of the spending account.', 'Required': False}, {'Name': 'Description', 'Type': 'string', 'Description': 'Description of the payment.', 'Required': False}, {'Name': 'Amount', 'Type': 'float', 'Description': 'If null, Payment applies to order total (or total of specific Line Items, if set), minus any other Payments where Amount is set.', 'Required': False}, {'Name': 'Accepted', 'Type': 'boolean', 'Description': 'Accepted of the payment.', 'Required': False}, {'Name': 'xp', 'Type': 'object', 'Description': 'Container for extended (custom) properties of the payment.', 'Required': False}, {'Name': 'Transactions', 'Type': 'array', 'Description': 'Transactions of the payment.', 'Required': False}]}## Create a new payment
### `POST` `v1/orders/{direction}/{orderID}/payments`

| Parameters      | Description                    |
|------------------|---------------------------------|
| Name            | direction                      |
| Type            | string                         |
| Description     | Direction of the order, from the current user's perspective. Possible values: incoming, outgoing. |
| Required        | True                           |
| Name            | orderID                        |
| Type            | string                         |
| Description     | ID of the order.               |
| Required        | True                           |

 **Requestbody**: 
{'Sample': '{\r\n  "ID": "",\r\n  "Type": "PurchaseOrder",\r\n  "CreditCardID": "",\r\n  "SpendingAccountID": "",\r\n  "Description": "",\r\n  "Amount": 0,\r\n  "Accepted": false,\r\n  "xp": {}\r\n}', 'Fields': [{'Name': 'ID', 'Type': 'string', 'Description': 'ID of the payment. Can only contain characters Aa-Zz, 0-9, -, and _. Searchable: priority level 1. Sortable.', 'Required': False}, {'Name': 'Type', 'Type': 'string', 'Description': 'Type of the payment. Sortable. Possible values: PurchaseOrder, CreditCard, SpendingAccount.', 'Required': False}, {'Name': 'CreditCardID', 'Type': 'string', 'Description': 'ID of the credit card. Sortable.', 'Required': False}, {'Name': 'SpendingAccountID', 'Type': 'string', 'Description': 'ID of the spending account. Sortable.', 'Required': False}, {'Name': 'Description', 'Type': 'string', 'Description': 'Description of the payment. Max length 2000 characters. Searchable: priority level 2.', 'Required': False}, {'Name': 'Amount', 'Type': 'float', 'Description': 'If null, Payment applies to order total (or total of specific Line Items, if set), minus any other Payments where Amount is set.', 'Required': False}, {'Name': 'Accepted', 'Type': 'boolean', 'Description': 'Accepted of the payment.', 'Required': False}, {'Name': 'xp', 'Type': 'object', 'Description': 'Container for extended (custom) properties of the payment.', 'Required': False}]}
 **Responsestatus**: `201`

 **Responsebody**: 
{'Sample': '{\r\n  "ID": "",\r\n  "Type": "PurchaseOrder",\r\n  "DateCreated": "2018-03-21T23:00:00+00:00",\r\n  "CreditCardID": "",\r\n  "SpendingAccountID": "",\r\n  "Description": "",\r\n  "Amount": 0,\r\n  "Accepted": false,\r\n  "xp": {},\r\n  "Transactions": [\r\n    {\r\n      "ID": "",\r\n      "Type": "",\r\n      "DateExecuted": "2018-03-21T23:00:00+00:00",\r\n      "Amount": 0,\r\n      "Succeeded": false,\r\n      "ResultCode": "",\r\n      "ResultMessage": "",\r\n      "xp": {}\r\n    }\r\n  ]\r\n}', 'Fields': [{'Name': 'ID', 'Type': 'string', 'Description': 'ID of the payment.', 'Required': False}, {'Name': 'Type', 'Type': 'string', 'Description': 'Type of the payment. Possible values: PurchaseOrder, CreditCard, SpendingAccount.', 'Required': False}, {'Name': 'DateCreated', 'Type': 'date', 'Description': 'Date created of the payment.', 'Required': False}, {'Name': 'CreditCardID', 'Type': 'string', 'Description': 'ID of the credit card.', 'Required': False}, {'Name': 'SpendingAccountID', 'Type': 'string', 'Description': 'ID of the spending account.', 'Required': False}, {'Name': 'Description', 'Type': 'string', 'Description': 'Description of the payment.', 'Required': False}, {'Name': 'Amount', 'Type': 'float', 'Description': 'If null, Payment applies to order total (or total of specific Line Items, if set), minus any other Payments where Amount is set.', 'Required': False}, {'Name': 'Accepted', 'Type': 'boolean', 'Description': 'Accepted of the payment.', 'Required': False}, {'Name': 'xp', 'Type': 'object', 'Description': 'Container for extended (custom) properties of the payment.', 'Required': False}, {'Name': 'Transactions', 'Type': 'array', 'Description': 'Transactions of the payment.', 'Required': False}]}## Delete a payment
### `DELETE` `v1/orders/{direction}/{orderID}/payments/{paymentID}`

| Parameters      | Description                    |
|------------------|---------------------------------|
| Name            | direction                      |
| Type            | string                         |
| Description     | Direction of the order, from the current user's perspective. Possible values: incoming, outgoing. |
| Required        | True                           |
| Name            | orderID                        |
| Type            | string                         |
| Description     | ID of the order.               |
| Required        | True                           |
| Name            | paymentID                      |
| Type            | string                         |
| Description     | ID of the payment.             |
| Required        | True                           |

 **Requestbody**: 
None
 **Responsestatus**: `204`

 **Responsebody**: 
None## Partially update a payment
### `PATCH` `v1/orders/{direction}/{orderID}/payments/{paymentID}`

| Parameters      | Description                    |
|------------------|---------------------------------|
| Name            | direction                      |
| Type            | string                         |
| Description     | Direction of the order, from the current user's perspective. Possible values: incoming, outgoing. |
| Required        | True                           |
| Name            | orderID                        |
| Type            | string                         |
| Description     | ID of the order.               |
| Required        | True                           |
| Name            | paymentID                      |
| Type            | string                         |
| Description     | ID of the payment.             |
| Required        | True                           |

 **Requestbody**: 
{'Sample': '{\r\n  "ID": "",\r\n  "Type": "PurchaseOrder",\r\n  "CreditCardID": "",\r\n  "SpendingAccountID": "",\r\n  "Description": "",\r\n  "Amount": 0,\r\n  "Accepted": false,\r\n  "xp": {}\r\n}', 'Fields': [{'Name': 'ID', 'Type': 'string', 'Description': 'ID of the payment. Can only contain characters Aa-Zz, 0-9, -, and _. Searchable: priority level 1. Sortable.', 'Required': False}, {'Name': 'Type', 'Type': 'string', 'Description': 'Type of the payment. Sortable. Possible values: PurchaseOrder, CreditCard, SpendingAccount.', 'Required': False}, {'Name': 'CreditCardID', 'Type': 'string', 'Description': 'ID of the credit card. Sortable.', 'Required': False}, {'Name': 'SpendingAccountID', 'Type': 'string', 'Description': 'ID of the spending account. Sortable.', 'Required': False}, {'Name': 'Description', 'Type': 'string', 'Description': 'Description of the payment. Max length 2000 characters. Searchable: priority level 2.', 'Required': False}, {'Name': 'Amount', 'Type': 'float', 'Description': 'If null, Payment applies to order total (or total of specific Line Items, if set), minus any other Payments where Amount is set.', 'Required': False}, {'Name': 'Accepted', 'Type': 'boolean', 'Description': 'Accepted of the payment.', 'Required': False}, {'Name': 'xp', 'Type': 'object', 'Description': 'Container for extended (custom) properties of the payment.', 'Required': False}]}
 **Responsestatus**: `200`

 **Responsebody**: 
{'Sample': '{\r\n  "ID": "",\r\n  "Type": "PurchaseOrder",\r\n  "DateCreated": "2018-03-21T23:00:00+00:00",\r\n  "CreditCardID": "",\r\n  "SpendingAccountID": "",\r\n  "Description": "",\r\n  "Amount": 0,\r\n  "Accepted": false,\r\n  "xp": {},\r\n  "Transactions": [\r\n    {\r\n      "ID": "",\r\n      "Type": "",\r\n      "DateExecuted": "2018-03-21T23:00:00+00:00",\r\n      "Amount": 0,\r\n      "Succeeded": false,\r\n      "ResultCode": "",\r\n      "ResultMessage": "",\r\n      "xp": {}\r\n    }\r\n  ]\r\n}', 'Fields': [{'Name': 'ID', 'Type': 'string', 'Description': 'ID of the payment.', 'Required': False}, {'Name': 'Type', 'Type': 'string', 'Description': 'Type of the payment. Possible values: PurchaseOrder, CreditCard, SpendingAccount.', 'Required': False}, {'Name': 'DateCreated', 'Type': 'date', 'Description': 'Date created of the payment.', 'Required': False}, {'Name': 'CreditCardID', 'Type': 'string', 'Description': 'ID of the credit card.', 'Required': False}, {'Name': 'SpendingAccountID', 'Type': 'string', 'Description': 'ID of the spending account.', 'Required': False}, {'Name': 'Description', 'Type': 'string', 'Description': 'Description of the payment.', 'Required': False}, {'Name': 'Amount', 'Type': 'float', 'Description': 'If null, Payment applies to order total (or total of specific Line Items, if set), minus any other Payments where Amount is set.', 'Required': False}, {'Name': 'Accepted', 'Type': 'boolean', 'Description': 'Accepted of the payment.', 'Required': False}, {'Name': 'xp', 'Type': 'object', 'Description': 'Container for extended (custom) properties of the payment.', 'Required': False}, {'Name': 'Transactions', 'Type': 'array', 'Description': 'Transactions of the payment.', 'Required': False}]}## Create a new payment transaction
### `POST` `v1/orders/{direction}/{orderID}/payments/{paymentID}/transactions`

| Parameters      | Description                    |
|------------------|---------------------------------|
| Name            | direction                      |
| Type            | string                         |
| Description     | Direction of the order, from the current user's perspective. Possible values: incoming, outgoing. |
| Required        | True                           |
| Name            | orderID                        |
| Type            | string                         |
| Description     | ID of the order.               |
| Required        | True                           |
| Name            | paymentID                      |
| Type            | string                         |
| Description     | ID of the payment.             |
| Required        | True                           |

 **Requestbody**: 
{'Sample': '{\r\n  "ID": "",\r\n  "Type": "",\r\n  "DateExecuted": "2018-03-21T23:00:00+00:00",\r\n  "Amount": 0,\r\n  "Succeeded": false,\r\n  "ResultCode": "",\r\n  "ResultMessage": "",\r\n  "xp": {}\r\n}', 'Fields': [{'Name': 'ID', 'Type': 'string', 'Description': 'ID of the payment transaction. Can only contain characters Aa-Zz, 0-9, -, and _. Searchable: priority level 1. Sortable.', 'Required': False}, {'Name': 'Type', 'Type': 'string', 'Description': 'Type of the payment transaction. Required. Sortable.', 'Required': True}, {'Name': 'DateExecuted', 'Type': 'date', 'Description': 'Date executed of the payment transaction. Required. Sortable: priority level 1.', 'Required': True}, {'Name': 'Amount', 'Type': 'float', 'Description': 'Usually the same as Payment Amount, but can be different. A charge might have a subsequent partial credit, for example.', 'Required': False}, {'Name': 'Succeeded', 'Type': 'boolean', 'Description': 'Succeeded of the payment transaction. Sortable.', 'Required': False}, {'Name': 'ResultCode', 'Type': 'string', 'Description': 'Result code of the payment transaction. Sortable.', 'Required': False}, {'Name': 'ResultMessage', 'Type': 'string', 'Description': 'Result message of the payment transaction. Sortable.', 'Required': False}, {'Name': 'xp', 'Type': 'object', 'Description': 'Container for extended (custom) properties of the payment transaction.', 'Required': False}]}
 **Responsestatus**: `201`

 **Responsebody**: 
{'Sample': '{\r\n  "ID": "",\r\n  "Type": "PurchaseOrder",\r\n  "DateCreated": "2018-03-21T23:00:00+00:00",\r\n  "CreditCardID": "",\r\n  "SpendingAccountID": "",\r\n  "Description": "",\r\n  "Amount": 0,\r\n  "Accepted": false,\r\n  "xp": {},\r\n  "Transactions": [\r\n    {\r\n      "ID": "",\r\n      "Type": "",\r\n      "DateExecuted": "2018-03-21T23:00:00+00:00",\r\n      "Amount": 0,\r\n      "Succeeded": false,\r\n      "ResultCode": "",\r\n      "ResultMessage": "",\r\n      "xp": {}\r\n    }\r\n  ]\r\n}', 'Fields': [{'Name': 'ID', 'Type': 'string', 'Description': 'ID of the payment.', 'Required': False}, {'Name': 'Type', 'Type': 'string', 'Description': 'Type of the payment. Possible values: PurchaseOrder, CreditCard, SpendingAccount.', 'Required': False}, {'Name': 'DateCreated', 'Type': 'date', 'Description': 'Date created of the payment.', 'Required': False}, {'Name': 'CreditCardID', 'Type': 'string', 'Description': 'ID of the credit card.', 'Required': False}, {'Name': 'SpendingAccountID', 'Type': 'string', 'Description': 'ID of the spending account.', 'Required': False}, {'Name': 'Description', 'Type': 'string', 'Description': 'Description of the payment.', 'Required': False}, {'Name': 'Amount', 'Type': 'float', 'Description': 'If null, Payment applies to order total (or total of specific Line Items, if set), minus any other Payments where Amount is set.', 'Required': False}, {'Name': 'Accepted', 'Type': 'boolean', 'Description': 'Accepted of the payment.', 'Required': False}, {'Name': 'xp', 'Type': 'object', 'Description': 'Container for extended (custom) properties of the payment.', 'Required': False}, {'Name': 'Transactions', 'Type': 'array', 'Description': 'Transactions of the payment.', 'Required': False}]}## Delete a payment transaction
### `DELETE` `v1/orders/{direction}/{orderID}/payments/{paymentID}/transactions/{transactionID}`

| Parameters      | Description                    |
|------------------|---------------------------------|
| Name            | direction                      |
| Type            | string                         |
| Description     | Direction of the order, from the current user's perspective. Possible values: incoming, outgoing. |
| Required        | True                           |
| Name            | orderID                        |
| Type            | string                         |
| Description     | ID of the order.               |
| Required        | True                           |
| Name            | paymentID                      |
| Type            | string                         |
| Description     | ID of the payment.             |
| Required        | True                           |
| Name            | transactionID                  |
| Type            | string                         |
| Description     | ID of the transaction.         |
| Required        | True                           |

 **Requestbody**: 
None
 **Responsestatus**: `204`

 **Responsebody**: 
None