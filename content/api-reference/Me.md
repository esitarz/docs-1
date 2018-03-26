---
title: Me
date: 2018-03-26
category: API Reference
tags: Me And My Stuff
slug: Me-And-My-Stuff-Me
---
"Me" is a container for read-only endpoints that return a filtered view
of things that the current buyer user is allowed to see, i.e. things
that they are assigned to either directly or as a member of a buyer
organization or user group. It also provides ways for a user to update
or change their own information.

---

## `GET` `v1/me`
Get the Current Authenticated User
## Requestbody
**Responsestatus**: `200`

## Responsebody
```
{'Buyer': {'ID': '', 'DefaultCatalogID': ''}, 'ID': '', 'Username': '', 'FirstName': '', 'LastName': '', 'Email': '', 'Phone': '', 'TermsAccepted': '2018-03-21T23:00:00+00:00', 'Active': False, 'xp': {}, 'AvailableRoles': ['']}
```


| Parameters      | Description                    |
|------------------|---------------------------------|
| Name            | Buyer                          |
| Type            | object                         |
| Description     | Buyer of the user.             |
| Required        | False                          |


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

## `PUT` `v1/me`
Update the Currently Authenticated User
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
{'Buyer': {'ID': '', 'DefaultCatalogID': ''}, 'ID': '', 'Username': '', 'FirstName': '', 'LastName': '', 'Email': '', 'Phone': '', 'TermsAccepted': '2018-03-21T23:00:00+00:00', 'Active': False, 'xp': {}, 'AvailableRoles': ['']}
```


| Parameters      | Description                    |
|------------------|---------------------------------|
| Name            | Buyer                          |
| Type            | object                         |
| Description     | Buyer of the user.             |
| Required        | False                          |


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

## `PATCH` `v1/me`
Patch the Currently Authenticated User
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
{'Buyer': {'ID': '', 'DefaultCatalogID': ''}, 'ID': '', 'Username': '', 'FirstName': '', 'LastName': '', 'Email': '', 'Phone': '', 'TermsAccepted': '2018-03-21T23:00:00+00:00', 'Active': False, 'xp': {}, 'AvailableRoles': ['']}
```


| Parameters      | Description                    |
|------------------|---------------------------------|
| Name            | Buyer                          |
| Type            | object                         |
| Description     | Buyer of the user.             |
| Required        | False                          |


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

## `PUT` `v1/me/register`
Register a register

| Parameters      | Description                    |
|------------------|---------------------------------|


| Parameters      | Description                    |
|------------------|---------------------------------|
| Name            | anonUserToken                  |
| Type            | string                         |
| Description     | Anon user token of the user.   |
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
{}
```

## `PUT` `v1/me/orders`
Transfer a anon user order

| Parameters      | Description                    |
|------------------|---------------------------------|


| Parameters      | Description                    |
|------------------|---------------------------------|
| Name            | anonUserToken                  |
| Type            | string                         |
| Description     | Anon user token of the me.     |
| Required        | True                           |

## Requestbody
**Responsestatus**: `204`

## Responsebody
## `POST` `v1/me/password`
Reset a password by token
## Requestbody
```
{'NewPassword': ''}
```

```
[{'Name': 'NewPassword', 'Type': 'string', 'Description': 'New password of the token password reset. Required.', 'Required': True}]
```

**Responsestatus**: `204`

## Responsebody