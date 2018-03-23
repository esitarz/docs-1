---
title: Impersonation Configs
date: 2018-03-23
category: API Reference
tags: Authentication And Authorization
slug: ImpersonationConfigs
---


## `GET` `v1/impersonationconfig/{impersonationConfigID}`
Get a single impersonation config

| Parameters      | Description                    |
|------------------|---------------------------------|


| Parameters      | Description                    |
|------------------|---------------------------------|
| Name            | impersonationConfigID          |
| Type            | string                         |
| Description     | ID of the impersonation config. |
| Required        | True                           |

## Requestbody
**Responsestatus**: `200`

## Responsebody
```
{'ID': '', 'ImpersonationBuyerID': '', 'ImpersonationGroupID': '', 'ImpersonationUserID': '', 'BuyerID': '', 'GroupID': '', 'UserID': '', 'SecurityProfileID': '', 'ClientID': ''}
```


| Parameters      | Description                    |
|------------------|---------------------------------|
| Name            | ID                             |
| Type            | string                         |
| Description     | ID of the impersonation config. |
| Required        | False                          |


| Parameters      | Description                    |
|------------------|---------------------------------|
| Name            | ImpersonationBuyerID           |
| Type            | string                         |
| Description     | ID of the impersonation buyer. |
| Required        | False                          |


| Parameters      | Description                    |
|------------------|---------------------------------|
| Name            | ImpersonationGroupID           |
| Type            | string                         |
| Description     | ID of the impersonation group. |
| Required        | False                          |


| Parameters      | Description                    |
|------------------|---------------------------------|
| Name            | ImpersonationUserID            |
| Type            | string                         |
| Description     | ID of the impersonation user.  |
| Required        | False                          |


| Parameters      | Description                    |
|------------------|---------------------------------|
| Name            | BuyerID                        |
| Type            | string                         |
| Description     | ID of the buyer.               |
| Required        | True                           |


| Parameters      | Description                    |
|------------------|---------------------------------|
| Name            | GroupID                        |
| Type            | string                         |
| Description     | ID of the group.               |
| Required        | False                          |


| Parameters      | Description                    |
|------------------|---------------------------------|
| Name            | UserID                         |
| Type            | string                         |
| Description     | ID of the user.                |
| Required        | False                          |


| Parameters      | Description                    |
|------------------|---------------------------------|
| Name            | SecurityProfileID              |
| Type            | string                         |
| Description     | ID of the security profile.    |
| Required        | True                           |


| Parameters      | Description                    |
|------------------|---------------------------------|
| Name            | ClientID                       |
| Type            | string                         |
| Description     | ID of the client.              |
| Required        | True                           |

## `GET` `v1/impersonationconfig`
Get a list of impersonation configs

| Parameters      | Description                    |
|------------------|---------------------------------|


| Parameters      | Description                    |
|------------------|---------------------------------|
| Name            | search                         |
| Type            | string                         |
| Description     | Word or phrase to search for.  |
| Required        | False                          |


| Parameters      | Description                    |
|------------------|---------------------------------|
| Name            | searchOn                       |
| Type            | string                         |
| Description     | Comma-delimited list of fields to search on. |
| Required        | False                          |


| Parameters      | Description                    |
|------------------|---------------------------------|
| Name            | sortBy                         |
| Type            | string                         |
| Description     | Comma-delimited list of fields to sort by. |
| Required        | False                          |


| Parameters      | Description                    |
|------------------|---------------------------------|
| Name            | page                           |
| Type            | integer                        |
| Description     | Page of results to return. Default: 1 |
| Required        | False                          |


| Parameters      | Description                    |
|------------------|---------------------------------|
| Name            | pageSize                       |
| Type            | integer                        |
| Description     | Number of results to return per page. Default: 20, max: 100. |
| Required        | False                          |


| Parameters      | Description                    |
|------------------|---------------------------------|
| Name            | filters                        |
| Type            | object                         |
| Description     | Any additional key/value pairs passed in the query string are interpretted as filters. Valid keys are top-level properties of the returned model or 'xp.???' |
| Required        | False                          |

## Requestbody
**Responsestatus**: `200`

## Responsebody
```
{'Meta': {'Page': 1, 'PageSize': 20, 'TotalCount': 25, 'TotalPages': 2, 'ItemRange': [1, 20]}, 'Items': [{'ID': '', 'ImpersonationBuyerID': '', 'ImpersonationGroupID': '', 'ImpersonationUserID': '', 'BuyerID': '', 'GroupID': '', 'UserID': '', 'SecurityProfileID': '', 'ClientID': ''}]}
```


| Parameters      | Description                    |
|------------------|---------------------------------|
| Name            | ID                             |
| Type            | string                         |
| Description     | ID of the impersonation config. |
| Required        | False                          |


| Parameters      | Description                    |
|------------------|---------------------------------|
| Name            | ImpersonationBuyerID           |
| Type            | string                         |
| Description     | ID of the impersonation buyer. |
| Required        | False                          |


| Parameters      | Description                    |
|------------------|---------------------------------|
| Name            | ImpersonationGroupID           |
| Type            | string                         |
| Description     | ID of the impersonation group. |
| Required        | False                          |


| Parameters      | Description                    |
|------------------|---------------------------------|
| Name            | ImpersonationUserID            |
| Type            | string                         |
| Description     | ID of the impersonation user.  |
| Required        | False                          |


| Parameters      | Description                    |
|------------------|---------------------------------|
| Name            | BuyerID                        |
| Type            | string                         |
| Description     | ID of the buyer.               |
| Required        | True                           |


| Parameters      | Description                    |
|------------------|---------------------------------|
| Name            | GroupID                        |
| Type            | string                         |
| Description     | ID of the group.               |
| Required        | False                          |


| Parameters      | Description                    |
|------------------|---------------------------------|
| Name            | UserID                         |
| Type            | string                         |
| Description     | ID of the user.                |
| Required        | False                          |


| Parameters      | Description                    |
|------------------|---------------------------------|
| Name            | SecurityProfileID              |
| Type            | string                         |
| Description     | ID of the security profile.    |
| Required        | True                           |


| Parameters      | Description                    |
|------------------|---------------------------------|
| Name            | ClientID                       |
| Type            | string                         |
| Description     | ID of the client.              |
| Required        | True                           |

## `POST` `v1/impersonationconfig`
Create a new impersonation config
## Requestbody
```
{'ID': '', 'ImpersonationBuyerID': '', 'ImpersonationGroupID': '', 'ImpersonationUserID': '', 'BuyerID': '', 'GroupID': '', 'UserID': '', 'SecurityProfileID': '', 'ClientID': ''}
```

```
[{'Name': 'ID', 'Type': 'string', 'Description': 'ID of the impersonation config. Can only contain characters Aa-Zz, 0-9, -, and _. Searchable: priority level 8. Sortable: priority level 8.', 'Required': False}, {'Name': 'ImpersonationBuyerID', 'Type': 'string', 'Description': 'ID of the impersonation buyer. Searchable: priority level 0. Sortable: priority level 0.', 'Required': False}, {'Name': 'ImpersonationGroupID', 'Type': 'string', 'Description': 'ID of the impersonation group. Searchable: priority level 1. Sortable: priority level 1.', 'Required': False}, {'Name': 'ImpersonationUserID', 'Type': 'string', 'Description': 'ID of the impersonation user. Searchable: priority level 2. Sortable: priority level 2.', 'Required': False}, {'Name': 'BuyerID', 'Type': 'string', 'Description': 'ID of the buyer. Required. Searchable: priority level 3. Sortable: priority level 3.', 'Required': True}, {'Name': 'GroupID', 'Type': 'string', 'Description': 'ID of the group. Searchable: priority level 4. Sortable: priority level 4.', 'Required': False}, {'Name': 'UserID', 'Type': 'string', 'Description': 'ID of the user. Searchable: priority level 5. Sortable: priority level 5.', 'Required': False}, {'Name': 'SecurityProfileID', 'Type': 'string', 'Description': 'ID of the security profile. Required. Searchable: priority level 6. Sortable: priority level 6.', 'Required': True}, {'Name': 'ClientID', 'Type': 'string', 'Description': 'ID of the client. Required. Searchable: priority level 7. Sortable: priority level 7.', 'Required': True}]
```

**Responsestatus**: `201`

## Responsebody
```
{'ID': '', 'ImpersonationBuyerID': '', 'ImpersonationGroupID': '', 'ImpersonationUserID': '', 'BuyerID': '', 'GroupID': '', 'UserID': '', 'SecurityProfileID': '', 'ClientID': ''}
```


| Parameters      | Description                    |
|------------------|---------------------------------|
| Name            | ID                             |
| Type            | string                         |
| Description     | ID of the impersonation config. |
| Required        | False                          |


| Parameters      | Description                    |
|------------------|---------------------------------|
| Name            | ImpersonationBuyerID           |
| Type            | string                         |
| Description     | ID of the impersonation buyer. |
| Required        | False                          |


| Parameters      | Description                    |
|------------------|---------------------------------|
| Name            | ImpersonationGroupID           |
| Type            | string                         |
| Description     | ID of the impersonation group. |
| Required        | False                          |


| Parameters      | Description                    |
|------------------|---------------------------------|
| Name            | ImpersonationUserID            |
| Type            | string                         |
| Description     | ID of the impersonation user.  |
| Required        | False                          |


| Parameters      | Description                    |
|------------------|---------------------------------|
| Name            | BuyerID                        |
| Type            | string                         |
| Description     | ID of the buyer.               |
| Required        | True                           |


| Parameters      | Description                    |
|------------------|---------------------------------|
| Name            | GroupID                        |
| Type            | string                         |
| Description     | ID of the group.               |
| Required        | False                          |


| Parameters      | Description                    |
|------------------|---------------------------------|
| Name            | UserID                         |
| Type            | string                         |
| Description     | ID of the user.                |
| Required        | False                          |


| Parameters      | Description                    |
|------------------|---------------------------------|
| Name            | SecurityProfileID              |
| Type            | string                         |
| Description     | ID of the security profile.    |
| Required        | True                           |


| Parameters      | Description                    |
|------------------|---------------------------------|
| Name            | ClientID                       |
| Type            | string                         |
| Description     | ID of the client.              |
| Required        | True                           |

## `PUT` `v1/impersonationconfig/{impersonationConfigID}`
Create or update an impersonation config

| Parameters      | Description                    |
|------------------|---------------------------------|


| Parameters      | Description                    |
|------------------|---------------------------------|
| Name            | impersonationConfigID          |
| Type            | string                         |
| Description     | ID of the impersonation config. |
| Required        | True                           |

## Requestbody
```
{'ID': '', 'ImpersonationBuyerID': '', 'ImpersonationGroupID': '', 'ImpersonationUserID': '', 'BuyerID': '', 'GroupID': '', 'UserID': '', 'SecurityProfileID': '', 'ClientID': ''}
```

```
[{'Name': 'ID', 'Type': 'string', 'Description': 'ID of the impersonation config. Can only contain characters Aa-Zz, 0-9, -, and _. Searchable: priority level 8. Sortable: priority level 8.', 'Required': False}, {'Name': 'ImpersonationBuyerID', 'Type': 'string', 'Description': 'ID of the impersonation buyer. Searchable: priority level 0. Sortable: priority level 0.', 'Required': False}, {'Name': 'ImpersonationGroupID', 'Type': 'string', 'Description': 'ID of the impersonation group. Searchable: priority level 1. Sortable: priority level 1.', 'Required': False}, {'Name': 'ImpersonationUserID', 'Type': 'string', 'Description': 'ID of the impersonation user. Searchable: priority level 2. Sortable: priority level 2.', 'Required': False}, {'Name': 'BuyerID', 'Type': 'string', 'Description': 'ID of the buyer. Required. Searchable: priority level 3. Sortable: priority level 3.', 'Required': True}, {'Name': 'GroupID', 'Type': 'string', 'Description': 'ID of the group. Searchable: priority level 4. Sortable: priority level 4.', 'Required': False}, {'Name': 'UserID', 'Type': 'string', 'Description': 'ID of the user. Searchable: priority level 5. Sortable: priority level 5.', 'Required': False}, {'Name': 'SecurityProfileID', 'Type': 'string', 'Description': 'ID of the security profile. Required. Searchable: priority level 6. Sortable: priority level 6.', 'Required': True}, {'Name': 'ClientID', 'Type': 'string', 'Description': 'ID of the client. Required. Searchable: priority level 7. Sortable: priority level 7.', 'Required': True}]
```

**Responsestatus**: `200`

## Responsebody
```
{'ID': '', 'ImpersonationBuyerID': '', 'ImpersonationGroupID': '', 'ImpersonationUserID': '', 'BuyerID': '', 'GroupID': '', 'UserID': '', 'SecurityProfileID': '', 'ClientID': ''}
```


| Parameters      | Description                    |
|------------------|---------------------------------|
| Name            | ID                             |
| Type            | string                         |
| Description     | ID of the impersonation config. |
| Required        | False                          |


| Parameters      | Description                    |
|------------------|---------------------------------|
| Name            | ImpersonationBuyerID           |
| Type            | string                         |
| Description     | ID of the impersonation buyer. |
| Required        | False                          |


| Parameters      | Description                    |
|------------------|---------------------------------|
| Name            | ImpersonationGroupID           |
| Type            | string                         |
| Description     | ID of the impersonation group. |
| Required        | False                          |


| Parameters      | Description                    |
|------------------|---------------------------------|
| Name            | ImpersonationUserID            |
| Type            | string                         |
| Description     | ID of the impersonation user.  |
| Required        | False                          |


| Parameters      | Description                    |
|------------------|---------------------------------|
| Name            | BuyerID                        |
| Type            | string                         |
| Description     | ID of the buyer.               |
| Required        | True                           |


| Parameters      | Description                    |
|------------------|---------------------------------|
| Name            | GroupID                        |
| Type            | string                         |
| Description     | ID of the group.               |
| Required        | False                          |


| Parameters      | Description                    |
|------------------|---------------------------------|
| Name            | UserID                         |
| Type            | string                         |
| Description     | ID of the user.                |
| Required        | False                          |


| Parameters      | Description                    |
|------------------|---------------------------------|
| Name            | SecurityProfileID              |
| Type            | string                         |
| Description     | ID of the security profile.    |
| Required        | True                           |


| Parameters      | Description                    |
|------------------|---------------------------------|
| Name            | ClientID                       |
| Type            | string                         |
| Description     | ID of the client.              |
| Required        | True                           |

## `DELETE` `v1/impersonationconfig/{impersonationConfigID}`
Delete an impersonation config

| Parameters      | Description                    |
|------------------|---------------------------------|


| Parameters      | Description                    |
|------------------|---------------------------------|
| Name            | impersonationConfigID          |
| Type            | string                         |
| Description     | ID of the impersonation config. |
| Required        | True                           |

## Requestbody
**Responsestatus**: `204`

## Responsebody
## `PATCH` `v1/impersonationconfig/{impersonationConfigID}`
Partially update an impersonation config

| Parameters      | Description                    |
|------------------|---------------------------------|


| Parameters      | Description                    |
|------------------|---------------------------------|
| Name            | impersonationConfigID          |
| Type            | string                         |
| Description     | ID of the impersonation config. |
| Required        | True                           |

## Requestbody
```
{'ID': '', 'ImpersonationBuyerID': '', 'ImpersonationGroupID': '', 'ImpersonationUserID': '', 'BuyerID': '', 'GroupID': '', 'UserID': '', 'SecurityProfileID': '', 'ClientID': ''}
```

```
[{'Name': 'ID', 'Type': 'string', 'Description': 'ID of the impersonation config. Can only contain characters Aa-Zz, 0-9, -, and _. Searchable: priority level 8. Sortable: priority level 8.', 'Required': False}, {'Name': 'ImpersonationBuyerID', 'Type': 'string', 'Description': 'ID of the impersonation buyer. Searchable: priority level 0. Sortable: priority level 0.', 'Required': False}, {'Name': 'ImpersonationGroupID', 'Type': 'string', 'Description': 'ID of the impersonation group. Searchable: priority level 1. Sortable: priority level 1.', 'Required': False}, {'Name': 'ImpersonationUserID', 'Type': 'string', 'Description': 'ID of the impersonation user. Searchable: priority level 2. Sortable: priority level 2.', 'Required': False}, {'Name': 'BuyerID', 'Type': 'string', 'Description': 'ID of the buyer. Required. Searchable: priority level 3. Sortable: priority level 3.', 'Required': True}, {'Name': 'GroupID', 'Type': 'string', 'Description': 'ID of the group. Searchable: priority level 4. Sortable: priority level 4.', 'Required': False}, {'Name': 'UserID', 'Type': 'string', 'Description': 'ID of the user. Searchable: priority level 5. Sortable: priority level 5.', 'Required': False}, {'Name': 'SecurityProfileID', 'Type': 'string', 'Description': 'ID of the security profile. Required. Searchable: priority level 6. Sortable: priority level 6.', 'Required': True}, {'Name': 'ClientID', 'Type': 'string', 'Description': 'ID of the client. Required. Searchable: priority level 7. Sortable: priority level 7.', 'Required': True}]
```

**Responsestatus**: `200`

## Responsebody
```
{'ID': '', 'ImpersonationBuyerID': '', 'ImpersonationGroupID': '', 'ImpersonationUserID': '', 'BuyerID': '', 'GroupID': '', 'UserID': '', 'SecurityProfileID': '', 'ClientID': ''}
```


| Parameters      | Description                    |
|------------------|---------------------------------|
| Name            | ID                             |
| Type            | string                         |
| Description     | ID of the impersonation config. |
| Required        | False                          |


| Parameters      | Description                    |
|------------------|---------------------------------|
| Name            | ImpersonationBuyerID           |
| Type            | string                         |
| Description     | ID of the impersonation buyer. |
| Required        | False                          |


| Parameters      | Description                    |
|------------------|---------------------------------|
| Name            | ImpersonationGroupID           |
| Type            | string                         |
| Description     | ID of the impersonation group. |
| Required        | False                          |


| Parameters      | Description                    |
|------------------|---------------------------------|
| Name            | ImpersonationUserID            |
| Type            | string                         |
| Description     | ID of the impersonation user.  |
| Required        | False                          |


| Parameters      | Description                    |
|------------------|---------------------------------|
| Name            | BuyerID                        |
| Type            | string                         |
| Description     | ID of the buyer.               |
| Required        | True                           |


| Parameters      | Description                    |
|------------------|---------------------------------|
| Name            | GroupID                        |
| Type            | string                         |
| Description     | ID of the group.               |
| Required        | False                          |


| Parameters      | Description                    |
|------------------|---------------------------------|
| Name            | UserID                         |
| Type            | string                         |
| Description     | ID of the user.                |
| Required        | False                          |


| Parameters      | Description                    |
|------------------|---------------------------------|
| Name            | SecurityProfileID              |
| Type            | string                         |
| Description     | ID of the security profile.    |
| Required        | True                           |


| Parameters      | Description                    |
|------------------|---------------------------------|
| Name            | ClientID                       |
| Type            | string                         |
| Description     | ID of the client.              |
| Required        | True                           |
