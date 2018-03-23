---
title: Shipments
date: 2018-03-23
category: API Reference
tags: Orders And Fulfillment
slug: Shipments
---
A Shipment is a grouping of one or more Line Items from one or more
Orders that is physically packaged and delivered to the Buyer as a
single unit. It is typically created by the Seller after the Order is
submitted as part of the fulfillment process.

---

## Get a single shipment
### `GET` `v1/shipments/{shipmentID}`

| Parameters      | Description                    |
|------------------|---------------------------------|
| Name            | shipmentID                     |
| Type            | string                         |
| Description     | ID of the shipment.            |
| Required        | True                           |

 **Requestbody**: 
None
 **Responsestatus**: `200`

 **Responsebody**: 
{'Sample': '{\r\n  "ID": "",\r\n  "BuyerID": "",\r\n  "Shipper": "",\r\n  "DateShipped": "2018-03-21T23:00:00+00:00",\r\n  "DateDelivered": "2018-03-21T23:00:00+00:00",\r\n  "TrackingNumber": "",\r\n  "Cost": 0,\r\n  "xp": {},\r\n  "Account": "",\r\n  "FromAddressID": "",\r\n  "ToAddressID": "",\r\n  "FromAddress": {\r\n    "ID": "",\r\n    "DateCreated": "2018-03-21T23:00:00+00:00",\r\n    "CompanyName": "",\r\n    "FirstName": "",\r\n    "LastName": "",\r\n    "Street1": "",\r\n    "Street2": "",\r\n    "City": "",\r\n    "State": "",\r\n    "Zip": "",\r\n    "Country": "",\r\n    "Phone": "",\r\n    "AddressName": "",\r\n    "xp": {}\r\n  },\r\n  "ToAddress": {\r\n    "ID": "",\r\n    "DateCreated": "2018-03-21T23:00:00+00:00",\r\n    "CompanyName": "",\r\n    "FirstName": "",\r\n    "LastName": "",\r\n    "Street1": "",\r\n    "Street2": "",\r\n    "City": "",\r\n    "State": "",\r\n    "Zip": "",\r\n    "Country": "",\r\n    "Phone": "",\r\n    "AddressName": "",\r\n    "xp": {}\r\n  }\r\n}', 'Fields': [{'Name': 'ID', 'Type': 'string', 'Description': 'ID of the shipment.', 'Required': False}, {'Name': 'BuyerID', 'Type': 'string', 'Description': 'ID of the buyer.', 'Required': False}, {'Name': 'Shipper', 'Type': 'string', 'Description': 'Shipper of the shipment.', 'Required': False}, {'Name': 'DateShipped', 'Type': 'date', 'Description': 'Date shipped of the shipment.', 'Required': False}, {'Name': 'DateDelivered', 'Type': 'date', 'Description': 'Date delivered of the shipment.', 'Required': False}, {'Name': 'TrackingNumber', 'Type': 'string', 'Description': 'Tracking number of the shipment.', 'Required': False}, {'Name': 'Cost', 'Type': 'float', 'Description': 'Cost of the shipment.', 'Required': False}, {'Name': 'xp', 'Type': 'object', 'Description': 'Container for extended (custom) properties of the shipment.', 'Required': False}, {'Name': 'Account', 'Type': 'string', 'Description': 'Account of the shipment.', 'Required': False}, {'Name': 'FromAddressID', 'Type': 'string', 'Description': 'ID of the from address.', 'Required': False}, {'Name': 'ToAddressID', 'Type': 'string', 'Description': 'ID of the to address.', 'Required': False}, {'Name': 'FromAddress', 'Type': 'object', 'Description': 'From address of the shipment.', 'Required': False}, {'Name': 'ToAddress', 'Type': 'object', 'Description': 'To address of the shipment.', 'Required': False}]}
## Get a list of shipments
### `GET` `v1/shipments`

| Parameters      | Description                    |
|------------------|---------------------------------|
| Name            | orderID                        |
| Type            | string                         |
| Description     | ID of the order.               |
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
{'Sample': '{\r\n  "Meta": {\r\n    "Page": 1,\r\n    "PageSize": 20,\r\n    "TotalCount": 25,\r\n    "TotalPages": 2,\r\n    "ItemRange": [\r\n      1,\r\n      20\r\n    ]\r\n  },\r\n  "Items": [\r\n    {\r\n      "ID": "",\r\n      "BuyerID": "",\r\n      "Shipper": "",\r\n      "DateShipped": "2018-03-21T23:00:00+00:00",\r\n      "DateDelivered": "2018-03-21T23:00:00+00:00",\r\n      "TrackingNumber": "",\r\n      "Cost": 0,\r\n      "xp": {},\r\n      "Account": "",\r\n      "FromAddressID": "",\r\n      "ToAddressID": "",\r\n      "FromAddress": {\r\n        "ID": "",\r\n        "DateCreated": "2018-03-21T23:00:00+00:00",\r\n        "CompanyName": "",\r\n        "FirstName": "",\r\n        "LastName": "",\r\n        "Street1": "",\r\n        "Street2": "",\r\n        "City": "",\r\n        "State": "",\r\n        "Zip": "",\r\n        "Country": "",\r\n        "Phone": "",\r\n        "AddressName": "",\r\n        "xp": {}\r\n      },\r\n      "ToAddress": {\r\n        "ID": "",\r\n        "DateCreated": "2018-03-21T23:00:00+00:00",\r\n        "CompanyName": "",\r\n        "FirstName": "",\r\n        "LastName": "",\r\n        "Street1": "",\r\n        "Street2": "",\r\n        "City": "",\r\n        "State": "",\r\n        "Zip": "",\r\n        "Country": "",\r\n        "Phone": "",\r\n        "AddressName": "",\r\n        "xp": {}\r\n      }\r\n    }\r\n  ]\r\n}', 'Fields': [{'Name': 'ID', 'Type': 'string', 'Description': 'ID of the shipment.', 'Required': False}, {'Name': 'BuyerID', 'Type': 'string', 'Description': 'ID of the buyer.', 'Required': False}, {'Name': 'Shipper', 'Type': 'string', 'Description': 'Shipper of the shipment.', 'Required': False}, {'Name': 'DateShipped', 'Type': 'date', 'Description': 'Date shipped of the shipment.', 'Required': False}, {'Name': 'DateDelivered', 'Type': 'date', 'Description': 'Date delivered of the shipment.', 'Required': False}, {'Name': 'TrackingNumber', 'Type': 'string', 'Description': 'Tracking number of the shipment.', 'Required': False}, {'Name': 'Cost', 'Type': 'float', 'Description': 'Cost of the shipment.', 'Required': False}, {'Name': 'xp', 'Type': 'object', 'Description': 'Container for extended (custom) properties of the shipment.', 'Required': False}, {'Name': 'Account', 'Type': 'string', 'Description': 'Account of the shipment.', 'Required': False}, {'Name': 'FromAddressID', 'Type': 'string', 'Description': 'ID of the from address.', 'Required': False}, {'Name': 'ToAddressID', 'Type': 'string', 'Description': 'ID of the to address.', 'Required': False}, {'Name': 'FromAddress', 'Type': 'object', 'Description': 'From address of the shipment.', 'Required': False}, {'Name': 'ToAddress', 'Type': 'object', 'Description': 'To address of the shipment.', 'Required': False}]}
## Create a new shipment
### `POST` `v1/shipments`

| Parameters      | Description                    |
|------------------|---------------------------------|

 **Requestbody**: 
{'Sample': '{\r\n  "ID": "",\r\n  "BuyerID": "",\r\n  "Shipper": "",\r\n  "DateShipped": "2018-03-21T23:00:00+00:00",\r\n  "DateDelivered": "2018-03-21T23:00:00+00:00",\r\n  "TrackingNumber": "",\r\n  "Cost": 0,\r\n  "xp": {},\r\n  "Account": "",\r\n  "FromAddressID": "",\r\n  "ToAddressID": ""\r\n}', 'Fields': [{'Name': 'ID', 'Type': 'string', 'Description': 'ID of the shipment. Can only contain characters Aa-Zz, 0-9, -, and _. Searchable: priority level 1. Sortable.', 'Required': False}, {'Name': 'BuyerID', 'Type': 'string', 'Description': 'ID of the buyer. Searchable: priority level 1. Sortable.', 'Required': False}, {'Name': 'Shipper', 'Type': 'string', 'Description': 'Shipper of the shipment. Searchable: priority level 2. Sortable.', 'Required': False}, {'Name': 'DateShipped', 'Type': 'date', 'Description': 'Date shipped of the shipment. Searchable: priority level 3. Sortable: priority level 1.', 'Required': False}, {'Name': 'DateDelivered', 'Type': 'date', 'Description': 'Date delivered of the shipment. Searchable: priority level 4. Sortable.', 'Required': False}, {'Name': 'TrackingNumber', 'Type': 'string', 'Description': 'Tracking number of the shipment. Max length 3000 characters. Searchable: priority level 4.', 'Required': False}, {'Name': 'Cost', 'Type': 'float', 'Description': 'Cost of the shipment. Sortable.', 'Required': False}, {'Name': 'xp', 'Type': 'object', 'Description': 'Container for extended (custom) properties of the shipment.', 'Required': False}, {'Name': 'Account', 'Type': 'string', 'Description': 'Account of the shipment.', 'Required': False}, {'Name': 'FromAddressID', 'Type': 'string', 'Description': 'ID of the from address.', 'Required': False}, {'Name': 'ToAddressID', 'Type': 'string', 'Description': 'ID of the to address.', 'Required': False}]}
 **Responsestatus**: `201`

 **Responsebody**: 
{'Sample': '{\r\n  "ID": "",\r\n  "BuyerID": "",\r\n  "Shipper": "",\r\n  "DateShipped": "2018-03-21T23:00:00+00:00",\r\n  "DateDelivered": "2018-03-21T23:00:00+00:00",\r\n  "TrackingNumber": "",\r\n  "Cost": 0,\r\n  "xp": {},\r\n  "Account": "",\r\n  "FromAddressID": "",\r\n  "ToAddressID": "",\r\n  "FromAddress": {\r\n    "ID": "",\r\n    "DateCreated": "2018-03-21T23:00:00+00:00",\r\n    "CompanyName": "",\r\n    "FirstName": "",\r\n    "LastName": "",\r\n    "Street1": "",\r\n    "Street2": "",\r\n    "City": "",\r\n    "State": "",\r\n    "Zip": "",\r\n    "Country": "",\r\n    "Phone": "",\r\n    "AddressName": "",\r\n    "xp": {}\r\n  },\r\n  "ToAddress": {\r\n    "ID": "",\r\n    "DateCreated": "2018-03-21T23:00:00+00:00",\r\n    "CompanyName": "",\r\n    "FirstName": "",\r\n    "LastName": "",\r\n    "Street1": "",\r\n    "Street2": "",\r\n    "City": "",\r\n    "State": "",\r\n    "Zip": "",\r\n    "Country": "",\r\n    "Phone": "",\r\n    "AddressName": "",\r\n    "xp": {}\r\n  }\r\n}', 'Fields': [{'Name': 'ID', 'Type': 'string', 'Description': 'ID of the shipment.', 'Required': False}, {'Name': 'BuyerID', 'Type': 'string', 'Description': 'ID of the buyer.', 'Required': False}, {'Name': 'Shipper', 'Type': 'string', 'Description': 'Shipper of the shipment.', 'Required': False}, {'Name': 'DateShipped', 'Type': 'date', 'Description': 'Date shipped of the shipment.', 'Required': False}, {'Name': 'DateDelivered', 'Type': 'date', 'Description': 'Date delivered of the shipment.', 'Required': False}, {'Name': 'TrackingNumber', 'Type': 'string', 'Description': 'Tracking number of the shipment.', 'Required': False}, {'Name': 'Cost', 'Type': 'float', 'Description': 'Cost of the shipment.', 'Required': False}, {'Name': 'xp', 'Type': 'object', 'Description': 'Container for extended (custom) properties of the shipment.', 'Required': False}, {'Name': 'Account', 'Type': 'string', 'Description': 'Account of the shipment.', 'Required': False}, {'Name': 'FromAddressID', 'Type': 'string', 'Description': 'ID of the from address.', 'Required': False}, {'Name': 'ToAddressID', 'Type': 'string', 'Description': 'ID of the to address.', 'Required': False}, {'Name': 'FromAddress', 'Type': 'object', 'Description': 'From address of the shipment.', 'Required': False}, {'Name': 'ToAddress', 'Type': 'object', 'Description': 'To address of the shipment.', 'Required': False}]}
## Create or update a shipment
### `PUT` `v1/shipments/{shipmentID}`

| Parameters      | Description                    |
|------------------|---------------------------------|
| Name            | shipmentID                     |
| Type            | string                         |
| Description     | ID of the shipment.            |
| Required        | True                           |

 **Requestbody**: 
{'Sample': '{\r\n  "ID": "",\r\n  "BuyerID": "",\r\n  "Shipper": "",\r\n  "DateShipped": "2018-03-21T23:00:00+00:00",\r\n  "DateDelivered": "2018-03-21T23:00:00+00:00",\r\n  "TrackingNumber": "",\r\n  "Cost": 0,\r\n  "xp": {},\r\n  "Account": "",\r\n  "FromAddressID": "",\r\n  "ToAddressID": ""\r\n}', 'Fields': [{'Name': 'ID', 'Type': 'string', 'Description': 'ID of the shipment. Can only contain characters Aa-Zz, 0-9, -, and _. Searchable: priority level 1. Sortable.', 'Required': False}, {'Name': 'BuyerID', 'Type': 'string', 'Description': 'ID of the buyer. Searchable: priority level 1. Sortable.', 'Required': False}, {'Name': 'Shipper', 'Type': 'string', 'Description': 'Shipper of the shipment. Searchable: priority level 2. Sortable.', 'Required': False}, {'Name': 'DateShipped', 'Type': 'date', 'Description': 'Date shipped of the shipment. Searchable: priority level 3. Sortable: priority level 1.', 'Required': False}, {'Name': 'DateDelivered', 'Type': 'date', 'Description': 'Date delivered of the shipment. Searchable: priority level 4. Sortable.', 'Required': False}, {'Name': 'TrackingNumber', 'Type': 'string', 'Description': 'Tracking number of the shipment. Max length 3000 characters. Searchable: priority level 4.', 'Required': False}, {'Name': 'Cost', 'Type': 'float', 'Description': 'Cost of the shipment. Sortable.', 'Required': False}, {'Name': 'xp', 'Type': 'object', 'Description': 'Container for extended (custom) properties of the shipment.', 'Required': False}, {'Name': 'Account', 'Type': 'string', 'Description': 'Account of the shipment.', 'Required': False}, {'Name': 'FromAddressID', 'Type': 'string', 'Description': 'ID of the from address.', 'Required': False}, {'Name': 'ToAddressID', 'Type': 'string', 'Description': 'ID of the to address.', 'Required': False}]}
 **Responsestatus**: `200`

 **Responsebody**: 
{'Sample': '{\r\n  "ID": "",\r\n  "BuyerID": "",\r\n  "Shipper": "",\r\n  "DateShipped": "2018-03-21T23:00:00+00:00",\r\n  "DateDelivered": "2018-03-21T23:00:00+00:00",\r\n  "TrackingNumber": "",\r\n  "Cost": 0,\r\n  "xp": {},\r\n  "Account": "",\r\n  "FromAddressID": "",\r\n  "ToAddressID": "",\r\n  "FromAddress": {\r\n    "ID": "",\r\n    "DateCreated": "2018-03-21T23:00:00+00:00",\r\n    "CompanyName": "",\r\n    "FirstName": "",\r\n    "LastName": "",\r\n    "Street1": "",\r\n    "Street2": "",\r\n    "City": "",\r\n    "State": "",\r\n    "Zip": "",\r\n    "Country": "",\r\n    "Phone": "",\r\n    "AddressName": "",\r\n    "xp": {}\r\n  },\r\n  "ToAddress": {\r\n    "ID": "",\r\n    "DateCreated": "2018-03-21T23:00:00+00:00",\r\n    "CompanyName": "",\r\n    "FirstName": "",\r\n    "LastName": "",\r\n    "Street1": "",\r\n    "Street2": "",\r\n    "City": "",\r\n    "State": "",\r\n    "Zip": "",\r\n    "Country": "",\r\n    "Phone": "",\r\n    "AddressName": "",\r\n    "xp": {}\r\n  }\r\n}', 'Fields': [{'Name': 'ID', 'Type': 'string', 'Description': 'ID of the shipment.', 'Required': False}, {'Name': 'BuyerID', 'Type': 'string', 'Description': 'ID of the buyer.', 'Required': False}, {'Name': 'Shipper', 'Type': 'string', 'Description': 'Shipper of the shipment.', 'Required': False}, {'Name': 'DateShipped', 'Type': 'date', 'Description': 'Date shipped of the shipment.', 'Required': False}, {'Name': 'DateDelivered', 'Type': 'date', 'Description': 'Date delivered of the shipment.', 'Required': False}, {'Name': 'TrackingNumber', 'Type': 'string', 'Description': 'Tracking number of the shipment.', 'Required': False}, {'Name': 'Cost', 'Type': 'float', 'Description': 'Cost of the shipment.', 'Required': False}, {'Name': 'xp', 'Type': 'object', 'Description': 'Container for extended (custom) properties of the shipment.', 'Required': False}, {'Name': 'Account', 'Type': 'string', 'Description': 'Account of the shipment.', 'Required': False}, {'Name': 'FromAddressID', 'Type': 'string', 'Description': 'ID of the from address.', 'Required': False}, {'Name': 'ToAddressID', 'Type': 'string', 'Description': 'ID of the to address.', 'Required': False}, {'Name': 'FromAddress', 'Type': 'object', 'Description': 'From address of the shipment.', 'Required': False}, {'Name': 'ToAddress', 'Type': 'object', 'Description': 'To address of the shipment.', 'Required': False}]}
## Delete a shipment
### `DELETE` `v1/shipments/{shipmentID}`

| Parameters      | Description                    |
|------------------|---------------------------------|
| Name            | shipmentID                     |
| Type            | string                         |
| Description     | ID of the shipment.            |
| Required        | True                           |

 **Requestbody**: 
None
 **Responsestatus**: `204`

 **Responsebody**: 
None
## Partially update a shipment
### `PATCH` `v1/shipments/{shipmentID}`

| Parameters      | Description                    |
|------------------|---------------------------------|
| Name            | shipmentID                     |
| Type            | string                         |
| Description     | ID of the shipment.            |
| Required        | True                           |

 **Requestbody**: 
{'Sample': '{\r\n  "ID": "",\r\n  "BuyerID": "",\r\n  "Shipper": "",\r\n  "DateShipped": "2018-03-21T23:00:00+00:00",\r\n  "DateDelivered": "2018-03-21T23:00:00+00:00",\r\n  "TrackingNumber": "",\r\n  "Cost": 0,\r\n  "xp": {},\r\n  "Account": "",\r\n  "FromAddressID": "",\r\n  "ToAddressID": ""\r\n}', 'Fields': [{'Name': 'ID', 'Type': 'string', 'Description': 'ID of the shipment. Can only contain characters Aa-Zz, 0-9, -, and _. Searchable: priority level 1. Sortable.', 'Required': False}, {'Name': 'BuyerID', 'Type': 'string', 'Description': 'ID of the buyer. Searchable: priority level 1. Sortable.', 'Required': False}, {'Name': 'Shipper', 'Type': 'string', 'Description': 'Shipper of the shipment. Searchable: priority level 2. Sortable.', 'Required': False}, {'Name': 'DateShipped', 'Type': 'date', 'Description': 'Date shipped of the shipment. Searchable: priority level 3. Sortable: priority level 1.', 'Required': False}, {'Name': 'DateDelivered', 'Type': 'date', 'Description': 'Date delivered of the shipment. Searchable: priority level 4. Sortable.', 'Required': False}, {'Name': 'TrackingNumber', 'Type': 'string', 'Description': 'Tracking number of the shipment. Max length 3000 characters. Searchable: priority level 4.', 'Required': False}, {'Name': 'Cost', 'Type': 'float', 'Description': 'Cost of the shipment. Sortable.', 'Required': False}, {'Name': 'xp', 'Type': 'object', 'Description': 'Container for extended (custom) properties of the shipment.', 'Required': False}, {'Name': 'Account', 'Type': 'string', 'Description': 'Account of the shipment.', 'Required': False}, {'Name': 'FromAddressID', 'Type': 'string', 'Description': 'ID of the from address.', 'Required': False}, {'Name': 'ToAddressID', 'Type': 'string', 'Description': 'ID of the to address.', 'Required': False}]}
 **Responsestatus**: `200`

 **Responsebody**: 
{'Sample': '{\r\n  "ID": "",\r\n  "BuyerID": "",\r\n  "Shipper": "",\r\n  "DateShipped": "2018-03-21T23:00:00+00:00",\r\n  "DateDelivered": "2018-03-21T23:00:00+00:00",\r\n  "TrackingNumber": "",\r\n  "Cost": 0,\r\n  "xp": {},\r\n  "Account": "",\r\n  "FromAddressID": "",\r\n  "ToAddressID": "",\r\n  "FromAddress": {\r\n    "ID": "",\r\n    "DateCreated": "2018-03-21T23:00:00+00:00",\r\n    "CompanyName": "",\r\n    "FirstName": "",\r\n    "LastName": "",\r\n    "Street1": "",\r\n    "Street2": "",\r\n    "City": "",\r\n    "State": "",\r\n    "Zip": "",\r\n    "Country": "",\r\n    "Phone": "",\r\n    "AddressName": "",\r\n    "xp": {}\r\n  },\r\n  "ToAddress": {\r\n    "ID": "",\r\n    "DateCreated": "2018-03-21T23:00:00+00:00",\r\n    "CompanyName": "",\r\n    "FirstName": "",\r\n    "LastName": "",\r\n    "Street1": "",\r\n    "Street2": "",\r\n    "City": "",\r\n    "State": "",\r\n    "Zip": "",\r\n    "Country": "",\r\n    "Phone": "",\r\n    "AddressName": "",\r\n    "xp": {}\r\n  }\r\n}', 'Fields': [{'Name': 'ID', 'Type': 'string', 'Description': 'ID of the shipment.', 'Required': False}, {'Name': 'BuyerID', 'Type': 'string', 'Description': 'ID of the buyer.', 'Required': False}, {'Name': 'Shipper', 'Type': 'string', 'Description': 'Shipper of the shipment.', 'Required': False}, {'Name': 'DateShipped', 'Type': 'date', 'Description': 'Date shipped of the shipment.', 'Required': False}, {'Name': 'DateDelivered', 'Type': 'date', 'Description': 'Date delivered of the shipment.', 'Required': False}, {'Name': 'TrackingNumber', 'Type': 'string', 'Description': 'Tracking number of the shipment.', 'Required': False}, {'Name': 'Cost', 'Type': 'float', 'Description': 'Cost of the shipment.', 'Required': False}, {'Name': 'xp', 'Type': 'object', 'Description': 'Container for extended (custom) properties of the shipment.', 'Required': False}, {'Name': 'Account', 'Type': 'string', 'Description': 'Account of the shipment.', 'Required': False}, {'Name': 'FromAddressID', 'Type': 'string', 'Description': 'ID of the from address.', 'Required': False}, {'Name': 'ToAddressID', 'Type': 'string', 'Description': 'ID of the to address.', 'Required': False}, {'Name': 'FromAddress', 'Type': 'object', 'Description': 'From address of the shipment.', 'Required': False}, {'Name': 'ToAddress', 'Type': 'object', 'Description': 'To address of the shipment.', 'Required': False}]}
## Get a list of shipment items
### `GET` `v1/shipments/{shipmentID}/items`

| Parameters      | Description                    |
|------------------|---------------------------------|
| Name            | shipmentID                     |
| Type            | string                         |
| Description     | ID of the shipment.            |
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
{'Sample': '{\r\n  "Meta": {\r\n    "Page": 1,\r\n    "PageSize": 20,\r\n    "TotalCount": 25,\r\n    "TotalPages": 2,\r\n    "ItemRange": [\r\n      1,\r\n      20\r\n    ]\r\n  },\r\n  "Items": [\r\n    {\r\n      "OrderID": "",\r\n      "LineItemID": "",\r\n      "QuantityShipped": 0,\r\n      "UnitPrice": 0,\r\n      "CostCenter": "",\r\n      "DateNeeded": "2018-03-21T23:00:00+00:00",\r\n      "Product": {\r\n        "ID": "",\r\n        "Name": "",\r\n        "Description": "",\r\n        "QuantityMultiplier": 0,\r\n        "ShipWeight": 0,\r\n        "ShipHeight": 0,\r\n        "ShipWidth": 0,\r\n        "ShipLength": 0,\r\n        "xp": {}\r\n      },\r\n      "Specs": [\r\n        {\r\n          "SpecID": "",\r\n          "Name": "",\r\n          "OptionID": "",\r\n          "Value": ""\r\n        }\r\n      ],\r\n      "xp": {}\r\n    }\r\n  ]\r\n}', 'Fields': [{'Name': 'OrderID', 'Type': 'string', 'Description': 'ID of the order.', 'Required': True}, {'Name': 'LineItemID', 'Type': 'string', 'Description': 'ID of the line item.', 'Required': True}, {'Name': 'QuantityShipped', 'Type': 'integer', 'Description': 'Quantity shipped of the shipment item.', 'Required': True}, {'Name': 'UnitPrice', 'Type': 'float', 'Description': 'Unit price of the shipment item.', 'Required': False}, {'Name': 'CostCenter', 'Type': 'string', 'Description': 'Cost center of the shipment item.', 'Required': False}, {'Name': 'DateNeeded', 'Type': 'date', 'Description': 'Date needed of the shipment item.', 'Required': False}, {'Name': 'Product', 'Type': 'object', 'Description': 'Product of the shipment item.', 'Required': False}, {'Name': 'Specs', 'Type': 'array', 'Description': 'Specs of the shipment item.', 'Required': False}, {'Name': 'xp', 'Type': 'object', 'Description': 'Container for extended (custom) properties of the shipment item.', 'Required': False}]}
## Get a single shipment item
### `GET` `v1/shipments/{shipmentID}/items/{orderID}/{lineItemID}`

| Parameters      | Description                    |
|------------------|---------------------------------|
| Name            | shipmentID                     |
| Type            | string                         |
| Description     | ID of the shipment.            |
| Required        | True                           |
| Name            | orderID                        |
| Type            | string                         |
| Description     | ID of the order.               |
| Required        | True                           |
| Name            | lineItemID                     |
| Type            | string                         |
| Description     | ID of the line item.           |
| Required        | True                           |

 **Requestbody**: 
None
 **Responsestatus**: `200`

 **Responsebody**: 
{'Sample': '{\r\n  "OrderID": "",\r\n  "LineItemID": "",\r\n  "QuantityShipped": 0,\r\n  "UnitPrice": 0,\r\n  "CostCenter": "",\r\n  "DateNeeded": "2018-03-21T23:00:00+00:00",\r\n  "Product": {\r\n    "ID": "",\r\n    "Name": "",\r\n    "Description": "",\r\n    "QuantityMultiplier": 0,\r\n    "ShipWeight": 0,\r\n    "ShipHeight": 0,\r\n    "ShipWidth": 0,\r\n    "ShipLength": 0,\r\n    "xp": {}\r\n  },\r\n  "Specs": [\r\n    {\r\n      "SpecID": "",\r\n      "Name": "",\r\n      "OptionID": "",\r\n      "Value": ""\r\n    }\r\n  ],\r\n  "xp": {}\r\n}', 'Fields': [{'Name': 'OrderID', 'Type': 'string', 'Description': 'ID of the order.', 'Required': True}, {'Name': 'LineItemID', 'Type': 'string', 'Description': 'ID of the line item.', 'Required': True}, {'Name': 'QuantityShipped', 'Type': 'integer', 'Description': 'Quantity shipped of the shipment item.', 'Required': True}, {'Name': 'UnitPrice', 'Type': 'float', 'Description': 'Unit price of the shipment item.', 'Required': False}, {'Name': 'CostCenter', 'Type': 'string', 'Description': 'Cost center of the shipment item.', 'Required': False}, {'Name': 'DateNeeded', 'Type': 'date', 'Description': 'Date needed of the shipment item.', 'Required': False}, {'Name': 'Product', 'Type': 'object', 'Description': 'Product of the shipment item.', 'Required': False}, {'Name': 'Specs', 'Type': 'array', 'Description': 'Specs of the shipment item.', 'Required': False}, {'Name': 'xp', 'Type': 'object', 'Description': 'Container for extended (custom) properties of the shipment item.', 'Required': False}]}
## Save a shipment item
### `POST` `v1/shipments/{shipmentID}/items`

| Parameters      | Description                    |
|------------------|---------------------------------|
| Name            | shipmentID                     |
| Type            | string                         |
| Description     | ID of the shipment.            |
| Required        | True                           |

 **Requestbody**: 
{'Sample': '{\r\n  "OrderID": "",\r\n  "LineItemID": "",\r\n  "QuantityShipped": 0\r\n}', 'Fields': [{'Name': 'OrderID', 'Type': 'string', 'Description': 'ID of the order. Required.', 'Required': True}, {'Name': 'LineItemID', 'Type': 'string', 'Description': 'ID of the line item. Required.', 'Required': True}, {'Name': 'QuantityShipped', 'Type': 'integer', 'Description': 'Quantity shipped of the shipment item. Required.', 'Required': True}]}
 **Responsestatus**: `200`

 **Responsebody**: 
{'Sample': '{\r\n  "OrderID": "",\r\n  "LineItemID": "",\r\n  "QuantityShipped": 0,\r\n  "UnitPrice": 0,\r\n  "CostCenter": "",\r\n  "DateNeeded": "2018-03-21T23:00:00+00:00",\r\n  "Product": {\r\n    "ID": "",\r\n    "Name": "",\r\n    "Description": "",\r\n    "QuantityMultiplier": 0,\r\n    "ShipWeight": 0,\r\n    "ShipHeight": 0,\r\n    "ShipWidth": 0,\r\n    "ShipLength": 0,\r\n    "xp": {}\r\n  },\r\n  "Specs": [\r\n    {\r\n      "SpecID": "",\r\n      "Name": "",\r\n      "OptionID": "",\r\n      "Value": ""\r\n    }\r\n  ],\r\n  "xp": {}\r\n}', 'Fields': [{'Name': 'OrderID', 'Type': 'string', 'Description': 'ID of the order.', 'Required': True}, {'Name': 'LineItemID', 'Type': 'string', 'Description': 'ID of the line item.', 'Required': True}, {'Name': 'QuantityShipped', 'Type': 'integer', 'Description': 'Quantity shipped of the shipment item.', 'Required': True}, {'Name': 'UnitPrice', 'Type': 'float', 'Description': 'Unit price of the shipment item.', 'Required': False}, {'Name': 'CostCenter', 'Type': 'string', 'Description': 'Cost center of the shipment item.', 'Required': False}, {'Name': 'DateNeeded', 'Type': 'date', 'Description': 'Date needed of the shipment item.', 'Required': False}, {'Name': 'Product', 'Type': 'object', 'Description': 'Product of the shipment item.', 'Required': False}, {'Name': 'Specs', 'Type': 'array', 'Description': 'Specs of the shipment item.', 'Required': False}, {'Name': 'xp', 'Type': 'object', 'Description': 'Container for extended (custom) properties of the shipment item.', 'Required': False}]}
## Delete a shipment item
### `DELETE` `v1/shipments/{shipmentID}/items/{orderID}/{lineItemID}`

| Parameters      | Description                    |
|------------------|---------------------------------|
| Name            | shipmentID                     |
| Type            | string                         |
| Description     | ID of the shipment.            |
| Required        | True                           |
| Name            | orderID                        |
| Type            | string                         |
| Description     | ID of the order.               |
| Required        | True                           |
| Name            | lineItemID                     |
| Type            | string                         |
| Description     | ID of the line item.           |
| Required        | True                           |

 **Requestbody**: 
None
 **Responsestatus**: `204`

 **Responsebody**: 
None