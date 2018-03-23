---
title: Security Profiles
date: 2018-03-23
category: API Reference
tags: Authentication And Authorization
slug: SecurityProfiles
---


## Get a single security profile
### `GET` `v1/securityprofiles/{securityProfileID}`

| Parameters      | Description                    |
|------------------|---------------------------------|
| Name            | securityProfileID              |
| Type            | string                         |
| Description     | ID of the security profile.    |
| Required        | True                           |

 **Requestbody**: 
None
 **Responsestatus**: `200`

 **Responsebody**: 
{'Sample': '{\r\n  "ID": "",\r\n  "Name": "",\r\n  "Roles": [\r\n    "DevCenterImpersonate"\r\n  ]\r\n}', 'Fields': [{'Name': 'ID', 'Type': 'string', 'Description': 'ID of the security profile.', 'Required': False}, {'Name': 'Name', 'Type': 'string', 'Description': 'Name of the security profile.', 'Required': True}, {'Name': 'Roles', 'Type': 'array', 'Description': 'Roles of the security profile.', 'Required': False}]}
## Get a list of security profiles
### `GET` `v1/securityprofiles`

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
{'Sample': '{\r\n  "Meta": {\r\n    "Page": 1,\r\n    "PageSize": 20,\r\n    "TotalCount": 25,\r\n    "TotalPages": 2,\r\n    "ItemRange": [\r\n      1,\r\n      20\r\n    ]\r\n  },\r\n  "Items": [\r\n    {\r\n      "ID": "",\r\n      "Name": "",\r\n      "Roles": [\r\n        "DevCenterImpersonate"\r\n      ]\r\n    }\r\n  ]\r\n}', 'Fields': [{'Name': 'ID', 'Type': 'string', 'Description': 'ID of the security profile.', 'Required': False}, {'Name': 'Name', 'Type': 'string', 'Description': 'Name of the security profile.', 'Required': True}, {'Name': 'Roles', 'Type': 'array', 'Description': 'Roles of the security profile.', 'Required': False}]}
## Get a list of security profile assignments
### `GET` `v1/securityprofiles/assignments`

| Parameters      | Description                    |
|------------------|---------------------------------|
| Name            | buyerID                        |
| Type            | string                         |
| Description     | ID of the buyer.               |
| Required        | False                          |
| Name            | supplierID                     |
| Type            | string                         |
| Description     | ID of the supplier.            |
| Required        | False                          |
| Name            | securityProfileID              |
| Type            | string                         |
| Description     | ID of the security profile.    |
| Required        | False                          |
| Name            | userID                         |
| Type            | string                         |
| Description     | ID of the user.                |
| Required        | False                          |
| Name            | userGroupID                    |
| Type            | string                         |
| Description     | ID of the user group.          |
| Required        | False                          |
| Name            | commerceRole                   |
| Type            | string                         |
| Description     | Commerce role of the security profile assignment. Possible values: Buyer, Seller, Supplier. |
| Required        | False                          |
| Name            | level                          |
| Type            | string                         |
| Description     | Level of the security profile assignment. Possible values: User, Group, Company. |
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
{'Sample': '{\r\n  "Meta": {\r\n    "Page": 1,\r\n    "PageSize": 20,\r\n    "TotalCount": 25,\r\n    "TotalPages": 2,\r\n    "ItemRange": [\r\n      1,\r\n      20\r\n    ]\r\n  },\r\n  "Items": [\r\n    {\r\n      "SecurityProfileID": "",\r\n      "BuyerID": "",\r\n      "SupplierID": "",\r\n      "UserID": "",\r\n      "UserGroupID": ""\r\n    }\r\n  ]\r\n}', 'Fields': [{'Name': 'SecurityProfileID', 'Type': 'string', 'Description': 'ID of the security profile.', 'Required': True}, {'Name': 'BuyerID', 'Type': 'string', 'Description': 'ID of the buyer.', 'Required': False}, {'Name': 'SupplierID', 'Type': 'string', 'Description': 'ID of the supplier.', 'Required': False}, {'Name': 'UserID', 'Type': 'string', 'Description': 'ID of the user.', 'Required': False}, {'Name': 'UserGroupID', 'Type': 'string', 'Description': 'ID of the user group.', 'Required': False}]}
## Delete a security profile assignment
### `DELETE` `v1/securityprofiles/{securityProfileID}/assignments`

| Parameters      | Description                    |
|------------------|---------------------------------|
| Name            | securityProfileID              |
| Type            | string                         |
| Description     | ID of the security profile.    |
| Required        | True                           |
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

 **Requestbody**: 
None
 **Responsestatus**: `204`

 **Responsebody**: 
None
## Save a security profile assignment
### `POST` `v1/securityprofiles/assignments`

| Parameters      | Description                    |
|------------------|---------------------------------|

 **Requestbody**: 
{'Sample': '{\r\n  "SecurityProfileID": "",\r\n  "BuyerID": "",\r\n  "SupplierID": "",\r\n  "UserID": "",\r\n  "UserGroupID": ""\r\n}', 'Fields': [{'Name': 'SecurityProfileID', 'Type': 'string', 'Description': 'ID of the security profile. Required. Sortable: priority level 1.', 'Required': True}, {'Name': 'BuyerID', 'Type': 'string', 'Description': 'ID of the buyer.', 'Required': False}, {'Name': 'SupplierID', 'Type': 'string', 'Description': 'ID of the supplier.', 'Required': False}, {'Name': 'UserID', 'Type': 'string', 'Description': 'ID of the user. Sortable: priority level 2.', 'Required': False}, {'Name': 'UserGroupID', 'Type': 'string', 'Description': 'ID of the user group.', 'Required': False}]}
 **Responsestatus**: `204`

 **Responsebody**: 
None