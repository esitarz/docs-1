---
title: Categories
date: 2018-03-23
category: API Reference
tags: Product Catalogs
slug: Categories
---
Categories are used within a catalog to group and place content for a
specific audience. Content can be in the form of another category,
nested categories, products or HTML.

---

## Get a single category
### `GET` `v1/catalogs/{catalogID}/categories/{categoryID}`

| Parameters      | Description                    |
|------------------|---------------------------------|
| Name            | catalogID                      |
| Type            | string                         |
| Description     | ID of the catalog.             |
| Required        | True                           |
| Name            | categoryID                     |
| Type            | string                         |
| Description     | ID of the category.            |
| Required        | True                           |

 **Requestbody**: 
None
 **Responsestatus**: `200`

 **Responsebody**: 
{'Sample': '{\r\n  "ID": "",\r\n  "Name": "",\r\n  "Description": "",\r\n  "ListOrder": 1,\r\n  "Active": false,\r\n  "ParentID": "",\r\n  "ChildCount": 0,\r\n  "xp": {}\r\n}', 'Fields': [{'Name': 'ID', 'Type': 'string', 'Description': 'ID of the category.', 'Required': False}, {'Name': 'Name', 'Type': 'string', 'Description': 'Name of the category.', 'Required': True}, {'Name': 'Description', 'Type': 'string', 'Description': 'Description of the category.', 'Required': False}, {'Name': 'ListOrder', 'Type': 'integer', 'Description': 'Order that the category appears within its parent or catalog (if root level).', 'Required': False}, {'Name': 'Active', 'Type': 'boolean', 'Description': 'If false, buyers cannot see this Category or any Categories or Products under it.', 'Required': False}, {'Name': 'ParentID', 'Type': 'string', 'Description': 'ID of the parent category.', 'Required': False}, {'Name': 'ChildCount', 'Type': 'integer', 'Description': 'Number of categories that are *immediate* children of this category.', 'Required': False}, {'Name': 'xp', 'Type': 'object', 'Description': 'Container for extended (custom) properties of the category.', 'Required': False}]}
## Get a list of categories
### `GET` `v1/catalogs/{catalogID}/categories`

| Parameters      | Description                    |
|------------------|---------------------------------|
| Name            | catalogID                      |
| Type            | string                         |
| Description     | ID of the catalog.             |
| Required        | True                           |
| Name            | depth                          |
| Type            | string                         |
| Description     | Depth of the category.         |
| Required        | False                          |
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
{'Sample': '{\r\n  "Meta": {\r\n    "Page": 1,\r\n    "PageSize": 20,\r\n    "TotalCount": 25,\r\n    "TotalPages": 2,\r\n    "ItemRange": [\r\n      1,\r\n      20\r\n    ]\r\n  },\r\n  "Items": [\r\n    {\r\n      "ID": "",\r\n      "Name": "",\r\n      "Description": "",\r\n      "ListOrder": 1,\r\n      "Active": false,\r\n      "ParentID": "",\r\n      "ChildCount": 0,\r\n      "xp": {}\r\n    }\r\n  ]\r\n}', 'Fields': [{'Name': 'ID', 'Type': 'string', 'Description': 'ID of the category.', 'Required': False}, {'Name': 'Name', 'Type': 'string', 'Description': 'Name of the category.', 'Required': True}, {'Name': 'Description', 'Type': 'string', 'Description': 'Description of the category.', 'Required': False}, {'Name': 'ListOrder', 'Type': 'integer', 'Description': 'Order that the category appears within its parent or catalog (if root level).', 'Required': False}, {'Name': 'Active', 'Type': 'boolean', 'Description': 'If false, buyers cannot see this Category or any Categories or Products under it.', 'Required': False}, {'Name': 'ParentID', 'Type': 'string', 'Description': 'ID of the parent category.', 'Required': False}, {'Name': 'ChildCount', 'Type': 'integer', 'Description': 'Number of categories that are *immediate* children of this category.', 'Required': False}, {'Name': 'xp', 'Type': 'object', 'Description': 'Container for extended (custom) properties of the category.', 'Required': False}]}
## Create a new category
### `POST` `v1/catalogs/{catalogID}/categories`

| Parameters      | Description                    |
|------------------|---------------------------------|
| Name            | catalogID                      |
| Type            | string                         |
| Description     | ID of the catalog.             |
| Required        | True                           |

 **Requestbody**: 
{'Sample': '{\r\n  "ID": "",\r\n  "Name": "",\r\n  "Description": "",\r\n  "ListOrder": 1,\r\n  "Active": false,\r\n  "ParentID": "",\r\n  "xp": {}\r\n}', 'Fields': [{'Name': 'ID', 'Type': 'string', 'Description': 'ID of the category. Can only contain characters Aa-Zz, 0-9, -, and _. Searchable: priority level 1. Sortable.', 'Required': False}, {'Name': 'Name', 'Type': 'string', 'Description': 'Name of the category. Required. Max length 100 characters. Searchable: priority level 2. Sortable.', 'Required': True}, {'Name': 'Description', 'Type': 'string', 'Description': 'Description of the category. Max length 2000 characters. Searchable: priority level 3.', 'Required': False}, {'Name': 'ListOrder', 'Type': 'integer', 'Description': 'Order that the category appears within its parent or catalog (if root level).', 'Required': False}, {'Name': 'Active', 'Type': 'boolean', 'Description': 'If false, buyers cannot see this Category or any Categories or Products under it.', 'Required': False}, {'Name': 'ParentID', 'Type': 'string', 'Description': 'ID of the parent category.', 'Required': False}, {'Name': 'xp', 'Type': 'object', 'Description': 'Container for extended (custom) properties of the category.', 'Required': False}]}
 **Responsestatus**: `201`

 **Responsebody**: 
{'Sample': '{\r\n  "ID": "",\r\n  "Name": "",\r\n  "Description": "",\r\n  "ListOrder": 1,\r\n  "Active": false,\r\n  "ParentID": "",\r\n  "ChildCount": 0,\r\n  "xp": {}\r\n}', 'Fields': [{'Name': 'ID', 'Type': 'string', 'Description': 'ID of the category.', 'Required': False}, {'Name': 'Name', 'Type': 'string', 'Description': 'Name of the category.', 'Required': True}, {'Name': 'Description', 'Type': 'string', 'Description': 'Description of the category.', 'Required': False}, {'Name': 'ListOrder', 'Type': 'integer', 'Description': 'Order that the category appears within its parent or catalog (if root level).', 'Required': False}, {'Name': 'Active', 'Type': 'boolean', 'Description': 'If false, buyers cannot see this Category or any Categories or Products under it.', 'Required': False}, {'Name': 'ParentID', 'Type': 'string', 'Description': 'ID of the parent category.', 'Required': False}, {'Name': 'ChildCount', 'Type': 'integer', 'Description': 'Number of categories that are *immediate* children of this category.', 'Required': False}, {'Name': 'xp', 'Type': 'object', 'Description': 'Container for extended (custom) properties of the category.', 'Required': False}]}
## Create or update a category
### `PUT` `v1/catalogs/{catalogID}/categories/{categoryID}`

| Parameters      | Description                    |
|------------------|---------------------------------|
| Name            | catalogID                      |
| Type            | string                         |
| Description     | ID of the catalog.             |
| Required        | True                           |
| Name            | categoryID                     |
| Type            | string                         |
| Description     | ID of the category.            |
| Required        | True                           |

 **Requestbody**: 
{'Sample': '{\r\n  "ID": "",\r\n  "Name": "",\r\n  "Description": "",\r\n  "ListOrder": 1,\r\n  "Active": false,\r\n  "ParentID": "",\r\n  "xp": {}\r\n}', 'Fields': [{'Name': 'ID', 'Type': 'string', 'Description': 'ID of the category. Can only contain characters Aa-Zz, 0-9, -, and _. Searchable: priority level 1. Sortable.', 'Required': False}, {'Name': 'Name', 'Type': 'string', 'Description': 'Name of the category. Required. Max length 100 characters. Searchable: priority level 2. Sortable.', 'Required': True}, {'Name': 'Description', 'Type': 'string', 'Description': 'Description of the category. Max length 2000 characters. Searchable: priority level 3.', 'Required': False}, {'Name': 'ListOrder', 'Type': 'integer', 'Description': 'Order that the category appears within its parent or catalog (if root level).', 'Required': False}, {'Name': 'Active', 'Type': 'boolean', 'Description': 'If false, buyers cannot see this Category or any Categories or Products under it.', 'Required': False}, {'Name': 'ParentID', 'Type': 'string', 'Description': 'ID of the parent category.', 'Required': False}, {'Name': 'xp', 'Type': 'object', 'Description': 'Container for extended (custom) properties of the category.', 'Required': False}]}
 **Responsestatus**: `200`

 **Responsebody**: 
{'Sample': '{\r\n  "ID": "",\r\n  "Name": "",\r\n  "Description": "",\r\n  "ListOrder": 1,\r\n  "Active": false,\r\n  "ParentID": "",\r\n  "ChildCount": 0,\r\n  "xp": {}\r\n}', 'Fields': [{'Name': 'ID', 'Type': 'string', 'Description': 'ID of the category.', 'Required': False}, {'Name': 'Name', 'Type': 'string', 'Description': 'Name of the category.', 'Required': True}, {'Name': 'Description', 'Type': 'string', 'Description': 'Description of the category.', 'Required': False}, {'Name': 'ListOrder', 'Type': 'integer', 'Description': 'Order that the category appears within its parent or catalog (if root level).', 'Required': False}, {'Name': 'Active', 'Type': 'boolean', 'Description': 'If false, buyers cannot see this Category or any Categories or Products under it.', 'Required': False}, {'Name': 'ParentID', 'Type': 'string', 'Description': 'ID of the parent category.', 'Required': False}, {'Name': 'ChildCount', 'Type': 'integer', 'Description': 'Number of categories that are *immediate* children of this category.', 'Required': False}, {'Name': 'xp', 'Type': 'object', 'Description': 'Container for extended (custom) properties of the category.', 'Required': False}]}
## Delete a category
### `DELETE` `v1/catalogs/{catalogID}/categories/{categoryID}`

| Parameters      | Description                    |
|------------------|---------------------------------|
| Name            | catalogID                      |
| Type            | string                         |
| Description     | ID of the catalog.             |
| Required        | True                           |
| Name            | categoryID                     |
| Type            | string                         |
| Description     | ID of the category.            |
| Required        | True                           |

 **Requestbody**: 
None
 **Responsestatus**: `204`

 **Responsebody**: 
None
## Partially update a category
### `PATCH` `v1/catalogs/{catalogID}/categories/{categoryID}`

| Parameters      | Description                    |
|------------------|---------------------------------|
| Name            | catalogID                      |
| Type            | string                         |
| Description     | ID of the catalog.             |
| Required        | True                           |
| Name            | categoryID                     |
| Type            | string                         |
| Description     | ID of the category.            |
| Required        | True                           |

 **Requestbody**: 
{'Sample': '{\r\n  "ID": "",\r\n  "Name": "",\r\n  "Description": "",\r\n  "ListOrder": 1,\r\n  "Active": false,\r\n  "ParentID": "",\r\n  "xp": {}\r\n}', 'Fields': [{'Name': 'ID', 'Type': 'string', 'Description': 'ID of the category. Can only contain characters Aa-Zz, 0-9, -, and _. Searchable: priority level 1. Sortable.', 'Required': False}, {'Name': 'Name', 'Type': 'string', 'Description': 'Name of the category. Required. Max length 100 characters. Searchable: priority level 2. Sortable.', 'Required': True}, {'Name': 'Description', 'Type': 'string', 'Description': 'Description of the category. Max length 2000 characters. Searchable: priority level 3.', 'Required': False}, {'Name': 'ListOrder', 'Type': 'integer', 'Description': 'Order that the category appears within its parent or catalog (if root level).', 'Required': False}, {'Name': 'Active', 'Type': 'boolean', 'Description': 'If false, buyers cannot see this Category or any Categories or Products under it.', 'Required': False}, {'Name': 'ParentID', 'Type': 'string', 'Description': 'ID of the parent category.', 'Required': False}, {'Name': 'xp', 'Type': 'object', 'Description': 'Container for extended (custom) properties of the category.', 'Required': False}]}
 **Responsestatus**: `200`

 **Responsebody**: 
{'Sample': '{\r\n  "ID": "",\r\n  "Name": "",\r\n  "Description": "",\r\n  "ListOrder": 1,\r\n  "Active": false,\r\n  "ParentID": "",\r\n  "ChildCount": 0,\r\n  "xp": {}\r\n}', 'Fields': [{'Name': 'ID', 'Type': 'string', 'Description': 'ID of the category.', 'Required': False}, {'Name': 'Name', 'Type': 'string', 'Description': 'Name of the category.', 'Required': True}, {'Name': 'Description', 'Type': 'string', 'Description': 'Description of the category.', 'Required': False}, {'Name': 'ListOrder', 'Type': 'integer', 'Description': 'Order that the category appears within its parent or catalog (if root level).', 'Required': False}, {'Name': 'Active', 'Type': 'boolean', 'Description': 'If false, buyers cannot see this Category or any Categories or Products under it.', 'Required': False}, {'Name': 'ParentID', 'Type': 'string', 'Description': 'ID of the parent category.', 'Required': False}, {'Name': 'ChildCount', 'Type': 'integer', 'Description': 'Number of categories that are *immediate* children of this category.', 'Required': False}, {'Name': 'xp', 'Type': 'object', 'Description': 'Container for extended (custom) properties of the category.', 'Required': False}]}
## Get a list of category assignments
### `GET` `v1/catalogs/{catalogID}/categories/assignments`

| Parameters      | Description                    |
|------------------|---------------------------------|
| Name            | catalogID                      |
| Type            | string                         |
| Description     | ID of the catalog.             |
| Required        | True                           |
| Name            | categoryID                     |
| Type            | string                         |
| Description     | ID of the category.            |
| Required        | False                          |
| Name            | buyerID                        |
| Type            | string                         |
| Description     | ID of the buyer.               |
| Required        | False                          |
| Name            | userID                         |
| Type            | string                         |
| Description     | ID of the user.                |
| Required        | False                          |
| Name            | userGroupID                    |
| Type            | string                         |
| Description     | ID of the user group.          |
| Required        | False                          |
| Name            | level                          |
| Type            | string                         |
| Description     | Level of the category assignment. Possible values: User, Group, Company. |
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
{'Sample': '{\r\n  "Meta": {\r\n    "Page": 1,\r\n    "PageSize": 20,\r\n    "TotalCount": 25,\r\n    "TotalPages": 2,\r\n    "ItemRange": [\r\n      1,\r\n      20\r\n    ]\r\n  },\r\n  "Items": [\r\n    {\r\n      "CategoryID": "",\r\n      "BuyerID": "",\r\n      "UserGroupID": "",\r\n      "Visible": false,\r\n      "ViewAllProducts": false\r\n    }\r\n  ]\r\n}', 'Fields': [{'Name': 'CategoryID', 'Type': 'string', 'Description': 'ID of the category.', 'Required': True}, {'Name': 'BuyerID', 'Type': 'string', 'Description': 'ID of the buyer.', 'Required': True}, {'Name': 'UserGroupID', 'Type': 'string', 'Description': 'ID of the user group.', 'Required': False}, {'Name': 'Visible', 'Type': 'boolean', 'Description': 'Optional. Set to null to inherit from parent category or catlog level.', 'Required': False}, {'Name': 'ViewAllProducts', 'Type': 'boolean', 'Description': 'Optional. Set to null to inherit from parent category or catlog level.', 'Required': False}]}
## Delete a category assignment
### `DELETE` `v1/catalogs/{catalogID}/categories/{categoryID}/assignments`

| Parameters      | Description                    |
|------------------|---------------------------------|
| Name            | catalogID                      |
| Type            | string                         |
| Description     | ID of the catalog.             |
| Required        | True                           |
| Name            | categoryID                     |
| Type            | string                         |
| Description     | ID of the category.            |
| Required        | True                           |
| Name            | buyerID                        |
| Type            | string                         |
| Description     | ID of the buyer.               |
| Required        | True                           |
| Name            | userID                         |
| Type            | string                         |
| Description     | ID of the user.                |
| Required        | False                          |
| Name            | userGroupID                    |
| Type            | string                         |
| Description     | ID of the user group.          |
| Required        | False                          |

 **Requestbody**: 
None
 **Responsestatus**: `204`

 **Responsebody**: 
None
## Save a category assignment
### `POST` `v1/catalogs/{catalogID}/categories/assignments`

| Parameters      | Description                    |
|------------------|---------------------------------|
| Name            | catalogID                      |
| Type            | string                         |
| Description     | ID of the catalog.             |
| Required        | True                           |

 **Requestbody**: 
{'Sample': '{\r\n  "CategoryID": "",\r\n  "BuyerID": "",\r\n  "UserGroupID": "",\r\n  "Visible": false,\r\n  "ViewAllProducts": false\r\n}', 'Fields': [{'Name': 'CategoryID', 'Type': 'string', 'Description': 'ID of the category. Required. Sortable: priority level 1.', 'Required': True}, {'Name': 'BuyerID', 'Type': 'string', 'Description': 'ID of the buyer. Required. Sortable: priority level 2.', 'Required': True}, {'Name': 'UserGroupID', 'Type': 'string', 'Description': 'ID of the user group.', 'Required': False}, {'Name': 'Visible', 'Type': 'boolean', 'Description': 'Optional. Set to null to inherit from parent category or catlog level.', 'Required': False}, {'Name': 'ViewAllProducts', 'Type': 'boolean', 'Description': 'Optional. Set to null to inherit from parent category or catlog level.', 'Required': False}]}
 **Responsestatus**: `204`

 **Responsebody**: 
None
## Get a list of category product assignments
### `GET` `v1/catalogs/{catalogID}/categories/productassignments`

| Parameters      | Description                    |
|------------------|---------------------------------|
| Name            | catalogID                      |
| Type            | string                         |
| Description     | ID of the catalog.             |
| Required        | True                           |
| Name            | categoryID                     |
| Type            | string                         |
| Description     | ID of the category.            |
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
{'Sample': '{\r\n  "Meta": {\r\n    "Page": 1,\r\n    "PageSize": 20,\r\n    "TotalCount": 25,\r\n    "TotalPages": 2,\r\n    "ItemRange": [\r\n      1,\r\n      20\r\n    ]\r\n  },\r\n  "Items": [\r\n    {\r\n      "CategoryID": "",\r\n      "ProductID": "",\r\n      "ListOrder": 1\r\n    }\r\n  ]\r\n}', 'Fields': [{'Name': 'CategoryID', 'Type': 'string', 'Description': 'ID of the category.', 'Required': True}, {'Name': 'ProductID', 'Type': 'string', 'Description': 'ID of the product.', 'Required': True}, {'Name': 'ListOrder', 'Type': 'integer', 'Description': 'List order of the category product assignment.', 'Required': False}]}
## Save a category product assignment
### `POST` `v1/catalogs/{catalogID}/categories/productassignments`

| Parameters      | Description                    |
|------------------|---------------------------------|
| Name            | catalogID                      |
| Type            | string                         |
| Description     | ID of the catalog.             |
| Required        | True                           |

 **Requestbody**: 
{'Sample': '{\r\n  "CategoryID": "",\r\n  "ProductID": "",\r\n  "ListOrder": 1\r\n}', 'Fields': [{'Name': 'CategoryID', 'Type': 'string', 'Description': 'ID of the category. Required.', 'Required': True}, {'Name': 'ProductID', 'Type': 'string', 'Description': 'ID of the product. Required.', 'Required': True}, {'Name': 'ListOrder', 'Type': 'integer', 'Description': 'List order of the category product assignment.', 'Required': False}]}
 **Responsestatus**: `204`

 **Responsebody**: 
None
## Delete a category product assignment
### `DELETE` `v1/catalogs/{catalogID}/categories/{categoryID}/productassignments/{productID}`

| Parameters      | Description                    |
|------------------|---------------------------------|
| Name            | catalogID                      |
| Type            | string                         |
| Description     | ID of the catalog.             |
| Required        | True                           |
| Name            | categoryID                     |
| Type            | string                         |
| Description     | ID of the category.            |
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