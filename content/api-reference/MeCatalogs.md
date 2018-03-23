---
title: Catalogs
date: 2018-03-23
category: API Reference
tags: Me And My Stuff
slug: MeCatalogs
---
"Me" is a container for read-only endpoints that return a filtered view
of things that the current buyer user is allowed to see, i.e. things
that they are assigned to either directly or as a member of a buyer
organization or user group. It also provides ways for a user to update
or change their own information.

---
## Get a list of catalogs visible to this user
### `GET` `v1/me/catalogs`

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
{'Sample': '{\r\n  "Meta": {\r\n    "Page": 1,\r\n    "PageSize": 20,\r\n    "TotalCount": 25,\r\n    "TotalPages": 2,\r\n    "ItemRange": [\r\n      1,\r\n      20\r\n    ]\r\n  },\r\n  "Items": [\r\n    {\r\n      "ID": "",\r\n      "Name": "",\r\n      "Description": "",\r\n      "Active": false,\r\n      "CategoryCount": 0,\r\n      "xp": {}\r\n    }\r\n  ]\r\n}', 'Fields': [{'Name': 'ID', 'Type': 'string', 'Description': 'ID of the catalog.', 'Required': False}, {'Name': 'Name', 'Type': 'string', 'Description': 'Name of the catalog.', 'Required': True}, {'Name': 'Description', 'Type': 'string', 'Description': 'Description of the catalog.', 'Required': False}, {'Name': 'Active', 'Type': 'boolean', 'Description': 'Active of the catalog.', 'Required': False}, {'Name': 'CategoryCount', 'Type': 'integer', 'Description': 'Category count of the catalog.', 'Required': False}, {'Name': 'xp', 'Type': 'object', 'Description': 'Container for extended (custom) properties of the catalog.', 'Required': False}]}## Get a single catalog
### `GET` `v1/me/catalogs/{catalogID}`

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