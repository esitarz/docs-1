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

## `GET` `v1/incrementors/{incrementorID}`
Get a single incrementor

| Parameters      | Description                    |
|------------------|---------------------------------|


| Parameters      | Description                    |
|------------------|---------------------------------|
| Name            | incrementorID                  |
| Type            | string                         |
| Description     | ID of the incrementor.         |
| Required        | True                           |

## Requestbody
**Responsestatus**: `200`

## Responsebody
```
{'ID': '', 'Name': '', 'LastNumber': 0, 'LeftPaddingCount': 0}
```


| Parameters      | Description                    |
|------------------|---------------------------------|
| Name            | ID                             |
| Type            | string                         |
| Description     | ID of the incrementor.         |
| Required        | False                          |


| Parameters      | Description                    |
|------------------|---------------------------------|
| Name            | Name                           |
| Type            | string                         |
| Description     | Name of the incrementor.       |
| Required        | False                          |


| Parameters      | Description                    |
|------------------|---------------------------------|
| Name            | LastNumber                     |
| Type            | integer                        |
| Description     | Last number of the incrementor. |
| Required        | True                           |


| Parameters      | Description                    |
|------------------|---------------------------------|
| Name            | LeftPaddingCount               |
| Type            | integer                        |
| Description     | Left padding count of the incrementor. |
| Required        | True                           |

## `GET` `v1/incrementors`
Get a list of incrementors

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
{'Meta': {'Page': 1, 'PageSize': 20, 'TotalCount': 25, 'TotalPages': 2, 'ItemRange': [1, 20]}, 'Items': [{'ID': '', 'Name': '', 'LastNumber': 0, 'LeftPaddingCount': 0}]}
```


| Parameters      | Description                    |
|------------------|---------------------------------|
| Name            | ID                             |
| Type            | string                         |
| Description     | ID of the incrementor.         |
| Required        | False                          |


| Parameters      | Description                    |
|------------------|---------------------------------|
| Name            | Name                           |
| Type            | string                         |
| Description     | Name of the incrementor.       |
| Required        | False                          |


| Parameters      | Description                    |
|------------------|---------------------------------|
| Name            | LastNumber                     |
| Type            | integer                        |
| Description     | Last number of the incrementor. |
| Required        | True                           |


| Parameters      | Description                    |
|------------------|---------------------------------|
| Name            | LeftPaddingCount               |
| Type            | integer                        |
| Description     | Left padding count of the incrementor. |
| Required        | True                           |

## `POST` `v1/incrementors`
Create a new incrementor
## Requestbody
```
{'ID': '', 'Name': '', 'LastNumber': 0, 'LeftPaddingCount': 0}
```

```
[{'Name': 'ID', 'Type': 'string', 'Description': 'ID of the incrementor. Can only contain characters Aa-Zz, 0-9, -, and _. Searchable: priority level 1. Sortable: priority level 1.', 'Required': False}, {'Name': 'Name', 'Type': 'string', 'Description': 'Name of the incrementor. Max length 100 characters. Searchable: priority level 2. Sortable: priority level 2.', 'Required': False}, {'Name': 'LastNumber', 'Type': 'integer', 'Description': 'Last number of the incrementor. Required. Must be between 0 and 2147483647.', 'Required': True}, {'Name': 'LeftPaddingCount', 'Type': 'integer', 'Description': 'Left padding count of the incrementor. Required. Must be between 0 and 25.', 'Required': True}]
```

**Responsestatus**: `201`

## Responsebody
```
{'ID': '', 'Name': '', 'LastNumber': 0, 'LeftPaddingCount': 0}
```


| Parameters      | Description                    |
|------------------|---------------------------------|
| Name            | ID                             |
| Type            | string                         |
| Description     | ID of the incrementor.         |
| Required        | False                          |


| Parameters      | Description                    |
|------------------|---------------------------------|
| Name            | Name                           |
| Type            | string                         |
| Description     | Name of the incrementor.       |
| Required        | False                          |


| Parameters      | Description                    |
|------------------|---------------------------------|
| Name            | LastNumber                     |
| Type            | integer                        |
| Description     | Last number of the incrementor. |
| Required        | True                           |


| Parameters      | Description                    |
|------------------|---------------------------------|
| Name            | LeftPaddingCount               |
| Type            | integer                        |
| Description     | Left padding count of the incrementor. |
| Required        | True                           |

## `PUT` `v1/incrementors/{incrementorID}`
Create or update an incrementor

| Parameters      | Description                    |
|------------------|---------------------------------|


| Parameters      | Description                    |
|------------------|---------------------------------|
| Name            | incrementorID                  |
| Type            | string                         |
| Description     | ID of the incrementor.         |
| Required        | True                           |

## Requestbody
```
{'ID': '', 'Name': '', 'LastNumber': 0, 'LeftPaddingCount': 0}
```

```
[{'Name': 'ID', 'Type': 'string', 'Description': 'ID of the incrementor. Can only contain characters Aa-Zz, 0-9, -, and _. Searchable: priority level 1. Sortable: priority level 1.', 'Required': False}, {'Name': 'Name', 'Type': 'string', 'Description': 'Name of the incrementor. Max length 100 characters. Searchable: priority level 2. Sortable: priority level 2.', 'Required': False}, {'Name': 'LastNumber', 'Type': 'integer', 'Description': 'Last number of the incrementor. Required. Must be between 0 and 2147483647.', 'Required': True}, {'Name': 'LeftPaddingCount', 'Type': 'integer', 'Description': 'Left padding count of the incrementor. Required. Must be between 0 and 25.', 'Required': True}]
```

**Responsestatus**: `200`

## Responsebody
```
{'ID': '', 'Name': '', 'LastNumber': 0, 'LeftPaddingCount': 0}
```


| Parameters      | Description                    |
|------------------|---------------------------------|
| Name            | ID                             |
| Type            | string                         |
| Description     | ID of the incrementor.         |
| Required        | False                          |


| Parameters      | Description                    |
|------------------|---------------------------------|
| Name            | Name                           |
| Type            | string                         |
| Description     | Name of the incrementor.       |
| Required        | False                          |


| Parameters      | Description                    |
|------------------|---------------------------------|
| Name            | LastNumber                     |
| Type            | integer                        |
| Description     | Last number of the incrementor. |
| Required        | True                           |


| Parameters      | Description                    |
|------------------|---------------------------------|
| Name            | LeftPaddingCount               |
| Type            | integer                        |
| Description     | Left padding count of the incrementor. |
| Required        | True                           |

## `DELETE` `v1/incrementors/{incrementorID}`
Delete an incrementor

| Parameters      | Description                    |
|------------------|---------------------------------|


| Parameters      | Description                    |
|------------------|---------------------------------|
| Name            | incrementorID                  |
| Type            | string                         |
| Description     | ID of the incrementor.         |
| Required        | True                           |

## Requestbody
**Responsestatus**: `204`

## Responsebody
## `PATCH` `v1/incrementors/{incrementorID}`
Partially update an incrementor

| Parameters      | Description                    |
|------------------|---------------------------------|


| Parameters      | Description                    |
|------------------|---------------------------------|
| Name            | incrementorID                  |
| Type            | string                         |
| Description     | ID of the incrementor.         |
| Required        | True                           |

## Requestbody
```
{'ID': '', 'Name': '', 'LastNumber': 0, 'LeftPaddingCount': 0}
```

```
[{'Name': 'ID', 'Type': 'string', 'Description': 'ID of the incrementor. Can only contain characters Aa-Zz, 0-9, -, and _. Searchable: priority level 1. Sortable: priority level 1.', 'Required': False}, {'Name': 'Name', 'Type': 'string', 'Description': 'Name of the incrementor. Max length 100 characters. Searchable: priority level 2. Sortable: priority level 2.', 'Required': False}, {'Name': 'LastNumber', 'Type': 'integer', 'Description': 'Last number of the incrementor. Required. Must be between 0 and 2147483647.', 'Required': True}, {'Name': 'LeftPaddingCount', 'Type': 'integer', 'Description': 'Left padding count of the incrementor. Required. Must be between 0 and 25.', 'Required': True}]
```

**Responsestatus**: `200`

## Responsebody
```
{'ID': '', 'Name': '', 'LastNumber': 0, 'LeftPaddingCount': 0}
```


| Parameters      | Description                    |
|------------------|---------------------------------|
| Name            | ID                             |
| Type            | string                         |
| Description     | ID of the incrementor.         |
| Required        | False                          |


| Parameters      | Description                    |
|------------------|---------------------------------|
| Name            | Name                           |
| Type            | string                         |
| Description     | Name of the incrementor.       |
| Required        | False                          |


| Parameters      | Description                    |
|------------------|---------------------------------|
| Name            | LastNumber                     |
| Type            | integer                        |
| Description     | Last number of the incrementor. |
| Required        | True                           |


| Parameters      | Description                    |
|------------------|---------------------------------|
| Name            | LeftPaddingCount               |
| Type            | integer                        |
| Description     | Left padding count of the incrementor. |
| Required        | True                           |
