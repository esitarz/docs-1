---
title: Impersonation Configs
date: 2018-03-27
category: API Reference
tags: Authentication And Authorization
slug: Authentication-And-Authorization-ImpersonationConfigs
---


## `GET` `v1/impersonationconfig/{impersonationConfigID}`
Get a single impersonation config

| Name | Type | Description | Required | 
|---|---|---|---|
| impersonationConfigID | string | ID of the impersonation config. | True |

## Response Body
	:::json
	{
	    "BuyerID": "",
	    "ClientID": "",
	    "GroupID": "",
	    "ID": "",
	    "ImpersonationBuyerID": "",
	    "ImpersonationGroupID": "",
	    "ImpersonationUserID": "",
	    "SecurityProfileID": "",
	    "UserID": ""
	}


| Name | Type | Description | Required | 
|---|---|---|---|
| ID | string | ID of the impersonation config. | False |
| ImpersonationBuyerID | string | ID of the impersonation buyer. | False |
| ImpersonationGroupID | string | ID of the impersonation group. | False |
| ImpersonationUserID | string | ID of the impersonation user. | False |
| BuyerID | string | ID of the buyer. | True |
| GroupID | string | ID of the group. | False |
| UserID | string | ID of the user. | False |
| SecurityProfileID | string | ID of the security profile. | True |
| ClientID | string | ID of the client. | True |

## `GET` `v1/impersonationconfig`
Get a list of impersonation configs

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
	            "BuyerID": "",
	            "ClientID": "",
	            "GroupID": "",
	            "ID": "",
	            "ImpersonationBuyerID": "",
	            "ImpersonationGroupID": "",
	            "ImpersonationUserID": "",
	            "SecurityProfileID": "",
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
| ID | string | ID of the impersonation config. | False |
| ImpersonationBuyerID | string | ID of the impersonation buyer. | False |
| ImpersonationGroupID | string | ID of the impersonation group. | False |
| ImpersonationUserID | string | ID of the impersonation user. | False |
| BuyerID | string | ID of the buyer. | True |
| GroupID | string | ID of the group. | False |
| UserID | string | ID of the user. | False |
| SecurityProfileID | string | ID of the security profile. | True |
| ClientID | string | ID of the client. | True |

## `POST` `v1/impersonationconfig`
Create a new impersonation config
## Request Body
	:::json
	{
	    "BuyerID": "",
	    "ClientID": "",
	    "GroupID": "",
	    "ID": "",
	    "ImpersonationBuyerID": "",
	    "ImpersonationGroupID": "",
	    "ImpersonationUserID": "",
	    "SecurityProfileID": "",
	    "UserID": ""
	}


| Name | Type | Description | Required | 
|---|---|---|---|
| ID | string | ID of the impersonation config. Can only contain characters Aa-Zz, 0-9, -, and _. Searchable: priority level 8. Sortable: priority level 8. | False |
| ImpersonationBuyerID | string | ID of the impersonation buyer. Searchable: priority level 0. Sortable: priority level 0. | False |
| ImpersonationGroupID | string | ID of the impersonation group. Searchable: priority level 1. Sortable: priority level 1. | False |
| ImpersonationUserID | string | ID of the impersonation user. Searchable: priority level 2. Sortable: priority level 2. | False |
| BuyerID | string | ID of the buyer. Required. Searchable: priority level 3. Sortable: priority level 3. | True |
| GroupID | string | ID of the group. Searchable: priority level 4. Sortable: priority level 4. | False |
| UserID | string | ID of the user. Searchable: priority level 5. Sortable: priority level 5. | False |
| SecurityProfileID | string | ID of the security profile. Required. Searchable: priority level 6. Sortable: priority level 6. | True |
| ClientID | string | ID of the client. Required. Searchable: priority level 7. Sortable: priority level 7. | True |

## Response Body
	:::json
	{
	    "BuyerID": "",
	    "ClientID": "",
	    "GroupID": "",
	    "ID": "",
	    "ImpersonationBuyerID": "",
	    "ImpersonationGroupID": "",
	    "ImpersonationUserID": "",
	    "SecurityProfileID": "",
	    "UserID": ""
	}


| Name | Type | Description | Required | 
|---|---|---|---|
| ID | string | ID of the impersonation config. | False |
| ImpersonationBuyerID | string | ID of the impersonation buyer. | False |
| ImpersonationGroupID | string | ID of the impersonation group. | False |
| ImpersonationUserID | string | ID of the impersonation user. | False |
| BuyerID | string | ID of the buyer. | True |
| GroupID | string | ID of the group. | False |
| UserID | string | ID of the user. | False |
| SecurityProfileID | string | ID of the security profile. | True |
| ClientID | string | ID of the client. | True |

## `PUT` `v1/impersonationconfig/{impersonationConfigID}`
Create or update an impersonation config

| Name | Type | Description | Required | 
|---|---|---|---|
| impersonationConfigID | string | ID of the impersonation config. | True |

## Request Body
	:::json
	{
	    "BuyerID": "",
	    "ClientID": "",
	    "GroupID": "",
	    "ID": "",
	    "ImpersonationBuyerID": "",
	    "ImpersonationGroupID": "",
	    "ImpersonationUserID": "",
	    "SecurityProfileID": "",
	    "UserID": ""
	}


| Name | Type | Description | Required | 
|---|---|---|---|
| ID | string | ID of the impersonation config. Can only contain characters Aa-Zz, 0-9, -, and _. Searchable: priority level 8. Sortable: priority level 8. | False |
| ImpersonationBuyerID | string | ID of the impersonation buyer. Searchable: priority level 0. Sortable: priority level 0. | False |
| ImpersonationGroupID | string | ID of the impersonation group. Searchable: priority level 1. Sortable: priority level 1. | False |
| ImpersonationUserID | string | ID of the impersonation user. Searchable: priority level 2. Sortable: priority level 2. | False |
| BuyerID | string | ID of the buyer. Required. Searchable: priority level 3. Sortable: priority level 3. | True |
| GroupID | string | ID of the group. Searchable: priority level 4. Sortable: priority level 4. | False |
| UserID | string | ID of the user. Searchable: priority level 5. Sortable: priority level 5. | False |
| SecurityProfileID | string | ID of the security profile. Required. Searchable: priority level 6. Sortable: priority level 6. | True |
| ClientID | string | ID of the client. Required. Searchable: priority level 7. Sortable: priority level 7. | True |

## Response Body
	:::json
	{
	    "BuyerID": "",
	    "ClientID": "",
	    "GroupID": "",
	    "ID": "",
	    "ImpersonationBuyerID": "",
	    "ImpersonationGroupID": "",
	    "ImpersonationUserID": "",
	    "SecurityProfileID": "",
	    "UserID": ""
	}


| Name | Type | Description | Required | 
|---|---|---|---|
| ID | string | ID of the impersonation config. | False |
| ImpersonationBuyerID | string | ID of the impersonation buyer. | False |
| ImpersonationGroupID | string | ID of the impersonation group. | False |
| ImpersonationUserID | string | ID of the impersonation user. | False |
| BuyerID | string | ID of the buyer. | True |
| GroupID | string | ID of the group. | False |
| UserID | string | ID of the user. | False |
| SecurityProfileID | string | ID of the security profile. | True |
| ClientID | string | ID of the client. | True |

## `DELETE` `v1/impersonationconfig/{impersonationConfigID}`
Delete an impersonation config

| Name | Type | Description | Required | 
|---|---|---|---|
| impersonationConfigID | string | ID of the impersonation config. | True |

## Response Body
## `PATCH` `v1/impersonationconfig/{impersonationConfigID}`
Partially update an impersonation config

| Name | Type | Description | Required | 
|---|---|---|---|
| impersonationConfigID | string | ID of the impersonation config. | True |

## Request Body
	:::json
	{
	    "BuyerID": "",
	    "ClientID": "",
	    "GroupID": "",
	    "ID": "",
	    "ImpersonationBuyerID": "",
	    "ImpersonationGroupID": "",
	    "ImpersonationUserID": "",
	    "SecurityProfileID": "",
	    "UserID": ""
	}


| Name | Type | Description | Required | 
|---|---|---|---|
| ID | string | ID of the impersonation config. Can only contain characters Aa-Zz, 0-9, -, and _. Searchable: priority level 8. Sortable: priority level 8. | False |
| ImpersonationBuyerID | string | ID of the impersonation buyer. Searchable: priority level 0. Sortable: priority level 0. | False |
| ImpersonationGroupID | string | ID of the impersonation group. Searchable: priority level 1. Sortable: priority level 1. | False |
| ImpersonationUserID | string | ID of the impersonation user. Searchable: priority level 2. Sortable: priority level 2. | False |
| BuyerID | string | ID of the buyer. Required. Searchable: priority level 3. Sortable: priority level 3. | True |
| GroupID | string | ID of the group. Searchable: priority level 4. Sortable: priority level 4. | False |
| UserID | string | ID of the user. Searchable: priority level 5. Sortable: priority level 5. | False |
| SecurityProfileID | string | ID of the security profile. Required. Searchable: priority level 6. Sortable: priority level 6. | True |
| ClientID | string | ID of the client. Required. Searchable: priority level 7. Sortable: priority level 7. | True |

## Response Body
	:::json
	{
	    "BuyerID": "",
	    "ClientID": "",
	    "GroupID": "",
	    "ID": "",
	    "ImpersonationBuyerID": "",
	    "ImpersonationGroupID": "",
	    "ImpersonationUserID": "",
	    "SecurityProfileID": "",
	    "UserID": ""
	}


| Name | Type | Description | Required | 
|---|---|---|---|
| ID | string | ID of the impersonation config. | False |
| ImpersonationBuyerID | string | ID of the impersonation buyer. | False |
| ImpersonationGroupID | string | ID of the impersonation group. | False |
| ImpersonationUserID | string | ID of the impersonation user. | False |
| BuyerID | string | ID of the buyer. | True |
| GroupID | string | ID of the group. | False |
| UserID | string | ID of the user. | False |
| SecurityProfileID | string | ID of the security profile. | True |
| ClientID | string | ID of the client. | True |
