---
title: Price Schedules
date: 2018-03-23
category: API Reference
tags: Product Catalogs
slug: PriceSchedules
---
Price schedules allow the same product to be sold across multiple
channels. A price schedule may include quantity price breaks, min and
max quantity per order, whether to apply tax or shipping calculations,
or to what type of order the price schedule applies.

---

## Get a single price schedule
### `GET` `v1/priceschedules/{priceScheduleID}`

| Parameters      | Description                    |
|------------------|---------------------------------|
| Name            | priceScheduleID                |
| Type            | string                         |
| Description     | ID of the price schedule.      |
| Required        | True                           |

 **Requestbody**: 
None
 **Responsestatus**: `200`

 **Responsebody**: 
{'Sample': '{\r\n  "ID": "",\r\n  "Name": "",\r\n  "ApplyTax": false,\r\n  "ApplyShipping": false,\r\n  "MinQuantity": 0,\r\n  "MaxQuantity": 0,\r\n  "UseCumulativeQuantity": false,\r\n  "RestrictedQuantity": false,\r\n  "PriceBreaks": [\r\n    {\r\n      "Quantity": 0,\r\n      "Price": 0\r\n    }\r\n  ],\r\n  "xp": {}\r\n}', 'Fields': [{'Name': 'ID', 'Type': 'string', 'Description': 'ID of the price schedule.', 'Required': False}, {'Name': 'Name', 'Type': 'string', 'Description': 'Name of the price schedule.', 'Required': True}, {'Name': 'ApplyTax', 'Type': 'boolean', 'Description': 'Apply tax of the price schedule.', 'Required': False}, {'Name': 'ApplyShipping', 'Type': 'boolean', 'Description': 'Apply shipping of the price schedule.', 'Required': False}, {'Name': 'MinQuantity', 'Type': 'integer', 'Description': 'Min quantity of the price schedule.', 'Required': False}, {'Name': 'MaxQuantity', 'Type': 'integer', 'Description': 'Max quantity of the price schedule.', 'Required': False}, {'Name': 'UseCumulativeQuantity', 'Type': 'boolean', 'Description': 'Use cumulative quantity of the price schedule.', 'Required': False}, {'Name': 'RestrictedQuantity', 'Type': 'boolean', 'Description': 'Restricted quantity of the price schedule.', 'Required': False}, {'Name': 'PriceBreaks', 'Type': 'array', 'Description': 'Price breaks of the price schedule.', 'Required': False}, {'Name': 'xp', 'Type': 'object', 'Description': 'Container for extended (custom) properties of the price schedule.', 'Required': False}]}
## Get a list of price schedules
### `GET` `v1/priceschedules`

| Parameters      | Description                    |
|------------------|---------------------------------|
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
{'Sample': '{\r\n  "Meta": {\r\n    "Page": 1,\r\n    "PageSize": 20,\r\n    "TotalCount": 25,\r\n    "TotalPages": 2,\r\n    "ItemRange": [\r\n      1,\r\n      20\r\n    ]\r\n  },\r\n  "Items": [\r\n    {\r\n      "ID": "",\r\n      "Name": "",\r\n      "ApplyTax": false,\r\n      "ApplyShipping": false,\r\n      "MinQuantity": 0,\r\n      "MaxQuantity": 0,\r\n      "UseCumulativeQuantity": false,\r\n      "RestrictedQuantity": false,\r\n      "PriceBreaks": [\r\n        {\r\n          "Quantity": 0,\r\n          "Price": 0\r\n        }\r\n      ],\r\n      "xp": {}\r\n    }\r\n  ]\r\n}', 'Fields': [{'Name': 'ID', 'Type': 'string', 'Description': 'ID of the price schedule.', 'Required': False}, {'Name': 'Name', 'Type': 'string', 'Description': 'Name of the price schedule.', 'Required': True}, {'Name': 'ApplyTax', 'Type': 'boolean', 'Description': 'Apply tax of the price schedule.', 'Required': False}, {'Name': 'ApplyShipping', 'Type': 'boolean', 'Description': 'Apply shipping of the price schedule.', 'Required': False}, {'Name': 'MinQuantity', 'Type': 'integer', 'Description': 'Min quantity of the price schedule.', 'Required': False}, {'Name': 'MaxQuantity', 'Type': 'integer', 'Description': 'Max quantity of the price schedule.', 'Required': False}, {'Name': 'UseCumulativeQuantity', 'Type': 'boolean', 'Description': 'Use cumulative quantity of the price schedule.', 'Required': False}, {'Name': 'RestrictedQuantity', 'Type': 'boolean', 'Description': 'Restricted quantity of the price schedule.', 'Required': False}, {'Name': 'PriceBreaks', 'Type': 'array', 'Description': 'Price breaks of the price schedule.', 'Required': False}, {'Name': 'xp', 'Type': 'object', 'Description': 'Container for extended (custom) properties of the price schedule.', 'Required': False}]}
## Create a new price schedule
### `POST` `v1/priceschedules`

| Parameters      | Description                    |
|------------------|---------------------------------|

 **Requestbody**: 
{'Sample': '{\r\n  "ID": "",\r\n  "Name": "",\r\n  "ApplyTax": false,\r\n  "ApplyShipping": false,\r\n  "MinQuantity": 0,\r\n  "MaxQuantity": 0,\r\n  "UseCumulativeQuantity": false,\r\n  "RestrictedQuantity": false,\r\n  "PriceBreaks": [\r\n    {\r\n      "Quantity": 0,\r\n      "Price": 0\r\n    }\r\n  ],\r\n  "xp": {}\r\n}', 'Fields': [{'Name': 'ID', 'Type': 'string', 'Description': 'ID of the price schedule. Can only contain characters Aa-Zz, 0-9, -, and _. Searchable: priority level 1. Sortable: priority level 2.', 'Required': False}, {'Name': 'Name', 'Type': 'string', 'Description': 'Name of the price schedule. Required. Max length 100 characters. Searchable: priority level 2. Sortable: priority level 1.', 'Required': True}, {'Name': 'ApplyTax', 'Type': 'boolean', 'Description': 'Apply tax of the price schedule. Searchable: priority level 3.', 'Required': False}, {'Name': 'ApplyShipping', 'Type': 'boolean', 'Description': 'Apply shipping of the price schedule.', 'Required': False}, {'Name': 'MinQuantity', 'Type': 'integer', 'Description': 'Min quantity of the price schedule. Must be at least 1.', 'Required': False}, {'Name': 'MaxQuantity', 'Type': 'integer', 'Description': 'Max quantity of the price schedule.', 'Required': False}, {'Name': 'UseCumulativeQuantity', 'Type': 'boolean', 'Description': 'Use cumulative quantity of the price schedule.', 'Required': False}, {'Name': 'RestrictedQuantity', 'Type': 'boolean', 'Description': 'Restricted quantity of the price schedule.', 'Required': False}, {'Name': 'PriceBreaks', 'Type': 'array', 'Description': 'Price breaks of the price schedule.', 'Required': False}, {'Name': 'xp', 'Type': 'object', 'Description': 'Container for extended (custom) properties of the price schedule.', 'Required': False}]}
 **Responsestatus**: `201`

 **Responsebody**: 
{'Sample': '{\r\n  "ID": "",\r\n  "Name": "",\r\n  "ApplyTax": false,\r\n  "ApplyShipping": false,\r\n  "MinQuantity": 0,\r\n  "MaxQuantity": 0,\r\n  "UseCumulativeQuantity": false,\r\n  "RestrictedQuantity": false,\r\n  "PriceBreaks": [\r\n    {\r\n      "Quantity": 0,\r\n      "Price": 0\r\n    }\r\n  ],\r\n  "xp": {}\r\n}', 'Fields': [{'Name': 'ID', 'Type': 'string', 'Description': 'ID of the price schedule.', 'Required': False}, {'Name': 'Name', 'Type': 'string', 'Description': 'Name of the price schedule.', 'Required': True}, {'Name': 'ApplyTax', 'Type': 'boolean', 'Description': 'Apply tax of the price schedule.', 'Required': False}, {'Name': 'ApplyShipping', 'Type': 'boolean', 'Description': 'Apply shipping of the price schedule.', 'Required': False}, {'Name': 'MinQuantity', 'Type': 'integer', 'Description': 'Min quantity of the price schedule.', 'Required': False}, {'Name': 'MaxQuantity', 'Type': 'integer', 'Description': 'Max quantity of the price schedule.', 'Required': False}, {'Name': 'UseCumulativeQuantity', 'Type': 'boolean', 'Description': 'Use cumulative quantity of the price schedule.', 'Required': False}, {'Name': 'RestrictedQuantity', 'Type': 'boolean', 'Description': 'Restricted quantity of the price schedule.', 'Required': False}, {'Name': 'PriceBreaks', 'Type': 'array', 'Description': 'Price breaks of the price schedule.', 'Required': False}, {'Name': 'xp', 'Type': 'object', 'Description': 'Container for extended (custom) properties of the price schedule.', 'Required': False}]}
## Create or update a price schedule
### `PUT` `v1/priceschedules/{priceScheduleID}`

| Parameters      | Description                    |
|------------------|---------------------------------|
| Name            | priceScheduleID                |
| Type            | string                         |
| Description     | ID of the price schedule.      |
| Required        | True                           |

 **Requestbody**: 
{'Sample': '{\r\n  "ID": "",\r\n  "Name": "",\r\n  "ApplyTax": false,\r\n  "ApplyShipping": false,\r\n  "MinQuantity": 0,\r\n  "MaxQuantity": 0,\r\n  "UseCumulativeQuantity": false,\r\n  "RestrictedQuantity": false,\r\n  "PriceBreaks": [\r\n    {\r\n      "Quantity": 0,\r\n      "Price": 0\r\n    }\r\n  ],\r\n  "xp": {}\r\n}', 'Fields': [{'Name': 'ID', 'Type': 'string', 'Description': 'ID of the price schedule. Can only contain characters Aa-Zz, 0-9, -, and _. Searchable: priority level 1. Sortable: priority level 2.', 'Required': False}, {'Name': 'Name', 'Type': 'string', 'Description': 'Name of the price schedule. Required. Max length 100 characters. Searchable: priority level 2. Sortable: priority level 1.', 'Required': True}, {'Name': 'ApplyTax', 'Type': 'boolean', 'Description': 'Apply tax of the price schedule. Searchable: priority level 3.', 'Required': False}, {'Name': 'ApplyShipping', 'Type': 'boolean', 'Description': 'Apply shipping of the price schedule.', 'Required': False}, {'Name': 'MinQuantity', 'Type': 'integer', 'Description': 'Min quantity of the price schedule. Must be at least 1.', 'Required': False}, {'Name': 'MaxQuantity', 'Type': 'integer', 'Description': 'Max quantity of the price schedule.', 'Required': False}, {'Name': 'UseCumulativeQuantity', 'Type': 'boolean', 'Description': 'Use cumulative quantity of the price schedule.', 'Required': False}, {'Name': 'RestrictedQuantity', 'Type': 'boolean', 'Description': 'Restricted quantity of the price schedule.', 'Required': False}, {'Name': 'PriceBreaks', 'Type': 'array', 'Description': 'Price breaks of the price schedule.', 'Required': False}, {'Name': 'xp', 'Type': 'object', 'Description': 'Container for extended (custom) properties of the price schedule.', 'Required': False}]}
 **Responsestatus**: `200`

 **Responsebody**: 
{'Sample': '{\r\n  "ID": "",\r\n  "Name": "",\r\n  "ApplyTax": false,\r\n  "ApplyShipping": false,\r\n  "MinQuantity": 0,\r\n  "MaxQuantity": 0,\r\n  "UseCumulativeQuantity": false,\r\n  "RestrictedQuantity": false,\r\n  "PriceBreaks": [\r\n    {\r\n      "Quantity": 0,\r\n      "Price": 0\r\n    }\r\n  ],\r\n  "xp": {}\r\n}', 'Fields': [{'Name': 'ID', 'Type': 'string', 'Description': 'ID of the price schedule.', 'Required': False}, {'Name': 'Name', 'Type': 'string', 'Description': 'Name of the price schedule.', 'Required': True}, {'Name': 'ApplyTax', 'Type': 'boolean', 'Description': 'Apply tax of the price schedule.', 'Required': False}, {'Name': 'ApplyShipping', 'Type': 'boolean', 'Description': 'Apply shipping of the price schedule.', 'Required': False}, {'Name': 'MinQuantity', 'Type': 'integer', 'Description': 'Min quantity of the price schedule.', 'Required': False}, {'Name': 'MaxQuantity', 'Type': 'integer', 'Description': 'Max quantity of the price schedule.', 'Required': False}, {'Name': 'UseCumulativeQuantity', 'Type': 'boolean', 'Description': 'Use cumulative quantity of the price schedule.', 'Required': False}, {'Name': 'RestrictedQuantity', 'Type': 'boolean', 'Description': 'Restricted quantity of the price schedule.', 'Required': False}, {'Name': 'PriceBreaks', 'Type': 'array', 'Description': 'Price breaks of the price schedule.', 'Required': False}, {'Name': 'xp', 'Type': 'object', 'Description': 'Container for extended (custom) properties of the price schedule.', 'Required': False}]}
## Delete a price schedule
### `DELETE` `v1/priceschedules/{priceScheduleID}`

| Parameters      | Description                    |
|------------------|---------------------------------|
| Name            | priceScheduleID                |
| Type            | string                         |
| Description     | ID of the price schedule.      |
| Required        | True                           |

 **Requestbody**: 
None
 **Responsestatus**: `204`

 **Responsebody**: 
None
## Partially update a price schedule
### `PATCH` `v1/priceschedules/{priceScheduleID}`

| Parameters      | Description                    |
|------------------|---------------------------------|
| Name            | priceScheduleID                |
| Type            | string                         |
| Description     | ID of the price schedule.      |
| Required        | True                           |

 **Requestbody**: 
{'Sample': '{\r\n  "ID": "",\r\n  "Name": "",\r\n  "ApplyTax": false,\r\n  "ApplyShipping": false,\r\n  "MinQuantity": 0,\r\n  "MaxQuantity": 0,\r\n  "UseCumulativeQuantity": false,\r\n  "RestrictedQuantity": false,\r\n  "PriceBreaks": [\r\n    {\r\n      "Quantity": 0,\r\n      "Price": 0\r\n    }\r\n  ],\r\n  "xp": {}\r\n}', 'Fields': [{'Name': 'ID', 'Type': 'string', 'Description': 'ID of the price schedule. Can only contain characters Aa-Zz, 0-9, -, and _. Searchable: priority level 1. Sortable: priority level 2.', 'Required': False}, {'Name': 'Name', 'Type': 'string', 'Description': 'Name of the price schedule. Required. Max length 100 characters. Searchable: priority level 2. Sortable: priority level 1.', 'Required': True}, {'Name': 'ApplyTax', 'Type': 'boolean', 'Description': 'Apply tax of the price schedule. Searchable: priority level 3.', 'Required': False}, {'Name': 'ApplyShipping', 'Type': 'boolean', 'Description': 'Apply shipping of the price schedule.', 'Required': False}, {'Name': 'MinQuantity', 'Type': 'integer', 'Description': 'Min quantity of the price schedule. Must be at least 1.', 'Required': False}, {'Name': 'MaxQuantity', 'Type': 'integer', 'Description': 'Max quantity of the price schedule.', 'Required': False}, {'Name': 'UseCumulativeQuantity', 'Type': 'boolean', 'Description': 'Use cumulative quantity of the price schedule.', 'Required': False}, {'Name': 'RestrictedQuantity', 'Type': 'boolean', 'Description': 'Restricted quantity of the price schedule.', 'Required': False}, {'Name': 'PriceBreaks', 'Type': 'array', 'Description': 'Price breaks of the price schedule.', 'Required': False}, {'Name': 'xp', 'Type': 'object', 'Description': 'Container for extended (custom) properties of the price schedule.', 'Required': False}]}
 **Responsestatus**: `200`

 **Responsebody**: 
{'Sample': '{\r\n  "ID": "",\r\n  "Name": "",\r\n  "ApplyTax": false,\r\n  "ApplyShipping": false,\r\n  "MinQuantity": 0,\r\n  "MaxQuantity": 0,\r\n  "UseCumulativeQuantity": false,\r\n  "RestrictedQuantity": false,\r\n  "PriceBreaks": [\r\n    {\r\n      "Quantity": 0,\r\n      "Price": 0\r\n    }\r\n  ],\r\n  "xp": {}\r\n}', 'Fields': [{'Name': 'ID', 'Type': 'string', 'Description': 'ID of the price schedule.', 'Required': False}, {'Name': 'Name', 'Type': 'string', 'Description': 'Name of the price schedule.', 'Required': True}, {'Name': 'ApplyTax', 'Type': 'boolean', 'Description': 'Apply tax of the price schedule.', 'Required': False}, {'Name': 'ApplyShipping', 'Type': 'boolean', 'Description': 'Apply shipping of the price schedule.', 'Required': False}, {'Name': 'MinQuantity', 'Type': 'integer', 'Description': 'Min quantity of the price schedule.', 'Required': False}, {'Name': 'MaxQuantity', 'Type': 'integer', 'Description': 'Max quantity of the price schedule.', 'Required': False}, {'Name': 'UseCumulativeQuantity', 'Type': 'boolean', 'Description': 'Use cumulative quantity of the price schedule.', 'Required': False}, {'Name': 'RestrictedQuantity', 'Type': 'boolean', 'Description': 'Restricted quantity of the price schedule.', 'Required': False}, {'Name': 'PriceBreaks', 'Type': 'array', 'Description': 'Price breaks of the price schedule.', 'Required': False}, {'Name': 'xp', 'Type': 'object', 'Description': 'Container for extended (custom) properties of the price schedule.', 'Required': False}]}
## Save a price schedule price break
### `POST` `v1/priceschedules/{priceScheduleID}/PriceBreaks`

| Parameters      | Description                    |
|------------------|---------------------------------|
| Name            | priceScheduleID                |
| Type            | string                         |
| Description     | ID of the price schedule.      |
| Required        | True                           |

 **Requestbody**: 
{'Sample': '{\r\n  "Quantity": 0,\r\n  "Price": 0\r\n}', 'Fields': [{'Name': 'Quantity', 'Type': 'integer', 'Description': 'Quantity of the price break. Required. Must be at least 0.', 'Required': True}, {'Name': 'Price', 'Type': 'float', 'Description': 'Price of the price break. Required.', 'Required': True}]}
 **Responsestatus**: `201`

 **Responsebody**: 
{'Sample': '{\r\n  "ID": "",\r\n  "Name": "",\r\n  "ApplyTax": false,\r\n  "ApplyShipping": false,\r\n  "MinQuantity": 0,\r\n  "MaxQuantity": 0,\r\n  "UseCumulativeQuantity": false,\r\n  "RestrictedQuantity": false,\r\n  "PriceBreaks": [\r\n    {\r\n      "Quantity": 0,\r\n      "Price": 0\r\n    }\r\n  ],\r\n  "xp": {}\r\n}', 'Fields': [{'Name': 'ID', 'Type': 'string', 'Description': 'ID of the price schedule.', 'Required': False}, {'Name': 'Name', 'Type': 'string', 'Description': 'Name of the price schedule.', 'Required': True}, {'Name': 'ApplyTax', 'Type': 'boolean', 'Description': 'Apply tax of the price schedule.', 'Required': False}, {'Name': 'ApplyShipping', 'Type': 'boolean', 'Description': 'Apply shipping of the price schedule.', 'Required': False}, {'Name': 'MinQuantity', 'Type': 'integer', 'Description': 'Min quantity of the price schedule.', 'Required': False}, {'Name': 'MaxQuantity', 'Type': 'integer', 'Description': 'Max quantity of the price schedule.', 'Required': False}, {'Name': 'UseCumulativeQuantity', 'Type': 'boolean', 'Description': 'Use cumulative quantity of the price schedule.', 'Required': False}, {'Name': 'RestrictedQuantity', 'Type': 'boolean', 'Description': 'Restricted quantity of the price schedule.', 'Required': False}, {'Name': 'PriceBreaks', 'Type': 'array', 'Description': 'Price breaks of the price schedule.', 'Required': False}, {'Name': 'xp', 'Type': 'object', 'Description': 'Container for extended (custom) properties of the price schedule.', 'Required': False}]}
## Delete a price schedule price break
### `DELETE` `v1/priceschedules/{priceScheduleID}/PriceBreaks`

| Parameters      | Description                    |
|------------------|---------------------------------|
| Name            | priceScheduleID                |
| Type            | string                         |
| Description     | ID of the price schedule.      |
| Required        | True                           |
| Name            | quantity                       |
| Type            | integer                        |
| Description     | Quantity of the price schedule. |
| Required        | True                           |

 **Requestbody**: 
None
 **Responsestatus**: `204`

 **Responsebody**: 
None