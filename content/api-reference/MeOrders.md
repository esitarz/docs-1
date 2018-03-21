---
title: Orders
date: 2018-03-19 18:56:07
category: content\api-reference
tags: MeAndMyStuff
slug: MeOrders
---
[{'ID': 'ListOrders', 'Name': 'Get a list of orders visible to this user', 'Comments': ['List orders created by this user.'], 'HttpVerb': 'GET', 'UriTemplate': 'v1/me/orders', 'Parameters': [{'Name': 'from', 'Type': 'date', 'Description': 'Lower bound of date range that the order was created (if outgoing) or submitted (if incoming).', 'Required': False}, {'Name': 'to', 'Type': 'date', 'Description': 'Upper bound of date range that the order was created (if outgoing) or submitted (if incoming).', 'Required': False}, {'Name': 'search', 'Type': 'string', 'Description': 'Word or phrase to search for.', 'Required': False}, {'Name': 'searchOn', 'Type': 'string', 'Description': 'Comma-delimited list of fields to search on.', 'Required': False}, {'Name': 'sortBy', 'Type': 'string', 'Description': 'Comma-delimited list of fields to sort by.', 'Required': False}, {'Name': 'page', 'Type': 'integer', 'Description': 'Page of results to return. Default: 1', 'Required': False}, {'Name': 'pageSize', 'Type': 'integer', 'Description': 'Number of results to return per page. Default: 20, max: 100.', 'Required': False}, {'Name': 'filters', 'Type': 'object', 'Description': "Any additional key/value pairs passed in the query string are interpretted as filters. Valid keys are top-level properties of the returned model or 'xp.???'", 'Required': False}], 'RequestBody': None, 'ResponseStatus': 200, 'ResponseBody': {'Sample': '{\r\n  "Meta": {\r\n    "Page": 1,\r\n    "PageSize": 20,\r\n    "TotalCount": 25,\r\n    "TotalPages": 2,\r\n    "ItemRange": [\r\n      1,\r\n      20\r\n    ]\r\n  },\r\n  "Items": [\r\n    {\r\n      "ID": "",\r\n      "FromUser": {\r\n        "ID": "",\r\n        "Username": "",\r\n        "FirstName": "",\r\n        "LastName": "",\r\n        "Email": "",\r\n        "Phone": "",\r\n        "TermsAccepted": "2018-03-20T05:00:00+00:00",\r\n        "Active": false,\r\n        "xp": {},\r\n        "AvailableRoles": [\r\n          ""\r\n        ]\r\n      },\r\n      "FromCompanyID": "",\r\n      "FromUserID": "",\r\n      "BillingAddressID": "",\r\n      "BillingAddress": {\r\n        "ID": "",\r\n        "CompanyName": "",\r\n        "FirstName": "",\r\n        "LastName": "",\r\n        "Street1": "",\r\n        "Street2": "",\r\n        "City": "",\r\n        "State": "",\r\n        "Zip": "",\r\n        "Country": "",\r\n        "Phone": "",\r\n        "AddressName": "",\r\n        "xp": {}\r\n      },\r\n      "ShippingAddressID": "",\r\n      "Comments": "",\r\n      "LineItemCount": 0,\r\n      "Status": "Unsubmitted",\r\n      "DateCreated": "2018-03-20T05:00:00+00:00",\r\n      "DateSubmitted": "2018-03-20T05:00:00+00:00",\r\n      "DateApproved": "2018-03-20T05:00:00+00:00",\r\n      "DateDeclined": "2018-03-20T05:00:00+00:00",\r\n      "DateCanceled": "2018-03-20T05:00:00+00:00",\r\n      "DateCompleted": "2018-03-20T05:00:00+00:00",\r\n      "Subtotal": 0,\r\n      "ShippingCost": 0,\r\n      "TaxCost": 0,\r\n      "PromotionDiscount": 0,\r\n      "Total": 0,\r\n      "IsSubmitted": false,\r\n      "xp": {}\r\n    }\r\n  ]\r\n}', 'Fields': [{'Name': 'ID', 'Type': 'string', 'Description': 'ID of the order.', 'Required': False}, {'Name': 'FromUser', 'Type': 'object', 'Description': 'From user of the order.', 'Required': False}, {'Name': 'FromCompanyID', 'Type': 'string', 'Description': 'ID of the from company.', 'Required': False}, {'Name': 'FromUserID', 'Type': 'string', 'Description': 'ID of the from user.', 'Required': False}, {'Name': 'BillingAddressID', 'Type': 'string', 'Description': 'ID of the billing address.', 'Required': False}, {'Name': 'BillingAddress', 'Type': 'object', 'Description': 'Billing address of the order.', 'Required': False}, {'Name': 'ShippingAddressID', 'Type': 'string', 'Description': 'ID of the Shipping Address for all LineItems on the Order. Null when there are multiple Shipping Addresses involved.', 'Required': False}, {'Name': 'Comments', 'Type': 'string', 'Description': 'Comments of the order.', 'Required': False}, {'Name': 'LineItemCount', 'Type': 'integer', 'Description': 'Line item count of the order.', 'Required': False}, {'Name': 'Status', 'Type': 'string', 'Description': 'Status of the order. Possible values: Unsubmitted, AwaitingApproval, Declined, Open, Completed, Canceled.', 'Required': False}, {'Name': 'DateCreated', 'Type': 'date', 'Description': 'Date created of the order.', 'Required': False}, {'Name': 'DateSubmitted', 'Type': 'date', 'Description': 'Date submitted of the order.', 'Required': False}, {'Name': 'DateApproved', 'Type': 'date', 'Description': 'Date approved of the order.', 'Required': False}, {'Name': 'DateDeclined', 'Type': 'date', 'Description': 'Date declined of the order.', 'Required': False}, {'Name': 'DateCanceled', 'Type': 'date', 'Description': 'Date canceled of the order.', 'Required': False}, {'Name': 'DateCompleted', 'Type': 'date', 'Description': 'Date completed of the order.', 'Required': False}, {'Name': 'Subtotal', 'Type': 'float', 'Description': 'Subtotal of the order.', 'Required': False}, {'Name': 'ShippingCost', 'Type': 'float', 'Description': 'Shipping cost of the order.', 'Required': False}, {'Name': 'TaxCost', 'Type': 'float', 'Description': 'Tax cost of the order.', 'Required': False}, {'Name': 'PromotionDiscount', 'Type': 'float', 'Description': 'Promotion discount of the order.', 'Required': False}, {'Name': 'Total', 'Type': 'float', 'Description': 'Total of the order.', 'Required': False}, {'Name': 'IsSubmitted', 'Type': 'boolean', 'Description': 'True if this Order has been passed from the Buyer to the Seller.', 'Required': False}, {'Name': 'xp', 'Type': 'object', 'Description': 'Container for extended (custom) properties of the order.', 'Required': False}]}, 'Roles': ['FullAccess', 'Shopper']}, {'ID': 'ListApprovableOrders', 'Name': 'Get a list of orders that this user can approve', 'Comments': [], 'HttpVerb': 'GET', 'UriTemplate': 'v1/me/orders/approvable', 'Parameters': [{'Name': 'from', 'Type': 'date', 'Description': 'Lower bound of date range that the order was created (if outgoing) or submitted (if incoming).', 'Required': False}, {'Name': 'to', 'Type': 'date', 'Description': 'Upper bound of date range that the order was created (if outgoing) or submitted (if incoming).', 'Required': False}, {'Name': 'search', 'Type': 'string', 'Description': 'Word or phrase to search for.', 'Required': False}, {'Name': 'searchOn', 'Type': 'string', 'Description': 'Comma-delimited list of fields to search on.', 'Required': False}, {'Name': 'sortBy', 'Type': 'string', 'Description': 'Comma-delimited list of fields to sort by.', 'Required': False}, {'Name': 'page', 'Type': 'integer', 'Description': 'Page of results to return. Default: 1', 'Required': False}, {'Name': 'pageSize', 'Type': 'integer', 'Description': 'Number of results to return per page. Default: 20, max: 100.', 'Required': False}, {'Name': 'filters', 'Type': 'object', 'Description': "Any additional key/value pairs passed in the query string are interpretted as filters. Valid keys are top-level properties of the returned model or 'xp.???'", 'Required': False}], 'RequestBody': None, 'ResponseStatus': 200, 'ResponseBody': {'Sample': '{\r\n  "Meta": {\r\n    "Page": 1,\r\n    "PageSize": 20,\r\n    "TotalCount": 25,\r\n    "TotalPages": 2,\r\n    "ItemRange": [\r\n      1,\r\n      20\r\n    ]\r\n  },\r\n  "Items": [\r\n    {\r\n      "ID": "",\r\n      "FromUser": {\r\n        "ID": "",\r\n        "Username": "",\r\n        "FirstName": "",\r\n        "LastName": "",\r\n        "Email": "",\r\n        "Phone": "",\r\n        "TermsAccepted": "2018-03-20T05:00:00+00:00",\r\n        "Active": false,\r\n        "xp": {},\r\n        "AvailableRoles": [\r\n          ""\r\n        ]\r\n      },\r\n      "FromCompanyID": "",\r\n      "FromUserID": "",\r\n      "BillingAddressID": "",\r\n      "BillingAddress": {\r\n        "ID": "",\r\n        "CompanyName": "",\r\n        "FirstName": "",\r\n        "LastName": "",\r\n        "Street1": "",\r\n        "Street2": "",\r\n        "City": "",\r\n        "State": "",\r\n        "Zip": "",\r\n        "Country": "",\r\n        "Phone": "",\r\n        "AddressName": "",\r\n        "xp": {}\r\n      },\r\n      "ShippingAddressID": "",\r\n      "Comments": "",\r\n      "LineItemCount": 0,\r\n      "Status": "Unsubmitted",\r\n      "DateCreated": "2018-03-20T05:00:00+00:00",\r\n      "DateSubmitted": "2018-03-20T05:00:00+00:00",\r\n      "DateApproved": "2018-03-20T05:00:00+00:00",\r\n      "DateDeclined": "2018-03-20T05:00:00+00:00",\r\n      "DateCanceled": "2018-03-20T05:00:00+00:00",\r\n      "DateCompleted": "2018-03-20T05:00:00+00:00",\r\n      "Subtotal": 0,\r\n      "ShippingCost": 0,\r\n      "TaxCost": 0,\r\n      "PromotionDiscount": 0,\r\n      "Total": 0,\r\n      "IsSubmitted": false,\r\n      "xp": {}\r\n    }\r\n  ]\r\n}', 'Fields': [{'Name': 'ID', 'Type': 'string', 'Description': 'ID of the order.', 'Required': False}, {'Name': 'FromUser', 'Type': 'object', 'Description': 'From user of the order.', 'Required': False}, {'Name': 'FromCompanyID', 'Type': 'string', 'Description': 'ID of the from company.', 'Required': False}, {'Name': 'FromUserID', 'Type': 'string', 'Description': 'ID of the from user.', 'Required': False}, {'Name': 'BillingAddressID', 'Type': 'string', 'Description': 'ID of the billing address.', 'Required': False}, {'Name': 'BillingAddress', 'Type': 'object', 'Description': 'Billing address of the order.', 'Required': False}, {'Name': 'ShippingAddressID', 'Type': 'string', 'Description': 'ID of the Shipping Address for all LineItems on the Order. Null when there are multiple Shipping Addresses involved.', 'Required': False}, {'Name': 'Comments', 'Type': 'string', 'Description': 'Comments of the order.', 'Required': False}, {'Name': 'LineItemCount', 'Type': 'integer', 'Description': 'Line item count of the order.', 'Required': False}, {'Name': 'Status', 'Type': 'string', 'Description': 'Status of the order. Possible values: Unsubmitted, AwaitingApproval, Declined, Open, Completed, Canceled.', 'Required': False}, {'Name': 'DateCreated', 'Type': 'date', 'Description': 'Date created of the order.', 'Required': False}, {'Name': 'DateSubmitted', 'Type': 'date', 'Description': 'Date submitted of the order.', 'Required': False}, {'Name': 'DateApproved', 'Type': 'date', 'Description': 'Date approved of the order.', 'Required': False}, {'Name': 'DateDeclined', 'Type': 'date', 'Description': 'Date declined of the order.', 'Required': False}, {'Name': 'DateCanceled', 'Type': 'date', 'Description': 'Date canceled of the order.', 'Required': False}, {'Name': 'DateCompleted', 'Type': 'date', 'Description': 'Date completed of the order.', 'Required': False}, {'Name': 'Subtotal', 'Type': 'float', 'Description': 'Subtotal of the order.', 'Required': False}, {'Name': 'ShippingCost', 'Type': 'float', 'Description': 'Shipping cost of the order.', 'Required': False}, {'Name': 'TaxCost', 'Type': 'float', 'Description': 'Tax cost of the order.', 'Required': False}, {'Name': 'PromotionDiscount', 'Type': 'float', 'Description': 'Promotion discount of the order.', 'Required': False}, {'Name': 'Total', 'Type': 'float', 'Description': 'Total of the order.', 'Required': False}, {'Name': 'IsSubmitted', 'Type': 'boolean', 'Description': 'True if this Order has been passed from the Buyer to the Seller.', 'Required': False}, {'Name': 'xp', 'Type': 'object', 'Description': 'Container for extended (custom) properties of the order.', 'Required': False}]}, 'Roles': ['FullAccess', 'Shopper']}]