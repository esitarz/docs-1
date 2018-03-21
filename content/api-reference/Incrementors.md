---
title: Incrementors
date: 2018-03-19 18:56:07
category: content\api-reference
tags: Seller
slug: Incrementors
---
[{'ID': 'Get', 'Name': 'Get a single incrementor', 'Comments': [], 'HttpVerb': 'GET', 'UriTemplate': 'v1/incrementors/{incrementorID}', 'Parameters': [{'Name': 'incrementorID', 'Type': 'string', 'Description': 'ID of the incrementor.', 'Required': True}], 'RequestBody': None, 'ResponseStatus': 200, 'ResponseBody': {'Sample': '{\r\n  "ID": "",\r\n  "Name": "",\r\n  "LastNumber": 0,\r\n  "LeftPaddingCount": 0\r\n}', 'Fields': [{'Name': 'ID', 'Type': 'string', 'Description': 'ID of the incrementor.', 'Required': False}, {'Name': 'Name', 'Type': 'string', 'Description': 'Name of the incrementor.', 'Required': False}, {'Name': 'LastNumber', 'Type': 'integer', 'Description': 'Last number of the incrementor.', 'Required': True}, {'Name': 'LeftPaddingCount', 'Type': 'integer', 'Description': 'Left padding count of the incrementor.', 'Required': True}]}, 'Roles': ['FullAccess', 'IncrementorAdmin', 'IncrementorReader']}, {'ID': 'List', 'Name': 'Get a list of incrementors', 'Comments': [], 'HttpVerb': 'GET', 'UriTemplate': 'v1/incrementors', 'Parameters': [{'Name': 'search', 'Type': 'string', 'Description': 'Word or phrase to search for.', 'Required': False}, {'Name': 'searchOn', 'Type': 'string', 'Description': 'Comma-delimited list of fields to search on.', 'Required': False}, {'Name': 'sortBy', 'Type': 'string', 'Description': 'Comma-delimited list of fields to sort by.', 'Required': False}, {'Name': 'page', 'Type': 'integer', 'Description': 'Page of results to return. Default: 1', 'Required': False}, {'Name': 'pageSize', 'Type': 'integer', 'Description': 'Number of results to return per page. Default: 20, max: 100.', 'Required': False}, {'Name': 'filters', 'Type': 'object', 'Description': "Any additional key/value pairs passed in the query string are interpretted as filters. Valid keys are top-level properties of the returned model or 'xp.???'", 'Required': False}], 'RequestBody': None, 'ResponseStatus': 200, 'ResponseBody': {'Sample': '{\r\n  "Meta": {\r\n    "Page": 1,\r\n    "PageSize": 20,\r\n    "TotalCount": 25,\r\n    "TotalPages": 2,\r\n    "ItemRange": [\r\n      1,\r\n      20\r\n    ]\r\n  },\r\n  "Items": [\r\n    {\r\n      "ID": "",\r\n      "Name": "",\r\n      "LastNumber": 0,\r\n      "LeftPaddingCount": 0\r\n    }\r\n  ]\r\n}', 'Fields': [{'Name': 'ID', 'Type': 'string', 'Description': 'ID of the incrementor.', 'Required': False}, {'Name': 'Name', 'Type': 'string', 'Description': 'Name of the incrementor.', 'Required': False}, {'Name': 'LastNumber', 'Type': 'integer', 'Description': 'Last number of the incrementor.', 'Required': True}, {'Name': 'LeftPaddingCount', 'Type': 'integer', 'Description': 'Left padding count of the incrementor.', 'Required': True}]}, 'Roles': ['FullAccess', 'IncrementorAdmin', 'IncrementorReader']}, {'ID': 'Create', 'Name': 'Create a new incrementor', 'Comments': [], 'HttpVerb': 'POST', 'UriTemplate': 'v1/incrementors', 'Parameters': [], 'RequestBody': {'Sample': '{\r\n  "ID": "",\r\n  "Name": "",\r\n  "LastNumber": 0,\r\n  "LeftPaddingCount": 0\r\n}', 'Fields': [{'Name': 'ID', 'Type': 'string', 'Description': 'ID of the incrementor. Can only contain characters Aa-Zz, 0-9, -, and _. Searchable: priority level 1. Sortable: priority level 1.', 'Required': False}, {'Name': 'Name', 'Type': 'string', 'Description': 'Name of the incrementor. Max length 100 characters. Searchable: priority level 2. Sortable: priority level 2.', 'Required': False}, {'Name': 'LastNumber', 'Type': 'integer', 'Description': 'Last number of the incrementor. Required. Must be between 0 and 2147483647.', 'Required': True}, {'Name': 'LeftPaddingCount', 'Type': 'integer', 'Description': 'Left padding count of the incrementor. Required. Must be between 0 and 25.', 'Required': True}]}, 'ResponseStatus': 201, 'ResponseBody': {'Sample': '{\r\n  "ID": "",\r\n  "Name": "",\r\n  "LastNumber": 0,\r\n  "LeftPaddingCount": 0\r\n}', 'Fields': [{'Name': 'ID', 'Type': 'string', 'Description': 'ID of the incrementor.', 'Required': False}, {'Name': 'Name', 'Type': 'string', 'Description': 'Name of the incrementor.', 'Required': False}, {'Name': 'LastNumber', 'Type': 'integer', 'Description': 'Last number of the incrementor.', 'Required': True}, {'Name': 'LeftPaddingCount', 'Type': 'integer', 'Description': 'Left padding count of the incrementor.', 'Required': True}]}, 'Roles': ['FullAccess', 'IncrementorAdmin']}, {'ID': 'Update', 'Name': 'Create or update an incrementor', 'Comments': [], 'HttpVerb': 'PUT', 'UriTemplate': 'v1/incrementors/{incrementorID}', 'Parameters': [{'Name': 'incrementorID', 'Type': 'string', 'Description': 'ID of the incrementor.', 'Required': True}], 'RequestBody': {'Sample': '{\r\n  "ID": "",\r\n  "Name": "",\r\n  "LastNumber": 0,\r\n  "LeftPaddingCount": 0\r\n}', 'Fields': [{'Name': 'ID', 'Type': 'string', 'Description': 'ID of the incrementor. Can only contain characters Aa-Zz, 0-9, -, and _. Searchable: priority level 1. Sortable: priority level 1.', 'Required': False}, {'Name': 'Name', 'Type': 'string', 'Description': 'Name of the incrementor. Max length 100 characters. Searchable: priority level 2. Sortable: priority level 2.', 'Required': False}, {'Name': 'LastNumber', 'Type': 'integer', 'Description': 'Last number of the incrementor. Required. Must be between 0 and 2147483647.', 'Required': True}, {'Name': 'LeftPaddingCount', 'Type': 'integer', 'Description': 'Left padding count of the incrementor. Required. Must be between 0 and 25.', 'Required': True}]}, 'ResponseStatus': 200, 'ResponseBody': {'Sample': '{\r\n  "ID": "",\r\n  "Name": "",\r\n  "LastNumber": 0,\r\n  "LeftPaddingCount": 0\r\n}', 'Fields': [{'Name': 'ID', 'Type': 'string', 'Description': 'ID of the incrementor.', 'Required': False}, {'Name': 'Name', 'Type': 'string', 'Description': 'Name of the incrementor.', 'Required': False}, {'Name': 'LastNumber', 'Type': 'integer', 'Description': 'Last number of the incrementor.', 'Required': True}, {'Name': 'LeftPaddingCount', 'Type': 'integer', 'Description': 'Left padding count of the incrementor.', 'Required': True}]}, 'Roles': ['FullAccess', 'IncrementorAdmin']}, {'ID': 'Delete', 'Name': 'Delete an incrementor', 'Comments': [], 'HttpVerb': 'DELETE', 'UriTemplate': 'v1/incrementors/{incrementorID}', 'Parameters': [{'Name': 'incrementorID', 'Type': 'string', 'Description': 'ID of the incrementor.', 'Required': True}], 'RequestBody': None, 'ResponseStatus': 204, 'ResponseBody': None, 'Roles': ['FullAccess', 'IncrementorAdmin']}, {'ID': 'Patch', 'Name': 'Partially update an incrementor', 'Comments': [], 'HttpVerb': 'PATCH', 'UriTemplate': 'v1/incrementors/{incrementorID}', 'Parameters': [{'Name': 'incrementorID', 'Type': 'string', 'Description': 'ID of the incrementor.', 'Required': True}], 'RequestBody': {'Sample': '{\r\n  "ID": "",\r\n  "Name": "",\r\n  "LastNumber": 0,\r\n  "LeftPaddingCount": 0\r\n}', 'Fields': [{'Name': 'ID', 'Type': 'string', 'Description': 'ID of the incrementor. Can only contain characters Aa-Zz, 0-9, -, and _. Searchable: priority level 1. Sortable: priority level 1.', 'Required': False}, {'Name': 'Name', 'Type': 'string', 'Description': 'Name of the incrementor. Max length 100 characters. Searchable: priority level 2. Sortable: priority level 2.', 'Required': False}, {'Name': 'LastNumber', 'Type': 'integer', 'Description': 'Last number of the incrementor. Required. Must be between 0 and 2147483647.', 'Required': True}, {'Name': 'LeftPaddingCount', 'Type': 'integer', 'Description': 'Left padding count of the incrementor. Required. Must be between 0 and 25.', 'Required': True}]}, 'ResponseStatus': 200, 'ResponseBody': {'Sample': '{\r\n  "ID": "",\r\n  "Name": "",\r\n  "LastNumber": 0,\r\n  "LeftPaddingCount": 0\r\n}', 'Fields': [{'Name': 'ID', 'Type': 'string', 'Description': 'ID of the incrementor.', 'Required': False}, {'Name': 'Name', 'Type': 'string', 'Description': 'Name of the incrementor.', 'Required': False}, {'Name': 'LastNumber', 'Type': 'integer', 'Description': 'Last number of the incrementor.', 'Required': True}, {'Name': 'LeftPaddingCount', 'Type': 'integer', 'Description': 'Left padding count of the incrementor.', 'Required': True}]}, 'Roles': ['FullAccess', 'IncrementorAdmin']}]