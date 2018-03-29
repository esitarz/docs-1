---
title: Categories
date: 2018-03-27
category: API Reference
tags: Me And My Stuff
slug: Me-And-My-Stuff-MeCategories
---
"Me" is a container for read-only endpoints that return a filtered view
of things that the current buyer user is allowed to see, i.e. things
that they are assigned to either directly or as a member of a buyer
organization or user group. It also provides ways for a user to update
or change their own information.

---

## `GET` `v1/me/categories`
Get a list of categories visible to this user

| Name | Type | Description | Required | 
|---|---|---|---|
| depth | string | Depth of the category. | False |
| catalogID | string | ID of the catalog. | False |
| productID | string | ID of the product. | False |
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
	            "Active": false,
	            "ChildCount": 0,
	            "Description": "",
	            "ID": "",
	            "ListOrder": 1,
	            "Name": "",
	            "ParentID": "",
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
| ID | string | ID of the category. | False |
| Name | string | Name of the category. | True |
| Description | string | Description of the category. | False |
| ListOrder | integer | Order that the category appears within its parent or catalog (if root level). | False |
| Active | boolean | If false, buyers cannot see this Category or any Categories or Products under it. | False |
| ParentID | string | ID of the parent category. | False |
| ChildCount | integer | Number of categories that are *immediate* children of this category. | False |
| xp | object | Container for extended (custom) properties of the category. | False |

## `GET` `v1/me/categories/{categoryID}`
Get a single category

| Name | Type | Description | Required | 
|---|---|---|---|
| categoryID | string | ID of the category. | True |
| catalogID | string | ID of the catalog. | True |

## Response Body
	:::json
	{
	    "Active": false,
	    "ChildCount": 0,
	    "Description": "",
	    "ID": "",
	    "ListOrder": 1,
	    "Name": "",
	    "ParentID": "",
	    "xp": {}
	}


| Name | Type | Description | Required | 
|---|---|---|---|
| ID | string | ID of the category. | False |
| Name | string | Name of the category. | True |
| Description | string | Description of the category. | False |
| ListOrder | integer | Order that the category appears within its parent or catalog (if root level). | False |
| Active | boolean | If false, buyers cannot see this Category or any Categories or Products under it. | False |
| ParentID | string | ID of the parent category. | False |
| ChildCount | integer | Number of categories that are *immediate* children of this category. | False |
| xp | object | Container for extended (custom) properties of the category. | False |
