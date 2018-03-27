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

| Parameters      | Description                    |
|------------------|---------------------------------|


| Parameters      | Description                    |
|------------------|---------------------------------|
| Name            | incrementorID                  |
| Type            | string                         |
| Description     | ID of the incrementor.         |
| Required        | True                           |

## Request Body
**Response Status**: `200`

## Response Body
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

| Parameters      | Description                    |
|------------------|---------------------------------|


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

**Response Status**: `201`

## Response Body
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

| Parameters      | Description                    |
|------------------|---------------------------------|


| Parameters      | Description                    |
|------------------|---------------------------------|
| Name            | incrementorID                  |
| Type            | string                         |
| Description     | ID of the incrementor.         |
| Required        | True                           |

## Request Body
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

**Response Status**: `200`

## Response Body
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

| Parameters      | Description                    |
|------------------|---------------------------------|


| Parameters      | Description                    |
|------------------|---------------------------------|
| Name            | incrementorID                  |
| Type            | string                         |
| Description     | ID of the incrementor.         |
| Required        | True                           |

## Request Body
**Response Status**: `204`

## Response Body
## `PATCH` `v1/incrementors/{incrementorID}`
Partially update an incrementor

| Parameters      | Description                    |
|------------------|---------------------------------|


| Parameters      | Description                    |
|------------------|---------------------------------|
| Name            | incrementorID                  |
| Type            | string                         |
| Description     | ID of the incrementor.         |
| Required        | True                           |

## Request Body
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

**Response Status**: `200`

## Response Body
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
