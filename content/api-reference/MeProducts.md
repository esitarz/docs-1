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

## `GET` `v1/me/products`
Get a list of products visible to this user

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
| Name            | depth                          |
| Type            | string                         |
| Description     | Depth of the product.          |
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
{'Meta': {'Page': 1, 'PageSize': 20, 'TotalCount': 25, 'TotalPages': 2, 'ItemRange': [1, 20]}, 'Items': [{'ID': '', 'PriceSchedule': {'ID': '', 'Name': '', 'ApplyTax': False, 'ApplyShipping': False, 'MinQuantity': 0, 'MaxQuantity': 0, 'UseCumulativeQuantity': False, 'RestrictedQuantity': False, 'PriceBreaks': [{'Quantity': 0, 'Price': 0}], 'xp': {}}, 'Name': '', 'Description': '', 'QuantityMultiplier': 0, 'ShipWeight': 0, 'ShipHeight': 0, 'ShipWidth': 0, 'ShipLength': 0, 'Active': False, 'SpecCount': 0, 'xp': {}, 'VariantCount': 0, 'ShipFromAddressID': '', 'Inventory': {'Enabled': False, 'NotificationPoint': 0, 'VariantLevelTracking': False, 'OrderCanExceed': False, 'QuantityAvailable': 0, 'LastUpdated': '2018-03-21T23:00:00+00:00'}, 'AutoForwardSupplierID': ''}]}
```


| Parameters      | Description                    |
|------------------|---------------------------------|
| Name            | ID                             |
| Type            | string                         |
| Description     | ID of the product.             |
| Required        | False                          |


| Parameters      | Description                    |
|------------------|---------------------------------|
| Name            | PriceSchedule                  |
| Type            | object                         |
| Description     | Price schedule of the product. |
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

## `GET` `v1/me/products/{productID}`
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
{'ID': '', 'PriceSchedule': {'ID': '', 'Name': '', 'ApplyTax': False, 'ApplyShipping': False, 'MinQuantity': 0, 'MaxQuantity': 0, 'UseCumulativeQuantity': False, 'RestrictedQuantity': False, 'PriceBreaks': [{'Quantity': 0, 'Price': 0}], 'xp': {}}, 'Name': '', 'Description': '', 'QuantityMultiplier': 0, 'ShipWeight': 0, 'ShipHeight': 0, 'ShipWidth': 0, 'ShipLength': 0, 'Active': False, 'SpecCount': 0, 'xp': {}, 'VariantCount': 0, 'ShipFromAddressID': '', 'Inventory': {'Enabled': False, 'NotificationPoint': 0, 'VariantLevelTracking': False, 'OrderCanExceed': False, 'QuantityAvailable': 0, 'LastUpdated': '2018-03-21T23:00:00+00:00'}, 'AutoForwardSupplierID': ''}
```


| Parameters      | Description                    |
|------------------|---------------------------------|
| Name            | ID                             |
| Type            | string                         |
| Description     | ID of the product.             |
| Required        | False                          |


| Parameters      | Description                    |
|------------------|---------------------------------|
| Name            | PriceSchedule                  |
| Type            | object                         |
| Description     | Price schedule of the product. |
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

## `GET` `v1/me/products/{productID}/specs`
Get a list of specs visible to this user

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
| Name            | catalogID                      |
| Type            | string                         |
| Description     | ID of the catalog.             |
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
{'Meta': {'Page': 1, 'PageSize': 20, 'TotalCount': 25, 'TotalPages': 2, 'ItemRange': [1, 20]}, 'Items': [{'Options': [{'ID': '', 'Value': '', 'ListOrder': 1, 'IsOpenText': False, 'PriceMarkupType': 'NoMarkup', 'PriceMarkup': 0, 'xp': {}}], 'ID': '', 'ListOrder': 1, 'Name': '', 'DefaultValue': '', 'Required': False, 'AllowOpenText': False, 'DefaultOptionID': '', 'DefinesVariant': False, 'xp': {}}]}
```


| Parameters      | Description                    |
|------------------|---------------------------------|
| Name            | Options                        |
| Type            | array                          |
| Description     | Options of the spec.           |
| Required        | False                          |


| Parameters      | Description                    |
|------------------|---------------------------------|
| Name            | ID                             |
| Type            | string                         |
| Description     | ID of the spec.                |
| Required        | False                          |


| Parameters      | Description                    |
|------------------|---------------------------------|
| Name            | ListOrder                      |
| Type            | integer                        |
| Description     | List order of the spec.        |
| Required        | False                          |


| Parameters      | Description                    |
|------------------|---------------------------------|
| Name            | Name                           |
| Type            | string                         |
| Description     | Name of the spec.              |
| Required        | True                           |


| Parameters      | Description                    |
|------------------|---------------------------------|
| Name            | DefaultValue                   |
| Type            | string                         |
| Description     | Default value of the spec.     |
| Required        | False                          |


| Parameters      | Description                    |
|------------------|---------------------------------|
| Name            | Required                       |
| Type            | boolean                        |
| Description     | Required of the spec.          |
| Required        | False                          |


| Parameters      | Description                    |
|------------------|---------------------------------|
| Name            | AllowOpenText                  |
| Type            | boolean                        |
| Description     | Allow open text of the spec.   |
| Required        | False                          |


| Parameters      | Description                    |
|------------------|---------------------------------|
| Name            | DefaultOptionID                |
| Type            | string                         |
| Description     | ID of the default option.      |
| Required        | False                          |


| Parameters      | Description                    |
|------------------|---------------------------------|
| Name            | DefinesVariant                 |
| Type            | boolean                        |
| Description     | True if each unique combinations of this Spec's Options map to unique Product Variants/SKUs. |
| Required        | False                          |


| Parameters      | Description                    |
|------------------|---------------------------------|
| Name            | xp                             |
| Type            | object                         |
| Description     | Container for extended (custom) properties of the spec. |
| Required        | False                          |

## `GET` `v1/me/products/{productID}/specs/{specID}`
Get a single spec

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
| Name            | specID                         |
| Type            | string                         |
| Description     | ID of the spec.                |
| Required        | True                           |


| Parameters      | Description                    |
|------------------|---------------------------------|
| Name            | catalogID                      |
| Type            | string                         |
| Description     | ID of the catalog.             |
| Required        | False                          |

## Requestbody
**Responsestatus**: `200`

## Responsebody
```
{'Options': [{'ID': '', 'Value': '', 'ListOrder': 1, 'IsOpenText': False, 'PriceMarkupType': 'NoMarkup', 'PriceMarkup': 0, 'xp': {}}], 'ID': '', 'ListOrder': 1, 'Name': '', 'DefaultValue': '', 'Required': False, 'AllowOpenText': False, 'DefaultOptionID': '', 'DefinesVariant': False, 'xp': {}}
```


| Parameters      | Description                    |
|------------------|---------------------------------|
| Name            | Options                        |
| Type            | array                          |
| Description     | Options of the spec.           |
| Required        | False                          |


| Parameters      | Description                    |
|------------------|---------------------------------|
| Name            | ID                             |
| Type            | string                         |
| Description     | ID of the spec.                |
| Required        | False                          |


| Parameters      | Description                    |
|------------------|---------------------------------|
| Name            | ListOrder                      |
| Type            | integer                        |
| Description     | List order of the spec.        |
| Required        | False                          |


| Parameters      | Description                    |
|------------------|---------------------------------|
| Name            | Name                           |
| Type            | string                         |
| Description     | Name of the spec.              |
| Required        | True                           |


| Parameters      | Description                    |
|------------------|---------------------------------|
| Name            | DefaultValue                   |
| Type            | string                         |
| Description     | Default value of the spec.     |
| Required        | False                          |


| Parameters      | Description                    |
|------------------|---------------------------------|
| Name            | Required                       |
| Type            | boolean                        |
| Description     | Required of the spec.          |
| Required        | False                          |


| Parameters      | Description                    |
|------------------|---------------------------------|
| Name            | AllowOpenText                  |
| Type            | boolean                        |
| Description     | Allow open text of the spec.   |
| Required        | False                          |


| Parameters      | Description                    |
|------------------|---------------------------------|
| Name            | DefaultOptionID                |
| Type            | string                         |
| Description     | ID of the default option.      |
| Required        | False                          |


| Parameters      | Description                    |
|------------------|---------------------------------|
| Name            | DefinesVariant                 |
| Type            | boolean                        |
| Description     | True if each unique combinations of this Spec's Options map to unique Product Variants/SKUs. |
| Required        | False                          |


| Parameters      | Description                    |
|------------------|---------------------------------|
| Name            | xp                             |
| Type            | object                         |
| Description     | Container for extended (custom) properties of the spec. |
| Required        | False                          |
