---
title: Catalogs
date: 2018-03-23
category: API Reference
tags: Product Catalogs
slug: Catalogs
---
A Catalog represents a group of categories used to group and place
content for a specific audience. All buyers are issued and assigned a
default catalog upon creation. Catalogs can be shared between buyers
using assignments.

---

## Get a single catalog
### `GET` `v1/catalogs/{catalogID}`

| Parameters      | Description                    |
|------------------|---------------------------------|
| Name            | catalogID                      |
| Type            | string                         |
| Description     | ID of the catalog.             |
| Required        | True                           |

 **Requestbody**: 
None
 **Responsestatus**: `200`

 **Responsebody**: 
{'Sample': '{\r\n  "ID": "",\r\n  "Name": "",\r\n  "Description": "",\r\n  "Active": false,\r\n  "CategoryCount": 0,\r\n  "xp": {}\r\n}', 'Fields': [{'Name': 'ID', 'Type': 'string', 'Description': 'ID of the catalog.', 'Required': False}, {'Name': 'Name', 'Type': 'string', 'Description': 'Name of the catalog.', 'Required': True}, {'Name': 'Description', 'Type': 'string', 'Description': 'Description of the catalog.', 'Required': False}, {'Name': 'Active', 'Type': 'boolean', 'Description': 'Active of the catalog.', 'Required': False}, {'Name': 'CategoryCount', 'Type': 'integer', 'Description': 'Category count of the catalog.', 'Required': False}, {'Name': 'xp', 'Type': 'object', 'Description': 'Container for extended (custom) properties of the catalog.', 'Required': False}]}
## Get a list of catalogs
### `GET` `v1/catalogs`

| Parameters      | Description                    |
|------------------|---------------------------------|
| Name            | search                         |
| Type            | string                         |
| Description     | Word or phrase to search for.  |
| Required        | False                          |
| Name            | searchOn                       |
| Type            | string                         |
| Description     | Comma-delimited list of fields to search on. |
| Required        | False                          |
| Name            | sortBy                         |
| Type            | string                         |
| Description     | Comma-delimited list of fields to sort by. |
| Required        | False                          |
| Name            | page                           |
| Type            | integer                        |
| Description     | Page of results to return. Default: 1 |
| Required        | False                          |
| Name            | pageSize                       |
| Type            | integer                        |
| Description     | Number of results to return per page. Default: 20, max: 100. |
| Required        | False                          |
| Name            | filters                        |
| Type            | object                         |
| Description     | Any additional key/value pairs passed in the query string are interpretted as filters. Valid keys are top-level properties of the returned model or 'xp.???' |
| Required        | False                          |

 **Requestbody**: 
None
 **Responsestatus**: `200`

 **Responsebody**: 
{'Sample': '{\r\n  "Meta": {\r\n    "Page": 1,\r\n    "PageSize": 20,\r\n    "TotalCount": 25,\r\n    "TotalPages": 2,\r\n    "ItemRange": [\r\n      1,\r\n      20\r\n    ]\r\n  },\r\n  "Items": [\r\n    {\r\n      "ID": "",\r\n      "Name": "",\r\n      "Description": "",\r\n      "Active": false,\r\n      "CategoryCount": 0,\r\n      "xp": {}\r\n    }\r\n  ]\r\n}', 'Fields': [{'Name': 'ID', 'Type': 'string', 'Description': 'ID of the catalog.', 'Required': False}, {'Name': 'Name', 'Type': 'string', 'Description': 'Name of the catalog.', 'Required': True}, {'Name': 'Description', 'Type': 'string', 'Description': 'Description of the catalog.', 'Required': False}, {'Name': 'Active', 'Type': 'boolean', 'Description': 'Active of the catalog.', 'Required': False}, {'Name': 'CategoryCount', 'Type': 'integer', 'Description': 'Category count of the catalog.', 'Required': False}, {'Name': 'xp', 'Type': 'object', 'Description': 'Container for extended (custom) properties of the catalog.', 'Required': False}]}
## Create a new catalog
### `POST` `v1/catalogs`

| Parameters      | Description                    |
|------------------|---------------------------------|

 **Requestbody**: 
{'Sample': '{\r\n  "ID": "",\r\n  "Name": "",\r\n  "Description": "",\r\n  "Active": false,\r\n  "xp": {}\r\n}', 'Fields': [{'Name': 'ID', 'Type': 'string', 'Description': 'ID of the catalog. Can only contain characters Aa-Zz, 0-9, -, and _. Searchable: priority level 1. Sortable: priority level 2.', 'Required': False}, {'Name': 'Name', 'Type': 'string', 'Description': 'Name of the catalog. Required. Max length 100 characters. Searchable: priority level 2. Sortable: priority level 1.', 'Required': True}, {'Name': 'Description', 'Type': 'string', 'Description': 'Description of the catalog. Max length 2000 characters. Searchable: priority level 3.', 'Required': False}, {'Name': 'Active', 'Type': 'boolean', 'Description': 'Active of the catalog.', 'Required': False}, {'Name': 'xp', 'Type': 'object', 'Description': 'Container for extended (custom) properties of the catalog.', 'Required': False}]}
 **Responsestatus**: `201`

 **Responsebody**: 
{'Sample': '{\r\n  "ID": "",\r\n  "Name": "",\r\n  "Description": "",\r\n  "Active": false,\r\n  "CategoryCount": 0,\r\n  "xp": {}\r\n}', 'Fields': [{'Name': 'ID', 'Type': 'string', 'Description': 'ID of the catalog.', 'Required': False}, {'Name': 'Name', 'Type': 'string', 'Description': 'Name of the catalog.', 'Required': True}, {'Name': 'Description', 'Type': 'string', 'Description': 'Description of the catalog.', 'Required': False}, {'Name': 'Active', 'Type': 'boolean', 'Description': 'Active of the catalog.', 'Required': False}, {'Name': 'CategoryCount', 'Type': 'integer', 'Description': 'Category count of the catalog.', 'Required': False}, {'Name': 'xp', 'Type': 'object', 'Description': 'Container for extended (custom) properties of the catalog.', 'Required': False}]}
## Create or update a catalog
### `PUT` `v1/catalogs/{catalogID}`

| Parameters      | Description                    |
|------------------|---------------------------------|
| Name            | catalogID                      |
| Type            | string                         |
| Description     | ID of the catalog.             |
| Required        | True                           |

 **Requestbody**: 
{'Sample': '{\r\n  "ID": "",\r\n  "Name": "",\r\n  "Description": "",\r\n  "Active": false,\r\n  "xp": {}\r\n}', 'Fields': [{'Name': 'ID', 'Type': 'string', 'Description': 'ID of the catalog. Can only contain characters Aa-Zz, 0-9, -, and _. Searchable: priority level 1. Sortable: priority level 2.', 'Required': False}, {'Name': 'Name', 'Type': 'string', 'Description': 'Name of the catalog. Required. Max length 100 characters. Searchable: priority level 2. Sortable: priority level 1.', 'Required': True}, {'Name': 'Description', 'Type': 'string', 'Description': 'Description of the catalog. Max length 2000 characters. Searchable: priority level 3.', 'Required': False}, {'Name': 'Active', 'Type': 'boolean', 'Description': 'Active of the catalog.', 'Required': False}, {'Name': 'xp', 'Type': 'object', 'Description': 'Container for extended (custom) properties of the catalog.', 'Required': False}]}
 **Responsestatus**: `200`

 **Responsebody**: 
{'Sample': '{\r\n  "ID": "",\r\n  "Name": "",\r\n  "Description": "",\r\n  "Active": false,\r\n  "CategoryCount": 0,\r\n  "xp": {}\r\n}', 'Fields': [{'Name': 'ID', 'Type': 'string', 'Description': 'ID of the catalog.', 'Required': False}, {'Name': 'Name', 'Type': 'string', 'Description': 'Name of the catalog.', 'Required': True}, {'Name': 'Description', 'Type': 'string', 'Description': 'Description of the catalog.', 'Required': False}, {'Name': 'Active', 'Type': 'boolean', 'Description': 'Active of the catalog.', 'Required': False}, {'Name': 'CategoryCount', 'Type': 'integer', 'Description': 'Category count of the catalog.', 'Required': False}, {'Name': 'xp', 'Type': 'object', 'Description': 'Container for extended (custom) properties of the catalog.', 'Required': False}]}
## Delete a catalog
### `DELETE` `v1/catalogs/{catalogID}`

| Parameters      | Description                    |
|------------------|---------------------------------|
| Name            | catalogID                      |
| Type            | string                         |
| Description     | ID of the catalog.             |
| Required        | True                           |

 **Requestbody**: 
None
 **Responsestatus**: `204`

 **Responsebody**: 
None
## Partially update a catalog
### `PATCH` `v1/catalogs/{catalogID}`

| Parameters      | Description                    |
|------------------|---------------------------------|
| Name            | catalogID                      |
| Type            | string                         |
| Description     | ID of the catalog.             |
| Required        | True                           |

 **Requestbody**: 
{'Sample': '{\r\n  "ID": "",\r\n  "Name": "",\r\n  "Description": "",\r\n  "Active": false,\r\n  "xp": {}\r\n}', 'Fields': [{'Name': 'ID', 'Type': 'string', 'Description': 'ID of the catalog. Can only contain characters Aa-Zz, 0-9, -, and _. Searchable: priority level 1. Sortable: priority level 2.', 'Required': False}, {'Name': 'Name', 'Type': 'string', 'Description': 'Name of the catalog. Required. Max length 100 characters. Searchable: priority level 2. Sortable: priority level 1.', 'Required': True}, {'Name': 'Description', 'Type': 'string', 'Description': 'Description of the catalog. Max length 2000 characters. Searchable: priority level 3.', 'Required': False}, {'Name': 'Active', 'Type': 'boolean', 'Description': 'Active of the catalog.', 'Required': False}, {'Name': 'xp', 'Type': 'object', 'Description': 'Container for extended (custom) properties of the catalog.', 'Required': False}]}
 **Responsestatus**: `200`

 **Responsebody**: 
{'Sample': '{\r\n  "ID": "",\r\n  "Name": "",\r\n  "Description": "",\r\n  "Active": false,\r\n  "CategoryCount": 0,\r\n  "xp": {}\r\n}', 'Fields': [{'Name': 'ID', 'Type': 'string', 'Description': 'ID of the catalog.', 'Required': False}, {'Name': 'Name', 'Type': 'string', 'Description': 'Name of the catalog.', 'Required': True}, {'Name': 'Description', 'Type': 'string', 'Description': 'Description of the catalog.', 'Required': False}, {'Name': 'Active', 'Type': 'boolean', 'Description': 'Active of the catalog.', 'Required': False}, {'Name': 'CategoryCount', 'Type': 'integer', 'Description': 'Category count of the catalog.', 'Required': False}, {'Name': 'xp', 'Type': 'object', 'Description': 'Container for extended (custom) properties of the catalog.', 'Required': False}]}
## Get a list of catalog assignments
### `GET` `v1/catalogs/assignments`

| Parameters      | Description                    |
|------------------|---------------------------------|
| Name            | catalogID                      |
| Type            | string                         |
| Description     | ID of the catalog.             |
| Required        | False                          |
| Name            | buyerID                        |
| Type            | string                         |
| Description     | ID of the buyer.               |
| Required        | False                          |
| Name            | page                           |
| Type            | integer                        |
| Description     | Page of results to return. Default: 1 |
| Required        | False                          |
| Name            | pageSize                       |
| Type            | integer                        |
| Description     | Number of results to return per page. Default: 20, max: 100. |
| Required        | False                          |

 **Requestbody**: 
None
 **Responsestatus**: `200`

 **Responsebody**: 
{'Sample': '{\r\n  "Meta": {\r\n    "Page": 1,\r\n    "PageSize": 20,\r\n    "TotalCount": 25,\r\n    "TotalPages": 2,\r\n    "ItemRange": [\r\n      1,\r\n      20\r\n    ]\r\n  },\r\n  "Items": [\r\n    {\r\n      "CatalogID": "",\r\n      "BuyerID": "",\r\n      "ViewAllCategories": false,\r\n      "ViewAllProducts": false\r\n    }\r\n  ]\r\n}', 'Fields': [{'Name': 'CatalogID', 'Type': 'string', 'Description': 'ID of the catalog.', 'Required': True}, {'Name': 'BuyerID', 'Type': 'string', 'Description': 'ID of the buyer.', 'Required': True}, {'Name': 'ViewAllCategories', 'Type': 'boolean', 'Description': 'View all categories of the catalog assignment.', 'Required': False}, {'Name': 'ViewAllProducts', 'Type': 'boolean', 'Description': 'View all products of the catalog assignment.', 'Required': False}]}
## Save a catalog assignment
### `POST` `v1/catalogs/assignments`

| Parameters      | Description                    |
|------------------|---------------------------------|

 **Requestbody**: 
{'Sample': '{\r\n  "CatalogID": "",\r\n  "BuyerID": "",\r\n  "ViewAllCategories": false,\r\n  "ViewAllProducts": false\r\n}', 'Fields': [{'Name': 'CatalogID', 'Type': 'string', 'Description': 'ID of the catalog. Required. Sortable: priority level 1.', 'Required': True}, {'Name': 'BuyerID', 'Type': 'string', 'Description': 'ID of the buyer. Required.', 'Required': True}, {'Name': 'ViewAllCategories', 'Type': 'boolean', 'Description': 'View all categories of the catalog assignment.', 'Required': False}, {'Name': 'ViewAllProducts', 'Type': 'boolean', 'Description': 'View all products of the catalog assignment.', 'Required': False}]}
 **Responsestatus**: `204`

 **Responsebody**: 
None
## Delete a catalog assignment
### `DELETE` `v1/catalogs/{catalogID}/assignments`

| Parameters      | Description                    |
|------------------|---------------------------------|
| Name            | catalogID                      |
| Type            | string                         |
| Description     | ID of the catalog.             |
| Required        | True                           |
| Name            | buyerID                        |
| Type            | string                         |
| Description     | ID of the buyer.               |
| Required        | True                           |

 **Requestbody**: 
None
 **Responsestatus**: `204`

 **Responsebody**: 
None
## Get a list of catalog product assignments
### `GET` `v1/catalogs/productassignments`

| Parameters      | Description                    |
|------------------|---------------------------------|
| Name            | catalogID                      |
| Type            | string                         |
| Description     | ID of the catalog.             |
| Required        | False                          |
| Name            | productID                      |
| Type            | string                         |
| Description     | ID of the product.             |
| Required        | False                          |
| Name            | page                           |
| Type            | integer                        |
| Description     | Page of results to return. Default: 1 |
| Required        | False                          |
| Name            | pageSize                       |
| Type            | integer                        |
| Description     | Number of results to return per page. Default: 20, max: 100. |
| Required        | False                          |

 **Requestbody**: 
None
 **Responsestatus**: `200`

 **Responsebody**: 
{'Sample': '{\r\n  "Meta": {\r\n    "Page": 1,\r\n    "PageSize": 20,\r\n    "TotalCount": 25,\r\n    "TotalPages": 2,\r\n    "ItemRange": [\r\n      1,\r\n      20\r\n    ]\r\n  },\r\n  "Items": [\r\n    {\r\n      "CatalogID": "",\r\n      "ProductID": ""\r\n    }\r\n  ]\r\n}', 'Fields': [{'Name': 'CatalogID', 'Type': 'string', 'Description': 'ID of the catalog.', 'Required': True}, {'Name': 'ProductID', 'Type': 'string', 'Description': 'ID of the product.', 'Required': True}]}
## Save a catalog product assignment
### `POST` `v1/catalogs/productassignments`

| Parameters      | Description                    |
|------------------|---------------------------------|

 **Requestbody**: 
{'Sample': '{\r\n  "CatalogID": "",\r\n  "ProductID": ""\r\n}', 'Fields': [{'Name': 'CatalogID', 'Type': 'string', 'Description': 'ID of the catalog. Required.', 'Required': True}, {'Name': 'ProductID', 'Type': 'string', 'Description': 'ID of the product. Required.', 'Required': True}]}
 **Responsestatus**: `204`

 **Responsebody**: 
None
## Delete a catalog product assignment
### `DELETE` `v1/catalogs/{catalogID}/productassignments/{productID}`

| Parameters      | Description                    |
|------------------|---------------------------------|
| Name            | catalogID                      |
| Type            | string                         |
| Description     | ID of the catalog.             |
| Required        | True                           |
| Name            | productID                      |
| Type            | string                         |
| Description     | ID of the product.             |
| Required        | True                           |

 **Requestbody**: 
None
 **Responsestatus**: `204`

 **Responsebody**: 
None