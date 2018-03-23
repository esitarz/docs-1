---
title: Suppliers
date: 2018-03-23
category: API Reference
tags: Suppliers
slug: Suppliers
---
Suppliers are the organizations that supply products distributed by
Seller oganizations.

---

## Get a single supplier
### `GET` `v1/suppliers/{supplierID}`

| Parameters      | Description                    |
|------------------|---------------------------------|
| Name            | supplierID                     |
| Type            | string                         |
| Description     | ID of the supplier.            |
| Required        | True                           |

 **Requestbody**: 
None
 **Responsestatus**: `200`

 **Responsebody**: 
{'Sample': '{\r\n  "ID": "",\r\n  "Name": "",\r\n  "Active": false,\r\n  "xp": {}\r\n}', 'Fields': [{'Name': 'ID', 'Type': 'string', 'Description': 'ID of the supplier.', 'Required': False}, {'Name': 'Name', 'Type': 'string', 'Description': 'Name of the supplier.', 'Required': True}, {'Name': 'Active', 'Type': 'boolean', 'Description': 'Active of the supplier.', 'Required': False}, {'Name': 'xp', 'Type': 'object', 'Description': 'Container for extended (custom) properties of the supplier.', 'Required': False}]}
## Get a list of suppliers
### `GET` `v1/suppliers`

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
{'Sample': '{\r\n  "Meta": {\r\n    "Page": 1,\r\n    "PageSize": 20,\r\n    "TotalCount": 25,\r\n    "TotalPages": 2,\r\n    "ItemRange": [\r\n      1,\r\n      20\r\n    ]\r\n  },\r\n  "Items": [\r\n    {\r\n      "ID": "",\r\n      "Name": "",\r\n      "Active": false,\r\n      "xp": {}\r\n    }\r\n  ]\r\n}', 'Fields': [{'Name': 'ID', 'Type': 'string', 'Description': 'ID of the supplier.', 'Required': False}, {'Name': 'Name', 'Type': 'string', 'Description': 'Name of the supplier.', 'Required': True}, {'Name': 'Active', 'Type': 'boolean', 'Description': 'Active of the supplier.', 'Required': False}, {'Name': 'xp', 'Type': 'object', 'Description': 'Container for extended (custom) properties of the supplier.', 'Required': False}]}
## Create a new supplier
### `POST` `v1/suppliers`

| Parameters      | Description                    |
|------------------|---------------------------------|

 **Requestbody**: 
{'Sample': '{\r\n  "ID": "",\r\n  "Name": "",\r\n  "Active": false,\r\n  "xp": {}\r\n}', 'Fields': [{'Name': 'ID', 'Type': 'string', 'Description': 'ID of the supplier. Can only contain characters Aa-Zz, 0-9, -, and _. Searchable: priority level 2. Sortable: priority level 1.', 'Required': False}, {'Name': 'Name', 'Type': 'string', 'Description': 'Name of the supplier. Required. Max length 100 characters. Searchable: priority level 1. Sortable: priority level 2.', 'Required': True}, {'Name': 'Active', 'Type': 'boolean', 'Description': 'Active of the supplier.', 'Required': False}, {'Name': 'xp', 'Type': 'object', 'Description': 'Container for extended (custom) properties of the supplier.', 'Required': False}]}
 **Responsestatus**: `201`

 **Responsebody**: 
{'Sample': '{\r\n  "ID": "",\r\n  "Name": "",\r\n  "Active": false,\r\n  "xp": {}\r\n}', 'Fields': [{'Name': 'ID', 'Type': 'string', 'Description': 'ID of the supplier.', 'Required': False}, {'Name': 'Name', 'Type': 'string', 'Description': 'Name of the supplier.', 'Required': True}, {'Name': 'Active', 'Type': 'boolean', 'Description': 'Active of the supplier.', 'Required': False}, {'Name': 'xp', 'Type': 'object', 'Description': 'Container for extended (custom) properties of the supplier.', 'Required': False}]}
## Create or update a supplier
### `PUT` `v1/suppliers/{supplierID}`

| Parameters      | Description                    |
|------------------|---------------------------------|
| Name            | supplierID                     |
| Type            | string                         |
| Description     | ID of the supplier.            |
| Required        | True                           |

 **Requestbody**: 
{'Sample': '{\r\n  "ID": "",\r\n  "Name": "",\r\n  "Active": false,\r\n  "xp": {}\r\n}', 'Fields': [{'Name': 'ID', 'Type': 'string', 'Description': 'ID of the supplier. Can only contain characters Aa-Zz, 0-9, -, and _. Searchable: priority level 2. Sortable: priority level 1.', 'Required': False}, {'Name': 'Name', 'Type': 'string', 'Description': 'Name of the supplier. Required. Max length 100 characters. Searchable: priority level 1. Sortable: priority level 2.', 'Required': True}, {'Name': 'Active', 'Type': 'boolean', 'Description': 'Active of the supplier.', 'Required': False}, {'Name': 'xp', 'Type': 'object', 'Description': 'Container for extended (custom) properties of the supplier.', 'Required': False}]}
 **Responsestatus**: `200`

 **Responsebody**: 
{'Sample': '{\r\n  "ID": "",\r\n  "Name": "",\r\n  "Active": false,\r\n  "xp": {}\r\n}', 'Fields': [{'Name': 'ID', 'Type': 'string', 'Description': 'ID of the supplier.', 'Required': False}, {'Name': 'Name', 'Type': 'string', 'Description': 'Name of the supplier.', 'Required': True}, {'Name': 'Active', 'Type': 'boolean', 'Description': 'Active of the supplier.', 'Required': False}, {'Name': 'xp', 'Type': 'object', 'Description': 'Container for extended (custom) properties of the supplier.', 'Required': False}]}
## Delete a supplier
### `DELETE` `v1/suppliers/{supplierID}`

| Parameters      | Description                    |
|------------------|---------------------------------|
| Name            | supplierID                     |
| Type            | string                         |
| Description     | ID of the supplier.            |
| Required        | True                           |

 **Requestbody**: 
None
 **Responsestatus**: `204`

 **Responsebody**: 
None
## Partially update a supplier
### `PATCH` `v1/suppliers/{supplierID}`

| Parameters      | Description                    |
|------------------|---------------------------------|
| Name            | supplierID                     |
| Type            | string                         |
| Description     | ID of the supplier.            |
| Required        | True                           |

 **Requestbody**: 
{'Sample': '{\r\n  "ID": "",\r\n  "Name": "",\r\n  "Active": false,\r\n  "xp": {}\r\n}', 'Fields': [{'Name': 'ID', 'Type': 'string', 'Description': 'ID of the supplier. Can only contain characters Aa-Zz, 0-9, -, and _. Searchable: priority level 2. Sortable: priority level 1.', 'Required': False}, {'Name': 'Name', 'Type': 'string', 'Description': 'Name of the supplier. Required. Max length 100 characters. Searchable: priority level 1. Sortable: priority level 2.', 'Required': True}, {'Name': 'Active', 'Type': 'boolean', 'Description': 'Active of the supplier.', 'Required': False}, {'Name': 'xp', 'Type': 'object', 'Description': 'Container for extended (custom) properties of the supplier.', 'Required': False}]}
 **Responsestatus**: `200`

 **Responsebody**: 
{'Sample': '{\r\n  "ID": "",\r\n  "Name": "",\r\n  "Active": false,\r\n  "xp": {}\r\n}', 'Fields': [{'Name': 'ID', 'Type': 'string', 'Description': 'ID of the supplier.', 'Required': False}, {'Name': 'Name', 'Type': 'string', 'Description': 'Name of the supplier.', 'Required': True}, {'Name': 'Active', 'Type': 'boolean', 'Description': 'Active of the supplier.', 'Required': False}, {'Name': 'xp', 'Type': 'object', 'Description': 'Container for extended (custom) properties of the supplier.', 'Required': False}]}