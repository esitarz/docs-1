---
title: Buyers
date: 2018-03-23
category: API Reference
tags: Buyers
slug: Buyers
---
Buyers, or customers, are the organizations that view the categories and
products and place orders.

---
## Get a single buyer
### `GET` `v1/buyers/{buyerID}`

| Parameters      | Description                    |
|------------------|---------------------------------|
| Name            | buyerID                        |
| Type            | string                         |
| Description     | ID of the buyer.               |
| Required        | True                           |

 **Requestbody**: 
None
 **Responsestatus**: `200`

 **Responsebody**: 
{'Sample': '{\r\n  "ID": "",\r\n  "Name": "",\r\n  "DefaultCatalogID": "",\r\n  "Active": false,\r\n  "xp": {}\r\n}', 'Fields': [{'Name': 'ID', 'Type': 'string', 'Description': 'ID of the buyer.', 'Required': False}, {'Name': 'Name', 'Type': 'string', 'Description': 'Name of the buyer.', 'Required': True}, {'Name': 'DefaultCatalogID', 'Type': 'string', 'Description': 'ID of the default catalog.', 'Required': False}, {'Name': 'Active', 'Type': 'boolean', 'Description': 'Active of the buyer.', 'Required': False}, {'Name': 'xp', 'Type': 'object', 'Description': 'Container for extended (custom) properties of the buyer.', 'Required': False}]}## Get a list of buyers
### `GET` `v1/buyers`

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
{'Sample': '{\r\n  "Meta": {\r\n    "Page": 1,\r\n    "PageSize": 20,\r\n    "TotalCount": 25,\r\n    "TotalPages": 2,\r\n    "ItemRange": [\r\n      1,\r\n      20\r\n    ]\r\n  },\r\n  "Items": [\r\n    {\r\n      "ID": "",\r\n      "Name": "",\r\n      "DefaultCatalogID": "",\r\n      "Active": false,\r\n      "xp": {}\r\n    }\r\n  ]\r\n}', 'Fields': [{'Name': 'ID', 'Type': 'string', 'Description': 'ID of the buyer.', 'Required': False}, {'Name': 'Name', 'Type': 'string', 'Description': 'Name of the buyer.', 'Required': True}, {'Name': 'DefaultCatalogID', 'Type': 'string', 'Description': 'ID of the default catalog.', 'Required': False}, {'Name': 'Active', 'Type': 'boolean', 'Description': 'Active of the buyer.', 'Required': False}, {'Name': 'xp', 'Type': 'object', 'Description': 'Container for extended (custom) properties of the buyer.', 'Required': False}]}## Create a new buyer
### `POST` `v1/buyers`

| Parameters      | Description                    |
|------------------|---------------------------------|

 **Requestbody**: 
{'Sample': '{\r\n  "ID": "",\r\n  "Name": "",\r\n  "DefaultCatalogID": "",\r\n  "Active": false,\r\n  "xp": {}\r\n}', 'Fields': [{'Name': 'ID', 'Type': 'string', 'Description': 'ID of the buyer. Can only contain characters Aa-Zz, 0-9, -, and _. Searchable: priority level 2. Sortable: priority level 1.', 'Required': False}, {'Name': 'Name', 'Type': 'string', 'Description': 'Name of the buyer. Required. Max length 100 characters. Searchable: priority level 1. Sortable: priority level 2.', 'Required': True}, {'Name': 'DefaultCatalogID', 'Type': 'string', 'Description': 'ID of the default catalog.', 'Required': False}, {'Name': 'Active', 'Type': 'boolean', 'Description': 'Active of the buyer.', 'Required': False}, {'Name': 'xp', 'Type': 'object', 'Description': 'Container for extended (custom) properties of the buyer.', 'Required': False}]}
 **Responsestatus**: `201`

 **Responsebody**: 
{'Sample': '{\r\n  "ID": "",\r\n  "Name": "",\r\n  "DefaultCatalogID": "",\r\n  "Active": false,\r\n  "xp": {}\r\n}', 'Fields': [{'Name': 'ID', 'Type': 'string', 'Description': 'ID of the buyer.', 'Required': False}, {'Name': 'Name', 'Type': 'string', 'Description': 'Name of the buyer.', 'Required': True}, {'Name': 'DefaultCatalogID', 'Type': 'string', 'Description': 'ID of the default catalog.', 'Required': False}, {'Name': 'Active', 'Type': 'boolean', 'Description': 'Active of the buyer.', 'Required': False}, {'Name': 'xp', 'Type': 'object', 'Description': 'Container for extended (custom) properties of the buyer.', 'Required': False}]}## Create or update a buyer
### `PUT` `v1/buyers/{buyerID}`

| Parameters      | Description                    |
|------------------|---------------------------------|
| Name            | buyerID                        |
| Type            | string                         |
| Description     | ID of the buyer.               |
| Required        | True                           |

 **Requestbody**: 
{'Sample': '{\r\n  "ID": "",\r\n  "Name": "",\r\n  "DefaultCatalogID": "",\r\n  "Active": false,\r\n  "xp": {}\r\n}', 'Fields': [{'Name': 'ID', 'Type': 'string', 'Description': 'ID of the buyer. Can only contain characters Aa-Zz, 0-9, -, and _. Searchable: priority level 2. Sortable: priority level 1.', 'Required': False}, {'Name': 'Name', 'Type': 'string', 'Description': 'Name of the buyer. Required. Max length 100 characters. Searchable: priority level 1. Sortable: priority level 2.', 'Required': True}, {'Name': 'DefaultCatalogID', 'Type': 'string', 'Description': 'ID of the default catalog.', 'Required': False}, {'Name': 'Active', 'Type': 'boolean', 'Description': 'Active of the buyer.', 'Required': False}, {'Name': 'xp', 'Type': 'object', 'Description': 'Container for extended (custom) properties of the buyer.', 'Required': False}]}
 **Responsestatus**: `200`

 **Responsebody**: 
{'Sample': '{\r\n  "ID": "",\r\n  "Name": "",\r\n  "DefaultCatalogID": "",\r\n  "Active": false,\r\n  "xp": {}\r\n}', 'Fields': [{'Name': 'ID', 'Type': 'string', 'Description': 'ID of the buyer.', 'Required': False}, {'Name': 'Name', 'Type': 'string', 'Description': 'Name of the buyer.', 'Required': True}, {'Name': 'DefaultCatalogID', 'Type': 'string', 'Description': 'ID of the default catalog.', 'Required': False}, {'Name': 'Active', 'Type': 'boolean', 'Description': 'Active of the buyer.', 'Required': False}, {'Name': 'xp', 'Type': 'object', 'Description': 'Container for extended (custom) properties of the buyer.', 'Required': False}]}## Delete a buyer
### `DELETE` `v1/buyers/{buyerID}`

| Parameters      | Description                    |
|------------------|---------------------------------|
| Name            | buyerID                        |
| Type            | string                         |
| Description     | ID of the buyer.               |
| Required        | True                           |

 **Requestbody**: 
None
 **Responsestatus**: `204`

 **Responsebody**: 
None## Partially update a buyer
### `PATCH` `v1/buyers/{buyerID}`

| Parameters      | Description                    |
|------------------|---------------------------------|
| Name            | buyerID                        |
| Type            | string                         |
| Description     | ID of the buyer.               |
| Required        | True                           |

 **Requestbody**: 
{'Sample': '{\r\n  "ID": "",\r\n  "Name": "",\r\n  "DefaultCatalogID": "",\r\n  "Active": false,\r\n  "xp": {}\r\n}', 'Fields': [{'Name': 'ID', 'Type': 'string', 'Description': 'ID of the buyer. Can only contain characters Aa-Zz, 0-9, -, and _. Searchable: priority level 2. Sortable: priority level 1.', 'Required': False}, {'Name': 'Name', 'Type': 'string', 'Description': 'Name of the buyer. Required. Max length 100 characters. Searchable: priority level 1. Sortable: priority level 2.', 'Required': True}, {'Name': 'DefaultCatalogID', 'Type': 'string', 'Description': 'ID of the default catalog.', 'Required': False}, {'Name': 'Active', 'Type': 'boolean', 'Description': 'Active of the buyer.', 'Required': False}, {'Name': 'xp', 'Type': 'object', 'Description': 'Container for extended (custom) properties of the buyer.', 'Required': False}]}
 **Responsestatus**: `200`

 **Responsebody**: 
{'Sample': '{\r\n  "ID": "",\r\n  "Name": "",\r\n  "DefaultCatalogID": "",\r\n  "Active": false,\r\n  "xp": {}\r\n}', 'Fields': [{'Name': 'ID', 'Type': 'string', 'Description': 'ID of the buyer.', 'Required': False}, {'Name': 'Name', 'Type': 'string', 'Description': 'Name of the buyer.', 'Required': True}, {'Name': 'DefaultCatalogID', 'Type': 'string', 'Description': 'ID of the default catalog.', 'Required': False}, {'Name': 'Active', 'Type': 'boolean', 'Description': 'Active of the buyer.', 'Required': False}, {'Name': 'xp', 'Type': 'object', 'Description': 'Container for extended (custom) properties of the buyer.', 'Required': False}]}