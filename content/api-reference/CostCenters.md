---
title: Cost Centers
date: 2018-03-23
category: API Reference
tags: Buyers
slug: CostCenters
---
A cost center is used to allocate organizational expenditures. Different
businesses call these by different names such as "allocation codes" or
"charge back codes", but the basic purpose is the same - to allocate an
expense back to someone or some department of an organization.

---

## Get a single cost center
### `GET` `v1/buyers/{buyerID}/costcenters/{costCenterID}`

| Parameters      | Description                    |
|------------------|---------------------------------|
| Name            | buyerID                        |
| Type            | string                         |
| Description     | ID of the buyer.               |
| Required        | True                           |
| Name            | costCenterID                   |
| Type            | string                         |
| Description     | ID of the cost center.         |
| Required        | True                           |

 **Requestbody**: 
None
 **Responsestatus**: `200`

 **Responsebody**: 
{'Sample': '{\r\n  "ID": "",\r\n  "Name": "",\r\n  "Description": "",\r\n  "xp": {}\r\n}', 'Fields': [{'Name': 'ID', 'Type': 'string', 'Description': 'ID of the cost center.', 'Required': False}, {'Name': 'Name', 'Type': 'string', 'Description': 'Name of the cost center.', 'Required': True}, {'Name': 'Description', 'Type': 'string', 'Description': 'Description of the cost center.', 'Required': False}, {'Name': 'xp', 'Type': 'object', 'Description': 'Container for extended (custom) properties of the cost center.', 'Required': False}]}
## Get a list of cost centers
### `GET` `v1/buyers/{buyerID}/costcenters`

| Parameters      | Description                    |
|------------------|---------------------------------|
| Name            | buyerID                        |
| Type            | string                         |
| Description     | ID of the buyer.               |
| Required        | True                           |
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
{'Sample': '{\r\n  "Meta": {\r\n    "Page": 1,\r\n    "PageSize": 20,\r\n    "TotalCount": 25,\r\n    "TotalPages": 2,\r\n    "ItemRange": [\r\n      1,\r\n      20\r\n    ]\r\n  },\r\n  "Items": [\r\n    {\r\n      "ID": "",\r\n      "Name": "",\r\n      "Description": "",\r\n      "xp": {}\r\n    }\r\n  ]\r\n}', 'Fields': [{'Name': 'ID', 'Type': 'string', 'Description': 'ID of the cost center.', 'Required': False}, {'Name': 'Name', 'Type': 'string', 'Description': 'Name of the cost center.', 'Required': True}, {'Name': 'Description', 'Type': 'string', 'Description': 'Description of the cost center.', 'Required': False}, {'Name': 'xp', 'Type': 'object', 'Description': 'Container for extended (custom) properties of the cost center.', 'Required': False}]}
## Create a new cost center
### `POST` `v1/buyers/{buyerID}/costcenters`

| Parameters      | Description                    |
|------------------|---------------------------------|
| Name            | buyerID                        |
| Type            | string                         |
| Description     | ID of the buyer.               |
| Required        | True                           |

 **Requestbody**: 
{'Sample': '{\r\n  "ID": "",\r\n  "Name": "",\r\n  "Description": "",\r\n  "xp": {}\r\n}', 'Fields': [{'Name': 'ID', 'Type': 'string', 'Description': 'ID of the cost center. Can only contain characters Aa-Zz, 0-9, -, and _. Searchable: priority level 1. Sortable: priority level 2.', 'Required': False}, {'Name': 'Name', 'Type': 'string', 'Description': 'Name of the cost center. Required. Max length 100 characters. Searchable: priority level 2. Sortable: priority level 1.', 'Required': True}, {'Name': 'Description', 'Type': 'string', 'Description': 'Description of the cost center. Max length 2000 characters. Searchable: priority level 3.', 'Required': False}, {'Name': 'xp', 'Type': 'object', 'Description': 'Container for extended (custom) properties of the cost center.', 'Required': False}]}
 **Responsestatus**: `201`

 **Responsebody**: 
{'Sample': '{\r\n  "ID": "",\r\n  "Name": "",\r\n  "Description": "",\r\n  "xp": {}\r\n}', 'Fields': [{'Name': 'ID', 'Type': 'string', 'Description': 'ID of the cost center.', 'Required': False}, {'Name': 'Name', 'Type': 'string', 'Description': 'Name of the cost center.', 'Required': True}, {'Name': 'Description', 'Type': 'string', 'Description': 'Description of the cost center.', 'Required': False}, {'Name': 'xp', 'Type': 'object', 'Description': 'Container for extended (custom) properties of the cost center.', 'Required': False}]}
## Create or update a cost center
### `PUT` `v1/buyers/{buyerID}/costcenters/{costCenterID}`

| Parameters      | Description                    |
|------------------|---------------------------------|
| Name            | buyerID                        |
| Type            | string                         |
| Description     | ID of the buyer.               |
| Required        | True                           |
| Name            | costCenterID                   |
| Type            | string                         |
| Description     | ID of the cost center.         |
| Required        | True                           |

 **Requestbody**: 
{'Sample': '{\r\n  "ID": "",\r\n  "Name": "",\r\n  "Description": "",\r\n  "xp": {}\r\n}', 'Fields': [{'Name': 'ID', 'Type': 'string', 'Description': 'ID of the cost center. Can only contain characters Aa-Zz, 0-9, -, and _. Searchable: priority level 1. Sortable: priority level 2.', 'Required': False}, {'Name': 'Name', 'Type': 'string', 'Description': 'Name of the cost center. Required. Max length 100 characters. Searchable: priority level 2. Sortable: priority level 1.', 'Required': True}, {'Name': 'Description', 'Type': 'string', 'Description': 'Description of the cost center. Max length 2000 characters. Searchable: priority level 3.', 'Required': False}, {'Name': 'xp', 'Type': 'object', 'Description': 'Container for extended (custom) properties of the cost center.', 'Required': False}]}
 **Responsestatus**: `200`

 **Responsebody**: 
{'Sample': '{\r\n  "ID": "",\r\n  "Name": "",\r\n  "Description": "",\r\n  "xp": {}\r\n}', 'Fields': [{'Name': 'ID', 'Type': 'string', 'Description': 'ID of the cost center.', 'Required': False}, {'Name': 'Name', 'Type': 'string', 'Description': 'Name of the cost center.', 'Required': True}, {'Name': 'Description', 'Type': 'string', 'Description': 'Description of the cost center.', 'Required': False}, {'Name': 'xp', 'Type': 'object', 'Description': 'Container for extended (custom) properties of the cost center.', 'Required': False}]}
## Delete a cost center
### `DELETE` `v1/buyers/{buyerID}/costcenters/{costCenterID}`

| Parameters      | Description                    |
|------------------|---------------------------------|
| Name            | buyerID                        |
| Type            | string                         |
| Description     | ID of the buyer.               |
| Required        | True                           |
| Name            | costCenterID                   |
| Type            | string                         |
| Description     | ID of the cost center.         |
| Required        | True                           |

 **Requestbody**: 
None
 **Responsestatus**: `204`

 **Responsebody**: 
None
## Partially update a cost center
### `PATCH` `v1/buyers/{buyerID}/costcenters/{costCenterID}`

| Parameters      | Description                    |
|------------------|---------------------------------|
| Name            | buyerID                        |
| Type            | string                         |
| Description     | ID of the buyer.               |
| Required        | True                           |
| Name            | costCenterID                   |
| Type            | string                         |
| Description     | ID of the cost center.         |
| Required        | True                           |

 **Requestbody**: 
{'Sample': '{\r\n  "ID": "",\r\n  "Name": "",\r\n  "Description": "",\r\n  "xp": {}\r\n}', 'Fields': [{'Name': 'ID', 'Type': 'string', 'Description': 'ID of the cost center. Can only contain characters Aa-Zz, 0-9, -, and _. Searchable: priority level 1. Sortable: priority level 2.', 'Required': False}, {'Name': 'Name', 'Type': 'string', 'Description': 'Name of the cost center. Required. Max length 100 characters. Searchable: priority level 2. Sortable: priority level 1.', 'Required': True}, {'Name': 'Description', 'Type': 'string', 'Description': 'Description of the cost center. Max length 2000 characters. Searchable: priority level 3.', 'Required': False}, {'Name': 'xp', 'Type': 'object', 'Description': 'Container for extended (custom) properties of the cost center.', 'Required': False}]}
 **Responsestatus**: `200`

 **Responsebody**: 
{'Sample': '{\r\n  "ID": "",\r\n  "Name": "",\r\n  "Description": "",\r\n  "xp": {}\r\n}', 'Fields': [{'Name': 'ID', 'Type': 'string', 'Description': 'ID of the cost center.', 'Required': False}, {'Name': 'Name', 'Type': 'string', 'Description': 'Name of the cost center.', 'Required': True}, {'Name': 'Description', 'Type': 'string', 'Description': 'Description of the cost center.', 'Required': False}, {'Name': 'xp', 'Type': 'object', 'Description': 'Container for extended (custom) properties of the cost center.', 'Required': False}]}
## Get a list of cost center assignments
### `GET` `v1/buyers/{buyerID}/costcenters/assignments`

| Parameters      | Description                    |
|------------------|---------------------------------|
| Name            | buyerID                        |
| Type            | string                         |
| Description     | ID of the buyer.               |
| Required        | True                           |
| Name            | costCenterID                   |
| Type            | string                         |
| Description     | ID of the cost center.         |
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
| Description     | Level of the cost center assignment. Possible values: User, Group, Company. |
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
{'Sample': '{\r\n  "Meta": {\r\n    "Page": 1,\r\n    "PageSize": 20,\r\n    "TotalCount": 25,\r\n    "TotalPages": 2,\r\n    "ItemRange": [\r\n      1,\r\n      20\r\n    ]\r\n  },\r\n  "Items": [\r\n    {\r\n      "CostCenterID": "",\r\n      "UserGroupID": ""\r\n    }\r\n  ]\r\n}', 'Fields': [{'Name': 'CostCenterID', 'Type': 'string', 'Description': 'ID of the cost center.', 'Required': True}, {'Name': 'UserGroupID', 'Type': 'string', 'Description': 'ID of the user group.', 'Required': False}]}
## Delete a cost center assignment
### `DELETE` `v1/buyers/{buyerID}/costcenters/{costCenterID}/assignments`

| Parameters      | Description                    |
|------------------|---------------------------------|
| Name            | buyerID                        |
| Type            | string                         |
| Description     | ID of the buyer.               |
| Required        | True                           |
| Name            | costCenterID                   |
| Type            | string                         |
| Description     | ID of the cost center.         |
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
## Save a cost center assignment
### `POST` `v1/buyers/{buyerID}/costcenters/assignments`

| Parameters      | Description                    |
|------------------|---------------------------------|
| Name            | buyerID                        |
| Type            | string                         |
| Description     | ID of the buyer.               |
| Required        | True                           |

 **Requestbody**: 
{'Sample': '{\r\n  "CostCenterID": "",\r\n  "UserGroupID": ""\r\n}', 'Fields': [{'Name': 'CostCenterID', 'Type': 'string', 'Description': 'ID of the cost center. Required. Sortable: priority level 1.', 'Required': True}, {'Name': 'UserGroupID', 'Type': 'string', 'Description': 'ID of the user group. Sortable: priority level 3.', 'Required': False}]}
 **Responsestatus**: `204`

 **Responsebody**: 
None