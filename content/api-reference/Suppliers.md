---
title: Suppliers
date: 2018-03-27
category: API Reference
tags: Suppliers
slug: Suppliers-Suppliers
---
Suppliers are the organizations that supply products distributed by
Seller oganizations.

---

## `GET` `v1/suppliers/{supplierID}`
Get a single supplier

| Name | Type | Description | Required | 
|---|---|---|---|
| supplierID | string | ID of the supplier. | True |

## Response Body
	{
	    "Active": false,
	    "ID": "",
	    "Name": "",
	    "xp": {}
	}
| Name | Type | Description | Required | 
|---|---|---|---|
| ID | string | ID of the supplier. | False |
| Name | string | Name of the supplier. | True |
| Active | boolean | Active of the supplier. | False |
| xp | object | Container for extended (custom) properties of the supplier. | False |

## `GET` `v1/suppliers`
Get a list of suppliers

| Name | Type | Description | Required | 
|---|---|---|---|
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
	            "Active": false,
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
| ID | string | ID of the supplier. | False |
| Name | string | Name of the supplier. | True |
| Active | boolean | Active of the supplier. | False |
| xp | object | Container for extended (custom) properties of the supplier. | False |

## `POST` `v1/suppliers`
Create a new supplier
## Request Body
	{
	    "Active": false,
	    "ID": "",
	    "Name": "",
	    "xp": {}
	}
| Name | Type | Description | Required | 
|---|---|---|---|
| ID | string | ID of the supplier. Can only contain characters Aa-Zz, 0-9, -, and _. Searchable: priority level 2. Sortable: priority level 1. | False |
| Name | string | Name of the supplier. Required. Max length 100 characters. Searchable: priority level 1. Sortable: priority level 2. | True |
| Active | boolean | Active of the supplier. | False |
| xp | object | Container for extended (custom) properties of the supplier. | False |

## Response Body
	{
	    "Active": false,
	    "ID": "",
	    "Name": "",
	    "xp": {}
	}
| Name | Type | Description | Required | 
|---|---|---|---|
| ID | string | ID of the supplier. | False |
| Name | string | Name of the supplier. | True |
| Active | boolean | Active of the supplier. | False |
| xp | object | Container for extended (custom) properties of the supplier. | False |

## `PUT` `v1/suppliers/{supplierID}`
Create or update a supplier

| Name | Type | Description | Required | 
|---|---|---|---|
| supplierID | string | ID of the supplier. | True |

## Request Body
	{
	    "Active": false,
	    "ID": "",
	    "Name": "",
	    "xp": {}
	}
| Name | Type | Description | Required | 
|---|---|---|---|
| ID | string | ID of the supplier. Can only contain characters Aa-Zz, 0-9, -, and _. Searchable: priority level 2. Sortable: priority level 1. | False |
| Name | string | Name of the supplier. Required. Max length 100 characters. Searchable: priority level 1. Sortable: priority level 2. | True |
| Active | boolean | Active of the supplier. | False |
| xp | object | Container for extended (custom) properties of the supplier. | False |

## Response Body
	{
	    "Active": false,
	    "ID": "",
	    "Name": "",
	    "xp": {}
	}
| Name | Type | Description | Required | 
|---|---|---|---|
| ID | string | ID of the supplier. | False |
| Name | string | Name of the supplier. | True |
| Active | boolean | Active of the supplier. | False |
| xp | object | Container for extended (custom) properties of the supplier. | False |

## `DELETE` `v1/suppliers/{supplierID}`
Delete a supplier

| Name | Type | Description | Required | 
|---|---|---|---|
| supplierID | string | ID of the supplier. | True |

## Response Body
## `PATCH` `v1/suppliers/{supplierID}`
Partially update a supplier

| Name | Type | Description | Required | 
|---|---|---|---|
| supplierID | string | ID of the supplier. | True |

## Request Body
	{
	    "Active": false,
	    "ID": "",
	    "Name": "",
	    "xp": {}
	}
| Name | Type | Description | Required | 
|---|---|---|---|
| ID | string | ID of the supplier. Can only contain characters Aa-Zz, 0-9, -, and _. Searchable: priority level 2. Sortable: priority level 1. | False |
| Name | string | Name of the supplier. Required. Max length 100 characters. Searchable: priority level 1. Sortable: priority level 2. | True |
| Active | boolean | Active of the supplier. | False |
| xp | object | Container for extended (custom) properties of the supplier. | False |

## Response Body
	{
	    "Active": false,
	    "ID": "",
	    "Name": "",
	    "xp": {}
	}
| Name | Type | Description | Required | 
|---|---|---|---|
| ID | string | ID of the supplier. | False |
| Name | string | Name of the supplier. | True |
| Active | boolean | Active of the supplier. | False |
| xp | object | Container for extended (custom) properties of the supplier. | False |
