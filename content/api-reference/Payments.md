---
title: Payments
date: 2018-03-27
category: API Reference
tags: Orders And Fulfillment
slug: Orders-And-Fulfillment-Payments
---


## `GET` `v1/orders/{direction}/{orderID}/payments/{paymentID}`
Get a single payment

| Name | Type | Description | Required | 
|---|---|---|---|
| direction | string | Direction of the order, from the current user's perspective. Possible values: incoming, outgoing. | True |
| orderID | string | ID of the order. | True |
| paymentID | string | ID of the payment. | True |

## Response Body
	:::json
	{
	    "Accepted": false,
	    "Amount": 0,
	    "CreditCardID": "",
	    "DateCreated": "2018-03-27T19:00:00+00:00",
	    "Description": "",
	    "ID": "",
	    "SpendingAccountID": "",
	    "Transactions": [
	        {
	            "Amount": 0,
	            "DateExecuted": "2018-03-27T19:00:00+00:00",
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

| Name | Type | Description | Required | 
|---|---|---|---|
| direction | string | Direction of the order, from the current user's perspective. Possible values: incoming, outgoing. | True |
| orderID | string | ID of the order. | True |
| search | string | Word or phrase to search for. | False |
| searchOn | string | Comma-delimited list of fields to search on. | False |
| sortBy | string | Comma-delimited list of fields to sort by. | False |
| page | integer | Page of results to return. Default: 1 | False |
| pageSize | integer | Number of results to return per page. Default: 20, max: 100. | False |
| filters | object | Any additional key/value pairs passed in the query string are interpretted as filters. Valid keys are top-level properties of the returned model or 'xp.???' | False |

## Response Body
	:::json
	{
	    "Items": [
	        {
	            "Accepted": false,
	            "Amount": 0,
	            "CreditCardID": "",
	            "DateCreated": "2018-03-27T19:00:00+00:00",
	            "Description": "",
	            "ID": "",
	            "SpendingAccountID": "",
	            "Transactions": [
	                {
	                    "Amount": 0,
	                    "DateExecuted": "2018-03-27T19:00:00+00:00",
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

| Name | Type | Description | Required | 
|---|---|---|---|
| direction | string | Direction of the order, from the current user's perspective. Possible values: incoming, outgoing. | True |
| orderID | string | ID of the order. | True |

## Request Body
	:::json
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

## Response Body
	:::json
	{
	    "Accepted": false,
	    "Amount": 0,
	    "CreditCardID": "",
	    "DateCreated": "2018-03-27T19:00:00+00:00",
	    "Description": "",
	    "ID": "",
	    "SpendingAccountID": "",
	    "Transactions": [
	        {
	            "Amount": 0,
	            "DateExecuted": "2018-03-27T19:00:00+00:00",
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

| Name | Type | Description | Required | 
|---|---|---|---|
| direction | string | Direction of the order, from the current user's perspective. Possible values: incoming, outgoing. | True |
| orderID | string | ID of the order. | True |
| paymentID | string | ID of the payment. | True |

## Response Body
## `PATCH` `v1/orders/{direction}/{orderID}/payments/{paymentID}`
Partially update a payment

| Name | Type | Description | Required | 
|---|---|---|---|
| direction | string | Direction of the order, from the current user's perspective. Possible values: incoming, outgoing. | True |
| orderID | string | ID of the order. | True |
| paymentID | string | ID of the payment. | True |

## Request Body
	:::json
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

## Response Body
	:::json
	{
	    "Accepted": false,
	    "Amount": 0,
	    "CreditCardID": "",
	    "DateCreated": "2018-03-27T19:00:00+00:00",
	    "Description": "",
	    "ID": "",
	    "SpendingAccountID": "",
	    "Transactions": [
	        {
	            "Amount": 0,
	            "DateExecuted": "2018-03-27T19:00:00+00:00",
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

| Name | Type | Description | Required | 
|---|---|---|---|
| direction | string | Direction of the order, from the current user's perspective. Possible values: incoming, outgoing. | True |
| orderID | string | ID of the order. | True |
| paymentID | string | ID of the payment. | True |

## Request Body
	:::json
	{
	    "Amount": 0,
	    "DateExecuted": "2018-03-27T19:00:00+00:00",
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

## Response Body
	:::json
	{
	    "Accepted": false,
	    "Amount": 0,
	    "CreditCardID": "",
	    "DateCreated": "2018-03-27T19:00:00+00:00",
	    "Description": "",
	    "ID": "",
	    "SpendingAccountID": "",
	    "Transactions": [
	        {
	            "Amount": 0,
	            "DateExecuted": "2018-03-27T19:00:00+00:00",
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

| Name | Type | Description | Required | 
|---|---|---|---|
| direction | string | Direction of the order, from the current user's perspective. Possible values: incoming, outgoing. | True |
| orderID | string | ID of the order. | True |
| paymentID | string | ID of the payment. | True |
| transactionID | string | ID of the transaction. | True |

## Response Body