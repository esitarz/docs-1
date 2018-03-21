---
title: Shipments
date: 2018-03-19 18:56:07
category: content\api-reference
tags: OrdersAndFulfillment
slug: Shipments
---
[{'ID': 'Get', 'Name': 'Get a single shipment', 'Comments': [], 'HttpVerb': 'GET', 'UriTemplate': 'v1/shipments/{shipmentID}', 'Parameters': [{'Name': 'shipmentID', 'Type': 'string', 'Description': 'ID of the shipment.', 'Required': True}], 'RequestBody': None, 'ResponseStatus': 200, 'ResponseBody': {'Sample': '{\r\n  "ID": "",\r\n  "BuyerID": "",\r\n  "Shipper": "",\r\n  "DateShipped": "2018-03-20T05:00:00+00:00",\r\n  "DateDelivered": "2018-03-20T05:00:00+00:00",\r\n  "TrackingNumber": "",\r\n  "Cost": 0,\r\n  "xp": {},\r\n  "Account": "",\r\n  "FromAddressID": "",\r\n  "ToAddressID": "",\r\n  "FromAddress": {\r\n    "ID": "",\r\n    "CompanyName": "",\r\n    "FirstName": "",\r\n    "LastName": "",\r\n    "Street1": "",\r\n    "Street2": "",\r\n    "City": "",\r\n    "State": "",\r\n    "Zip": "",\r\n    "Country": "",\r\n    "Phone": "",\r\n    "AddressName": "",\r\n    "xp": {}\r\n  },\r\n  "ToAddress": {\r\n    "ID": "",\r\n    "CompanyName": "",\r\n    "FirstName": "",\r\n    "LastName": "",\r\n    "Street1": "",\r\n    "Street2": "",\r\n    "City": "",\r\n    "State": "",\r\n    "Zip": "",\r\n    "Country": "",\r\n    "Phone": "",\r\n    "AddressName": "",\r\n    "xp": {}\r\n  }\r\n}', 'Fields': [{'Name': 'ID', 'Type': 'string', 'Description': 'ID of the shipment.', 'Required': False}, {'Name': 'BuyerID', 'Type': 'string', 'Description': 'ID of the buyer.', 'Required': False}, {'Name': 'Shipper', 'Type': 'string', 'Description': 'Shipper of the shipment.', 'Required': False}, {'Name': 'DateShipped', 'Type': 'date', 'Description': 'Date shipped of the shipment.', 'Required': False}, {'Name': 'DateDelivered', 'Type': 'date', 'Description': 'Date delivered of the shipment.', 'Required': False}, {'Name': 'TrackingNumber', 'Type': 'string', 'Description': 'Tracking number of the shipment.', 'Required': False}, {'Name': 'Cost', 'Type': 'float', 'Description': 'Cost of the shipment.', 'Required': False}, {'Name': 'xp', 'Type': 'object', 'Description': 'Container for extended (custom) properties of the shipment.', 'Required': False}, {'Name': 'Account', 'Type': 'string', 'Description': 'Account of the shipment.', 'Required': False}, {'Name': 'FromAddressID', 'Type': 'string', 'Description': 'ID of the from address.', 'Required': False}, {'Name': 'ToAddressID', 'Type': 'string', 'Description': 'ID of the to address.', 'Required': False}, {'Name': 'FromAddress', 'Type': 'object', 'Description': 'From address of the shipment.', 'Required': False}, {'Name': 'ToAddress', 'Type': 'object', 'Description': 'To address of the shipment.', 'Required': False}]}, 'Roles': ['FullAccess', 'ShipmentAdmin', 'ShipmentReader']}, {'ID': 'List', 'Name': 'Get a list of shipments', 'Comments': [], 'HttpVerb': 'GET', 'UriTemplate': 'v1/shipments', 'Parameters': [{'Name': 'orderID', 'Type': 'string', 'Description': 'ID of the order.', 'Required': False}, {'Name': 'search', 'Type': 'string', 'Description': 'Word or phrase to search for.', 'Required': False}, {'Name': 'searchOn', 'Type': 'string', 'Description': 'Comma-delimited list of fields to search on.', 'Required': False}, {'Name': 'sortBy', 'Type': 'string', 'Description': 'Comma-delimited list of fields to sort by.', 'Required': False}, {'Name': 'page', 'Type': 'integer', 'Description': 'Page of results to return. Default: 1', 'Required': False}, {'Name': 'pageSize', 'Type': 'integer', 'Description': 'Number of results to return per page. Default: 20, max: 100.', 'Required': False}, {'Name': 'filters', 'Type': 'object', 'Description': "Any additional key/value pairs passed in the query string are interpretted as filters. Valid keys are top-level properties of the returned model or 'xp.???'", 'Required': False}], 'RequestBody': None, 'ResponseStatus': 200, 'ResponseBody': {'Sample': '{\r\n  "Meta": {\r\n    "Page": 1,\r\n    "PageSize": 20,\r\n    "TotalCount": 25,\r\n    "TotalPages": 2,\r\n    "ItemRange": [\r\n      1,\r\n      20\r\n    ]\r\n  },\r\n  "Items": [\r\n    {\r\n      "ID": "",\r\n      "BuyerID": "",\r\n      "Shipper": "",\r\n      "DateShipped": "2018-03-20T05:00:00+00:00",\r\n      "DateDelivered": "2018-03-20T05:00:00+00:00",\r\n      "TrackingNumber": "",\r\n      "Cost": 0,\r\n      "xp": {},\r\n      "Account": "",\r\n      "FromAddressID": "",\r\n      "ToAddressID": "",\r\n      "FromAddress": {\r\n        "ID": "",\r\n        "CompanyName": "",\r\n        "FirstName": "",\r\n        "LastName": "",\r\n        "Street1": "",\r\n        "Street2": "",\r\n        "City": "",\r\n        "State": "",\r\n        "Zip": "",\r\n        "Country": "",\r\n        "Phone": "",\r\n        "AddressName": "",\r\n        "xp": {}\r\n      },\r\n      "ToAddress": {\r\n        "ID": "",\r\n        "CompanyName": "",\r\n        "FirstName": "",\r\n        "LastName": "",\r\n        "Street1": "",\r\n        "Street2": "",\r\n        "City": "",\r\n        "State": "",\r\n        "Zip": "",\r\n        "Country": "",\r\n        "Phone": "",\r\n        "AddressName": "",\r\n        "xp": {}\r\n      }\r\n    }\r\n  ]\r\n}', 'Fields': [{'Name': 'ID', 'Type': 'string', 'Description': 'ID of the shipment.', 'Required': False}, {'Name': 'BuyerID', 'Type': 'string', 'Description': 'ID of the buyer.', 'Required': False}, {'Name': 'Shipper', 'Type': 'string', 'Description': 'Shipper of the shipment.', 'Required': False}, {'Name': 'DateShipped', 'Type': 'date', 'Description': 'Date shipped of the shipment.', 'Required': False}, {'Name': 'DateDelivered', 'Type': 'date', 'Description': 'Date delivered of the shipment.', 'Required': False}, {'Name': 'TrackingNumber', 'Type': 'string', 'Description': 'Tracking number of the shipment.', 'Required': False}, {'Name': 'Cost', 'Type': 'float', 'Description': 'Cost of the shipment.', 'Required': False}, {'Name': 'xp', 'Type': 'object', 'Description': 'Container for extended (custom) properties of the shipment.', 'Required': False}, {'Name': 'Account', 'Type': 'string', 'Description': 'Account of the shipment.', 'Required': False}, {'Name': 'FromAddressID', 'Type': 'string', 'Description': 'ID of the from address.', 'Required': False}, {'Name': 'ToAddressID', 'Type': 'string', 'Description': 'ID of the to address.', 'Required': False}, {'Name': 'FromAddress', 'Type': 'object', 'Description': 'From address of the shipment.', 'Required': False}, {'Name': 'ToAddress', 'Type': 'object', 'Description': 'To address of the shipment.', 'Required': False}]}, 'Roles': ['FullAccess', 'ShipmentAdmin', 'ShipmentReader']}, {'ID': 'Create', 'Name': 'Create a new shipment', 'Comments': [], 'HttpVerb': 'POST', 'UriTemplate': 'v1/shipments', 'Parameters': [], 'RequestBody': {'Sample': '{\r\n  "ID": "",\r\n  "BuyerID": "",\r\n  "Shipper": "",\r\n  "DateShipped": "2018-03-20T05:00:00+00:00",\r\n  "DateDelivered": "2018-03-20T05:00:00+00:00",\r\n  "TrackingNumber": "",\r\n  "Cost": 0,\r\n  "xp": {},\r\n  "Account": "",\r\n  "FromAddressID": "",\r\n  "ToAddressID": ""\r\n}', 'Fields': [{'Name': 'ID', 'Type': 'string', 'Description': 'ID of the shipment. Can only contain characters Aa-Zz, 0-9, -, and _. Searchable: priority level 1. Sortable.', 'Required': False}, {'Name': 'BuyerID', 'Type': 'string', 'Description': 'ID of the buyer. Searchable: priority level 1. Sortable.', 'Required': False}, {'Name': 'Shipper', 'Type': 'string', 'Description': 'Shipper of the shipment. Searchable: priority level 2. Sortable.', 'Required': False}, {'Name': 'DateShipped', 'Type': 'date', 'Description': 'Date shipped of the shipment. Searchable: priority level 3. Sortable: priority level 1.', 'Required': False}, {'Name': 'DateDelivered', 'Type': 'date', 'Description': 'Date delivered of the shipment. Searchable: priority level 4. Sortable.', 'Required': False}, {'Name': 'TrackingNumber', 'Type': 'string', 'Description': 'Tracking number of the shipment. Max length 3000 characters. Searchable: priority level 4.', 'Required': False}, {'Name': 'Cost', 'Type': 'float', 'Description': 'Cost of the shipment. Sortable.', 'Required': False}, {'Name': 'xp', 'Type': 'object', 'Description': 'Container for extended (custom) properties of the shipment.', 'Required': False}, {'Name': 'Account', 'Type': 'string', 'Description': 'Account of the shipment.', 'Required': False}, {'Name': 'FromAddressID', 'Type': 'string', 'Description': 'ID of the from address.', 'Required': False}, {'Name': 'ToAddressID', 'Type': 'string', 'Description': 'ID of the to address.', 'Required': False}]}, 'ResponseStatus': 201, 'ResponseBody': {'Sample': '{\r\n  "ID": "",\r\n  "BuyerID": "",\r\n  "Shipper": "",\r\n  "DateShipped": "2018-03-20T05:00:00+00:00",\r\n  "DateDelivered": "2018-03-20T05:00:00+00:00",\r\n  "TrackingNumber": "",\r\n  "Cost": 0,\r\n  "xp": {},\r\n  "Account": "",\r\n  "FromAddressID": "",\r\n  "ToAddressID": "",\r\n  "FromAddress": {\r\n    "ID": "",\r\n    "CompanyName": "",\r\n    "FirstName": "",\r\n    "LastName": "",\r\n    "Street1": "",\r\n    "Street2": "",\r\n    "City": "",\r\n    "State": "",\r\n    "Zip": "",\r\n    "Country": "",\r\n    "Phone": "",\r\n    "AddressName": "",\r\n    "xp": {}\r\n  },\r\n  "ToAddress": {\r\n    "ID": "",\r\n    "CompanyName": "",\r\n    "FirstName": "",\r\n    "LastName": "",\r\n    "Street1": "",\r\n    "Street2": "",\r\n    "City": "",\r\n    "State": "",\r\n    "Zip": "",\r\n    "Country": "",\r\n    "Phone": "",\r\n    "AddressName": "",\r\n    "xp": {}\r\n  }\r\n}', 'Fields': [{'Name': 'ID', 'Type': 'string', 'Description': 'ID of the shipment.', 'Required': False}, {'Name': 'BuyerID', 'Type': 'string', 'Description': 'ID of the buyer.', 'Required': False}, {'Name': 'Shipper', 'Type': 'string', 'Description': 'Shipper of the shipment.', 'Required': False}, {'Name': 'DateShipped', 'Type': 'date', 'Description': 'Date shipped of the shipment.', 'Required': False}, {'Name': 'DateDelivered', 'Type': 'date', 'Description': 'Date delivered of the shipment.', 'Required': False}, {'Name': 'TrackingNumber', 'Type': 'string', 'Description': 'Tracking number of the shipment.', 'Required': False}, {'Name': 'Cost', 'Type': 'float', 'Description': 'Cost of the shipment.', 'Required': False}, {'Name': 'xp', 'Type': 'object', 'Description': 'Container for extended (custom) properties of the shipment.', 'Required': False}, {'Name': 'Account', 'Type': 'string', 'Description': 'Account of the shipment.', 'Required': False}, {'Name': 'FromAddressID', 'Type': 'string', 'Description': 'ID of the from address.', 'Required': False}, {'Name': 'ToAddressID', 'Type': 'string', 'Description': 'ID of the to address.', 'Required': False}, {'Name': 'FromAddress', 'Type': 'object', 'Description': 'From address of the shipment.', 'Required': False}, {'Name': 'ToAddress', 'Type': 'object', 'Description': 'To address of the shipment.', 'Required': False}]}, 'Roles': ['FullAccess', 'ShipmentAdmin']}, {'ID': 'Update', 'Name': 'Create or update a shipment', 'Comments': [], 'HttpVerb': 'PUT', 'UriTemplate': 'v1/shipments/{shipmentID}', 'Parameters': [{'Name': 'shipmentID', 'Type': 'string', 'Description': 'ID of the shipment.', 'Required': True}], 'RequestBody': {'Sample': '{\r\n  "ID": "",\r\n  "BuyerID": "",\r\n  "Shipper": "",\r\n  "DateShipped": "2018-03-20T05:00:00+00:00",\r\n  "DateDelivered": "2018-03-20T05:00:00+00:00",\r\n  "TrackingNumber": "",\r\n  "Cost": 0,\r\n  "xp": {},\r\n  "Account": "",\r\n  "FromAddressID": "",\r\n  "ToAddressID": ""\r\n}', 'Fields': [{'Name': 'ID', 'Type': 'string', 'Description': 'ID of the shipment. Can only contain characters Aa-Zz, 0-9, -, and _. Searchable: priority level 1. Sortable.', 'Required': False}, {'Name': 'BuyerID', 'Type': 'string', 'Description': 'ID of the buyer. Searchable: priority level 1. Sortable.', 'Required': False}, {'Name': 'Shipper', 'Type': 'string', 'Description': 'Shipper of the shipment. Searchable: priority level 2. Sortable.', 'Required': False}, {'Name': 'DateShipped', 'Type': 'date', 'Description': 'Date shipped of the shipment. Searchable: priority level 3. Sortable: priority level 1.', 'Required': False}, {'Name': 'DateDelivered', 'Type': 'date', 'Description': 'Date delivered of the shipment. Searchable: priority level 4. Sortable.', 'Required': False}, {'Name': 'TrackingNumber', 'Type': 'string', 'Description': 'Tracking number of the shipment. Max length 3000 characters. Searchable: priority level 4.', 'Required': False}, {'Name': 'Cost', 'Type': 'float', 'Description': 'Cost of the shipment. Sortable.', 'Required': False}, {'Name': 'xp', 'Type': 'object', 'Description': 'Container for extended (custom) properties of the shipment.', 'Required': False}, {'Name': 'Account', 'Type': 'string', 'Description': 'Account of the shipment.', 'Required': False}, {'Name': 'FromAddressID', 'Type': 'string', 'Description': 'ID of the from address.', 'Required': False}, {'Name': 'ToAddressID', 'Type': 'string', 'Description': 'ID of the to address.', 'Required': False}]}, 'ResponseStatus': 200, 'ResponseBody': {'Sample': '{\r\n  "ID": "",\r\n  "BuyerID": "",\r\n  "Shipper": "",\r\n  "DateShipped": "2018-03-20T05:00:00+00:00",\r\n  "DateDelivered": "2018-03-20T05:00:00+00:00",\r\n  "TrackingNumber": "",\r\n  "Cost": 0,\r\n  "xp": {},\r\n  "Account": "",\r\n  "FromAddressID": "",\r\n  "ToAddressID": "",\r\n  "FromAddress": {\r\n    "ID": "",\r\n    "CompanyName": "",\r\n    "FirstName": "",\r\n    "LastName": "",\r\n    "Street1": "",\r\n    "Street2": "",\r\n    "City": "",\r\n    "State": "",\r\n    "Zip": "",\r\n    "Country": "",\r\n    "Phone": "",\r\n    "AddressName": "",\r\n    "xp": {}\r\n  },\r\n  "ToAddress": {\r\n    "ID": "",\r\n    "CompanyName": "",\r\n    "FirstName": "",\r\n    "LastName": "",\r\n    "Street1": "",\r\n    "Street2": "",\r\n    "City": "",\r\n    "State": "",\r\n    "Zip": "",\r\n    "Country": "",\r\n    "Phone": "",\r\n    "AddressName": "",\r\n    "xp": {}\r\n  }\r\n}', 'Fields': [{'Name': 'ID', 'Type': 'string', 'Description': 'ID of the shipment.', 'Required': False}, {'Name': 'BuyerID', 'Type': 'string', 'Description': 'ID of the buyer.', 'Required': False}, {'Name': 'Shipper', 'Type': 'string', 'Description': 'Shipper of the shipment.', 'Required': False}, {'Name': 'DateShipped', 'Type': 'date', 'Description': 'Date shipped of the shipment.', 'Required': False}, {'Name': 'DateDelivered', 'Type': 'date', 'Description': 'Date delivered of the shipment.', 'Required': False}, {'Name': 'TrackingNumber', 'Type': 'string', 'Description': 'Tracking number of the shipment.', 'Required': False}, {'Name': 'Cost', 'Type': 'float', 'Description': 'Cost of the shipment.', 'Required': False}, {'Name': 'xp', 'Type': 'object', 'Description': 'Container for extended (custom) properties of the shipment.', 'Required': False}, {'Name': 'Account', 'Type': 'string', 'Description': 'Account of the shipment.', 'Required': False}, {'Name': 'FromAddressID', 'Type': 'string', 'Description': 'ID of the from address.', 'Required': False}, {'Name': 'ToAddressID', 'Type': 'string', 'Description': 'ID of the to address.', 'Required': False}, {'Name': 'FromAddress', 'Type': 'object', 'Description': 'From address of the shipment.', 'Required': False}, {'Name': 'ToAddress', 'Type': 'object', 'Description': 'To address of the shipment.', 'Required': False}]}, 'Roles': ['FullAccess', 'ShipmentAdmin']}, {'ID': 'Delete', 'Name': 'Delete a shipment', 'Comments': [], 'HttpVerb': 'DELETE', 'UriTemplate': 'v1/shipments/{shipmentID}', 'Parameters': [{'Name': 'shipmentID', 'Type': 'string', 'Description': 'ID of the shipment.', 'Required': True}], 'RequestBody': None, 'ResponseStatus': 204, 'ResponseBody': None, 'Roles': ['FullAccess', 'ShipmentAdmin']}, {'ID': 'Patch', 'Name': 'Partially update a shipment', 'Comments': [], 'HttpVerb': 'PATCH', 'UriTemplate': 'v1/shipments/{shipmentID}', 'Parameters': [{'Name': 'shipmentID', 'Type': 'string', 'Description': 'ID of the shipment.', 'Required': True}], 'RequestBody': {'Sample': '{\r\n  "ID": "",\r\n  "BuyerID": "",\r\n  "Shipper": "",\r\n  "DateShipped": "2018-03-20T05:00:00+00:00",\r\n  "DateDelivered": "2018-03-20T05:00:00+00:00",\r\n  "TrackingNumber": "",\r\n  "Cost": 0,\r\n  "xp": {},\r\n  "Account": "",\r\n  "FromAddressID": "",\r\n  "ToAddressID": ""\r\n}', 'Fields': [{'Name': 'ID', 'Type': 'string', 'Description': 'ID of the shipment. Can only contain characters Aa-Zz, 0-9, -, and _. Searchable: priority level 1. Sortable.', 'Required': False}, {'Name': 'BuyerID', 'Type': 'string', 'Description': 'ID of the buyer. Searchable: priority level 1. Sortable.', 'Required': False}, {'Name': 'Shipper', 'Type': 'string', 'Description': 'Shipper of the shipment. Searchable: priority level 2. Sortable.', 'Required': False}, {'Name': 'DateShipped', 'Type': 'date', 'Description': 'Date shipped of the shipment. Searchable: priority level 3. Sortable: priority level 1.', 'Required': False}, {'Name': 'DateDelivered', 'Type': 'date', 'Description': 'Date delivered of the shipment. Searchable: priority level 4. Sortable.', 'Required': False}, {'Name': 'TrackingNumber', 'Type': 'string', 'Description': 'Tracking number of the shipment. Max length 3000 characters. Searchable: priority level 4.', 'Required': False}, {'Name': 'Cost', 'Type': 'float', 'Description': 'Cost of the shipment. Sortable.', 'Required': False}, {'Name': 'xp', 'Type': 'object', 'Description': 'Container for extended (custom) properties of the shipment.', 'Required': False}, {'Name': 'Account', 'Type': 'string', 'Description': 'Account of the shipment.', 'Required': False}, {'Name': 'FromAddressID', 'Type': 'string', 'Description': 'ID of the from address.', 'Required': False}, {'Name': 'ToAddressID', 'Type': 'string', 'Description': 'ID of the to address.', 'Required': False}]}, 'ResponseStatus': 200, 'ResponseBody': {'Sample': '{\r\n  "ID": "",\r\n  "BuyerID": "",\r\n  "Shipper": "",\r\n  "DateShipped": "2018-03-20T05:00:00+00:00",\r\n  "DateDelivered": "2018-03-20T05:00:00+00:00",\r\n  "TrackingNumber": "",\r\n  "Cost": 0,\r\n  "xp": {},\r\n  "Account": "",\r\n  "FromAddressID": "",\r\n  "ToAddressID": "",\r\n  "FromAddress": {\r\n    "ID": "",\r\n    "CompanyName": "",\r\n    "FirstName": "",\r\n    "LastName": "",\r\n    "Street1": "",\r\n    "Street2": "",\r\n    "City": "",\r\n    "State": "",\r\n    "Zip": "",\r\n    "Country": "",\r\n    "Phone": "",\r\n    "AddressName": "",\r\n    "xp": {}\r\n  },\r\n  "ToAddress": {\r\n    "ID": "",\r\n    "CompanyName": "",\r\n    "FirstName": "",\r\n    "LastName": "",\r\n    "Street1": "",\r\n    "Street2": "",\r\n    "City": "",\r\n    "State": "",\r\n    "Zip": "",\r\n    "Country": "",\r\n    "Phone": "",\r\n    "AddressName": "",\r\n    "xp": {}\r\n  }\r\n}', 'Fields': [{'Name': 'ID', 'Type': 'string', 'Description': 'ID of the shipment.', 'Required': False}, {'Name': 'BuyerID', 'Type': 'string', 'Description': 'ID of the buyer.', 'Required': False}, {'Name': 'Shipper', 'Type': 'string', 'Description': 'Shipper of the shipment.', 'Required': False}, {'Name': 'DateShipped', 'Type': 'date', 'Description': 'Date shipped of the shipment.', 'Required': False}, {'Name': 'DateDelivered', 'Type': 'date', 'Description': 'Date delivered of the shipment.', 'Required': False}, {'Name': 'TrackingNumber', 'Type': 'string', 'Description': 'Tracking number of the shipment.', 'Required': False}, {'Name': 'Cost', 'Type': 'float', 'Description': 'Cost of the shipment.', 'Required': False}, {'Name': 'xp', 'Type': 'object', 'Description': 'Container for extended (custom) properties of the shipment.', 'Required': False}, {'Name': 'Account', 'Type': 'string', 'Description': 'Account of the shipment.', 'Required': False}, {'Name': 'FromAddressID', 'Type': 'string', 'Description': 'ID of the from address.', 'Required': False}, {'Name': 'ToAddressID', 'Type': 'string', 'Description': 'ID of the to address.', 'Required': False}, {'Name': 'FromAddress', 'Type': 'object', 'Description': 'From address of the shipment.', 'Required': False}, {'Name': 'ToAddress', 'Type': 'object', 'Description': 'To address of the shipment.', 'Required': False}]}, 'Roles': ['FullAccess', 'ShipmentAdmin']}, {'ID': 'ListItems', 'Name': 'Get a list of shipment items', 'Comments': [], 'HttpVerb': 'GET', 'UriTemplate': 'v1/shipments/{shipmentID}/items', 'Parameters': [{'Name': 'shipmentID', 'Type': 'string', 'Description': 'ID of the shipment.', 'Required': True}, {'Name': 'search', 'Type': 'string', 'Description': 'Word or phrase to search for.', 'Required': False}, {'Name': 'searchOn', 'Type': 'string', 'Description': 'Comma-delimited list of fields to search on.', 'Required': False}, {'Name': 'sortBy', 'Type': 'string', 'Description': 'Comma-delimited list of fields to sort by.', 'Required': False}, {'Name': 'page', 'Type': 'integer', 'Description': 'Page of results to return. Default: 1', 'Required': False}, {'Name': 'pageSize', 'Type': 'integer', 'Description': 'Number of results to return per page. Default: 20, max: 100.', 'Required': False}, {'Name': 'filters', 'Type': 'object', 'Description': "Any additional key/value pairs passed in the query string are interpretted as filters. Valid keys are top-level properties of the returned model or 'xp.???'", 'Required': False}], 'RequestBody': None, 'ResponseStatus': 200, 'ResponseBody': {'Sample': '{\r\n  "Meta": {\r\n    "Page": 1,\r\n    "PageSize": 20,\r\n    "TotalCount": 25,\r\n    "TotalPages": 2,\r\n    "ItemRange": [\r\n      1,\r\n      20\r\n    ]\r\n  },\r\n  "Items": [\r\n    {\r\n      "OrderID": "",\r\n      "LineItemID": "",\r\n      "QuantityShipped": 0,\r\n      "UnitPrice": 0,\r\n      "CostCenter": "",\r\n      "DateNeeded": "2018-03-20T05:00:00+00:00",\r\n      "Product": {\r\n        "ID": "",\r\n        "Name": "",\r\n        "Description": "",\r\n        "QuantityMultiplier": 0,\r\n        "ShipWeight": 0,\r\n        "ShipHeight": 0,\r\n        "ShipWidth": 0,\r\n        "ShipLength": 0,\r\n        "xp": {}\r\n      },\r\n      "Specs": [\r\n        {\r\n          "SpecID": "",\r\n          "Name": "",\r\n          "OptionID": "",\r\n          "Value": ""\r\n        }\r\n      ],\r\n      "xp": {}\r\n    }\r\n  ]\r\n}', 'Fields': [{'Name': 'OrderID', 'Type': 'string', 'Description': 'ID of the order.', 'Required': True}, {'Name': 'LineItemID', 'Type': 'string', 'Description': 'ID of the line item.', 'Required': True}, {'Name': 'QuantityShipped', 'Type': 'integer', 'Description': 'Quantity shipped of the shipment item.', 'Required': True}, {'Name': 'UnitPrice', 'Type': 'float', 'Description': 'Unit price of the shipment item.', 'Required': False}, {'Name': 'CostCenter', 'Type': 'string', 'Description': 'Cost center of the shipment item.', 'Required': False}, {'Name': 'DateNeeded', 'Type': 'date', 'Description': 'Date needed of the shipment item.', 'Required': False}, {'Name': 'Product', 'Type': 'object', 'Description': 'Product of the shipment item.', 'Required': False}, {'Name': 'Specs', 'Type': 'array', 'Description': 'Specs of the shipment item.', 'Required': False}, {'Name': 'xp', 'Type': 'object', 'Description': 'Container for extended (custom) properties of the shipment item.', 'Required': False}]}, 'Roles': ['FullAccess', 'ShipmentAdmin', 'ShipmentReader']}, {'ID': 'GetItem', 'Name': 'Get a single shipment item', 'Comments': [], 'HttpVerb': 'GET', 'UriTemplate': 'v1/shipments/{shipmentID}/items/{orderID}/{lineItemID}', 'Parameters': [{'Name': 'shipmentID', 'Type': 'string', 'Description': 'ID of the shipment.', 'Required': True}, {'Name': 'orderID', 'Type': 'string', 'Description': 'ID of the order.', 'Required': True}, {'Name': 'lineItemID', 'Type': 'string', 'Description': 'ID of the line item.', 'Required': True}], 'RequestBody': None, 'ResponseStatus': 200, 'ResponseBody': {'Sample': '{\r\n  "OrderID": "",\r\n  "LineItemID": "",\r\n  "QuantityShipped": 0,\r\n  "UnitPrice": 0,\r\n  "CostCenter": "",\r\n  "DateNeeded": "2018-03-20T05:00:00+00:00",\r\n  "Product": {\r\n    "ID": "",\r\n    "Name": "",\r\n    "Description": "",\r\n    "QuantityMultiplier": 0,\r\n    "ShipWeight": 0,\r\n    "ShipHeight": 0,\r\n    "ShipWidth": 0,\r\n    "ShipLength": 0,\r\n    "xp": {}\r\n  },\r\n  "Specs": [\r\n    {\r\n      "SpecID": "",\r\n      "Name": "",\r\n      "OptionID": "",\r\n      "Value": ""\r\n    }\r\n  ],\r\n  "xp": {}\r\n}', 'Fields': [{'Name': 'OrderID', 'Type': 'string', 'Description': 'ID of the order.', 'Required': True}, {'Name': 'LineItemID', 'Type': 'string', 'Description': 'ID of the line item.', 'Required': True}, {'Name': 'QuantityShipped', 'Type': 'integer', 'Description': 'Quantity shipped of the shipment item.', 'Required': True}, {'Name': 'UnitPrice', 'Type': 'float', 'Description': 'Unit price of the shipment item.', 'Required': False}, {'Name': 'CostCenter', 'Type': 'string', 'Description': 'Cost center of the shipment item.', 'Required': False}, {'Name': 'DateNeeded', 'Type': 'date', 'Description': 'Date needed of the shipment item.', 'Required': False}, {'Name': 'Product', 'Type': 'object', 'Description': 'Product of the shipment item.', 'Required': False}, {'Name': 'Specs', 'Type': 'array', 'Description': 'Specs of the shipment item.', 'Required': False}, {'Name': 'xp', 'Type': 'object', 'Description': 'Container for extended (custom) properties of the shipment item.', 'Required': False}]}, 'Roles': ['FullAccess', 'ShipmentAdmin', 'ShipmentReader']}, {'ID': 'SaveItem', 'Name': 'Save a shipment item', 'Comments': [], 'HttpVerb': 'POST', 'UriTemplate': 'v1/shipments/{shipmentID}/items', 'Parameters': [{'Name': 'shipmentID', 'Type': 'string', 'Description': 'ID of the shipment.', 'Required': True}], 'RequestBody': {'Sample': '{\r\n  "OrderID": "",\r\n  "LineItemID": "",\r\n  "QuantityShipped": 0\r\n}', 'Fields': [{'Name': 'OrderID', 'Type': 'string', 'Description': 'ID of the order. Required.', 'Required': True}, {'Name': 'LineItemID', 'Type': 'string', 'Description': 'ID of the line item. Required.', 'Required': True}, {'Name': 'QuantityShipped', 'Type': 'integer', 'Description': 'Quantity shipped of the shipment item. Required.', 'Required': True}]}, 'ResponseStatus': 200, 'ResponseBody': {'Sample': '{\r\n  "OrderID": "",\r\n  "LineItemID": "",\r\n  "QuantityShipped": 0,\r\n  "UnitPrice": 0,\r\n  "CostCenter": "",\r\n  "DateNeeded": "2018-03-20T05:00:00+00:00",\r\n  "Product": {\r\n    "ID": "",\r\n    "Name": "",\r\n    "Description": "",\r\n    "QuantityMultiplier": 0,\r\n    "ShipWeight": 0,\r\n    "ShipHeight": 0,\r\n    "ShipWidth": 0,\r\n    "ShipLength": 0,\r\n    "xp": {}\r\n  },\r\n  "Specs": [\r\n    {\r\n      "SpecID": "",\r\n      "Name": "",\r\n      "OptionID": "",\r\n      "Value": ""\r\n    }\r\n  ],\r\n  "xp": {}\r\n}', 'Fields': [{'Name': 'OrderID', 'Type': 'string', 'Description': 'ID of the order.', 'Required': True}, {'Name': 'LineItemID', 'Type': 'string', 'Description': 'ID of the line item.', 'Required': True}, {'Name': 'QuantityShipped', 'Type': 'integer', 'Description': 'Quantity shipped of the shipment item.', 'Required': True}, {'Name': 'UnitPrice', 'Type': 'float', 'Description': 'Unit price of the shipment item.', 'Required': False}, {'Name': 'CostCenter', 'Type': 'string', 'Description': 'Cost center of the shipment item.', 'Required': False}, {'Name': 'DateNeeded', 'Type': 'date', 'Description': 'Date needed of the shipment item.', 'Required': False}, {'Name': 'Product', 'Type': 'object', 'Description': 'Product of the shipment item.', 'Required': False}, {'Name': 'Specs', 'Type': 'array', 'Description': 'Specs of the shipment item.', 'Required': False}, {'Name': 'xp', 'Type': 'object', 'Description': 'Container for extended (custom) properties of the shipment item.', 'Required': False}]}, 'Roles': ['FullAccess', 'ShipmentAdmin']}, {'ID': 'DeleteItem', 'Name': 'Delete a shipment item', 'Comments': [], 'HttpVerb': 'DELETE', 'UriTemplate': 'v1/shipments/{shipmentID}/items/{orderID}/{lineItemID}', 'Parameters': [{'Name': 'shipmentID', 'Type': 'string', 'Description': 'ID of the shipment.', 'Required': True}, {'Name': 'orderID', 'Type': 'string', 'Description': 'ID of the order.', 'Required': True}, {'Name': 'lineItemID', 'Type': 'string', 'Description': 'ID of the line item.', 'Required': True}], 'RequestBody': None, 'ResponseStatus': 204, 'ResponseBody': None, 'Roles': ['FullAccess', 'ShipmentAdmin']}]