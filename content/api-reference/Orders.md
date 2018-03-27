---
title: Orders
date: 2018-03-27
category: API Reference
tags: Orders And Fulfillment
slug: Orders-And-Fulfillment-Orders
---
An Order represents a business transaction between two parties. It
typically consists of a collection of Line Items, a Payment Method, Tax
and Shipping information, etc. The OrderCloud platform defines various
"actions" that can be performed against Orders, such as Submit, Approve,
Ship, etc. These actions transform the state of the order and often
trigger external events such as financial transactions.

---

## `GET` `v1/orders/{direction}/{orderID}`
Get a single order

| Name | Type | Description | Required | 
|---|---|---|---|
| direction | string | Direction of the order, from the current user's perspective. Possible values: incoming, outgoing. | True |
| orderID | string | ID of the order. | True |

## Response Body
	{
	    "BillingAddress": {
	        "AddressName": "",
	        "City": "",
	        "CompanyName": "",
	        "Country": "",
	        "DateCreated": "2018-03-21T23:00:00+00:00",
	        "FirstName": "",
	        "ID": "",
	        "LastName": "",
	        "Phone": "",
	        "State": "",
	        "Street1": "",
	        "Street2": "",
	        "Zip": "",
	        "xp": {}
	    },
	    "BillingAddressID": "",
	    "Comments": "",
	    "DateApproved": "2018-03-21T23:00:00+00:00",
	    "DateCanceled": "2018-03-21T23:00:00+00:00",
	    "DateCompleted": "2018-03-21T23:00:00+00:00",
	    "DateCreated": "2018-03-21T23:00:00+00:00",
	    "DateDeclined": "2018-03-21T23:00:00+00:00",
	    "DateSubmitted": "2018-03-21T23:00:00+00:00",
	    "FromCompanyID": "",
	    "FromUser": {
	        "Active": false,
	        "AvailableRoles": [
	            ""
	        ],
	        "Email": "",
	        "FirstName": "",
	        "ID": "",
	        "LastName": "",
	        "Phone": "",
	        "TermsAccepted": "2018-03-21T23:00:00+00:00",
	        "Username": "",
	        "xp": {}
	    },
	    "FromUserID": "",
	    "ID": "",
	    "IsSubmitted": false,
	    "LineItemCount": 0,
	    "PromotionDiscount": 0,
	    "ShippingAddressID": "",
	    "ShippingCost": 0,
	    "Status": "Unsubmitted",
	    "Subtotal": 0,
	    "TaxCost": 0,
	    "Total": 0,
	    "xp": {}
	}
| Name | Type | Description | Required | 
|---|---|---|---|
| ID | string | ID of the order. | False |
| FromUser | object | From user of the order. | False |
| FromCompanyID | string | ID of the from company. | False |
| FromUserID | string | ID of the from user. | False |
| BillingAddressID | string | ID of the billing address. | False |
| BillingAddress | object | Billing address of the order. | False |
| ShippingAddressID | string | ID of the Shipping Address for all LineItems on the Order. Null when there are multiple Shipping Addresses involved. | False |
| Comments | string | Comments of the order. | False |
| LineItemCount | integer | Line item count of the order. | False |
| Status | string | Status of the order. Possible values: Unsubmitted, AwaitingApproval, Declined, Open, Completed, Canceled. | False |
| DateCreated | date | Date created of the order. | False |
| DateSubmitted | date | Date submitted of the order. | False |
| DateApproved | date | Date approved of the order. | False |
| DateDeclined | date | Date declined of the order. | False |
| DateCanceled | date | Date canceled of the order. | False |
| DateCompleted | date | Date completed of the order. | False |
| Subtotal | float | Subtotal of the order. | False |
| ShippingCost | float | Shipping cost of the order. | False |
| TaxCost | float | Tax cost of the order. | False |
| PromotionDiscount | float | Promotion discount of the order. | False |
| Total | float | Total of the order. | False |
| IsSubmitted | boolean | True if this Order has been passed from the Buyer to the Seller. | False |
| xp | object | Container for extended (custom) properties of the order. | False |

## `GET` `v1/orders/{direction}`
Get a list of orders

| Name | Type | Description | Required | 
|---|---|---|---|
| direction | string | Direction of the order, from the current user's perspective. Possible values: incoming, outgoing. | True |
| buyerID | string | ID of the buyer. | False |
| supplierID | string | ID of the supplier. | False |
| from | date | Lower bound of date range that the order was created. | False |
| to | date | Upper bound of date range that the order was created. | False |
| search | string | Word or phrase to search for. | False |
| searchOn | string | Comma-delimited list of fields to search on. | False |
| sortBy | string | Comma-delimited list of fields to sort by. | False |
| page | integer | Page of results to return. Default: 1 | False |
| pageSize | integer | Number of results to return per page. Default: 20, max: 100. | False |
| filters | object | Any additional key/value pairs passed in the query string are interpretted as filters. Valid keys are top-level properties of the returned model or 'xp.???' | False |

## Response Body
	{
	    "Items": [
	        {
	            "BillingAddress": {
	                "AddressName": "",
	                "City": "",
	                "CompanyName": "",
	                "Country": "",
	                "DateCreated": "2018-03-21T23:00:00+00:00",
	                "FirstName": "",
	                "ID": "",
	                "LastName": "",
	                "Phone": "",
	                "State": "",
	                "Street1": "",
	                "Street2": "",
	                "Zip": "",
	                "xp": {}
	            },
	            "BillingAddressID": "",
	            "Comments": "",
	            "DateApproved": "2018-03-21T23:00:00+00:00",
	            "DateCanceled": "2018-03-21T23:00:00+00:00",
	            "DateCompleted": "2018-03-21T23:00:00+00:00",
	            "DateCreated": "2018-03-21T23:00:00+00:00",
	            "DateDeclined": "2018-03-21T23:00:00+00:00",
	            "DateSubmitted": "2018-03-21T23:00:00+00:00",
	            "FromCompanyID": "",
	            "FromUser": {
	                "Active": false,
	                "AvailableRoles": [
	                    ""
	                ],
	                "Email": "",
	                "FirstName": "",
	                "ID": "",
	                "LastName": "",
	                "Phone": "",
	                "TermsAccepted": "2018-03-21T23:00:00+00:00",
	                "Username": "",
	                "xp": {}
	            },
	            "FromUserID": "",
	            "ID": "",
	            "IsSubmitted": false,
	            "LineItemCount": 0,
	            "PromotionDiscount": 0,
	            "ShippingAddressID": "",
	            "ShippingCost": 0,
	            "Status": "Unsubmitted",
	            "Subtotal": 0,
	            "TaxCost": 0,
	            "Total": 0,
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
| ID | string | ID of the order. | False |
| FromUser | object | From user of the order. | False |
| FromCompanyID | string | ID of the from company. | False |
| FromUserID | string | ID of the from user. | False |
| BillingAddressID | string | ID of the billing address. | False |
| BillingAddress | object | Billing address of the order. | False |
| ShippingAddressID | string | ID of the Shipping Address for all LineItems on the Order. Null when there are multiple Shipping Addresses involved. | False |
| Comments | string | Comments of the order. | False |
| LineItemCount | integer | Line item count of the order. | False |
| Status | string | Status of the order. Possible values: Unsubmitted, AwaitingApproval, Declined, Open, Completed, Canceled. | False |
| DateCreated | date | Date created of the order. | False |
| DateSubmitted | date | Date submitted of the order. | False |
| DateApproved | date | Date approved of the order. | False |
| DateDeclined | date | Date declined of the order. | False |
| DateCanceled | date | Date canceled of the order. | False |
| DateCompleted | date | Date completed of the order. | False |
| Subtotal | float | Subtotal of the order. | False |
| ShippingCost | float | Shipping cost of the order. | False |
| TaxCost | float | Tax cost of the order. | False |
| PromotionDiscount | float | Promotion discount of the order. | False |
| Total | float | Total of the order. | False |
| IsSubmitted | boolean | True if this Order has been passed from the Buyer to the Seller. | False |
| xp | object | Container for extended (custom) properties of the order. | False |

## `POST` `v1/orders/{direction}`
Create a new order

| Name | Type | Description | Required | 
|---|---|---|---|
| direction | string | Direction of the order, from the current user's perspective. Possible values: incoming, outgoing. | True |

## Request Body
	{
	    "BillingAddressID": "",
	    "Comments": "",
	    "FromCompanyID": "",
	    "FromUserID": "",
	    "ID": "",
	    "ShippingAddressID": "",
	    "ShippingCost": 0,
	    "TaxCost": 0,
	    "xp": {}
	}
| Name | Type | Description | Required | 
|---|---|---|---|
| ID | string | ID of the order. Can only contain characters Aa-Zz, 0-9, -, and _. Searchable: priority level 1. Sortable. | False |
| FromCompanyID | string | ID of the from company. Searchable: priority level 2. Sortable. | False |
| FromUserID | string | ID of the from user. Sortable. | False |
| BillingAddressID | string | ID of the billing address. | False |
| ShippingAddressID | string | ID of the Shipping Address for all LineItems on the Order. Null when there are multiple Shipping Addresses involved. | False |
| Comments | string | Comments of the order. Max length 2000 characters. Searchable: priority level 4. | False |
| ShippingCost | float | Shipping cost of the order. Sortable. | False |
| TaxCost | float | Tax cost of the order. Sortable. | False |
| xp | object | Container for extended (custom) properties of the order. | False |

## Response Body
	{
	    "BillingAddress": {
	        "AddressName": "",
	        "City": "",
	        "CompanyName": "",
	        "Country": "",
	        "DateCreated": "2018-03-21T23:00:00+00:00",
	        "FirstName": "",
	        "ID": "",
	        "LastName": "",
	        "Phone": "",
	        "State": "",
	        "Street1": "",
	        "Street2": "",
	        "Zip": "",
	        "xp": {}
	    },
	    "BillingAddressID": "",
	    "Comments": "",
	    "DateApproved": "2018-03-21T23:00:00+00:00",
	    "DateCanceled": "2018-03-21T23:00:00+00:00",
	    "DateCompleted": "2018-03-21T23:00:00+00:00",
	    "DateCreated": "2018-03-21T23:00:00+00:00",
	    "DateDeclined": "2018-03-21T23:00:00+00:00",
	    "DateSubmitted": "2018-03-21T23:00:00+00:00",
	    "FromCompanyID": "",
	    "FromUser": {
	        "Active": false,
	        "AvailableRoles": [
	            ""
	        ],
	        "Email": "",
	        "FirstName": "",
	        "ID": "",
	        "LastName": "",
	        "Phone": "",
	        "TermsAccepted": "2018-03-21T23:00:00+00:00",
	        "Username": "",
	        "xp": {}
	    },
	    "FromUserID": "",
	    "ID": "",
	    "IsSubmitted": false,
	    "LineItemCount": 0,
	    "PromotionDiscount": 0,
	    "ShippingAddressID": "",
	    "ShippingCost": 0,
	    "Status": "Unsubmitted",
	    "Subtotal": 0,
	    "TaxCost": 0,
	    "Total": 0,
	    "xp": {}
	}
| Name | Type | Description | Required | 
|---|---|---|---|
| ID | string | ID of the order. | False |
| FromUser | object | From user of the order. | False |
| FromCompanyID | string | ID of the from company. | False |
| FromUserID | string | ID of the from user. | False |
| BillingAddressID | string | ID of the billing address. | False |
| BillingAddress | object | Billing address of the order. | False |
| ShippingAddressID | string | ID of the Shipping Address for all LineItems on the Order. Null when there are multiple Shipping Addresses involved. | False |
| Comments | string | Comments of the order. | False |
| LineItemCount | integer | Line item count of the order. | False |
| Status | string | Status of the order. Possible values: Unsubmitted, AwaitingApproval, Declined, Open, Completed, Canceled. | False |
| DateCreated | date | Date created of the order. | False |
| DateSubmitted | date | Date submitted of the order. | False |
| DateApproved | date | Date approved of the order. | False |
| DateDeclined | date | Date declined of the order. | False |
| DateCanceled | date | Date canceled of the order. | False |
| DateCompleted | date | Date completed of the order. | False |
| Subtotal | float | Subtotal of the order. | False |
| ShippingCost | float | Shipping cost of the order. | False |
| TaxCost | float | Tax cost of the order. | False |
| PromotionDiscount | float | Promotion discount of the order. | False |
| Total | float | Total of the order. | False |
| IsSubmitted | boolean | True if this Order has been passed from the Buyer to the Seller. | False |
| xp | object | Container for extended (custom) properties of the order. | False |

## `PUT` `v1/orders/{direction}/{orderID}`
Create or update an order

| Name | Type | Description | Required | 
|---|---|---|---|
| direction | string | Direction of the order, from the current user's perspective. Possible values: incoming, outgoing. | True |
| orderID | string | ID of the order. | True |

## Request Body
	{
	    "BillingAddressID": "",
	    "Comments": "",
	    "FromCompanyID": "",
	    "FromUserID": "",
	    "ID": "",
	    "ShippingAddressID": "",
	    "ShippingCost": 0,
	    "TaxCost": 0,
	    "xp": {}
	}
| Name | Type | Description | Required | 
|---|---|---|---|
| ID | string | ID of the order. Can only contain characters Aa-Zz, 0-9, -, and _. Searchable: priority level 1. Sortable. | False |
| FromCompanyID | string | ID of the from company. Searchable: priority level 2. Sortable. | False |
| FromUserID | string | ID of the from user. Sortable. | False |
| BillingAddressID | string | ID of the billing address. | False |
| ShippingAddressID | string | ID of the Shipping Address for all LineItems on the Order. Null when there are multiple Shipping Addresses involved. | False |
| Comments | string | Comments of the order. Max length 2000 characters. Searchable: priority level 4. | False |
| ShippingCost | float | Shipping cost of the order. Sortable. | False |
| TaxCost | float | Tax cost of the order. Sortable. | False |
| xp | object | Container for extended (custom) properties of the order. | False |

## Response Body
	{
	    "BillingAddress": {
	        "AddressName": "",
	        "City": "",
	        "CompanyName": "",
	        "Country": "",
	        "DateCreated": "2018-03-21T23:00:00+00:00",
	        "FirstName": "",
	        "ID": "",
	        "LastName": "",
	        "Phone": "",
	        "State": "",
	        "Street1": "",
	        "Street2": "",
	        "Zip": "",
	        "xp": {}
	    },
	    "BillingAddressID": "",
	    "Comments": "",
	    "DateApproved": "2018-03-21T23:00:00+00:00",
	    "DateCanceled": "2018-03-21T23:00:00+00:00",
	    "DateCompleted": "2018-03-21T23:00:00+00:00",
	    "DateCreated": "2018-03-21T23:00:00+00:00",
	    "DateDeclined": "2018-03-21T23:00:00+00:00",
	    "DateSubmitted": "2018-03-21T23:00:00+00:00",
	    "FromCompanyID": "",
	    "FromUser": {
	        "Active": false,
	        "AvailableRoles": [
	            ""
	        ],
	        "Email": "",
	        "FirstName": "",
	        "ID": "",
	        "LastName": "",
	        "Phone": "",
	        "TermsAccepted": "2018-03-21T23:00:00+00:00",
	        "Username": "",
	        "xp": {}
	    },
	    "FromUserID": "",
	    "ID": "",
	    "IsSubmitted": false,
	    "LineItemCount": 0,
	    "PromotionDiscount": 0,
	    "ShippingAddressID": "",
	    "ShippingCost": 0,
	    "Status": "Unsubmitted",
	    "Subtotal": 0,
	    "TaxCost": 0,
	    "Total": 0,
	    "xp": {}
	}
| Name | Type | Description | Required | 
|---|---|---|---|
| ID | string | ID of the order. | False |
| FromUser | object | From user of the order. | False |
| FromCompanyID | string | ID of the from company. | False |
| FromUserID | string | ID of the from user. | False |
| BillingAddressID | string | ID of the billing address. | False |
| BillingAddress | object | Billing address of the order. | False |
| ShippingAddressID | string | ID of the Shipping Address for all LineItems on the Order. Null when there are multiple Shipping Addresses involved. | False |
| Comments | string | Comments of the order. | False |
| LineItemCount | integer | Line item count of the order. | False |
| Status | string | Status of the order. Possible values: Unsubmitted, AwaitingApproval, Declined, Open, Completed, Canceled. | False |
| DateCreated | date | Date created of the order. | False |
| DateSubmitted | date | Date submitted of the order. | False |
| DateApproved | date | Date approved of the order. | False |
| DateDeclined | date | Date declined of the order. | False |
| DateCanceled | date | Date canceled of the order. | False |
| DateCompleted | date | Date completed of the order. | False |
| Subtotal | float | Subtotal of the order. | False |
| ShippingCost | float | Shipping cost of the order. | False |
| TaxCost | float | Tax cost of the order. | False |
| PromotionDiscount | float | Promotion discount of the order. | False |
| Total | float | Total of the order. | False |
| IsSubmitted | boolean | True if this Order has been passed from the Buyer to the Seller. | False |
| xp | object | Container for extended (custom) properties of the order. | False |

## `DELETE` `v1/orders/{direction}/{orderID}`
Delete an order

| Name | Type | Description | Required | 
|---|---|---|---|
| direction | string | Direction of the order, from the current user's perspective. Possible values: incoming, outgoing. | True |
| orderID | string | ID of the order. | True |

## Response Body
## `GET` `v1/orders/{direction}/{orderID}/approvals`
Get a list of order approvals

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
	{
	    "Items": [
	        {
	            "ApprovalRuleID": "",
	            "Approver": {
	                "Active": false,
	                "AvailableRoles": [
	                    ""
	                ],
	                "Email": "",
	                "FirstName": "",
	                "ID": "",
	                "LastName": "",
	                "Phone": "",
	                "TermsAccepted": "2018-03-21T23:00:00+00:00",
	                "Username": "",
	                "xp": {}
	            },
	            "ApprovingGroupID": "",
	            "Comments": "",
	            "DateCompleted": "2018-03-21T23:00:00+00:00",
	            "DateCreated": "2018-03-21T23:00:00+00:00",
	            "Status": "Pending"
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
| ApprovalRuleID | string | ID of the approval rule. | False |
| ApprovingGroupID | string | ID of the approving group. | False |
| Status | string | Status of the order approval. Possible values: Pending, Approved, Declined. | False |
| DateCreated | date | Date created of the order approval. | False |
| DateCompleted | date | Date completed of the order approval. | False |
| Approver | object | Approver of the order approval. | False |
| Comments | string | Comments of the order approval. | False |

## `GET` `v1/orders/{direction}/{orderID}/eligibleapprovers`
Get a list of order eligible approvers

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
	{
	    "Items": [
	        {
	            "Active": false,
	            "AvailableRoles": [
	                ""
	            ],
	            "Email": "",
	            "FirstName": "",
	            "ID": "",
	            "LastName": "",
	            "Phone": "",
	            "TermsAccepted": "2018-03-21T23:00:00+00:00",
	            "Username": "",
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
| ID | string | ID of the user. | False |
| Username | string | Username of the user. | True |
| FirstName | string | First name of the user. | True |
| LastName | string | Last name of the user. | True |
| Email | string | Email of the user. | True |
| Phone | string | Phone of the user. | False |
| TermsAccepted | date | Terms accepted of the user. | False |
| Active | boolean | Active of the user. | True |
| xp | object | Container for extended (custom) properties of the user. | False |
| AvailableRoles | array | Available roles of the user. | False |

## `PATCH` `v1/orders/{direction}/{orderID}`
Partially update an order

| Name | Type | Description | Required | 
|---|---|---|---|
| direction | string | Direction of the order, from the current user's perspective. Possible values: incoming, outgoing. | True |
| orderID | string | ID of the order. | True |

## Request Body
	{
	    "BillingAddressID": "",
	    "Comments": "",
	    "FromCompanyID": "",
	    "FromUserID": "",
	    "ID": "",
	    "ShippingAddressID": "",
	    "ShippingCost": 0,
	    "TaxCost": 0,
	    "xp": {}
	}
| Name | Type | Description | Required | 
|---|---|---|---|
| ID | string | ID of the order. Can only contain characters Aa-Zz, 0-9, -, and _. Searchable: priority level 1. Sortable. | False |
| FromCompanyID | string | ID of the from company. Searchable: priority level 2. Sortable. | False |
| FromUserID | string | ID of the from user. Sortable. | False |
| BillingAddressID | string | ID of the billing address. | False |
| ShippingAddressID | string | ID of the Shipping Address for all LineItems on the Order. Null when there are multiple Shipping Addresses involved. | False |
| Comments | string | Comments of the order. Max length 2000 characters. Searchable: priority level 4. | False |
| ShippingCost | float | Shipping cost of the order. Sortable. | False |
| TaxCost | float | Tax cost of the order. Sortable. | False |
| xp | object | Container for extended (custom) properties of the order. | False |

## Response Body
	{
	    "BillingAddress": {
	        "AddressName": "",
	        "City": "",
	        "CompanyName": "",
	        "Country": "",
	        "DateCreated": "2018-03-21T23:00:00+00:00",
	        "FirstName": "",
	        "ID": "",
	        "LastName": "",
	        "Phone": "",
	        "State": "",
	        "Street1": "",
	        "Street2": "",
	        "Zip": "",
	        "xp": {}
	    },
	    "BillingAddressID": "",
	    "Comments": "",
	    "DateApproved": "2018-03-21T23:00:00+00:00",
	    "DateCanceled": "2018-03-21T23:00:00+00:00",
	    "DateCompleted": "2018-03-21T23:00:00+00:00",
	    "DateCreated": "2018-03-21T23:00:00+00:00",
	    "DateDeclined": "2018-03-21T23:00:00+00:00",
	    "DateSubmitted": "2018-03-21T23:00:00+00:00",
	    "FromCompanyID": "",
	    "FromUser": {
	        "Active": false,
	        "AvailableRoles": [
	            ""
	        ],
	        "Email": "",
	        "FirstName": "",
	        "ID": "",
	        "LastName": "",
	        "Phone": "",
	        "TermsAccepted": "2018-03-21T23:00:00+00:00",
	        "Username": "",
	        "xp": {}
	    },
	    "FromUserID": "",
	    "ID": "",
	    "IsSubmitted": false,
	    "LineItemCount": 0,
	    "PromotionDiscount": 0,
	    "ShippingAddressID": "",
	    "ShippingCost": 0,
	    "Status": "Unsubmitted",
	    "Subtotal": 0,
	    "TaxCost": 0,
	    "Total": 0,
	    "xp": {}
	}
| Name | Type | Description | Required | 
|---|---|---|---|
| ID | string | ID of the order. | False |
| FromUser | object | From user of the order. | False |
| FromCompanyID | string | ID of the from company. | False |
| FromUserID | string | ID of the from user. | False |
| BillingAddressID | string | ID of the billing address. | False |
| BillingAddress | object | Billing address of the order. | False |
| ShippingAddressID | string | ID of the Shipping Address for all LineItems on the Order. Null when there are multiple Shipping Addresses involved. | False |
| Comments | string | Comments of the order. | False |
| LineItemCount | integer | Line item count of the order. | False |
| Status | string | Status of the order. Possible values: Unsubmitted, AwaitingApproval, Declined, Open, Completed, Canceled. | False |
| DateCreated | date | Date created of the order. | False |
| DateSubmitted | date | Date submitted of the order. | False |
| DateApproved | date | Date approved of the order. | False |
| DateDeclined | date | Date declined of the order. | False |
| DateCanceled | date | Date canceled of the order. | False |
| DateCompleted | date | Date completed of the order. | False |
| Subtotal | float | Subtotal of the order. | False |
| ShippingCost | float | Shipping cost of the order. | False |
| TaxCost | float | Tax cost of the order. | False |
| PromotionDiscount | float | Promotion discount of the order. | False |
| Total | float | Total of the order. | False |
| IsSubmitted | boolean | True if this Order has been passed from the Buyer to the Seller. | False |
| xp | object | Container for extended (custom) properties of the order. | False |

## `POST` `v1/orders/{direction}/{orderID}/submit`
Submit an order submit

| Name | Type | Description | Required | 
|---|---|---|---|
| direction | string | Direction of the order, from the current user's perspective. Possible values: incoming, outgoing. | True |
| orderID | string | ID of the order. | True |

## Response Body
	{
	    "BillingAddress": {
	        "AddressName": "",
	        "City": "",
	        "CompanyName": "",
	        "Country": "",
	        "DateCreated": "2018-03-21T23:00:00+00:00",
	        "FirstName": "",
	        "ID": "",
	        "LastName": "",
	        "Phone": "",
	        "State": "",
	        "Street1": "",
	        "Street2": "",
	        "Zip": "",
	        "xp": {}
	    },
	    "BillingAddressID": "",
	    "Comments": "",
	    "DateApproved": "2018-03-21T23:00:00+00:00",
	    "DateCanceled": "2018-03-21T23:00:00+00:00",
	    "DateCompleted": "2018-03-21T23:00:00+00:00",
	    "DateCreated": "2018-03-21T23:00:00+00:00",
	    "DateDeclined": "2018-03-21T23:00:00+00:00",
	    "DateSubmitted": "2018-03-21T23:00:00+00:00",
	    "FromCompanyID": "",
	    "FromUser": {
	        "Active": false,
	        "AvailableRoles": [
	            ""
	        ],
	        "Email": "",
	        "FirstName": "",
	        "ID": "",
	        "LastName": "",
	        "Phone": "",
	        "TermsAccepted": "2018-03-21T23:00:00+00:00",
	        "Username": "",
	        "xp": {}
	    },
	    "FromUserID": "",
	    "ID": "",
	    "IsSubmitted": false,
	    "LineItemCount": 0,
	    "PromotionDiscount": 0,
	    "ShippingAddressID": "",
	    "ShippingCost": 0,
	    "Status": "Unsubmitted",
	    "Subtotal": 0,
	    "TaxCost": 0,
	    "Total": 0,
	    "xp": {}
	}
| Name | Type | Description | Required | 
|---|---|---|---|
| ID | string | ID of the order. | False |
| FromUser | object | From user of the order. | False |
| FromCompanyID | string | ID of the from company. | False |
| FromUserID | string | ID of the from user. | False |
| BillingAddressID | string | ID of the billing address. | False |
| BillingAddress | object | Billing address of the order. | False |
| ShippingAddressID | string | ID of the Shipping Address for all LineItems on the Order. Null when there are multiple Shipping Addresses involved. | False |
| Comments | string | Comments of the order. | False |
| LineItemCount | integer | Line item count of the order. | False |
| Status | string | Status of the order. Possible values: Unsubmitted, AwaitingApproval, Declined, Open, Completed, Canceled. | False |
| DateCreated | date | Date created of the order. | False |
| DateSubmitted | date | Date submitted of the order. | False |
| DateApproved | date | Date approved of the order. | False |
| DateDeclined | date | Date declined of the order. | False |
| DateCanceled | date | Date canceled of the order. | False |
| DateCompleted | date | Date completed of the order. | False |
| Subtotal | float | Subtotal of the order. | False |
| ShippingCost | float | Shipping cost of the order. | False |
| TaxCost | float | Tax cost of the order. | False |
| PromotionDiscount | float | Promotion discount of the order. | False |
| Total | float | Total of the order. | False |
| IsSubmitted | boolean | True if this Order has been passed from the Buyer to the Seller. | False |
| xp | object | Container for extended (custom) properties of the order. | False |

## `POST` `v1/orders/{direction}/{orderID}/approve`
Approve an order approve

| Name | Type | Description | Required | 
|---|---|---|---|
| direction | string | Direction of the order, from the current user's perspective. Possible values: incoming, outgoing. | True |
| orderID | string | ID of the order. | True |

## Request Body
	{
	    "AllowResubmit": false,
	    "Comments": ""
	}
| Name | Type | Description | Required | 
|---|---|---|---|
| Comments | string | Comments of the order approval info. Max length 2000 characters. | False |
| AllowResubmit | boolean | Allow resubmit of the order approval info. | False |

## Response Body
	{
	    "BillingAddress": {
	        "AddressName": "",
	        "City": "",
	        "CompanyName": "",
	        "Country": "",
	        "DateCreated": "2018-03-21T23:00:00+00:00",
	        "FirstName": "",
	        "ID": "",
	        "LastName": "",
	        "Phone": "",
	        "State": "",
	        "Street1": "",
	        "Street2": "",
	        "Zip": "",
	        "xp": {}
	    },
	    "BillingAddressID": "",
	    "Comments": "",
	    "DateApproved": "2018-03-21T23:00:00+00:00",
	    "DateCanceled": "2018-03-21T23:00:00+00:00",
	    "DateCompleted": "2018-03-21T23:00:00+00:00",
	    "DateCreated": "2018-03-21T23:00:00+00:00",
	    "DateDeclined": "2018-03-21T23:00:00+00:00",
	    "DateSubmitted": "2018-03-21T23:00:00+00:00",
	    "FromCompanyID": "",
	    "FromUser": {
	        "Active": false,
	        "AvailableRoles": [
	            ""
	        ],
	        "Email": "",
	        "FirstName": "",
	        "ID": "",
	        "LastName": "",
	        "Phone": "",
	        "TermsAccepted": "2018-03-21T23:00:00+00:00",
	        "Username": "",
	        "xp": {}
	    },
	    "FromUserID": "",
	    "ID": "",
	    "IsSubmitted": false,
	    "LineItemCount": 0,
	    "PromotionDiscount": 0,
	    "ShippingAddressID": "",
	    "ShippingCost": 0,
	    "Status": "Unsubmitted",
	    "Subtotal": 0,
	    "TaxCost": 0,
	    "Total": 0,
	    "xp": {}
	}
| Name | Type | Description | Required | 
|---|---|---|---|
| ID | string | ID of the order. | False |
| FromUser | object | From user of the order. | False |
| FromCompanyID | string | ID of the from company. | False |
| FromUserID | string | ID of the from user. | False |
| BillingAddressID | string | ID of the billing address. | False |
| BillingAddress | object | Billing address of the order. | False |
| ShippingAddressID | string | ID of the Shipping Address for all LineItems on the Order. Null when there are multiple Shipping Addresses involved. | False |
| Comments | string | Comments of the order. | False |
| LineItemCount | integer | Line item count of the order. | False |
| Status | string | Status of the order. Possible values: Unsubmitted, AwaitingApproval, Declined, Open, Completed, Canceled. | False |
| DateCreated | date | Date created of the order. | False |
| DateSubmitted | date | Date submitted of the order. | False |
| DateApproved | date | Date approved of the order. | False |
| DateDeclined | date | Date declined of the order. | False |
| DateCanceled | date | Date canceled of the order. | False |
| DateCompleted | date | Date completed of the order. | False |
| Subtotal | float | Subtotal of the order. | False |
| ShippingCost | float | Shipping cost of the order. | False |
| TaxCost | float | Tax cost of the order. | False |
| PromotionDiscount | float | Promotion discount of the order. | False |
| Total | float | Total of the order. | False |
| IsSubmitted | boolean | True if this Order has been passed from the Buyer to the Seller. | False |
| xp | object | Container for extended (custom) properties of the order. | False |

## `POST` `v1/orders/{direction}/{orderID}/decline`
Decline an order decline

| Name | Type | Description | Required | 
|---|---|---|---|
| direction | string | Direction of the order, from the current user's perspective. Possible values: incoming, outgoing. | True |
| orderID | string | ID of the order. | True |

## Request Body
	{
	    "AllowResubmit": false,
	    "Comments": ""
	}
| Name | Type | Description | Required | 
|---|---|---|---|
| Comments | string | Comments of the order approval info. Max length 2000 characters. | False |
| AllowResubmit | boolean | Allow resubmit of the order approval info. | False |

## Response Body
	{
	    "BillingAddress": {
	        "AddressName": "",
	        "City": "",
	        "CompanyName": "",
	        "Country": "",
	        "DateCreated": "2018-03-21T23:00:00+00:00",
	        "FirstName": "",
	        "ID": "",
	        "LastName": "",
	        "Phone": "",
	        "State": "",
	        "Street1": "",
	        "Street2": "",
	        "Zip": "",
	        "xp": {}
	    },
	    "BillingAddressID": "",
	    "Comments": "",
	    "DateApproved": "2018-03-21T23:00:00+00:00",
	    "DateCanceled": "2018-03-21T23:00:00+00:00",
	    "DateCompleted": "2018-03-21T23:00:00+00:00",
	    "DateCreated": "2018-03-21T23:00:00+00:00",
	    "DateDeclined": "2018-03-21T23:00:00+00:00",
	    "DateSubmitted": "2018-03-21T23:00:00+00:00",
	    "FromCompanyID": "",
	    "FromUser": {
	        "Active": false,
	        "AvailableRoles": [
	            ""
	        ],
	        "Email": "",
	        "FirstName": "",
	        "ID": "",
	        "LastName": "",
	        "Phone": "",
	        "TermsAccepted": "2018-03-21T23:00:00+00:00",
	        "Username": "",
	        "xp": {}
	    },
	    "FromUserID": "",
	    "ID": "",
	    "IsSubmitted": false,
	    "LineItemCount": 0,
	    "PromotionDiscount": 0,
	    "ShippingAddressID": "",
	    "ShippingCost": 0,
	    "Status": "Unsubmitted",
	    "Subtotal": 0,
	    "TaxCost": 0,
	    "Total": 0,
	    "xp": {}
	}
| Name | Type | Description | Required | 
|---|---|---|---|
| ID | string | ID of the order. | False |
| FromUser | object | From user of the order. | False |
| FromCompanyID | string | ID of the from company. | False |
| FromUserID | string | ID of the from user. | False |
| BillingAddressID | string | ID of the billing address. | False |
| BillingAddress | object | Billing address of the order. | False |
| ShippingAddressID | string | ID of the Shipping Address for all LineItems on the Order. Null when there are multiple Shipping Addresses involved. | False |
| Comments | string | Comments of the order. | False |
| LineItemCount | integer | Line item count of the order. | False |
| Status | string | Status of the order. Possible values: Unsubmitted, AwaitingApproval, Declined, Open, Completed, Canceled. | False |
| DateCreated | date | Date created of the order. | False |
| DateSubmitted | date | Date submitted of the order. | False |
| DateApproved | date | Date approved of the order. | False |
| DateDeclined | date | Date declined of the order. | False |
| DateCanceled | date | Date canceled of the order. | False |
| DateCompleted | date | Date completed of the order. | False |
| Subtotal | float | Subtotal of the order. | False |
| ShippingCost | float | Shipping cost of the order. | False |
| TaxCost | float | Tax cost of the order. | False |
| PromotionDiscount | float | Promotion discount of the order. | False |
| Total | float | Total of the order. | False |
| IsSubmitted | boolean | True if this Order has been passed from the Buyer to the Seller. | False |
| xp | object | Container for extended (custom) properties of the order. | False |

## `POST` `v1/orders/{direction}/{orderID}/cancel`
Cancel an order cancel

| Name | Type | Description | Required | 
|---|---|---|---|
| direction | string | Direction of the order, from the current user's perspective. Possible values: incoming, outgoing. | True |
| orderID | string | ID of the order. | True |

## Response Body
	{
	    "BillingAddress": {
	        "AddressName": "",
	        "City": "",
	        "CompanyName": "",
	        "Country": "",
	        "DateCreated": "2018-03-21T23:00:00+00:00",
	        "FirstName": "",
	        "ID": "",
	        "LastName": "",
	        "Phone": "",
	        "State": "",
	        "Street1": "",
	        "Street2": "",
	        "Zip": "",
	        "xp": {}
	    },
	    "BillingAddressID": "",
	    "Comments": "",
	    "DateApproved": "2018-03-21T23:00:00+00:00",
	    "DateCanceled": "2018-03-21T23:00:00+00:00",
	    "DateCompleted": "2018-03-21T23:00:00+00:00",
	    "DateCreated": "2018-03-21T23:00:00+00:00",
	    "DateDeclined": "2018-03-21T23:00:00+00:00",
	    "DateSubmitted": "2018-03-21T23:00:00+00:00",
	    "FromCompanyID": "",
	    "FromUser": {
	        "Active": false,
	        "AvailableRoles": [
	            ""
	        ],
	        "Email": "",
	        "FirstName": "",
	        "ID": "",
	        "LastName": "",
	        "Phone": "",
	        "TermsAccepted": "2018-03-21T23:00:00+00:00",
	        "Username": "",
	        "xp": {}
	    },
	    "FromUserID": "",
	    "ID": "",
	    "IsSubmitted": false,
	    "LineItemCount": 0,
	    "PromotionDiscount": 0,
	    "ShippingAddressID": "",
	    "ShippingCost": 0,
	    "Status": "Unsubmitted",
	    "Subtotal": 0,
	    "TaxCost": 0,
	    "Total": 0,
	    "xp": {}
	}
| Name | Type | Description | Required | 
|---|---|---|---|
| ID | string | ID of the order. | False |
| FromUser | object | From user of the order. | False |
| FromCompanyID | string | ID of the from company. | False |
| FromUserID | string | ID of the from user. | False |
| BillingAddressID | string | ID of the billing address. | False |
| BillingAddress | object | Billing address of the order. | False |
| ShippingAddressID | string | ID of the Shipping Address for all LineItems on the Order. Null when there are multiple Shipping Addresses involved. | False |
| Comments | string | Comments of the order. | False |
| LineItemCount | integer | Line item count of the order. | False |
| Status | string | Status of the order. Possible values: Unsubmitted, AwaitingApproval, Declined, Open, Completed, Canceled. | False |
| DateCreated | date | Date created of the order. | False |
| DateSubmitted | date | Date submitted of the order. | False |
| DateApproved | date | Date approved of the order. | False |
| DateDeclined | date | Date declined of the order. | False |
| DateCanceled | date | Date canceled of the order. | False |
| DateCompleted | date | Date completed of the order. | False |
| Subtotal | float | Subtotal of the order. | False |
| ShippingCost | float | Shipping cost of the order. | False |
| TaxCost | float | Tax cost of the order. | False |
| PromotionDiscount | float | Promotion discount of the order. | False |
| Total | float | Total of the order. | False |
| IsSubmitted | boolean | True if this Order has been passed from the Buyer to the Seller. | False |
| xp | object | Container for extended (custom) properties of the order. | False |

## `POST` `v1/orders/{direction}/{orderID}/ship`
Ship an order ship

| Name | Type | Description | Required | 
|---|---|---|---|
| direction | string | Direction of the order, from the current user's perspective. Possible values: incoming, outgoing. | True |
| orderID | string | ID of the order. | True |

## Request Body
	{
	    "Account": "",
	    "BuyerID": "",
	    "Cost": 0,
	    "DateDelivered": "2018-03-21T23:00:00+00:00",
	    "DateShipped": "2018-03-21T23:00:00+00:00",
	    "FromAddressID": "",
	    "ID": "",
	    "Shipper": "",
	    "ToAddressID": "",
	    "TrackingNumber": "",
	    "xp": {}
	}
| Name | Type | Description | Required | 
|---|---|---|---|
| ID | string | ID of the shipment. Can only contain characters Aa-Zz, 0-9, -, and _. Searchable: priority level 1. Sortable. | False |
| BuyerID | string | ID of the buyer. Searchable: priority level 1. Sortable. | False |
| Shipper | string | Shipper of the shipment. Searchable: priority level 2. Sortable. | False |
| DateShipped | date | Date shipped of the shipment. Searchable: priority level 3. Sortable: priority level 1. | False |
| DateDelivered | date | Date delivered of the shipment. Searchable: priority level 4. Sortable. | False |
| TrackingNumber | string | Tracking number of the shipment. Max length 3000 characters. Searchable: priority level 4. | False |
| Cost | float | Cost of the shipment. Sortable. | False |
| xp | object | Container for extended (custom) properties of the shipment. | False |
| Account | string | Account of the shipment. | False |
| FromAddressID | string | ID of the from address. | False |
| ToAddressID | string | ID of the to address. | False |

## Response Body
	{
	    "BillingAddress": {
	        "AddressName": "",
	        "City": "",
	        "CompanyName": "",
	        "Country": "",
	        "DateCreated": "2018-03-21T23:00:00+00:00",
	        "FirstName": "",
	        "ID": "",
	        "LastName": "",
	        "Phone": "",
	        "State": "",
	        "Street1": "",
	        "Street2": "",
	        "Zip": "",
	        "xp": {}
	    },
	    "BillingAddressID": "",
	    "Comments": "",
	    "DateApproved": "2018-03-21T23:00:00+00:00",
	    "DateCanceled": "2018-03-21T23:00:00+00:00",
	    "DateCompleted": "2018-03-21T23:00:00+00:00",
	    "DateCreated": "2018-03-21T23:00:00+00:00",
	    "DateDeclined": "2018-03-21T23:00:00+00:00",
	    "DateSubmitted": "2018-03-21T23:00:00+00:00",
	    "FromCompanyID": "",
	    "FromUser": {
	        "Active": false,
	        "AvailableRoles": [
	            ""
	        ],
	        "Email": "",
	        "FirstName": "",
	        "ID": "",
	        "LastName": "",
	        "Phone": "",
	        "TermsAccepted": "2018-03-21T23:00:00+00:00",
	        "Username": "",
	        "xp": {}
	    },
	    "FromUserID": "",
	    "ID": "",
	    "IsSubmitted": false,
	    "LineItemCount": 0,
	    "PromotionDiscount": 0,
	    "ShippingAddressID": "",
	    "ShippingCost": 0,
	    "Status": "Unsubmitted",
	    "Subtotal": 0,
	    "TaxCost": 0,
	    "Total": 0,
	    "xp": {}
	}
| Name | Type | Description | Required | 
|---|---|---|---|
| ID | string | ID of the order. | False |
| FromUser | object | From user of the order. | False |
| FromCompanyID | string | ID of the from company. | False |
| FromUserID | string | ID of the from user. | False |
| BillingAddressID | string | ID of the billing address. | False |
| BillingAddress | object | Billing address of the order. | False |
| ShippingAddressID | string | ID of the Shipping Address for all LineItems on the Order. Null when there are multiple Shipping Addresses involved. | False |
| Comments | string | Comments of the order. | False |
| LineItemCount | integer | Line item count of the order. | False |
| Status | string | Status of the order. Possible values: Unsubmitted, AwaitingApproval, Declined, Open, Completed, Canceled. | False |
| DateCreated | date | Date created of the order. | False |
| DateSubmitted | date | Date submitted of the order. | False |
| DateApproved | date | Date approved of the order. | False |
| DateDeclined | date | Date declined of the order. | False |
| DateCanceled | date | Date canceled of the order. | False |
| DateCompleted | date | Date completed of the order. | False |
| Subtotal | float | Subtotal of the order. | False |
| ShippingCost | float | Shipping cost of the order. | False |
| TaxCost | float | Tax cost of the order. | False |
| PromotionDiscount | float | Promotion discount of the order. | False |
| Total | float | Total of the order. | False |
| IsSubmitted | boolean | True if this Order has been passed from the Buyer to the Seller. | False |
| xp | object | Container for extended (custom) properties of the order. | False |

## `PUT` `v1/orders/{direction}/{orderID}/shipto`
Set an shipping address

| Name | Type | Description | Required | 
|---|---|---|---|
| direction | string | Direction of the order, from the current user's perspective. Possible values: incoming, outgoing. | True |
| orderID | string | ID of the order. | True |

## Request Body
	{
	    "AddressName": "",
	    "City": "",
	    "CompanyName": "",
	    "Country": "",
	    "FirstName": "",
	    "ID": "",
	    "LastName": "",
	    "Phone": "",
	    "State": "",
	    "Street1": "",
	    "Street2": "",
	    "Zip": "",
	    "xp": {}
	}
| Name | Type | Description | Required | 
|---|---|---|---|
| ID | string | ID of the address. Can only contain characters Aa-Zz, 0-9, -, and _. Searchable: priority level 1. Sortable: priority level 2. | False |
| CompanyName | string | Company name of the address. Max length 100 characters. Sortable. | False |
| FirstName | string | First name of the address. Max length 100 characters. Searchable: priority level 7. Sortable. | False |
| LastName | string | Last name of the address. Max length 100 characters. Searchable: priority level 6. Sortable. | False |
| Street1 | string | Street 1 of the address. Required. Max length 100 characters. Searchable: priority level 4. Sortable. | True |
| Street2 | string | Street 2 of the address. Max length 100 characters. Searchable: priority level 5. Sortable. | False |
| City | string | City of the address. Required. Max length 100 characters. Searchable: priority level 3. Sortable. | True |
| State | string | State of the address. Required. Max length 100 characters. Searchable: priority level 7. Sortable. | True |
| Zip | string | Zip of the address. Required. Max length 100 characters. Searchable: priority level 6. Sortable. | True |
| Country | string | Country of the address. Required. Max length 2 characters. Sortable. | True |
| Phone | string | Phone of the address. Max length 100 characters. Sortable. | False |
| AddressName | string | Address name of the address. Max length 100 characters. Searchable: priority level 2. Sortable: priority level 1. | False |
| xp | object | Container for extended (custom) properties of the address. | False |

## Response Body
	{
	    "BillingAddress": {
	        "AddressName": "",
	        "City": "",
	        "CompanyName": "",
	        "Country": "",
	        "DateCreated": "2018-03-21T23:00:00+00:00",
	        "FirstName": "",
	        "ID": "",
	        "LastName": "",
	        "Phone": "",
	        "State": "",
	        "Street1": "",
	        "Street2": "",
	        "Zip": "",
	        "xp": {}
	    },
	    "BillingAddressID": "",
	    "Comments": "",
	    "DateApproved": "2018-03-21T23:00:00+00:00",
	    "DateCanceled": "2018-03-21T23:00:00+00:00",
	    "DateCompleted": "2018-03-21T23:00:00+00:00",
	    "DateCreated": "2018-03-21T23:00:00+00:00",
	    "DateDeclined": "2018-03-21T23:00:00+00:00",
	    "DateSubmitted": "2018-03-21T23:00:00+00:00",
	    "FromCompanyID": "",
	    "FromUser": {
	        "Active": false,
	        "AvailableRoles": [
	            ""
	        ],
	        "Email": "",
	        "FirstName": "",
	        "ID": "",
	        "LastName": "",
	        "Phone": "",
	        "TermsAccepted": "2018-03-21T23:00:00+00:00",
	        "Username": "",
	        "xp": {}
	    },
	    "FromUserID": "",
	    "ID": "",
	    "IsSubmitted": false,
	    "LineItemCount": 0,
	    "PromotionDiscount": 0,
	    "ShippingAddressID": "",
	    "ShippingCost": 0,
	    "Status": "Unsubmitted",
	    "Subtotal": 0,
	    "TaxCost": 0,
	    "Total": 0,
	    "xp": {}
	}
| Name | Type | Description | Required | 
|---|---|---|---|
| ID | string | ID of the order. | False |
| FromUser | object | From user of the order. | False |
| FromCompanyID | string | ID of the from company. | False |
| FromUserID | string | ID of the from user. | False |
| BillingAddressID | string | ID of the billing address. | False |
| BillingAddress | object | Billing address of the order. | False |
| ShippingAddressID | string | ID of the Shipping Address for all LineItems on the Order. Null when there are multiple Shipping Addresses involved. | False |
| Comments | string | Comments of the order. | False |
| LineItemCount | integer | Line item count of the order. | False |
| Status | string | Status of the order. Possible values: Unsubmitted, AwaitingApproval, Declined, Open, Completed, Canceled. | False |
| DateCreated | date | Date created of the order. | False |
| DateSubmitted | date | Date submitted of the order. | False |
| DateApproved | date | Date approved of the order. | False |
| DateDeclined | date | Date declined of the order. | False |
| DateCanceled | date | Date canceled of the order. | False |
| DateCompleted | date | Date completed of the order. | False |
| Subtotal | float | Subtotal of the order. | False |
| ShippingCost | float | Shipping cost of the order. | False |
| TaxCost | float | Tax cost of the order. | False |
| PromotionDiscount | float | Promotion discount of the order. | False |
| Total | float | Total of the order. | False |
| IsSubmitted | boolean | True if this Order has been passed from the Buyer to the Seller. | False |
| xp | object | Container for extended (custom) properties of the order. | False |

## `PATCH` `v1/orders/{direction}/{orderID}/shipto`
Partially update an order shipping address

| Name | Type | Description | Required | 
|---|---|---|---|
| direction | string | Direction of the order, from the current user's perspective. Possible values: incoming, outgoing. | True |
| orderID | string | ID of the order. | True |

## Request Body
	{
	    "AddressName": "",
	    "City": "",
	    "CompanyName": "",
	    "Country": "",
	    "FirstName": "",
	    "ID": "",
	    "LastName": "",
	    "Phone": "",
	    "State": "",
	    "Street1": "",
	    "Street2": "",
	    "Zip": "",
	    "xp": {}
	}
| Name | Type | Description | Required | 
|---|---|---|---|
| ID | string | ID of the address. Can only contain characters Aa-Zz, 0-9, -, and _. Searchable: priority level 1. Sortable: priority level 2. | False |
| CompanyName | string | Company name of the address. Max length 100 characters. Sortable. | False |
| FirstName | string | First name of the address. Max length 100 characters. Searchable: priority level 7. Sortable. | False |
| LastName | string | Last name of the address. Max length 100 characters. Searchable: priority level 6. Sortable. | False |
| Street1 | string | Street 1 of the address. Required. Max length 100 characters. Searchable: priority level 4. Sortable. | True |
| Street2 | string | Street 2 of the address. Max length 100 characters. Searchable: priority level 5. Sortable. | False |
| City | string | City of the address. Required. Max length 100 characters. Searchable: priority level 3. Sortable. | True |
| State | string | State of the address. Required. Max length 100 characters. Searchable: priority level 7. Sortable. | True |
| Zip | string | Zip of the address. Required. Max length 100 characters. Searchable: priority level 6. Sortable. | True |
| Country | string | Country of the address. Required. Max length 2 characters. Sortable. | True |
| Phone | string | Phone of the address. Max length 100 characters. Sortable. | False |
| AddressName | string | Address name of the address. Max length 100 characters. Searchable: priority level 2. Sortable: priority level 1. | False |
| xp | object | Container for extended (custom) properties of the address. | False |

## Response Body
	{
	    "BillingAddress": {
	        "AddressName": "",
	        "City": "",
	        "CompanyName": "",
	        "Country": "",
	        "DateCreated": "2018-03-21T23:00:00+00:00",
	        "FirstName": "",
	        "ID": "",
	        "LastName": "",
	        "Phone": "",
	        "State": "",
	        "Street1": "",
	        "Street2": "",
	        "Zip": "",
	        "xp": {}
	    },
	    "BillingAddressID": "",
	    "Comments": "",
	    "DateApproved": "2018-03-21T23:00:00+00:00",
	    "DateCanceled": "2018-03-21T23:00:00+00:00",
	    "DateCompleted": "2018-03-21T23:00:00+00:00",
	    "DateCreated": "2018-03-21T23:00:00+00:00",
	    "DateDeclined": "2018-03-21T23:00:00+00:00",
	    "DateSubmitted": "2018-03-21T23:00:00+00:00",
	    "FromCompanyID": "",
	    "FromUser": {
	        "Active": false,
	        "AvailableRoles": [
	            ""
	        ],
	        "Email": "",
	        "FirstName": "",
	        "ID": "",
	        "LastName": "",
	        "Phone": "",
	        "TermsAccepted": "2018-03-21T23:00:00+00:00",
	        "Username": "",
	        "xp": {}
	    },
	    "FromUserID": "",
	    "ID": "",
	    "IsSubmitted": false,
	    "LineItemCount": 0,
	    "PromotionDiscount": 0,
	    "ShippingAddressID": "",
	    "ShippingCost": 0,
	    "Status": "Unsubmitted",
	    "Subtotal": 0,
	    "TaxCost": 0,
	    "Total": 0,
	    "xp": {}
	}
| Name | Type | Description | Required | 
|---|---|---|---|
| ID | string | ID of the order. | False |
| FromUser | object | From user of the order. | False |
| FromCompanyID | string | ID of the from company. | False |
| FromUserID | string | ID of the from user. | False |
| BillingAddressID | string | ID of the billing address. | False |
| BillingAddress | object | Billing address of the order. | False |
| ShippingAddressID | string | ID of the Shipping Address for all LineItems on the Order. Null when there are multiple Shipping Addresses involved. | False |
| Comments | string | Comments of the order. | False |
| LineItemCount | integer | Line item count of the order. | False |
| Status | string | Status of the order. Possible values: Unsubmitted, AwaitingApproval, Declined, Open, Completed, Canceled. | False |
| DateCreated | date | Date created of the order. | False |
| DateSubmitted | date | Date submitted of the order. | False |
| DateApproved | date | Date approved of the order. | False |
| DateDeclined | date | Date declined of the order. | False |
| DateCanceled | date | Date canceled of the order. | False |
| DateCompleted | date | Date completed of the order. | False |
| Subtotal | float | Subtotal of the order. | False |
| ShippingCost | float | Shipping cost of the order. | False |
| TaxCost | float | Tax cost of the order. | False |
| PromotionDiscount | float | Promotion discount of the order. | False |
| Total | float | Total of the order. | False |
| IsSubmitted | boolean | True if this Order has been passed from the Buyer to the Seller. | False |
| xp | object | Container for extended (custom) properties of the order. | False |

## `PUT` `v1/orders/{direction}/{orderID}/billto`
Set an billing address

| Name | Type | Description | Required | 
|---|---|---|---|
| direction | string | Direction of the order, from the current user's perspective. Possible values: incoming, outgoing. | True |
| orderID | string | ID of the order. | True |

## Request Body
	{
	    "AddressName": "",
	    "City": "",
	    "CompanyName": "",
	    "Country": "",
	    "FirstName": "",
	    "ID": "",
	    "LastName": "",
	    "Phone": "",
	    "State": "",
	    "Street1": "",
	    "Street2": "",
	    "Zip": "",
	    "xp": {}
	}
| Name | Type | Description | Required | 
|---|---|---|---|
| ID | string | ID of the address. Can only contain characters Aa-Zz, 0-9, -, and _. Searchable: priority level 1. Sortable: priority level 2. | False |
| CompanyName | string | Company name of the address. Max length 100 characters. Sortable. | False |
| FirstName | string | First name of the address. Max length 100 characters. Searchable: priority level 7. Sortable. | False |
| LastName | string | Last name of the address. Max length 100 characters. Searchable: priority level 6. Sortable. | False |
| Street1 | string | Street 1 of the address. Required. Max length 100 characters. Searchable: priority level 4. Sortable. | True |
| Street2 | string | Street 2 of the address. Max length 100 characters. Searchable: priority level 5. Sortable. | False |
| City | string | City of the address. Required. Max length 100 characters. Searchable: priority level 3. Sortable. | True |
| State | string | State of the address. Required. Max length 100 characters. Searchable: priority level 7. Sortable. | True |
| Zip | string | Zip of the address. Required. Max length 100 characters. Searchable: priority level 6. Sortable. | True |
| Country | string | Country of the address. Required. Max length 2 characters. Sortable. | True |
| Phone | string | Phone of the address. Max length 100 characters. Sortable. | False |
| AddressName | string | Address name of the address. Max length 100 characters. Searchable: priority level 2. Sortable: priority level 1. | False |
| xp | object | Container for extended (custom) properties of the address. | False |

## Response Body
	{
	    "BillingAddress": {
	        "AddressName": "",
	        "City": "",
	        "CompanyName": "",
	        "Country": "",
	        "DateCreated": "2018-03-21T23:00:00+00:00",
	        "FirstName": "",
	        "ID": "",
	        "LastName": "",
	        "Phone": "",
	        "State": "",
	        "Street1": "",
	        "Street2": "",
	        "Zip": "",
	        "xp": {}
	    },
	    "BillingAddressID": "",
	    "Comments": "",
	    "DateApproved": "2018-03-21T23:00:00+00:00",
	    "DateCanceled": "2018-03-21T23:00:00+00:00",
	    "DateCompleted": "2018-03-21T23:00:00+00:00",
	    "DateCreated": "2018-03-21T23:00:00+00:00",
	    "DateDeclined": "2018-03-21T23:00:00+00:00",
	    "DateSubmitted": "2018-03-21T23:00:00+00:00",
	    "FromCompanyID": "",
	    "FromUser": {
	        "Active": false,
	        "AvailableRoles": [
	            ""
	        ],
	        "Email": "",
	        "FirstName": "",
	        "ID": "",
	        "LastName": "",
	        "Phone": "",
	        "TermsAccepted": "2018-03-21T23:00:00+00:00",
	        "Username": "",
	        "xp": {}
	    },
	    "FromUserID": "",
	    "ID": "",
	    "IsSubmitted": false,
	    "LineItemCount": 0,
	    "PromotionDiscount": 0,
	    "ShippingAddressID": "",
	    "ShippingCost": 0,
	    "Status": "Unsubmitted",
	    "Subtotal": 0,
	    "TaxCost": 0,
	    "Total": 0,
	    "xp": {}
	}
| Name | Type | Description | Required | 
|---|---|---|---|
| ID | string | ID of the order. | False |
| FromUser | object | From user of the order. | False |
| FromCompanyID | string | ID of the from company. | False |
| FromUserID | string | ID of the from user. | False |
| BillingAddressID | string | ID of the billing address. | False |
| BillingAddress | object | Billing address of the order. | False |
| ShippingAddressID | string | ID of the Shipping Address for all LineItems on the Order. Null when there are multiple Shipping Addresses involved. | False |
| Comments | string | Comments of the order. | False |
| LineItemCount | integer | Line item count of the order. | False |
| Status | string | Status of the order. Possible values: Unsubmitted, AwaitingApproval, Declined, Open, Completed, Canceled. | False |
| DateCreated | date | Date created of the order. | False |
| DateSubmitted | date | Date submitted of the order. | False |
| DateApproved | date | Date approved of the order. | False |
| DateDeclined | date | Date declined of the order. | False |
| DateCanceled | date | Date canceled of the order. | False |
| DateCompleted | date | Date completed of the order. | False |
| Subtotal | float | Subtotal of the order. | False |
| ShippingCost | float | Shipping cost of the order. | False |
| TaxCost | float | Tax cost of the order. | False |
| PromotionDiscount | float | Promotion discount of the order. | False |
| Total | float | Total of the order. | False |
| IsSubmitted | boolean | True if this Order has been passed from the Buyer to the Seller. | False |
| xp | object | Container for extended (custom) properties of the order. | False |

## `PATCH` `v1/orders/{direction}/{orderID}/billto`
Partially update an order billing address

| Name | Type | Description | Required | 
|---|---|---|---|
| direction | string | Direction of the order, from the current user's perspective. Possible values: incoming, outgoing. | True |
| orderID | string | ID of the order. | True |

## Request Body
	{
	    "AddressName": "",
	    "City": "",
	    "CompanyName": "",
	    "Country": "",
	    "FirstName": "",
	    "ID": "",
	    "LastName": "",
	    "Phone": "",
	    "State": "",
	    "Street1": "",
	    "Street2": "",
	    "Zip": "",
	    "xp": {}
	}
| Name | Type | Description | Required | 
|---|---|---|---|
| ID | string | ID of the address. Can only contain characters Aa-Zz, 0-9, -, and _. Searchable: priority level 1. Sortable: priority level 2. | False |
| CompanyName | string | Company name of the address. Max length 100 characters. Sortable. | False |
| FirstName | string | First name of the address. Max length 100 characters. Searchable: priority level 7. Sortable. | False |
| LastName | string | Last name of the address. Max length 100 characters. Searchable: priority level 6. Sortable. | False |
| Street1 | string | Street 1 of the address. Required. Max length 100 characters. Searchable: priority level 4. Sortable. | True |
| Street2 | string | Street 2 of the address. Max length 100 characters. Searchable: priority level 5. Sortable. | False |
| City | string | City of the address. Required. Max length 100 characters. Searchable: priority level 3. Sortable. | True |
| State | string | State of the address. Required. Max length 100 characters. Searchable: priority level 7. Sortable. | True |
| Zip | string | Zip of the address. Required. Max length 100 characters. Searchable: priority level 6. Sortable. | True |
| Country | string | Country of the address. Required. Max length 2 characters. Sortable. | True |
| Phone | string | Phone of the address. Max length 100 characters. Sortable. | False |
| AddressName | string | Address name of the address. Max length 100 characters. Searchable: priority level 2. Sortable: priority level 1. | False |
| xp | object | Container for extended (custom) properties of the address. | False |

## Response Body
	{
	    "BillingAddress": {
	        "AddressName": "",
	        "City": "",
	        "CompanyName": "",
	        "Country": "",
	        "DateCreated": "2018-03-21T23:00:00+00:00",
	        "FirstName": "",
	        "ID": "",
	        "LastName": "",
	        "Phone": "",
	        "State": "",
	        "Street1": "",
	        "Street2": "",
	        "Zip": "",
	        "xp": {}
	    },
	    "BillingAddressID": "",
	    "Comments": "",
	    "DateApproved": "2018-03-21T23:00:00+00:00",
	    "DateCanceled": "2018-03-21T23:00:00+00:00",
	    "DateCompleted": "2018-03-21T23:00:00+00:00",
	    "DateCreated": "2018-03-21T23:00:00+00:00",
	    "DateDeclined": "2018-03-21T23:00:00+00:00",
	    "DateSubmitted": "2018-03-21T23:00:00+00:00",
	    "FromCompanyID": "",
	    "FromUser": {
	        "Active": false,
	        "AvailableRoles": [
	            ""
	        ],
	        "Email": "",
	        "FirstName": "",
	        "ID": "",
	        "LastName": "",
	        "Phone": "",
	        "TermsAccepted": "2018-03-21T23:00:00+00:00",
	        "Username": "",
	        "xp": {}
	    },
	    "FromUserID": "",
	    "ID": "",
	    "IsSubmitted": false,
	    "LineItemCount": 0,
	    "PromotionDiscount": 0,
	    "ShippingAddressID": "",
	    "ShippingCost": 0,
	    "Status": "Unsubmitted",
	    "Subtotal": 0,
	    "TaxCost": 0,
	    "Total": 0,
	    "xp": {}
	}
| Name | Type | Description | Required | 
|---|---|---|---|
| ID | string | ID of the order. | False |
| FromUser | object | From user of the order. | False |
| FromCompanyID | string | ID of the from company. | False |
| FromUserID | string | ID of the from user. | False |
| BillingAddressID | string | ID of the billing address. | False |
| BillingAddress | object | Billing address of the order. | False |
| ShippingAddressID | string | ID of the Shipping Address for all LineItems on the Order. Null when there are multiple Shipping Addresses involved. | False |
| Comments | string | Comments of the order. | False |
| LineItemCount | integer | Line item count of the order. | False |
| Status | string | Status of the order. Possible values: Unsubmitted, AwaitingApproval, Declined, Open, Completed, Canceled. | False |
| DateCreated | date | Date created of the order. | False |
| DateSubmitted | date | Date submitted of the order. | False |
| DateApproved | date | Date approved of the order. | False |
| DateDeclined | date | Date declined of the order. | False |
| DateCanceled | date | Date canceled of the order. | False |
| DateCompleted | date | Date completed of the order. | False |
| Subtotal | float | Subtotal of the order. | False |
| ShippingCost | float | Shipping cost of the order. | False |
| TaxCost | float | Tax cost of the order. | False |
| PromotionDiscount | float | Promotion discount of the order. | False |
| Total | float | Total of the order. | False |
| IsSubmitted | boolean | True if this Order has been passed from the Buyer to the Seller. | False |
| xp | object | Container for extended (custom) properties of the order. | False |

## `PATCH` `v1/orders/{direction}/{orderID}/fromuser`
Partially update an order from user

| Name | Type | Description | Required | 
|---|---|---|---|
| direction | string | Direction of the order, from the current user's perspective. Possible values: incoming, outgoing. | True |
| orderID | string | ID of the order. | True |

## Request Body
	{
	    "Active": false,
	    "Email": "",
	    "FirstName": "",
	    "ID": "",
	    "LastName": "",
	    "Password": "",
	    "Phone": "",
	    "TermsAccepted": "2018-03-21T23:00:00+00:00",
	    "Username": "",
	    "xp": {}
	}
| Name | Type | Description | Required | 
|---|---|---|---|
| ID | string | ID of the user. Can only contain characters Aa-Zz, 0-9, -, and _. Searchable: priority level 1. Sortable. | False |
| Username | string | Username of the user. Required. Max length 100 characters. Searchable: priority level 2. Sortable: priority level 3. | True |
| Password | string | Password of the user. | False |
| FirstName | string | First name of the user. Required. Max length 100 characters. Searchable: priority level 4. Sortable: priority level 2. | True |
| LastName | string | Last name of the user. Required. Max length 100 characters. Searchable: priority level 3. Sortable: priority level 1. | True |
| Email | string | Email of the user. Required. Max length 200 characters. Searchable: priority level 5. Sortable. | True |
| Phone | string | Phone of the user. Max length 100 characters. | False |
| TermsAccepted | date | Terms accepted of the user. | False |
| Active | boolean | Active of the user. Required. | True |
| xp | object | Container for extended (custom) properties of the user. | False |

## Response Body
	{
	    "BillingAddress": {
	        "AddressName": "",
	        "City": "",
	        "CompanyName": "",
	        "Country": "",
	        "DateCreated": "2018-03-21T23:00:00+00:00",
	        "FirstName": "",
	        "ID": "",
	        "LastName": "",
	        "Phone": "",
	        "State": "",
	        "Street1": "",
	        "Street2": "",
	        "Zip": "",
	        "xp": {}
	    },
	    "BillingAddressID": "",
	    "Comments": "",
	    "DateApproved": "2018-03-21T23:00:00+00:00",
	    "DateCanceled": "2018-03-21T23:00:00+00:00",
	    "DateCompleted": "2018-03-21T23:00:00+00:00",
	    "DateCreated": "2018-03-21T23:00:00+00:00",
	    "DateDeclined": "2018-03-21T23:00:00+00:00",
	    "DateSubmitted": "2018-03-21T23:00:00+00:00",
	    "FromCompanyID": "",
	    "FromUser": {
	        "Active": false,
	        "AvailableRoles": [
	            ""
	        ],
	        "Email": "",
	        "FirstName": "",
	        "ID": "",
	        "LastName": "",
	        "Phone": "",
	        "TermsAccepted": "2018-03-21T23:00:00+00:00",
	        "Username": "",
	        "xp": {}
	    },
	    "FromUserID": "",
	    "ID": "",
	    "IsSubmitted": false,
	    "LineItemCount": 0,
	    "PromotionDiscount": 0,
	    "ShippingAddressID": "",
	    "ShippingCost": 0,
	    "Status": "Unsubmitted",
	    "Subtotal": 0,
	    "TaxCost": 0,
	    "Total": 0,
	    "xp": {}
	}
| Name | Type | Description | Required | 
|---|---|---|---|
| ID | string | ID of the order. | False |
| FromUser | object | From user of the order. | False |
| FromCompanyID | string | ID of the from company. | False |
| FromUserID | string | ID of the from user. | False |
| BillingAddressID | string | ID of the billing address. | False |
| BillingAddress | object | Billing address of the order. | False |
| ShippingAddressID | string | ID of the Shipping Address for all LineItems on the Order. Null when there are multiple Shipping Addresses involved. | False |
| Comments | string | Comments of the order. | False |
| LineItemCount | integer | Line item count of the order. | False |
| Status | string | Status of the order. Possible values: Unsubmitted, AwaitingApproval, Declined, Open, Completed, Canceled. | False |
| DateCreated | date | Date created of the order. | False |
| DateSubmitted | date | Date submitted of the order. | False |
| DateApproved | date | Date approved of the order. | False |
| DateDeclined | date | Date declined of the order. | False |
| DateCanceled | date | Date canceled of the order. | False |
| DateCompleted | date | Date completed of the order. | False |
| Subtotal | float | Subtotal of the order. | False |
| ShippingCost | float | Shipping cost of the order. | False |
| TaxCost | float | Tax cost of the order. | False |
| PromotionDiscount | float | Promotion discount of the order. | False |
| Total | float | Total of the order. | False |
| IsSubmitted | boolean | True if this Order has been passed from the Buyer to the Seller. | False |
| xp | object | Container for extended (custom) properties of the order. | False |

## `POST` `v1/orders/{direction}/{orderID}/promotions/{promoCode}`
Add an promotion

| Name | Type | Description | Required | 
|---|---|---|---|
| direction | string | Direction of the order, from the current user's perspective. Possible values: incoming, outgoing. | True |
| orderID | string | ID of the order. | True |
| promoCode | string | Promo code of the promotion. | True |

## Response Body
	{
	    "CanCombine": false,
	    "Code": "",
	    "Description": "",
	    "EligibleExpression": "",
	    "ExpirationDate": "2018-03-21T23:00:00+00:00",
	    "FinePrint": "",
	    "ID": "",
	    "Name": "",
	    "RedemptionCount": 0,
	    "RedemptionLimit": 0,
	    "RedemptionLimitPerUser": 0,
	    "StartDate": "2018-03-21T23:00:00+00:00",
	    "ValueExpression": "",
	    "xp": {}
	}
| Name | Type | Description | Required | 
|---|---|---|---|
| ID | string | ID of the promotion. | False |
| Code | string | Must be unique. Entered by buyer when adding promo to order. | True |
| Name | string | Name of the promotion. | False |
| RedemptionLimit | integer | Redemption limit of the promotion. | False |
| RedemptionLimitPerUser | integer | Redemption limit per user of the promotion. | False |
| RedemptionCount | integer | Redemption count of the promotion. | False |
| Description | string | Description of the promotion. | False |
| FinePrint | string | Terms, conditions, and other legal jargon. | False |
| StartDate | date | Start date of the promotion. | False |
| ExpirationDate | date | Expiration date of the promotion. | False |
| EligibleExpression | string | Eligible expression of the promotion. | True |
| ValueExpression | string | Value expression of the promotion. | True |
| CanCombine | boolean | Can combine of the promotion. | False |
| xp | object | Container for extended (custom) properties of the promotion. | False |

## `GET` `v1/orders/{direction}/{orderID}/promotions`
Get a list of order promotions

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
	{
	    "Items": [
	        {
	            "Amount": 0,
	            "CanCombine": false,
	            "Code": "",
	            "Description": "",
	            "EligibleExpression": "",
	            "ExpirationDate": "2018-03-21T23:00:00+00:00",
	            "FinePrint": "",
	            "ID": "",
	            "Name": "",
	            "RedemptionCount": 0,
	            "RedemptionLimit": 0,
	            "RedemptionLimitPerUser": 0,
	            "StartDate": "2018-03-21T23:00:00+00:00",
	            "ValueExpression": "",
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
| Amount | float | Amount of the order promotion. | False |
| ID | string | ID of the order promotion. | False |
| Code | string | Must be unique. Entered by buyer when adding promo to order. | True |
| Name | string | Name of the order promotion. | False |
| RedemptionLimit | integer | Redemption limit of the order promotion. | False |
| RedemptionLimitPerUser | integer | Redemption limit per user of the order promotion. | False |
| RedemptionCount | integer | Redemption count of the order promotion. | False |
| Description | string | Description of the order promotion. | False |
| FinePrint | string | Terms, conditions, and other legal jargon. | False |
| StartDate | date | Start date of the order promotion. | False |
| ExpirationDate | date | Expiration date of the order promotion. | False |
| EligibleExpression | string | Eligible expression of the order promotion. | True |
| ValueExpression | string | Value expression of the order promotion. | True |
| CanCombine | boolean | Can combine of the order promotion. | False |
| xp | object | Container for extended (custom) properties of the order promotion. | False |

## `DELETE` `v1/orders/{direction}/{orderID}/promotions/{promoCode}`
Remove an promotion

| Name | Type | Description | Required | 
|---|---|---|---|
| direction | string | Direction of the order, from the current user's perspective. Possible values: incoming, outgoing. | True |
| orderID | string | ID of the order. | True |
| promoCode | string | Promo code of the order. | True |

## Response Body
	{
	    "BillingAddress": {
	        "AddressName": "",
	        "City": "",
	        "CompanyName": "",
	        "Country": "",
	        "DateCreated": "2018-03-21T23:00:00+00:00",
	        "FirstName": "",
	        "ID": "",
	        "LastName": "",
	        "Phone": "",
	        "State": "",
	        "Street1": "",
	        "Street2": "",
	        "Zip": "",
	        "xp": {}
	    },
	    "BillingAddressID": "",
	    "Comments": "",
	    "DateApproved": "2018-03-21T23:00:00+00:00",
	    "DateCanceled": "2018-03-21T23:00:00+00:00",
	    "DateCompleted": "2018-03-21T23:00:00+00:00",
	    "DateCreated": "2018-03-21T23:00:00+00:00",
	    "DateDeclined": "2018-03-21T23:00:00+00:00",
	    "DateSubmitted": "2018-03-21T23:00:00+00:00",
	    "FromCompanyID": "",
	    "FromUser": {
	        "Active": false,
	        "AvailableRoles": [
	            ""
	        ],
	        "Email": "",
	        "FirstName": "",
	        "ID": "",
	        "LastName": "",
	        "Phone": "",
	        "TermsAccepted": "2018-03-21T23:00:00+00:00",
	        "Username": "",
	        "xp": {}
	    },
	    "FromUserID": "",
	    "ID": "",
	    "IsSubmitted": false,
	    "LineItemCount": 0,
	    "PromotionDiscount": 0,
	    "ShippingAddressID": "",
	    "ShippingCost": 0,
	    "Status": "Unsubmitted",
	    "Subtotal": 0,
	    "TaxCost": 0,
	    "Total": 0,
	    "xp": {}
	}
| Name | Type | Description | Required | 
|---|---|---|---|
| ID | string | ID of the order. | False |
| FromUser | object | From user of the order. | False |
| FromCompanyID | string | ID of the from company. | False |
| FromUserID | string | ID of the from user. | False |
| BillingAddressID | string | ID of the billing address. | False |
| BillingAddress | object | Billing address of the order. | False |
| ShippingAddressID | string | ID of the Shipping Address for all LineItems on the Order. Null when there are multiple Shipping Addresses involved. | False |
| Comments | string | Comments of the order. | False |
| LineItemCount | integer | Line item count of the order. | False |
| Status | string | Status of the order. Possible values: Unsubmitted, AwaitingApproval, Declined, Open, Completed, Canceled. | False |
| DateCreated | date | Date created of the order. | False |
| DateSubmitted | date | Date submitted of the order. | False |
| DateApproved | date | Date approved of the order. | False |
| DateDeclined | date | Date declined of the order. | False |
| DateCanceled | date | Date canceled of the order. | False |
| DateCompleted | date | Date completed of the order. | False |
| Subtotal | float | Subtotal of the order. | False |
| ShippingCost | float | Shipping cost of the order. | False |
| TaxCost | float | Tax cost of the order. | False |
| PromotionDiscount | float | Promotion discount of the order. | False |
| Total | float | Total of the order. | False |
| IsSubmitted | boolean | True if this Order has been passed from the Buyer to the Seller. | False |
| xp | object | Container for extended (custom) properties of the order. | False |
