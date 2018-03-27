---
title: Categories
date: 2018-03-27
category: API Reference
tags: Product Catalogs
slug: Product-Catalogs-Categories
---
Categories are used within a catalog to group and place content for a
specific audience. Content can be in the form of another category,
nested categories, products or HTML.

---

## `GET` `v1/catalogs/{catalogID}/categories/{categoryID}`
Get a single category

| Name | Type | Description | Required | 
|---|---|---|---|
| catalogID | string | ID of the catalog. | True |
| categoryID | string | ID of the category. | True |

## Response Body
	{
	    "Active": false,
	    "ChildCount": 0,
	    "Description": "",
	    "ID": "",
	    "ListOrder": 1,
	    "Name": "",
	    "ParentID": "",
	    "xp": {}
	}
| Name | Type | Description | Required | 
|---|---|---|---|
| ID | string | ID of the category. | False |
| Name | string | Name of the category. | True |
| Description | string | Description of the category. | False |
| ListOrder | integer | Order that the category appears within its parent or catalog (if root level). | False |
| Active | boolean | If false, buyers cannot see this Category or any Categories or Products under it. | False |
| ParentID | string | ID of the parent category. | False |
| ChildCount | integer | Number of categories that are *immediate* children of this category. | False |
| xp | object | Container for extended (custom) properties of the category. | False |

## `GET` `v1/catalogs/{catalogID}/categories`
Get a list of categories

| Name | Type | Description | Required | 
|---|---|---|---|
| catalogID | string | ID of the catalog. | True |
| depth | string | Depth of the category. | False |
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
	            "ChildCount": 0,
	            "Description": "",
	            "ID": "",
	            "ListOrder": 1,
	            "Name": "",
	            "ParentID": "",
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
| ID | string | ID of the category. | False |
| Name | string | Name of the category. | True |
| Description | string | Description of the category. | False |
| ListOrder | integer | Order that the category appears within its parent or catalog (if root level). | False |
| Active | boolean | If false, buyers cannot see this Category or any Categories or Products under it. | False |
| ParentID | string | ID of the parent category. | False |
| ChildCount | integer | Number of categories that are *immediate* children of this category. | False |
| xp | object | Container for extended (custom) properties of the category. | False |

## `POST` `v1/catalogs/{catalogID}/categories`
Create a new category

| Name | Type | Description | Required | 
|---|---|---|---|
| catalogID | string | ID of the catalog. | True |

## Request Body
	{
	    "Active": false,
	    "Description": "",
	    "ID": "",
	    "ListOrder": 1,
	    "Name": "",
	    "ParentID": "",
	    "xp": {}
	}
| Name | Type | Description | Required | 
|---|---|---|---|
| ID | string | ID of the category. Can only contain characters Aa-Zz, 0-9, -, and _. Searchable: priority level 1. Sortable. | False |
| Name | string | Name of the category. Required. Max length 100 characters. Searchable: priority level 2. Sortable. | True |
| Description | string | Description of the category. Max length 2000 characters. Searchable: priority level 3. | False |
| ListOrder | integer | Order that the category appears within its parent or catalog (if root level). | False |
| Active | boolean | If false, buyers cannot see this Category or any Categories or Products under it. | False |
| ParentID | string | ID of the parent category. | False |
| xp | object | Container for extended (custom) properties of the category. | False |

## Response Body
	{
	    "Active": false,
	    "ChildCount": 0,
	    "Description": "",
	    "ID": "",
	    "ListOrder": 1,
	    "Name": "",
	    "ParentID": "",
	    "xp": {}
	}
| Name | Type | Description | Required | 
|---|---|---|---|
| ID | string | ID of the category. | False |
| Name | string | Name of the category. | True |
| Description | string | Description of the category. | False |
| ListOrder | integer | Order that the category appears within its parent or catalog (if root level). | False |
| Active | boolean | If false, buyers cannot see this Category or any Categories or Products under it. | False |
| ParentID | string | ID of the parent category. | False |
| ChildCount | integer | Number of categories that are *immediate* children of this category. | False |
| xp | object | Container for extended (custom) properties of the category. | False |

## `PUT` `v1/catalogs/{catalogID}/categories/{categoryID}`
Create or update a category

| Name | Type | Description | Required | 
|---|---|---|---|
| catalogID | string | ID of the catalog. | True |
| categoryID | string | ID of the category. | True |

## Request Body
	{
	    "Active": false,
	    "Description": "",
	    "ID": "",
	    "ListOrder": 1,
	    "Name": "",
	    "ParentID": "",
	    "xp": {}
	}
| Name | Type | Description | Required | 
|---|---|---|---|
| ID | string | ID of the category. Can only contain characters Aa-Zz, 0-9, -, and _. Searchable: priority level 1. Sortable. | False |
| Name | string | Name of the category. Required. Max length 100 characters. Searchable: priority level 2. Sortable. | True |
| Description | string | Description of the category. Max length 2000 characters. Searchable: priority level 3. | False |
| ListOrder | integer | Order that the category appears within its parent or catalog (if root level). | False |
| Active | boolean | If false, buyers cannot see this Category or any Categories or Products under it. | False |
| ParentID | string | ID of the parent category. | False |
| xp | object | Container for extended (custom) properties of the category. | False |

## Response Body
	{
	    "Active": false,
	    "ChildCount": 0,
	    "Description": "",
	    "ID": "",
	    "ListOrder": 1,
	    "Name": "",
	    "ParentID": "",
	    "xp": {}
	}
| Name | Type | Description | Required | 
|---|---|---|---|
| ID | string | ID of the category. | False |
| Name | string | Name of the category. | True |
| Description | string | Description of the category. | False |
| ListOrder | integer | Order that the category appears within its parent or catalog (if root level). | False |
| Active | boolean | If false, buyers cannot see this Category or any Categories or Products under it. | False |
| ParentID | string | ID of the parent category. | False |
| ChildCount | integer | Number of categories that are *immediate* children of this category. | False |
| xp | object | Container for extended (custom) properties of the category. | False |

## `DELETE` `v1/catalogs/{catalogID}/categories/{categoryID}`
Delete a category

| Name | Type | Description | Required | 
|---|---|---|---|
| catalogID | string | ID of the catalog. | True |
| categoryID | string | ID of the category. | True |

## Response Body
## `PATCH` `v1/catalogs/{catalogID}/categories/{categoryID}`
Partially update a category

| Name | Type | Description | Required | 
|---|---|---|---|
| catalogID | string | ID of the catalog. | True |
| categoryID | string | ID of the category. | True |

## Request Body
	{
	    "Active": false,
	    "Description": "",
	    "ID": "",
	    "ListOrder": 1,
	    "Name": "",
	    "ParentID": "",
	    "xp": {}
	}
| Name | Type | Description | Required | 
|---|---|---|---|
| ID | string | ID of the category. Can only contain characters Aa-Zz, 0-9, -, and _. Searchable: priority level 1. Sortable. | False |
| Name | string | Name of the category. Required. Max length 100 characters. Searchable: priority level 2. Sortable. | True |
| Description | string | Description of the category. Max length 2000 characters. Searchable: priority level 3. | False |
| ListOrder | integer | Order that the category appears within its parent or catalog (if root level). | False |
| Active | boolean | If false, buyers cannot see this Category or any Categories or Products under it. | False |
| ParentID | string | ID of the parent category. | False |
| xp | object | Container for extended (custom) properties of the category. | False |

## Response Body
	{
	    "Active": false,
	    "ChildCount": 0,
	    "Description": "",
	    "ID": "",
	    "ListOrder": 1,
	    "Name": "",
	    "ParentID": "",
	    "xp": {}
	}
| Name | Type | Description | Required | 
|---|---|---|---|
| ID | string | ID of the category. | False |
| Name | string | Name of the category. | True |
| Description | string | Description of the category. | False |
| ListOrder | integer | Order that the category appears within its parent or catalog (if root level). | False |
| Active | boolean | If false, buyers cannot see this Category or any Categories or Products under it. | False |
| ParentID | string | ID of the parent category. | False |
| ChildCount | integer | Number of categories that are *immediate* children of this category. | False |
| xp | object | Container for extended (custom) properties of the category. | False |

## `GET` `v1/catalogs/{catalogID}/categories/assignments`
Get a list of category assignments

| Name | Type | Description | Required | 
|---|---|---|---|
| catalogID | string | ID of the catalog. | True |
| categoryID | string | ID of the category. | False |
| buyerID | string | ID of the buyer. | False |
| userID | string | ID of the user. | False |
| userGroupID | string | ID of the user group. | False |
| level | string | Level of the category assignment. Possible values: User, Group, Company. | False |
| page | integer | Page of results to return. Default: 1 | False |
| pageSize | integer | Number of results to return per page. Default: 20, max: 100. | False |

## Response Body
	{
	    "Items": [
	        {
	            "BuyerID": "",
	            "CategoryID": "",
	            "UserGroupID": "",
	            "ViewAllProducts": false,
	            "Visible": false
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
| CategoryID | string | ID of the category. | True |
| BuyerID | string | ID of the buyer. | True |
| UserGroupID | string | ID of the user group. | False |
| Visible | boolean | Optional. Set to null to inherit from parent category or catlog level. | False |
| ViewAllProducts | boolean | Optional. Set to null to inherit from parent category or catlog level. | False |

## `DELETE` `v1/catalogs/{catalogID}/categories/{categoryID}/assignments`
Delete a category assignment

| Name | Type | Description | Required | 
|---|---|---|---|
| catalogID | string | ID of the catalog. | True |
| categoryID | string | ID of the category. | True |
| buyerID | string | ID of the buyer. | True |
| userID | string | ID of the user. | False |
| userGroupID | string | ID of the user group. | False |

## Response Body
## `POST` `v1/catalogs/{catalogID}/categories/assignments`
Save a category assignment

| Name | Type | Description | Required | 
|---|---|---|---|
| catalogID | string | ID of the catalog. | True |

## Request Body
	{
	    "BuyerID": "",
	    "CategoryID": "",
	    "UserGroupID": "",
	    "ViewAllProducts": false,
	    "Visible": false
	}
| Name | Type | Description | Required | 
|---|---|---|---|
| CategoryID | string | ID of the category. Required. Sortable: priority level 1. | True |
| BuyerID | string | ID of the buyer. Required. Sortable: priority level 2. | True |
| UserGroupID | string | ID of the user group. | False |
| Visible | boolean | Optional. Set to null to inherit from parent category or catlog level. | False |
| ViewAllProducts | boolean | Optional. Set to null to inherit from parent category or catlog level. | False |

## Response Body
## `GET` `v1/catalogs/{catalogID}/categories/productassignments`
Get a list of category product assignments

| Name | Type | Description | Required | 
|---|---|---|---|
| catalogID | string | ID of the catalog. | True |
| categoryID | string | ID of the category. | False |
| productID | string | ID of the product. | False |
| page | integer | Page of results to return. Default: 1 | False |
| pageSize | integer | Number of results to return per page. Default: 20, max: 100. | False |

## Response Body
	{
	    "Items": [
	        {
	            "CategoryID": "",
	            "ListOrder": 1,
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
| CategoryID | string | ID of the category. | True |
| ProductID | string | ID of the product. | True |
| ListOrder | integer | List order of the category product assignment. | False |

## `POST` `v1/catalogs/{catalogID}/categories/productassignments`
Save a category product assignment

| Name | Type | Description | Required | 
|---|---|---|---|
| catalogID | string | ID of the catalog. | True |

## Request Body
	{
	    "CategoryID": "",
	    "ListOrder": 1,
	    "ProductID": ""
	}
| Name | Type | Description | Required | 
|---|---|---|---|
| CategoryID | string | ID of the category. Required. | True |
| ProductID | string | ID of the product. Required. | True |
| ListOrder | integer | List order of the category product assignment. | False |

## Response Body
## `DELETE` `v1/catalogs/{catalogID}/categories/{categoryID}/productassignments/{productID}`
Delete a category product assignment

| Name | Type | Description | Required | 
|---|---|---|---|
| catalogID | string | ID of the catalog. | True |
| categoryID | string | ID of the category. | True |
| productID | string | ID of the product. | True |

## Response Body