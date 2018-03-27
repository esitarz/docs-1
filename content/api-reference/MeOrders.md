---
title: Orders
date: 2018-03-27
category: API Reference
tags: Me And My Stuff
slug: Me-And-My-Stuff-MeOrders
---
"Me" is a container for read-only endpoints that return a filtered view
of things that the current buyer user is allowed to see, i.e. things
that they are assigned to either directly or as a member of a buyer
organization or user group. It also provides ways for a user to update
or change their own information.

---

## `GET` `v1/me/orders`
Get a list of orders visible to this user

| Parameters      | Description                    |
|------------------|---------------------------------|


| Parameters      | Description                    |
|------------------|---------------------------------|
| Name            | from                           |
| Type            | date                           |
| Description     | Lower bound of date range that the order was created (if outgoing) or submitted (if incoming). |
| Required        | False                          |


| Parameters      | Description                    |
|------------------|---------------------------------|
| Name            | to                             |
| Type            | date                           |
| Description     | Upper bound of date range that the order was created (if outgoing) or submitted (if incoming). |
| Required        | False                          |


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
	            "BillingAddress": {
	                "AddressName": "",
	                "City": "",
	                "CompanyName": "",
	                "Country": "",
	                "DateCreated": "2018-03-27T16:00:00+00:00",
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
	            "DateApproved": "2018-03-27T16:00:00+00:00",
	            "DateCanceled": "2018-03-27T16:00:00+00:00",
	            "DateCompleted": "2018-03-27T16:00:00+00:00",
	            "DateCreated": "2018-03-27T16:00:00+00:00",
	            "DateDeclined": "2018-03-27T16:00:00+00:00",
	            "DateSubmitted": "2018-03-27T16:00:00+00:00",
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
	                "TermsAccepted": "2018-03-27T16:00:00+00:00",
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
| DateSubmitted | date | Date submitted of the order. | False |
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

## `GET` `v1/me/orders/approvable`
Get a list of orders that this user can approve

| Parameters      | Description                    |
|------------------|---------------------------------|


| Parameters      | Description                    |
|------------------|---------------------------------|
| Name            | from                           |
| Type            | date                           |
| Description     | Lower bound of date range that the order was created (if outgoing) or submitted (if incoming). |
| Required        | False                          |


| Parameters      | Description                    |
|------------------|---------------------------------|
| Name            | to                             |
| Type            | date                           |
| Description     | Upper bound of date range that the order was created (if outgoing) or submitted (if incoming). |
| Required        | False                          |


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
	            "BillingAddress": {
	                "AddressName": "",
	                "City": "",
	                "CompanyName": "",
	                "Country": "",
	                "DateCreated": "2018-03-27T16:00:00+00:00",
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
	            "DateApproved": "2018-03-27T16:00:00+00:00",
	            "DateCanceled": "2018-03-27T16:00:00+00:00",
	            "DateCompleted": "2018-03-27T16:00:00+00:00",
	            "DateCreated": "2018-03-27T16:00:00+00:00",
	            "DateDeclined": "2018-03-27T16:00:00+00:00",
	            "DateSubmitted": "2018-03-27T16:00:00+00:00",
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
	                "TermsAccepted": "2018-03-27T16:00:00+00:00",
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
| DateSubmitted | date | Date submitted of the order. | False |
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
