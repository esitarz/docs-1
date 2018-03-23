---
title: Impersonation Configs
date: 2018-03-23
category: API Reference
tags: Authentication And Authorization
slug: ImpersonationConfigs
---


## Get a single impersonation config
### `GET` `v1/impersonationconfig/{impersonationConfigID}`

| Parameters      | Description                    |
|------------------|---------------------------------|
| Name            | impersonationConfigID          |
| Type            | string                         |
| Description     | ID of the impersonation config. |
| Required        | True                           |

 **Requestbody**: 
None
 **Responsestatus**: `200`

 **Responsebody**: 
{'Sample': '{\r\n  "ID": "",\r\n  "ImpersonationBuyerID": "",\r\n  "ImpersonationGroupID": "",\r\n  "ImpersonationUserID": "",\r\n  "BuyerID": "",\r\n  "GroupID": "",\r\n  "UserID": "",\r\n  "SecurityProfileID": "",\r\n  "ClientID": ""\r\n}', 'Fields': [{'Name': 'ID', 'Type': 'string', 'Description': 'ID of the impersonation config.', 'Required': False}, {'Name': 'ImpersonationBuyerID', 'Type': 'string', 'Description': 'ID of the impersonation buyer.', 'Required': False}, {'Name': 'ImpersonationGroupID', 'Type': 'string', 'Description': 'ID of the impersonation group.', 'Required': False}, {'Name': 'ImpersonationUserID', 'Type': 'string', 'Description': 'ID of the impersonation user.', 'Required': False}, {'Name': 'BuyerID', 'Type': 'string', 'Description': 'ID of the buyer.', 'Required': True}, {'Name': 'GroupID', 'Type': 'string', 'Description': 'ID of the group.', 'Required': False}, {'Name': 'UserID', 'Type': 'string', 'Description': 'ID of the user.', 'Required': False}, {'Name': 'SecurityProfileID', 'Type': 'string', 'Description': 'ID of the security profile.', 'Required': True}, {'Name': 'ClientID', 'Type': 'string', 'Description': 'ID of the client.', 'Required': True}]}
## Get a list of impersonation configs
### `GET` `v1/impersonationconfig`

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
{'Sample': '{\r\n  "Meta": {\r\n    "Page": 1,\r\n    "PageSize": 20,\r\n    "TotalCount": 25,\r\n    "TotalPages": 2,\r\n    "ItemRange": [\r\n      1,\r\n      20\r\n    ]\r\n  },\r\n  "Items": [\r\n    {\r\n      "ID": "",\r\n      "ImpersonationBuyerID": "",\r\n      "ImpersonationGroupID": "",\r\n      "ImpersonationUserID": "",\r\n      "BuyerID": "",\r\n      "GroupID": "",\r\n      "UserID": "",\r\n      "SecurityProfileID": "",\r\n      "ClientID": ""\r\n    }\r\n  ]\r\n}', 'Fields': [{'Name': 'ID', 'Type': 'string', 'Description': 'ID of the impersonation config.', 'Required': False}, {'Name': 'ImpersonationBuyerID', 'Type': 'string', 'Description': 'ID of the impersonation buyer.', 'Required': False}, {'Name': 'ImpersonationGroupID', 'Type': 'string', 'Description': 'ID of the impersonation group.', 'Required': False}, {'Name': 'ImpersonationUserID', 'Type': 'string', 'Description': 'ID of the impersonation user.', 'Required': False}, {'Name': 'BuyerID', 'Type': 'string', 'Description': 'ID of the buyer.', 'Required': True}, {'Name': 'GroupID', 'Type': 'string', 'Description': 'ID of the group.', 'Required': False}, {'Name': 'UserID', 'Type': 'string', 'Description': 'ID of the user.', 'Required': False}, {'Name': 'SecurityProfileID', 'Type': 'string', 'Description': 'ID of the security profile.', 'Required': True}, {'Name': 'ClientID', 'Type': 'string', 'Description': 'ID of the client.', 'Required': True}]}
## Create a new impersonation config
### `POST` `v1/impersonationconfig`

| Parameters      | Description                    |
|------------------|---------------------------------|

 **Requestbody**: 
{'Sample': '{\r\n  "ID": "",\r\n  "ImpersonationBuyerID": "",\r\n  "ImpersonationGroupID": "",\r\n  "ImpersonationUserID": "",\r\n  "BuyerID": "",\r\n  "GroupID": "",\r\n  "UserID": "",\r\n  "SecurityProfileID": "",\r\n  "ClientID": ""\r\n}', 'Fields': [{'Name': 'ID', 'Type': 'string', 'Description': 'ID of the impersonation config. Can only contain characters Aa-Zz, 0-9, -, and _. Searchable: priority level 8. Sortable: priority level 8.', 'Required': False}, {'Name': 'ImpersonationBuyerID', 'Type': 'string', 'Description': 'ID of the impersonation buyer. Searchable: priority level 0. Sortable: priority level 0.', 'Required': False}, {'Name': 'ImpersonationGroupID', 'Type': 'string', 'Description': 'ID of the impersonation group. Searchable: priority level 1. Sortable: priority level 1.', 'Required': False}, {'Name': 'ImpersonationUserID', 'Type': 'string', 'Description': 'ID of the impersonation user. Searchable: priority level 2. Sortable: priority level 2.', 'Required': False}, {'Name': 'BuyerID', 'Type': 'string', 'Description': 'ID of the buyer. Required. Searchable: priority level 3. Sortable: priority level 3.', 'Required': True}, {'Name': 'GroupID', 'Type': 'string', 'Description': 'ID of the group. Searchable: priority level 4. Sortable: priority level 4.', 'Required': False}, {'Name': 'UserID', 'Type': 'string', 'Description': 'ID of the user. Searchable: priority level 5. Sortable: priority level 5.', 'Required': False}, {'Name': 'SecurityProfileID', 'Type': 'string', 'Description': 'ID of the security profile. Required. Searchable: priority level 6. Sortable: priority level 6.', 'Required': True}, {'Name': 'ClientID', 'Type': 'string', 'Description': 'ID of the client. Required. Searchable: priority level 7. Sortable: priority level 7.', 'Required': True}]}
 **Responsestatus**: `201`

 **Responsebody**: 
{'Sample': '{\r\n  "ID": "",\r\n  "ImpersonationBuyerID": "",\r\n  "ImpersonationGroupID": "",\r\n  "ImpersonationUserID": "",\r\n  "BuyerID": "",\r\n  "GroupID": "",\r\n  "UserID": "",\r\n  "SecurityProfileID": "",\r\n  "ClientID": ""\r\n}', 'Fields': [{'Name': 'ID', 'Type': 'string', 'Description': 'ID of the impersonation config.', 'Required': False}, {'Name': 'ImpersonationBuyerID', 'Type': 'string', 'Description': 'ID of the impersonation buyer.', 'Required': False}, {'Name': 'ImpersonationGroupID', 'Type': 'string', 'Description': 'ID of the impersonation group.', 'Required': False}, {'Name': 'ImpersonationUserID', 'Type': 'string', 'Description': 'ID of the impersonation user.', 'Required': False}, {'Name': 'BuyerID', 'Type': 'string', 'Description': 'ID of the buyer.', 'Required': True}, {'Name': 'GroupID', 'Type': 'string', 'Description': 'ID of the group.', 'Required': False}, {'Name': 'UserID', 'Type': 'string', 'Description': 'ID of the user.', 'Required': False}, {'Name': 'SecurityProfileID', 'Type': 'string', 'Description': 'ID of the security profile.', 'Required': True}, {'Name': 'ClientID', 'Type': 'string', 'Description': 'ID of the client.', 'Required': True}]}
## Create or update an impersonation config
### `PUT` `v1/impersonationconfig/{impersonationConfigID}`

| Parameters      | Description                    |
|------------------|---------------------------------|
| Name            | impersonationConfigID          |
| Type            | string                         |
| Description     | ID of the impersonation config. |
| Required        | True                           |

 **Requestbody**: 
{'Sample': '{\r\n  "ID": "",\r\n  "ImpersonationBuyerID": "",\r\n  "ImpersonationGroupID": "",\r\n  "ImpersonationUserID": "",\r\n  "BuyerID": "",\r\n  "GroupID": "",\r\n  "UserID": "",\r\n  "SecurityProfileID": "",\r\n  "ClientID": ""\r\n}', 'Fields': [{'Name': 'ID', 'Type': 'string', 'Description': 'ID of the impersonation config. Can only contain characters Aa-Zz, 0-9, -, and _. Searchable: priority level 8. Sortable: priority level 8.', 'Required': False}, {'Name': 'ImpersonationBuyerID', 'Type': 'string', 'Description': 'ID of the impersonation buyer. Searchable: priority level 0. Sortable: priority level 0.', 'Required': False}, {'Name': 'ImpersonationGroupID', 'Type': 'string', 'Description': 'ID of the impersonation group. Searchable: priority level 1. Sortable: priority level 1.', 'Required': False}, {'Name': 'ImpersonationUserID', 'Type': 'string', 'Description': 'ID of the impersonation user. Searchable: priority level 2. Sortable: priority level 2.', 'Required': False}, {'Name': 'BuyerID', 'Type': 'string', 'Description': 'ID of the buyer. Required. Searchable: priority level 3. Sortable: priority level 3.', 'Required': True}, {'Name': 'GroupID', 'Type': 'string', 'Description': 'ID of the group. Searchable: priority level 4. Sortable: priority level 4.', 'Required': False}, {'Name': 'UserID', 'Type': 'string', 'Description': 'ID of the user. Searchable: priority level 5. Sortable: priority level 5.', 'Required': False}, {'Name': 'SecurityProfileID', 'Type': 'string', 'Description': 'ID of the security profile. Required. Searchable: priority level 6. Sortable: priority level 6.', 'Required': True}, {'Name': 'ClientID', 'Type': 'string', 'Description': 'ID of the client. Required. Searchable: priority level 7. Sortable: priority level 7.', 'Required': True}]}
 **Responsestatus**: `200`

 **Responsebody**: 
{'Sample': '{\r\n  "ID": "",\r\n  "ImpersonationBuyerID": "",\r\n  "ImpersonationGroupID": "",\r\n  "ImpersonationUserID": "",\r\n  "BuyerID": "",\r\n  "GroupID": "",\r\n  "UserID": "",\r\n  "SecurityProfileID": "",\r\n  "ClientID": ""\r\n}', 'Fields': [{'Name': 'ID', 'Type': 'string', 'Description': 'ID of the impersonation config.', 'Required': False}, {'Name': 'ImpersonationBuyerID', 'Type': 'string', 'Description': 'ID of the impersonation buyer.', 'Required': False}, {'Name': 'ImpersonationGroupID', 'Type': 'string', 'Description': 'ID of the impersonation group.', 'Required': False}, {'Name': 'ImpersonationUserID', 'Type': 'string', 'Description': 'ID of the impersonation user.', 'Required': False}, {'Name': 'BuyerID', 'Type': 'string', 'Description': 'ID of the buyer.', 'Required': True}, {'Name': 'GroupID', 'Type': 'string', 'Description': 'ID of the group.', 'Required': False}, {'Name': 'UserID', 'Type': 'string', 'Description': 'ID of the user.', 'Required': False}, {'Name': 'SecurityProfileID', 'Type': 'string', 'Description': 'ID of the security profile.', 'Required': True}, {'Name': 'ClientID', 'Type': 'string', 'Description': 'ID of the client.', 'Required': True}]}
## Delete an impersonation config
### `DELETE` `v1/impersonationconfig/{impersonationConfigID}`

| Parameters      | Description                    |
|------------------|---------------------------------|
| Name            | impersonationConfigID          |
| Type            | string                         |
| Description     | ID of the impersonation config. |
| Required        | True                           |

 **Requestbody**: 
None
 **Responsestatus**: `204`

 **Responsebody**: 
None
## Partially update an impersonation config
### `PATCH` `v1/impersonationconfig/{impersonationConfigID}`

| Parameters      | Description                    |
|------------------|---------------------------------|
| Name            | impersonationConfigID          |
| Type            | string                         |
| Description     | ID of the impersonation config. |
| Required        | True                           |

 **Requestbody**: 
{'Sample': '{\r\n  "ID": "",\r\n  "ImpersonationBuyerID": "",\r\n  "ImpersonationGroupID": "",\r\n  "ImpersonationUserID": "",\r\n  "BuyerID": "",\r\n  "GroupID": "",\r\n  "UserID": "",\r\n  "SecurityProfileID": "",\r\n  "ClientID": ""\r\n}', 'Fields': [{'Name': 'ID', 'Type': 'string', 'Description': 'ID of the impersonation config. Can only contain characters Aa-Zz, 0-9, -, and _. Searchable: priority level 8. Sortable: priority level 8.', 'Required': False}, {'Name': 'ImpersonationBuyerID', 'Type': 'string', 'Description': 'ID of the impersonation buyer. Searchable: priority level 0. Sortable: priority level 0.', 'Required': False}, {'Name': 'ImpersonationGroupID', 'Type': 'string', 'Description': 'ID of the impersonation group. Searchable: priority level 1. Sortable: priority level 1.', 'Required': False}, {'Name': 'ImpersonationUserID', 'Type': 'string', 'Description': 'ID of the impersonation user. Searchable: priority level 2. Sortable: priority level 2.', 'Required': False}, {'Name': 'BuyerID', 'Type': 'string', 'Description': 'ID of the buyer. Required. Searchable: priority level 3. Sortable: priority level 3.', 'Required': True}, {'Name': 'GroupID', 'Type': 'string', 'Description': 'ID of the group. Searchable: priority level 4. Sortable: priority level 4.', 'Required': False}, {'Name': 'UserID', 'Type': 'string', 'Description': 'ID of the user. Searchable: priority level 5. Sortable: priority level 5.', 'Required': False}, {'Name': 'SecurityProfileID', 'Type': 'string', 'Description': 'ID of the security profile. Required. Searchable: priority level 6. Sortable: priority level 6.', 'Required': True}, {'Name': 'ClientID', 'Type': 'string', 'Description': 'ID of the client. Required. Searchable: priority level 7. Sortable: priority level 7.', 'Required': True}]}
 **Responsestatus**: `200`

 **Responsebody**: 
{'Sample': '{\r\n  "ID": "",\r\n  "ImpersonationBuyerID": "",\r\n  "ImpersonationGroupID": "",\r\n  "ImpersonationUserID": "",\r\n  "BuyerID": "",\r\n  "GroupID": "",\r\n  "UserID": "",\r\n  "SecurityProfileID": "",\r\n  "ClientID": ""\r\n}', 'Fields': [{'Name': 'ID', 'Type': 'string', 'Description': 'ID of the impersonation config.', 'Required': False}, {'Name': 'ImpersonationBuyerID', 'Type': 'string', 'Description': 'ID of the impersonation buyer.', 'Required': False}, {'Name': 'ImpersonationGroupID', 'Type': 'string', 'Description': 'ID of the impersonation group.', 'Required': False}, {'Name': 'ImpersonationUserID', 'Type': 'string', 'Description': 'ID of the impersonation user.', 'Required': False}, {'Name': 'BuyerID', 'Type': 'string', 'Description': 'ID of the buyer.', 'Required': True}, {'Name': 'GroupID', 'Type': 'string', 'Description': 'ID of the group.', 'Required': False}, {'Name': 'UserID', 'Type': 'string', 'Description': 'ID of the user.', 'Required': False}, {'Name': 'SecurityProfileID', 'Type': 'string', 'Description': 'ID of the security profile.', 'Required': True}, {'Name': 'ClientID', 'Type': 'string', 'Description': 'ID of the client.', 'Required': True}]}