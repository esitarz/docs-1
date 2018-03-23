---
title: Products
date: 2018-03-23
category: API Reference
tags: Me And My Stuff
slug: MeProducts
---
"Me" is a container for read-only endpoints that return a filtered view
of things that the current buyer user is allowed to see, i.e. things
that they are assigned to either directly or as a member of a buyer
organization or user group. It also provides ways for a user to update
or change their own information.

---
## Get a list of products visible to this user
### `GET` `v1/me/products`

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
| Name            | depth                          |
| Type            | string                         |
| Description     | Depth of the product.          |
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
{'Sample': '{\r\n  "Meta": {\r\n    "Page": 1,\r\n    "PageSize": 20,\r\n    "TotalCount": 25,\r\n    "TotalPages": 2,\r\n    "ItemRange": [\r\n      1,\r\n      20\r\n    ]\r\n  },\r\n  "Items": [\r\n    {\r\n      "ID": "",\r\n      "PriceSchedule": {\r\n        "ID": "",\r\n        "Name": "",\r\n        "ApplyTax": false,\r\n        "ApplyShipping": false,\r\n        "MinQuantity": 0,\r\n        "MaxQuantity": 0,\r\n        "UseCumulativeQuantity": false,\r\n        "RestrictedQuantity": false,\r\n        "PriceBreaks": [\r\n          {\r\n            "Quantity": 0,\r\n            "Price": 0\r\n          }\r\n        ],\r\n        "xp": {}\r\n      },\r\n      "Name": "",\r\n      "Description": "",\r\n      "QuantityMultiplier": 0,\r\n      "ShipWeight": 0,\r\n      "ShipHeight": 0,\r\n      "ShipWidth": 0,\r\n      "ShipLength": 0,\r\n      "Active": false,\r\n      "SpecCount": 0,\r\n      "xp": {},\r\n      "VariantCount": 0,\r\n      "ShipFromAddressID": "",\r\n      "Inventory": {\r\n        "Enabled": false,\r\n        "NotificationPoint": 0,\r\n        "VariantLevelTracking": false,\r\n        "OrderCanExceed": false,\r\n        "QuantityAvailable": 0,\r\n        "LastUpdated": "2018-03-21T23:00:00+00:00"\r\n      },\r\n      "AutoForwardSupplierID": ""\r\n    }\r\n  ]\r\n}', 'Fields': [{'Name': 'ID', 'Type': 'string', 'Description': 'ID of the product.', 'Required': False}, {'Name': 'PriceSchedule', 'Type': 'object', 'Description': 'Price schedule of the product.', 'Required': False}, {'Name': 'Name', 'Type': 'string', 'Description': 'Name of the product.', 'Required': True}, {'Name': 'Description', 'Type': 'string', 'Description': 'Description of the product.', 'Required': False}, {'Name': 'QuantityMultiplier', 'Type': 'integer', 'Description': 'Quantity multiplier of the product.', 'Required': True}, {'Name': 'ShipWeight', 'Type': 'float', 'Description': 'Ship weight of the product.', 'Required': False}, {'Name': 'ShipHeight', 'Type': 'float', 'Description': 'Ship height of the product.', 'Required': False}, {'Name': 'ShipWidth', 'Type': 'float', 'Description': 'Ship width of the product.', 'Required': False}, {'Name': 'ShipLength', 'Type': 'float', 'Description': 'Ship length of the product.', 'Required': False}, {'Name': 'Active', 'Type': 'boolean', 'Description': 'Active of the product.', 'Required': False}, {'Name': 'SpecCount', 'Type': 'integer', 'Description': 'Spec count of the product.', 'Required': False}, {'Name': 'xp', 'Type': 'object', 'Description': 'Container for extended (custom) properties of the product.', 'Required': False}, {'Name': 'VariantCount', 'Type': 'integer', 'Description': 'Variant count of the product.', 'Required': False}, {'Name': 'ShipFromAddressID', 'Type': 'string', 'Description': 'ID of the ship from address.', 'Required': False}, {'Name': 'Inventory', 'Type': 'object', 'Description': 'Inventory of the product.', 'Required': False}, {'Name': 'AutoForwardSupplierID', 'Type': 'string', 'Description': 'ID of the auto forward supplier.', 'Required': False}]}## Get a single product
### `GET` `v1/me/products/{productID}`

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
{'Sample': '{\r\n  "ID": "",\r\n  "PriceSchedule": {\r\n    "ID": "",\r\n    "Name": "",\r\n    "ApplyTax": false,\r\n    "ApplyShipping": false,\r\n    "MinQuantity": 0,\r\n    "MaxQuantity": 0,\r\n    "UseCumulativeQuantity": false,\r\n    "RestrictedQuantity": false,\r\n    "PriceBreaks": [\r\n      {\r\n        "Quantity": 0,\r\n        "Price": 0\r\n      }\r\n    ],\r\n    "xp": {}\r\n  },\r\n  "Name": "",\r\n  "Description": "",\r\n  "QuantityMultiplier": 0,\r\n  "ShipWeight": 0,\r\n  "ShipHeight": 0,\r\n  "ShipWidth": 0,\r\n  "ShipLength": 0,\r\n  "Active": false,\r\n  "SpecCount": 0,\r\n  "xp": {},\r\n  "VariantCount": 0,\r\n  "ShipFromAddressID": "",\r\n  "Inventory": {\r\n    "Enabled": false,\r\n    "NotificationPoint": 0,\r\n    "VariantLevelTracking": false,\r\n    "OrderCanExceed": false,\r\n    "QuantityAvailable": 0,\r\n    "LastUpdated": "2018-03-21T23:00:00+00:00"\r\n  },\r\n  "AutoForwardSupplierID": ""\r\n}', 'Fields': [{'Name': 'ID', 'Type': 'string', 'Description': 'ID of the product.', 'Required': False}, {'Name': 'PriceSchedule', 'Type': 'object', 'Description': 'Price schedule of the product.', 'Required': False}, {'Name': 'Name', 'Type': 'string', 'Description': 'Name of the product.', 'Required': True}, {'Name': 'Description', 'Type': 'string', 'Description': 'Description of the product.', 'Required': False}, {'Name': 'QuantityMultiplier', 'Type': 'integer', 'Description': 'Quantity multiplier of the product.', 'Required': True}, {'Name': 'ShipWeight', 'Type': 'float', 'Description': 'Ship weight of the product.', 'Required': False}, {'Name': 'ShipHeight', 'Type': 'float', 'Description': 'Ship height of the product.', 'Required': False}, {'Name': 'ShipWidth', 'Type': 'float', 'Description': 'Ship width of the product.', 'Required': False}, {'Name': 'ShipLength', 'Type': 'float', 'Description': 'Ship length of the product.', 'Required': False}, {'Name': 'Active', 'Type': 'boolean', 'Description': 'Active of the product.', 'Required': False}, {'Name': 'SpecCount', 'Type': 'integer', 'Description': 'Spec count of the product.', 'Required': False}, {'Name': 'xp', 'Type': 'object', 'Description': 'Container for extended (custom) properties of the product.', 'Required': False}, {'Name': 'VariantCount', 'Type': 'integer', 'Description': 'Variant count of the product.', 'Required': False}, {'Name': 'ShipFromAddressID', 'Type': 'string', 'Description': 'ID of the ship from address.', 'Required': False}, {'Name': 'Inventory', 'Type': 'object', 'Description': 'Inventory of the product.', 'Required': False}, {'Name': 'AutoForwardSupplierID', 'Type': 'string', 'Description': 'ID of the auto forward supplier.', 'Required': False}]}## Get a list of specs visible to this user
### `GET` `v1/me/products/{productID}/specs`

| Parameters      | Description                    |
|------------------|---------------------------------|
| Name            | productID                      |
| Type            | string                         |
| Description     | ID of the product.             |
| Required        | True                           |
| Name            | catalogID                      |
| Type            | string                         |
| Description     | ID of the catalog.             |
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
{'Sample': '{\r\n  "Meta": {\r\n    "Page": 1,\r\n    "PageSize": 20,\r\n    "TotalCount": 25,\r\n    "TotalPages": 2,\r\n    "ItemRange": [\r\n      1,\r\n      20\r\n    ]\r\n  },\r\n  "Items": [\r\n    {\r\n      "Options": [\r\n        {\r\n          "ID": "",\r\n          "Value": "",\r\n          "ListOrder": 1,\r\n          "IsOpenText": false,\r\n          "PriceMarkupType": "NoMarkup",\r\n          "PriceMarkup": 0,\r\n          "xp": {}\r\n        }\r\n      ],\r\n      "ID": "",\r\n      "ListOrder": 1,\r\n      "Name": "",\r\n      "DefaultValue": "",\r\n      "Required": false,\r\n      "AllowOpenText": false,\r\n      "DefaultOptionID": "",\r\n      "DefinesVariant": false,\r\n      "xp": {}\r\n    }\r\n  ]\r\n}', 'Fields': [{'Name': 'Options', 'Type': 'array', 'Description': 'Options of the spec.', 'Required': False}, {'Name': 'ID', 'Type': 'string', 'Description': 'ID of the spec.', 'Required': False}, {'Name': 'ListOrder', 'Type': 'integer', 'Description': 'List order of the spec.', 'Required': False}, {'Name': 'Name', 'Type': 'string', 'Description': 'Name of the spec.', 'Required': True}, {'Name': 'DefaultValue', 'Type': 'string', 'Description': 'Default value of the spec.', 'Required': False}, {'Name': 'Required', 'Type': 'boolean', 'Description': 'Required of the spec.', 'Required': False}, {'Name': 'AllowOpenText', 'Type': 'boolean', 'Description': 'Allow open text of the spec.', 'Required': False}, {'Name': 'DefaultOptionID', 'Type': 'string', 'Description': 'ID of the default option.', 'Required': False}, {'Name': 'DefinesVariant', 'Type': 'boolean', 'Description': "True if each unique combinations of this Spec's Options map to unique Product Variants/SKUs.", 'Required': False}, {'Name': 'xp', 'Type': 'object', 'Description': 'Container for extended (custom) properties of the spec.', 'Required': False}]}## Get a single spec
### `GET` `v1/me/products/{productID}/specs/{specID}`

| Parameters      | Description                    |
|------------------|---------------------------------|
| Name            | productID                      |
| Type            | string                         |
| Description     | ID of the product.             |
| Required        | True                           |
| Name            | specID                         |
| Type            | string                         |
| Description     | ID of the spec.                |
| Required        | True                           |
| Name            | catalogID                      |
| Type            | string                         |
| Description     | ID of the catalog.             |
| Required        | False                          |

 **Requestbody**: 
None
 **Responsestatus**: `200`

 **Responsebody**: 
{'Sample': '{\r\n  "Options": [\r\n    {\r\n      "ID": "",\r\n      "Value": "",\r\n      "ListOrder": 1,\r\n      "IsOpenText": false,\r\n      "PriceMarkupType": "NoMarkup",\r\n      "PriceMarkup": 0,\r\n      "xp": {}\r\n    }\r\n  ],\r\n  "ID": "",\r\n  "ListOrder": 1,\r\n  "Name": "",\r\n  "DefaultValue": "",\r\n  "Required": false,\r\n  "AllowOpenText": false,\r\n  "DefaultOptionID": "",\r\n  "DefinesVariant": false,\r\n  "xp": {}\r\n}', 'Fields': [{'Name': 'Options', 'Type': 'array', 'Description': 'Options of the spec.', 'Required': False}, {'Name': 'ID', 'Type': 'string', 'Description': 'ID of the spec.', 'Required': False}, {'Name': 'ListOrder', 'Type': 'integer', 'Description': 'List order of the spec.', 'Required': False}, {'Name': 'Name', 'Type': 'string', 'Description': 'Name of the spec.', 'Required': True}, {'Name': 'DefaultValue', 'Type': 'string', 'Description': 'Default value of the spec.', 'Required': False}, {'Name': 'Required', 'Type': 'boolean', 'Description': 'Required of the spec.', 'Required': False}, {'Name': 'AllowOpenText', 'Type': 'boolean', 'Description': 'Allow open text of the spec.', 'Required': False}, {'Name': 'DefaultOptionID', 'Type': 'string', 'Description': 'ID of the default option.', 'Required': False}, {'Name': 'DefinesVariant', 'Type': 'boolean', 'Description': "True if each unique combinations of this Spec's Options map to unique Product Variants/SKUs.", 'Required': False}, {'Name': 'xp', 'Type': 'object', 'Description': 'Container for extended (custom) properties of the spec.', 'Required': False}]}