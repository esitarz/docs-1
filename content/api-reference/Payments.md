---
title: Payments
date: 2018-03-27
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

## Request Body
**Response Status**: `200`

## Response Body
	{
	    "Accepted": false,
	    "Amount": 0,
	    "CreditCardID": "",
	    "DateCreated": "2018-03-27T16:00:00+00:00",
	    "Description": "",
	    "ID": "",
	    "SpendingAccountID": "",
	    "Transactions": [
	        {
	            "Amount": 0,
	            "DateExecuted": "2018-03-27T16:00:00+00:00",
	            "ID": "",
	            "ResultCode": "",
	            "ResultMessage": "",
	            "Succeeded": false,
	            "Type": "",
	            "xp": {}
	        }
	    ],
	    "Type": "PurchaseOrder",
	    "xp": {}
	}
| Name | Type | Description | Required | 
|---|---|---|---|
| ID | string | ID of the payment. | False |
| Type | string | Type of the payment. Possible values: PurchaseOrder, CreditCard, SpendingAccount. | False |
| DateCreated | date | Date created of the payment. | False |
| CreditCardID | string | ID of the credit card. | False |
| SpendingAccountID | string | ID of the spending account. | False |
| Description | string | Description of the payment. | False |
| Amount | float | If null, Payment applies to order total (or total of specific Line Items, if set), minus any other Payments where Amount is set. | False |
| Accepted | boolean | Accepted of the payment. | False |
| xp | object | Container for extended (custom) properties of the payment. | False |
| Transactions | array | Transactions of the payment. | False |

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

## Request Body
**Response Status**: `200`

## Response Body
	{
	    "Items": [
	        {
	            "Accepted": false,
	            "Amount": 0,
	            "CreditCardID": "",
	            "DateCreated": "2018-03-27T16:00:00+00:00",
	            "Description": "",
	            "ID": "",
	            "SpendingAccountID": "",
	            "Transactions": [
	                {
	                    "Amount": 0,
	                    "DateExecuted": "2018-03-27T16:00:00+00:00",
	                    "ID": "",
	                    "ResultCode": "",
	                    "ResultMessage": "",
	                    "Succeeded": false,
	                    "Type": "",
	                    "xp": {}
	                }
	            ],
	            "Type": "PurchaseOrder",
	            "xp": {}
	        }
	    ],
	    "Meta": {
	        "ItemRange": [
	            1,
	            20
	        ],
	        "Page": 1,
	        "PageSize": 20,
	        "TotalCount": 25,
	        "TotalPages": 2
	    }
	}
| Name | Type | Description | Required | 
|---|---|---|---|
| ID | string | ID of the payment. | False |
| Type | string | Type of the payment. Possible values: PurchaseOrder, CreditCard, SpendingAccount. | False |
| DateCreated | date | Date created of the payment. | False |
| CreditCardID | string | ID of the credit card. | False |
| SpendingAccountID | string | ID of the spending account. | False |
| Description | string | Description of the payment. | False |
| Amount | float | If null, Payment applies to order total (or total of specific Line Items, if set), minus any other Payments where Amount is set. | False |
| Accepted | boolean | Accepted of the payment. | False |
| xp | object | Container for extended (custom) properties of the payment. | False |
| Transactions | array | Transactions of the payment. | False |

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

## Request Body
	{
	    "Accepted": false,
	    "Amount": 0,
	    "CreditCardID": "",
	    "Description": "",
	    "ID": "",
	    "SpendingAccountID": "",
	    "Type": "PurchaseOrder",
	    "xp": {}
	}
| Name | Type | Description | Required | 
|---|---|---|---|
| ID | string | ID of the payment. Can only contain characters Aa-Zz, 0-9, -, and _. Searchable: priority level 1. Sortable. | False |
| Type | string | Type of the payment. Sortable. Possible values: PurchaseOrder, CreditCard, SpendingAccount. | False |
| CreditCardID | string | ID of the credit card. Sortable. | False |
| SpendingAccountID | string | ID of the spending account. Sortable. | False |
| Description | string | Description of the payment. Max length 2000 characters. Searchable: priority level 2. | False |
| Amount | float | If null, Payment applies to order total (or total of specific Line Items, if set), minus any other Payments where Amount is set. | False |
| Accepted | boolean | Accepted of the payment. | False |
| xp | object | Container for extended (custom) properties of the payment. | False |

**Response Status**: `201`

## Response Body
	{
	    "Accepted": false,
	    "Amount": 0,
	    "CreditCardID": "",
	    "DateCreated": "2018-03-27T16:00:00+00:00",
	    "Description": "",
	    "ID": "",
	    "SpendingAccountID": "",
	    "Transactions": [
	        {
	            "Amount": 0,
	            "DateExecuted": "2018-03-27T16:00:00+00:00",
	            "ID": "",
	            "ResultCode": "",
	            "ResultMessage": "",
	            "Succeeded": false,
	            "Type": "",
	            "xp": {}
	        }
	    ],
	    "Type": "PurchaseOrder",
	    "xp": {}
	}
| Name | Type | Description | Required | 
|---|---|---|---|
| ID | string | ID of the payment. | False |
| Type | string | Type of the payment. Possible values: PurchaseOrder, CreditCard, SpendingAccount. | False |
| DateCreated | date | Date created of the payment. | False |
| CreditCardID | string | ID of the credit card. | False |
| SpendingAccountID | string | ID of the spending account. | False |
| Description | string | Description of the payment. | False |
| Amount | float | If null, Payment applies to order total (or total of specific Line Items, if set), minus any other Payments where Amount is set. | False |
| Accepted | boolean | Accepted of the payment. | False |
| xp | object | Container for extended (custom) properties of the payment. | False |
| Transactions | array | Transactions of the payment. | False |

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

## Request Body
**Response Status**: `204`

## Response Body
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

## Request Body
	{
	    "Accepted": false,
	    "Amount": 0,
	    "CreditCardID": "",
	    "Description": "",
	    "ID": "",
	    "SpendingAccountID": "",
	    "Type": "PurchaseOrder",
	    "xp": {}
	}
| Name | Type | Description | Required | 
|---|---|---|---|
| ID | string | ID of the payment. Can only contain characters Aa-Zz, 0-9, -, and _. Searchable: priority level 1. Sortable. | False |
| Type | string | Type of the payment. Sortable. Possible values: PurchaseOrder, CreditCard, SpendingAccount. | False |
| CreditCardID | string | ID of the credit card. Sortable. | False |
| SpendingAccountID | string | ID of the spending account. Sortable. | False |
| Description | string | Description of the payment. Max length 2000 characters. Searchable: priority level 2. | False |
| Amount | float | If null, Payment applies to order total (or total of specific Line Items, if set), minus any other Payments where Amount is set. | False |
| Accepted | boolean | Accepted of the payment. | False |
| xp | object | Container for extended (custom) properties of the payment. | False |

**Response Status**: `200`

## Response Body
	{
	    "Accepted": false,
	    "Amount": 0,
	    "CreditCardID": "",
	    "DateCreated": "2018-03-27T16:00:00+00:00",
	    "Description": "",
	    "ID": "",
	    "SpendingAccountID": "",
	    "Transactions": [
	        {
	            "Amount": 0,
	            "DateExecuted": "2018-03-27T16:00:00+00:00",
	            "ID": "",
	            "ResultCode": "",
	            "ResultMessage": "",
	            "Succeeded": false,
	            "Type": "",
	            "xp": {}
	        }
	    ],
	    "Type": "PurchaseOrder",
	    "xp": {}
	}
| Name | Type | Description | Required | 
|---|---|---|---|
| ID | string | ID of the payment. | False |
| Type | string | Type of the payment. Possible values: PurchaseOrder, CreditCard, SpendingAccount. | False |
| DateCreated | date | Date created of the payment. | False |
| CreditCardID | string | ID of the credit card. | False |
| SpendingAccountID | string | ID of the spending account. | False |
| Description | string | Description of the payment. | False |
| Amount | float | If null, Payment applies to order total (or total of specific Line Items, if set), minus any other Payments where Amount is set. | False |
| Accepted | boolean | Accepted of the payment. | False |
| xp | object | Container for extended (custom) properties of the payment. | False |
| Transactions | array | Transactions of the payment. | False |

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

## Request Body
	{
	    "Amount": 0,
	    "DateExecuted": "2018-03-27T16:00:00+00:00",
	    "ID": "",
	    "ResultCode": "",
	    "ResultMessage": "",
	    "Succeeded": false,
	    "Type": "",
	    "xp": {}
	}
| Name | Type | Description | Required | 
|---|---|---|---|
| ID | string | ID of the payment transaction. Can only contain characters Aa-Zz, 0-9, -, and _. Searchable: priority level 1. Sortable. | False |
| Type | string | Type of the payment transaction. Required. Sortable. | True |
| DateExecuted | date | Date executed of the payment transaction. Required. Sortable: priority level 1. | True |
| Amount | float | Usually the same as Payment Amount, but can be different. A charge might have a subsequent partial credit, for example. | False |
| Succeeded | boolean | Succeeded of the payment transaction. Sortable. | False |
| ResultCode | string | Result code of the payment transaction. Sortable. | False |
| ResultMessage | string | Result message of the payment transaction. Sortable. | False |
| xp | object | Container for extended (custom) properties of the payment transaction. | False |

**Response Status**: `201`

## Response Body
	{
	    "Accepted": false,
	    "Amount": 0,
	    "CreditCardID": "",
	    "DateCreated": "2018-03-27T16:00:00+00:00",
	    "Description": "",
	    "ID": "",
	    "SpendingAccountID": "",
	    "Transactions": [
	        {
	            "Amount": 0,
	            "DateExecuted": "2018-03-27T16:00:00+00:00",
	            "ID": "",
	            "ResultCode": "",
	            "ResultMessage": "",
	            "Succeeded": false,
	            "Type": "",
	            "xp": {}
	        }
	    ],
	    "Type": "PurchaseOrder",
	    "xp": {}
	}
| Name | Type | Description | Required | 
|---|---|---|---|
| ID | string | ID of the payment. | False |
| Type | string | Type of the payment. Possible values: PurchaseOrder, CreditCard, SpendingAccount. | False |
| DateCreated | date | Date created of the payment. | False |
| CreditCardID | string | ID of the credit card. | False |
| SpendingAccountID | string | ID of the spending account. | False |
| Description | string | Description of the payment. | False |
| Amount | float | If null, Payment applies to order total (or total of specific Line Items, if set), minus any other Payments where Amount is set. | False |
| Accepted | boolean | Accepted of the payment. | False |
| xp | object | Container for extended (custom) properties of the payment. | False |
| Transactions | array | Transactions of the payment. | False |

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

## Request Body
**Response Status**: `204`

## Response Body