---
title: Supplier Users
date: 2018-03-23
category: API Reference
tags: Suppliers
slug: SupplierUsers
---
A user is a person with access to the application. The properties of a
user define who they are and what they are able to do with their login
to the application.

---

## Get a single supplier user
### `GET` `v1/suppliers/{supplierID}/users/{userID}`

| Parameters      | Description                    |
|------------------|---------------------------------|
| Name            | supplierID                     |
| Type            | string                         |
| Description     | ID of the supplier.            |
| Required        | True                           |
| Name            | userID                         |
| Type            | string                         |
| Description     | ID of the user.                |
| Required        | True                           |

 **Requestbody**: 
None
 **Responsestatus**: `200`

 **Responsebody**: 
{'Sample': '{\r\n  "ID": "",\r\n  "Username": "",\r\n  "FirstName": "",\r\n  "LastName": "",\r\n  "Email": "",\r\n  "Phone": "",\r\n  "TermsAccepted": "2018-03-21T23:00:00+00:00",\r\n  "Active": false,\r\n  "xp": {},\r\n  "AvailableRoles": [\r\n    ""\r\n  ]\r\n}', 'Fields': [{'Name': 'ID', 'Type': 'string', 'Description': 'ID of the user.', 'Required': False}, {'Name': 'Username', 'Type': 'string', 'Description': 'Username of the user.', 'Required': True}, {'Name': 'FirstName', 'Type': 'string', 'Description': 'First name of the user.', 'Required': True}, {'Name': 'LastName', 'Type': 'string', 'Description': 'Last name of the user.', 'Required': True}, {'Name': 'Email', 'Type': 'string', 'Description': 'Email of the user.', 'Required': True}, {'Name': 'Phone', 'Type': 'string', 'Description': 'Phone of the user.', 'Required': False}, {'Name': 'TermsAccepted', 'Type': 'date', 'Description': 'Terms accepted of the user.', 'Required': False}, {'Name': 'Active', 'Type': 'boolean', 'Description': 'Active of the user.', 'Required': True}, {'Name': 'xp', 'Type': 'object', 'Description': 'Container for extended (custom) properties of the user.', 'Required': False}, {'Name': 'AvailableRoles', 'Type': 'array', 'Description': 'Available roles of the user.', 'Required': False}]}
## Get a list of supplier users
### `GET` `v1/suppliers/{supplierID}/users`

| Parameters      | Description                    |
|------------------|---------------------------------|
| Name            | supplierID                     |
| Type            | string                         |
| Description     | ID of the supplier.            |
| Required        | True                           |
| Name            | userGroupID                    |
| Type            | string                         |
| Description     | ID of the user group.          |
| Required        | False                          |
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
{'Sample': '{\r\n  "Meta": {\r\n    "Page": 1,\r\n    "PageSize": 20,\r\n    "TotalCount": 25,\r\n    "TotalPages": 2,\r\n    "ItemRange": [\r\n      1,\r\n      20\r\n    ]\r\n  },\r\n  "Items": [\r\n    {\r\n      "ID": "",\r\n      "Username": "",\r\n      "FirstName": "",\r\n      "LastName": "",\r\n      "Email": "",\r\n      "Phone": "",\r\n      "TermsAccepted": "2018-03-21T23:00:00+00:00",\r\n      "Active": false,\r\n      "xp": {},\r\n      "AvailableRoles": [\r\n        ""\r\n      ]\r\n    }\r\n  ]\r\n}', 'Fields': [{'Name': 'ID', 'Type': 'string', 'Description': 'ID of the user.', 'Required': False}, {'Name': 'Username', 'Type': 'string', 'Description': 'Username of the user.', 'Required': True}, {'Name': 'FirstName', 'Type': 'string', 'Description': 'First name of the user.', 'Required': True}, {'Name': 'LastName', 'Type': 'string', 'Description': 'Last name of the user.', 'Required': True}, {'Name': 'Email', 'Type': 'string', 'Description': 'Email of the user.', 'Required': True}, {'Name': 'Phone', 'Type': 'string', 'Description': 'Phone of the user.', 'Required': False}, {'Name': 'TermsAccepted', 'Type': 'date', 'Description': 'Terms accepted of the user.', 'Required': False}, {'Name': 'Active', 'Type': 'boolean', 'Description': 'Active of the user.', 'Required': True}, {'Name': 'xp', 'Type': 'object', 'Description': 'Container for extended (custom) properties of the user.', 'Required': False}, {'Name': 'AvailableRoles', 'Type': 'array', 'Description': 'Available roles of the user.', 'Required': False}]}
## Create a new supplier user
### `POST` `v1/suppliers/{supplierID}/users`

| Parameters      | Description                    |
|------------------|---------------------------------|
| Name            | supplierID                     |
| Type            | string                         |
| Description     | ID of the supplier.            |
| Required        | True                           |

 **Requestbody**: 
{'Sample': '{\r\n  "ID": "",\r\n  "Username": "",\r\n  "Password": "",\r\n  "FirstName": "",\r\n  "LastName": "",\r\n  "Email": "",\r\n  "Phone": "",\r\n  "TermsAccepted": "2018-03-21T23:00:00+00:00",\r\n  "Active": false,\r\n  "xp": {}\r\n}', 'Fields': [{'Name': 'ID', 'Type': 'string', 'Description': 'ID of the user. Can only contain characters Aa-Zz, 0-9, -, and _. Searchable: priority level 1. Sortable.', 'Required': False}, {'Name': 'Username', 'Type': 'string', 'Description': 'Username of the user. Required. Max length 100 characters. Searchable: priority level 2. Sortable: priority level 3.', 'Required': True}, {'Name': 'Password', 'Type': 'string', 'Description': 'Password of the user.', 'Required': False}, {'Name': 'FirstName', 'Type': 'string', 'Description': 'First name of the user. Required. Max length 100 characters. Searchable: priority level 4. Sortable: priority level 2.', 'Required': True}, {'Name': 'LastName', 'Type': 'string', 'Description': 'Last name of the user. Required. Max length 100 characters. Searchable: priority level 3. Sortable: priority level 1.', 'Required': True}, {'Name': 'Email', 'Type': 'string', 'Description': 'Email of the user. Required. Max length 200 characters. Searchable: priority level 5. Sortable.', 'Required': True}, {'Name': 'Phone', 'Type': 'string', 'Description': 'Phone of the user. Max length 100 characters.', 'Required': False}, {'Name': 'TermsAccepted', 'Type': 'date', 'Description': 'Terms accepted of the user.', 'Required': False}, {'Name': 'Active', 'Type': 'boolean', 'Description': 'Active of the user. Required.', 'Required': True}, {'Name': 'xp', 'Type': 'object', 'Description': 'Container for extended (custom) properties of the user.', 'Required': False}]}
 **Responsestatus**: `201`

 **Responsebody**: 
{'Sample': '{\r\n  "ID": "",\r\n  "Username": "",\r\n  "FirstName": "",\r\n  "LastName": "",\r\n  "Email": "",\r\n  "Phone": "",\r\n  "TermsAccepted": "2018-03-21T23:00:00+00:00",\r\n  "Active": false,\r\n  "xp": {},\r\n  "AvailableRoles": [\r\n    ""\r\n  ]\r\n}', 'Fields': [{'Name': 'ID', 'Type': 'string', 'Description': 'ID of the user.', 'Required': False}, {'Name': 'Username', 'Type': 'string', 'Description': 'Username of the user.', 'Required': True}, {'Name': 'FirstName', 'Type': 'string', 'Description': 'First name of the user.', 'Required': True}, {'Name': 'LastName', 'Type': 'string', 'Description': 'Last name of the user.', 'Required': True}, {'Name': 'Email', 'Type': 'string', 'Description': 'Email of the user.', 'Required': True}, {'Name': 'Phone', 'Type': 'string', 'Description': 'Phone of the user.', 'Required': False}, {'Name': 'TermsAccepted', 'Type': 'date', 'Description': 'Terms accepted of the user.', 'Required': False}, {'Name': 'Active', 'Type': 'boolean', 'Description': 'Active of the user.', 'Required': True}, {'Name': 'xp', 'Type': 'object', 'Description': 'Container for extended (custom) properties of the user.', 'Required': False}, {'Name': 'AvailableRoles', 'Type': 'array', 'Description': 'Available roles of the user.', 'Required': False}]}
## Create or update a supplier user
### `PUT` `v1/suppliers/{supplierID}/users/{userID}`

| Parameters      | Description                    |
|------------------|---------------------------------|
| Name            | supplierID                     |
| Type            | string                         |
| Description     | ID of the supplier.            |
| Required        | True                           |
| Name            | userID                         |
| Type            | string                         |
| Description     | ID of the user.                |
| Required        | True                           |

 **Requestbody**: 
{'Sample': '{\r\n  "ID": "",\r\n  "Username": "",\r\n  "Password": "",\r\n  "FirstName": "",\r\n  "LastName": "",\r\n  "Email": "",\r\n  "Phone": "",\r\n  "TermsAccepted": "2018-03-21T23:00:00+00:00",\r\n  "Active": false,\r\n  "xp": {}\r\n}', 'Fields': [{'Name': 'ID', 'Type': 'string', 'Description': 'ID of the user. Can only contain characters Aa-Zz, 0-9, -, and _. Searchable: priority level 1. Sortable.', 'Required': False}, {'Name': 'Username', 'Type': 'string', 'Description': 'Username of the user. Required. Max length 100 characters. Searchable: priority level 2. Sortable: priority level 3.', 'Required': True}, {'Name': 'Password', 'Type': 'string', 'Description': 'Password of the user.', 'Required': False}, {'Name': 'FirstName', 'Type': 'string', 'Description': 'First name of the user. Required. Max length 100 characters. Searchable: priority level 4. Sortable: priority level 2.', 'Required': True}, {'Name': 'LastName', 'Type': 'string', 'Description': 'Last name of the user. Required. Max length 100 characters. Searchable: priority level 3. Sortable: priority level 1.', 'Required': True}, {'Name': 'Email', 'Type': 'string', 'Description': 'Email of the user. Required. Max length 200 characters. Searchable: priority level 5. Sortable.', 'Required': True}, {'Name': 'Phone', 'Type': 'string', 'Description': 'Phone of the user. Max length 100 characters.', 'Required': False}, {'Name': 'TermsAccepted', 'Type': 'date', 'Description': 'Terms accepted of the user.', 'Required': False}, {'Name': 'Active', 'Type': 'boolean', 'Description': 'Active of the user. Required.', 'Required': True}, {'Name': 'xp', 'Type': 'object', 'Description': 'Container for extended (custom) properties of the user.', 'Required': False}]}
 **Responsestatus**: `200`

 **Responsebody**: 
{'Sample': '{\r\n  "ID": "",\r\n  "Username": "",\r\n  "FirstName": "",\r\n  "LastName": "",\r\n  "Email": "",\r\n  "Phone": "",\r\n  "TermsAccepted": "2018-03-21T23:00:00+00:00",\r\n  "Active": false,\r\n  "xp": {},\r\n  "AvailableRoles": [\r\n    ""\r\n  ]\r\n}', 'Fields': [{'Name': 'ID', 'Type': 'string', 'Description': 'ID of the user.', 'Required': False}, {'Name': 'Username', 'Type': 'string', 'Description': 'Username of the user.', 'Required': True}, {'Name': 'FirstName', 'Type': 'string', 'Description': 'First name of the user.', 'Required': True}, {'Name': 'LastName', 'Type': 'string', 'Description': 'Last name of the user.', 'Required': True}, {'Name': 'Email', 'Type': 'string', 'Description': 'Email of the user.', 'Required': True}, {'Name': 'Phone', 'Type': 'string', 'Description': 'Phone of the user.', 'Required': False}, {'Name': 'TermsAccepted', 'Type': 'date', 'Description': 'Terms accepted of the user.', 'Required': False}, {'Name': 'Active', 'Type': 'boolean', 'Description': 'Active of the user.', 'Required': True}, {'Name': 'xp', 'Type': 'object', 'Description': 'Container for extended (custom) properties of the user.', 'Required': False}, {'Name': 'AvailableRoles', 'Type': 'array', 'Description': 'Available roles of the user.', 'Required': False}]}
## Delete a supplier user
### `DELETE` `v1/suppliers/{supplierID}/users/{userID}`

| Parameters      | Description                    |
|------------------|---------------------------------|
| Name            | supplierID                     |
| Type            | string                         |
| Description     | ID of the supplier.            |
| Required        | True                           |
| Name            | userID                         |
| Type            | string                         |
| Description     | ID of the user.                |
| Required        | True                           |

 **Requestbody**: 
None
 **Responsestatus**: `204`

 **Responsebody**: 
None
## Partially update a supplier user
### `PATCH` `v1/suppliers/{supplierID}/users/{userID}`

| Parameters      | Description                    |
|------------------|---------------------------------|
| Name            | supplierID                     |
| Type            | string                         |
| Description     | ID of the supplier.            |
| Required        | True                           |
| Name            | userID                         |
| Type            | string                         |
| Description     | ID of the user.                |
| Required        | True                           |

 **Requestbody**: 
{'Sample': '{\r\n  "ID": "",\r\n  "Username": "",\r\n  "Password": "",\r\n  "FirstName": "",\r\n  "LastName": "",\r\n  "Email": "",\r\n  "Phone": "",\r\n  "TermsAccepted": "2018-03-21T23:00:00+00:00",\r\n  "Active": false,\r\n  "xp": {}\r\n}', 'Fields': [{'Name': 'ID', 'Type': 'string', 'Description': 'ID of the user. Can only contain characters Aa-Zz, 0-9, -, and _. Searchable: priority level 1. Sortable.', 'Required': False}, {'Name': 'Username', 'Type': 'string', 'Description': 'Username of the user. Required. Max length 100 characters. Searchable: priority level 2. Sortable: priority level 3.', 'Required': True}, {'Name': 'Password', 'Type': 'string', 'Description': 'Password of the user.', 'Required': False}, {'Name': 'FirstName', 'Type': 'string', 'Description': 'First name of the user. Required. Max length 100 characters. Searchable: priority level 4. Sortable: priority level 2.', 'Required': True}, {'Name': 'LastName', 'Type': 'string', 'Description': 'Last name of the user. Required. Max length 100 characters. Searchable: priority level 3. Sortable: priority level 1.', 'Required': True}, {'Name': 'Email', 'Type': 'string', 'Description': 'Email of the user. Required. Max length 200 characters. Searchable: priority level 5. Sortable.', 'Required': True}, {'Name': 'Phone', 'Type': 'string', 'Description': 'Phone of the user. Max length 100 characters.', 'Required': False}, {'Name': 'TermsAccepted', 'Type': 'date', 'Description': 'Terms accepted of the user.', 'Required': False}, {'Name': 'Active', 'Type': 'boolean', 'Description': 'Active of the user. Required.', 'Required': True}, {'Name': 'xp', 'Type': 'object', 'Description': 'Container for extended (custom) properties of the user.', 'Required': False}]}
 **Responsestatus**: `200`

 **Responsebody**: 
{'Sample': '{\r\n  "ID": "",\r\n  "Username": "",\r\n  "FirstName": "",\r\n  "LastName": "",\r\n  "Email": "",\r\n  "Phone": "",\r\n  "TermsAccepted": "2018-03-21T23:00:00+00:00",\r\n  "Active": false,\r\n  "xp": {},\r\n  "AvailableRoles": [\r\n    ""\r\n  ]\r\n}', 'Fields': [{'Name': 'ID', 'Type': 'string', 'Description': 'ID of the user.', 'Required': False}, {'Name': 'Username', 'Type': 'string', 'Description': 'Username of the user.', 'Required': True}, {'Name': 'FirstName', 'Type': 'string', 'Description': 'First name of the user.', 'Required': True}, {'Name': 'LastName', 'Type': 'string', 'Description': 'Last name of the user.', 'Required': True}, {'Name': 'Email', 'Type': 'string', 'Description': 'Email of the user.', 'Required': True}, {'Name': 'Phone', 'Type': 'string', 'Description': 'Phone of the user.', 'Required': False}, {'Name': 'TermsAccepted', 'Type': 'date', 'Description': 'Terms accepted of the user.', 'Required': False}, {'Name': 'Active', 'Type': 'boolean', 'Description': 'Active of the user.', 'Required': True}, {'Name': 'xp', 'Type': 'object', 'Description': 'Container for extended (custom) properties of the user.', 'Required': False}, {'Name': 'AvailableRoles', 'Type': 'array', 'Description': 'Available roles of the user.', 'Required': False}]}
## Get a single supplier user access token
### `POST` `v1/suppliers/{supplierID}/users/{userID}/accesstoken`

| Parameters      | Description                    |
|------------------|---------------------------------|
| Name            | supplierID                     |
| Type            | string                         |
| Description     | ID of the supplier.            |
| Required        | True                           |
| Name            | userID                         |
| Type            | string                         |
| Description     | ID of the user.                |
| Required        | True                           |

 **Requestbody**: 
{'Sample': '{\r\n  "ClientID": "",\r\n  "Roles": [\r\n    "DevCenterImpersonate"\r\n  ]\r\n}', 'Fields': [{'Name': 'ClientID', 'Type': 'string', 'Description': 'ID of the client.', 'Required': False}, {'Name': 'Roles', 'Type': 'array', 'Description': 'Roles of the impersonate token request.', 'Required': False}]}
 **Responsestatus**: `200`

 **Responsebody**: 
{'Sample': '{\r\n  "access_token": "",\r\n  "expires_in": 0,\r\n  "token_type": "",\r\n  "refresh_token": ""\r\n}', 'Fields': [{'Name': 'access_token', 'Type': 'string', 'Description': 'Access token of the access token.', 'Required': False}, {'Name': 'expires_in', 'Type': 'integer', 'Description': 'Expires in of the access token.', 'Required': False}, {'Name': 'token_type', 'Type': 'string', 'Description': 'Token type of the access token.', 'Required': False}, {'Name': 'refresh_token', 'Type': 'string', 'Description': 'Refresh token of the access token.', 'Required': False}]}