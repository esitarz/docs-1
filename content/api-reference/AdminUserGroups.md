---
title: Admin User Groups
date: 2018-03-27
category: API Reference
tags: Seller
slug: Seller-AdminUserGroups
---


## `GET` `v1/usergroups/{userGroupID}`
Get a single admin user group

| Name | Type | Description | Required | 
|---|---|---|---|
| userGroupID | string | ID of the user group. | True |

## Response Body
	:::json
	{
	    "Description": "",
	    "ID": "",
	    "Name": "",
	    "xp": {}
	}


| Name | Type | Description | Required | 
|---|---|---|---|
| ID | string | ID of the user group. | False |
| Name | string | Name of the user group. | True |
| Description | string | Description of the user group. | False |
| xp | object | Container for extended (custom) properties of the user group. | False |

## `GET` `v1/usergroups`
Get a list of admin user groups

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
| ID | string | ID of the user group. | False |
| Name | string | Name of the user group. | True |
| Description | string | Description of the user group. | False |
| xp | object | Container for extended (custom) properties of the user group. | False |

## `POST` `v1/usergroups`
Create a new admin user group
## Request Body
	:::json
	{
	    "Description": "",
	    "ID": "",
	    "Name": "",
	    "xp": {}
	}


| Name | Type | Description | Required | 
|---|---|---|---|
| ID | string | ID of the user group. Can only contain characters Aa-Zz, 0-9, -, and _. Searchable: priority level 1. Sortable: priority level 2. | False |
| Name | string | Name of the user group. Required. Max length 100 characters. Searchable: priority level 2. Sortable: priority level 1. | True |
| Description | string | Description of the user group. Max length 2000 characters. Searchable: priority level 3. | False |
| xp | object | Container for extended (custom) properties of the user group. | False |

## Response Body
	:::json
	{
	    "Description": "",
	    "ID": "",
	    "Name": "",
	    "xp": {}
	}


| Name | Type | Description | Required | 
|---|---|---|---|
| ID | string | ID of the user group. | False |
| Name | string | Name of the user group. | True |
| Description | string | Description of the user group. | False |
| xp | object | Container for extended (custom) properties of the user group. | False |

## `PUT` `v1/usergroups/{userGroupID}`
Create or update an admin user group

| Name | Type | Description | Required | 
|---|---|---|---|
| userGroupID | string | ID of the user group. | True |

## Request Body
	:::json
	{
	    "Description": "",
	    "ID": "",
	    "Name": "",
	    "xp": {}
	}


| Name | Type | Description | Required | 
|---|---|---|---|
| ID | string | ID of the user group. Can only contain characters Aa-Zz, 0-9, -, and _. Searchable: priority level 1. Sortable: priority level 2. | False |
| Name | string | Name of the user group. Required. Max length 100 characters. Searchable: priority level 2. Sortable: priority level 1. | True |
| Description | string | Description of the user group. Max length 2000 characters. Searchable: priority level 3. | False |
| xp | object | Container for extended (custom) properties of the user group. | False |

## Response Body
	:::json
	{
	    "Description": "",
	    "ID": "",
	    "Name": "",
	    "xp": {}
	}


| Name | Type | Description | Required | 
|---|---|---|---|
| ID | string | ID of the user group. | False |
| Name | string | Name of the user group. | True |
| Description | string | Description of the user group. | False |
| xp | object | Container for extended (custom) properties of the user group. | False |

## `DELETE` `v1/usergroups/{userGroupID}`
Delete an admin user group

| Name | Type | Description | Required | 
|---|---|---|---|
| userGroupID | string | ID of the user group. | True |

## Response Body
## `PATCH` `v1/usergroups/{userGroupID}`
Partially update an admin user group

| Name | Type | Description | Required | 
|---|---|---|---|
| userGroupID | string | ID of the user group. | True |

## Request Body
	:::json
	{
	    "Description": "",
	    "ID": "",
	    "Name": "",
	    "xp": {}
	}


| Name | Type | Description | Required | 
|---|---|---|---|
| ID | string | ID of the user group. Can only contain characters Aa-Zz, 0-9, -, and _. Searchable: priority level 1. Sortable: priority level 2. | False |
| Name | string | Name of the user group. Required. Max length 100 characters. Searchable: priority level 2. Sortable: priority level 1. | True |
| Description | string | Description of the user group. Max length 2000 characters. Searchable: priority level 3. | False |
| xp | object | Container for extended (custom) properties of the user group. | False |

## Response Body
	:::json
	{
	    "Description": "",
	    "ID": "",
	    "Name": "",
	    "xp": {}
	}


| Name | Type | Description | Required | 
|---|---|---|---|
| ID | string | ID of the user group. | False |
| Name | string | Name of the user group. | True |
| Description | string | Description of the user group. | False |
| xp | object | Container for extended (custom) properties of the user group. | False |

## `GET` `v1/usergroups/assignments`
Get a list of admin user group user assignments

| Name | Type | Description | Required | 
|---|---|---|---|
| userGroupID | string | ID of the user group. | False |
| userID | string | ID of the user. | False |
| page | integer | Page of results to return. Default: 1 | False |
| pageSize | integer | Number of results to return per page. Default: 20, max: 100. | False |

## Response Body
	:::json
	{
	    "Items": [
	        {
	            "UserGroupID": "",
	            "UserID": ""
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
| UserGroupID | string | ID of the user group. | False |
| UserID | string | ID of the user. | False |

## `DELETE` `v1/usergroups/{userGroupID}/assignments/{userID}`
Delete an admin user group user assignment

| Name | Type | Description | Required | 
|---|---|---|---|
| userGroupID | string | ID of the user group. | True |
| userID | string | ID of the user. | True |

## Response Body
## `POST` `v1/usergroups/assignments`
Save an admin user group user assignment
## Request Body
	:::json
	{
	    "UserGroupID": "",
	    "UserID": ""
	}


| Name | Type | Description | Required | 
|---|---|---|---|
| UserGroupID | string | ID of the user group. | False |
| UserID | string | ID of the user. | False |

## Response Body