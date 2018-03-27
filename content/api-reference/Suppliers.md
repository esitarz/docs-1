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

| Parameters      | Description                    |
|------------------|---------------------------------|


| Parameters      | Description                    |
|------------------|---------------------------------|
| Name            | supplierID                     |
| Type            | string                         |
| Description     | ID of the supplier.            |
| Required        | True                           |

## Request Body
**Response Status**: `200`

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

**Response Status**: `201`

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

| Parameters      | Description                    |
|------------------|---------------------------------|


| Parameters      | Description                    |
|------------------|---------------------------------|
| Name            | supplierID                     |
| Type            | string                         |
| Description     | ID of the supplier.            |
| Required        | True                           |

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

**Response Status**: `200`

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

| Parameters      | Description                    |
|------------------|---------------------------------|


| Parameters      | Description                    |
|------------------|---------------------------------|
| Name            | supplierID                     |
| Type            | string                         |
| Description     | ID of the supplier.            |
| Required        | True                           |

## Request Body
**Response Status**: `204`

## Response Body
## `PATCH` `v1/suppliers/{supplierID}`
Partially update a supplier

| Parameters      | Description                    |
|------------------|---------------------------------|


| Parameters      | Description                    |
|------------------|---------------------------------|
| Name            | supplierID                     |
| Type            | string                         |
| Description     | ID of the supplier.            |
| Required        | True                           |

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

**Response Status**: `200`

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
