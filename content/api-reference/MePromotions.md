---
title: Promotions
date: 2018-03-27
category: API Reference
tags: Me And My Stuff
slug: Me-And-My-Stuff-MePromotions
---
"Me" is a container for read-only endpoints that return a filtered view
of things that the current buyer user is allowed to see, i.e. things
that they are assigned to either directly or as a member of a buyer
organization or user group. It also provides ways for a user to update
or change their own information.

---

## `GET` `v1/me/promotions`
Get a list of promotions visible to this user

| Name | Type | Description | Required | 
|---|---|---|---|
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
	            "CanCombine": false,
	            "Code": "",
	            "Description": "",
	            "EligibleExpression": "",
	            "ExpirationDate": "2018-03-27T19:00:00+00:00",
	            "FinePrint": "",
	            "ID": "",
	            "Name": "",
	            "RedemptionCount": 0,
	            "RedemptionLimit": 0,
	            "RedemptionLimitPerUser": 0,
	            "StartDate": "2018-03-27T19:00:00+00:00",
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

## `GET` `v1/me/promotions/{promotionID}`
Get a single promotion

| Name | Type | Description | Required | 
|---|---|---|---|
| promotionID | string | ID of the promotion. | True |

## Response Body
	:::json
	{
	    "CanCombine": false,
	    "Code": "",
	    "Description": "",
	    "EligibleExpression": "",
	    "ExpirationDate": "2018-03-27T19:00:00+00:00",
	    "FinePrint": "",
	    "ID": "",
	    "Name": "",
	    "RedemptionCount": 0,
	    "RedemptionLimit": 0,
	    "RedemptionLimitPerUser": 0,
	    "StartDate": "2018-03-27T19:00:00+00:00",
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
