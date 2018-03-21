---
title: Addresses
date: 2018-03-19 18:56:07
category: content\api-reference
tags: MeAndMyStuff
slug: MeAddresses
---
[{'ID': 'ListAddresses', 'Name': 'Get a list of addresses visible to this user', 'Comments': ['Only available to Buyer Users.'], 'HttpVerb': 'GET', 'UriTemplate': 'v1/me/addresses', 'Parameters': [{'Name': 'search', 'Type': 'string', 'Description': 'Word or phrase to search for.', 'Required': False}, {'Name': 'searchOn', 'Type': 'string', 'Description': 'Comma-delimited list of fields to search on.', 'Required': False}, {'Name': 'sortBy', 'Type': 'string', 'Description': 'Comma-delimited list of fields to sort by.', 'Required': False}, {'Name': 'page', 'Type': 'integer', 'Description': 'Page of results to return. Default: 1', 'Required': False}, {'Name': 'pageSize', 'Type': 'integer', 'Description': 'Number of results to return per page. Default: 20, max: 100.', 'Required': False}, {'Name': 'filters', 'Type': 'object', 'Description': "Any additional key/value pairs passed in the query string are interpretted as filters. Valid keys are top-level properties of the returned model or 'xp.???'", 'Required': False}], 'RequestBody': None, 'ResponseStatus': 200, 'ResponseBody': {'Sample': '{\r\n  "Meta": {\r\n    "Page": 1,\r\n    "PageSize": 20,\r\n    "TotalCount": 25,\r\n    "TotalPages": 2,\r\n    "ItemRange": [\r\n      1,\r\n      20\r\n    ]\r\n  },\r\n  "Items": [\r\n    {\r\n      "ID": "",\r\n      "Shipping": false,\r\n      "Billing": false,\r\n      "Editable": false,\r\n      "CompanyName": "",\r\n      "FirstName": "",\r\n      "LastName": "",\r\n      "Street1": "",\r\n      "Street2": "",\r\n      "City": "",\r\n      "State": "",\r\n      "Zip": "",\r\n      "Country": "",\r\n      "Phone": "",\r\n      "AddressName": "",\r\n      "xp": {}\r\n    }\r\n  ]\r\n}', 'Fields': [{'Name': 'ID', 'Type': 'string', 'Description': 'ID of the address.', 'Required': False}, {'Name': 'Shipping', 'Type': 'boolean', 'Description': 'Shipping of the address.', 'Required': False}, {'Name': 'Billing', 'Type': 'boolean', 'Description': 'Billing of the address.', 'Required': False}, {'Name': 'Editable', 'Type': 'boolean', 'Description': 'Editable of the address.', 'Required': False}, {'Name': 'CompanyName', 'Type': 'string', 'Description': 'Company name of the address.', 'Required': False}, {'Name': 'FirstName', 'Type': 'string', 'Description': 'First name of the address.', 'Required': False}, {'Name': 'LastName', 'Type': 'string', 'Description': 'Last name of the address.', 'Required': False}, {'Name': 'Street1', 'Type': 'string', 'Description': 'Street 1 of the address.', 'Required': True}, {'Name': 'Street2', 'Type': 'string', 'Description': 'Street 2 of the address.', 'Required': False}, {'Name': 'City', 'Type': 'string', 'Description': 'City of the address.', 'Required': True}, {'Name': 'State', 'Type': 'string', 'Description': 'State of the address.', 'Required': True}, {'Name': 'Zip', 'Type': 'string', 'Description': 'Zip of the address.', 'Required': True}, {'Name': 'Country', 'Type': 'string', 'Description': 'Country of the address.', 'Required': True}, {'Name': 'Phone', 'Type': 'string', 'Description': 'Phone of the address.', 'Required': False}, {'Name': 'AddressName', 'Type': 'string', 'Description': 'Address name of the address.', 'Required': False}, {'Name': 'xp', 'Type': 'object', 'Description': 'Container for extended (custom) properties of the address.', 'Required': False}]}, 'Roles': ['FullAccess', 'MeAddressAdmin', 'Shopper']}, {'ID': 'CreateAddress', 'Name': 'Create a new address', 'Comments': ['Only available to Buyer Users.'], 'HttpVerb': 'POST', 'UriTemplate': 'v1/me/addresses', 'Parameters': [], 'RequestBody': {'Sample': '{\r\n  "Shipping": false,\r\n  "Billing": false,\r\n  "CompanyName": "",\r\n  "FirstName": "",\r\n  "LastName": "",\r\n  "Street1": "",\r\n  "Street2": "",\r\n  "City": "",\r\n  "State": "",\r\n  "Zip": "",\r\n  "Country": "",\r\n  "Phone": "",\r\n  "AddressName": "",\r\n  "xp": {}\r\n}', 'Fields': [{'Name': 'Shipping', 'Type': 'boolean', 'Description': 'Shipping of the address. Searchable: priority level 6.', 'Required': False}, {'Name': 'Billing', 'Type': 'boolean', 'Description': 'Billing of the address. Searchable: priority level 7.', 'Required': False}, {'Name': 'CompanyName', 'Type': 'string', 'Description': 'Company name of the address. Max length 100 characters. Sortable.', 'Required': False}, {'Name': 'FirstName', 'Type': 'string', 'Description': 'First name of the address. Max length 100 characters. Searchable: priority level 7. Sortable.', 'Required': False}, {'Name': 'LastName', 'Type': 'string', 'Description': 'Last name of the address. Max length 100 characters. Searchable: priority level 6. Sortable.', 'Required': False}, {'Name': 'Street1', 'Type': 'string', 'Description': 'Street 1 of the address. Required. Max length 100 characters. Searchable: priority level 4. Sortable.', 'Required': True}, {'Name': 'Street2', 'Type': 'string', 'Description': 'Street 2 of the address. Max length 100 characters. Searchable: priority level 5. Sortable.', 'Required': False}, {'Name': 'City', 'Type': 'string', 'Description': 'City of the address. Required. Max length 100 characters. Searchable: priority level 3. Sortable.', 'Required': True}, {'Name': 'State', 'Type': 'string', 'Description': 'State of the address. Required. Max length 100 characters. Searchable: priority level 7. Sortable.', 'Required': True}, {'Name': 'Zip', 'Type': 'string', 'Description': 'Zip of the address. Required. Max length 100 characters. Searchable: priority level 6. Sortable.', 'Required': True}, {'Name': 'Country', 'Type': 'string', 'Description': 'Country of the address. Required. Max length 2 characters. Sortable.', 'Required': True}, {'Name': 'Phone', 'Type': 'string', 'Description': 'Phone of the address. Max length 100 characters. Sortable.', 'Required': False}, {'Name': 'AddressName', 'Type': 'string', 'Description': 'Address name of the address. Max length 100 characters. Searchable: priority level 2. Sortable: priority level 1.', 'Required': False}, {'Name': 'xp', 'Type': 'object', 'Description': 'Container for extended (custom) properties of the address.', 'Required': False}]}, 'ResponseStatus': 201, 'ResponseBody': {'Sample': '{\r\n  "ID": "",\r\n  "Shipping": false,\r\n  "Billing": false,\r\n  "Editable": false,\r\n  "CompanyName": "",\r\n  "FirstName": "",\r\n  "LastName": "",\r\n  "Street1": "",\r\n  "Street2": "",\r\n  "City": "",\r\n  "State": "",\r\n  "Zip": "",\r\n  "Country": "",\r\n  "Phone": "",\r\n  "AddressName": "",\r\n  "xp": {}\r\n}', 'Fields': [{'Name': 'ID', 'Type': 'string', 'Description': 'ID of the address.', 'Required': False}, {'Name': 'Shipping', 'Type': 'boolean', 'Description': 'Shipping of the address.', 'Required': False}, {'Name': 'Billing', 'Type': 'boolean', 'Description': 'Billing of the address.', 'Required': False}, {'Name': 'Editable', 'Type': 'boolean', 'Description': 'Editable of the address.', 'Required': False}, {'Name': 'CompanyName', 'Type': 'string', 'Description': 'Company name of the address.', 'Required': False}, {'Name': 'FirstName', 'Type': 'string', 'Description': 'First name of the address.', 'Required': False}, {'Name': 'LastName', 'Type': 'string', 'Description': 'Last name of the address.', 'Required': False}, {'Name': 'Street1', 'Type': 'string', 'Description': 'Street 1 of the address.', 'Required': True}, {'Name': 'Street2', 'Type': 'string', 'Description': 'Street 2 of the address.', 'Required': False}, {'Name': 'City', 'Type': 'string', 'Description': 'City of the address.', 'Required': True}, {'Name': 'State', 'Type': 'string', 'Description': 'State of the address.', 'Required': True}, {'Name': 'Zip', 'Type': 'string', 'Description': 'Zip of the address.', 'Required': True}, {'Name': 'Country', 'Type': 'string', 'Description': 'Country of the address.', 'Required': True}, {'Name': 'Phone', 'Type': 'string', 'Description': 'Phone of the address.', 'Required': False}, {'Name': 'AddressName', 'Type': 'string', 'Description': 'Address name of the address.', 'Required': False}, {'Name': 'xp', 'Type': 'object', 'Description': 'Container for extended (custom) properties of the address.', 'Required': False}]}, 'Roles': ['FullAccess', 'MeAddressAdmin']}, {'ID': 'GetAddress', 'Name': 'Get a single address', 'Comments': ['Only available to Buyer Users.'], 'HttpVerb': 'GET', 'UriTemplate': 'v1/me/addresses/{addressID}', 'Parameters': [{'Name': 'addressID', 'Type': 'string', 'Description': 'ID of the address.', 'Required': True}], 'RequestBody': None, 'ResponseStatus': 200, 'ResponseBody': {'Sample': '{\r\n  "ID": "",\r\n  "Shipping": false,\r\n  "Billing": false,\r\n  "Editable": false,\r\n  "CompanyName": "",\r\n  "FirstName": "",\r\n  "LastName": "",\r\n  "Street1": "",\r\n  "Street2": "",\r\n  "City": "",\r\n  "State": "",\r\n  "Zip": "",\r\n  "Country": "",\r\n  "Phone": "",\r\n  "AddressName": "",\r\n  "xp": {}\r\n}', 'Fields': [{'Name': 'ID', 'Type': 'string', 'Description': 'ID of the address.', 'Required': False}, {'Name': 'Shipping', 'Type': 'boolean', 'Description': 'Shipping of the address.', 'Required': False}, {'Name': 'Billing', 'Type': 'boolean', 'Description': 'Billing of the address.', 'Required': False}, {'Name': 'Editable', 'Type': 'boolean', 'Description': 'Editable of the address.', 'Required': False}, {'Name': 'CompanyName', 'Type': 'string', 'Description': 'Company name of the address.', 'Required': False}, {'Name': 'FirstName', 'Type': 'string', 'Description': 'First name of the address.', 'Required': False}, {'Name': 'LastName', 'Type': 'string', 'Description': 'Last name of the address.', 'Required': False}, {'Name': 'Street1', 'Type': 'string', 'Description': 'Street 1 of the address.', 'Required': True}, {'Name': 'Street2', 'Type': 'string', 'Description': 'Street 2 of the address.', 'Required': False}, {'Name': 'City', 'Type': 'string', 'Description': 'City of the address.', 'Required': True}, {'Name': 'State', 'Type': 'string', 'Description': 'State of the address.', 'Required': True}, {'Name': 'Zip', 'Type': 'string', 'Description': 'Zip of the address.', 'Required': True}, {'Name': 'Country', 'Type': 'string', 'Description': 'Country of the address.', 'Required': True}, {'Name': 'Phone', 'Type': 'string', 'Description': 'Phone of the address.', 'Required': False}, {'Name': 'AddressName', 'Type': 'string', 'Description': 'Address name of the address.', 'Required': False}, {'Name': 'xp', 'Type': 'object', 'Description': 'Container for extended (custom) properties of the address.', 'Required': False}]}, 'Roles': ['FullAccess', 'MeAddressAdmin', 'Shopper']}, {'ID': 'UpdateAddress', 'Name': 'Create or update an address', 'Comments': ['Only available to Buyer Users.'], 'HttpVerb': 'PUT', 'UriTemplate': 'v1/me/addresses/{addressID}', 'Parameters': [{'Name': 'addressID', 'Type': 'string', 'Description': 'ID of the address.', 'Required': True}], 'RequestBody': {'Sample': '{\r\n  "Shipping": false,\r\n  "Billing": false,\r\n  "CompanyName": "",\r\n  "FirstName": "",\r\n  "LastName": "",\r\n  "Street1": "",\r\n  "Street2": "",\r\n  "City": "",\r\n  "State": "",\r\n  "Zip": "",\r\n  "Country": "",\r\n  "Phone": "",\r\n  "AddressName": "",\r\n  "xp": {}\r\n}', 'Fields': [{'Name': 'Shipping', 'Type': 'boolean', 'Description': 'Shipping of the address. Searchable: priority level 6.', 'Required': False}, {'Name': 'Billing', 'Type': 'boolean', 'Description': 'Billing of the address. Searchable: priority level 7.', 'Required': False}, {'Name': 'CompanyName', 'Type': 'string', 'Description': 'Company name of the address. Max length 100 characters. Sortable.', 'Required': False}, {'Name': 'FirstName', 'Type': 'string', 'Description': 'First name of the address. Max length 100 characters. Searchable: priority level 7. Sortable.', 'Required': False}, {'Name': 'LastName', 'Type': 'string', 'Description': 'Last name of the address. Max length 100 characters. Searchable: priority level 6. Sortable.', 'Required': False}, {'Name': 'Street1', 'Type': 'string', 'Description': 'Street 1 of the address. Required. Max length 100 characters. Searchable: priority level 4. Sortable.', 'Required': True}, {'Name': 'Street2', 'Type': 'string', 'Description': 'Street 2 of the address. Max length 100 characters. Searchable: priority level 5. Sortable.', 'Required': False}, {'Name': 'City', 'Type': 'string', 'Description': 'City of the address. Required. Max length 100 characters. Searchable: priority level 3. Sortable.', 'Required': True}, {'Name': 'State', 'Type': 'string', 'Description': 'State of the address. Required. Max length 100 characters. Searchable: priority level 7. Sortable.', 'Required': True}, {'Name': 'Zip', 'Type': 'string', 'Description': 'Zip of the address. Required. Max length 100 characters. Searchable: priority level 6. Sortable.', 'Required': True}, {'Name': 'Country', 'Type': 'string', 'Description': 'Country of the address. Required. Max length 2 characters. Sortable.', 'Required': True}, {'Name': 'Phone', 'Type': 'string', 'Description': 'Phone of the address. Max length 100 characters. Sortable.', 'Required': False}, {'Name': 'AddressName', 'Type': 'string', 'Description': 'Address name of the address. Max length 100 characters. Searchable: priority level 2. Sortable: priority level 1.', 'Required': False}, {'Name': 'xp', 'Type': 'object', 'Description': 'Container for extended (custom) properties of the address.', 'Required': False}]}, 'ResponseStatus': 200, 'ResponseBody': {'Sample': '{\r\n  "ID": "",\r\n  "Shipping": false,\r\n  "Billing": false,\r\n  "Editable": false,\r\n  "CompanyName": "",\r\n  "FirstName": "",\r\n  "LastName": "",\r\n  "Street1": "",\r\n  "Street2": "",\r\n  "City": "",\r\n  "State": "",\r\n  "Zip": "",\r\n  "Country": "",\r\n  "Phone": "",\r\n  "AddressName": "",\r\n  "xp": {}\r\n}', 'Fields': [{'Name': 'ID', 'Type': 'string', 'Description': 'ID of the address.', 'Required': False}, {'Name': 'Shipping', 'Type': 'boolean', 'Description': 'Shipping of the address.', 'Required': False}, {'Name': 'Billing', 'Type': 'boolean', 'Description': 'Billing of the address.', 'Required': False}, {'Name': 'Editable', 'Type': 'boolean', 'Description': 'Editable of the address.', 'Required': False}, {'Name': 'CompanyName', 'Type': 'string', 'Description': 'Company name of the address.', 'Required': False}, {'Name': 'FirstName', 'Type': 'string', 'Description': 'First name of the address.', 'Required': False}, {'Name': 'LastName', 'Type': 'string', 'Description': 'Last name of the address.', 'Required': False}, {'Name': 'Street1', 'Type': 'string', 'Description': 'Street 1 of the address.', 'Required': True}, {'Name': 'Street2', 'Type': 'string', 'Description': 'Street 2 of the address.', 'Required': False}, {'Name': 'City', 'Type': 'string', 'Description': 'City of the address.', 'Required': True}, {'Name': 'State', 'Type': 'string', 'Description': 'State of the address.', 'Required': True}, {'Name': 'Zip', 'Type': 'string', 'Description': 'Zip of the address.', 'Required': True}, {'Name': 'Country', 'Type': 'string', 'Description': 'Country of the address.', 'Required': True}, {'Name': 'Phone', 'Type': 'string', 'Description': 'Phone of the address.', 'Required': False}, {'Name': 'AddressName', 'Type': 'string', 'Description': 'Address name of the address.', 'Required': False}, {'Name': 'xp', 'Type': 'object', 'Description': 'Container for extended (custom) properties of the address.', 'Required': False}]}, 'Roles': ['FullAccess', 'MeAddressAdmin']}, {'ID': 'PatchAddress', 'Name': 'Partially update an address', 'Comments': ['Only available to Buyer Users.'], 'HttpVerb': 'PATCH', 'UriTemplate': 'v1/me/addresses/{addressID}', 'Parameters': [{'Name': 'addressID', 'Type': 'string', 'Description': 'ID of the address.', 'Required': True}], 'RequestBody': {'Sample': '{\r\n  "Shipping": false,\r\n  "Billing": false,\r\n  "CompanyName": "",\r\n  "FirstName": "",\r\n  "LastName": "",\r\n  "Street1": "",\r\n  "Street2": "",\r\n  "City": "",\r\n  "State": "",\r\n  "Zip": "",\r\n  "Country": "",\r\n  "Phone": "",\r\n  "AddressName": "",\r\n  "xp": {}\r\n}', 'Fields': [{'Name': 'Shipping', 'Type': 'boolean', 'Description': 'Shipping of the address. Searchable: priority level 6.', 'Required': False}, {'Name': 'Billing', 'Type': 'boolean', 'Description': 'Billing of the address. Searchable: priority level 7.', 'Required': False}, {'Name': 'CompanyName', 'Type': 'string', 'Description': 'Company name of the address. Max length 100 characters. Sortable.', 'Required': False}, {'Name': 'FirstName', 'Type': 'string', 'Description': 'First name of the address. Max length 100 characters. Searchable: priority level 7. Sortable.', 'Required': False}, {'Name': 'LastName', 'Type': 'string', 'Description': 'Last name of the address. Max length 100 characters. Searchable: priority level 6. Sortable.', 'Required': False}, {'Name': 'Street1', 'Type': 'string', 'Description': 'Street 1 of the address. Required. Max length 100 characters. Searchable: priority level 4. Sortable.', 'Required': True}, {'Name': 'Street2', 'Type': 'string', 'Description': 'Street 2 of the address. Max length 100 characters. Searchable: priority level 5. Sortable.', 'Required': False}, {'Name': 'City', 'Type': 'string', 'Description': 'City of the address. Required. Max length 100 characters. Searchable: priority level 3. Sortable.', 'Required': True}, {'Name': 'State', 'Type': 'string', 'Description': 'State of the address. Required. Max length 100 characters. Searchable: priority level 7. Sortable.', 'Required': True}, {'Name': 'Zip', 'Type': 'string', 'Description': 'Zip of the address. Required. Max length 100 characters. Searchable: priority level 6. Sortable.', 'Required': True}, {'Name': 'Country', 'Type': 'string', 'Description': 'Country of the address. Required. Max length 2 characters. Sortable.', 'Required': True}, {'Name': 'Phone', 'Type': 'string', 'Description': 'Phone of the address. Max length 100 characters. Sortable.', 'Required': False}, {'Name': 'AddressName', 'Type': 'string', 'Description': 'Address name of the address. Max length 100 characters. Searchable: priority level 2. Sortable: priority level 1.', 'Required': False}, {'Name': 'xp', 'Type': 'object', 'Description': 'Container for extended (custom) properties of the address.', 'Required': False}]}, 'ResponseStatus': 204, 'ResponseBody': None, 'Roles': ['FullAccess', 'MeAddressAdmin']}, {'ID': 'DeleteAddress', 'Name': 'Delete an address', 'Comments': ['Only available to Buyer Users.'], 'HttpVerb': 'DELETE', 'UriTemplate': 'v1/me/addresses/{addressID}', 'Parameters': [{'Name': 'addressID', 'Type': 'string', 'Description': 'ID of the address.', 'Required': True}], 'RequestBody': None, 'ResponseStatus': 204, 'ResponseBody': None, 'Roles': ['FullAccess', 'MeAddressAdmin']}]