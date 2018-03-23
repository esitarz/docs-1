---
title: Products
date: 2018-03-23
category: API Reference
tags: Product Catalogs
slug: Products
---
A Product represents a physical, digital, or absract good that is
offered for sale by a seller organization and is purchase-able by Buyer
Users via an Order.
Products can be a static SKU or a version of a static SKU, known as a
Variant. For example, a variant is often a size or color choice that
drives a different product SKU.
Products may also have inventory associated with them and various
inventory attributes like quantity available and re-order notifications.

---
## Get a single product
### `GET` `v1/products/{productID}`

| Parameters      | Description                    |
|------------------|---------------------------------|
| Name            | productID                      |
| Type            | string                         |
| Description     | ID of the product.             |
| Required        | True                           |

 **Requestbody**: 
None
 **Responsestatus**: `200`

 **Responsebody**: 
{'Sample': '{\r\n  "DefaultPriceScheduleID": "",\r\n  "ID": "",\r\n  "Name": "",\r\n  "Description": "",\r\n  "QuantityMultiplier": 0,\r\n  "ShipWeight": 0,\r\n  "ShipHeight": 0,\r\n  "ShipWidth": 0,\r\n  "ShipLength": 0,\r\n  "Active": false,\r\n  "SpecCount": 0,\r\n  "xp": {},\r\n  "VariantCount": 0,\r\n  "ShipFromAddressID": "",\r\n  "Inventory": {\r\n    "Enabled": false,\r\n    "NotificationPoint": 0,\r\n    "VariantLevelTracking": false,\r\n    "OrderCanExceed": false,\r\n    "QuantityAvailable": 0,\r\n    "LastUpdated": "2018-03-21T23:00:00+00:00"\r\n  },\r\n  "AutoForwardSupplierID": ""\r\n}', 'Fields': [{'Name': 'DefaultPriceScheduleID', 'Type': 'string', 'Description': 'ID of the default price schedule.', 'Required': False}, {'Name': 'ID', 'Type': 'string', 'Description': 'ID of the product.', 'Required': False}, {'Name': 'Name', 'Type': 'string', 'Description': 'Name of the product.', 'Required': True}, {'Name': 'Description', 'Type': 'string', 'Description': 'Description of the product.', 'Required': False}, {'Name': 'QuantityMultiplier', 'Type': 'integer', 'Description': 'Quantity multiplier of the product.', 'Required': True}, {'Name': 'ShipWeight', 'Type': 'float', 'Description': 'Ship weight of the product.', 'Required': False}, {'Name': 'ShipHeight', 'Type': 'float', 'Description': 'Ship height of the product.', 'Required': False}, {'Name': 'ShipWidth', 'Type': 'float', 'Description': 'Ship width of the product.', 'Required': False}, {'Name': 'ShipLength', 'Type': 'float', 'Description': 'Ship length of the product.', 'Required': False}, {'Name': 'Active', 'Type': 'boolean', 'Description': 'Active of the product.', 'Required': False}, {'Name': 'SpecCount', 'Type': 'integer', 'Description': 'Spec count of the product.', 'Required': False}, {'Name': 'xp', 'Type': 'object', 'Description': 'Container for extended (custom) properties of the product.', 'Required': False}, {'Name': 'VariantCount', 'Type': 'integer', 'Description': 'Variant count of the product.', 'Required': False}, {'Name': 'ShipFromAddressID', 'Type': 'string', 'Description': 'ID of the ship from address.', 'Required': False}, {'Name': 'Inventory', 'Type': 'object', 'Description': 'Inventory of the product.', 'Required': False}, {'Name': 'AutoForwardSupplierID', 'Type': 'string', 'Description': 'ID of the auto forward supplier.', 'Required': False}]}## Get a list of products
### `GET` `v1/products`

| Parameters      | Description                    |
|------------------|---------------------------------|
| Name            | catalogID                      |
| Type            | string                         |
| Description     | ID of the catalog.             |
| Required        | False                          |
| Name            | categoryID                     |
| Type            | string                         |
| Description     | ID of the category.            |
| Required        | False                          |
| Name            | supplierID                     |
| Type            | string                         |
| Description     | ID of the supplier.            |
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
{'Sample': '{\r\n  "Meta": {\r\n    "Page": 1,\r\n    "PageSize": 20,\r\n    "TotalCount": 25,\r\n    "TotalPages": 2,\r\n    "ItemRange": [\r\n      1,\r\n      20\r\n    ]\r\n  },\r\n  "Items": [\r\n    {\r\n      "DefaultPriceScheduleID": "",\r\n      "ID": "",\r\n      "Name": "",\r\n      "Description": "",\r\n      "QuantityMultiplier": 0,\r\n      "ShipWeight": 0,\r\n      "ShipHeight": 0,\r\n      "ShipWidth": 0,\r\n      "ShipLength": 0,\r\n      "Active": false,\r\n      "SpecCount": 0,\r\n      "xp": {},\r\n      "VariantCount": 0,\r\n      "ShipFromAddressID": "",\r\n      "Inventory": {\r\n        "Enabled": false,\r\n        "NotificationPoint": 0,\r\n        "VariantLevelTracking": false,\r\n        "OrderCanExceed": false,\r\n        "QuantityAvailable": 0,\r\n        "LastUpdated": "2018-03-21T23:00:00+00:00"\r\n      },\r\n      "AutoForwardSupplierID": ""\r\n    }\r\n  ]\r\n}', 'Fields': [{'Name': 'DefaultPriceScheduleID', 'Type': 'string', 'Description': 'ID of the default price schedule.', 'Required': False}, {'Name': 'ID', 'Type': 'string', 'Description': 'ID of the product.', 'Required': False}, {'Name': 'Name', 'Type': 'string', 'Description': 'Name of the product.', 'Required': True}, {'Name': 'Description', 'Type': 'string', 'Description': 'Description of the product.', 'Required': False}, {'Name': 'QuantityMultiplier', 'Type': 'integer', 'Description': 'Quantity multiplier of the product.', 'Required': True}, {'Name': 'ShipWeight', 'Type': 'float', 'Description': 'Ship weight of the product.', 'Required': False}, {'Name': 'ShipHeight', 'Type': 'float', 'Description': 'Ship height of the product.', 'Required': False}, {'Name': 'ShipWidth', 'Type': 'float', 'Description': 'Ship width of the product.', 'Required': False}, {'Name': 'ShipLength', 'Type': 'float', 'Description': 'Ship length of the product.', 'Required': False}, {'Name': 'Active', 'Type': 'boolean', 'Description': 'Active of the product.', 'Required': False}, {'Name': 'SpecCount', 'Type': 'integer', 'Description': 'Spec count of the product.', 'Required': False}, {'Name': 'xp', 'Type': 'object', 'Description': 'Container for extended (custom) properties of the product.', 'Required': False}, {'Name': 'VariantCount', 'Type': 'integer', 'Description': 'Variant count of the product.', 'Required': False}, {'Name': 'ShipFromAddressID', 'Type': 'string', 'Description': 'ID of the ship from address.', 'Required': False}, {'Name': 'Inventory', 'Type': 'object', 'Description': 'Inventory of the product.', 'Required': False}, {'Name': 'AutoForwardSupplierID', 'Type': 'string', 'Description': 'ID of the auto forward supplier.', 'Required': False}]}## Create a new product
### `POST` `v1/products`

| Parameters      | Description                    |
|------------------|---------------------------------|

 **Requestbody**: 
{'Sample': '{\r\n  "DefaultPriceScheduleID": "",\r\n  "ID": "",\r\n  "Name": "",\r\n  "Description": "",\r\n  "QuantityMultiplier": 0,\r\n  "ShipWeight": 0,\r\n  "ShipHeight": 0,\r\n  "ShipWidth": 0,\r\n  "ShipLength": 0,\r\n  "Active": false,\r\n  "xp": {},\r\n  "ShipFromAddressID": "",\r\n  "Inventory": {\r\n    "Enabled": false,\r\n    "NotificationPoint": 0,\r\n    "VariantLevelTracking": false,\r\n    "OrderCanExceed": false,\r\n    "QuantityAvailable": 0\r\n  },\r\n  "AutoForwardSupplierID": ""\r\n}', 'Fields': [{'Name': 'DefaultPriceScheduleID', 'Type': 'string', 'Description': 'ID of the default price schedule.', 'Required': False}, {'Name': 'ID', 'Type': 'string', 'Description': 'ID of the product. Can only contain characters Aa-Zz, 0-9, -, and _. Searchable: priority level 1. Sortable: priority level 2.', 'Required': False}, {'Name': 'Name', 'Type': 'string', 'Description': 'Name of the product. Required. Max length 100 characters. Searchable: priority level 2. Sortable: priority level 1.', 'Required': True}, {'Name': 'Description', 'Type': 'string', 'Description': 'Description of the product. Max length 2000 characters. Searchable: priority level 3.', 'Required': False}, {'Name': 'QuantityMultiplier', 'Type': 'integer', 'Description': 'Quantity multiplier of the product. Required. Must be at least 1.', 'Required': True}, {'Name': 'ShipWeight', 'Type': 'float', 'Description': 'Ship weight of the product.', 'Required': False}, {'Name': 'ShipHeight', 'Type': 'float', 'Description': 'Ship height of the product.', 'Required': False}, {'Name': 'ShipWidth', 'Type': 'float', 'Description': 'Ship width of the product.', 'Required': False}, {'Name': 'ShipLength', 'Type': 'float', 'Description': 'Ship length of the product.', 'Required': False}, {'Name': 'Active', 'Type': 'boolean', 'Description': 'Active of the product.', 'Required': False}, {'Name': 'xp', 'Type': 'object', 'Description': 'Container for extended (custom) properties of the product.', 'Required': False}, {'Name': 'ShipFromAddressID', 'Type': 'string', 'Description': 'ID of the ship from address.', 'Required': False}, {'Name': 'Inventory', 'Type': 'object', 'Description': 'Inventory of the product.', 'Required': False}, {'Name': 'AutoForwardSupplierID', 'Type': 'string', 'Description': 'ID of the auto forward supplier.', 'Required': False}]}
 **Responsestatus**: `201`

 **Responsebody**: 
{'Sample': '{\r\n  "DefaultPriceScheduleID": "",\r\n  "ID": "",\r\n  "Name": "",\r\n  "Description": "",\r\n  "QuantityMultiplier": 0,\r\n  "ShipWeight": 0,\r\n  "ShipHeight": 0,\r\n  "ShipWidth": 0,\r\n  "ShipLength": 0,\r\n  "Active": false,\r\n  "SpecCount": 0,\r\n  "xp": {},\r\n  "VariantCount": 0,\r\n  "ShipFromAddressID": "",\r\n  "Inventory": {\r\n    "Enabled": false,\r\n    "NotificationPoint": 0,\r\n    "VariantLevelTracking": false,\r\n    "OrderCanExceed": false,\r\n    "QuantityAvailable": 0,\r\n    "LastUpdated": "2018-03-21T23:00:00+00:00"\r\n  },\r\n  "AutoForwardSupplierID": ""\r\n}', 'Fields': [{'Name': 'DefaultPriceScheduleID', 'Type': 'string', 'Description': 'ID of the default price schedule.', 'Required': False}, {'Name': 'ID', 'Type': 'string', 'Description': 'ID of the product.', 'Required': False}, {'Name': 'Name', 'Type': 'string', 'Description': 'Name of the product.', 'Required': True}, {'Name': 'Description', 'Type': 'string', 'Description': 'Description of the product.', 'Required': False}, {'Name': 'QuantityMultiplier', 'Type': 'integer', 'Description': 'Quantity multiplier of the product.', 'Required': True}, {'Name': 'ShipWeight', 'Type': 'float', 'Description': 'Ship weight of the product.', 'Required': False}, {'Name': 'ShipHeight', 'Type': 'float', 'Description': 'Ship height of the product.', 'Required': False}, {'Name': 'ShipWidth', 'Type': 'float', 'Description': 'Ship width of the product.', 'Required': False}, {'Name': 'ShipLength', 'Type': 'float', 'Description': 'Ship length of the product.', 'Required': False}, {'Name': 'Active', 'Type': 'boolean', 'Description': 'Active of the product.', 'Required': False}, {'Name': 'SpecCount', 'Type': 'integer', 'Description': 'Spec count of the product.', 'Required': False}, {'Name': 'xp', 'Type': 'object', 'Description': 'Container for extended (custom) properties of the product.', 'Required': False}, {'Name': 'VariantCount', 'Type': 'integer', 'Description': 'Variant count of the product.', 'Required': False}, {'Name': 'ShipFromAddressID', 'Type': 'string', 'Description': 'ID of the ship from address.', 'Required': False}, {'Name': 'Inventory', 'Type': 'object', 'Description': 'Inventory of the product.', 'Required': False}, {'Name': 'AutoForwardSupplierID', 'Type': 'string', 'Description': 'ID of the auto forward supplier.', 'Required': False}]}## Create or update a product
### `PUT` `v1/products/{productID}`

| Parameters      | Description                    |
|------------------|---------------------------------|
| Name            | productID                      |
| Type            | string                         |
| Description     | ID of the product.             |
| Required        | True                           |

 **Requestbody**: 
{'Sample': '{\r\n  "DefaultPriceScheduleID": "",\r\n  "ID": "",\r\n  "Name": "",\r\n  "Description": "",\r\n  "QuantityMultiplier": 0,\r\n  "ShipWeight": 0,\r\n  "ShipHeight": 0,\r\n  "ShipWidth": 0,\r\n  "ShipLength": 0,\r\n  "Active": false,\r\n  "xp": {},\r\n  "ShipFromAddressID": "",\r\n  "Inventory": {\r\n    "Enabled": false,\r\n    "NotificationPoint": 0,\r\n    "VariantLevelTracking": false,\r\n    "OrderCanExceed": false,\r\n    "QuantityAvailable": 0\r\n  },\r\n  "AutoForwardSupplierID": ""\r\n}', 'Fields': [{'Name': 'DefaultPriceScheduleID', 'Type': 'string', 'Description': 'ID of the default price schedule.', 'Required': False}, {'Name': 'ID', 'Type': 'string', 'Description': 'ID of the product. Can only contain characters Aa-Zz, 0-9, -, and _. Searchable: priority level 1. Sortable: priority level 2.', 'Required': False}, {'Name': 'Name', 'Type': 'string', 'Description': 'Name of the product. Required. Max length 100 characters. Searchable: priority level 2. Sortable: priority level 1.', 'Required': True}, {'Name': 'Description', 'Type': 'string', 'Description': 'Description of the product. Max length 2000 characters. Searchable: priority level 3.', 'Required': False}, {'Name': 'QuantityMultiplier', 'Type': 'integer', 'Description': 'Quantity multiplier of the product. Required. Must be at least 1.', 'Required': True}, {'Name': 'ShipWeight', 'Type': 'float', 'Description': 'Ship weight of the product.', 'Required': False}, {'Name': 'ShipHeight', 'Type': 'float', 'Description': 'Ship height of the product.', 'Required': False}, {'Name': 'ShipWidth', 'Type': 'float', 'Description': 'Ship width of the product.', 'Required': False}, {'Name': 'ShipLength', 'Type': 'float', 'Description': 'Ship length of the product.', 'Required': False}, {'Name': 'Active', 'Type': 'boolean', 'Description': 'Active of the product.', 'Required': False}, {'Name': 'xp', 'Type': 'object', 'Description': 'Container for extended (custom) properties of the product.', 'Required': False}, {'Name': 'ShipFromAddressID', 'Type': 'string', 'Description': 'ID of the ship from address.', 'Required': False}, {'Name': 'Inventory', 'Type': 'object', 'Description': 'Inventory of the product.', 'Required': False}, {'Name': 'AutoForwardSupplierID', 'Type': 'string', 'Description': 'ID of the auto forward supplier.', 'Required': False}]}
 **Responsestatus**: `200`

 **Responsebody**: 
{'Sample': '{\r\n  "DefaultPriceScheduleID": "",\r\n  "ID": "",\r\n  "Name": "",\r\n  "Description": "",\r\n  "QuantityMultiplier": 0,\r\n  "ShipWeight": 0,\r\n  "ShipHeight": 0,\r\n  "ShipWidth": 0,\r\n  "ShipLength": 0,\r\n  "Active": false,\r\n  "SpecCount": 0,\r\n  "xp": {},\r\n  "VariantCount": 0,\r\n  "ShipFromAddressID": "",\r\n  "Inventory": {\r\n    "Enabled": false,\r\n    "NotificationPoint": 0,\r\n    "VariantLevelTracking": false,\r\n    "OrderCanExceed": false,\r\n    "QuantityAvailable": 0,\r\n    "LastUpdated": "2018-03-21T23:00:00+00:00"\r\n  },\r\n  "AutoForwardSupplierID": ""\r\n}', 'Fields': [{'Name': 'DefaultPriceScheduleID', 'Type': 'string', 'Description': 'ID of the default price schedule.', 'Required': False}, {'Name': 'ID', 'Type': 'string', 'Description': 'ID of the product.', 'Required': False}, {'Name': 'Name', 'Type': 'string', 'Description': 'Name of the product.', 'Required': True}, {'Name': 'Description', 'Type': 'string', 'Description': 'Description of the product.', 'Required': False}, {'Name': 'QuantityMultiplier', 'Type': 'integer', 'Description': 'Quantity multiplier of the product.', 'Required': True}, {'Name': 'ShipWeight', 'Type': 'float', 'Description': 'Ship weight of the product.', 'Required': False}, {'Name': 'ShipHeight', 'Type': 'float', 'Description': 'Ship height of the product.', 'Required': False}, {'Name': 'ShipWidth', 'Type': 'float', 'Description': 'Ship width of the product.', 'Required': False}, {'Name': 'ShipLength', 'Type': 'float', 'Description': 'Ship length of the product.', 'Required': False}, {'Name': 'Active', 'Type': 'boolean', 'Description': 'Active of the product.', 'Required': False}, {'Name': 'SpecCount', 'Type': 'integer', 'Description': 'Spec count of the product.', 'Required': False}, {'Name': 'xp', 'Type': 'object', 'Description': 'Container for extended (custom) properties of the product.', 'Required': False}, {'Name': 'VariantCount', 'Type': 'integer', 'Description': 'Variant count of the product.', 'Required': False}, {'Name': 'ShipFromAddressID', 'Type': 'string', 'Description': 'ID of the ship from address.', 'Required': False}, {'Name': 'Inventory', 'Type': 'object', 'Description': 'Inventory of the product.', 'Required': False}, {'Name': 'AutoForwardSupplierID', 'Type': 'string', 'Description': 'ID of the auto forward supplier.', 'Required': False}]}## Delete a product
### `DELETE` `v1/products/{productID}`

| Parameters      | Description                    |
|------------------|---------------------------------|
| Name            | productID                      |
| Type            | string                         |
| Description     | ID of the product.             |
| Required        | True                           |

 **Requestbody**: 
None
 **Responsestatus**: `204`

 **Responsebody**: 
None## Partially update a product
### `PATCH` `v1/products/{productID}`

| Parameters      | Description                    |
|------------------|---------------------------------|
| Name            | productID                      |
| Type            | string                         |
| Description     | ID of the product.             |
| Required        | True                           |

 **Requestbody**: 
{'Sample': '{\r\n  "DefaultPriceScheduleID": "",\r\n  "ID": "",\r\n  "Name": "",\r\n  "Description": "",\r\n  "QuantityMultiplier": 0,\r\n  "ShipWeight": 0,\r\n  "ShipHeight": 0,\r\n  "ShipWidth": 0,\r\n  "ShipLength": 0,\r\n  "Active": false,\r\n  "xp": {},\r\n  "ShipFromAddressID": "",\r\n  "Inventory": {\r\n    "Enabled": false,\r\n    "NotificationPoint": 0,\r\n    "VariantLevelTracking": false,\r\n    "OrderCanExceed": false,\r\n    "QuantityAvailable": 0\r\n  },\r\n  "AutoForwardSupplierID": ""\r\n}', 'Fields': [{'Name': 'DefaultPriceScheduleID', 'Type': 'string', 'Description': 'ID of the default price schedule.', 'Required': False}, {'Name': 'ID', 'Type': 'string', 'Description': 'ID of the product. Can only contain characters Aa-Zz, 0-9, -, and _. Searchable: priority level 1. Sortable: priority level 2.', 'Required': False}, {'Name': 'Name', 'Type': 'string', 'Description': 'Name of the product. Required. Max length 100 characters. Searchable: priority level 2. Sortable: priority level 1.', 'Required': True}, {'Name': 'Description', 'Type': 'string', 'Description': 'Description of the product. Max length 2000 characters. Searchable: priority level 3.', 'Required': False}, {'Name': 'QuantityMultiplier', 'Type': 'integer', 'Description': 'Quantity multiplier of the product. Required. Must be at least 1.', 'Required': True}, {'Name': 'ShipWeight', 'Type': 'float', 'Description': 'Ship weight of the product.', 'Required': False}, {'Name': 'ShipHeight', 'Type': 'float', 'Description': 'Ship height of the product.', 'Required': False}, {'Name': 'ShipWidth', 'Type': 'float', 'Description': 'Ship width of the product.', 'Required': False}, {'Name': 'ShipLength', 'Type': 'float', 'Description': 'Ship length of the product.', 'Required': False}, {'Name': 'Active', 'Type': 'boolean', 'Description': 'Active of the product.', 'Required': False}, {'Name': 'xp', 'Type': 'object', 'Description': 'Container for extended (custom) properties of the product.', 'Required': False}, {'Name': 'ShipFromAddressID', 'Type': 'string', 'Description': 'ID of the ship from address.', 'Required': False}, {'Name': 'Inventory', 'Type': 'object', 'Description': 'Inventory of the product.', 'Required': False}, {'Name': 'AutoForwardSupplierID', 'Type': 'string', 'Description': 'ID of the auto forward supplier.', 'Required': False}]}
 **Responsestatus**: `200`

 **Responsebody**: 
{'Sample': '{\r\n  "DefaultPriceScheduleID": "",\r\n  "ID": "",\r\n  "Name": "",\r\n  "Description": "",\r\n  "QuantityMultiplier": 0,\r\n  "ShipWeight": 0,\r\n  "ShipHeight": 0,\r\n  "ShipWidth": 0,\r\n  "ShipLength": 0,\r\n  "Active": false,\r\n  "SpecCount": 0,\r\n  "xp": {},\r\n  "VariantCount": 0,\r\n  "ShipFromAddressID": "",\r\n  "Inventory": {\r\n    "Enabled": false,\r\n    "NotificationPoint": 0,\r\n    "VariantLevelTracking": false,\r\n    "OrderCanExceed": false,\r\n    "QuantityAvailable": 0,\r\n    "LastUpdated": "2018-03-21T23:00:00+00:00"\r\n  },\r\n  "AutoForwardSupplierID": ""\r\n}', 'Fields': [{'Name': 'DefaultPriceScheduleID', 'Type': 'string', 'Description': 'ID of the default price schedule.', 'Required': False}, {'Name': 'ID', 'Type': 'string', 'Description': 'ID of the product.', 'Required': False}, {'Name': 'Name', 'Type': 'string', 'Description': 'Name of the product.', 'Required': True}, {'Name': 'Description', 'Type': 'string', 'Description': 'Description of the product.', 'Required': False}, {'Name': 'QuantityMultiplier', 'Type': 'integer', 'Description': 'Quantity multiplier of the product.', 'Required': True}, {'Name': 'ShipWeight', 'Type': 'float', 'Description': 'Ship weight of the product.', 'Required': False}, {'Name': 'ShipHeight', 'Type': 'float', 'Description': 'Ship height of the product.', 'Required': False}, {'Name': 'ShipWidth', 'Type': 'float', 'Description': 'Ship width of the product.', 'Required': False}, {'Name': 'ShipLength', 'Type': 'float', 'Description': 'Ship length of the product.', 'Required': False}, {'Name': 'Active', 'Type': 'boolean', 'Description': 'Active of the product.', 'Required': False}, {'Name': 'SpecCount', 'Type': 'integer', 'Description': 'Spec count of the product.', 'Required': False}, {'Name': 'xp', 'Type': 'object', 'Description': 'Container for extended (custom) properties of the product.', 'Required': False}, {'Name': 'VariantCount', 'Type': 'integer', 'Description': 'Variant count of the product.', 'Required': False}, {'Name': 'ShipFromAddressID', 'Type': 'string', 'Description': 'ID of the ship from address.', 'Required': False}, {'Name': 'Inventory', 'Type': 'object', 'Description': 'Inventory of the product.', 'Required': False}, {'Name': 'AutoForwardSupplierID', 'Type': 'string', 'Description': 'ID of the auto forward supplier.', 'Required': False}]}## Generate a variants
### `POST` `v1/products/{productID}/variants/generate`

| Parameters      | Description                    |
|------------------|---------------------------------|
| Name            | productID                      |
| Type            | string                         |
| Description     | ID of the product.             |
| Required        | True                           |
| Name            | overwriteExisting              |
| Type            | boolean                        |
| Description     | Overwrite existing of the product. |
| Required        | False                          |

 **Requestbody**: 
None
 **Responsestatus**: `201`

 **Responsebody**: 
{'Sample': '{\r\n  "DefaultPriceScheduleID": "",\r\n  "ID": "",\r\n  "Name": "",\r\n  "Description": "",\r\n  "QuantityMultiplier": 0,\r\n  "ShipWeight": 0,\r\n  "ShipHeight": 0,\r\n  "ShipWidth": 0,\r\n  "ShipLength": 0,\r\n  "Active": false,\r\n  "SpecCount": 0,\r\n  "xp": {},\r\n  "VariantCount": 0,\r\n  "ShipFromAddressID": "",\r\n  "Inventory": {\r\n    "Enabled": false,\r\n    "NotificationPoint": 0,\r\n    "VariantLevelTracking": false,\r\n    "OrderCanExceed": false,\r\n    "QuantityAvailable": 0,\r\n    "LastUpdated": "2018-03-21T23:00:00+00:00"\r\n  },\r\n  "AutoForwardSupplierID": ""\r\n}', 'Fields': [{'Name': 'DefaultPriceScheduleID', 'Type': 'string', 'Description': 'ID of the default price schedule.', 'Required': False}, {'Name': 'ID', 'Type': 'string', 'Description': 'ID of the product.', 'Required': False}, {'Name': 'Name', 'Type': 'string', 'Description': 'Name of the product.', 'Required': True}, {'Name': 'Description', 'Type': 'string', 'Description': 'Description of the product.', 'Required': False}, {'Name': 'QuantityMultiplier', 'Type': 'integer', 'Description': 'Quantity multiplier of the product.', 'Required': True}, {'Name': 'ShipWeight', 'Type': 'float', 'Description': 'Ship weight of the product.', 'Required': False}, {'Name': 'ShipHeight', 'Type': 'float', 'Description': 'Ship height of the product.', 'Required': False}, {'Name': 'ShipWidth', 'Type': 'float', 'Description': 'Ship width of the product.', 'Required': False}, {'Name': 'ShipLength', 'Type': 'float', 'Description': 'Ship length of the product.', 'Required': False}, {'Name': 'Active', 'Type': 'boolean', 'Description': 'Active of the product.', 'Required': False}, {'Name': 'SpecCount', 'Type': 'integer', 'Description': 'Spec count of the product.', 'Required': False}, {'Name': 'xp', 'Type': 'object', 'Description': 'Container for extended (custom) properties of the product.', 'Required': False}, {'Name': 'VariantCount', 'Type': 'integer', 'Description': 'Variant count of the product.', 'Required': False}, {'Name': 'ShipFromAddressID', 'Type': 'string', 'Description': 'ID of the ship from address.', 'Required': False}, {'Name': 'Inventory', 'Type': 'object', 'Description': 'Inventory of the product.', 'Required': False}, {'Name': 'AutoForwardSupplierID', 'Type': 'string', 'Description': 'ID of the auto forward supplier.', 'Required': False}]}## Get a list of product variants
### `GET` `v1/products/{productID}/variants`

| Parameters      | Description                    |
|------------------|---------------------------------|
| Name            | productID                      |
| Type            | string                         |
| Description     | ID of the product.             |
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
{'Sample': '{\r\n  "Meta": {\r\n    "Page": 1,\r\n    "PageSize": 20,\r\n    "TotalCount": 25,\r\n    "TotalPages": 2,\r\n    "ItemRange": [\r\n      1,\r\n      20\r\n    ]\r\n  },\r\n  "Items": [\r\n    {\r\n      "ID": "",\r\n      "Name": "",\r\n      "Description": "",\r\n      "Active": false,\r\n      "xp": {}\r\n    }\r\n  ]\r\n}', 'Fields': [{'Name': 'ID', 'Type': 'string', 'Description': 'ID of the variant.', 'Required': False}, {'Name': 'Name', 'Type': 'string', 'Description': 'Name of the variant.', 'Required': False}, {'Name': 'Description', 'Type': 'string', 'Description': 'Description of the variant.', 'Required': False}, {'Name': 'Active', 'Type': 'boolean', 'Description': 'Active of the variant.', 'Required': False}, {'Name': 'xp', 'Type': 'object', 'Description': 'Container for extended (custom) properties of the variant.', 'Required': False}]}## Create or update a product variant
### `PUT` `v1/products/{productID}/variants/{variantID}`

| Parameters      | Description                    |
|------------------|---------------------------------|
| Name            | productID                      |
| Type            | string                         |
| Description     | ID of the product.             |
| Required        | True                           |
| Name            | variantID                      |
| Type            | string                         |
| Description     | ID of the variant.             |
| Required        | True                           |

 **Requestbody**: 
{'Sample': '{\r\n  "ID": "",\r\n  "Name": "",\r\n  "Description": "",\r\n  "Active": false,\r\n  "xp": {}\r\n}', 'Fields': [{'Name': 'ID', 'Type': 'string', 'Description': 'ID of the variant. Can only contain characters Aa-Zz, 0-9, -, and _. Searchable: priority level 1. Sortable: priority level 1.', 'Required': False}, {'Name': 'Name', 'Type': 'string', 'Description': 'Name of the variant. Searchable: priority level 2. Sortable: priority level 2.', 'Required': False}, {'Name': 'Description', 'Type': 'string', 'Description': 'Description of the variant. Max length 2000 characters. Searchable: priority level 3.', 'Required': False}, {'Name': 'Active', 'Type': 'boolean', 'Description': 'Active of the variant.', 'Required': False}, {'Name': 'xp', 'Type': 'object', 'Description': 'Container for extended (custom) properties of the variant.', 'Required': False}]}
 **Responsestatus**: `200`

 **Responsebody**: 
{'Sample': '{\r\n  "ID": "",\r\n  "Name": "",\r\n  "Description": "",\r\n  "Active": false,\r\n  "xp": {}\r\n}', 'Fields': [{'Name': 'ID', 'Type': 'string', 'Description': 'ID of the variant.', 'Required': False}, {'Name': 'Name', 'Type': 'string', 'Description': 'Name of the variant.', 'Required': False}, {'Name': 'Description', 'Type': 'string', 'Description': 'Description of the variant.', 'Required': False}, {'Name': 'Active', 'Type': 'boolean', 'Description': 'Active of the variant.', 'Required': False}, {'Name': 'xp', 'Type': 'object', 'Description': 'Container for extended (custom) properties of the variant.', 'Required': False}]}## Partially update a product variant
### `PATCH` `v1/products/{productID}/variants/{variantID}`

| Parameters      | Description                    |
|------------------|---------------------------------|
| Name            | productID                      |
| Type            | string                         |
| Description     | ID of the product.             |
| Required        | True                           |
| Name            | variantID                      |
| Type            | string                         |
| Description     | ID of the variant.             |
| Required        | True                           |

 **Requestbody**: 
{'Sample': '{\r\n  "ID": "",\r\n  "Name": "",\r\n  "Description": "",\r\n  "Active": false,\r\n  "xp": {}\r\n}', 'Fields': [{'Name': 'ID', 'Type': 'string', 'Description': 'ID of the variant. Can only contain characters Aa-Zz, 0-9, -, and _. Searchable: priority level 1. Sortable: priority level 1.', 'Required': False}, {'Name': 'Name', 'Type': 'string', 'Description': 'Name of the variant. Searchable: priority level 2. Sortable: priority level 2.', 'Required': False}, {'Name': 'Description', 'Type': 'string', 'Description': 'Description of the variant. Max length 2000 characters. Searchable: priority level 3.', 'Required': False}, {'Name': 'Active', 'Type': 'boolean', 'Description': 'Active of the variant.', 'Required': False}, {'Name': 'xp', 'Type': 'object', 'Description': 'Container for extended (custom) properties of the variant.', 'Required': False}]}
 **Responsestatus**: `200`

 **Responsebody**: 
{'Sample': '{\r\n  "ID": "",\r\n  "Name": "",\r\n  "Description": "",\r\n  "Active": false,\r\n  "xp": {}\r\n}', 'Fields': [{'Name': 'ID', 'Type': 'string', 'Description': 'ID of the variant.', 'Required': False}, {'Name': 'Name', 'Type': 'string', 'Description': 'Name of the variant.', 'Required': False}, {'Name': 'Description', 'Type': 'string', 'Description': 'Description of the variant.', 'Required': False}, {'Name': 'Active', 'Type': 'boolean', 'Description': 'Active of the variant.', 'Required': False}, {'Name': 'xp', 'Type': 'object', 'Description': 'Container for extended (custom) properties of the variant.', 'Required': False}]}## Get a single product variant
### `GET` `v1/products/{productID}/variants/{variantID}`

| Parameters      | Description                    |
|------------------|---------------------------------|
| Name            | productID                      |
| Type            | string                         |
| Description     | ID of the product.             |
| Required        | True                           |
| Name            | variantID                      |
| Type            | string                         |
| Description     | ID of the variant.             |
| Required        | True                           |

 **Requestbody**: 
None
 **Responsestatus**: `200`

 **Responsebody**: 
{'Sample': '{\r\n  "ID": "",\r\n  "Name": "",\r\n  "Description": "",\r\n  "Active": false,\r\n  "xp": {}\r\n}', 'Fields': [{'Name': 'ID', 'Type': 'string', 'Description': 'ID of the variant.', 'Required': False}, {'Name': 'Name', 'Type': 'string', 'Description': 'Name of the variant.', 'Required': False}, {'Name': 'Description', 'Type': 'string', 'Description': 'Description of the variant.', 'Required': False}, {'Name': 'Active', 'Type': 'boolean', 'Description': 'Active of the variant.', 'Required': False}, {'Name': 'xp', 'Type': 'object', 'Description': 'Container for extended (custom) properties of the variant.', 'Required': False}]}## Get a list of product suppliers
### `GET` `v1/products/{productID}/suppliers`

| Parameters      | Description                    |
|------------------|---------------------------------|
| Name            | productID                      |
| Type            | string                         |
| Description     | ID of the product.             |
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
{'Sample': '{\r\n  "Meta": {\r\n    "Page": 1,\r\n    "PageSize": 20,\r\n    "TotalCount": 25,\r\n    "TotalPages": 2,\r\n    "ItemRange": [\r\n      1,\r\n      20\r\n    ]\r\n  },\r\n  "Items": [\r\n    {\r\n      "ID": "",\r\n      "Name": "",\r\n      "Active": false,\r\n      "xp": {}\r\n    }\r\n  ]\r\n}', 'Fields': [{'Name': 'ID', 'Type': 'string', 'Description': 'ID of the supplier.', 'Required': False}, {'Name': 'Name', 'Type': 'string', 'Description': 'Name of the supplier.', 'Required': True}, {'Name': 'Active', 'Type': 'boolean', 'Description': 'Active of the supplier.', 'Required': False}, {'Name': 'xp', 'Type': 'object', 'Description': 'Container for extended (custom) properties of the supplier.', 'Required': False}]}## Save a product supplier
### `PUT` `v1/products/{productID}/suppliers/{supplierID}`

| Parameters      | Description                    |
|------------------|---------------------------------|
| Name            | productID                      |
| Type            | string                         |
| Description     | ID of the product.             |
| Required        | True                           |
| Name            | supplierID                     |
| Type            | string                         |
| Description     | ID of the supplier.            |
| Required        | True                           |

 **Requestbody**: 
None
 **Responsestatus**: `204`

 **Responsebody**: 
None## Remove a supplier
### `DELETE` `v1/products/{productID}/suppliers/{supplierID}`

| Parameters      | Description                    |
|------------------|---------------------------------|
| Name            | productID                      |
| Type            | string                         |
| Description     | ID of the product.             |
| Required        | True                           |
| Name            | supplierID                     |
| Type            | string                         |
| Description     | ID of the supplier.            |
| Required        | True                           |

 **Requestbody**: 
None
 **Responsestatus**: `204`

 **Responsebody**: 
None## Save a product assignment
### `POST` `v1/products/assignments`

| Parameters      | Description                    |
|------------------|---------------------------------|

 **Requestbody**: 
{'Sample': '{\r\n  "ProductID": "",\r\n  "BuyerID": "",\r\n  "UserGroupID": "",\r\n  "PriceScheduleID": ""\r\n}', 'Fields': [{'Name': 'ProductID', 'Type': 'string', 'Description': 'ID of the product. Required.', 'Required': True}, {'Name': 'BuyerID', 'Type': 'string', 'Description': 'ID of the buyer. Required.', 'Required': True}, {'Name': 'UserGroupID', 'Type': 'string', 'Description': 'ID of the user group.', 'Required': False}, {'Name': 'PriceScheduleID', 'Type': 'string', 'Description': 'ID of the price schedule.', 'Required': False}]}
 **Responsestatus**: `204`

 **Responsebody**: 
None## Get a list of product assignments
### `GET` `v1/products/assignments`

| Parameters      | Description                    |
|------------------|---------------------------------|
| Name            | productID                      |
| Type            | string                         |
| Description     | ID of the product.             |
| Required        | False                          |
| Name            | priceScheduleID                |
| Type            | string                         |
| Description     | ID of the price schedule.      |
| Required        | False                          |
| Name            | buyerID                        |
| Type            | string                         |
| Description     | ID of the buyer.               |
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
| Description     | Level of the product assignment. Possible values: User, Group, Company. |
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
{'Sample': '{\r\n  "Meta": {\r\n    "Page": 1,\r\n    "PageSize": 20,\r\n    "TotalCount": 25,\r\n    "TotalPages": 2,\r\n    "ItemRange": [\r\n      1,\r\n      20\r\n    ]\r\n  },\r\n  "Items": [\r\n    {\r\n      "ProductID": "",\r\n      "BuyerID": "",\r\n      "UserGroupID": "",\r\n      "PriceScheduleID": ""\r\n    }\r\n  ]\r\n}', 'Fields': [{'Name': 'ProductID', 'Type': 'string', 'Description': 'ID of the product.', 'Required': True}, {'Name': 'BuyerID', 'Type': 'string', 'Description': 'ID of the buyer.', 'Required': True}, {'Name': 'UserGroupID', 'Type': 'string', 'Description': 'ID of the user group.', 'Required': False}, {'Name': 'PriceScheduleID', 'Type': 'string', 'Description': 'ID of the price schedule.', 'Required': False}]}## Delete a product assignment
### `DELETE` `v1/products/{productID}/assignments/{buyerID}`

| Parameters      | Description                    |
|------------------|---------------------------------|
| Name            | productID                      |
| Type            | string                         |
| Description     | ID of the product.             |
| Required        | True                           |
| Name            | buyerID                        |
| Type            | string                         |
| Description     | ID of the buyer.               |
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