---
title: Security Profiles
date: 2018-03-27
category: API Reference
tags: Authentication And Authorization
slug: Authentication-And-Authorization-SecurityProfiles
---


## `GET` `v1/securityprofiles/{securityProfileID}`
Get a single security profile

| Parameters      | Description                    |
|------------------|---------------------------------|


| Parameters      | Description                    |
|------------------|---------------------------------|
| Name            | securityProfileID              |
| Type            | string                         |
| Description     | ID of the security profile.    |
| Required        | True                           |

## Request Body
**Response Status**: `200`

## Response Body
	{
	    "ID": "",
	    "Name": "",
	    "Roles": [
	        "DevCenterImpersonate"
	    ]
	}
| Name | Type | Description | Required | 
|---|---|---|---|
| ID | string | ID of the security profile. | False |
| Name | string | Name of the security profile. | True |
| Roles | array | Roles of the security profile. | False |

## `GET` `v1/securityprofiles`
Get a list of security profiles

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
	            "Name": "",
	            "Roles": [
	                "DevCenterImpersonate"
	            ]
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
| ID | string | ID of the security profile. | False |
| Name | string | Name of the security profile. | True |
| Roles | array | Roles of the security profile. | False |

## `GET` `v1/securityprofiles/assignments`
Get a list of security profile assignments

| Parameters      | Description                    |
|------------------|---------------------------------|


| Parameters      | Description                    |
|------------------|---------------------------------|
| Name            | buyerID                        |
| Type            | string                         |
| Description     | ID of the buyer.               |
| Required        | False                          |


| Parameters      | Description                    |
|------------------|---------------------------------|
| Name            | supplierID                     |
| Type            | string                         |
| Description     | ID of the supplier.            |
| Required        | False                          |


| Parameters      | Description                    |
|------------------|---------------------------------|
| Name            | securityProfileID              |
| Type            | string                         |
| Description     | ID of the security profile.    |
| Required        | False                          |


| Parameters      | Description                    |
|------------------|---------------------------------|
| Name            | userID                         |
| Type            | string                         |
| Description     | ID of the user.                |
| Required        | False                          |


| Parameters      | Description                    |
|------------------|---------------------------------|
| Name            | userGroupID                    |
| Type            | string                         |
| Description     | ID of the user group.          |
| Required        | False                          |


| Parameters      | Description                    |
|------------------|---------------------------------|
| Name            | commerceRole                   |
| Type            | string                         |
| Description     | Commerce role of the security profile assignment. Possible values: Buyer, Seller, Supplier. |
| Required        | False                          |


| Parameters      | Description                    |
|------------------|---------------------------------|
| Name            | level                          |
| Type            | string                         |
| Description     | Level of the security profile assignment. Possible values: User, Group, Company. |
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
	            "BuyerID": "",
	            "SecurityProfileID": "",
	            "SupplierID": "",
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
| SecurityProfileID | string | ID of the security profile. | True |
| BuyerID | string | ID of the buyer. | False |
| SupplierID | string | ID of the supplier. | False |
| UserID | string | ID of the user. | False |
| UserGroupID | string | ID of the user group. | False |

## `DELETE` `v1/securityprofiles/{securityProfileID}/assignments`
Delete a security profile assignment

| Parameters      | Description                    |
|------------------|---------------------------------|


| Parameters      | Description                    |
|------------------|---------------------------------|
| Name            | securityProfileID              |
| Type            | string                         |
| Description     | ID of the security profile.    |
| Required        | True                           |


| Parameters      | Description                    |
|------------------|---------------------------------|
| Name            | buyerID                        |
| Type            | string                         |
| Description     | ID of the buyer.               |
| Required        | False                          |


| Parameters      | Description                    |
|------------------|---------------------------------|
| Name            | userID                         |
| Type            | string                         |
| Description     | ID of the user.                |
| Required        | False                          |


| Parameters      | Description                    |
|------------------|---------------------------------|
| Name            | userGroupID                    |
| Type            | string                         |
| Description     | ID of the user group.          |
| Required        | False                          |

## Request Body
**Response Status**: `204`

## Response Body
## `POST` `v1/securityprofiles/assignments`
Save a security profile assignment
## Request Body
	{
	    "BuyerID": "",
	    "SecurityProfileID": "",
	    "SupplierID": "",
	    "UserGroupID": "",
	    "UserID": ""
	}
| Name | Type | Description | Required | 
|---|---|---|---|
| SecurityProfileID | string | ID of the security profile. Required. Sortable: priority level 1. | True |
| BuyerID | string | ID of the buyer. | False |
| SupplierID | string | ID of the supplier. | False |
| UserID | string | ID of the user. Sortable: priority level 2. | False |
| UserGroupID | string | ID of the user group. | False |

**Response Status**: `204`

## Response Body