---
title: Incrementors
date: 2018-03-23
category: API Reference
tags: Seller
slug: Incrementors
---
An incrementor is used to add an atomically incremented number to your
object IDs. For example, "aprefix-{myIncrementorID}", will yield an
order ID of aprefix-10010.

---
## Get a single incrementor
### `GET` `v1/incrementors/{incrementorID}`

| Parameters      | Description                    |
|------------------|---------------------------------|
| Name            | incrementorID                  |
| Type            | string                         |
| Description     | ID of the incrementor.         |
| Required        | True                           |

 **Requestbody**: 
None
 **Responsestatus**: `200`

 **Responsebody**: 
{'Sample': '{\r\n  "ID": "",\r\n  "Name": "",\r\n  "LastNumber": 0,\r\n  "LeftPaddingCount": 0\r\n}', 'Fields': [{'Name': 'ID', 'Type': 'string', 'Description': 'ID of the incrementor.', 'Required': False}, {'Name': 'Name', 'Type': 'string', 'Description': 'Name of the incrementor.', 'Required': False}, {'Name': 'LastNumber', 'Type': 'integer', 'Description': 'Last number of the incrementor.', 'Required': True}, {'Name': 'LeftPaddingCount', 'Type': 'integer', 'Description': 'Left padding count of the incrementor.', 'Required': True}]}## Get a list of incrementors
### `GET` `v1/incrementors`

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
{'Sample': '{\r\n  "Meta": {\r\n    "Page": 1,\r\n    "PageSize": 20,\r\n    "TotalCount": 25,\r\n    "TotalPages": 2,\r\n    "ItemRange": [\r\n      1,\r\n      20\r\n    ]\r\n  },\r\n  "Items": [\r\n    {\r\n      "ID": "",\r\n      "Name": "",\r\n      "LastNumber": 0,\r\n      "LeftPaddingCount": 0\r\n    }\r\n  ]\r\n}', 'Fields': [{'Name': 'ID', 'Type': 'string', 'Description': 'ID of the incrementor.', 'Required': False}, {'Name': 'Name', 'Type': 'string', 'Description': 'Name of the incrementor.', 'Required': False}, {'Name': 'LastNumber', 'Type': 'integer', 'Description': 'Last number of the incrementor.', 'Required': True}, {'Name': 'LeftPaddingCount', 'Type': 'integer', 'Description': 'Left padding count of the incrementor.', 'Required': True}]}## Create a new incrementor
### `POST` `v1/incrementors`

| Parameters      | Description                    |
|------------------|---------------------------------|

 **Requestbody**: 
{'Sample': '{\r\n  "ID": "",\r\n  "Name": "",\r\n  "LastNumber": 0,\r\n  "LeftPaddingCount": 0\r\n}', 'Fields': [{'Name': 'ID', 'Type': 'string', 'Description': 'ID of the incrementor. Can only contain characters Aa-Zz, 0-9, -, and _. Searchable: priority level 1. Sortable: priority level 1.', 'Required': False}, {'Name': 'Name', 'Type': 'string', 'Description': 'Name of the incrementor. Max length 100 characters. Searchable: priority level 2. Sortable: priority level 2.', 'Required': False}, {'Name': 'LastNumber', 'Type': 'integer', 'Description': 'Last number of the incrementor. Required. Must be between 0 and 2147483647.', 'Required': True}, {'Name': 'LeftPaddingCount', 'Type': 'integer', 'Description': 'Left padding count of the incrementor. Required. Must be between 0 and 25.', 'Required': True}]}
 **Responsestatus**: `201`

 **Responsebody**: 
{'Sample': '{\r\n  "ID": "",\r\n  "Name": "",\r\n  "LastNumber": 0,\r\n  "LeftPaddingCount": 0\r\n}', 'Fields': [{'Name': 'ID', 'Type': 'string', 'Description': 'ID of the incrementor.', 'Required': False}, {'Name': 'Name', 'Type': 'string', 'Description': 'Name of the incrementor.', 'Required': False}, {'Name': 'LastNumber', 'Type': 'integer', 'Description': 'Last number of the incrementor.', 'Required': True}, {'Name': 'LeftPaddingCount', 'Type': 'integer', 'Description': 'Left padding count of the incrementor.', 'Required': True}]}## Create or update an incrementor
### `PUT` `v1/incrementors/{incrementorID}`

| Parameters      | Description                    |
|------------------|---------------------------------|
| Name            | incrementorID                  |
| Type            | string                         |
| Description     | ID of the incrementor.         |
| Required        | True                           |

 **Requestbody**: 
{'Sample': '{\r\n  "ID": "",\r\n  "Name": "",\r\n  "LastNumber": 0,\r\n  "LeftPaddingCount": 0\r\n}', 'Fields': [{'Name': 'ID', 'Type': 'string', 'Description': 'ID of the incrementor. Can only contain characters Aa-Zz, 0-9, -, and _. Searchable: priority level 1. Sortable: priority level 1.', 'Required': False}, {'Name': 'Name', 'Type': 'string', 'Description': 'Name of the incrementor. Max length 100 characters. Searchable: priority level 2. Sortable: priority level 2.', 'Required': False}, {'Name': 'LastNumber', 'Type': 'integer', 'Description': 'Last number of the incrementor. Required. Must be between 0 and 2147483647.', 'Required': True}, {'Name': 'LeftPaddingCount', 'Type': 'integer', 'Description': 'Left padding count of the incrementor. Required. Must be between 0 and 25.', 'Required': True}]}
 **Responsestatus**: `200`

 **Responsebody**: 
{'Sample': '{\r\n  "ID": "",\r\n  "Name": "",\r\n  "LastNumber": 0,\r\n  "LeftPaddingCount": 0\r\n}', 'Fields': [{'Name': 'ID', 'Type': 'string', 'Description': 'ID of the incrementor.', 'Required': False}, {'Name': 'Name', 'Type': 'string', 'Description': 'Name of the incrementor.', 'Required': False}, {'Name': 'LastNumber', 'Type': 'integer', 'Description': 'Last number of the incrementor.', 'Required': True}, {'Name': 'LeftPaddingCount', 'Type': 'integer', 'Description': 'Left padding count of the incrementor.', 'Required': True}]}## Delete an incrementor
### `DELETE` `v1/incrementors/{incrementorID}`

| Parameters      | Description                    |
|------------------|---------------------------------|
| Name            | incrementorID                  |
| Type            | string                         |
| Description     | ID of the incrementor.         |
| Required        | True                           |

 **Requestbody**: 
None
 **Responsestatus**: `204`

 **Responsebody**: 
None## Partially update an incrementor
### `PATCH` `v1/incrementors/{incrementorID}`

| Parameters      | Description                    |
|------------------|---------------------------------|
| Name            | incrementorID                  |
| Type            | string                         |
| Description     | ID of the incrementor.         |
| Required        | True                           |

 **Requestbody**: 
{'Sample': '{\r\n  "ID": "",\r\n  "Name": "",\r\n  "LastNumber": 0,\r\n  "LeftPaddingCount": 0\r\n}', 'Fields': [{'Name': 'ID', 'Type': 'string', 'Description': 'ID of the incrementor. Can only contain characters Aa-Zz, 0-9, -, and _. Searchable: priority level 1. Sortable: priority level 1.', 'Required': False}, {'Name': 'Name', 'Type': 'string', 'Description': 'Name of the incrementor. Max length 100 characters. Searchable: priority level 2. Sortable: priority level 2.', 'Required': False}, {'Name': 'LastNumber', 'Type': 'integer', 'Description': 'Last number of the incrementor. Required. Must be between 0 and 2147483647.', 'Required': True}, {'Name': 'LeftPaddingCount', 'Type': 'integer', 'Description': 'Left padding count of the incrementor. Required. Must be between 0 and 25.', 'Required': True}]}
 **Responsestatus**: `200`

 **Responsebody**: 
{'Sample': '{\r\n  "ID": "",\r\n  "Name": "",\r\n  "LastNumber": 0,\r\n  "LeftPaddingCount": 0\r\n}', 'Fields': [{'Name': 'ID', 'Type': 'string', 'Description': 'ID of the incrementor.', 'Required': False}, {'Name': 'Name', 'Type': 'string', 'Description': 'Name of the incrementor.', 'Required': False}, {'Name': 'LastNumber', 'Type': 'integer', 'Description': 'Last number of the incrementor.', 'Required': True}, {'Name': 'LeftPaddingCount', 'Type': 'integer', 'Description': 'Left padding count of the incrementor.', 'Required': True}]}