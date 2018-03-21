---
title: Addresses
date: 2018-03-19 18:56:07
category: content\api-reference
tags: Buyers
slug: Addresses
---
[{'ID': 'Get', 'Name': 'Get a single address', 'Comments': [], 'HttpVerb': 'GET', 'UriTemplate': 'v1/buyers/{buyerID}/addresses/{addressID}', 'Parameters': [{'Name': 'buyerID', 'Type': 'string', 'Description': 'ID of the buyer.', 'Required': True}, {'Name': 'addressID', 'Type': 'string', 'Description': 'ID of the address.', 'Required': True}], 'RequestBody': None, 'ResponseStatus': 200, 'ResponseBody': {'Sample': '{\r\n  "ID": "",\r\n  "CompanyName": "",\r\n  "FirstName": "",\r\n  "LastName": "",\r\n  "Street1": "",\r\n  "Street2": "",\r\n  "City": "",\r\n  "State": "",\r\n  "Zip": "",\r\n  "Country": "",\r\n  "Phone": "",\r\n  "AddressName": "",\r\n  "xp": {}\r\n}', 'Fields': [{'Name': 'ID', 'Type': 'string', 'Description': 'ID of the address.', 'Required': False}, {'Name': 'CompanyName', 'Type': 'string', 'Description': 'Company name of the address.', 'Required': False}, {'Name': 'FirstName', 'Type': 'string', 'Description': 'First name of the address.', 'Required': False}, {'Name': 'LastName', 'Type': 'string', 'Description': 'Last name of the address.', 'Required': False}, {'Name': 'Street1', 'Type': 'string', 'Description': 'Street 1 of the address.', 'Required': True}, {'Name': 'Street2', 'Type': 'string', 'Description': 'Street 2 of the address.', 'Required': False}, {'Name': 'City', 'Type': 'string', 'Description': 'City of the address.', 'Required': True}, {'Name': 'State', 'Type': 'string', 'Description': 'State of the address.', 'Required': True}, {'Name': 'Zip', 'Type': 'string', 'Description': 'Zip of the address.', 'Required': True}, {'Name': 'Country', 'Type': 'string', 'Description': 'Country of the address.', 'Required': True}, {'Name': 'Phone', 'Type': 'string', 'Description': 'Phone of the address.', 'Required': False}, {'Name': 'AddressName', 'Type': 'string', 'Description': 'Address name of the address.', 'Required': False}, {'Name': 'xp', 'Type': 'object', 'Description': 'Container for extended (custom) properties of the address.', 'Required': False}]}, 'Roles': ['FullAccess', 'AddressAdmin', 'AddressReader']}, {'ID': 'List', 'Name': 'Get a list of addresses', 'Comments': [], 'HttpVerb': 'GET', 'UriTemplate': 'v1/buyers/{buyerID}/addresses', 'Parameters': [{'Name': 'buyerID', 'Type': 'string', 'Description': 'ID of the buyer.', 'Required': True}, {'Name': 'search', 'Type': 'string', 'Description': 'Word or phrase to search for.', 'Required': False}, {'Name': 'searchOn', 'Type': 'string', 'Description': 'Comma-delimited list of fields to search on.', 'Required': False}, {'Name': 'sortBy', 'Type': 'string', 'Description': 'Comma-delimited list of fields to sort by.', 'Required': False}, {'Name': 'page', 'Type': 'integer', 'Description': 'Page of results to return. Default: 1', 'Required': False}, {'Name': 'pageSize', 'Type': 'integer', 'Description': 'Number of results to return per page. Default: 20, max: 100.', 'Required': False}, {'Name': 'filters', 'Type': 'object', 'Description': "Any additional key/value pairs passed in the query string are interpretted as filters. Valid keys are top-level properties of the returned model or 'xp.???'", 'Required': False}], 'RequestBody': None, 'ResponseStatus': 200, 'ResponseBody': {'Sample': '{\r\n  "Meta": {\r\n    "Page": 1,\r\n    "PageSize": 20,\r\n    "TotalCount": 25,\r\n    "TotalPages": 2,\r\n    "ItemRange": [\r\n      1,\r\n      20\r\n    ]\r\n  },\r\n  "Items": [\r\n    {\r\n      "ID": "",\r\n      "CompanyName": "",\r\n      "FirstName": "",\r\n      "LastName": "",\r\n      "Street1": "",\r\n      "Street2": "",\r\n      "City": "",\r\n      "State": "",\r\n      "Zip": "",\r\n      "Country": "",\r\n      "Phone": "",\r\n      "AddressName": "",\r\n      "xp": {}\r\n    }\r\n  ]\r\n}', 'Fields': [{'Name': 'ID', 'Type': 'string', 'Description': 'ID of the address.', 'Required': False}, {'Name': 'CompanyName', 'Type': 'string', 'Description': 'Company name of the address.', 'Required': False}, {'Name': 'FirstName', 'Type': 'string', 'Description': 'First name of the address.', 'Required': False}, {'Name': 'LastName', 'Type': 'string', 'Description': 'Last name of the address.', 'Required': False}, {'Name': 'Street1', 'Type': 'string', 'Description': 'Street 1 of the address.', 'Required': True}, {'Name': 'Street2', 'Type': 'string', 'Description': 'Street 2 of the address.', 'Required': False}, {'Name': 'City', 'Type': 'string', 'Description': 'City of the address.', 'Required': True}, {'Name': 'State', 'Type': 'string', 'Description': 'State of the address.', 'Required': True}, {'Name': 'Zip', 'Type': 'string', 'Description': 'Zip of the address.', 'Required': True}, {'Name': 'Country', 'Type': 'string', 'Description': 'Country of the address.', 'Required': True}, {'Name': 'Phone', 'Type': 'string', 'Description': 'Phone of the address.', 'Required': False}, {'Name': 'AddressName', 'Type': 'string', 'Description': 'Address name of the address.', 'Required': False}, {'Name': 'xp', 'Type': 'object', 'Description': 'Container for extended (custom) properties of the address.', 'Required': False}]}, 'Roles': ['FullAccess', 'AddressAdmin', 'AddressReader']}, {'ID': 'Create', 'Name': 'Create a new address', 'Comments': [], 'HttpVerb': 'POST', 'UriTemplate': 'v1/buyers/{buyerID}/addresses', 'Parameters': [{'Name': 'buyerID', 'Type': 'string', 'Description': 'ID of the buyer.', 'Required': True}], 'RequestBody': {'Sample': '{\r\n  "ID": "",\r\n  "CompanyName": "",\r\n  "FirstName": "",\r\n  "LastName": "",\r\n  "Street1": "",\r\n  "Street2": "",\r\n  "City": "",\r\n  "State": "",\r\n  "Zip": "",\r\n  "Country": "",\r\n  "Phone": "",\r\n  "AddressName": "",\r\n  "xp": {}\r\n}', 'Fields': [{'Name': 'ID', 'Type': 'string', 'Description': 'ID of the address. Can only contain characters Aa-Zz, 0-9, -, and _. Searchable: priority level 1. Sortable: priority level 2.', 'Required': False}, {'Name': 'CompanyName', 'Type': 'string', 'Description': 'Company name of the address. Max length 100 characters. Sortable.', 'Required': False}, {'Name': 'FirstName', 'Type': 'string', 'Description': 'First name of the address. Max length 100 characters. Searchable: priority level 7. Sortable.', 'Required': False}, {'Name': 'LastName', 'Type': 'string', 'Description': 'Last name of the address. Max length 100 characters. Searchable: priority level 6. Sortable.', 'Required': False}, {'Name': 'Street1', 'Type': 'string', 'Description': 'Street 1 of the address. Required. Max length 100 characters. Searchable: priority level 4. Sortable.', 'Required': True}, {'Name': 'Street2', 'Type': 'string', 'Description': 'Street 2 of the address. Max length 100 characters. Searchable: priority level 5. Sortable.', 'Required': False}, {'Name': 'City', 'Type': 'string', 'Description': 'City of the address. Required. Max length 100 characters. Searchable: priority level 3. Sortable.', 'Required': True}, {'Name': 'State', 'Type': 'string', 'Description': 'State of the address. Required. Max length 100 characters. Searchable: priority level 7. Sortable.', 'Required': True}, {'Name': 'Zip', 'Type': 'string', 'Description': 'Zip of the address. Required. Max length 100 characters. Searchable: priority level 6. Sortable.', 'Required': True}, {'Name': 'Country', 'Type': 'string', 'Description': 'Country of the address. Required. Max length 2 characters. Sortable.', 'Required': True}, {'Name': 'Phone', 'Type': 'string', 'Description': 'Phone of the address. Max length 100 characters. Sortable.', 'Required': False}, {'Name': 'AddressName', 'Type': 'string', 'Description': 'Address name of the address. Max length 100 characters. Searchable: priority level 2. Sortable: priority level 1.', 'Required': False}, {'Name': 'xp', 'Type': 'object', 'Description': 'Container for extended (custom) properties of the address.', 'Required': False}]}, 'ResponseStatus': 201, 'ResponseBody': {'Sample': '{\r\n  "ID": "",\r\n  "CompanyName": "",\r\n  "FirstName": "",\r\n  "LastName": "",\r\n  "Street1": "",\r\n  "Street2": "",\r\n  "City": "",\r\n  "State": "",\r\n  "Zip": "",\r\n  "Country": "",\r\n  "Phone": "",\r\n  "AddressName": "",\r\n  "xp": {}\r\n}', 'Fields': [{'Name': 'ID', 'Type': 'string', 'Description': 'ID of the address.', 'Required': False}, {'Name': 'CompanyName', 'Type': 'string', 'Description': 'Company name of the address.', 'Required': False}, {'Name': 'FirstName', 'Type': 'string', 'Description': 'First name of the address.', 'Required': False}, {'Name': 'LastName', 'Type': 'string', 'Description': 'Last name of the address.', 'Required': False}, {'Name': 'Street1', 'Type': 'string', 'Description': 'Street 1 of the address.', 'Required': True}, {'Name': 'Street2', 'Type': 'string', 'Description': 'Street 2 of the address.', 'Required': False}, {'Name': 'City', 'Type': 'string', 'Description': 'City of the address.', 'Required': True}, {'Name': 'State', 'Type': 'string', 'Description': 'State of the address.', 'Required': True}, {'Name': 'Zip', 'Type': 'string', 'Description': 'Zip of the address.', 'Required': True}, {'Name': 'Country', 'Type': 'string', 'Description': 'Country of the address.', 'Required': True}, {'Name': 'Phone', 'Type': 'string', 'Description': 'Phone of the address.', 'Required': False}, {'Name': 'AddressName', 'Type': 'string', 'Description': 'Address name of the address.', 'Required': False}, {'Name': 'xp', 'Type': 'object', 'Description': 'Container for extended (custom) properties of the address.', 'Required': False}]}, 'Roles': ['FullAccess', 'AddressAdmin']}, {'ID': 'Update', 'Name': 'Create or update an address', 'Comments': [], 'HttpVerb': 'PUT', 'UriTemplate': 'v1/buyers/{buyerID}/addresses/{addressID}', 'Parameters': [{'Name': 'buyerID', 'Type': 'string', 'Description': 'ID of the buyer.', 'Required': True}, {'Name': 'addressID', 'Type': 'string', 'Description': 'ID of the address.', 'Required': True}], 'RequestBody': {'Sample': '{\r\n  "ID": "",\r\n  "CompanyName": "",\r\n  "FirstName": "",\r\n  "LastName": "",\r\n  "Street1": "",\r\n  "Street2": "",\r\n  "City": "",\r\n  "State": "",\r\n  "Zip": "",\r\n  "Country": "",\r\n  "Phone": "",\r\n  "AddressName": "",\r\n  "xp": {}\r\n}', 'Fields': [{'Name': 'ID', 'Type': 'string', 'Description': 'ID of the address. Can only contain characters Aa-Zz, 0-9, -, and _. Searchable: priority level 1. Sortable: priority level 2.', 'Required': False}, {'Name': 'CompanyName', 'Type': 'string', 'Description': 'Company name of the address. Max length 100 characters. Sortable.', 'Required': False}, {'Name': 'FirstName', 'Type': 'string', 'Description': 'First name of the address. Max length 100 characters. Searchable: priority level 7. Sortable.', 'Required': False}, {'Name': 'LastName', 'Type': 'string', 'Description': 'Last name of the address. Max length 100 characters. Searchable: priority level 6. Sortable.', 'Required': False}, {'Name': 'Street1', 'Type': 'string', 'Description': 'Street 1 of the address. Required. Max length 100 characters. Searchable: priority level 4. Sortable.', 'Required': True}, {'Name': 'Street2', 'Type': 'string', 'Description': 'Street 2 of the address. Max length 100 characters. Searchable: priority level 5. Sortable.', 'Required': False}, {'Name': 'City', 'Type': 'string', 'Description': 'City of the address. Required. Max length 100 characters. Searchable: priority level 3. Sortable.', 'Required': True}, {'Name': 'State', 'Type': 'string', 'Description': 'State of the address. Required. Max length 100 characters. Searchable: priority level 7. Sortable.', 'Required': True}, {'Name': 'Zip', 'Type': 'string', 'Description': 'Zip of the address. Required. Max length 100 characters. Searchable: priority level 6. Sortable.', 'Required': True}, {'Name': 'Country', 'Type': 'string', 'Description': 'Country of the address. Required. Max length 2 characters. Sortable.', 'Required': True}, {'Name': 'Phone', 'Type': 'string', 'Description': 'Phone of the address. Max length 100 characters. Sortable.', 'Required': False}, {'Name': 'AddressName', 'Type': 'string', 'Description': 'Address name of the address. Max length 100 characters. Searchable: priority level 2. Sortable: priority level 1.', 'Required': False}, {'Name': 'xp', 'Type': 'object', 'Description': 'Container for extended (custom) properties of the address.', 'Required': False}]}, 'ResponseStatus': 200, 'ResponseBody': {'Sample': '{\r\n  "ID": "",\r\n  "CompanyName": "",\r\n  "FirstName": "",\r\n  "LastName": "",\r\n  "Street1": "",\r\n  "Street2": "",\r\n  "City": "",\r\n  "State": "",\r\n  "Zip": "",\r\n  "Country": "",\r\n  "Phone": "",\r\n  "AddressName": "",\r\n  "xp": {}\r\n}', 'Fields': [{'Name': 'ID', 'Type': 'string', 'Description': 'ID of the address.', 'Required': False}, {'Name': 'CompanyName', 'Type': 'string', 'Description': 'Company name of the address.', 'Required': False}, {'Name': 'FirstName', 'Type': 'string', 'Description': 'First name of the address.', 'Required': False}, {'Name': 'LastName', 'Type': 'string', 'Description': 'Last name of the address.', 'Required': False}, {'Name': 'Street1', 'Type': 'string', 'Description': 'Street 1 of the address.', 'Required': True}, {'Name': 'Street2', 'Type': 'string', 'Description': 'Street 2 of the address.', 'Required': False}, {'Name': 'City', 'Type': 'string', 'Description': 'City of the address.', 'Required': True}, {'Name': 'State', 'Type': 'string', 'Description': 'State of the address.', 'Required': True}, {'Name': 'Zip', 'Type': 'string', 'Description': 'Zip of the address.', 'Required': True}, {'Name': 'Country', 'Type': 'string', 'Description': 'Country of the address.', 'Required': True}, {'Name': 'Phone', 'Type': 'string', 'Description': 'Phone of the address.', 'Required': False}, {'Name': 'AddressName', 'Type': 'string', 'Description': 'Address name of the address.', 'Required': False}, {'Name': 'xp', 'Type': 'object', 'Description': 'Container for extended (custom) properties of the address.', 'Required': False}]}, 'Roles': ['FullAccess', 'AddressAdmin']}, {'ID': 'Delete', 'Name': 'Delete an address', 'Comments': [], 'HttpVerb': 'DELETE', 'UriTemplate': 'v1/buyers/{buyerID}/addresses/{addressID}', 'Parameters': [{'Name': 'buyerID', 'Type': 'string', 'Description': 'ID of the buyer.', 'Required': True}, {'Name': 'addressID', 'Type': 'string', 'Description': 'ID of the address.', 'Required': True}], 'RequestBody': None, 'ResponseStatus': 204, 'ResponseBody': None, 'Roles': ['FullAccess', 'AddressAdmin']}, {'ID': 'Patch', 'Name': 'Partially update an address', 'Comments': [], 'HttpVerb': 'PATCH', 'UriTemplate': 'v1/buyers/{buyerID}/addresses/{addressID}', 'Parameters': [{'Name': 'buyerID', 'Type': 'string', 'Description': 'ID of the buyer.', 'Required': True}, {'Name': 'addressID', 'Type': 'string', 'Description': 'ID of the address.', 'Required': True}], 'RequestBody': {'Sample': '{\r\n  "ID": "",\r\n  "CompanyName": "",\r\n  "FirstName": "",\r\n  "LastName": "",\r\n  "Street1": "",\r\n  "Street2": "",\r\n  "City": "",\r\n  "State": "",\r\n  "Zip": "",\r\n  "Country": "",\r\n  "Phone": "",\r\n  "AddressName": "",\r\n  "xp": {}\r\n}', 'Fields': [{'Name': 'ID', 'Type': 'string', 'Description': 'ID of the address. Can only contain characters Aa-Zz, 0-9, -, and _. Searchable: priority level 1. Sortable: priority level 2.', 'Required': False}, {'Name': 'CompanyName', 'Type': 'string', 'Description': 'Company name of the address. Max length 100 characters. Sortable.', 'Required': False}, {'Name': 'FirstName', 'Type': 'string', 'Description': 'First name of the address. Max length 100 characters. Searchable: priority level 7. Sortable.', 'Required': False}, {'Name': 'LastName', 'Type': 'string', 'Description': 'Last name of the address. Max length 100 characters. Searchable: priority level 6. Sortable.', 'Required': False}, {'Name': 'Street1', 'Type': 'string', 'Description': 'Street 1 of the address. Required. Max length 100 characters. Searchable: priority level 4. Sortable.', 'Required': True}, {'Name': 'Street2', 'Type': 'string', 'Description': 'Street 2 of the address. Max length 100 characters. Searchable: priority level 5. Sortable.', 'Required': False}, {'Name': 'City', 'Type': 'string', 'Description': 'City of the address. Required. Max length 100 characters. Searchable: priority level 3. Sortable.', 'Required': True}, {'Name': 'State', 'Type': 'string', 'Description': 'State of the address. Required. Max length 100 characters. Searchable: priority level 7. Sortable.', 'Required': True}, {'Name': 'Zip', 'Type': 'string', 'Description': 'Zip of the address. Required. Max length 100 characters. Searchable: priority level 6. Sortable.', 'Required': True}, {'Name': 'Country', 'Type': 'string', 'Description': 'Country of the address. Required. Max length 2 characters. Sortable.', 'Required': True}, {'Name': 'Phone', 'Type': 'string', 'Description': 'Phone of the address. Max length 100 characters. Sortable.', 'Required': False}, {'Name': 'AddressName', 'Type': 'string', 'Description': 'Address name of the address. Max length 100 characters. Searchable: priority level 2. Sortable: priority level 1.', 'Required': False}, {'Name': 'xp', 'Type': 'object', 'Description': 'Container for extended (custom) properties of the address.', 'Required': False}]}, 'ResponseStatus': 200, 'ResponseBody': {'Sample': '{\r\n  "ID": "",\r\n  "CompanyName": "",\r\n  "FirstName": "",\r\n  "LastName": "",\r\n  "Street1": "",\r\n  "Street2": "",\r\n  "City": "",\r\n  "State": "",\r\n  "Zip": "",\r\n  "Country": "",\r\n  "Phone": "",\r\n  "AddressName": "",\r\n  "xp": {}\r\n}', 'Fields': [{'Name': 'ID', 'Type': 'string', 'Description': 'ID of the address.', 'Required': False}, {'Name': 'CompanyName', 'Type': 'string', 'Description': 'Company name of the address.', 'Required': False}, {'Name': 'FirstName', 'Type': 'string', 'Description': 'First name of the address.', 'Required': False}, {'Name': 'LastName', 'Type': 'string', 'Description': 'Last name of the address.', 'Required': False}, {'Name': 'Street1', 'Type': 'string', 'Description': 'Street 1 of the address.', 'Required': True}, {'Name': 'Street2', 'Type': 'string', 'Description': 'Street 2 of the address.', 'Required': False}, {'Name': 'City', 'Type': 'string', 'Description': 'City of the address.', 'Required': True}, {'Name': 'State', 'Type': 'string', 'Description': 'State of the address.', 'Required': True}, {'Name': 'Zip', 'Type': 'string', 'Description': 'Zip of the address.', 'Required': True}, {'Name': 'Country', 'Type': 'string', 'Description': 'Country of the address.', 'Required': True}, {'Name': 'Phone', 'Type': 'string', 'Description': 'Phone of the address.', 'Required': False}, {'Name': 'AddressName', 'Type': 'string', 'Description': 'Address name of the address.', 'Required': False}, {'Name': 'xp', 'Type': 'object', 'Description': 'Container for extended (custom) properties of the address.', 'Required': False}]}, 'Roles': ['FullAccess', 'AddressAdmin']}, {'ID': 'ListAssignments', 'Name': 'Get a list of address assignments', 'Comments': [], 'HttpVerb': 'GET', 'UriTemplate': 'v1/buyers/{buyerID}/addresses/assignments', 'Parameters': [{'Name': 'buyerID', 'Type': 'string', 'Description': 'ID of the buyer.', 'Required': True}, {'Name': 'addressID', 'Type': 'string', 'Description': 'ID of the address.', 'Required': False}, {'Name': 'userID', 'Type': 'string', 'Description': 'ID of the user.', 'Required': False}, {'Name': 'userGroupID', 'Type': 'string', 'Description': 'ID of the user group.', 'Required': False}, {'Name': 'level', 'Type': 'string', 'Description': 'Level of the address assignment. Possible values: User, Group, Company.', 'Required': False}, {'Name': 'isShipping', 'Type': 'boolean', 'Description': 'Is shipping of the address assignment.', 'Required': False}, {'Name': 'isBilling', 'Type': 'boolean', 'Description': 'Is billing of the address assignment.', 'Required': False}, {'Name': 'page', 'Type': 'integer', 'Description': 'Page of results to return. Default: 1', 'Required': False}, {'Name': 'pageSize', 'Type': 'integer', 'Description': 'Number of results to return per page. Default: 20, max: 100.', 'Required': False}], 'RequestBody': None, 'ResponseStatus': 200, 'ResponseBody': {'Sample': '{\r\n  "Meta": {\r\n    "Page": 1,\r\n    "PageSize": 20,\r\n    "TotalCount": 25,\r\n    "TotalPages": 2,\r\n    "ItemRange": [\r\n      1,\r\n      20\r\n    ]\r\n  },\r\n  "Items": [\r\n    {\r\n      "AddressID": "",\r\n      "UserID": "",\r\n      "UserGroupID": "",\r\n      "IsShipping": false,\r\n      "IsBilling": false\r\n    }\r\n  ]\r\n}', 'Fields': [{'Name': 'AddressID', 'Type': 'string', 'Description': 'ID of the address.', 'Required': True}, {'Name': 'UserID', 'Type': 'string', 'Description': 'ID of the user.', 'Required': False}, {'Name': 'UserGroupID', 'Type': 'string', 'Description': 'ID of the user group.', 'Required': False}, {'Name': 'IsShipping', 'Type': 'boolean', 'Description': 'Is shipping of the address assignment.', 'Required': False}, {'Name': 'IsBilling', 'Type': 'boolean', 'Description': 'Is billing of the address assignment.', 'Required': False}]}, 'Roles': ['FullAccess', 'AddressAdmin', 'AddressReader']}, {'ID': 'DeleteAssignment', 'Name': 'Delete an address assignment', 'Comments': [], 'HttpVerb': 'DELETE', 'UriTemplate': 'v1/buyers/{buyerID}/addresses/{addressID}/assignments', 'Parameters': [{'Name': 'buyerID', 'Type': 'string', 'Description': 'ID of the buyer.', 'Required': True}, {'Name': 'addressID', 'Type': 'string', 'Description': 'ID of the address.', 'Required': True}, {'Name': 'userID', 'Type': 'string', 'Description': 'ID of the user.', 'Required': False}, {'Name': 'userGroupID', 'Type': 'string', 'Description': 'ID of the user group.', 'Required': False}], 'RequestBody': None, 'ResponseStatus': 204, 'ResponseBody': None, 'Roles': ['FullAccess', 'AddressAdmin']}, {'ID': 'SaveAssignment', 'Name': 'Save an address assignment', 'Comments': [], 'HttpVerb': 'POST', 'UriTemplate': 'v1/buyers/{buyerID}/addresses/assignments', 'Parameters': [{'Name': 'buyerID', 'Type': 'string', 'Description': 'ID of the buyer.', 'Required': True}], 'RequestBody': {'Sample': '{\r\n  "AddressID": "",\r\n  "UserID": "",\r\n  "UserGroupID": "",\r\n  "IsShipping": false,\r\n  "IsBilling": false\r\n}', 'Fields': [{'Name': 'AddressID', 'Type': 'string', 'Description': 'ID of the address. Required. Sortable: priority level 1.', 'Required': True}, {'Name': 'UserID', 'Type': 'string', 'Description': 'ID of the user. Sortable: priority level 2.', 'Required': False}, {'Name': 'UserGroupID', 'Type': 'string', 'Description': 'ID of the user group. Sortable: priority level 3.', 'Required': False}, {'Name': 'IsShipping', 'Type': 'boolean', 'Description': 'Is shipping of the address assignment.', 'Required': False}, {'Name': 'IsBilling', 'Type': 'boolean', 'Description': 'Is billing of the address assignment.', 'Required': False}]}, 'ResponseStatus': 204, 'ResponseBody': None, 'Roles': ['FullAccess', 'AddressAdmin']}]