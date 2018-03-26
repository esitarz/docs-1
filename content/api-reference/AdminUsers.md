---
title: Admin Users
date: 2018-03-26
category: API Reference
tags: Seller
slug: Seller-AdminUsers
---
Users on an Organization level are users that have administrative access
to things like adding users, creating catalogs, processing orders or
creating products. These users are not specific to a buyer company.

---

## `GET` `v1/adminusers/{userID}`
Get a single admin user

| Parameters      | Description                    |
|------------------|---------------------------------|


| Parameters      | Description                    |
|------------------|---------------------------------|
| Name            | userID                         |
| Type            | string                         |
| Description     | ID of the user.                |
| Required        | True                           |

## Requestbody
**Responsestatus**: `200`

## Responsebody
```
{'ID': '', 'Username': '', 'FirstName': '', 'LastName': '', 'Email': '', 'Phone': '', 'TermsAccepted': '2018-03-21T23:00:00+00:00', 'Active': False, 'xp': {}, 'AvailableRoles': ['']}
```


| Parameters      | Description                    |
|------------------|---------------------------------|
| Name            | ID                             |
| Type            | string                         |
| Description     | ID of the user.                |
| Required        | False                          |


| Parameters      | Description                    |
|------------------|---------------------------------|
| Name            | Username                       |
| Type            | string                         |
| Description     | Username of the user.          |
| Required        | True                           |


| Parameters      | Description                    |
|------------------|---------------------------------|
| Name            | FirstName                      |
| Type            | string                         |
| Description     | First name of the user.        |
| Required        | True                           |


| Parameters      | Description                    |
|------------------|---------------------------------|
| Name            | LastName                       |
| Type            | string                         |
| Description     | Last name of the user.         |
| Required        | True                           |


| Parameters      | Description                    |
|------------------|---------------------------------|
| Name            | Email                          |
| Type            | string                         |
| Description     | Email of the user.             |
| Required        | True                           |


| Parameters      | Description                    |
|------------------|---------------------------------|
| Name            | Phone                          |
| Type            | string                         |
| Description     | Phone of the user.             |
| Required        | False                          |


| Parameters      | Description                    |
|------------------|---------------------------------|
| Name            | TermsAccepted                  |
| Type            | date                           |
| Description     | Terms accepted of the user.    |
| Required        | False                          |


| Parameters      | Description                    |
|------------------|---------------------------------|
| Name            | Active                         |
| Type            | boolean                        |
| Description     | Active of the user.            |
| Required        | True                           |


| Parameters      | Description                    |
|------------------|---------------------------------|
| Name            | xp                             |
| Type            | object                         |
| Description     | Container for extended (custom) properties of the user. |
| Required        | False                          |


| Parameters      | Description                    |
|------------------|---------------------------------|
| Name            | AvailableRoles                 |
| Type            | array                          |
| Description     | Available roles of the user.   |
| Required        | False                          |

## `GET` `v1/adminusers`
Get a list of admin users

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
{'Meta': {'Page': 1, 'PageSize': 20, 'TotalCount': 25, 'TotalPages': 2, 'ItemRange': [1, 20]}, 'Items': [{'ID': '', 'Username': '', 'FirstName': '', 'LastName': '', 'Email': '', 'Phone': '', 'TermsAccepted': '2018-03-21T23:00:00+00:00', 'Active': False, 'xp': {}, 'AvailableRoles': ['']}]}
```


| Parameters      | Description                    |
|------------------|---------------------------------|
| Name            | ID                             |
| Type            | string                         |
| Description     | ID of the user.                |
| Required        | False                          |


| Parameters      | Description                    |
|------------------|---------------------------------|
| Name            | Username                       |
| Type            | string                         |
| Description     | Username of the user.          |
| Required        | True                           |


| Parameters      | Description                    |
|------------------|---------------------------------|
| Name            | FirstName                      |
| Type            | string                         |
| Description     | First name of the user.        |
| Required        | True                           |


| Parameters      | Description                    |
|------------------|---------------------------------|
| Name            | LastName                       |
| Type            | string                         |
| Description     | Last name of the user.         |
| Required        | True                           |


| Parameters      | Description                    |
|------------------|---------------------------------|
| Name            | Email                          |
| Type            | string                         |
| Description     | Email of the user.             |
| Required        | True                           |


| Parameters      | Description                    |
|------------------|---------------------------------|
| Name            | Phone                          |
| Type            | string                         |
| Description     | Phone of the user.             |
| Required        | False                          |


| Parameters      | Description                    |
|------------------|---------------------------------|
| Name            | TermsAccepted                  |
| Type            | date                           |
| Description     | Terms accepted of the user.    |
| Required        | False                          |


| Parameters      | Description                    |
|------------------|---------------------------------|
| Name            | Active                         |
| Type            | boolean                        |
| Description     | Active of the user.            |
| Required        | True                           |


| Parameters      | Description                    |
|------------------|---------------------------------|
| Name            | xp                             |
| Type            | object                         |
| Description     | Container for extended (custom) properties of the user. |
| Required        | False                          |


| Parameters      | Description                    |
|------------------|---------------------------------|
| Name            | AvailableRoles                 |
| Type            | array                          |
| Description     | Available roles of the user.   |
| Required        | False                          |

## `POST` `v1/adminusers`
Create a new admin user
## Requestbody
```
{'ID': '', 'Username': '', 'Password': '', 'FirstName': '', 'LastName': '', 'Email': '', 'Phone': '', 'TermsAccepted': '2018-03-21T23:00:00+00:00', 'Active': False, 'xp': {}}
```

```
[{'Name': 'ID', 'Type': 'string', 'Description': 'ID of the user. Can only contain characters Aa-Zz, 0-9, -, and _. Searchable: priority level 1. Sortable.', 'Required': False}, {'Name': 'Username', 'Type': 'string', 'Description': 'Username of the user. Required. Max length 100 characters. Searchable: priority level 2. Sortable: priority level 3.', 'Required': True}, {'Name': 'Password', 'Type': 'string', 'Description': 'Password of the user.', 'Required': False}, {'Name': 'FirstName', 'Type': 'string', 'Description': 'First name of the user. Required. Max length 100 characters. Searchable: priority level 4. Sortable: priority level 2.', 'Required': True}, {'Name': 'LastName', 'Type': 'string', 'Description': 'Last name of the user. Required. Max length 100 characters. Searchable: priority level 3. Sortable: priority level 1.', 'Required': True}, {'Name': 'Email', 'Type': 'string', 'Description': 'Email of the user. Required. Max length 200 characters. Searchable: priority level 5. Sortable.', 'Required': True}, {'Name': 'Phone', 'Type': 'string', 'Description': 'Phone of the user. Max length 100 characters.', 'Required': False}, {'Name': 'TermsAccepted', 'Type': 'date', 'Description': 'Terms accepted of the user.', 'Required': False}, {'Name': 'Active', 'Type': 'boolean', 'Description': 'Active of the user. Required.', 'Required': True}, {'Name': 'xp', 'Type': 'object', 'Description': 'Container for extended (custom) properties of the user.', 'Required': False}]
```

**Responsestatus**: `201`

## Responsebody
```
{'ID': '', 'Username': '', 'FirstName': '', 'LastName': '', 'Email': '', 'Phone': '', 'TermsAccepted': '2018-03-21T23:00:00+00:00', 'Active': False, 'xp': {}, 'AvailableRoles': ['']}
```


| Parameters      | Description                    |
|------------------|---------------------------------|
| Name            | ID                             |
| Type            | string                         |
| Description     | ID of the user.                |
| Required        | False                          |


| Parameters      | Description                    |
|------------------|---------------------------------|
| Name            | Username                       |
| Type            | string                         |
| Description     | Username of the user.          |
| Required        | True                           |


| Parameters      | Description                    |
|------------------|---------------------------------|
| Name            | FirstName                      |
| Type            | string                         |
| Description     | First name of the user.        |
| Required        | True                           |


| Parameters      | Description                    |
|------------------|---------------------------------|
| Name            | LastName                       |
| Type            | string                         |
| Description     | Last name of the user.         |
| Required        | True                           |


| Parameters      | Description                    |
|------------------|---------------------------------|
| Name            | Email                          |
| Type            | string                         |
| Description     | Email of the user.             |
| Required        | True                           |


| Parameters      | Description                    |
|------------------|---------------------------------|
| Name            | Phone                          |
| Type            | string                         |
| Description     | Phone of the user.             |
| Required        | False                          |


| Parameters      | Description                    |
|------------------|---------------------------------|
| Name            | TermsAccepted                  |
| Type            | date                           |
| Description     | Terms accepted of the user.    |
| Required        | False                          |


| Parameters      | Description                    |
|------------------|---------------------------------|
| Name            | Active                         |
| Type            | boolean                        |
| Description     | Active of the user.            |
| Required        | True                           |


| Parameters      | Description                    |
|------------------|---------------------------------|
| Name            | xp                             |
| Type            | object                         |
| Description     | Container for extended (custom) properties of the user. |
| Required        | False                          |


| Parameters      | Description                    |
|------------------|---------------------------------|
| Name            | AvailableRoles                 |
| Type            | array                          |
| Description     | Available roles of the user.   |
| Required        | False                          |

## `PUT` `v1/adminusers/{userID}`
Create or update an admin user

| Parameters      | Description                    |
|------------------|---------------------------------|


| Parameters      | Description                    |
|------------------|---------------------------------|
| Name            | userID                         |
| Type            | string                         |
| Description     | ID of the user.                |
| Required        | True                           |

## Requestbody
```
{'ID': '', 'Username': '', 'Password': '', 'FirstName': '', 'LastName': '', 'Email': '', 'Phone': '', 'TermsAccepted': '2018-03-21T23:00:00+00:00', 'Active': False, 'xp': {}}
```

```
[{'Name': 'ID', 'Type': 'string', 'Description': 'ID of the user. Can only contain characters Aa-Zz, 0-9, -, and _. Searchable: priority level 1. Sortable.', 'Required': False}, {'Name': 'Username', 'Type': 'string', 'Description': 'Username of the user. Required. Max length 100 characters. Searchable: priority level 2. Sortable: priority level 3.', 'Required': True}, {'Name': 'Password', 'Type': 'string', 'Description': 'Password of the user.', 'Required': False}, {'Name': 'FirstName', 'Type': 'string', 'Description': 'First name of the user. Required. Max length 100 characters. Searchable: priority level 4. Sortable: priority level 2.', 'Required': True}, {'Name': 'LastName', 'Type': 'string', 'Description': 'Last name of the user. Required. Max length 100 characters. Searchable: priority level 3. Sortable: priority level 1.', 'Required': True}, {'Name': 'Email', 'Type': 'string', 'Description': 'Email of the user. Required. Max length 200 characters. Searchable: priority level 5. Sortable.', 'Required': True}, {'Name': 'Phone', 'Type': 'string', 'Description': 'Phone of the user. Max length 100 characters.', 'Required': False}, {'Name': 'TermsAccepted', 'Type': 'date', 'Description': 'Terms accepted of the user.', 'Required': False}, {'Name': 'Active', 'Type': 'boolean', 'Description': 'Active of the user. Required.', 'Required': True}, {'Name': 'xp', 'Type': 'object', 'Description': 'Container for extended (custom) properties of the user.', 'Required': False}]
```

**Responsestatus**: `200`

## Responsebody
```
{'ID': '', 'Username': '', 'FirstName': '', 'LastName': '', 'Email': '', 'Phone': '', 'TermsAccepted': '2018-03-21T23:00:00+00:00', 'Active': False, 'xp': {}, 'AvailableRoles': ['']}
```


| Parameters      | Description                    |
|------------------|---------------------------------|
| Name            | ID                             |
| Type            | string                         |
| Description     | ID of the user.                |
| Required        | False                          |


| Parameters      | Description                    |
|------------------|---------------------------------|
| Name            | Username                       |
| Type            | string                         |
| Description     | Username of the user.          |
| Required        | True                           |


| Parameters      | Description                    |
|------------------|---------------------------------|
| Name            | FirstName                      |
| Type            | string                         |
| Description     | First name of the user.        |
| Required        | True                           |


| Parameters      | Description                    |
|------------------|---------------------------------|
| Name            | LastName                       |
| Type            | string                         |
| Description     | Last name of the user.         |
| Required        | True                           |


| Parameters      | Description                    |
|------------------|---------------------------------|
| Name            | Email                          |
| Type            | string                         |
| Description     | Email of the user.             |
| Required        | True                           |


| Parameters      | Description                    |
|------------------|---------------------------------|
| Name            | Phone                          |
| Type            | string                         |
| Description     | Phone of the user.             |
| Required        | False                          |


| Parameters      | Description                    |
|------------------|---------------------------------|
| Name            | TermsAccepted                  |
| Type            | date                           |
| Description     | Terms accepted of the user.    |
| Required        | False                          |


| Parameters      | Description                    |
|------------------|---------------------------------|
| Name            | Active                         |
| Type            | boolean                        |
| Description     | Active of the user.            |
| Required        | True                           |


| Parameters      | Description                    |
|------------------|---------------------------------|
| Name            | xp                             |
| Type            | object                         |
| Description     | Container for extended (custom) properties of the user. |
| Required        | False                          |


| Parameters      | Description                    |
|------------------|---------------------------------|
| Name            | AvailableRoles                 |
| Type            | array                          |
| Description     | Available roles of the user.   |
| Required        | False                          |

## `DELETE` `v1/adminusers/{userID}`
Delete an admin user

| Parameters      | Description                    |
|------------------|---------------------------------|


| Parameters      | Description                    |
|------------------|---------------------------------|
| Name            | userID                         |
| Type            | string                         |
| Description     | ID of the user.                |
| Required        | True                           |

## Requestbody
**Responsestatus**: `204`

## Responsebody
## `PATCH` `v1/adminusers/{userID}`
Partially update an admin user

| Parameters      | Description                    |
|------------------|---------------------------------|


| Parameters      | Description                    |
|------------------|---------------------------------|
| Name            | userID                         |
| Type            | string                         |
| Description     | ID of the user.                |
| Required        | True                           |

## Requestbody
```
{'ID': '', 'Username': '', 'Password': '', 'FirstName': '', 'LastName': '', 'Email': '', 'Phone': '', 'TermsAccepted': '2018-03-21T23:00:00+00:00', 'Active': False, 'xp': {}}
```

```
[{'Name': 'ID', 'Type': 'string', 'Description': 'ID of the user. Can only contain characters Aa-Zz, 0-9, -, and _. Searchable: priority level 1. Sortable.', 'Required': False}, {'Name': 'Username', 'Type': 'string', 'Description': 'Username of the user. Required. Max length 100 characters. Searchable: priority level 2. Sortable: priority level 3.', 'Required': True}, {'Name': 'Password', 'Type': 'string', 'Description': 'Password of the user.', 'Required': False}, {'Name': 'FirstName', 'Type': 'string', 'Description': 'First name of the user. Required. Max length 100 characters. Searchable: priority level 4. Sortable: priority level 2.', 'Required': True}, {'Name': 'LastName', 'Type': 'string', 'Description': 'Last name of the user. Required. Max length 100 characters. Searchable: priority level 3. Sortable: priority level 1.', 'Required': True}, {'Name': 'Email', 'Type': 'string', 'Description': 'Email of the user. Required. Max length 200 characters. Searchable: priority level 5. Sortable.', 'Required': True}, {'Name': 'Phone', 'Type': 'string', 'Description': 'Phone of the user. Max length 100 characters.', 'Required': False}, {'Name': 'TermsAccepted', 'Type': 'date', 'Description': 'Terms accepted of the user.', 'Required': False}, {'Name': 'Active', 'Type': 'boolean', 'Description': 'Active of the user. Required.', 'Required': True}, {'Name': 'xp', 'Type': 'object', 'Description': 'Container for extended (custom) properties of the user.', 'Required': False}]
```

**Responsestatus**: `200`

## Responsebody
```
{'ID': '', 'Username': '', 'FirstName': '', 'LastName': '', 'Email': '', 'Phone': '', 'TermsAccepted': '2018-03-21T23:00:00+00:00', 'Active': False, 'xp': {}, 'AvailableRoles': ['']}
```


| Parameters      | Description                    |
|------------------|---------------------------------|
| Name            | ID                             |
| Type            | string                         |
| Description     | ID of the user.                |
| Required        | False                          |


| Parameters      | Description                    |
|------------------|---------------------------------|
| Name            | Username                       |
| Type            | string                         |
| Description     | Username of the user.          |
| Required        | True                           |


| Parameters      | Description                    |
|------------------|---------------------------------|
| Name            | FirstName                      |
| Type            | string                         |
| Description     | First name of the user.        |
| Required        | True                           |


| Parameters      | Description                    |
|------------------|---------------------------------|
| Name            | LastName                       |
| Type            | string                         |
| Description     | Last name of the user.         |
| Required        | True                           |


| Parameters      | Description                    |
|------------------|---------------------------------|
| Name            | Email                          |
| Type            | string                         |
| Description     | Email of the user.             |
| Required        | True                           |


| Parameters      | Description                    |
|------------------|---------------------------------|
| Name            | Phone                          |
| Type            | string                         |
| Description     | Phone of the user.             |
| Required        | False                          |


| Parameters      | Description                    |
|------------------|---------------------------------|
| Name            | TermsAccepted                  |
| Type            | date                           |
| Description     | Terms accepted of the user.    |
| Required        | False                          |


| Parameters      | Description                    |
|------------------|---------------------------------|
| Name            | Active                         |
| Type            | boolean                        |
| Description     | Active of the user.            |
| Required        | True                           |


| Parameters      | Description                    |
|------------------|---------------------------------|
| Name            | xp                             |
| Type            | object                         |
| Description     | Container for extended (custom) properties of the user. |
| Required        | False                          |


| Parameters      | Description                    |
|------------------|---------------------------------|
| Name            | AvailableRoles                 |
| Type            | array                          |
| Description     | Available roles of the user.   |
| Required        | False                          |
