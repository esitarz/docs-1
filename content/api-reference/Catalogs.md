---
title: Catalogs
date: 2018-03-27
category: API Reference
tags: Product Catalogs
slug: Product-Catalogs-Catalogs
---
A Catalog represents a group of categories used to group and place
content for a specific audience. All buyers are issued and assigned a
default catalog upon creation. Catalogs can be shared between buyers
using assignments.

---

## `GET` `v1/catalogs/{catalogID}`
Get a single catalog

| Name | Type | Description | Required | 
|---|---|---|---|
| catalogID | string | ID of the catalog. | True |

## Response Body
	{
	    "Active": false,
	    "CategoryCount": 0,
	    "Description": "",
	    "ID": "",
	    "Name": "",
	    "xp": {}
	}
| Name | Type | Description | Required | 
|---|---|---|---|
| ID | string | ID of the catalog. | False |
| Name | string | Name of the catalog. | True |
| Description | string | Description of the catalog. | False |
| Active | boolean | Active of the catalog. | False |
| CategoryCount | integer | Category count of the catalog. | False |
| xp | object | Container for extended (custom) properties of the catalog. | False |

## `GET` `v1/catalogs`
Get a list of catalogs

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
	            "CategoryCount": 0,
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
| ID | string | ID of the catalog. | False |
| Name | string | Name of the catalog. | True |
| Description | string | Description of the catalog. | False |
| Active | boolean | Active of the catalog. | False |
| CategoryCount | integer | Category count of the catalog. | False |
| xp | object | Container for extended (custom) properties of the catalog. | False |

## `POST` `v1/catalogs`
Create a new catalog
## Request Body
	{
	    "Active": false,
	    "Description": "",
	    "ID": "",
	    "Name": "",
	    "xp": {}
	}
| Name | Type | Description | Required | 
|---|---|---|---|
| ID | string | ID of the catalog. Can only contain characters Aa-Zz, 0-9, -, and _. Searchable: priority level 1. Sortable: priority level 2. | False |
| Name | string | Name of the catalog. Required. Max length 100 characters. Searchable: priority level 2. Sortable: priority level 1. | True |
| Description | string | Description of the catalog. Max length 2000 characters. Searchable: priority level 3. | False |
| Active | boolean | Active of the catalog. | False |
| xp | object | Container for extended (custom) properties of the catalog. | False |

## Response Body
	{
	    "Active": false,
	    "CategoryCount": 0,
	    "Description": "",
	    "ID": "",
	    "Name": "",
	    "xp": {}
	}
| Name | Type | Description | Required | 
|---|---|---|---|
| ID | string | ID of the catalog. | False |
| Name | string | Name of the catalog. | True |
| Description | string | Description of the catalog. | False |
| Active | boolean | Active of the catalog. | False |
| CategoryCount | integer | Category count of the catalog. | False |
| xp | object | Container for extended (custom) properties of the catalog. | False |

## `PUT` `v1/catalogs/{catalogID}`
Create or update a catalog

| Name | Type | Description | Required | 
|---|---|---|---|
| catalogID | string | ID of the catalog. | True |

## Request Body
	{
	    "Active": false,
	    "Description": "",
	    "ID": "",
	    "Name": "",
	    "xp": {}
	}
| Name | Type | Description | Required | 
|---|---|---|---|
| ID | string | ID of the catalog. Can only contain characters Aa-Zz, 0-9, -, and _. Searchable: priority level 1. Sortable: priority level 2. | False |
| Name | string | Name of the catalog. Required. Max length 100 characters. Searchable: priority level 2. Sortable: priority level 1. | True |
| Description | string | Description of the catalog. Max length 2000 characters. Searchable: priority level 3. | False |
| Active | boolean | Active of the catalog. | False |
| xp | object | Container for extended (custom) properties of the catalog. | False |

## Response Body
	{
	    "Active": false,
	    "CategoryCount": 0,
	    "Description": "",
	    "ID": "",
	    "Name": "",
	    "xp": {}
	}
| Name | Type | Description | Required | 
|---|---|---|---|
| ID | string | ID of the catalog. | False |
| Name | string | Name of the catalog. | True |
| Description | string | Description of the catalog. | False |
| Active | boolean | Active of the catalog. | False |
| CategoryCount | integer | Category count of the catalog. | False |
| xp | object | Container for extended (custom) properties of the catalog. | False |

## `DELETE` `v1/catalogs/{catalogID}`
Delete a catalog

| Name | Type | Description | Required | 
|---|---|---|---|
| catalogID | string | ID of the catalog. | True |

## Response Body
## `PATCH` `v1/catalogs/{catalogID}`
Partially update a catalog

| Name | Type | Description | Required | 
|---|---|---|---|
| catalogID | string | ID of the catalog. | True |

## Request Body
	{
	    "Active": false,
	    "Description": "",
	    "ID": "",
	    "Name": "",
	    "xp": {}
	}
| Name | Type | Description | Required | 
|---|---|---|---|
| ID | string | ID of the catalog. Can only contain characters Aa-Zz, 0-9, -, and _. Searchable: priority level 1. Sortable: priority level 2. | False |
| Name | string | Name of the catalog. Required. Max length 100 characters. Searchable: priority level 2. Sortable: priority level 1. | True |
| Description | string | Description of the catalog. Max length 2000 characters. Searchable: priority level 3. | False |
| Active | boolean | Active of the catalog. | False |
| xp | object | Container for extended (custom) properties of the catalog. | False |

## Response Body
	{
	    "Active": false,
	    "CategoryCount": 0,
	    "Description": "",
	    "ID": "",
	    "Name": "",
	    "xp": {}
	}
| Name | Type | Description | Required | 
|---|---|---|---|
| ID | string | ID of the catalog. | False |
| Name | string | Name of the catalog. | True |
| Description | string | Description of the catalog. | False |
| Active | boolean | Active of the catalog. | False |
| CategoryCount | integer | Category count of the catalog. | False |
| xp | object | Container for extended (custom) properties of the catalog. | False |

## `GET` `v1/catalogs/assignments`
Get a list of catalog assignments

| Name | Type | Description | Required | 
|---|---|---|---|
| catalogID | string | ID of the catalog. | False |
| buyerID | string | ID of the buyer. | False |
| page | integer | Page of results to return. Default: 1 | False |
| pageSize | integer | Number of results to return per page. Default: 20, max: 100. | False |

## Response Body
	{
	    "Items": [
	        {
	            "BuyerID": "",
	            "CatalogID": "",
	            "ViewAllCategories": false,
	            "ViewAllProducts": false
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
| CatalogID | string | ID of the catalog. | True |
| BuyerID | string | ID of the buyer. | True |
| ViewAllCategories | boolean | View all categories of the catalog assignment. | False |
| ViewAllProducts | boolean | View all products of the catalog assignment. | False |

## `POST` `v1/catalogs/assignments`
Save a catalog assignment
## Request Body
	{
	    "BuyerID": "",
	    "CatalogID": "",
	    "ViewAllCategories": false,
	    "ViewAllProducts": false
	}
| Name | Type | Description | Required | 
|---|---|---|---|
| CatalogID | string | ID of the catalog. Required. Sortable: priority level 1. | True |
| BuyerID | string | ID of the buyer. Required. | True |
| ViewAllCategories | boolean | View all categories of the catalog assignment. | False |
| ViewAllProducts | boolean | View all products of the catalog assignment. | False |

## Response Body
## `DELETE` `v1/catalogs/{catalogID}/assignments`
Delete a catalog assignment

| Name | Type | Description | Required | 
|---|---|---|---|
| catalogID | string | ID of the catalog. | True |
| buyerID | string | ID of the buyer. | True |

## Response Body
## `GET` `v1/catalogs/productassignments`
Get a list of catalog product assignments

| Name | Type | Description | Required | 
|---|---|---|---|
| catalogID | string | ID of the catalog. | False |
| productID | string | ID of the product. | False |
| page | integer | Page of results to return. Default: 1 | False |
| pageSize | integer | Number of results to return per page. Default: 20, max: 100. | False |

## Response Body
	{
	    "Items": [
	        {
	            "CatalogID": "",
	            "ProductID": ""
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
| CatalogID | string | ID of the catalog. | True |
| ProductID | string | ID of the product. | True |

## `POST` `v1/catalogs/productassignments`
Save a catalog product assignment
## Request Body
	{
	    "CatalogID": "",
	    "ProductID": ""
	}
| Name | Type | Description | Required | 
|---|---|---|---|
| CatalogID | string | ID of the catalog. Required. | True |
| ProductID | string | ID of the product. Required. | True |

## Response Body
## `DELETE` `v1/catalogs/{catalogID}/productassignments/{productID}`
Delete a catalog product assignment

| Name | Type | Description | Required | 
|---|---|---|---|
| catalogID | string | ID of the catalog. | True |
| productID | string | ID of the product. | True |

## Response Body