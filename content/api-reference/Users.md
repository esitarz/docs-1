---
title: Users
date: 2018-03-23
category: API Reference
tags: Buyers
slug: Users
---
A user is a person with access to the application. The properties of a
user define who they are and what they are able to do with their login
to the application.

---

## `GET` `v1/buyers/{buyerID}/users/{userID}`
Get a single user

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

## `GET` `v1/buyers/{buyerID}/users`
Get a list of users

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
| Name            | userGroupID                    |
| Type            | string                         |
| Description     | ID of the user group.          |
| Required        | False                          |


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

## `POST` `v1/buyers/{buyerID}/users`
Create a new user

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

## `PUT` `v1/buyers/{buyerID}/users/{userID}`
Create or update a user

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

## `DELETE` `v1/buyers/{buyerID}/users/{userID}`
Delete a user

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
| Name            | userID                         |
| Type            | string                         |
| Description     | ID of the user.                |
| Required        | True                           |

## Requestbody
**Responsestatus**: `204`

## Responsebody
## `PATCH` `v1/buyers/{buyerID}/users/{userID}`
Partially update a user

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

## `POST` `v1/buyers/{buyerID}/users/{userID}/moveto/{newBuyerID}`
Move a user to a different buyer

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
| Name            | userID                         |
| Type            | string                         |
| Description     | ID of the user.                |
| Required        | True                           |


| Parameters      | Description                    |
|------------------|---------------------------------|
| Name            | newBuyerID                     |
| Type            | string                         |
| Description     | ID of the new buyer.           |
| Required        | True                           |


| Parameters      | Description                    |
|------------------|---------------------------------|
| Name            | orders                         |
| Type            | string                         |
| Description     | Orders of the user. Possible values: None, Unsubmitted, All. |
| Required        | True                           |

## Requestbody
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

## `POST` `v1/buyers/{buyerID}/users/{userID}/accesstoken`
Get a single user access token

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
| Name            | userID                         |
| Type            | string                         |
| Description     | ID of the user.                |
| Required        | True                           |

## Requestbody
```
{'ClientID': '', 'Roles': ['DevCenterImpersonate']}
```

```
[{'Name': 'ClientID', 'Type': 'string', 'Description': 'ID of the client.', 'Required': False}, {'Name': 'Roles', 'Type': 'array', 'Description': 'Roles of the impersonate token request.', 'Required': False}]
```

**Responsestatus**: `200`

## Responsebody
```
{'access_token': '', 'expires_in': 0, 'token_type': '', 'refresh_token': ''}
```


| Parameters      | Description                    |
|------------------|---------------------------------|
| Name            | access_token                   |
| Type            | string                         |
| Description     | Access token of the access token. |
| Required        | False                          |


| Parameters      | Description                    |
|------------------|---------------------------------|
| Name            | expires_in                     |
| Type            | integer                        |
| Description     | Expires in of the access token. |
| Required        | False                          |


| Parameters      | Description                    |
|------------------|---------------------------------|
| Name            | token_type                     |
| Type            | string                         |
| Description     | Token type of the access token. |
| Required        | False                          |


| Parameters      | Description                    |
|------------------|---------------------------------|
| Name            | refresh_token                  |
| Type            | string                         |
| Description     | Refresh token of the access token. |
| Required        | False                          |
