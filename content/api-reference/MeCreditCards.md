---
title: Credit Cards
date: 2018-03-19 18:56:07
category: content\api-reference
tags: MeAndMyStuff
slug: MeCreditCards
---
[{'ID': 'CreateCreditCard', 'Name': 'Create a new credit card', 'Comments': ['Only available to Buyer Users.'], 'HttpVerb': 'POST', 'UriTemplate': 'v1/me/creditcards', 'Parameters': [], 'RequestBody': {'Sample': '{\r\n  "Token": "",\r\n  "CardType": "",\r\n  "PartialAccountNumber": "",\r\n  "CardholderName": "",\r\n  "ExpirationDate": "2018-03-20T05:00:00+00:00",\r\n  "xp": {}\r\n}', 'Fields': [{'Name': 'Token', 'Type': 'string', 'Description': 'Token of the credit card.', 'Required': False}, {'Name': 'CardType', 'Type': 'string', 'Description': 'Card type of the credit card. Searchable: priority level 3. Sortable: priority level 3.', 'Required': False}, {'Name': 'PartialAccountNumber', 'Type': 'string', 'Description': 'Partial account number of the credit card. Max length 5 characters.', 'Required': False}, {'Name': 'CardholderName', 'Type': 'string', 'Description': 'Cardholder name of the credit card. Searchable: priority level 2. Sortable: priority level 2.', 'Required': False}, {'Name': 'ExpirationDate', 'Type': 'date', 'Description': 'Expiration date of the credit card. Searchable: priority level 4. Sortable: priority level 4.', 'Required': False}, {'Name': 'xp', 'Type': 'object', 'Description': 'Container for extended (custom) properties of the credit card.', 'Required': False}]}, 'ResponseStatus': 201, 'ResponseBody': {'Sample': '{\r\n  "ID": "",\r\n  "Editable": false,\r\n  "Token": "",\r\n  "DateCreated": "2018-03-20T05:00:00+00:00",\r\n  "CardType": "",\r\n  "PartialAccountNumber": "",\r\n  "CardholderName": "",\r\n  "ExpirationDate": "2018-03-20T05:00:00+00:00",\r\n  "xp": {}\r\n}', 'Fields': [{'Name': 'ID', 'Type': 'string', 'Description': 'ID of the credit card.', 'Required': False}, {'Name': 'Editable', 'Type': 'boolean', 'Description': 'Editable of the credit card.', 'Required': False}, {'Name': 'Token', 'Type': 'string', 'Description': 'Token of the credit card.', 'Required': False}, {'Name': 'DateCreated', 'Type': 'date', 'Description': 'Date created of the credit card.', 'Required': False}, {'Name': 'CardType', 'Type': 'string', 'Description': 'Card type of the credit card.', 'Required': False}, {'Name': 'PartialAccountNumber', 'Type': 'string', 'Description': 'Partial account number of the credit card.', 'Required': False}, {'Name': 'CardholderName', 'Type': 'string', 'Description': 'Cardholder name of the credit card.', 'Required': False}, {'Name': 'ExpirationDate', 'Type': 'date', 'Description': 'Expiration date of the credit card.', 'Required': False}, {'Name': 'xp', 'Type': 'object', 'Description': 'Container for extended (custom) properties of the credit card.', 'Required': False}]}, 'Roles': ['FullAccess', 'MeCreditCardAdmin']}, {'ID': 'ListCreditCards', 'Name': 'Get a list of credit cards visible to this user', 'Comments': ['Only available to Buyer Users.'], 'HttpVerb': 'GET', 'UriTemplate': 'v1/me/creditcards', 'Parameters': [{'Name': 'search', 'Type': 'string', 'Description': 'Word or phrase to search for.', 'Required': False}, {'Name': 'searchOn', 'Type': 'string', 'Description': 'Comma-delimited list of fields to search on.', 'Required': False}, {'Name': 'sortBy', 'Type': 'string', 'Description': 'Comma-delimited list of fields to sort by.', 'Required': False}, {'Name': 'page', 'Type': 'integer', 'Description': 'Page of results to return. Default: 1', 'Required': False}, {'Name': 'pageSize', 'Type': 'integer', 'Description': 'Number of results to return per page. Default: 20, max: 100.', 'Required': False}, {'Name': 'filters', 'Type': 'object', 'Description': "Any additional key/value pairs passed in the query string are interpretted as filters. Valid keys are top-level properties of the returned model or 'xp.???'", 'Required': False}], 'RequestBody': None, 'ResponseStatus': 200, 'ResponseBody': {'Sample': '{\r\n  "Meta": {\r\n    "Page": 1,\r\n    "PageSize": 20,\r\n    "TotalCount": 25,\r\n    "TotalPages": 2,\r\n    "ItemRange": [\r\n      1,\r\n      20\r\n    ]\r\n  },\r\n  "Items": [\r\n    {\r\n      "ID": "",\r\n      "Editable": false,\r\n      "Token": "",\r\n      "DateCreated": "2018-03-20T05:00:00+00:00",\r\n      "CardType": "",\r\n      "PartialAccountNumber": "",\r\n      "CardholderName": "",\r\n      "ExpirationDate": "2018-03-20T05:00:00+00:00",\r\n      "xp": {}\r\n    }\r\n  ]\r\n}', 'Fields': [{'Name': 'ID', 'Type': 'string', 'Description': 'ID of the credit card.', 'Required': False}, {'Name': 'Editable', 'Type': 'boolean', 'Description': 'Editable of the credit card.', 'Required': False}, {'Name': 'Token', 'Type': 'string', 'Description': 'Token of the credit card.', 'Required': False}, {'Name': 'DateCreated', 'Type': 'date', 'Description': 'Date created of the credit card.', 'Required': False}, {'Name': 'CardType', 'Type': 'string', 'Description': 'Card type of the credit card.', 'Required': False}, {'Name': 'PartialAccountNumber', 'Type': 'string', 'Description': 'Partial account number of the credit card.', 'Required': False}, {'Name': 'CardholderName', 'Type': 'string', 'Description': 'Cardholder name of the credit card.', 'Required': False}, {'Name': 'ExpirationDate', 'Type': 'date', 'Description': 'Expiration date of the credit card.', 'Required': False}, {'Name': 'xp', 'Type': 'object', 'Description': 'Container for extended (custom) properties of the credit card.', 'Required': False}]}, 'Roles': ['FullAccess', 'MeCreditCardAdmin', 'Shopper']}, {'ID': 'GetCreditCard', 'Name': 'Get a single credit card', 'Comments': ['Only available to Buyer Users.'], 'HttpVerb': 'GET', 'UriTemplate': 'v1/me/creditcards/{creditcardID}', 'Parameters': [{'Name': 'creditcardID', 'Type': 'string', 'Description': 'ID of the creditcard.', 'Required': True}], 'RequestBody': None, 'ResponseStatus': 200, 'ResponseBody': {'Sample': '{\r\n  "ID": "",\r\n  "Editable": false,\r\n  "Token": "",\r\n  "DateCreated": "2018-03-20T05:00:00+00:00",\r\n  "CardType": "",\r\n  "PartialAccountNumber": "",\r\n  "CardholderName": "",\r\n  "ExpirationDate": "2018-03-20T05:00:00+00:00",\r\n  "xp": {}\r\n}', 'Fields': [{'Name': 'ID', 'Type': 'string', 'Description': 'ID of the credit card.', 'Required': False}, {'Name': 'Editable', 'Type': 'boolean', 'Description': 'Editable of the credit card.', 'Required': False}, {'Name': 'Token', 'Type': 'string', 'Description': 'Token of the credit card.', 'Required': False}, {'Name': 'DateCreated', 'Type': 'date', 'Description': 'Date created of the credit card.', 'Required': False}, {'Name': 'CardType', 'Type': 'string', 'Description': 'Card type of the credit card.', 'Required': False}, {'Name': 'PartialAccountNumber', 'Type': 'string', 'Description': 'Partial account number of the credit card.', 'Required': False}, {'Name': 'CardholderName', 'Type': 'string', 'Description': 'Cardholder name of the credit card.', 'Required': False}, {'Name': 'ExpirationDate', 'Type': 'date', 'Description': 'Expiration date of the credit card.', 'Required': False}, {'Name': 'xp', 'Type': 'object', 'Description': 'Container for extended (custom) properties of the credit card.', 'Required': False}]}, 'Roles': ['FullAccess', 'MeCreditCardAdmin', 'Shopper']}, {'ID': 'UpdateCreditCard', 'Name': 'Create or update a credit card', 'Comments': ['Only available to Buyer Users.'], 'HttpVerb': 'PUT', 'UriTemplate': 'v1/me/creditcards/{creditcardID}', 'Parameters': [{'Name': 'creditcardID', 'Type': 'string', 'Description': 'ID of the creditcard.', 'Required': True}], 'RequestBody': {'Sample': '{\r\n  "Token": "",\r\n  "CardType": "",\r\n  "PartialAccountNumber": "",\r\n  "CardholderName": "",\r\n  "ExpirationDate": "2018-03-20T05:00:00+00:00",\r\n  "xp": {}\r\n}', 'Fields': [{'Name': 'Token', 'Type': 'string', 'Description': 'Token of the credit card.', 'Required': False}, {'Name': 'CardType', 'Type': 'string', 'Description': 'Card type of the credit card. Searchable: priority level 3. Sortable: priority level 3.', 'Required': False}, {'Name': 'PartialAccountNumber', 'Type': 'string', 'Description': 'Partial account number of the credit card. Max length 5 characters.', 'Required': False}, {'Name': 'CardholderName', 'Type': 'string', 'Description': 'Cardholder name of the credit card. Searchable: priority level 2. Sortable: priority level 2.', 'Required': False}, {'Name': 'ExpirationDate', 'Type': 'date', 'Description': 'Expiration date of the credit card. Searchable: priority level 4. Sortable: priority level 4.', 'Required': False}, {'Name': 'xp', 'Type': 'object', 'Description': 'Container for extended (custom) properties of the credit card.', 'Required': False}]}, 'ResponseStatus': 200, 'ResponseBody': {'Sample': '{\r\n  "ID": "",\r\n  "Editable": false,\r\n  "Token": "",\r\n  "DateCreated": "2018-03-20T05:00:00+00:00",\r\n  "CardType": "",\r\n  "PartialAccountNumber": "",\r\n  "CardholderName": "",\r\n  "ExpirationDate": "2018-03-20T05:00:00+00:00",\r\n  "xp": {}\r\n}', 'Fields': [{'Name': 'ID', 'Type': 'string', 'Description': 'ID of the credit card.', 'Required': False}, {'Name': 'Editable', 'Type': 'boolean', 'Description': 'Editable of the credit card.', 'Required': False}, {'Name': 'Token', 'Type': 'string', 'Description': 'Token of the credit card.', 'Required': False}, {'Name': 'DateCreated', 'Type': 'date', 'Description': 'Date created of the credit card.', 'Required': False}, {'Name': 'CardType', 'Type': 'string', 'Description': 'Card type of the credit card.', 'Required': False}, {'Name': 'PartialAccountNumber', 'Type': 'string', 'Description': 'Partial account number of the credit card.', 'Required': False}, {'Name': 'CardholderName', 'Type': 'string', 'Description': 'Cardholder name of the credit card.', 'Required': False}, {'Name': 'ExpirationDate', 'Type': 'date', 'Description': 'Expiration date of the credit card.', 'Required': False}, {'Name': 'xp', 'Type': 'object', 'Description': 'Container for extended (custom) properties of the credit card.', 'Required': False}]}, 'Roles': ['FullAccess', 'MeCreditCardAdmin']}, {'ID': 'PatchCreditCard', 'Name': 'Partially update a credit card', 'Comments': ['Only available to Buyer Users.'], 'HttpVerb': 'PATCH', 'UriTemplate': 'v1/me/creditcards/{creditcardID}', 'Parameters': [{'Name': 'creditcardID', 'Type': 'string', 'Description': 'ID of the creditcard.', 'Required': True}], 'RequestBody': {'Sample': '{\r\n  "Token": "",\r\n  "CardType": "",\r\n  "PartialAccountNumber": "",\r\n  "CardholderName": "",\r\n  "ExpirationDate": "2018-03-20T05:00:00+00:00",\r\n  "xp": {}\r\n}', 'Fields': [{'Name': 'Token', 'Type': 'string', 'Description': 'Token of the credit card.', 'Required': False}, {'Name': 'CardType', 'Type': 'string', 'Description': 'Card type of the credit card. Searchable: priority level 3. Sortable: priority level 3.', 'Required': False}, {'Name': 'PartialAccountNumber', 'Type': 'string', 'Description': 'Partial account number of the credit card. Max length 5 characters.', 'Required': False}, {'Name': 'CardholderName', 'Type': 'string', 'Description': 'Cardholder name of the credit card. Searchable: priority level 2. Sortable: priority level 2.', 'Required': False}, {'Name': 'ExpirationDate', 'Type': 'date', 'Description': 'Expiration date of the credit card. Searchable: priority level 4. Sortable: priority level 4.', 'Required': False}, {'Name': 'xp', 'Type': 'object', 'Description': 'Container for extended (custom) properties of the credit card.', 'Required': False}]}, 'ResponseStatus': 204, 'ResponseBody': None, 'Roles': ['FullAccess', 'MeCreditCardAdmin']}, {'ID': 'DeleteCreditCard', 'Name': 'Delete a credit card', 'Comments': ['Only available to Buyer Users.'], 'HttpVerb': 'DELETE', 'UriTemplate': 'v1/me/creditcards/{creditcardID}', 'Parameters': [{'Name': 'creditcardID', 'Type': 'string', 'Description': 'ID of the creditcard.', 'Required': True}], 'RequestBody': None, 'ResponseStatus': 204, 'ResponseBody': None, 'Roles': ['FullAccess', 'MeCreditCardAdmin']}]