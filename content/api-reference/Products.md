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

## `GET` `v1/products/{productID}`
Get a single product

| Parameters      | Description                    |
|------------------|---------------------------------|


| Parameters      | Description                    |
|------------------|---------------------------------|
| Name            | productID                      |
| Type            | string                         |
| Description     | ID of the product.             |
| Required        | True                           |

## Requestbody
**Responsestatus**: `200`

## Responsebody
```
{'DefaultPriceScheduleID': '', 'ID': '', 'Name': '', 'Description': '', 'QuantityMultiplier': 0, 'ShipWeight': 0, 'ShipHeight': 0, 'ShipWidth': 0, 'ShipLength': 0, 'Active': False, 'SpecCount': 0, 'xp': {}, 'VariantCount': 0, 'ShipFromAddressID': '', 'Inventory': {'Enabled': False, 'NotificationPoint': 0, 'VariantLevelTracking': False, 'OrderCanExceed': False, 'QuantityAvailable': 0, 'LastUpdated': '2018-03-21T23:00:00+00:00'}, 'AutoForwardSupplierID': ''}
```


| Parameters      | Description                    |
|------------------|---------------------------------|
| Name            | DefaultPriceScheduleID         |
| Type            | string                         |
| Description     | ID of the default price schedule. |
| Required        | False                          |


| Parameters      | Description                    |
|------------------|---------------------------------|
| Name            | ID                             |
| Type            | string                         |
| Description     | ID of the product.             |
| Required        | False                          |


| Parameters      | Description                    |
|------------------|---------------------------------|
| Name            | Name                           |
| Type            | string                         |
| Description     | Name of the product.           |
| Required        | True                           |


| Parameters      | Description                    |
|------------------|---------------------------------|
| Name            | Description                    |
| Type            | string                         |
| Description     | Description of the product.    |
| Required        | False                          |


| Parameters      | Description                    |
|------------------|---------------------------------|
| Name            | QuantityMultiplier             |
| Type            | integer                        |
| Description     | Quantity multiplier of the product. |
| Required        | True                           |


| Parameters      | Description                    |
|------------------|---------------------------------|
| Name            | ShipWeight                     |
| Type            | float                          |
| Description     | Ship weight of the product.    |
| Required        | False                          |


| Parameters      | Description                    |
|------------------|---------------------------------|
| Name            | ShipHeight                     |
| Type            | float                          |
| Description     | Ship height of the product.    |
| Required        | False                          |


| Parameters      | Description                    |
|------------------|---------------------------------|
| Name            | ShipWidth                      |
| Type            | float                          |
| Description     | Ship width of the product.     |
| Required        | False                          |


| Parameters      | Description                    |
|------------------|---------------------------------|
| Name            | ShipLength                     |
| Type            | float                          |
| Description     | Ship length of the product.    |
| Required        | False                          |


| Parameters      | Description                    |
|------------------|---------------------------------|
| Name            | Active                         |
| Type            | boolean                        |
| Description     | Active of the product.         |
| Required        | False                          |


| Parameters      | Description                    |
|------------------|---------------------------------|
| Name            | SpecCount                      |
| Type            | integer                        |
| Description     | Spec count of the product.     |
| Required        | False                          |


| Parameters      | Description                    |
|------------------|---------------------------------|
| Name            | xp                             |
| Type            | object                         |
| Description     | Container for extended (custom) properties of the product. |
| Required        | False                          |


| Parameters      | Description                    |
|------------------|---------------------------------|
| Name            | VariantCount                   |
| Type            | integer                        |
| Description     | Variant count of the product.  |
| Required        | False                          |


| Parameters      | Description                    |
|------------------|---------------------------------|
| Name            | ShipFromAddressID              |
| Type            | string                         |
| Description     | ID of the ship from address.   |
| Required        | False                          |


| Parameters      | Description                    |
|------------------|---------------------------------|
| Name            | Inventory                      |
| Type            | object                         |
| Description     | Inventory of the product.      |
| Required        | False                          |


| Parameters      | Description                    |
|------------------|---------------------------------|
| Name            | AutoForwardSupplierID          |
| Type            | string                         |
| Description     | ID of the auto forward supplier. |
| Required        | False                          |

## `GET` `v1/products`
Get a list of products

| Parameters      | Description                    |
|------------------|---------------------------------|


| Parameters      | Description                    |
|------------------|---------------------------------|
| Name            | catalogID                      |
| Type            | string                         |
| Description     | ID of the catalog.             |
| Required        | False                          |


| Parameters      | Description                    |
|------------------|---------------------------------|
| Name            | categoryID                     |
| Type            | string                         |
| Description     | ID of the category.            |
| Required        | False                          |


| Parameters      | Description                    |
|------------------|---------------------------------|
| Name            | supplierID                     |
| Type            | string                         |
| Description     | ID of the supplier.            |
| Required        | False                          |


| Parameters      | Description                    |
|------------------|---------------------------------|
| Name            | search                         |
| Type            | string                         |
| Description     | Word or phrase to search for.  |
| Required        | False                          |


| Parameters      | Description                    |
|------------------|---------------------------------|
| Name            | searchOn                       |
| Type            | string                         |
| Description     | Comma-delimited list of fields to search on. |
| Required        | False                          |


| Parameters      | Description                    |
|------------------|---------------------------------|
| Name            | sortBy                         |
| Type            | string                         |
| Description     | Comma-delimited list of fields to sort by. |
| Required        | False                          |


| Parameters      | Description                    |
|------------------|---------------------------------|
| Name            | page                           |
| Type            | integer                        |
| Description     | Page of results to return. Default: 1 |
| Required        | False                          |


| Parameters      | Description                    |
|------------------|---------------------------------|
| Name            | pageSize                       |
| Type            | integer                        |
| Description     | Number of results to return per page. Default: 20, max: 100. |
| Required        | False                          |


| Parameters      | Description                    |
|------------------|---------------------------------|
| Name            | filters                        |
| Type            | object                         |
| Description     | Any additional key/value pairs passed in the query string are interpretted as filters. Valid keys are top-level properties of the returned model or 'xp.???' |
| Required        | False                          |

## Requestbody
**Responsestatus**: `200`

## Responsebody
```
{'Meta': {'Page': 1, 'PageSize': 20, 'TotalCount': 25, 'TotalPages': 2, 'ItemRange': [1, 20]}, 'Items': [{'DefaultPriceScheduleID': '', 'ID': '', 'Name': '', 'Description': '', 'QuantityMultiplier': 0, 'ShipWeight': 0, 'ShipHeight': 0, 'ShipWidth': 0, 'ShipLength': 0, 'Active': False, 'SpecCount': 0, 'xp': {}, 'VariantCount': 0, 'ShipFromAddressID': '', 'Inventory': {'Enabled': False, 'NotificationPoint': 0, 'VariantLevelTracking': False, 'OrderCanExceed': False, 'QuantityAvailable': 0, 'LastUpdated': '2018-03-21T23:00:00+00:00'}, 'AutoForwardSupplierID': ''}]}
```


| Parameters      | Description                    |
|------------------|---------------------------------|
| Name            | DefaultPriceScheduleID         |
| Type            | string                         |
| Description     | ID of the default price schedule. |
| Required        | False                          |


| Parameters      | Description                    |
|------------------|---------------------------------|
| Name            | ID                             |
| Type            | string                         |
| Description     | ID of the product.             |
| Required        | False                          |


| Parameters      | Description                    |
|------------------|---------------------------------|
| Name            | Name                           |
| Type            | string                         |
| Description     | Name of the product.           |
| Required        | True                           |


| Parameters      | Description                    |
|------------------|---------------------------------|
| Name            | Description                    |
| Type            | string                         |
| Description     | Description of the product.    |
| Required        | False                          |


| Parameters      | Description                    |
|------------------|---------------------------------|
| Name            | QuantityMultiplier             |
| Type            | integer                        |
| Description     | Quantity multiplier of the product. |
| Required        | True                           |


| Parameters      | Description                    |
|------------------|---------------------------------|
| Name            | ShipWeight                     |
| Type            | float                          |
| Description     | Ship weight of the product.    |
| Required        | False                          |


| Parameters      | Description                    |
|------------------|---------------------------------|
| Name            | ShipHeight                     |
| Type            | float                          |
| Description     | Ship height of the product.    |
| Required        | False                          |


| Parameters      | Description                    |
|------------------|---------------------------------|
| Name            | ShipWidth                      |
| Type            | float                          |
| Description     | Ship width of the product.     |
| Required        | False                          |


| Parameters      | Description                    |
|------------------|---------------------------------|
| Name            | ShipLength                     |
| Type            | float                          |
| Description     | Ship length of the product.    |
| Required        | False                          |


| Parameters      | Description                    |
|------------------|---------------------------------|
| Name            | Active                         |
| Type            | boolean                        |
| Description     | Active of the product.         |
| Required        | False                          |


| Parameters      | Description                    |
|------------------|---------------------------------|
| Name            | SpecCount                      |
| Type            | integer                        |
| Description     | Spec count of the product.     |
| Required        | False                          |


| Parameters      | Description                    |
|------------------|---------------------------------|
| Name            | xp                             |
| Type            | object                         |
| Description     | Container for extended (custom) properties of the product. |
| Required        | False                          |


| Parameters      | Description                    |
|------------------|---------------------------------|
| Name            | VariantCount                   |
| Type            | integer                        |
| Description     | Variant count of the product.  |
| Required        | False                          |


| Parameters      | Description                    |
|------------------|---------------------------------|
| Name            | ShipFromAddressID              |
| Type            | string                         |
| Description     | ID of the ship from address.   |
| Required        | False                          |


| Parameters      | Description                    |
|------------------|---------------------------------|
| Name            | Inventory                      |
| Type            | object                         |
| Description     | Inventory of the product.      |
| Required        | False                          |


| Parameters      | Description                    |
|------------------|---------------------------------|
| Name            | AutoForwardSupplierID          |
| Type            | string                         |
| Description     | ID of the auto forward supplier. |
| Required        | False                          |

## `POST` `v1/products`
Create a new product
## Requestbody
```
{'DefaultPriceScheduleID': '', 'ID': '', 'Name': '', 'Description': '', 'QuantityMultiplier': 0, 'ShipWeight': 0, 'ShipHeight': 0, 'ShipWidth': 0, 'ShipLength': 0, 'Active': False, 'xp': {}, 'ShipFromAddressID': '', 'Inventory': {'Enabled': False, 'NotificationPoint': 0, 'VariantLevelTracking': False, 'OrderCanExceed': False, 'QuantityAvailable': 0}, 'AutoForwardSupplierID': ''}
```

```
[{'Name': 'DefaultPriceScheduleID', 'Type': 'string', 'Description': 'ID of the default price schedule.', 'Required': False}, {'Name': 'ID', 'Type': 'string', 'Description': 'ID of the product. Can only contain characters Aa-Zz, 0-9, -, and _. Searchable: priority level 1. Sortable: priority level 2.', 'Required': False}, {'Name': 'Name', 'Type': 'string', 'Description': 'Name of the product. Required. Max length 100 characters. Searchable: priority level 2. Sortable: priority level 1.', 'Required': True}, {'Name': 'Description', 'Type': 'string', 'Description': 'Description of the product. Max length 2000 characters. Searchable: priority level 3.', 'Required': False}, {'Name': 'QuantityMultiplier', 'Type': 'integer', 'Description': 'Quantity multiplier of the product. Required. Must be at least 1.', 'Required': True}, {'Name': 'ShipWeight', 'Type': 'float', 'Description': 'Ship weight of the product.', 'Required': False}, {'Name': 'ShipHeight', 'Type': 'float', 'Description': 'Ship height of the product.', 'Required': False}, {'Name': 'ShipWidth', 'Type': 'float', 'Description': 'Ship width of the product.', 'Required': False}, {'Name': 'ShipLength', 'Type': 'float', 'Description': 'Ship length of the product.', 'Required': False}, {'Name': 'Active', 'Type': 'boolean', 'Description': 'Active of the product.', 'Required': False}, {'Name': 'xp', 'Type': 'object', 'Description': 'Container for extended (custom) properties of the product.', 'Required': False}, {'Name': 'ShipFromAddressID', 'Type': 'string', 'Description': 'ID of the ship from address.', 'Required': False}, {'Name': 'Inventory', 'Type': 'object', 'Description': 'Inventory of the product.', 'Required': False}, {'Name': 'AutoForwardSupplierID', 'Type': 'string', 'Description': 'ID of the auto forward supplier.', 'Required': False}]
```

**Responsestatus**: `201`

## Responsebody
```
{'DefaultPriceScheduleID': '', 'ID': '', 'Name': '', 'Description': '', 'QuantityMultiplier': 0, 'ShipWeight': 0, 'ShipHeight': 0, 'ShipWidth': 0, 'ShipLength': 0, 'Active': False, 'SpecCount': 0, 'xp': {}, 'VariantCount': 0, 'ShipFromAddressID': '', 'Inventory': {'Enabled': False, 'NotificationPoint': 0, 'VariantLevelTracking': False, 'OrderCanExceed': False, 'QuantityAvailable': 0, 'LastUpdated': '2018-03-21T23:00:00+00:00'}, 'AutoForwardSupplierID': ''}
```


| Parameters      | Description                    |
|------------------|---------------------------------|
| Name            | DefaultPriceScheduleID         |
| Type            | string                         |
| Description     | ID of the default price schedule. |
| Required        | False                          |


| Parameters      | Description                    |
|------------------|---------------------------------|
| Name            | ID                             |
| Type            | string                         |
| Description     | ID of the product.             |
| Required        | False                          |


| Parameters      | Description                    |
|------------------|---------------------------------|
| Name            | Name                           |
| Type            | string                         |
| Description     | Name of the product.           |
| Required        | True                           |


| Parameters      | Description                    |
|------------------|---------------------------------|
| Name            | Description                    |
| Type            | string                         |
| Description     | Description of the product.    |
| Required        | False                          |


| Parameters      | Description                    |
|------------------|---------------------------------|
| Name            | QuantityMultiplier             |
| Type            | integer                        |
| Description     | Quantity multiplier of the product. |
| Required        | True                           |


| Parameters      | Description                    |
|------------------|---------------------------------|
| Name            | ShipWeight                     |
| Type            | float                          |
| Description     | Ship weight of the product.    |
| Required        | False                          |


| Parameters      | Description                    |
|------------------|---------------------------------|
| Name            | ShipHeight                     |
| Type            | float                          |
| Description     | Ship height of the product.    |
| Required        | False                          |


| Parameters      | Description                    |
|------------------|---------------------------------|
| Name            | ShipWidth                      |
| Type            | float                          |
| Description     | Ship width of the product.     |
| Required        | False                          |


| Parameters      | Description                    |
|------------------|---------------------------------|
| Name            | ShipLength                     |
| Type            | float                          |
| Description     | Ship length of the product.    |
| Required        | False                          |


| Parameters      | Description                    |
|------------------|---------------------------------|
| Name            | Active                         |
| Type            | boolean                        |
| Description     | Active of the product.         |
| Required        | False                          |


| Parameters      | Description                    |
|------------------|---------------------------------|
| Name            | SpecCount                      |
| Type            | integer                        |
| Description     | Spec count of the product.     |
| Required        | False                          |


| Parameters      | Description                    |
|------------------|---------------------------------|
| Name            | xp                             |
| Type            | object                         |
| Description     | Container for extended (custom) properties of the product. |
| Required        | False                          |


| Parameters      | Description                    |
|------------------|---------------------------------|
| Name            | VariantCount                   |
| Type            | integer                        |
| Description     | Variant count of the product.  |
| Required        | False                          |


| Parameters      | Description                    |
|------------------|---------------------------------|
| Name            | ShipFromAddressID              |
| Type            | string                         |
| Description     | ID of the ship from address.   |
| Required        | False                          |


| Parameters      | Description                    |
|------------------|---------------------------------|
| Name            | Inventory                      |
| Type            | object                         |
| Description     | Inventory of the product.      |
| Required        | False                          |


| Parameters      | Description                    |
|------------------|---------------------------------|
| Name            | AutoForwardSupplierID          |
| Type            | string                         |
| Description     | ID of the auto forward supplier. |
| Required        | False                          |

## `PUT` `v1/products/{productID}`
Create or update a product

| Parameters      | Description                    |
|------------------|---------------------------------|


| Parameters      | Description                    |
|------------------|---------------------------------|
| Name            | productID                      |
| Type            | string                         |
| Description     | ID of the product.             |
| Required        | True                           |

## Requestbody
```
{'DefaultPriceScheduleID': '', 'ID': '', 'Name': '', 'Description': '', 'QuantityMultiplier': 0, 'ShipWeight': 0, 'ShipHeight': 0, 'ShipWidth': 0, 'ShipLength': 0, 'Active': False, 'xp': {}, 'ShipFromAddressID': '', 'Inventory': {'Enabled': False, 'NotificationPoint': 0, 'VariantLevelTracking': False, 'OrderCanExceed': False, 'QuantityAvailable': 0}, 'AutoForwardSupplierID': ''}
```

```
[{'Name': 'DefaultPriceScheduleID', 'Type': 'string', 'Description': 'ID of the default price schedule.', 'Required': False}, {'Name': 'ID', 'Type': 'string', 'Description': 'ID of the product. Can only contain characters Aa-Zz, 0-9, -, and _. Searchable: priority level 1. Sortable: priority level 2.', 'Required': False}, {'Name': 'Name', 'Type': 'string', 'Description': 'Name of the product. Required. Max length 100 characters. Searchable: priority level 2. Sortable: priority level 1.', 'Required': True}, {'Name': 'Description', 'Type': 'string', 'Description': 'Description of the product. Max length 2000 characters. Searchable: priority level 3.', 'Required': False}, {'Name': 'QuantityMultiplier', 'Type': 'integer', 'Description': 'Quantity multiplier of the product. Required. Must be at least 1.', 'Required': True}, {'Name': 'ShipWeight', 'Type': 'float', 'Description': 'Ship weight of the product.', 'Required': False}, {'Name': 'ShipHeight', 'Type': 'float', 'Description': 'Ship height of the product.', 'Required': False}, {'Name': 'ShipWidth', 'Type': 'float', 'Description': 'Ship width of the product.', 'Required': False}, {'Name': 'ShipLength', 'Type': 'float', 'Description': 'Ship length of the product.', 'Required': False}, {'Name': 'Active', 'Type': 'boolean', 'Description': 'Active of the product.', 'Required': False}, {'Name': 'xp', 'Type': 'object', 'Description': 'Container for extended (custom) properties of the product.', 'Required': False}, {'Name': 'ShipFromAddressID', 'Type': 'string', 'Description': 'ID of the ship from address.', 'Required': False}, {'Name': 'Inventory', 'Type': 'object', 'Description': 'Inventory of the product.', 'Required': False}, {'Name': 'AutoForwardSupplierID', 'Type': 'string', 'Description': 'ID of the auto forward supplier.', 'Required': False}]
```

**Responsestatus**: `200`

## Responsebody
```
{'DefaultPriceScheduleID': '', 'ID': '', 'Name': '', 'Description': '', 'QuantityMultiplier': 0, 'ShipWeight': 0, 'ShipHeight': 0, 'ShipWidth': 0, 'ShipLength': 0, 'Active': False, 'SpecCount': 0, 'xp': {}, 'VariantCount': 0, 'ShipFromAddressID': '', 'Inventory': {'Enabled': False, 'NotificationPoint': 0, 'VariantLevelTracking': False, 'OrderCanExceed': False, 'QuantityAvailable': 0, 'LastUpdated': '2018-03-21T23:00:00+00:00'}, 'AutoForwardSupplierID': ''}
```


| Parameters      | Description                    |
|------------------|---------------------------------|
| Name            | DefaultPriceScheduleID         |
| Type            | string                         |
| Description     | ID of the default price schedule. |
| Required        | False                          |


| Parameters      | Description                    |
|------------------|---------------------------------|
| Name            | ID                             |
| Type            | string                         |
| Description     | ID of the product.             |
| Required        | False                          |


| Parameters      | Description                    |
|------------------|---------------------------------|
| Name            | Name                           |
| Type            | string                         |
| Description     | Name of the product.           |
| Required        | True                           |


| Parameters      | Description                    |
|------------------|---------------------------------|
| Name            | Description                    |
| Type            | string                         |
| Description     | Description of the product.    |
| Required        | False                          |


| Parameters      | Description                    |
|------------------|---------------------------------|
| Name            | QuantityMultiplier             |
| Type            | integer                        |
| Description     | Quantity multiplier of the product. |
| Required        | True                           |


| Parameters      | Description                    |
|------------------|---------------------------------|
| Name            | ShipWeight                     |
| Type            | float                          |
| Description     | Ship weight of the product.    |
| Required        | False                          |


| Parameters      | Description                    |
|------------------|---------------------------------|
| Name            | ShipHeight                     |
| Type            | float                          |
| Description     | Ship height of the product.    |
| Required        | False                          |


| Parameters      | Description                    |
|------------------|---------------------------------|
| Name            | ShipWidth                      |
| Type            | float                          |
| Description     | Ship width of the product.     |
| Required        | False                          |


| Parameters      | Description                    |
|------------------|---------------------------------|
| Name            | ShipLength                     |
| Type            | float                          |
| Description     | Ship length of the product.    |
| Required        | False                          |


| Parameters      | Description                    |
|------------------|---------------------------------|
| Name            | Active                         |
| Type            | boolean                        |
| Description     | Active of the product.         |
| Required        | False                          |


| Parameters      | Description                    |
|------------------|---------------------------------|
| Name            | SpecCount                      |
| Type            | integer                        |
| Description     | Spec count of the product.     |
| Required        | False                          |


| Parameters      | Description                    |
|------------------|---------------------------------|
| Name            | xp                             |
| Type            | object                         |
| Description     | Container for extended (custom) properties of the product. |
| Required        | False                          |


| Parameters      | Description                    |
|------------------|---------------------------------|
| Name            | VariantCount                   |
| Type            | integer                        |
| Description     | Variant count of the product.  |
| Required        | False                          |


| Parameters      | Description                    |
|------------------|---------------------------------|
| Name            | ShipFromAddressID              |
| Type            | string                         |
| Description     | ID of the ship from address.   |
| Required        | False                          |


| Parameters      | Description                    |
|------------------|---------------------------------|
| Name            | Inventory                      |
| Type            | object                         |
| Description     | Inventory of the product.      |
| Required        | False                          |


| Parameters      | Description                    |
|------------------|---------------------------------|
| Name            | AutoForwardSupplierID          |
| Type            | string                         |
| Description     | ID of the auto forward supplier. |
| Required        | False                          |

## `DELETE` `v1/products/{productID}`
Delete a product

| Parameters      | Description                    |
|------------------|---------------------------------|


| Parameters      | Description                    |
|------------------|---------------------------------|
| Name            | productID                      |
| Type            | string                         |
| Description     | ID of the product.             |
| Required        | True                           |

## Requestbody
**Responsestatus**: `204`

## Responsebody
## `PATCH` `v1/products/{productID}`
Partially update a product

| Parameters      | Description                    |
|------------------|---------------------------------|


| Parameters      | Description                    |
|------------------|---------------------------------|
| Name            | productID                      |
| Type            | string                         |
| Description     | ID of the product.             |
| Required        | True                           |

## Requestbody
```
{'DefaultPriceScheduleID': '', 'ID': '', 'Name': '', 'Description': '', 'QuantityMultiplier': 0, 'ShipWeight': 0, 'ShipHeight': 0, 'ShipWidth': 0, 'ShipLength': 0, 'Active': False, 'xp': {}, 'ShipFromAddressID': '', 'Inventory': {'Enabled': False, 'NotificationPoint': 0, 'VariantLevelTracking': False, 'OrderCanExceed': False, 'QuantityAvailable': 0}, 'AutoForwardSupplierID': ''}
```

```
[{'Name': 'DefaultPriceScheduleID', 'Type': 'string', 'Description': 'ID of the default price schedule.', 'Required': False}, {'Name': 'ID', 'Type': 'string', 'Description': 'ID of the product. Can only contain characters Aa-Zz, 0-9, -, and _. Searchable: priority level 1. Sortable: priority level 2.', 'Required': False}, {'Name': 'Name', 'Type': 'string', 'Description': 'Name of the product. Required. Max length 100 characters. Searchable: priority level 2. Sortable: priority level 1.', 'Required': True}, {'Name': 'Description', 'Type': 'string', 'Description': 'Description of the product. Max length 2000 characters. Searchable: priority level 3.', 'Required': False}, {'Name': 'QuantityMultiplier', 'Type': 'integer', 'Description': 'Quantity multiplier of the product. Required. Must be at least 1.', 'Required': True}, {'Name': 'ShipWeight', 'Type': 'float', 'Description': 'Ship weight of the product.', 'Required': False}, {'Name': 'ShipHeight', 'Type': 'float', 'Description': 'Ship height of the product.', 'Required': False}, {'Name': 'ShipWidth', 'Type': 'float', 'Description': 'Ship width of the product.', 'Required': False}, {'Name': 'ShipLength', 'Type': 'float', 'Description': 'Ship length of the product.', 'Required': False}, {'Name': 'Active', 'Type': 'boolean', 'Description': 'Active of the product.', 'Required': False}, {'Name': 'xp', 'Type': 'object', 'Description': 'Container for extended (custom) properties of the product.', 'Required': False}, {'Name': 'ShipFromAddressID', 'Type': 'string', 'Description': 'ID of the ship from address.', 'Required': False}, {'Name': 'Inventory', 'Type': 'object', 'Description': 'Inventory of the product.', 'Required': False}, {'Name': 'AutoForwardSupplierID', 'Type': 'string', 'Description': 'ID of the auto forward supplier.', 'Required': False}]
```

**Responsestatus**: `200`

## Responsebody
```
{'DefaultPriceScheduleID': '', 'ID': '', 'Name': '', 'Description': '', 'QuantityMultiplier': 0, 'ShipWeight': 0, 'ShipHeight': 0, 'ShipWidth': 0, 'ShipLength': 0, 'Active': False, 'SpecCount': 0, 'xp': {}, 'VariantCount': 0, 'ShipFromAddressID': '', 'Inventory': {'Enabled': False, 'NotificationPoint': 0, 'VariantLevelTracking': False, 'OrderCanExceed': False, 'QuantityAvailable': 0, 'LastUpdated': '2018-03-21T23:00:00+00:00'}, 'AutoForwardSupplierID': ''}
```


| Parameters      | Description                    |
|------------------|---------------------------------|
| Name            | DefaultPriceScheduleID         |
| Type            | string                         |
| Description     | ID of the default price schedule. |
| Required        | False                          |


| Parameters      | Description                    |
|------------------|---------------------------------|
| Name            | ID                             |
| Type            | string                         |
| Description     | ID of the product.             |
| Required        | False                          |


| Parameters      | Description                    |
|------------------|---------------------------------|
| Name            | Name                           |
| Type            | string                         |
| Description     | Name of the product.           |
| Required        | True                           |


| Parameters      | Description                    |
|------------------|---------------------------------|
| Name            | Description                    |
| Type            | string                         |
| Description     | Description of the product.    |
| Required        | False                          |


| Parameters      | Description                    |
|------------------|---------------------------------|
| Name            | QuantityMultiplier             |
| Type            | integer                        |
| Description     | Quantity multiplier of the product. |
| Required        | True                           |


| Parameters      | Description                    |
|------------------|---------------------------------|
| Name            | ShipWeight                     |
| Type            | float                          |
| Description     | Ship weight of the product.    |
| Required        | False                          |


| Parameters      | Description                    |
|------------------|---------------------------------|
| Name            | ShipHeight                     |
| Type            | float                          |
| Description     | Ship height of the product.    |
| Required        | False                          |


| Parameters      | Description                    |
|------------------|---------------------------------|
| Name            | ShipWidth                      |
| Type            | float                          |
| Description     | Ship width of the product.     |
| Required        | False                          |


| Parameters      | Description                    |
|------------------|---------------------------------|
| Name            | ShipLength                     |
| Type            | float                          |
| Description     | Ship length of the product.    |
| Required        | False                          |


| Parameters      | Description                    |
|------------------|---------------------------------|
| Name            | Active                         |
| Type            | boolean                        |
| Description     | Active of the product.         |
| Required        | False                          |


| Parameters      | Description                    |
|------------------|---------------------------------|
| Name            | SpecCount                      |
| Type            | integer                        |
| Description     | Spec count of the product.     |
| Required        | False                          |


| Parameters      | Description                    |
|------------------|---------------------------------|
| Name            | xp                             |
| Type            | object                         |
| Description     | Container for extended (custom) properties of the product. |
| Required        | False                          |


| Parameters      | Description                    |
|------------------|---------------------------------|
| Name            | VariantCount                   |
| Type            | integer                        |
| Description     | Variant count of the product.  |
| Required        | False                          |


| Parameters      | Description                    |
|------------------|---------------------------------|
| Name            | ShipFromAddressID              |
| Type            | string                         |
| Description     | ID of the ship from address.   |
| Required        | False                          |


| Parameters      | Description                    |
|------------------|---------------------------------|
| Name            | Inventory                      |
| Type            | object                         |
| Description     | Inventory of the product.      |
| Required        | False                          |


| Parameters      | Description                    |
|------------------|---------------------------------|
| Name            | AutoForwardSupplierID          |
| Type            | string                         |
| Description     | ID of the auto forward supplier. |
| Required        | False                          |

## `POST` `v1/products/{productID}/variants/generate`
Generate a variants

| Parameters      | Description                    |
|------------------|---------------------------------|


| Parameters      | Description                    |
|------------------|---------------------------------|
| Name            | productID                      |
| Type            | string                         |
| Description     | ID of the product.             |
| Required        | True                           |


| Parameters      | Description                    |
|------------------|---------------------------------|
| Name            | overwriteExisting              |
| Type            | boolean                        |
| Description     | Overwrite existing of the product. |
| Required        | False                          |

## Requestbody
**Responsestatus**: `201`

## Responsebody
```
{'DefaultPriceScheduleID': '', 'ID': '', 'Name': '', 'Description': '', 'QuantityMultiplier': 0, 'ShipWeight': 0, 'ShipHeight': 0, 'ShipWidth': 0, 'ShipLength': 0, 'Active': False, 'SpecCount': 0, 'xp': {}, 'VariantCount': 0, 'ShipFromAddressID': '', 'Inventory': {'Enabled': False, 'NotificationPoint': 0, 'VariantLevelTracking': False, 'OrderCanExceed': False, 'QuantityAvailable': 0, 'LastUpdated': '2018-03-21T23:00:00+00:00'}, 'AutoForwardSupplierID': ''}
```


| Parameters      | Description                    |
|------------------|---------------------------------|
| Name            | DefaultPriceScheduleID         |
| Type            | string                         |
| Description     | ID of the default price schedule. |
| Required        | False                          |


| Parameters      | Description                    |
|------------------|---------------------------------|
| Name            | ID                             |
| Type            | string                         |
| Description     | ID of the product.             |
| Required        | False                          |


| Parameters      | Description                    |
|------------------|---------------------------------|
| Name            | Name                           |
| Type            | string                         |
| Description     | Name of the product.           |
| Required        | True                           |


| Parameters      | Description                    |
|------------------|---------------------------------|
| Name            | Description                    |
| Type            | string                         |
| Description     | Description of the product.    |
| Required        | False                          |


| Parameters      | Description                    |
|------------------|---------------------------------|
| Name            | QuantityMultiplier             |
| Type            | integer                        |
| Description     | Quantity multiplier of the product. |
| Required        | True                           |


| Parameters      | Description                    |
|------------------|---------------------------------|
| Name            | ShipWeight                     |
| Type            | float                          |
| Description     | Ship weight of the product.    |
| Required        | False                          |


| Parameters      | Description                    |
|------------------|---------------------------------|
| Name            | ShipHeight                     |
| Type            | float                          |
| Description     | Ship height of the product.    |
| Required        | False                          |


| Parameters      | Description                    |
|------------------|---------------------------------|
| Name            | ShipWidth                      |
| Type            | float                          |
| Description     | Ship width of the product.     |
| Required        | False                          |


| Parameters      | Description                    |
|------------------|---------------------------------|
| Name            | ShipLength                     |
| Type            | float                          |
| Description     | Ship length of the product.    |
| Required        | False                          |


| Parameters      | Description                    |
|------------------|---------------------------------|
| Name            | Active                         |
| Type            | boolean                        |
| Description     | Active of the product.         |
| Required        | False                          |


| Parameters      | Description                    |
|------------------|---------------------------------|
| Name            | SpecCount                      |
| Type            | integer                        |
| Description     | Spec count of the product.     |
| Required        | False                          |


| Parameters      | Description                    |
|------------------|---------------------------------|
| Name            | xp                             |
| Type            | object                         |
| Description     | Container for extended (custom) properties of the product. |
| Required        | False                          |


| Parameters      | Description                    |
|------------------|---------------------------------|
| Name            | VariantCount                   |
| Type            | integer                        |
| Description     | Variant count of the product.  |
| Required        | False                          |


| Parameters      | Description                    |
|------------------|---------------------------------|
| Name            | ShipFromAddressID              |
| Type            | string                         |
| Description     | ID of the ship from address.   |
| Required        | False                          |


| Parameters      | Description                    |
|------------------|---------------------------------|
| Name            | Inventory                      |
| Type            | object                         |
| Description     | Inventory of the product.      |
| Required        | False                          |


| Parameters      | Description                    |
|------------------|---------------------------------|
| Name            | AutoForwardSupplierID          |
| Type            | string                         |
| Description     | ID of the auto forward supplier. |
| Required        | False                          |

## `GET` `v1/products/{productID}/variants`
Get a list of product variants

| Parameters      | Description                    |
|------------------|---------------------------------|


| Parameters      | Description                    |
|------------------|---------------------------------|
| Name            | productID                      |
| Type            | string                         |
| Description     | ID of the product.             |
| Required        | True                           |


| Parameters      | Description                    |
|------------------|---------------------------------|
| Name            | search                         |
| Type            | string                         |
| Description     | Word or phrase to search for.  |
| Required        | False                          |


| Parameters      | Description                    |
|------------------|---------------------------------|
| Name            | searchOn                       |
| Type            | string                         |
| Description     | Comma-delimited list of fields to search on. |
| Required        | False                          |


| Parameters      | Description                    |
|------------------|---------------------------------|
| Name            | sortBy                         |
| Type            | string                         |
| Description     | Comma-delimited list of fields to sort by. |
| Required        | False                          |


| Parameters      | Description                    |
|------------------|---------------------------------|
| Name            | page                           |
| Type            | integer                        |
| Description     | Page of results to return. Default: 1 |
| Required        | False                          |


| Parameters      | Description                    |
|------------------|---------------------------------|
| Name            | pageSize                       |
| Type            | integer                        |
| Description     | Number of results to return per page. Default: 20, max: 100. |
| Required        | False                          |


| Parameters      | Description                    |
|------------------|---------------------------------|
| Name            | filters                        |
| Type            | object                         |
| Description     | Any additional key/value pairs passed in the query string are interpretted as filters. Valid keys are top-level properties of the returned model or 'xp.???' |
| Required        | False                          |

## Requestbody
**Responsestatus**: `200`

## Responsebody
```
{'Meta': {'Page': 1, 'PageSize': 20, 'TotalCount': 25, 'TotalPages': 2, 'ItemRange': [1, 20]}, 'Items': [{'ID': '', 'Name': '', 'Description': '', 'Active': False, 'xp': {}}]}
```


| Parameters      | Description                    |
|------------------|---------------------------------|
| Name            | ID                             |
| Type            | string                         |
| Description     | ID of the variant.             |
| Required        | False                          |


| Parameters      | Description                    |
|------------------|---------------------------------|
| Name            | Name                           |
| Type            | string                         |
| Description     | Name of the variant.           |
| Required        | False                          |


| Parameters      | Description                    |
|------------------|---------------------------------|
| Name            | Description                    |
| Type            | string                         |
| Description     | Description of the variant.    |
| Required        | False                          |


| Parameters      | Description                    |
|------------------|---------------------------------|
| Name            | Active                         |
| Type            | boolean                        |
| Description     | Active of the variant.         |
| Required        | False                          |


| Parameters      | Description                    |
|------------------|---------------------------------|
| Name            | xp                             |
| Type            | object                         |
| Description     | Container for extended (custom) properties of the variant. |
| Required        | False                          |

## `PUT` `v1/products/{productID}/variants/{variantID}`
Create or update a product variant

| Parameters      | Description                    |
|------------------|---------------------------------|


| Parameters      | Description                    |
|------------------|---------------------------------|
| Name            | productID                      |
| Type            | string                         |
| Description     | ID of the product.             |
| Required        | True                           |


| Parameters      | Description                    |
|------------------|---------------------------------|
| Name            | variantID                      |
| Type            | string                         |
| Description     | ID of the variant.             |
| Required        | True                           |

## Requestbody
```
{'ID': '', 'Name': '', 'Description': '', 'Active': False, 'xp': {}}
```

```
[{'Name': 'ID', 'Type': 'string', 'Description': 'ID of the variant. Can only contain characters Aa-Zz, 0-9, -, and _. Searchable: priority level 1. Sortable: priority level 1.', 'Required': False}, {'Name': 'Name', 'Type': 'string', 'Description': 'Name of the variant. Searchable: priority level 2. Sortable: priority level 2.', 'Required': False}, {'Name': 'Description', 'Type': 'string', 'Description': 'Description of the variant. Max length 2000 characters. Searchable: priority level 3.', 'Required': False}, {'Name': 'Active', 'Type': 'boolean', 'Description': 'Active of the variant.', 'Required': False}, {'Name': 'xp', 'Type': 'object', 'Description': 'Container for extended (custom) properties of the variant.', 'Required': False}]
```

**Responsestatus**: `200`

## Responsebody
```
{'ID': '', 'Name': '', 'Description': '', 'Active': False, 'xp': {}}
```


| Parameters      | Description                    |
|------------------|---------------------------------|
| Name            | ID                             |
| Type            | string                         |
| Description     | ID of the variant.             |
| Required        | False                          |


| Parameters      | Description                    |
|------------------|---------------------------------|
| Name            | Name                           |
| Type            | string                         |
| Description     | Name of the variant.           |
| Required        | False                          |


| Parameters      | Description                    |
|------------------|---------------------------------|
| Name            | Description                    |
| Type            | string                         |
| Description     | Description of the variant.    |
| Required        | False                          |


| Parameters      | Description                    |
|------------------|---------------------------------|
| Name            | Active                         |
| Type            | boolean                        |
| Description     | Active of the variant.         |
| Required        | False                          |


| Parameters      | Description                    |
|------------------|---------------------------------|
| Name            | xp                             |
| Type            | object                         |
| Description     | Container for extended (custom) properties of the variant. |
| Required        | False                          |

## `PATCH` `v1/products/{productID}/variants/{variantID}`
Partially update a product variant

| Parameters      | Description                    |
|------------------|---------------------------------|


| Parameters      | Description                    |
|------------------|---------------------------------|
| Name            | productID                      |
| Type            | string                         |
| Description     | ID of the product.             |
| Required        | True                           |


| Parameters      | Description                    |
|------------------|---------------------------------|
| Name            | variantID                      |
| Type            | string                         |
| Description     | ID of the variant.             |
| Required        | True                           |

## Requestbody
```
{'ID': '', 'Name': '', 'Description': '', 'Active': False, 'xp': {}}
```

```
[{'Name': 'ID', 'Type': 'string', 'Description': 'ID of the variant. Can only contain characters Aa-Zz, 0-9, -, and _. Searchable: priority level 1. Sortable: priority level 1.', 'Required': False}, {'Name': 'Name', 'Type': 'string', 'Description': 'Name of the variant. Searchable: priority level 2. Sortable: priority level 2.', 'Required': False}, {'Name': 'Description', 'Type': 'string', 'Description': 'Description of the variant. Max length 2000 characters. Searchable: priority level 3.', 'Required': False}, {'Name': 'Active', 'Type': 'boolean', 'Description': 'Active of the variant.', 'Required': False}, {'Name': 'xp', 'Type': 'object', 'Description': 'Container for extended (custom) properties of the variant.', 'Required': False}]
```

**Responsestatus**: `200`

## Responsebody
```
{'ID': '', 'Name': '', 'Description': '', 'Active': False, 'xp': {}}
```


| Parameters      | Description                    |
|------------------|---------------------------------|
| Name            | ID                             |
| Type            | string                         |
| Description     | ID of the variant.             |
| Required        | False                          |


| Parameters      | Description                    |
|------------------|---------------------------------|
| Name            | Name                           |
| Type            | string                         |
| Description     | Name of the variant.           |
| Required        | False                          |


| Parameters      | Description                    |
|------------------|---------------------------------|
| Name            | Description                    |
| Type            | string                         |
| Description     | Description of the variant.    |
| Required        | False                          |


| Parameters      | Description                    |
|------------------|---------------------------------|
| Name            | Active                         |
| Type            | boolean                        |
| Description     | Active of the variant.         |
| Required        | False                          |


| Parameters      | Description                    |
|------------------|---------------------------------|
| Name            | xp                             |
| Type            | object                         |
| Description     | Container for extended (custom) properties of the variant. |
| Required        | False                          |

## `GET` `v1/products/{productID}/variants/{variantID}`
Get a single product variant

| Parameters      | Description                    |
|------------------|---------------------------------|


| Parameters      | Description                    |
|------------------|---------------------------------|
| Name            | productID                      |
| Type            | string                         |
| Description     | ID of the product.             |
| Required        | True                           |


| Parameters      | Description                    |
|------------------|---------------------------------|
| Name            | variantID                      |
| Type            | string                         |
| Description     | ID of the variant.             |
| Required        | True                           |

## Requestbody
**Responsestatus**: `200`

## Responsebody
```
{'ID': '', 'Name': '', 'Description': '', 'Active': False, 'xp': {}}
```


| Parameters      | Description                    |
|------------------|---------------------------------|
| Name            | ID                             |
| Type            | string                         |
| Description     | ID of the variant.             |
| Required        | False                          |


| Parameters      | Description                    |
|------------------|---------------------------------|
| Name            | Name                           |
| Type            | string                         |
| Description     | Name of the variant.           |
| Required        | False                          |


| Parameters      | Description                    |
|------------------|---------------------------------|
| Name            | Description                    |
| Type            | string                         |
| Description     | Description of the variant.    |
| Required        | False                          |


| Parameters      | Description                    |
|------------------|---------------------------------|
| Name            | Active                         |
| Type            | boolean                        |
| Description     | Active of the variant.         |
| Required        | False                          |


| Parameters      | Description                    |
|------------------|---------------------------------|
| Name            | xp                             |
| Type            | object                         |
| Description     | Container for extended (custom) properties of the variant. |
| Required        | False                          |

## `GET` `v1/products/{productID}/suppliers`
Get a list of product suppliers

| Parameters      | Description                    |
|------------------|---------------------------------|


| Parameters      | Description                    |
|------------------|---------------------------------|
| Name            | productID                      |
| Type            | string                         |
| Description     | ID of the product.             |
| Required        | True                           |


| Parameters      | Description                    |
|------------------|---------------------------------|
| Name            | search                         |
| Type            | string                         |
| Description     | Word or phrase to search for.  |
| Required        | False                          |


| Parameters      | Description                    |
|------------------|---------------------------------|
| Name            | searchOn                       |
| Type            | string                         |
| Description     | Comma-delimited list of fields to search on. |
| Required        | False                          |


| Parameters      | Description                    |
|------------------|---------------------------------|
| Name            | sortBy                         |
| Type            | string                         |
| Description     | Comma-delimited list of fields to sort by. |
| Required        | False                          |


| Parameters      | Description                    |
|------------------|---------------------------------|
| Name            | page                           |
| Type            | integer                        |
| Description     | Page of results to return. Default: 1 |
| Required        | False                          |


| Parameters      | Description                    |
|------------------|---------------------------------|
| Name            | pageSize                       |
| Type            | integer                        |
| Description     | Number of results to return per page. Default: 20, max: 100. |
| Required        | False                          |


| Parameters      | Description                    |
|------------------|---------------------------------|
| Name            | filters                        |
| Type            | object                         |
| Description     | Any additional key/value pairs passed in the query string are interpretted as filters. Valid keys are top-level properties of the returned model or 'xp.???' |
| Required        | False                          |

## Requestbody
**Responsestatus**: `200`

## Responsebody
```
{'Meta': {'Page': 1, 'PageSize': 20, 'TotalCount': 25, 'TotalPages': 2, 'ItemRange': [1, 20]}, 'Items': [{'ID': '', 'Name': '', 'Active': False, 'xp': {}}]}
```


| Parameters      | Description                    |
|------------------|---------------------------------|
| Name            | ID                             |
| Type            | string                         |
| Description     | ID of the supplier.            |
| Required        | False                          |


| Parameters      | Description                    |
|------------------|---------------------------------|
| Name            | Name                           |
| Type            | string                         |
| Description     | Name of the supplier.          |
| Required        | True                           |


| Parameters      | Description                    |
|------------------|---------------------------------|
| Name            | Active                         |
| Type            | boolean                        |
| Description     | Active of the supplier.        |
| Required        | False                          |


| Parameters      | Description                    |
|------------------|---------------------------------|
| Name            | xp                             |
| Type            | object                         |
| Description     | Container for extended (custom) properties of the supplier. |
| Required        | False                          |

## `PUT` `v1/products/{productID}/suppliers/{supplierID}`
Save a product supplier

| Parameters      | Description                    |
|------------------|---------------------------------|


| Parameters      | Description                    |
|------------------|---------------------------------|
| Name            | productID                      |
| Type            | string                         |
| Description     | ID of the product.             |
| Required        | True                           |


| Parameters      | Description                    |
|------------------|---------------------------------|
| Name            | supplierID                     |
| Type            | string                         |
| Description     | ID of the supplier.            |
| Required        | True                           |

## Requestbody
**Responsestatus**: `204`

## Responsebody
## `DELETE` `v1/products/{productID}/suppliers/{supplierID}`
Remove a supplier

| Parameters      | Description                    |
|------------------|---------------------------------|


| Parameters      | Description                    |
|------------------|---------------------------------|
| Name            | productID                      |
| Type            | string                         |
| Description     | ID of the product.             |
| Required        | True                           |


| Parameters      | Description                    |
|------------------|---------------------------------|
| Name            | supplierID                     |
| Type            | string                         |
| Description     | ID of the supplier.            |
| Required        | True                           |

## Requestbody
**Responsestatus**: `204`

## Responsebody
## `POST` `v1/products/assignments`
Save a product assignment
## Requestbody
```
{'ProductID': '', 'BuyerID': '', 'UserGroupID': '', 'PriceScheduleID': ''}
```

```
[{'Name': 'ProductID', 'Type': 'string', 'Description': 'ID of the product. Required.', 'Required': True}, {'Name': 'BuyerID', 'Type': 'string', 'Description': 'ID of the buyer. Required.', 'Required': True}, {'Name': 'UserGroupID', 'Type': 'string', 'Description': 'ID of the user group.', 'Required': False}, {'Name': 'PriceScheduleID', 'Type': 'string', 'Description': 'ID of the price schedule.', 'Required': False}]
```

**Responsestatus**: `204`

## Responsebody
## `GET` `v1/products/assignments`
Get a list of product assignments

| Parameters      | Description                    |
|------------------|---------------------------------|


| Parameters      | Description                    |
|------------------|---------------------------------|
| Name            | productID                      |
| Type            | string                         |
| Description     | ID of the product.             |
| Required        | False                          |


| Parameters      | Description                    |
|------------------|---------------------------------|
| Name            | priceScheduleID                |
| Type            | string                         |
| Description     | ID of the price schedule.      |
| Required        | False                          |


| Parameters      | Description                    |
|------------------|---------------------------------|
| Name            | buyerID                        |
| Type            | string                         |
| Description     | ID of the buyer.               |
| Required        | False                          |


| Parameters      | Description                    |
|------------------|---------------------------------|
| Name            | userID                         |
| Type            | string                         |
| Description     | ID of the user.                |
| Required        | False                          |


| Parameters      | Description                    |
|------------------|---------------------------------|
| Name            | userGroupID                    |
| Type            | string                         |
| Description     | ID of the user group.          |
| Required        | False                          |


| Parameters      | Description                    |
|------------------|---------------------------------|
| Name            | level                          |
| Type            | string                         |
| Description     | Level of the product assignment. Possible values: User, Group, Company. |
| Required        | False                          |


| Parameters      | Description                    |
|------------------|---------------------------------|
| Name            | page                           |
| Type            | integer                        |
| Description     | Page of results to return. Default: 1 |
| Required        | False                          |


| Parameters      | Description                    |
|------------------|---------------------------------|
| Name            | pageSize                       |
| Type            | integer                        |
| Description     | Number of results to return per page. Default: 20, max: 100. |
| Required        | False                          |

## Requestbody
**Responsestatus**: `200`

## Responsebody
```
{'Meta': {'Page': 1, 'PageSize': 20, 'TotalCount': 25, 'TotalPages': 2, 'ItemRange': [1, 20]}, 'Items': [{'ProductID': '', 'BuyerID': '', 'UserGroupID': '', 'PriceScheduleID': ''}]}
```


| Parameters      | Description                    |
|------------------|---------------------------------|
| Name            | ProductID                      |
| Type            | string                         |
| Description     | ID of the product.             |
| Required        | True                           |


| Parameters      | Description                    |
|------------------|---------------------------------|
| Name            | BuyerID                        |
| Type            | string                         |
| Description     | ID of the buyer.               |
| Required        | True                           |


| Parameters      | Description                    |
|------------------|---------------------------------|
| Name            | UserGroupID                    |
| Type            | string                         |
| Description     | ID of the user group.          |
| Required        | False                          |


| Parameters      | Description                    |
|------------------|---------------------------------|
| Name            | PriceScheduleID                |
| Type            | string                         |
| Description     | ID of the price schedule.      |
| Required        | False                          |

## `DELETE` `v1/products/{productID}/assignments/{buyerID}`
Delete a product assignment

| Parameters      | Description                    |
|------------------|---------------------------------|


| Parameters      | Description                    |
|------------------|---------------------------------|
| Name            | productID                      |
| Type            | string                         |
| Description     | ID of the product.             |
| Required        | True                           |


| Parameters      | Description                    |
|------------------|---------------------------------|
| Name            | buyerID                        |
| Type            | string                         |
| Description     | ID of the buyer.               |
| Required        | True                           |


| Parameters      | Description                    |
|------------------|---------------------------------|
| Name            | userID                         |
| Type            | string                         |
| Description     | ID of the user.                |
| Required        | False                          |


| Parameters      | Description                    |
|------------------|---------------------------------|
| Name            | userGroupID                    |
| Type            | string                         |
| Description     | ID of the user group.          |
| Required        | False                          |

## Requestbody
**Responsestatus**: `204`

## Responsebody