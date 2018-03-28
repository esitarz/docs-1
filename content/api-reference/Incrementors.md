---
title: Incrementors
date: 2018-03-27
category: API Reference
tags: Seller
slug: Seller-Incrementors
---
An incrementor is used to add an atomically incremented number to your
object IDs. For example, "aprefix-{myIncrementorID}", will yield an
order ID of aprefix-10010.

---

## `GET` `v1/incrementors/{incrementorID}`
Get a single incrementor

| Name | Type | Description | Required | 
|---|---|---|---|
| incrementorID | string | ID of the incrementor. | True |

## Response Body
	:::json
	{
	    "ID": "",
	    "LastNumber": 0,
	    "LeftPaddingCount": 0,
	    "Name": ""
	}


| Name | Type | Description | Required | 
|---|---|---|---|
| ID | string | ID of the incrementor. | False |
| Name | string | Name of the incrementor. | False |
| LastNumber | integer | Last number of the incrementor. | True |
| LeftPaddingCount | integer | Left padding count of the incrementor. | True |

## `GET` `v1/incrementors`
Get a list of incrementors

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
	            "ID": "",
	            "LastNumber": 0,
	            "LeftPaddingCount": 0,
	            "Name": ""
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
| ID | string | ID of the incrementor. | False |
| Name | string | Name of the incrementor. | False |
| LastNumber | integer | Last number of the incrementor. | True |
| LeftPaddingCount | integer | Left padding count of the incrementor. | True |

## `POST` `v1/incrementors`
Create a new incrementor
## Request Body
	:::json
	{
	    "ID": "",
	    "LastNumber": 0,
	    "LeftPaddingCount": 0,
	    "Name": ""
	}


| Name | Type | Description | Required | 
|---|---|---|---|
| ID | string | ID of the incrementor. Can only contain characters Aa-Zz, 0-9, -, and _. Searchable: priority level 1. Sortable: priority level 1. | False |
| Name | string | Name of the incrementor. Max length 100 characters. Searchable: priority level 2. Sortable: priority level 2. | False |
| LastNumber | integer | Last number of the incrementor. Required. Must be between 0 and 2147483647. | True |
| LeftPaddingCount | integer | Left padding count of the incrementor. Required. Must be between 0 and 25. | True |

## Response Body
	:::json
	{
	    "ID": "",
	    "LastNumber": 0,
	    "LeftPaddingCount": 0,
	    "Name": ""
	}


| Name | Type | Description | Required | 
|---|---|---|---|
| ID | string | ID of the incrementor. | False |
| Name | string | Name of the incrementor. | False |
| LastNumber | integer | Last number of the incrementor. | True |
| LeftPaddingCount | integer | Left padding count of the incrementor. | True |

## `PUT` `v1/incrementors/{incrementorID}`
Create or update an incrementor

| Name | Type | Description | Required | 
|---|---|---|---|
| incrementorID | string | ID of the incrementor. | True |

## Request Body
	:::json
	{
	    "ID": "",
	    "LastNumber": 0,
	    "LeftPaddingCount": 0,
	    "Name": ""
	}


| Name | Type | Description | Required | 
|---|---|---|---|
| ID | string | ID of the incrementor. Can only contain characters Aa-Zz, 0-9, -, and _. Searchable: priority level 1. Sortable: priority level 1. | False |
| Name | string | Name of the incrementor. Max length 100 characters. Searchable: priority level 2. Sortable: priority level 2. | False |
| LastNumber | integer | Last number of the incrementor. Required. Must be between 0 and 2147483647. | True |
| LeftPaddingCount | integer | Left padding count of the incrementor. Required. Must be between 0 and 25. | True |

## Response Body
	:::json
	{
	    "ID": "",
	    "LastNumber": 0,
	    "LeftPaddingCount": 0,
	    "Name": ""
	}


| Name | Type | Description | Required | 
|---|---|---|---|
| ID | string | ID of the incrementor. | False |
| Name | string | Name of the incrementor. | False |
| LastNumber | integer | Last number of the incrementor. | True |
| LeftPaddingCount | integer | Left padding count of the incrementor. | True |

## `DELETE` `v1/incrementors/{incrementorID}`
Delete an incrementor

| Name | Type | Description | Required | 
|---|---|---|---|
| incrementorID | string | ID of the incrementor. | True |

## Response Body
## `PATCH` `v1/incrementors/{incrementorID}`
Partially update an incrementor

| Name | Type | Description | Required | 
|---|---|---|---|
| incrementorID | string | ID of the incrementor. | True |

## Request Body
	:::json
	{
	    "ID": "",
	    "LastNumber": 0,
	    "LeftPaddingCount": 0,
	    "Name": ""
	}


| Name | Type | Description | Required | 
|---|---|---|---|
| ID | string | ID of the incrementor. Can only contain characters Aa-Zz, 0-9, -, and _. Searchable: priority level 1. Sortable: priority level 1. | False |
| Name | string | Name of the incrementor. Max length 100 characters. Searchable: priority level 2. Sortable: priority level 2. | False |
| LastNumber | integer | Last number of the incrementor. Required. Must be between 0 and 2147483647. | True |
| LeftPaddingCount | integer | Left padding count of the incrementor. Required. Must be between 0 and 25. | True |

## Response Body
	:::json
	{
	    "ID": "",
	    "LastNumber": 0,
	    "LeftPaddingCount": 0,
	    "Name": ""
	}


| Name | Type | Description | Required | 
|---|---|---|---|
| ID | string | ID of the incrementor. | False |
| Name | string | Name of the incrementor. | False |
| LastNumber | integer | Last number of the incrementor. | True |
| LeftPaddingCount | integer | Left padding count of the incrementor. | True |
