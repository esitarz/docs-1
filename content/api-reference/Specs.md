---
title: Specs
date: 2018-03-23
category: API Reference
tags: Product Catalogs
slug: Specs
---
Specs are used to capture user input when adding a Product to an Order.
At its simplest, a spec is a name/value pair. A spec value may have a
price markup or markdown associated with it. In more advanced scenarios,
specs can drive the product SKU. For example, a product may be available
in 3 colors and 3 sizes and therefore have a total of 9 SKUs. **The
OrderCloud platform will choose the correct SKU based on the
user-selected color and size specs**.

---
## Get a single spec
### `GET` `v1/specs/{specID}`

| Parameters      | Description                    |
|------------------|---------------------------------|
| Name            | specID                         |
| Type            | string                         |
| Description     | ID of the spec.                |
| Required        | True                           |

 **Requestbody**: 
None
 **Responsestatus**: `200`

 **Responsebody**: 
{'Sample': '{\r\n  "OptionCount": 0,\r\n  "ID": "",\r\n  "ListOrder": 1,\r\n  "Name": "",\r\n  "DefaultValue": "",\r\n  "Required": false,\r\n  "AllowOpenText": false,\r\n  "DefaultOptionID": "",\r\n  "DefinesVariant": false,\r\n  "xp": {}\r\n}', 'Fields': [{'Name': 'OptionCount', 'Type': 'integer', 'Description': 'Option count of the spec.', 'Required': False}, {'Name': 'ID', 'Type': 'string', 'Description': 'ID of the spec.', 'Required': False}, {'Name': 'ListOrder', 'Type': 'integer', 'Description': 'List order of the spec.', 'Required': False}, {'Name': 'Name', 'Type': 'string', 'Description': 'Name of the spec.', 'Required': True}, {'Name': 'DefaultValue', 'Type': 'string', 'Description': 'Default value of the spec.', 'Required': False}, {'Name': 'Required', 'Type': 'boolean', 'Description': 'Required of the spec.', 'Required': False}, {'Name': 'AllowOpenText', 'Type': 'boolean', 'Description': 'Allow open text of the spec.', 'Required': False}, {'Name': 'DefaultOptionID', 'Type': 'string', 'Description': 'ID of the default option.', 'Required': False}, {'Name': 'DefinesVariant', 'Type': 'boolean', 'Description': "True if each unique combinations of this Spec's Options map to unique Product Variants/SKUs.", 'Required': False}, {'Name': 'xp', 'Type': 'object', 'Description': 'Container for extended (custom) properties of the spec.', 'Required': False}]}## Get a list of specs
### `GET` `v1/specs`

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
{'Sample': '{\r\n  "Meta": {\r\n    "Page": 1,\r\n    "PageSize": 20,\r\n    "TotalCount": 25,\r\n    "TotalPages": 2,\r\n    "ItemRange": [\r\n      1,\r\n      20\r\n    ]\r\n  },\r\n  "Items": [\r\n    {\r\n      "OptionCount": 0,\r\n      "ID": "",\r\n      "ListOrder": 1,\r\n      "Name": "",\r\n      "DefaultValue": "",\r\n      "Required": false,\r\n      "AllowOpenText": false,\r\n      "DefaultOptionID": "",\r\n      "DefinesVariant": false,\r\n      "xp": {}\r\n    }\r\n  ]\r\n}', 'Fields': [{'Name': 'OptionCount', 'Type': 'integer', 'Description': 'Option count of the spec.', 'Required': False}, {'Name': 'ID', 'Type': 'string', 'Description': 'ID of the spec.', 'Required': False}, {'Name': 'ListOrder', 'Type': 'integer', 'Description': 'List order of the spec.', 'Required': False}, {'Name': 'Name', 'Type': 'string', 'Description': 'Name of the spec.', 'Required': True}, {'Name': 'DefaultValue', 'Type': 'string', 'Description': 'Default value of the spec.', 'Required': False}, {'Name': 'Required', 'Type': 'boolean', 'Description': 'Required of the spec.', 'Required': False}, {'Name': 'AllowOpenText', 'Type': 'boolean', 'Description': 'Allow open text of the spec.', 'Required': False}, {'Name': 'DefaultOptionID', 'Type': 'string', 'Description': 'ID of the default option.', 'Required': False}, {'Name': 'DefinesVariant', 'Type': 'boolean', 'Description': "True if each unique combinations of this Spec's Options map to unique Product Variants/SKUs.", 'Required': False}, {'Name': 'xp', 'Type': 'object', 'Description': 'Container for extended (custom) properties of the spec.', 'Required': False}]}## Create a new spec
### `POST` `v1/specs`

| Parameters      | Description                    |
|------------------|---------------------------------|

 **Requestbody**: 
{'Sample': '{\r\n  "ID": "",\r\n  "ListOrder": 1,\r\n  "Name": "",\r\n  "DefaultValue": "",\r\n  "Required": false,\r\n  "AllowOpenText": false,\r\n  "DefaultOptionID": "",\r\n  "DefinesVariant": false,\r\n  "xp": {}\r\n}', 'Fields': [{'Name': 'ID', 'Type': 'string', 'Description': 'ID of the spec. Can only contain characters Aa-Zz, 0-9, -, and _. Searchable: priority level 3. Sortable: priority level 3.', 'Required': False}, {'Name': 'ListOrder', 'Type': 'integer', 'Description': 'List order of the spec. Searchable: priority level 2. Sortable: priority level 1.', 'Required': False}, {'Name': 'Name', 'Type': 'string', 'Description': 'Name of the spec. Required. Searchable: priority level 1. Sortable: priority level 2.', 'Required': True}, {'Name': 'DefaultValue', 'Type': 'string', 'Description': 'Default value of the spec. Max length 2000 characters.', 'Required': False}, {'Name': 'Required', 'Type': 'boolean', 'Description': 'Required of the spec. Searchable: priority level 4.', 'Required': False}, {'Name': 'AllowOpenText', 'Type': 'boolean', 'Description': 'Allow open text of the spec. Searchable: priority level 5.', 'Required': False}, {'Name': 'DefaultOptionID', 'Type': 'string', 'Description': 'ID of the default option.', 'Required': False}, {'Name': 'DefinesVariant', 'Type': 'boolean', 'Description': "True if each unique combinations of this Spec's Options map to unique Product Variants/SKUs.", 'Required': False}, {'Name': 'xp', 'Type': 'object', 'Description': 'Container for extended (custom) properties of the spec.', 'Required': False}]}
 **Responsestatus**: `201`

 **Responsebody**: 
{'Sample': '{\r\n  "OptionCount": 0,\r\n  "ID": "",\r\n  "ListOrder": 1,\r\n  "Name": "",\r\n  "DefaultValue": "",\r\n  "Required": false,\r\n  "AllowOpenText": false,\r\n  "DefaultOptionID": "",\r\n  "DefinesVariant": false,\r\n  "xp": {}\r\n}', 'Fields': [{'Name': 'OptionCount', 'Type': 'integer', 'Description': 'Option count of the spec.', 'Required': False}, {'Name': 'ID', 'Type': 'string', 'Description': 'ID of the spec.', 'Required': False}, {'Name': 'ListOrder', 'Type': 'integer', 'Description': 'List order of the spec.', 'Required': False}, {'Name': 'Name', 'Type': 'string', 'Description': 'Name of the spec.', 'Required': True}, {'Name': 'DefaultValue', 'Type': 'string', 'Description': 'Default value of the spec.', 'Required': False}, {'Name': 'Required', 'Type': 'boolean', 'Description': 'Required of the spec.', 'Required': False}, {'Name': 'AllowOpenText', 'Type': 'boolean', 'Description': 'Allow open text of the spec.', 'Required': False}, {'Name': 'DefaultOptionID', 'Type': 'string', 'Description': 'ID of the default option.', 'Required': False}, {'Name': 'DefinesVariant', 'Type': 'boolean', 'Description': "True if each unique combinations of this Spec's Options map to unique Product Variants/SKUs.", 'Required': False}, {'Name': 'xp', 'Type': 'object', 'Description': 'Container for extended (custom) properties of the spec.', 'Required': False}]}## Create or update a spec
### `PUT` `v1/specs/{specID}`

| Parameters      | Description                    |
|------------------|---------------------------------|
| Name            | specID                         |
| Type            | string                         |
| Description     | ID of the spec.                |
| Required        | True                           |

 **Requestbody**: 
{'Sample': '{\r\n  "ID": "",\r\n  "ListOrder": 1,\r\n  "Name": "",\r\n  "DefaultValue": "",\r\n  "Required": false,\r\n  "AllowOpenText": false,\r\n  "DefaultOptionID": "",\r\n  "DefinesVariant": false,\r\n  "xp": {}\r\n}', 'Fields': [{'Name': 'ID', 'Type': 'string', 'Description': 'ID of the spec. Can only contain characters Aa-Zz, 0-9, -, and _. Searchable: priority level 3. Sortable: priority level 3.', 'Required': False}, {'Name': 'ListOrder', 'Type': 'integer', 'Description': 'List order of the spec. Searchable: priority level 2. Sortable: priority level 1.', 'Required': False}, {'Name': 'Name', 'Type': 'string', 'Description': 'Name of the spec. Required. Searchable: priority level 1. Sortable: priority level 2.', 'Required': True}, {'Name': 'DefaultValue', 'Type': 'string', 'Description': 'Default value of the spec. Max length 2000 characters.', 'Required': False}, {'Name': 'Required', 'Type': 'boolean', 'Description': 'Required of the spec. Searchable: priority level 4.', 'Required': False}, {'Name': 'AllowOpenText', 'Type': 'boolean', 'Description': 'Allow open text of the spec. Searchable: priority level 5.', 'Required': False}, {'Name': 'DefaultOptionID', 'Type': 'string', 'Description': 'ID of the default option.', 'Required': False}, {'Name': 'DefinesVariant', 'Type': 'boolean', 'Description': "True if each unique combinations of this Spec's Options map to unique Product Variants/SKUs.", 'Required': False}, {'Name': 'xp', 'Type': 'object', 'Description': 'Container for extended (custom) properties of the spec.', 'Required': False}]}
 **Responsestatus**: `200`

 **Responsebody**: 
{'Sample': '{\r\n  "OptionCount": 0,\r\n  "ID": "",\r\n  "ListOrder": 1,\r\n  "Name": "",\r\n  "DefaultValue": "",\r\n  "Required": false,\r\n  "AllowOpenText": false,\r\n  "DefaultOptionID": "",\r\n  "DefinesVariant": false,\r\n  "xp": {}\r\n}', 'Fields': [{'Name': 'OptionCount', 'Type': 'integer', 'Description': 'Option count of the spec.', 'Required': False}, {'Name': 'ID', 'Type': 'string', 'Description': 'ID of the spec.', 'Required': False}, {'Name': 'ListOrder', 'Type': 'integer', 'Description': 'List order of the spec.', 'Required': False}, {'Name': 'Name', 'Type': 'string', 'Description': 'Name of the spec.', 'Required': True}, {'Name': 'DefaultValue', 'Type': 'string', 'Description': 'Default value of the spec.', 'Required': False}, {'Name': 'Required', 'Type': 'boolean', 'Description': 'Required of the spec.', 'Required': False}, {'Name': 'AllowOpenText', 'Type': 'boolean', 'Description': 'Allow open text of the spec.', 'Required': False}, {'Name': 'DefaultOptionID', 'Type': 'string', 'Description': 'ID of the default option.', 'Required': False}, {'Name': 'DefinesVariant', 'Type': 'boolean', 'Description': "True if each unique combinations of this Spec's Options map to unique Product Variants/SKUs.", 'Required': False}, {'Name': 'xp', 'Type': 'object', 'Description': 'Container for extended (custom) properties of the spec.', 'Required': False}]}## Delete a spec
### `DELETE` `v1/specs/{specID}`

| Parameters      | Description                    |
|------------------|---------------------------------|
| Name            | specID                         |
| Type            | string                         |
| Description     | ID of the spec.                |
| Required        | True                           |

 **Requestbody**: 
None
 **Responsestatus**: `204`

 **Responsebody**: 
None## Partially update a spec
### `PATCH` `v1/specs/{specID}`

| Parameters      | Description                    |
|------------------|---------------------------------|
| Name            | specID                         |
| Type            | string                         |
| Description     | ID of the spec.                |
| Required        | True                           |

 **Requestbody**: 
{'Sample': '{\r\n  "ID": "",\r\n  "ListOrder": 1,\r\n  "Name": "",\r\n  "DefaultValue": "",\r\n  "Required": false,\r\n  "AllowOpenText": false,\r\n  "DefaultOptionID": "",\r\n  "DefinesVariant": false,\r\n  "xp": {}\r\n}', 'Fields': [{'Name': 'ID', 'Type': 'string', 'Description': 'ID of the spec. Can only contain characters Aa-Zz, 0-9, -, and _. Searchable: priority level 3. Sortable: priority level 3.', 'Required': False}, {'Name': 'ListOrder', 'Type': 'integer', 'Description': 'List order of the spec. Searchable: priority level 2. Sortable: priority level 1.', 'Required': False}, {'Name': 'Name', 'Type': 'string', 'Description': 'Name of the spec. Required. Searchable: priority level 1. Sortable: priority level 2.', 'Required': True}, {'Name': 'DefaultValue', 'Type': 'string', 'Description': 'Default value of the spec. Max length 2000 characters.', 'Required': False}, {'Name': 'Required', 'Type': 'boolean', 'Description': 'Required of the spec. Searchable: priority level 4.', 'Required': False}, {'Name': 'AllowOpenText', 'Type': 'boolean', 'Description': 'Allow open text of the spec. Searchable: priority level 5.', 'Required': False}, {'Name': 'DefaultOptionID', 'Type': 'string', 'Description': 'ID of the default option.', 'Required': False}, {'Name': 'DefinesVariant', 'Type': 'boolean', 'Description': "True if each unique combinations of this Spec's Options map to unique Product Variants/SKUs.", 'Required': False}, {'Name': 'xp', 'Type': 'object', 'Description': 'Container for extended (custom) properties of the spec.', 'Required': False}]}
 **Responsestatus**: `200`

 **Responsebody**: 
{'Sample': '{\r\n  "OptionCount": 0,\r\n  "ID": "",\r\n  "ListOrder": 1,\r\n  "Name": "",\r\n  "DefaultValue": "",\r\n  "Required": false,\r\n  "AllowOpenText": false,\r\n  "DefaultOptionID": "",\r\n  "DefinesVariant": false,\r\n  "xp": {}\r\n}', 'Fields': [{'Name': 'OptionCount', 'Type': 'integer', 'Description': 'Option count of the spec.', 'Required': False}, {'Name': 'ID', 'Type': 'string', 'Description': 'ID of the spec.', 'Required': False}, {'Name': 'ListOrder', 'Type': 'integer', 'Description': 'List order of the spec.', 'Required': False}, {'Name': 'Name', 'Type': 'string', 'Description': 'Name of the spec.', 'Required': True}, {'Name': 'DefaultValue', 'Type': 'string', 'Description': 'Default value of the spec.', 'Required': False}, {'Name': 'Required', 'Type': 'boolean', 'Description': 'Required of the spec.', 'Required': False}, {'Name': 'AllowOpenText', 'Type': 'boolean', 'Description': 'Allow open text of the spec.', 'Required': False}, {'Name': 'DefaultOptionID', 'Type': 'string', 'Description': 'ID of the default option.', 'Required': False}, {'Name': 'DefinesVariant', 'Type': 'boolean', 'Description': "True if each unique combinations of this Spec's Options map to unique Product Variants/SKUs.", 'Required': False}, {'Name': 'xp', 'Type': 'object', 'Description': 'Container for extended (custom) properties of the spec.', 'Required': False}]}## Get a list of spec product assignments
### `GET` `v1/specs/productassignments`

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
{'Sample': '{\r\n  "Meta": {\r\n    "Page": 1,\r\n    "PageSize": 20,\r\n    "TotalCount": 25,\r\n    "TotalPages": 2,\r\n    "ItemRange": [\r\n      1,\r\n      20\r\n    ]\r\n  },\r\n  "Items": [\r\n    {\r\n      "SpecID": "",\r\n      "ProductID": "",\r\n      "DefaultValue": "",\r\n      "DefaultOptionID": ""\r\n    }\r\n  ]\r\n}', 'Fields': [{'Name': 'SpecID', 'Type': 'string', 'Description': 'ID of the spec.', 'Required': False}, {'Name': 'ProductID', 'Type': 'string', 'Description': 'ID of the product.', 'Required': False}, {'Name': 'DefaultValue', 'Type': 'string', 'Description': 'Optional. When defined, overrides the DefaultValue set on the Spec for just this Product.', 'Required': False}, {'Name': 'DefaultOptionID', 'Type': 'string', 'Description': 'Optional. When defined, overrides the DefaultOptionID set on the Spec for just this Product.', 'Required': False}]}## Delete a spec product assignment
### `DELETE` `v1/specs/{specID}/productassignments/{productID}`

| Parameters      | Description                    |
|------------------|---------------------------------|
| Name            | specID                         |
| Type            | string                         |
| Description     | ID of the spec.                |
| Required        | True                           |
| Name            | productID                      |
| Type            | string                         |
| Description     | ID of the product.             |
| Required        | True                           |

 **Requestbody**: 
None
 **Responsestatus**: `204`

 **Responsebody**: 
None## Save a spec product assignment
### `POST` `v1/specs/productassignments`

| Parameters      | Description                    |
|------------------|---------------------------------|

 **Requestbody**: 
{'Sample': '{\r\n  "SpecID": "",\r\n  "ProductID": "",\r\n  "DefaultValue": "",\r\n  "DefaultOptionID": ""\r\n}', 'Fields': [{'Name': 'SpecID', 'Type': 'string', 'Description': 'ID of the spec. Searchable: priority level 1. Sortable: priority level 1.', 'Required': False}, {'Name': 'ProductID', 'Type': 'string', 'Description': 'ID of the product. Searchable: priority level 2. Sortable: priority level 2.', 'Required': False}, {'Name': 'DefaultValue', 'Type': 'string', 'Description': 'Optional. When defined, overrides the DefaultValue set on the Spec for just this Product.', 'Required': False}, {'Name': 'DefaultOptionID', 'Type': 'string', 'Description': 'Optional. When defined, overrides the DefaultOptionID set on the Spec for just this Product.', 'Required': False}]}
 **Responsestatus**: `204`

 **Responsebody**: 
None## Create a new spec option
### `POST` `v1/specs/{specID}/options`

| Parameters      | Description                    |
|------------------|---------------------------------|
| Name            | specID                         |
| Type            | string                         |
| Description     | ID of the spec.                |
| Required        | True                           |

 **Requestbody**: 
{'Sample': '{\r\n  "ID": "",\r\n  "Value": "",\r\n  "ListOrder": 1,\r\n  "IsOpenText": false,\r\n  "PriceMarkupType": "NoMarkup",\r\n  "PriceMarkup": 0,\r\n  "xp": {}\r\n}', 'Fields': [{'Name': 'ID', 'Type': 'string', 'Description': 'ID of the spec option. Can only contain characters Aa-Zz, 0-9, -, and _. Searchable: priority level 2. Sortable: priority level 2.', 'Required': False}, {'Name': 'Value', 'Type': 'string', 'Description': 'Value of the spec option. Required. Max length 2000 characters. Searchable: priority level 1.', 'Required': True}, {'Name': 'ListOrder', 'Type': 'integer', 'Description': 'List order of the spec option. Searchable: priority level 4. Sortable: priority level 1.', 'Required': False}, {'Name': 'IsOpenText', 'Type': 'boolean', 'Description': 'Is open text of the spec option. Searchable: priority level 3.', 'Required': False}, {'Name': 'PriceMarkupType', 'Type': 'string', 'Description': 'Price markup type of the spec option. Searchable: priority level 5. Possible values: NoMarkup, AmountPerQuantity, AmountTotal, Percentage.', 'Required': False}, {'Name': 'PriceMarkup', 'Type': 'float', 'Description': 'Price markup of the spec option. Searchable: priority level 6.', 'Required': False}, {'Name': 'xp', 'Type': 'object', 'Description': 'Container for extended (custom) properties of the spec option.', 'Required': False}]}
 **Responsestatus**: `201`

 **Responsebody**: 
{'Sample': '{\r\n  "ID": "",\r\n  "Value": "",\r\n  "ListOrder": 1,\r\n  "IsOpenText": false,\r\n  "PriceMarkupType": "NoMarkup",\r\n  "PriceMarkup": 0,\r\n  "xp": {}\r\n}', 'Fields': [{'Name': 'ID', 'Type': 'string', 'Description': 'ID of the spec option.', 'Required': False}, {'Name': 'Value', 'Type': 'string', 'Description': 'Value of the spec option.', 'Required': True}, {'Name': 'ListOrder', 'Type': 'integer', 'Description': 'List order of the spec option.', 'Required': False}, {'Name': 'IsOpenText', 'Type': 'boolean', 'Description': 'Is open text of the spec option.', 'Required': False}, {'Name': 'PriceMarkupType', 'Type': 'string', 'Description': 'Price markup type of the spec option. Possible values: NoMarkup, AmountPerQuantity, AmountTotal, Percentage.', 'Required': False}, {'Name': 'PriceMarkup', 'Type': 'float', 'Description': 'Price markup of the spec option.', 'Required': False}, {'Name': 'xp', 'Type': 'object', 'Description': 'Container for extended (custom) properties of the spec option.', 'Required': False}]}## Get a list of spec options
### `GET` `v1/specs/{specID}/options`

| Parameters      | Description                    |
|------------------|---------------------------------|
| Name            | specID                         |
| Type            | string                         |
| Description     | ID of the spec.                |
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
{'Sample': '{\r\n  "Meta": {\r\n    "Page": 1,\r\n    "PageSize": 20,\r\n    "TotalCount": 25,\r\n    "TotalPages": 2,\r\n    "ItemRange": [\r\n      1,\r\n      20\r\n    ]\r\n  },\r\n  "Items": [\r\n    {\r\n      "ID": "",\r\n      "Value": "",\r\n      "ListOrder": 1,\r\n      "IsOpenText": false,\r\n      "PriceMarkupType": "NoMarkup",\r\n      "PriceMarkup": 0,\r\n      "xp": {}\r\n    }\r\n  ]\r\n}', 'Fields': [{'Name': 'ID', 'Type': 'string', 'Description': 'ID of the spec option.', 'Required': False}, {'Name': 'Value', 'Type': 'string', 'Description': 'Value of the spec option.', 'Required': True}, {'Name': 'ListOrder', 'Type': 'integer', 'Description': 'List order of the spec option.', 'Required': False}, {'Name': 'IsOpenText', 'Type': 'boolean', 'Description': 'Is open text of the spec option.', 'Required': False}, {'Name': 'PriceMarkupType', 'Type': 'string', 'Description': 'Price markup type of the spec option. Possible values: NoMarkup, AmountPerQuantity, AmountTotal, Percentage.', 'Required': False}, {'Name': 'PriceMarkup', 'Type': 'float', 'Description': 'Price markup of the spec option.', 'Required': False}, {'Name': 'xp', 'Type': 'object', 'Description': 'Container for extended (custom) properties of the spec option.', 'Required': False}]}## Create or update a spec option
### `PUT` `v1/specs/{specID}/options/{optionID}`

| Parameters      | Description                    |
|------------------|---------------------------------|
| Name            | specID                         |
| Type            | string                         |
| Description     | ID of the spec.                |
| Required        | True                           |
| Name            | optionID                       |
| Type            | string                         |
| Description     | ID of the option.              |
| Required        | True                           |

 **Requestbody**: 
{'Sample': '{\r\n  "ID": "",\r\n  "Value": "",\r\n  "ListOrder": 1,\r\n  "IsOpenText": false,\r\n  "PriceMarkupType": "NoMarkup",\r\n  "PriceMarkup": 0,\r\n  "xp": {}\r\n}', 'Fields': [{'Name': 'ID', 'Type': 'string', 'Description': 'ID of the spec option. Can only contain characters Aa-Zz, 0-9, -, and _. Searchable: priority level 2. Sortable: priority level 2.', 'Required': False}, {'Name': 'Value', 'Type': 'string', 'Description': 'Value of the spec option. Required. Max length 2000 characters. Searchable: priority level 1.', 'Required': True}, {'Name': 'ListOrder', 'Type': 'integer', 'Description': 'List order of the spec option. Searchable: priority level 4. Sortable: priority level 1.', 'Required': False}, {'Name': 'IsOpenText', 'Type': 'boolean', 'Description': 'Is open text of the spec option. Searchable: priority level 3.', 'Required': False}, {'Name': 'PriceMarkupType', 'Type': 'string', 'Description': 'Price markup type of the spec option. Searchable: priority level 5. Possible values: NoMarkup, AmountPerQuantity, AmountTotal, Percentage.', 'Required': False}, {'Name': 'PriceMarkup', 'Type': 'float', 'Description': 'Price markup of the spec option. Searchable: priority level 6.', 'Required': False}, {'Name': 'xp', 'Type': 'object', 'Description': 'Container for extended (custom) properties of the spec option.', 'Required': False}]}
 **Responsestatus**: `200`

 **Responsebody**: 
{'Sample': '{\r\n  "ID": "",\r\n  "Value": "",\r\n  "ListOrder": 1,\r\n  "IsOpenText": false,\r\n  "PriceMarkupType": "NoMarkup",\r\n  "PriceMarkup": 0,\r\n  "xp": {}\r\n}', 'Fields': [{'Name': 'ID', 'Type': 'string', 'Description': 'ID of the spec option.', 'Required': False}, {'Name': 'Value', 'Type': 'string', 'Description': 'Value of the spec option.', 'Required': True}, {'Name': 'ListOrder', 'Type': 'integer', 'Description': 'List order of the spec option.', 'Required': False}, {'Name': 'IsOpenText', 'Type': 'boolean', 'Description': 'Is open text of the spec option.', 'Required': False}, {'Name': 'PriceMarkupType', 'Type': 'string', 'Description': 'Price markup type of the spec option. Possible values: NoMarkup, AmountPerQuantity, AmountTotal, Percentage.', 'Required': False}, {'Name': 'PriceMarkup', 'Type': 'float', 'Description': 'Price markup of the spec option.', 'Required': False}, {'Name': 'xp', 'Type': 'object', 'Description': 'Container for extended (custom) properties of the spec option.', 'Required': False}]}## Partially update a spec option
### `PATCH` `v1/specs/{specID}/options/{optionID}`

| Parameters      | Description                    |
|------------------|---------------------------------|
| Name            | specID                         |
| Type            | string                         |
| Description     | ID of the spec.                |
| Required        | True                           |
| Name            | optionID                       |
| Type            | string                         |
| Description     | ID of the option.              |
| Required        | True                           |

 **Requestbody**: 
{'Sample': '{\r\n  "ID": "",\r\n  "Value": "",\r\n  "ListOrder": 1,\r\n  "IsOpenText": false,\r\n  "PriceMarkupType": "NoMarkup",\r\n  "PriceMarkup": 0,\r\n  "xp": {}\r\n}', 'Fields': [{'Name': 'ID', 'Type': 'string', 'Description': 'ID of the spec option. Can only contain characters Aa-Zz, 0-9, -, and _. Searchable: priority level 2. Sortable: priority level 2.', 'Required': False}, {'Name': 'Value', 'Type': 'string', 'Description': 'Value of the spec option. Required. Max length 2000 characters. Searchable: priority level 1.', 'Required': True}, {'Name': 'ListOrder', 'Type': 'integer', 'Description': 'List order of the spec option. Searchable: priority level 4. Sortable: priority level 1.', 'Required': False}, {'Name': 'IsOpenText', 'Type': 'boolean', 'Description': 'Is open text of the spec option. Searchable: priority level 3.', 'Required': False}, {'Name': 'PriceMarkupType', 'Type': 'string', 'Description': 'Price markup type of the spec option. Searchable: priority level 5. Possible values: NoMarkup, AmountPerQuantity, AmountTotal, Percentage.', 'Required': False}, {'Name': 'PriceMarkup', 'Type': 'float', 'Description': 'Price markup of the spec option. Searchable: priority level 6.', 'Required': False}, {'Name': 'xp', 'Type': 'object', 'Description': 'Container for extended (custom) properties of the spec option.', 'Required': False}]}
 **Responsestatus**: `200`

 **Responsebody**: 
{'Sample': '{\r\n  "ID": "",\r\n  "Value": "",\r\n  "ListOrder": 1,\r\n  "IsOpenText": false,\r\n  "PriceMarkupType": "NoMarkup",\r\n  "PriceMarkup": 0,\r\n  "xp": {}\r\n}', 'Fields': [{'Name': 'ID', 'Type': 'string', 'Description': 'ID of the spec option.', 'Required': False}, {'Name': 'Value', 'Type': 'string', 'Description': 'Value of the spec option.', 'Required': True}, {'Name': 'ListOrder', 'Type': 'integer', 'Description': 'List order of the spec option.', 'Required': False}, {'Name': 'IsOpenText', 'Type': 'boolean', 'Description': 'Is open text of the spec option.', 'Required': False}, {'Name': 'PriceMarkupType', 'Type': 'string', 'Description': 'Price markup type of the spec option. Possible values: NoMarkup, AmountPerQuantity, AmountTotal, Percentage.', 'Required': False}, {'Name': 'PriceMarkup', 'Type': 'float', 'Description': 'Price markup of the spec option.', 'Required': False}, {'Name': 'xp', 'Type': 'object', 'Description': 'Container for extended (custom) properties of the spec option.', 'Required': False}]}## Get a single spec option
### `GET` `v1/specs/{specID}/options/{optionID}`

| Parameters      | Description                    |
|------------------|---------------------------------|
| Name            | specID                         |
| Type            | string                         |
| Description     | ID of the spec.                |
| Required        | True                           |
| Name            | optionID                       |
| Type            | string                         |
| Description     | ID of the option.              |
| Required        | True                           |

 **Requestbody**: 
None
 **Responsestatus**: `200`

 **Responsebody**: 
{'Sample': '{\r\n  "ID": "",\r\n  "Value": "",\r\n  "ListOrder": 1,\r\n  "IsOpenText": false,\r\n  "PriceMarkupType": "NoMarkup",\r\n  "PriceMarkup": 0,\r\n  "xp": {}\r\n}', 'Fields': [{'Name': 'ID', 'Type': 'string', 'Description': 'ID of the spec option.', 'Required': False}, {'Name': 'Value', 'Type': 'string', 'Description': 'Value of the spec option.', 'Required': True}, {'Name': 'ListOrder', 'Type': 'integer', 'Description': 'List order of the spec option.', 'Required': False}, {'Name': 'IsOpenText', 'Type': 'boolean', 'Description': 'Is open text of the spec option.', 'Required': False}, {'Name': 'PriceMarkupType', 'Type': 'string', 'Description': 'Price markup type of the spec option. Possible values: NoMarkup, AmountPerQuantity, AmountTotal, Percentage.', 'Required': False}, {'Name': 'PriceMarkup', 'Type': 'float', 'Description': 'Price markup of the spec option.', 'Required': False}, {'Name': 'xp', 'Type': 'object', 'Description': 'Container for extended (custom) properties of the spec option.', 'Required': False}]}## Delete a spec option
### `DELETE` `v1/specs/{specID}/options/{optionID}`

| Parameters      | Description                    |
|------------------|---------------------------------|
| Name            | specID                         |
| Type            | string                         |
| Description     | ID of the spec.                |
| Required        | True                           |
| Name            | optionID                       |
| Type            | string                         |
| Description     | ID of the option.              |
| Required        | True                           |

 **Requestbody**: 
None
 **Responsestatus**: `204`

 **Responsebody**: 
None