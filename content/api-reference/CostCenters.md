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

## `GET` `v1/buyers/{buyerID}/costcenters/{costCenterID}`
Get a single cost center

| Parameters      | Description                    |
|------------------|---------------------------------|


| Parameters      | Description                    |
|------------------|---------------------------------|
| Name            | buyerID                        |
| Type            | string                         |
| Description     | ID of the buyer.               |
| Required        | True                           |


| Parameters      | Description                    |
|------------------|---------------------------------|
| Name            | costCenterID                   |
| Type            | string                         |
| Description     | ID of the cost center.         |
| Required        | True                           |

## Requestbody
**Responsestatus**: `200`

## Responsebody
```
{'ID': '', 'Name': '', 'Description': '', 'xp': {}}
```


| Parameters      | Description                    |
|------------------|---------------------------------|
| Name            | ID                             |
| Type            | string                         |
| Description     | ID of the cost center.         |
| Required        | False                          |


| Parameters      | Description                    |
|------------------|---------------------------------|
| Name            | Name                           |
| Type            | string                         |
| Description     | Name of the cost center.       |
| Required        | True                           |


| Parameters      | Description                    |
|------------------|---------------------------------|
| Name            | Description                    |
| Type            | string                         |
| Description     | Description of the cost center. |
| Required        | False                          |


| Parameters      | Description                    |
|------------------|---------------------------------|
| Name            | xp                             |
| Type            | object                         |
| Description     | Container for extended (custom) properties of the cost center. |
| Required        | False                          |

## `GET` `v1/buyers/{buyerID}/costcenters`
Get a list of cost centers

| Parameters      | Description                    |
|------------------|---------------------------------|


| Parameters      | Description                    |
|------------------|---------------------------------|
| Name            | buyerID                        |
| Type            | string                         |
| Description     | ID of the buyer.               |
| Required        | True                           |


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
{'Meta': {'Page': 1, 'PageSize': 20, 'TotalCount': 25, 'TotalPages': 2, 'ItemRange': [1, 20]}, 'Items': [{'ID': '', 'Name': '', 'Description': '', 'xp': {}}]}
```


| Parameters      | Description                    |
|------------------|---------------------------------|
| Name            | ID                             |
| Type            | string                         |
| Description     | ID of the cost center.         |
| Required        | False                          |


| Parameters      | Description                    |
|------------------|---------------------------------|
| Name            | Name                           |
| Type            | string                         |
| Description     | Name of the cost center.       |
| Required        | True                           |


| Parameters      | Description                    |
|------------------|---------------------------------|
| Name            | Description                    |
| Type            | string                         |
| Description     | Description of the cost center. |
| Required        | False                          |


| Parameters      | Description                    |
|------------------|---------------------------------|
| Name            | xp                             |
| Type            | object                         |
| Description     | Container for extended (custom) properties of the cost center. |
| Required        | False                          |

## `POST` `v1/buyers/{buyerID}/costcenters`
Create a new cost center

| Parameters      | Description                    |
|------------------|---------------------------------|


| Parameters      | Description                    |
|------------------|---------------------------------|
| Name            | buyerID                        |
| Type            | string                         |
| Description     | ID of the buyer.               |
| Required        | True                           |

## Requestbody
```
{'ID': '', 'Name': '', 'Description': '', 'xp': {}}
```

```
[{'Name': 'ID', 'Type': 'string', 'Description': 'ID of the cost center. Can only contain characters Aa-Zz, 0-9, -, and _. Searchable: priority level 1. Sortable: priority level 2.', 'Required': False}, {'Name': 'Name', 'Type': 'string', 'Description': 'Name of the cost center. Required. Max length 100 characters. Searchable: priority level 2. Sortable: priority level 1.', 'Required': True}, {'Name': 'Description', 'Type': 'string', 'Description': 'Description of the cost center. Max length 2000 characters. Searchable: priority level 3.', 'Required': False}, {'Name': 'xp', 'Type': 'object', 'Description': 'Container for extended (custom) properties of the cost center.', 'Required': False}]
```

**Responsestatus**: `201`

## Responsebody
```
{'ID': '', 'Name': '', 'Description': '', 'xp': {}}
```


| Parameters      | Description                    |
|------------------|---------------------------------|
| Name            | ID                             |
| Type            | string                         |
| Description     | ID of the cost center.         |
| Required        | False                          |


| Parameters      | Description                    |
|------------------|---------------------------------|
| Name            | Name                           |
| Type            | string                         |
| Description     | Name of the cost center.       |
| Required        | True                           |


| Parameters      | Description                    |
|------------------|---------------------------------|
| Name            | Description                    |
| Type            | string                         |
| Description     | Description of the cost center. |
| Required        | False                          |


| Parameters      | Description                    |
|------------------|---------------------------------|
| Name            | xp                             |
| Type            | object                         |
| Description     | Container for extended (custom) properties of the cost center. |
| Required        | False                          |

## `PUT` `v1/buyers/{buyerID}/costcenters/{costCenterID}`
Create or update a cost center

| Parameters      | Description                    |
|------------------|---------------------------------|


| Parameters      | Description                    |
|------------------|---------------------------------|
| Name            | buyerID                        |
| Type            | string                         |
| Description     | ID of the buyer.               |
| Required        | True                           |


| Parameters      | Description                    |
|------------------|---------------------------------|
| Name            | costCenterID                   |
| Type            | string                         |
| Description     | ID of the cost center.         |
| Required        | True                           |

## Requestbody
```
{'ID': '', 'Name': '', 'Description': '', 'xp': {}}
```

```
[{'Name': 'ID', 'Type': 'string', 'Description': 'ID of the cost center. Can only contain characters Aa-Zz, 0-9, -, and _. Searchable: priority level 1. Sortable: priority level 2.', 'Required': False}, {'Name': 'Name', 'Type': 'string', 'Description': 'Name of the cost center. Required. Max length 100 characters. Searchable: priority level 2. Sortable: priority level 1.', 'Required': True}, {'Name': 'Description', 'Type': 'string', 'Description': 'Description of the cost center. Max length 2000 characters. Searchable: priority level 3.', 'Required': False}, {'Name': 'xp', 'Type': 'object', 'Description': 'Container for extended (custom) properties of the cost center.', 'Required': False}]
```

**Responsestatus**: `200`

## Responsebody
```
{'ID': '', 'Name': '', 'Description': '', 'xp': {}}
```


| Parameters      | Description                    |
|------------------|---------------------------------|
| Name            | ID                             |
| Type            | string                         |
| Description     | ID of the cost center.         |
| Required        | False                          |


| Parameters      | Description                    |
|------------------|---------------------------------|
| Name            | Name                           |
| Type            | string                         |
| Description     | Name of the cost center.       |
| Required        | True                           |


| Parameters      | Description                    |
|------------------|---------------------------------|
| Name            | Description                    |
| Type            | string                         |
| Description     | Description of the cost center. |
| Required        | False                          |


| Parameters      | Description                    |
|------------------|---------------------------------|
| Name            | xp                             |
| Type            | object                         |
| Description     | Container for extended (custom) properties of the cost center. |
| Required        | False                          |

## `DELETE` `v1/buyers/{buyerID}/costcenters/{costCenterID}`
Delete a cost center

| Parameters      | Description                    |
|------------------|---------------------------------|


| Parameters      | Description                    |
|------------------|---------------------------------|
| Name            | buyerID                        |
| Type            | string                         |
| Description     | ID of the buyer.               |
| Required        | True                           |


| Parameters      | Description                    |
|------------------|---------------------------------|
| Name            | costCenterID                   |
| Type            | string                         |
| Description     | ID of the cost center.         |
| Required        | True                           |

## Requestbody
**Responsestatus**: `204`

## Responsebody
## `PATCH` `v1/buyers/{buyerID}/costcenters/{costCenterID}`
Partially update a cost center

| Parameters      | Description                    |
|------------------|---------------------------------|


| Parameters      | Description                    |
|------------------|---------------------------------|
| Name            | buyerID                        |
| Type            | string                         |
| Description     | ID of the buyer.               |
| Required        | True                           |


| Parameters      | Description                    |
|------------------|---------------------------------|
| Name            | costCenterID                   |
| Type            | string                         |
| Description     | ID of the cost center.         |
| Required        | True                           |

## Requestbody
```
{'ID': '', 'Name': '', 'Description': '', 'xp': {}}
```

```
[{'Name': 'ID', 'Type': 'string', 'Description': 'ID of the cost center. Can only contain characters Aa-Zz, 0-9, -, and _. Searchable: priority level 1. Sortable: priority level 2.', 'Required': False}, {'Name': 'Name', 'Type': 'string', 'Description': 'Name of the cost center. Required. Max length 100 characters. Searchable: priority level 2. Sortable: priority level 1.', 'Required': True}, {'Name': 'Description', 'Type': 'string', 'Description': 'Description of the cost center. Max length 2000 characters. Searchable: priority level 3.', 'Required': False}, {'Name': 'xp', 'Type': 'object', 'Description': 'Container for extended (custom) properties of the cost center.', 'Required': False}]
```

**Responsestatus**: `200`

## Responsebody
```
{'ID': '', 'Name': '', 'Description': '', 'xp': {}}
```


| Parameters      | Description                    |
|------------------|---------------------------------|
| Name            | ID                             |
| Type            | string                         |
| Description     | ID of the cost center.         |
| Required        | False                          |


| Parameters      | Description                    |
|------------------|---------------------------------|
| Name            | Name                           |
| Type            | string                         |
| Description     | Name of the cost center.       |
| Required        | True                           |


| Parameters      | Description                    |
|------------------|---------------------------------|
| Name            | Description                    |
| Type            | string                         |
| Description     | Description of the cost center. |
| Required        | False                          |


| Parameters      | Description                    |
|------------------|---------------------------------|
| Name            | xp                             |
| Type            | object                         |
| Description     | Container for extended (custom) properties of the cost center. |
| Required        | False                          |

## `GET` `v1/buyers/{buyerID}/costcenters/assignments`
Get a list of cost center assignments

| Parameters      | Description                    |
|------------------|---------------------------------|


| Parameters      | Description                    |
|------------------|---------------------------------|
| Name            | buyerID                        |
| Type            | string                         |
| Description     | ID of the buyer.               |
| Required        | True                           |


| Parameters      | Description                    |
|------------------|---------------------------------|
| Name            | costCenterID                   |
| Type            | string                         |
| Description     | ID of the cost center.         |
| Required        | False                          |


| Parameters      | Description                    |
|------------------|---------------------------------|
| Name            | userID                         |
| Type            | string                         |
| Description     | ID of the user.                |
| Required        | False                          |


| Parameters      | Description                    |
|------------------|---------------------------------|
| Name            | userGroupID                    |
| Type            | string                         |
| Description     | ID of the user group.          |
| Required        | False                          |


| Parameters      | Description                    |
|------------------|---------------------------------|
| Name            | level                          |
| Type            | string                         |
| Description     | Level of the cost center assignment. Possible values: User, Group, Company. |
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

## Requestbody
**Responsestatus**: `200`

## Responsebody
```
{'Meta': {'Page': 1, 'PageSize': 20, 'TotalCount': 25, 'TotalPages': 2, 'ItemRange': [1, 20]}, 'Items': [{'CostCenterID': '', 'UserGroupID': ''}]}
```


| Parameters      | Description                    |
|------------------|---------------------------------|
| Name            | CostCenterID                   |
| Type            | string                         |
| Description     | ID of the cost center.         |
| Required        | True                           |


| Parameters      | Description                    |
|------------------|---------------------------------|
| Name            | UserGroupID                    |
| Type            | string                         |
| Description     | ID of the user group.          |
| Required        | False                          |

## `DELETE` `v1/buyers/{buyerID}/costcenters/{costCenterID}/assignments`
Delete a cost center assignment

| Parameters      | Description                    |
|------------------|---------------------------------|


| Parameters      | Description                    |
|------------------|---------------------------------|
| Name            | buyerID                        |
| Type            | string                         |
| Description     | ID of the buyer.               |
| Required        | True                           |


| Parameters      | Description                    |
|------------------|---------------------------------|
| Name            | costCenterID                   |
| Type            | string                         |
| Description     | ID of the cost center.         |
| Required        | True                           |


| Parameters      | Description                    |
|------------------|---------------------------------|
| Name            | userID                         |
| Type            | string                         |
| Description     | ID of the user.                |
| Required        | False                          |


| Parameters      | Description                    |
|------------------|---------------------------------|
| Name            | userGroupID                    |
| Type            | string                         |
| Description     | ID of the user group.          |
| Required        | False                          |

## Requestbody
**Responsestatus**: `204`

## Responsebody
## `POST` `v1/buyers/{buyerID}/costcenters/assignments`
Save a cost center assignment

| Parameters      | Description                    |
|------------------|---------------------------------|


| Parameters      | Description                    |
|------------------|---------------------------------|
| Name            | buyerID                        |
| Type            | string                         |
| Description     | ID of the buyer.               |
| Required        | True                           |

## Requestbody
```
{'CostCenterID': '', 'UserGroupID': ''}
```

```
[{'Name': 'CostCenterID', 'Type': 'string', 'Description': 'ID of the cost center. Required. Sortable: priority level 1.', 'Required': True}, {'Name': 'UserGroupID', 'Type': 'string', 'Description': 'ID of the user group. Sortable: priority level 3.', 'Required': False}]
```

**Responsestatus**: `204`

## Responsebody