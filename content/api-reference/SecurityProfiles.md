---
title: Security Profiles
date: 2018-03-27
category: API Reference
tags: Authentication And Authorization
slug: Authentication-And-Authorization-SecurityProfiles
---


## `GET` `v1/securityprofiles/{securityProfileID}`
Get a single security profile

| Name | Type | Description | Required | 
|---|---|---|---|
| securityProfileID | string | ID of the security profile. | True |

## Response Body
	:::json
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

| Name | Type | Description | Required | 
|---|---|---|---|
| buyerID | string | ID of the buyer. | False |
| supplierID | string | ID of the supplier. | False |
| securityProfileID | string | ID of the security profile. | False |
| userID | string | ID of the user. | False |
| userGroupID | string | ID of the user group. | False |
| commerceRole | string | Commerce role of the security profile assignment. Possible values: Buyer, Seller, Supplier. | False |
| level | string | Level of the security profile assignment. Possible values: User, Group, Company. | False |
| page | integer | Page of results to return. Default: 1 | False |
| pageSize | integer | Number of results to return per page. Default: 20, max: 100. | False |

## Response Body
	:::json
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

| Name | Type | Description | Required | 
|---|---|---|---|
| securityProfileID | string | ID of the security profile. | True |
| buyerID | string | ID of the buyer. | False |
| userID | string | ID of the user. | False |
| userGroupID | string | ID of the user group. | False |

## Response Body
## `POST` `v1/securityprofiles/assignments`
Save a security profile assignment
## Request Body
	:::json
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

## Response Body