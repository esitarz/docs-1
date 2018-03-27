---
title: Cost Centers
date: 2018-03-27
category: API Reference
tags: Buyers
slug: Buyers-CostCenters
---
A cost center is used to allocate organizational expenditures. Different
businesses call these by different names such as "allocation codes" or
"charge back codes", but the basic purpose is the same - to allocate an
expense back to someone or some department of an organization.

---

## `GET` `v1/buyers/{buyerID}/costcenters/{costCenterID}`
Get a single cost center

| Name | Type | Description | Required | 
|---|---|---|---|
| buyerID | string | ID of the buyer. | True |
| costCenterID | string | ID of the cost center. | True |

## Response Body
	{
	    "Description": "",
	    "ID": "",
	    "Name": "",
	    "xp": {}
	}
| Name | Type | Description | Required | 
|---|---|---|---|
| ID | string | ID of the cost center. | False |
| Name | string | Name of the cost center. | True |
| Description | string | Description of the cost center. | False |
| xp | object | Container for extended (custom) properties of the cost center. | False |

## `GET` `v1/buyers/{buyerID}/costcenters`
Get a list of cost centers

| Name | Type | Description | Required | 
|---|---|---|---|
| buyerID | string | ID of the buyer. | True |
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
	            "Description": "",
	            "ID": "",
	            "Name": "",
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
| ID | string | ID of the cost center. | False |
| Name | string | Name of the cost center. | True |
| Description | string | Description of the cost center. | False |
| xp | object | Container for extended (custom) properties of the cost center. | False |

## `POST` `v1/buyers/{buyerID}/costcenters`
Create a new cost center

| Name | Type | Description | Required | 
|---|---|---|---|
| buyerID | string | ID of the buyer. | True |

## Request Body
	{
	    "Description": "",
	    "ID": "",
	    "Name": "",
	    "xp": {}
	}
| Name | Type | Description | Required | 
|---|---|---|---|
| ID | string | ID of the cost center. Can only contain characters Aa-Zz, 0-9, -, and _. Searchable: priority level 1. Sortable: priority level 2. | False |
| Name | string | Name of the cost center. Required. Max length 100 characters. Searchable: priority level 2. Sortable: priority level 1. | True |
| Description | string | Description of the cost center. Max length 2000 characters. Searchable: priority level 3. | False |
| xp | object | Container for extended (custom) properties of the cost center. | False |

## Response Body
	{
	    "Description": "",
	    "ID": "",
	    "Name": "",
	    "xp": {}
	}
| Name | Type | Description | Required | 
|---|---|---|---|
| ID | string | ID of the cost center. | False |
| Name | string | Name of the cost center. | True |
| Description | string | Description of the cost center. | False |
| xp | object | Container for extended (custom) properties of the cost center. | False |

## `PUT` `v1/buyers/{buyerID}/costcenters/{costCenterID}`
Create or update a cost center

| Name | Type | Description | Required | 
|---|---|---|---|
| buyerID | string | ID of the buyer. | True |
| costCenterID | string | ID of the cost center. | True |

## Request Body
	{
	    "Description": "",
	    "ID": "",
	    "Name": "",
	    "xp": {}
	}
| Name | Type | Description | Required | 
|---|---|---|---|
| ID | string | ID of the cost center. Can only contain characters Aa-Zz, 0-9, -, and _. Searchable: priority level 1. Sortable: priority level 2. | False |
| Name | string | Name of the cost center. Required. Max length 100 characters. Searchable: priority level 2. Sortable: priority level 1. | True |
| Description | string | Description of the cost center. Max length 2000 characters. Searchable: priority level 3. | False |
| xp | object | Container for extended (custom) properties of the cost center. | False |

## Response Body
	{
	    "Description": "",
	    "ID": "",
	    "Name": "",
	    "xp": {}
	}
| Name | Type | Description | Required | 
|---|---|---|---|
| ID | string | ID of the cost center. | False |
| Name | string | Name of the cost center. | True |
| Description | string | Description of the cost center. | False |
| xp | object | Container for extended (custom) properties of the cost center. | False |

## `DELETE` `v1/buyers/{buyerID}/costcenters/{costCenterID}`
Delete a cost center

| Name | Type | Description | Required | 
|---|---|---|---|
| buyerID | string | ID of the buyer. | True |
| costCenterID | string | ID of the cost center. | True |

## Response Body
## `PATCH` `v1/buyers/{buyerID}/costcenters/{costCenterID}`
Partially update a cost center

| Name | Type | Description | Required | 
|---|---|---|---|
| buyerID | string | ID of the buyer. | True |
| costCenterID | string | ID of the cost center. | True |

## Request Body
	{
	    "Description": "",
	    "ID": "",
	    "Name": "",
	    "xp": {}
	}
| Name | Type | Description | Required | 
|---|---|---|---|
| ID | string | ID of the cost center. Can only contain characters Aa-Zz, 0-9, -, and _. Searchable: priority level 1. Sortable: priority level 2. | False |
| Name | string | Name of the cost center. Required. Max length 100 characters. Searchable: priority level 2. Sortable: priority level 1. | True |
| Description | string | Description of the cost center. Max length 2000 characters. Searchable: priority level 3. | False |
| xp | object | Container for extended (custom) properties of the cost center. | False |

## Response Body
	{
	    "Description": "",
	    "ID": "",
	    "Name": "",
	    "xp": {}
	}
| Name | Type | Description | Required | 
|---|---|---|---|
| ID | string | ID of the cost center. | False |
| Name | string | Name of the cost center. | True |
| Description | string | Description of the cost center. | False |
| xp | object | Container for extended (custom) properties of the cost center. | False |

## `GET` `v1/buyers/{buyerID}/costcenters/assignments`
Get a list of cost center assignments

| Name | Type | Description | Required | 
|---|---|---|---|
| buyerID | string | ID of the buyer. | True |
| costCenterID | string | ID of the cost center. | False |
| userID | string | ID of the user. | False |
| userGroupID | string | ID of the user group. | False |
| level | string | Level of the cost center assignment. Possible values: User, Group, Company. | False |
| page | integer | Page of results to return. Default: 1 | False |
| pageSize | integer | Number of results to return per page. Default: 20, max: 100. | False |

## Response Body
	{
	    "Items": [
	        {
	            "CostCenterID": "",
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
| CostCenterID | string | ID of the cost center. | True |
| UserGroupID | string | ID of the user group. | False |

## `DELETE` `v1/buyers/{buyerID}/costcenters/{costCenterID}/assignments`
Delete a cost center assignment

| Name | Type | Description | Required | 
|---|---|---|---|
| buyerID | string | ID of the buyer. | True |
| costCenterID | string | ID of the cost center. | True |
| userID | string | ID of the user. | False |
| userGroupID | string | ID of the user group. | False |

## Response Body
## `POST` `v1/buyers/{buyerID}/costcenters/assignments`
Save a cost center assignment

| Name | Type | Description | Required | 
|---|---|---|---|
| buyerID | string | ID of the buyer. | True |

## Request Body
	{
	    "CostCenterID": "",
	    "UserGroupID": ""
	}
| Name | Type | Description | Required | 
|---|---|---|---|
| CostCenterID | string | ID of the cost center. Required. Sortable: priority level 1. | True |
| UserGroupID | string | ID of the user group. Sortable: priority level 3. | False |

## Response Body