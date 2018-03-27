---
title: Admin User Groups
date: 2018-03-27
category: API Reference
tags: Seller
slug: Seller-AdminUserGroups
---


## `GET` `v1/usergroups/{userGroupID}`
Get a single admin user group

| Parameters      | Description                    |
|------------------|---------------------------------|


| Parameters      | Description                    |
|------------------|---------------------------------|
| Name            | userGroupID                    |
| Type            | string                         |
| Description     | ID of the user group.          |
| Required        | True                           |

## Request Body
**Response Status**: `200`

## Response Body
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

**Response Status**: `201`

## Response Body
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

| Parameters      | Description                    |
|------------------|---------------------------------|


| Parameters      | Description                    |
|------------------|---------------------------------|
| Name            | userGroupID                    |
| Type            | string                         |
| Description     | ID of the user group.          |
| Required        | True                           |

## Request Body
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

**Response Status**: `200`

## Response Body
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

| Parameters      | Description                    |
|------------------|---------------------------------|


| Parameters      | Description                    |
|------------------|---------------------------------|
| Name            | userGroupID                    |
| Type            | string                         |
| Description     | ID of the user group.          |
| Required        | True                           |

## Request Body
**Response Status**: `204`

## Response Body
## `PATCH` `v1/usergroups/{userGroupID}`
Partially update an admin user group

| Parameters      | Description                    |
|------------------|---------------------------------|


| Parameters      | Description                    |
|------------------|---------------------------------|
| Name            | userGroupID                    |
| Type            | string                         |
| Description     | ID of the user group.          |
| Required        | True                           |

## Request Body
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

**Response Status**: `200`

## Response Body
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

| Parameters      | Description                    |
|------------------|---------------------------------|


| Parameters      | Description                    |
|------------------|---------------------------------|
| Name            | userGroupID                    |
| Type            | string                         |
| Description     | ID of the user group.          |
| Required        | False                          |


| Parameters      | Description                    |
|------------------|---------------------------------|
| Name            | userID                         |
| Type            | string                         |
| Description     | ID of the user.                |
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

## Request Body
**Response Status**: `200`

## Response Body
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

| Parameters      | Description                    |
|------------------|---------------------------------|


| Parameters      | Description                    |
|------------------|---------------------------------|
| Name            | userGroupID                    |
| Type            | string                         |
| Description     | ID of the user group.          |
| Required        | True                           |


| Parameters      | Description                    |
|------------------|---------------------------------|
| Name            | userID                         |
| Type            | string                         |
| Description     | ID of the user.                |
| Required        | True                           |

## Request Body
**Response Status**: `204`

## Response Body
## `POST` `v1/usergroups/assignments`
Save an admin user group user assignment
## Request Body
	{
	    "UserGroupID": "",
	    "UserID": ""
	}
| Name | Type | Description | Required | 
|---|---|---|---|
| UserGroupID | string | ID of the user group. | False |
| UserID | string | ID of the user. | False |

**Response Status**: `204`

## Response Body