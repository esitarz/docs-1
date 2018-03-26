---
title: Payments
date: 2018-03-26
category: API Reference
tags: Orders And Fulfillment
slug: Orders-And-Fulfillment-Payments
---


## `GET` `v1/orders/{direction}/{orderID}/payments/{paymentID}`
Get a single payment

| Parameters      | Description                    |
|------------------|---------------------------------|


| Parameters      | Description                    |
|------------------|---------------------------------|
| Name            | direction                      |
| Type            | string                         |
| Description     | Direction of the order, from the current user's perspective. Possible values: incoming, outgoing. |
| Required        | True                           |


| Parameters      | Description                    |
|------------------|---------------------------------|
| Name            | orderID                        |
| Type            | string                         |
| Description     | ID of the order.               |
| Required        | True                           |


| Parameters      | Description                    |
|------------------|---------------------------------|
| Name            | paymentID                      |
| Type            | string                         |
| Description     | ID of the payment.             |
| Required        | True                           |

## Requestbody
**Responsestatus**: `200`

## Responsebody
```
{'ID': '', 'Type': 'PurchaseOrder', 'DateCreated': '2018-03-21T23:00:00+00:00', 'CreditCardID': '', 'SpendingAccountID': '', 'Description': '', 'Amount': 0, 'Accepted': False, 'xp': {}, 'Transactions': [{'ID': '', 'Type': '', 'DateExecuted': '2018-03-21T23:00:00+00:00', 'Amount': 0, 'Succeeded': False, 'ResultCode': '', 'ResultMessage': '', 'xp': {}}]}
```


| Parameters      | Description                    |
|------------------|---------------------------------|
| Name            | ID                             |
| Type            | string                         |
| Description     | ID of the payment.             |
| Required        | False                          |


| Parameters      | Description                    |
|------------------|---------------------------------|
| Name            | Type                           |
| Type            | string                         |
| Description     | Type of the payment. Possible values: PurchaseOrder, CreditCard, SpendingAccount. |
| Required        | False                          |


| Parameters      | Description                    |
|------------------|---------------------------------|
| Name            | DateCreated                    |
| Type            | date                           |
| Description     | Date created of the payment.   |
| Required        | False                          |


| Parameters      | Description                    |
|------------------|---------------------------------|
| Name            | CreditCardID                   |
| Type            | string                         |
| Description     | ID of the credit card.         |
| Required        | False                          |


| Parameters      | Description                    |
|------------------|---------------------------------|
| Name            | SpendingAccountID              |
| Type            | string                         |
| Description     | ID of the spending account.    |
| Required        | False                          |


| Parameters      | Description                    |
|------------------|---------------------------------|
| Name            | Description                    |
| Type            | string                         |
| Description     | Description of the payment.    |
| Required        | False                          |


| Parameters      | Description                    |
|------------------|---------------------------------|
| Name            | Amount                         |
| Type            | float                          |
| Description     | If null, Payment applies to order total (or total of specific Line Items, if set), minus any other Payments where Amount is set. |
| Required        | False                          |


| Parameters      | Description                    |
|------------------|---------------------------------|
| Name            | Accepted                       |
| Type            | boolean                        |
| Description     | Accepted of the payment.       |
| Required        | False                          |


| Parameters      | Description                    |
|------------------|---------------------------------|
| Name            | xp                             |
| Type            | object                         |
| Description     | Container for extended (custom) properties of the payment. |
| Required        | False                          |


| Parameters      | Description                    |
|------------------|---------------------------------|
| Name            | Transactions                   |
| Type            | array                          |
| Description     | Transactions of the payment.   |
| Required        | False                          |

## `GET` `v1/orders/{direction}/{orderID}/payments`
Get a list of payments

| Parameters      | Description                    |
|------------------|---------------------------------|


| Parameters      | Description                    |
|------------------|---------------------------------|
| Name            | direction                      |
| Type            | string                         |
| Description     | Direction of the order, from the current user's perspective. Possible values: incoming, outgoing. |
| Required        | True                           |


| Parameters      | Description                    |
|------------------|---------------------------------|
| Name            | orderID                        |
| Type            | string                         |
| Description     | ID of the order.               |
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
{'Meta': {'Page': 1, 'PageSize': 20, 'TotalCount': 25, 'TotalPages': 2, 'ItemRange': [1, 20]}, 'Items': [{'ID': '', 'Type': 'PurchaseOrder', 'DateCreated': '2018-03-21T23:00:00+00:00', 'CreditCardID': '', 'SpendingAccountID': '', 'Description': '', 'Amount': 0, 'Accepted': False, 'xp': {}, 'Transactions': [{'ID': '', 'Type': '', 'DateExecuted': '2018-03-21T23:00:00+00:00', 'Amount': 0, 'Succeeded': False, 'ResultCode': '', 'ResultMessage': '', 'xp': {}}]}]}
```


| Parameters      | Description                    |
|------------------|---------------------------------|
| Name            | ID                             |
| Type            | string                         |
| Description     | ID of the payment.             |
| Required        | False                          |


| Parameters      | Description                    |
|------------------|---------------------------------|
| Name            | Type                           |
| Type            | string                         |
| Description     | Type of the payment. Possible values: PurchaseOrder, CreditCard, SpendingAccount. |
| Required        | False                          |


| Parameters      | Description                    |
|------------------|---------------------------------|
| Name            | DateCreated                    |
| Type            | date                           |
| Description     | Date created of the payment.   |
| Required        | False                          |


| Parameters      | Description                    |
|------------------|---------------------------------|
| Name            | CreditCardID                   |
| Type            | string                         |
| Description     | ID of the credit card.         |
| Required        | False                          |


| Parameters      | Description                    |
|------------------|---------------------------------|
| Name            | SpendingAccountID              |
| Type            | string                         |
| Description     | ID of the spending account.    |
| Required        | False                          |


| Parameters      | Description                    |
|------------------|---------------------------------|
| Name            | Description                    |
| Type            | string                         |
| Description     | Description of the payment.    |
| Required        | False                          |


| Parameters      | Description                    |
|------------------|---------------------------------|
| Name            | Amount                         |
| Type            | float                          |
| Description     | If null, Payment applies to order total (or total of specific Line Items, if set), minus any other Payments where Amount is set. |
| Required        | False                          |


| Parameters      | Description                    |
|------------------|---------------------------------|
| Name            | Accepted                       |
| Type            | boolean                        |
| Description     | Accepted of the payment.       |
| Required        | False                          |


| Parameters      | Description                    |
|------------------|---------------------------------|
| Name            | xp                             |
| Type            | object                         |
| Description     | Container for extended (custom) properties of the payment. |
| Required        | False                          |


| Parameters      | Description                    |
|------------------|---------------------------------|
| Name            | Transactions                   |
| Type            | array                          |
| Description     | Transactions of the payment.   |
| Required        | False                          |

## `POST` `v1/orders/{direction}/{orderID}/payments`
Create a new payment

| Parameters      | Description                    |
|------------------|---------------------------------|


| Parameters      | Description                    |
|------------------|---------------------------------|
| Name            | direction                      |
| Type            | string                         |
| Description     | Direction of the order, from the current user's perspective. Possible values: incoming, outgoing. |
| Required        | True                           |


| Parameters      | Description                    |
|------------------|---------------------------------|
| Name            | orderID                        |
| Type            | string                         |
| Description     | ID of the order.               |
| Required        | True                           |

## Requestbody
```
{'ID': '', 'Type': 'PurchaseOrder', 'CreditCardID': '', 'SpendingAccountID': '', 'Description': '', 'Amount': 0, 'Accepted': False, 'xp': {}}
```

```
[{'Name': 'ID', 'Type': 'string', 'Description': 'ID of the payment. Can only contain characters Aa-Zz, 0-9, -, and _. Searchable: priority level 1. Sortable.', 'Required': False}, {'Name': 'Type', 'Type': 'string', 'Description': 'Type of the payment. Sortable. Possible values: PurchaseOrder, CreditCard, SpendingAccount.', 'Required': False}, {'Name': 'CreditCardID', 'Type': 'string', 'Description': 'ID of the credit card. Sortable.', 'Required': False}, {'Name': 'SpendingAccountID', 'Type': 'string', 'Description': 'ID of the spending account. Sortable.', 'Required': False}, {'Name': 'Description', 'Type': 'string', 'Description': 'Description of the payment. Max length 2000 characters. Searchable: priority level 2.', 'Required': False}, {'Name': 'Amount', 'Type': 'float', 'Description': 'If null, Payment applies to order total (or total of specific Line Items, if set), minus any other Payments where Amount is set.', 'Required': False}, {'Name': 'Accepted', 'Type': 'boolean', 'Description': 'Accepted of the payment.', 'Required': False}, {'Name': 'xp', 'Type': 'object', 'Description': 'Container for extended (custom) properties of the payment.', 'Required': False}]
```

**Responsestatus**: `201`

## Responsebody
```
{'ID': '', 'Type': 'PurchaseOrder', 'DateCreated': '2018-03-21T23:00:00+00:00', 'CreditCardID': '', 'SpendingAccountID': '', 'Description': '', 'Amount': 0, 'Accepted': False, 'xp': {}, 'Transactions': [{'ID': '', 'Type': '', 'DateExecuted': '2018-03-21T23:00:00+00:00', 'Amount': 0, 'Succeeded': False, 'ResultCode': '', 'ResultMessage': '', 'xp': {}}]}
```


| Parameters      | Description                    |
|------------------|---------------------------------|
| Name            | ID                             |
| Type            | string                         |
| Description     | ID of the payment.             |
| Required        | False                          |


| Parameters      | Description                    |
|------------------|---------------------------------|
| Name            | Type                           |
| Type            | string                         |
| Description     | Type of the payment. Possible values: PurchaseOrder, CreditCard, SpendingAccount. |
| Required        | False                          |


| Parameters      | Description                    |
|------------------|---------------------------------|
| Name            | DateCreated                    |
| Type            | date                           |
| Description     | Date created of the payment.   |
| Required        | False                          |


| Parameters      | Description                    |
|------------------|---------------------------------|
| Name            | CreditCardID                   |
| Type            | string                         |
| Description     | ID of the credit card.         |
| Required        | False                          |


| Parameters      | Description                    |
|------------------|---------------------------------|
| Name            | SpendingAccountID              |
| Type            | string                         |
| Description     | ID of the spending account.    |
| Required        | False                          |


| Parameters      | Description                    |
|------------------|---------------------------------|
| Name            | Description                    |
| Type            | string                         |
| Description     | Description of the payment.    |
| Required        | False                          |


| Parameters      | Description                    |
|------------------|---------------------------------|
| Name            | Amount                         |
| Type            | float                          |
| Description     | If null, Payment applies to order total (or total of specific Line Items, if set), minus any other Payments where Amount is set. |
| Required        | False                          |


| Parameters      | Description                    |
|------------------|---------------------------------|
| Name            | Accepted                       |
| Type            | boolean                        |
| Description     | Accepted of the payment.       |
| Required        | False                          |


| Parameters      | Description                    |
|------------------|---------------------------------|
| Name            | xp                             |
| Type            | object                         |
| Description     | Container for extended (custom) properties of the payment. |
| Required        | False                          |


| Parameters      | Description                    |
|------------------|---------------------------------|
| Name            | Transactions                   |
| Type            | array                          |
| Description     | Transactions of the payment.   |
| Required        | False                          |

## `DELETE` `v1/orders/{direction}/{orderID}/payments/{paymentID}`
Delete a payment

| Parameters      | Description                    |
|------------------|---------------------------------|


| Parameters      | Description                    |
|------------------|---------------------------------|
| Name            | direction                      |
| Type            | string                         |
| Description     | Direction of the order, from the current user's perspective. Possible values: incoming, outgoing. |
| Required        | True                           |


| Parameters      | Description                    |
|------------------|---------------------------------|
| Name            | orderID                        |
| Type            | string                         |
| Description     | ID of the order.               |
| Required        | True                           |


| Parameters      | Description                    |
|------------------|---------------------------------|
| Name            | paymentID                      |
| Type            | string                         |
| Description     | ID of the payment.             |
| Required        | True                           |

## Requestbody
**Responsestatus**: `204`

## Responsebody
## `PATCH` `v1/orders/{direction}/{orderID}/payments/{paymentID}`
Partially update a payment

| Parameters      | Description                    |
|------------------|---------------------------------|


| Parameters      | Description                    |
|------------------|---------------------------------|
| Name            | direction                      |
| Type            | string                         |
| Description     | Direction of the order, from the current user's perspective. Possible values: incoming, outgoing. |
| Required        | True                           |


| Parameters      | Description                    |
|------------------|---------------------------------|
| Name            | orderID                        |
| Type            | string                         |
| Description     | ID of the order.               |
| Required        | True                           |


| Parameters      | Description                    |
|------------------|---------------------------------|
| Name            | paymentID                      |
| Type            | string                         |
| Description     | ID of the payment.             |
| Required        | True                           |

## Requestbody
```
{'ID': '', 'Type': 'PurchaseOrder', 'CreditCardID': '', 'SpendingAccountID': '', 'Description': '', 'Amount': 0, 'Accepted': False, 'xp': {}}
```

```
[{'Name': 'ID', 'Type': 'string', 'Description': 'ID of the payment. Can only contain characters Aa-Zz, 0-9, -, and _. Searchable: priority level 1. Sortable.', 'Required': False}, {'Name': 'Type', 'Type': 'string', 'Description': 'Type of the payment. Sortable. Possible values: PurchaseOrder, CreditCard, SpendingAccount.', 'Required': False}, {'Name': 'CreditCardID', 'Type': 'string', 'Description': 'ID of the credit card. Sortable.', 'Required': False}, {'Name': 'SpendingAccountID', 'Type': 'string', 'Description': 'ID of the spending account. Sortable.', 'Required': False}, {'Name': 'Description', 'Type': 'string', 'Description': 'Description of the payment. Max length 2000 characters. Searchable: priority level 2.', 'Required': False}, {'Name': 'Amount', 'Type': 'float', 'Description': 'If null, Payment applies to order total (or total of specific Line Items, if set), minus any other Payments where Amount is set.', 'Required': False}, {'Name': 'Accepted', 'Type': 'boolean', 'Description': 'Accepted of the payment.', 'Required': False}, {'Name': 'xp', 'Type': 'object', 'Description': 'Container for extended (custom) properties of the payment.', 'Required': False}]
```

**Responsestatus**: `200`

## Responsebody
```
{'ID': '', 'Type': 'PurchaseOrder', 'DateCreated': '2018-03-21T23:00:00+00:00', 'CreditCardID': '', 'SpendingAccountID': '', 'Description': '', 'Amount': 0, 'Accepted': False, 'xp': {}, 'Transactions': [{'ID': '', 'Type': '', 'DateExecuted': '2018-03-21T23:00:00+00:00', 'Amount': 0, 'Succeeded': False, 'ResultCode': '', 'ResultMessage': '', 'xp': {}}]}
```


| Parameters      | Description                    |
|------------------|---------------------------------|
| Name            | ID                             |
| Type            | string                         |
| Description     | ID of the payment.             |
| Required        | False                          |


| Parameters      | Description                    |
|------------------|---------------------------------|
| Name            | Type                           |
| Type            | string                         |
| Description     | Type of the payment. Possible values: PurchaseOrder, CreditCard, SpendingAccount. |
| Required        | False                          |


| Parameters      | Description                    |
|------------------|---------------------------------|
| Name            | DateCreated                    |
| Type            | date                           |
| Description     | Date created of the payment.   |
| Required        | False                          |


| Parameters      | Description                    |
|------------------|---------------------------------|
| Name            | CreditCardID                   |
| Type            | string                         |
| Description     | ID of the credit card.         |
| Required        | False                          |


| Parameters      | Description                    |
|------------------|---------------------------------|
| Name            | SpendingAccountID              |
| Type            | string                         |
| Description     | ID of the spending account.    |
| Required        | False                          |


| Parameters      | Description                    |
|------------------|---------------------------------|
| Name            | Description                    |
| Type            | string                         |
| Description     | Description of the payment.    |
| Required        | False                          |


| Parameters      | Description                    |
|------------------|---------------------------------|
| Name            | Amount                         |
| Type            | float                          |
| Description     | If null, Payment applies to order total (or total of specific Line Items, if set), minus any other Payments where Amount is set. |
| Required        | False                          |


| Parameters      | Description                    |
|------------------|---------------------------------|
| Name            | Accepted                       |
| Type            | boolean                        |
| Description     | Accepted of the payment.       |
| Required        | False                          |


| Parameters      | Description                    |
|------------------|---------------------------------|
| Name            | xp                             |
| Type            | object                         |
| Description     | Container for extended (custom) properties of the payment. |
| Required        | False                          |


| Parameters      | Description                    |
|------------------|---------------------------------|
| Name            | Transactions                   |
| Type            | array                          |
| Description     | Transactions of the payment.   |
| Required        | False                          |

## `POST` `v1/orders/{direction}/{orderID}/payments/{paymentID}/transactions`
Create a new payment transaction

| Parameters      | Description                    |
|------------------|---------------------------------|


| Parameters      | Description                    |
|------------------|---------------------------------|
| Name            | direction                      |
| Type            | string                         |
| Description     | Direction of the order, from the current user's perspective. Possible values: incoming, outgoing. |
| Required        | True                           |


| Parameters      | Description                    |
|------------------|---------------------------------|
| Name            | orderID                        |
| Type            | string                         |
| Description     | ID of the order.               |
| Required        | True                           |


| Parameters      | Description                    |
|------------------|---------------------------------|
| Name            | paymentID                      |
| Type            | string                         |
| Description     | ID of the payment.             |
| Required        | True                           |

## Requestbody
```
{'ID': '', 'Type': '', 'DateExecuted': '2018-03-21T23:00:00+00:00', 'Amount': 0, 'Succeeded': False, 'ResultCode': '', 'ResultMessage': '', 'xp': {}}
```

```
[{'Name': 'ID', 'Type': 'string', 'Description': 'ID of the payment transaction. Can only contain characters Aa-Zz, 0-9, -, and _. Searchable: priority level 1. Sortable.', 'Required': False}, {'Name': 'Type', 'Type': 'string', 'Description': 'Type of the payment transaction. Required. Sortable.', 'Required': True}, {'Name': 'DateExecuted', 'Type': 'date', 'Description': 'Date executed of the payment transaction. Required. Sortable: priority level 1.', 'Required': True}, {'Name': 'Amount', 'Type': 'float', 'Description': 'Usually the same as Payment Amount, but can be different. A charge might have a subsequent partial credit, for example.', 'Required': False}, {'Name': 'Succeeded', 'Type': 'boolean', 'Description': 'Succeeded of the payment transaction. Sortable.', 'Required': False}, {'Name': 'ResultCode', 'Type': 'string', 'Description': 'Result code of the payment transaction. Sortable.', 'Required': False}, {'Name': 'ResultMessage', 'Type': 'string', 'Description': 'Result message of the payment transaction. Sortable.', 'Required': False}, {'Name': 'xp', 'Type': 'object', 'Description': 'Container for extended (custom) properties of the payment transaction.', 'Required': False}]
```

**Responsestatus**: `201`

## Responsebody
```
{'ID': '', 'Type': 'PurchaseOrder', 'DateCreated': '2018-03-21T23:00:00+00:00', 'CreditCardID': '', 'SpendingAccountID': '', 'Description': '', 'Amount': 0, 'Accepted': False, 'xp': {}, 'Transactions': [{'ID': '', 'Type': '', 'DateExecuted': '2018-03-21T23:00:00+00:00', 'Amount': 0, 'Succeeded': False, 'ResultCode': '', 'ResultMessage': '', 'xp': {}}]}
```


| Parameters      | Description                    |
|------------------|---------------------------------|
| Name            | ID                             |
| Type            | string                         |
| Description     | ID of the payment.             |
| Required        | False                          |


| Parameters      | Description                    |
|------------------|---------------------------------|
| Name            | Type                           |
| Type            | string                         |
| Description     | Type of the payment. Possible values: PurchaseOrder, CreditCard, SpendingAccount. |
| Required        | False                          |


| Parameters      | Description                    |
|------------------|---------------------------------|
| Name            | DateCreated                    |
| Type            | date                           |
| Description     | Date created of the payment.   |
| Required        | False                          |


| Parameters      | Description                    |
|------------------|---------------------------------|
| Name            | CreditCardID                   |
| Type            | string                         |
| Description     | ID of the credit card.         |
| Required        | False                          |


| Parameters      | Description                    |
|------------------|---------------------------------|
| Name            | SpendingAccountID              |
| Type            | string                         |
| Description     | ID of the spending account.    |
| Required        | False                          |


| Parameters      | Description                    |
|------------------|---------------------------------|
| Name            | Description                    |
| Type            | string                         |
| Description     | Description of the payment.    |
| Required        | False                          |


| Parameters      | Description                    |
|------------------|---------------------------------|
| Name            | Amount                         |
| Type            | float                          |
| Description     | If null, Payment applies to order total (or total of specific Line Items, if set), minus any other Payments where Amount is set. |
| Required        | False                          |


| Parameters      | Description                    |
|------------------|---------------------------------|
| Name            | Accepted                       |
| Type            | boolean                        |
| Description     | Accepted of the payment.       |
| Required        | False                          |


| Parameters      | Description                    |
|------------------|---------------------------------|
| Name            | xp                             |
| Type            | object                         |
| Description     | Container for extended (custom) properties of the payment. |
| Required        | False                          |


| Parameters      | Description                    |
|------------------|---------------------------------|
| Name            | Transactions                   |
| Type            | array                          |
| Description     | Transactions of the payment.   |
| Required        | False                          |

## `DELETE` `v1/orders/{direction}/{orderID}/payments/{paymentID}/transactions/{transactionID}`
Delete a payment transaction

| Parameters      | Description                    |
|------------------|---------------------------------|


| Parameters      | Description                    |
|------------------|---------------------------------|
| Name            | direction                      |
| Type            | string                         |
| Description     | Direction of the order, from the current user's perspective. Possible values: incoming, outgoing. |
| Required        | True                           |


| Parameters      | Description                    |
|------------------|---------------------------------|
| Name            | orderID                        |
| Type            | string                         |
| Description     | ID of the order.               |
| Required        | True                           |


| Parameters      | Description                    |
|------------------|---------------------------------|
| Name            | paymentID                      |
| Type            | string                         |
| Description     | ID of the payment.             |
| Required        | True                           |


| Parameters      | Description                    |
|------------------|---------------------------------|
| Name            | transactionID                  |
| Type            | string                         |
| Description     | ID of the transaction.         |
| Required        | True                           |

## Requestbody
**Responsestatus**: `204`

## Responsebody