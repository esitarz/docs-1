---
title: Addresses
date: 2018-03-23
category: API Reference
tags: Buyers
slug: Addresses
---
Addresses are used for the purposes of billing and shipping an order. An
address may belong to a list that can be shared among many users if
appropriate.

---

## Get a single address
### `GET` `v1/buyers/{buyerID}/addresses/{addressID}`

| Parameters      | Description                    |
|------------------|---------------------------------|
| Name            | buyerID                        |
| Type            | string                         |
| Description     | ID of the buyer.               |
| Required        | True                           |
| Name            | addressID                      |
| Type            | string                         |
| Description     | ID of the address.             |
| Required        | True                           |

 **Requestbody**: 
None
 **Responsestatus**: `200`

 **Responsebody**: 
{'Sample': '{\r\n  "ID": "",\r\n  "DateCreated": "2018-03-21T23:00:00+00:00",\r\n  "CompanyName": "",\r\n  "FirstName": "",\r\n  "LastName": "",\r\n  "Street1": "",\r\n  "Street2": "",\r\n  "City": "",\r\n  "State": "",\r\n  "Zip": "",\r\n  "Country": "",\r\n  "Phone": "",\r\n  "AddressName": "",\r\n  "xp": {}\r\n}', 'Fields': [{'Name': 'ID', 'Type': 'string', 'Description': 'ID of the address.', 'Required': False}, {'Name': 'DateCreated', 'Type': 'date', 'Description': 'Date created of the address.', 'Required': False}, {'Name': 'CompanyName', 'Type': 'string', 'Description': 'Company name of the address.', 'Required': False}, {'Name': 'FirstName', 'Type': 'string', 'Description': 'First name of the address.', 'Required': False}, {'Name': 'LastName', 'Type': 'string', 'Description': 'Last name of the address.', 'Required': False}, {'Name': 'Street1', 'Type': 'string', 'Description': 'Street 1 of the address.', 'Required': True}, {'Name': 'Street2', 'Type': 'string', 'Description': 'Street 2 of the address.', 'Required': False}, {'Name': 'City', 'Type': 'string', 'Description': 'City of the address.', 'Required': True}, {'Name': 'State', 'Type': 'string', 'Description': 'State of the address.', 'Required': True}, {'Name': 'Zip', 'Type': 'string', 'Description': 'Zip of the address.', 'Required': True}, {'Name': 'Country', 'Type': 'string', 'Description': 'Country of the address.', 'Required': True}, {'Name': 'Phone', 'Type': 'string', 'Description': 'Phone of the address.', 'Required': False}, {'Name': 'AddressName', 'Type': 'string', 'Description': 'Address name of the address.', 'Required': False}, {'Name': 'xp', 'Type': 'object', 'Description': 'Container for extended (custom) properties of the address.', 'Required': False}]}
## Get a list of addresses
### `GET` `v1/buyers/{buyerID}/addresses`

| Parameters      | Description                    |
|------------------|---------------------------------|
| Name            | buyerID                        |
| Type            | string                         |
| Description     | ID of the buyer.               |
| Required        | True                           |
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
{'Sample': '{\r\n  "Meta": {\r\n    "Page": 1,\r\n    "PageSize": 20,\r\n    "TotalCount": 25,\r\n    "TotalPages": 2,\r\n    "ItemRange": [\r\n      1,\r\n      20\r\n    ]\r\n  },\r\n  "Items": [\r\n    {\r\n      "ID": "",\r\n      "DateCreated": "2018-03-21T23:00:00+00:00",\r\n      "CompanyName": "",\r\n      "FirstName": "",\r\n      "LastName": "",\r\n      "Street1": "",\r\n      "Street2": "",\r\n      "City": "",\r\n      "State": "",\r\n      "Zip": "",\r\n      "Country": "",\r\n      "Phone": "",\r\n      "AddressName": "",\r\n      "xp": {}\r\n    }\r\n  ]\r\n}', 'Fields': [{'Name': 'ID', 'Type': 'string', 'Description': 'ID of the address.', 'Required': False}, {'Name': 'DateCreated', 'Type': 'date', 'Description': 'Date created of the address.', 'Required': False}, {'Name': 'CompanyName', 'Type': 'string', 'Description': 'Company name of the address.', 'Required': False}, {'Name': 'FirstName', 'Type': 'string', 'Description': 'First name of the address.', 'Required': False}, {'Name': 'LastName', 'Type': 'string', 'Description': 'Last name of the address.', 'Required': False}, {'Name': 'Street1', 'Type': 'string', 'Description': 'Street 1 of the address.', 'Required': True}, {'Name': 'Street2', 'Type': 'string', 'Description': 'Street 2 of the address.', 'Required': False}, {'Name': 'City', 'Type': 'string', 'Description': 'City of the address.', 'Required': True}, {'Name': 'State', 'Type': 'string', 'Description': 'State of the address.', 'Required': True}, {'Name': 'Zip', 'Type': 'string', 'Description': 'Zip of the address.', 'Required': True}, {'Name': 'Country', 'Type': 'string', 'Description': 'Country of the address.', 'Required': True}, {'Name': 'Phone', 'Type': 'string', 'Description': 'Phone of the address.', 'Required': False}, {'Name': 'AddressName', 'Type': 'string', 'Description': 'Address name of the address.', 'Required': False}, {'Name': 'xp', 'Type': 'object', 'Description': 'Container for extended (custom) properties of the address.', 'Required': False}]}
## Create a new address
### `POST` `v1/buyers/{buyerID}/addresses`

| Parameters      | Description                    |
|------------------|---------------------------------|
| Name            | buyerID                        |
| Type            | string                         |
| Description     | ID of the buyer.               |
| Required        | True                           |

 **Requestbody**: 
{'Sample': '{\r\n  "ID": "",\r\n  "CompanyName": "",\r\n  "FirstName": "",\r\n  "LastName": "",\r\n  "Street1": "",\r\n  "Street2": "",\r\n  "City": "",\r\n  "State": "",\r\n  "Zip": "",\r\n  "Country": "",\r\n  "Phone": "",\r\n  "AddressName": "",\r\n  "xp": {}\r\n}', 'Fields': [{'Name': 'ID', 'Type': 'string', 'Description': 'ID of the address. Can only contain characters Aa-Zz, 0-9, -, and _. Searchable: priority level 1. Sortable: priority level 2.', 'Required': False}, {'Name': 'CompanyName', 'Type': 'string', 'Description': 'Company name of the address. Max length 100 characters. Sortable.', 'Required': False}, {'Name': 'FirstName', 'Type': 'string', 'Description': 'First name of the address. Max length 100 characters. Searchable: priority level 7. Sortable.', 'Required': False}, {'Name': 'LastName', 'Type': 'string', 'Description': 'Last name of the address. Max length 100 characters. Searchable: priority level 6. Sortable.', 'Required': False}, {'Name': 'Street1', 'Type': 'string', 'Description': 'Street 1 of the address. Required. Max length 100 characters. Searchable: priority level 4. Sortable.', 'Required': True}, {'Name': 'Street2', 'Type': 'string', 'Description': 'Street 2 of the address. Max length 100 characters. Searchable: priority level 5. Sortable.', 'Required': False}, {'Name': 'City', 'Type': 'string', 'Description': 'City of the address. Required. Max length 100 characters. Searchable: priority level 3. Sortable.', 'Required': True}, {'Name': 'State', 'Type': 'string', 'Description': 'State of the address. Required. Max length 100 characters. Searchable: priority level 7. Sortable.', 'Required': True}, {'Name': 'Zip', 'Type': 'string', 'Description': 'Zip of the address. Required. Max length 100 characters. Searchable: priority level 6. Sortable.', 'Required': True}, {'Name': 'Country', 'Type': 'string', 'Description': 'Country of the address. Required. Max length 2 characters. Sortable.', 'Required': True}, {'Name': 'Phone', 'Type': 'string', 'Description': 'Phone of the address. Max length 100 characters. Sortable.', 'Required': False}, {'Name': 'AddressName', 'Type': 'string', 'Description': 'Address name of the address. Max length 100 characters. Searchable: priority level 2. Sortable: priority level 1.', 'Required': False}, {'Name': 'xp', 'Type': 'object', 'Description': 'Container for extended (custom) properties of the address.', 'Required': False}]}
 **Responsestatus**: `201`

 **Responsebody**: 
{'Sample': '{\r\n  "ID": "",\r\n  "DateCreated": "2018-03-21T23:00:00+00:00",\r\n  "CompanyName": "",\r\n  "FirstName": "",\r\n  "LastName": "",\r\n  "Street1": "",\r\n  "Street2": "",\r\n  "City": "",\r\n  "State": "",\r\n  "Zip": "",\r\n  "Country": "",\r\n  "Phone": "",\r\n  "AddressName": "",\r\n  "xp": {}\r\n}', 'Fields': [{'Name': 'ID', 'Type': 'string', 'Description': 'ID of the address.', 'Required': False}, {'Name': 'DateCreated', 'Type': 'date', 'Description': 'Date created of the address.', 'Required': False}, {'Name': 'CompanyName', 'Type': 'string', 'Description': 'Company name of the address.', 'Required': False}, {'Name': 'FirstName', 'Type': 'string', 'Description': 'First name of the address.', 'Required': False}, {'Name': 'LastName', 'Type': 'string', 'Description': 'Last name of the address.', 'Required': False}, {'Name': 'Street1', 'Type': 'string', 'Description': 'Street 1 of the address.', 'Required': True}, {'Name': 'Street2', 'Type': 'string', 'Description': 'Street 2 of the address.', 'Required': False}, {'Name': 'City', 'Type': 'string', 'Description': 'City of the address.', 'Required': True}, {'Name': 'State', 'Type': 'string', 'Description': 'State of the address.', 'Required': True}, {'Name': 'Zip', 'Type': 'string', 'Description': 'Zip of the address.', 'Required': True}, {'Name': 'Country', 'Type': 'string', 'Description': 'Country of the address.', 'Required': True}, {'Name': 'Phone', 'Type': 'string', 'Description': 'Phone of the address.', 'Required': False}, {'Name': 'AddressName', 'Type': 'string', 'Description': 'Address name of the address.', 'Required': False}, {'Name': 'xp', 'Type': 'object', 'Description': 'Container for extended (custom) properties of the address.', 'Required': False}]}
## Create or update an address
### `PUT` `v1/buyers/{buyerID}/addresses/{addressID}`

| Parameters      | Description                    |
|------------------|---------------------------------|
| Name            | buyerID                        |
| Type            | string                         |
| Description     | ID of the buyer.               |
| Required        | True                           |
| Name            | addressID                      |
| Type            | string                         |
| Description     | ID of the address.             |
| Required        | True                           |

 **Requestbody**: 
{'Sample': '{\r\n  "ID": "",\r\n  "CompanyName": "",\r\n  "FirstName": "",\r\n  "LastName": "",\r\n  "Street1": "",\r\n  "Street2": "",\r\n  "City": "",\r\n  "State": "",\r\n  "Zip": "",\r\n  "Country": "",\r\n  "Phone": "",\r\n  "AddressName": "",\r\n  "xp": {}\r\n}', 'Fields': [{'Name': 'ID', 'Type': 'string', 'Description': 'ID of the address. Can only contain characters Aa-Zz, 0-9, -, and _. Searchable: priority level 1. Sortable: priority level 2.', 'Required': False}, {'Name': 'CompanyName', 'Type': 'string', 'Description': 'Company name of the address. Max length 100 characters. Sortable.', 'Required': False}, {'Name': 'FirstName', 'Type': 'string', 'Description': 'First name of the address. Max length 100 characters. Searchable: priority level 7. Sortable.', 'Required': False}, {'Name': 'LastName', 'Type': 'string', 'Description': 'Last name of the address. Max length 100 characters. Searchable: priority level 6. Sortable.', 'Required': False}, {'Name': 'Street1', 'Type': 'string', 'Description': 'Street 1 of the address. Required. Max length 100 characters. Searchable: priority level 4. Sortable.', 'Required': True}, {'Name': 'Street2', 'Type': 'string', 'Description': 'Street 2 of the address. Max length 100 characters. Searchable: priority level 5. Sortable.', 'Required': False}, {'Name': 'City', 'Type': 'string', 'Description': 'City of the address. Required. Max length 100 characters. Searchable: priority level 3. Sortable.', 'Required': True}, {'Name': 'State', 'Type': 'string', 'Description': 'State of the address. Required. Max length 100 characters. Searchable: priority level 7. Sortable.', 'Required': True}, {'Name': 'Zip', 'Type': 'string', 'Description': 'Zip of the address. Required. Max length 100 characters. Searchable: priority level 6. Sortable.', 'Required': True}, {'Name': 'Country', 'Type': 'string', 'Description': 'Country of the address. Required. Max length 2 characters. Sortable.', 'Required': True}, {'Name': 'Phone', 'Type': 'string', 'Description': 'Phone of the address. Max length 100 characters. Sortable.', 'Required': False}, {'Name': 'AddressName', 'Type': 'string', 'Description': 'Address name of the address. Max length 100 characters. Searchable: priority level 2. Sortable: priority level 1.', 'Required': False}, {'Name': 'xp', 'Type': 'object', 'Description': 'Container for extended (custom) properties of the address.', 'Required': False}]}
 **Responsestatus**: `200`

 **Responsebody**: 
{'Sample': '{\r\n  "ID": "",\r\n  "DateCreated": "2018-03-21T23:00:00+00:00",\r\n  "CompanyName": "",\r\n  "FirstName": "",\r\n  "LastName": "",\r\n  "Street1": "",\r\n  "Street2": "",\r\n  "City": "",\r\n  "State": "",\r\n  "Zip": "",\r\n  "Country": "",\r\n  "Phone": "",\r\n  "AddressName": "",\r\n  "xp": {}\r\n}', 'Fields': [{'Name': 'ID', 'Type': 'string', 'Description': 'ID of the address.', 'Required': False}, {'Name': 'DateCreated', 'Type': 'date', 'Description': 'Date created of the address.', 'Required': False}, {'Name': 'CompanyName', 'Type': 'string', 'Description': 'Company name of the address.', 'Required': False}, {'Name': 'FirstName', 'Type': 'string', 'Description': 'First name of the address.', 'Required': False}, {'Name': 'LastName', 'Type': 'string', 'Description': 'Last name of the address.', 'Required': False}, {'Name': 'Street1', 'Type': 'string', 'Description': 'Street 1 of the address.', 'Required': True}, {'Name': 'Street2', 'Type': 'string', 'Description': 'Street 2 of the address.', 'Required': False}, {'Name': 'City', 'Type': 'string', 'Description': 'City of the address.', 'Required': True}, {'Name': 'State', 'Type': 'string', 'Description': 'State of the address.', 'Required': True}, {'Name': 'Zip', 'Type': 'string', 'Description': 'Zip of the address.', 'Required': True}, {'Name': 'Country', 'Type': 'string', 'Description': 'Country of the address.', 'Required': True}, {'Name': 'Phone', 'Type': 'string', 'Description': 'Phone of the address.', 'Required': False}, {'Name': 'AddressName', 'Type': 'string', 'Description': 'Address name of the address.', 'Required': False}, {'Name': 'xp', 'Type': 'object', 'Description': 'Container for extended (custom) properties of the address.', 'Required': False}]}
## Delete an address
### `DELETE` `v1/buyers/{buyerID}/addresses/{addressID}`

| Parameters      | Description                    |
|------------------|---------------------------------|
| Name            | buyerID                        |
| Type            | string                         |
| Description     | ID of the buyer.               |
| Required        | True                           |
| Name            | addressID                      |
| Type            | string                         |
| Description     | ID of the address.             |
| Required        | True                           |

 **Requestbody**: 
None
 **Responsestatus**: `204`

 **Responsebody**: 
None
## Partially update an address
### `PATCH` `v1/buyers/{buyerID}/addresses/{addressID}`

| Parameters      | Description                    |
|------------------|---------------------------------|
| Name            | buyerID                        |
| Type            | string                         |
| Description     | ID of the buyer.               |
| Required        | True                           |
| Name            | addressID                      |
| Type            | string                         |
| Description     | ID of the address.             |
| Required        | True                           |

 **Requestbody**: 
{'Sample': '{\r\n  "ID": "",\r\n  "CompanyName": "",\r\n  "FirstName": "",\r\n  "LastName": "",\r\n  "Street1": "",\r\n  "Street2": "",\r\n  "City": "",\r\n  "State": "",\r\n  "Zip": "",\r\n  "Country": "",\r\n  "Phone": "",\r\n  "AddressName": "",\r\n  "xp": {}\r\n}', 'Fields': [{'Name': 'ID', 'Type': 'string', 'Description': 'ID of the address. Can only contain characters Aa-Zz, 0-9, -, and _. Searchable: priority level 1. Sortable: priority level 2.', 'Required': False}, {'Name': 'CompanyName', 'Type': 'string', 'Description': 'Company name of the address. Max length 100 characters. Sortable.', 'Required': False}, {'Name': 'FirstName', 'Type': 'string', 'Description': 'First name of the address. Max length 100 characters. Searchable: priority level 7. Sortable.', 'Required': False}, {'Name': 'LastName', 'Type': 'string', 'Description': 'Last name of the address. Max length 100 characters. Searchable: priority level 6. Sortable.', 'Required': False}, {'Name': 'Street1', 'Type': 'string', 'Description': 'Street 1 of the address. Required. Max length 100 characters. Searchable: priority level 4. Sortable.', 'Required': True}, {'Name': 'Street2', 'Type': 'string', 'Description': 'Street 2 of the address. Max length 100 characters. Searchable: priority level 5. Sortable.', 'Required': False}, {'Name': 'City', 'Type': 'string', 'Description': 'City of the address. Required. Max length 100 characters. Searchable: priority level 3. Sortable.', 'Required': True}, {'Name': 'State', 'Type': 'string', 'Description': 'State of the address. Required. Max length 100 characters. Searchable: priority level 7. Sortable.', 'Required': True}, {'Name': 'Zip', 'Type': 'string', 'Description': 'Zip of the address. Required. Max length 100 characters. Searchable: priority level 6. Sortable.', 'Required': True}, {'Name': 'Country', 'Type': 'string', 'Description': 'Country of the address. Required. Max length 2 characters. Sortable.', 'Required': True}, {'Name': 'Phone', 'Type': 'string', 'Description': 'Phone of the address. Max length 100 characters. Sortable.', 'Required': False}, {'Name': 'AddressName', 'Type': 'string', 'Description': 'Address name of the address. Max length 100 characters. Searchable: priority level 2. Sortable: priority level 1.', 'Required': False}, {'Name': 'xp', 'Type': 'object', 'Description': 'Container for extended (custom) properties of the address.', 'Required': False}]}
 **Responsestatus**: `200`

 **Responsebody**: 
{'Sample': '{\r\n  "ID": "",\r\n  "DateCreated": "2018-03-21T23:00:00+00:00",\r\n  "CompanyName": "",\r\n  "FirstName": "",\r\n  "LastName": "",\r\n  "Street1": "",\r\n  "Street2": "",\r\n  "City": "",\r\n  "State": "",\r\n  "Zip": "",\r\n  "Country": "",\r\n  "Phone": "",\r\n  "AddressName": "",\r\n  "xp": {}\r\n}', 'Fields': [{'Name': 'ID', 'Type': 'string', 'Description': 'ID of the address.', 'Required': False}, {'Name': 'DateCreated', 'Type': 'date', 'Description': 'Date created of the address.', 'Required': False}, {'Name': 'CompanyName', 'Type': 'string', 'Description': 'Company name of the address.', 'Required': False}, {'Name': 'FirstName', 'Type': 'string', 'Description': 'First name of the address.', 'Required': False}, {'Name': 'LastName', 'Type': 'string', 'Description': 'Last name of the address.', 'Required': False}, {'Name': 'Street1', 'Type': 'string', 'Description': 'Street 1 of the address.', 'Required': True}, {'Name': 'Street2', 'Type': 'string', 'Description': 'Street 2 of the address.', 'Required': False}, {'Name': 'City', 'Type': 'string', 'Description': 'City of the address.', 'Required': True}, {'Name': 'State', 'Type': 'string', 'Description': 'State of the address.', 'Required': True}, {'Name': 'Zip', 'Type': 'string', 'Description': 'Zip of the address.', 'Required': True}, {'Name': 'Country', 'Type': 'string', 'Description': 'Country of the address.', 'Required': True}, {'Name': 'Phone', 'Type': 'string', 'Description': 'Phone of the address.', 'Required': False}, {'Name': 'AddressName', 'Type': 'string', 'Description': 'Address name of the address.', 'Required': False}, {'Name': 'xp', 'Type': 'object', 'Description': 'Container for extended (custom) properties of the address.', 'Required': False}]}
## Get a list of address assignments
### `GET` `v1/buyers/{buyerID}/addresses/assignments`

| Parameters      | Description                    |
|------------------|---------------------------------|
| Name            | buyerID                        |
| Type            | string                         |
| Description     | ID of the buyer.               |
| Required        | True                           |
| Name            | addressID                      |
| Type            | string                         |
| Description     | ID of the address.             |
| Required        | False                          |
| Name            | userID                         |
| Type            | string                         |
| Description     | ID of the user.                |
| Required        | False                          |
| Name            | userGroupID                    |
| Type            | string                         |
| Description     | ID of the user group.          |
| Required        | False                          |
| Name            | level                          |
| Type            | string                         |
| Description     | Level of the address assignment. Possible values: User, Group, Company. |
| Required        | False                          |
| Name            | isShipping                     |
| Type            | boolean                        |
| Description     | Is shipping of the address assignment. |
| Required        | False                          |
| Name            | isBilling                      |
| Type            | boolean                        |
| Description     | Is billing of the address assignment. |
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
{'Sample': '{\r\n  "Meta": {\r\n    "Page": 1,\r\n    "PageSize": 20,\r\n    "TotalCount": 25,\r\n    "TotalPages": 2,\r\n    "ItemRange": [\r\n      1,\r\n      20\r\n    ]\r\n  },\r\n  "Items": [\r\n    {\r\n      "AddressID": "",\r\n      "UserID": "",\r\n      "UserGroupID": "",\r\n      "IsShipping": false,\r\n      "IsBilling": false\r\n    }\r\n  ]\r\n}', 'Fields': [{'Name': 'AddressID', 'Type': 'string', 'Description': 'ID of the address.', 'Required': True}, {'Name': 'UserID', 'Type': 'string', 'Description': 'ID of the user.', 'Required': False}, {'Name': 'UserGroupID', 'Type': 'string', 'Description': 'ID of the user group.', 'Required': False}, {'Name': 'IsShipping', 'Type': 'boolean', 'Description': 'Is shipping of the address assignment.', 'Required': False}, {'Name': 'IsBilling', 'Type': 'boolean', 'Description': 'Is billing of the address assignment.', 'Required': False}]}
## Delete an address assignment
### `DELETE` `v1/buyers/{buyerID}/addresses/{addressID}/assignments`

| Parameters      | Description                    |
|------------------|---------------------------------|
| Name            | buyerID                        |
| Type            | string                         |
| Description     | ID of the buyer.               |
| Required        | True                           |
| Name            | addressID                      |
| Type            | string                         |
| Description     | ID of the address.             |
| Required        | True                           |
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
## Save an address assignment
### `POST` `v1/buyers/{buyerID}/addresses/assignments`

| Parameters      | Description                    |
|------------------|---------------------------------|
| Name            | buyerID                        |
| Type            | string                         |
| Description     | ID of the buyer.               |
| Required        | True                           |

 **Requestbody**: 
{'Sample': '{\r\n  "AddressID": "",\r\n  "UserID": "",\r\n  "UserGroupID": "",\r\n  "IsShipping": false,\r\n  "IsBilling": false\r\n}', 'Fields': [{'Name': 'AddressID', 'Type': 'string', 'Description': 'ID of the address. Required. Sortable: priority level 1.', 'Required': True}, {'Name': 'UserID', 'Type': 'string', 'Description': 'ID of the user. Sortable: priority level 2.', 'Required': False}, {'Name': 'UserGroupID', 'Type': 'string', 'Description': 'ID of the user group. Sortable: priority level 3.', 'Required': False}, {'Name': 'IsShipping', 'Type': 'boolean', 'Description': 'Is shipping of the address assignment.', 'Required': False}, {'Name': 'IsBilling', 'Type': 'boolean', 'Description': 'Is billing of the address assignment.', 'Required': False}]}
 **Responsestatus**: `204`

 **Responsebody**: 
None