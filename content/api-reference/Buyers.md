---
title: Buyers
date: 2018-03-27
category: API Reference
tags: Buyers
slug: Buyers-Buyers
---
Buyers, or customers, are the organizations that view the categories and
products and place orders.

---

## `GET` `v1/buyers/{buyerID}`
Get a single buyer

| Name | Type | Description | Required | 
|---|---|---|---|
| buyerID | string | ID of the buyer. | True |

## Response Body
	:::json
	{
	    "Active": false,
	    "DefaultCatalogID": "",
	    "ID": "",
	    "Name": "",
	    "xp": {}
	}


| Name | Type | Description | Required | 
|---|---|---|---|
| ID | string | ID of the buyer. | False |
| Name | string | Name of the buyer. | True |
| DefaultCatalogID | string | ID of the default catalog. | False |
| Active | boolean | Active of the buyer. | False |
| xp | object | Container for extended (custom) properties of the buyer. | False |

## `GET` `v1/buyers`
Get a list of buyers

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
	            "Active": false,
	            "DefaultCatalogID": "",
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
| ID | string | ID of the buyer. | False |
| Name | string | Name of the buyer. | True |
| DefaultCatalogID | string | ID of the default catalog. | False |
| Active | boolean | Active of the buyer. | False |
| xp | object | Container for extended (custom) properties of the buyer. | False |

## `POST` `v1/buyers`
Create a new buyer
## Request Body
	:::json
	{
	    "Active": false,
	    "DefaultCatalogID": "",
	    "ID": "",
	    "Name": "",
	    "xp": {}
	}


| Name | Type | Description | Required | 
|---|---|---|---|
| ID | string | ID of the buyer. Can only contain characters Aa-Zz, 0-9, -, and _. Searchable: priority level 2. Sortable: priority level 1. | False |
| Name | string | Name of the buyer. Required. Max length 100 characters. Searchable: priority level 1. Sortable: priority level 2. | True |
| DefaultCatalogID | string | ID of the default catalog. | False |
| Active | boolean | Active of the buyer. | False |
| xp | object | Container for extended (custom) properties of the buyer. | False |

## Response Body
	:::json
	{
	    "Active": false,
	    "DefaultCatalogID": "",
	    "ID": "",
	    "Name": "",
	    "xp": {}
	}


| Name | Type | Description | Required | 
|---|---|---|---|
| ID | string | ID of the buyer. | False |
| Name | string | Name of the buyer. | True |
| DefaultCatalogID | string | ID of the default catalog. | False |
| Active | boolean | Active of the buyer. | False |
| xp | object | Container for extended (custom) properties of the buyer. | False |

## `PUT` `v1/buyers/{buyerID}`
Create or update a buyer

| Name | Type | Description | Required | 
|---|---|---|---|
| buyerID | string | ID of the buyer. | True |

## Request Body
	:::json
	{
	    "Active": false,
	    "DefaultCatalogID": "",
	    "ID": "",
	    "Name": "",
	    "xp": {}
	}


| Name | Type | Description | Required | 
|---|---|---|---|
| ID | string | ID of the buyer. Can only contain characters Aa-Zz, 0-9, -, and _. Searchable: priority level 2. Sortable: priority level 1. | False |
| Name | string | Name of the buyer. Required. Max length 100 characters. Searchable: priority level 1. Sortable: priority level 2. | True |
| DefaultCatalogID | string | ID of the default catalog. | False |
| Active | boolean | Active of the buyer. | False |
| xp | object | Container for extended (custom) properties of the buyer. | False |

## Response Body
	:::json
	{
	    "Active": false,
	    "DefaultCatalogID": "",
	    "ID": "",
	    "Name": "",
	    "xp": {}
	}


| Name | Type | Description | Required | 
|---|---|---|---|
| ID | string | ID of the buyer. | False |
| Name | string | Name of the buyer. | True |
| DefaultCatalogID | string | ID of the default catalog. | False |
| Active | boolean | Active of the buyer. | False |
| xp | object | Container for extended (custom) properties of the buyer. | False |

## `DELETE` `v1/buyers/{buyerID}`
Delete a buyer

| Name | Type | Description | Required | 
|---|---|---|---|
| buyerID | string | ID of the buyer. | True |

## Response Body
## `PATCH` `v1/buyers/{buyerID}`
Partially update a buyer

| Name | Type | Description | Required | 
|---|---|---|---|
| buyerID | string | ID of the buyer. | True |

## Request Body
	:::json
	{
	    "Active": false,
	    "DefaultCatalogID": "",
	    "ID": "",
	    "Name": "",
	    "xp": {}
	}


| Name | Type | Description | Required | 
|---|---|---|---|
| ID | string | ID of the buyer. Can only contain characters Aa-Zz, 0-9, -, and _. Searchable: priority level 2. Sortable: priority level 1. | False |
| Name | string | Name of the buyer. Required. Max length 100 characters. Searchable: priority level 1. Sortable: priority level 2. | True |
| DefaultCatalogID | string | ID of the default catalog. | False |
| Active | boolean | Active of the buyer. | False |
| xp | object | Container for extended (custom) properties of the buyer. | False |

## Response Body
	:::json
	{
	    "Active": false,
	    "DefaultCatalogID": "",
	    "ID": "",
	    "Name": "",
	    "xp": {}
	}


| Name | Type | Description | Required | 
|---|---|---|---|
| ID | string | ID of the buyer. | False |
| Name | string | Name of the buyer. | True |
| DefaultCatalogID | string | ID of the default catalog. | False |
| Active | boolean | Active of the buyer. | False |
| xp | object | Container for extended (custom) properties of the buyer. | False |
