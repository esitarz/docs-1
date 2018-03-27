---
title: Promotions
date: 2018-03-27
category: API Reference
tags: Orders And Fulfillment
slug: Orders-And-Fulfillment-Promotions
---
Promotions are used to reduce the cost of a line item or an order.
Promotions can have redemption rules that can be applied for available
dates, occurences and value.
 Promotions can be assigned to Products, Categories, Buyers, UserGroups
and Users for redemption.

---

## `GET` `v1/promotions/{promotionID}`
Get a single promotion

| Name | Type | Description | Required | 
|---|---|---|---|
| promotionID | string | ID of the promotion. | True |

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

## `GET` `v1/promotions`
Get a list of promotions

| Name | Type | Description | Required | 
|---|---|---|---|
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

## `POST` `v1/promotions`
Create a new promotion
## Request Body
	{
	    "CanCombine": false,
	    "Code": "",
	    "Description": "",
	    "EligibleExpression": "",
	    "ExpirationDate": "2018-03-21T23:00:00+00:00",
	    "FinePrint": "",
	    "ID": "",
	    "Name": "",
	    "RedemptionLimit": 0,
	    "RedemptionLimitPerUser": 0,
	    "StartDate": "2018-03-21T23:00:00+00:00",
	    "ValueExpression": "",
	    "xp": {}
	}
| Name | Type | Description | Required | 
|---|---|---|---|
| ID | string | ID of the promotion. Can only contain characters Aa-Zz, 0-9, -, and _. Searchable: priority level 1. Sortable: priority level 2. | False |
| Code | string | Must be unique. Entered by buyer when adding promo to order. | True |
| Name | string | Name of the promotion. Max length 100 characters. Searchable: priority level 2. Sortable: priority level 1. | False |
| RedemptionLimit | integer | Redemption limit of the promotion. | False |
| RedemptionLimitPerUser | integer | Redemption limit per user of the promotion. | False |
| Description | string | Description of the promotion. Max length 2000 characters. Searchable: priority level 4. | False |
| FinePrint | string | Terms, conditions, and other legal jargon. | False |
| StartDate | date | Start date of the promotion. Sortable. | False |
| ExpirationDate | date | Expiration date of the promotion. Sortable. | False |
| EligibleExpression | string | Eligible expression of the promotion. Required. Max length 400 characters. Searchable: priority level 6. Sortable. | True |
| ValueExpression | string | Value expression of the promotion. Required. Max length 400 characters. Searchable: priority level 7. Sortable. | True |
| CanCombine | boolean | Can combine of the promotion. Sortable. | False |
| xp | object | Container for extended (custom) properties of the promotion. | False |

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

## `PUT` `v1/promotions/{promotionID}`
Create or update a promotion

| Name | Type | Description | Required | 
|---|---|---|---|
| promotionID | string | ID of the promotion. | True |

## Request Body
	{
	    "CanCombine": false,
	    "Code": "",
	    "Description": "",
	    "EligibleExpression": "",
	    "ExpirationDate": "2018-03-21T23:00:00+00:00",
	    "FinePrint": "",
	    "ID": "",
	    "Name": "",
	    "RedemptionLimit": 0,
	    "RedemptionLimitPerUser": 0,
	    "StartDate": "2018-03-21T23:00:00+00:00",
	    "ValueExpression": "",
	    "xp": {}
	}
| Name | Type | Description | Required | 
|---|---|---|---|
| ID | string | ID of the promotion. Can only contain characters Aa-Zz, 0-9, -, and _. Searchable: priority level 1. Sortable: priority level 2. | False |
| Code | string | Must be unique. Entered by buyer when adding promo to order. | True |
| Name | string | Name of the promotion. Max length 100 characters. Searchable: priority level 2. Sortable: priority level 1. | False |
| RedemptionLimit | integer | Redemption limit of the promotion. | False |
| RedemptionLimitPerUser | integer | Redemption limit per user of the promotion. | False |
| Description | string | Description of the promotion. Max length 2000 characters. Searchable: priority level 4. | False |
| FinePrint | string | Terms, conditions, and other legal jargon. | False |
| StartDate | date | Start date of the promotion. Sortable. | False |
| ExpirationDate | date | Expiration date of the promotion. Sortable. | False |
| EligibleExpression | string | Eligible expression of the promotion. Required. Max length 400 characters. Searchable: priority level 6. Sortable. | True |
| ValueExpression | string | Value expression of the promotion. Required. Max length 400 characters. Searchable: priority level 7. Sortable. | True |
| CanCombine | boolean | Can combine of the promotion. Sortable. | False |
| xp | object | Container for extended (custom) properties of the promotion. | False |

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

## `DELETE` `v1/promotions/{promotionID}`
Delete a promotion

| Name | Type | Description | Required | 
|---|---|---|---|
| promotionID | string | ID of the promotion. | True |

## Response Body
## `PATCH` `v1/promotions/{promotionID}`
Partially update a promotion

| Name | Type | Description | Required | 
|---|---|---|---|
| promotionID | string | ID of the promotion. | True |

## Request Body
	{
	    "CanCombine": false,
	    "Code": "",
	    "Description": "",
	    "EligibleExpression": "",
	    "ExpirationDate": "2018-03-21T23:00:00+00:00",
	    "FinePrint": "",
	    "ID": "",
	    "Name": "",
	    "RedemptionLimit": 0,
	    "RedemptionLimitPerUser": 0,
	    "StartDate": "2018-03-21T23:00:00+00:00",
	    "ValueExpression": "",
	    "xp": {}
	}
| Name | Type | Description | Required | 
|---|---|---|---|
| ID | string | ID of the promotion. Can only contain characters Aa-Zz, 0-9, -, and _. Searchable: priority level 1. Sortable: priority level 2. | False |
| Code | string | Must be unique. Entered by buyer when adding promo to order. | True |
| Name | string | Name of the promotion. Max length 100 characters. Searchable: priority level 2. Sortable: priority level 1. | False |
| RedemptionLimit | integer | Redemption limit of the promotion. | False |
| RedemptionLimitPerUser | integer | Redemption limit per user of the promotion. | False |
| Description | string | Description of the promotion. Max length 2000 characters. Searchable: priority level 4. | False |
| FinePrint | string | Terms, conditions, and other legal jargon. | False |
| StartDate | date | Start date of the promotion. Sortable. | False |
| ExpirationDate | date | Expiration date of the promotion. Sortable. | False |
| EligibleExpression | string | Eligible expression of the promotion. Required. Max length 400 characters. Searchable: priority level 6. Sortable. | True |
| ValueExpression | string | Value expression of the promotion. Required. Max length 400 characters. Searchable: priority level 7. Sortable. | True |
| CanCombine | boolean | Can combine of the promotion. Sortable. | False |
| xp | object | Container for extended (custom) properties of the promotion. | False |

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

## `GET` `v1/promotions/assignments`
Get a list of promotion assignments

| Name | Type | Description | Required | 
|---|---|---|---|
| buyerID | string | ID of the buyer. | False |
| promotionID | string | ID of the promotion. | False |
| userID | string | ID of the user. | False |
| userGroupID | string | ID of the user group. | False |
| level | string | Level of the promotion assignment. Possible values: User, Group, Company. | False |
| page | integer | Page of results to return. Default: 1 | False |
| pageSize | integer | Number of results to return per page. Default: 20, max: 100. | False |

## Response Body
	{
	    "Items": [
	        {
	            "BuyerID": "",
	            "PromotionID": "",
	            "UserGroupID": ""
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
| PromotionID | string | ID of the promotion. | True |
| BuyerID | string | ID of the buyer. | True |
| UserGroupID | string | ID of the user group. | False |

## `POST` `v1/promotions/assignments`
Save a promotion assignment
## Request Body
	{
	    "BuyerID": "",
	    "PromotionID": "",
	    "UserGroupID": ""
	}
| Name | Type | Description | Required | 
|---|---|---|---|
| PromotionID | string | ID of the promotion. Required. Sortable: priority level 1. | True |
| BuyerID | string | ID of the buyer. Required. Sortable: priority level 2. | True |
| UserGroupID | string | ID of the user group. Sortable: priority level 4. | False |

## Response Body
## `DELETE` `v1/promotions/{promotionID}/assignments`
Delete a promotion assignment

| Name | Type | Description | Required | 
|---|---|---|---|
| promotionID | string | ID of the promotion. | True |
| buyerID | string | ID of the buyer. | True |
| userID | string | ID of the user. | False |
| userGroupID | string | ID of the user group. | False |

## Response Body