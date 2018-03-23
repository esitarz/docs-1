---
title: Me
date: 2018-03-23
category: API Reference
tags: Me And My Stuff
slug: Me
---
"Me" is a container for read-only endpoints that return a filtered view
of things that the current buyer user is allowed to see, i.e. things
that they are assigned to either directly or as a member of a buyer
organization or user group. It also provides ways for a user to update
or change their own information.

---
## Get the Current Authenticated User
### `GET` `v1/me`

| Parameters      | Description                    |
|------------------|---------------------------------|

 **Requestbody**: 
None
 **Responsestatus**: `200`

 **Responsebody**: 
{'Sample': '{\r\n  "Buyer": {\r\n    "ID": "",\r\n    "DefaultCatalogID": ""\r\n  },\r\n  "ID": "",\r\n  "Username": "",\r\n  "FirstName": "",\r\n  "LastName": "",\r\n  "Email": "",\r\n  "Phone": "",\r\n  "TermsAccepted": "2018-03-21T23:00:00+00:00",\r\n  "Active": false,\r\n  "xp": {},\r\n  "AvailableRoles": [\r\n    ""\r\n  ]\r\n}', 'Fields': [{'Name': 'Buyer', 'Type': 'object', 'Description': 'Buyer of the user.', 'Required': False}, {'Name': 'ID', 'Type': 'string', 'Description': 'ID of the user.', 'Required': False}, {'Name': 'Username', 'Type': 'string', 'Description': 'Username of the user.', 'Required': True}, {'Name': 'FirstName', 'Type': 'string', 'Description': 'First name of the user.', 'Required': True}, {'Name': 'LastName', 'Type': 'string', 'Description': 'Last name of the user.', 'Required': True}, {'Name': 'Email', 'Type': 'string', 'Description': 'Email of the user.', 'Required': True}, {'Name': 'Phone', 'Type': 'string', 'Description': 'Phone of the user.', 'Required': False}, {'Name': 'TermsAccepted', 'Type': 'date', 'Description': 'Terms accepted of the user.', 'Required': False}, {'Name': 'Active', 'Type': 'boolean', 'Description': 'Active of the user.', 'Required': True}, {'Name': 'xp', 'Type': 'object', 'Description': 'Container for extended (custom) properties of the user.', 'Required': False}, {'Name': 'AvailableRoles', 'Type': 'array', 'Description': 'Available roles of the user.', 'Required': False}]}## Update the Currently Authenticated User
### `PUT` `v1/me`

| Parameters      | Description                    |
|------------------|---------------------------------|

 **Requestbody**: 
{'Sample': '{\r\n  "ID": "",\r\n  "Username": "",\r\n  "Password": "",\r\n  "FirstName": "",\r\n  "LastName": "",\r\n  "Email": "",\r\n  "Phone": "",\r\n  "TermsAccepted": "2018-03-21T23:00:00+00:00",\r\n  "Active": false,\r\n  "xp": {}\r\n}', 'Fields': [{'Name': 'ID', 'Type': 'string', 'Description': 'ID of the user. Can only contain characters Aa-Zz, 0-9, -, and _. Searchable: priority level 1. Sortable.', 'Required': False}, {'Name': 'Username', 'Type': 'string', 'Description': 'Username of the user. Required. Max length 100 characters. Searchable: priority level 2. Sortable: priority level 3.', 'Required': True}, {'Name': 'Password', 'Type': 'string', 'Description': 'Password of the user.', 'Required': False}, {'Name': 'FirstName', 'Type': 'string', 'Description': 'First name of the user. Required. Max length 100 characters. Searchable: priority level 4. Sortable: priority level 2.', 'Required': True}, {'Name': 'LastName', 'Type': 'string', 'Description': 'Last name of the user. Required. Max length 100 characters. Searchable: priority level 3. Sortable: priority level 1.', 'Required': True}, {'Name': 'Email', 'Type': 'string', 'Description': 'Email of the user. Required. Max length 200 characters. Searchable: priority level 5. Sortable.', 'Required': True}, {'Name': 'Phone', 'Type': 'string', 'Description': 'Phone of the user. Max length 100 characters.', 'Required': False}, {'Name': 'TermsAccepted', 'Type': 'date', 'Description': 'Terms accepted of the user.', 'Required': False}, {'Name': 'Active', 'Type': 'boolean', 'Description': 'Active of the user. Required.', 'Required': True}, {'Name': 'xp', 'Type': 'object', 'Description': 'Container for extended (custom) properties of the user.', 'Required': False}]}
 **Responsestatus**: `200`

 **Responsebody**: 
{'Sample': '{\r\n  "Buyer": {\r\n    "ID": "",\r\n    "DefaultCatalogID": ""\r\n  },\r\n  "ID": "",\r\n  "Username": "",\r\n  "FirstName": "",\r\n  "LastName": "",\r\n  "Email": "",\r\n  "Phone": "",\r\n  "TermsAccepted": "2018-03-21T23:00:00+00:00",\r\n  "Active": false,\r\n  "xp": {},\r\n  "AvailableRoles": [\r\n    ""\r\n  ]\r\n}', 'Fields': [{'Name': 'Buyer', 'Type': 'object', 'Description': 'Buyer of the user.', 'Required': False}, {'Name': 'ID', 'Type': 'string', 'Description': 'ID of the user.', 'Required': False}, {'Name': 'Username', 'Type': 'string', 'Description': 'Username of the user.', 'Required': True}, {'Name': 'FirstName', 'Type': 'string', 'Description': 'First name of the user.', 'Required': True}, {'Name': 'LastName', 'Type': 'string', 'Description': 'Last name of the user.', 'Required': True}, {'Name': 'Email', 'Type': 'string', 'Description': 'Email of the user.', 'Required': True}, {'Name': 'Phone', 'Type': 'string', 'Description': 'Phone of the user.', 'Required': False}, {'Name': 'TermsAccepted', 'Type': 'date', 'Description': 'Terms accepted of the user.', 'Required': False}, {'Name': 'Active', 'Type': 'boolean', 'Description': 'Active of the user.', 'Required': True}, {'Name': 'xp', 'Type': 'object', 'Description': 'Container for extended (custom) properties of the user.', 'Required': False}, {'Name': 'AvailableRoles', 'Type': 'array', 'Description': 'Available roles of the user.', 'Required': False}]}## Patch the Currently Authenticated User
### `PATCH` `v1/me`

| Parameters      | Description                    |
|------------------|---------------------------------|

 **Requestbody**: 
{'Sample': '{\r\n  "ID": "",\r\n  "Username": "",\r\n  "Password": "",\r\n  "FirstName": "",\r\n  "LastName": "",\r\n  "Email": "",\r\n  "Phone": "",\r\n  "TermsAccepted": "2018-03-21T23:00:00+00:00",\r\n  "Active": false,\r\n  "xp": {}\r\n}', 'Fields': [{'Name': 'ID', 'Type': 'string', 'Description': 'ID of the user. Can only contain characters Aa-Zz, 0-9, -, and _. Searchable: priority level 1. Sortable.', 'Required': False}, {'Name': 'Username', 'Type': 'string', 'Description': 'Username of the user. Required. Max length 100 characters. Searchable: priority level 2. Sortable: priority level 3.', 'Required': True}, {'Name': 'Password', 'Type': 'string', 'Description': 'Password of the user.', 'Required': False}, {'Name': 'FirstName', 'Type': 'string', 'Description': 'First name of the user. Required. Max length 100 characters. Searchable: priority level 4. Sortable: priority level 2.', 'Required': True}, {'Name': 'LastName', 'Type': 'string', 'Description': 'Last name of the user. Required. Max length 100 characters. Searchable: priority level 3. Sortable: priority level 1.', 'Required': True}, {'Name': 'Email', 'Type': 'string', 'Description': 'Email of the user. Required. Max length 200 characters. Searchable: priority level 5. Sortable.', 'Required': True}, {'Name': 'Phone', 'Type': 'string', 'Description': 'Phone of the user. Max length 100 characters.', 'Required': False}, {'Name': 'TermsAccepted', 'Type': 'date', 'Description': 'Terms accepted of the user.', 'Required': False}, {'Name': 'Active', 'Type': 'boolean', 'Description': 'Active of the user. Required.', 'Required': True}, {'Name': 'xp', 'Type': 'object', 'Description': 'Container for extended (custom) properties of the user.', 'Required': False}]}
 **Responsestatus**: `200`

 **Responsebody**: 
{'Sample': '{\r\n  "Buyer": {\r\n    "ID": "",\r\n    "DefaultCatalogID": ""\r\n  },\r\n  "ID": "",\r\n  "Username": "",\r\n  "FirstName": "",\r\n  "LastName": "",\r\n  "Email": "",\r\n  "Phone": "",\r\n  "TermsAccepted": "2018-03-21T23:00:00+00:00",\r\n  "Active": false,\r\n  "xp": {},\r\n  "AvailableRoles": [\r\n    ""\r\n  ]\r\n}', 'Fields': [{'Name': 'Buyer', 'Type': 'object', 'Description': 'Buyer of the user.', 'Required': False}, {'Name': 'ID', 'Type': 'string', 'Description': 'ID of the user.', 'Required': False}, {'Name': 'Username', 'Type': 'string', 'Description': 'Username of the user.', 'Required': True}, {'Name': 'FirstName', 'Type': 'string', 'Description': 'First name of the user.', 'Required': True}, {'Name': 'LastName', 'Type': 'string', 'Description': 'Last name of the user.', 'Required': True}, {'Name': 'Email', 'Type': 'string', 'Description': 'Email of the user.', 'Required': True}, {'Name': 'Phone', 'Type': 'string', 'Description': 'Phone of the user.', 'Required': False}, {'Name': 'TermsAccepted', 'Type': 'date', 'Description': 'Terms accepted of the user.', 'Required': False}, {'Name': 'Active', 'Type': 'boolean', 'Description': 'Active of the user.', 'Required': True}, {'Name': 'xp', 'Type': 'object', 'Description': 'Container for extended (custom) properties of the user.', 'Required': False}, {'Name': 'AvailableRoles', 'Type': 'array', 'Description': 'Available roles of the user.', 'Required': False}]}## Register a register
### `PUT` `v1/me/register`

| Parameters      | Description                    |
|------------------|---------------------------------|
| Name            | anonUserToken                  |
| Type            | string                         |
| Description     | Anon user token of the user.   |
| Required        | True                           |

 **Requestbody**: 
{'Sample': '{\r\n  "ID": "",\r\n  "Username": "",\r\n  "Password": "",\r\n  "FirstName": "",\r\n  "LastName": "",\r\n  "Email": "",\r\n  "Phone": "",\r\n  "TermsAccepted": "2018-03-21T23:00:00+00:00",\r\n  "Active": false,\r\n  "xp": {}\r\n}', 'Fields': [{'Name': 'ID', 'Type': 'string', 'Description': 'ID of the user. Can only contain characters Aa-Zz, 0-9, -, and _. Searchable: priority level 1. Sortable.', 'Required': False}, {'Name': 'Username', 'Type': 'string', 'Description': 'Username of the user. Required. Max length 100 characters. Searchable: priority level 2. Sortable: priority level 3.', 'Required': True}, {'Name': 'Password', 'Type': 'string', 'Description': 'Password of the user.', 'Required': False}, {'Name': 'FirstName', 'Type': 'string', 'Description': 'First name of the user. Required. Max length 100 characters. Searchable: priority level 4. Sortable: priority level 2.', 'Required': True}, {'Name': 'LastName', 'Type': 'string', 'Description': 'Last name of the user. Required. Max length 100 characters. Searchable: priority level 3. Sortable: priority level 1.', 'Required': True}, {'Name': 'Email', 'Type': 'string', 'Description': 'Email of the user. Required. Max length 200 characters. Searchable: priority level 5. Sortable.', 'Required': True}, {'Name': 'Phone', 'Type': 'string', 'Description': 'Phone of the user. Max length 100 characters.', 'Required': False}, {'Name': 'TermsAccepted', 'Type': 'date', 'Description': 'Terms accepted of the user.', 'Required': False}, {'Name': 'Active', 'Type': 'boolean', 'Description': 'Active of the user. Required.', 'Required': True}, {'Name': 'xp', 'Type': 'object', 'Description': 'Container for extended (custom) properties of the user.', 'Required': False}]}
 **Responsestatus**: `200`

 **Responsebody**: 
{'Sample': '{}', 'Fields': []}## Transfer a anon user order
### `PUT` `v1/me/orders`

| Parameters      | Description                    |
|------------------|---------------------------------|
| Name            | anonUserToken                  |
| Type            | string                         |
| Description     | Anon user token of the me.     |
| Required        | True                           |

 **Requestbody**: 
None
 **Responsestatus**: `204`

 **Responsebody**: 
None## Reset a password by token
### `POST` `v1/me/password`

| Parameters      | Description                    |
|------------------|---------------------------------|

 **Requestbody**: 
{'Sample': '{\r\n  "NewPassword": ""\r\n}', 'Fields': [{'Name': 'NewPassword', 'Type': 'string', 'Description': 'New password of the token password reset. Required.', 'Required': True}]}
 **Responsestatus**: `204`

 **Responsebody**: 
None