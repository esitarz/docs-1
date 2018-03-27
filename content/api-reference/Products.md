---
title: Products
date: 2018-03-27
category: API Reference
tags: Product Catalogs
slug: Product-Catalogs-Products
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

## Request Body
**Response Status**: `200`

## Response Body
	{
	    "Active": false,
	    "AutoForwardSupplierID": "",
	    "DefaultPriceScheduleID": "",
	    "Description": "",
	    "ID": "",
	    "Inventory": {
	        "Enabled": false,
	        "LastUpdated": "2018-03-27T16:00:00+00:00",
	        "NotificationPoint": 0,
	        "OrderCanExceed": false,
	        "QuantityAvailable": 0,
	        "VariantLevelTracking": false
	    },
	    "Name": "",
	    "QuantityMultiplier": 0,
	    "ShipFromAddressID": "",
	    "ShipHeight": 0,
	    "ShipLength": 0,
	    "ShipWeight": 0,
	    "ShipWidth": 0,
	    "SpecCount": 0,
	    "VariantCount": 0,
	    "xp": {}
	}
| Name | Type | Description | Required | 
|---|---|---|---|
| DefaultPriceScheduleID | string | ID of the default price schedule. | False |
| ID | string | ID of the product. | False |
| Name | string | Name of the product. | True |
| Description | string | Description of the product. | False |
| QuantityMultiplier | integer | Quantity multiplier of the product. | True |
| ShipWeight | float | Ship weight of the product. | False |
| ShipHeight | float | Ship height of the product. | False |
| ShipWidth | float | Ship width of the product. | False |
| ShipLength | float | Ship length of the product. | False |
| Active | boolean | Active of the product. | False |
| SpecCount | integer | Spec count of the product. | False |
| xp | object | Container for extended (custom) properties of the product. | False |
| VariantCount | integer | Variant count of the product. | False |
| ShipFromAddressID | string | ID of the ship from address. | False |
| Inventory | object | Inventory of the product. | False |
| AutoForwardSupplierID | string | ID of the auto forward supplier. | False |

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

## Request Body
**Response Status**: `200`

## Response Body
	{
	    "Items": [
	        {
	            "Active": false,
	            "AutoForwardSupplierID": "",
	            "DefaultPriceScheduleID": "",
	            "Description": "",
	            "ID": "",
	            "Inventory": {
	                "Enabled": false,
	                "LastUpdated": "2018-03-27T16:00:00+00:00",
	                "NotificationPoint": 0,
	                "OrderCanExceed": false,
	                "QuantityAvailable": 0,
	                "VariantLevelTracking": false
	            },
	            "Name": "",
	            "QuantityMultiplier": 0,
	            "ShipFromAddressID": "",
	            "ShipHeight": 0,
	            "ShipLength": 0,
	            "ShipWeight": 0,
	            "ShipWidth": 0,
	            "SpecCount": 0,
	            "VariantCount": 0,
	            "xp": {}
	        }
	    ],
	    "Meta": {
	        "ItemRange": [
	            1,
	            20
	        ],
	        "Page": 1,
	        "PageSize": 20,
	        "TotalCount": 25,
	        "TotalPages": 2
	    }
	}
| Name | Type | Description | Required | 
|---|---|---|---|
| DefaultPriceScheduleID | string | ID of the default price schedule. | False |
| ID | string | ID of the product. | False |
| Name | string | Name of the product. | True |
| Description | string | Description of the product. | False |
| QuantityMultiplier | integer | Quantity multiplier of the product. | True |
| ShipWeight | float | Ship weight of the product. | False |
| ShipHeight | float | Ship height of the product. | False |
| ShipWidth | float | Ship width of the product. | False |
| ShipLength | float | Ship length of the product. | False |
| Active | boolean | Active of the product. | False |
| SpecCount | integer | Spec count of the product. | False |
| xp | object | Container for extended (custom) properties of the product. | False |
| VariantCount | integer | Variant count of the product. | False |
| ShipFromAddressID | string | ID of the ship from address. | False |
| Inventory | object | Inventory of the product. | False |
| AutoForwardSupplierID | string | ID of the auto forward supplier. | False |

## `POST` `v1/products`
Create a new product
## Request Body
	{
	    "Active": false,
	    "AutoForwardSupplierID": "",
	    "DefaultPriceScheduleID": "",
	    "Description": "",
	    "ID": "",
	    "Inventory": {
	        "Enabled": false,
	        "NotificationPoint": 0,
	        "OrderCanExceed": false,
	        "QuantityAvailable": 0,
	        "VariantLevelTracking": false
	    },
	    "Name": "",
	    "QuantityMultiplier": 0,
	    "ShipFromAddressID": "",
	    "ShipHeight": 0,
	    "ShipLength": 0,
	    "ShipWeight": 0,
	    "ShipWidth": 0,
	    "xp": {}
	}
| Name | Type | Description | Required | 
|---|---|---|---|
| DefaultPriceScheduleID | string | ID of the default price schedule. | False |
| ID | string | ID of the product. Can only contain characters Aa-Zz, 0-9, -, and _. Searchable: priority level 1. Sortable: priority level 2. | False |
| Name | string | Name of the product. Required. Max length 100 characters. Searchable: priority level 2. Sortable: priority level 1. | True |
| Description | string | Description of the product. Max length 2000 characters. Searchable: priority level 3. | False |
| QuantityMultiplier | integer | Quantity multiplier of the product. Required. Must be at least 1. | True |
| ShipWeight | float | Ship weight of the product. | False |
| ShipHeight | float | Ship height of the product. | False |
| ShipWidth | float | Ship width of the product. | False |
| ShipLength | float | Ship length of the product. | False |
| Active | boolean | Active of the product. | False |
| xp | object | Container for extended (custom) properties of the product. | False |
| ShipFromAddressID | string | ID of the ship from address. | False |
| Inventory | object | Inventory of the product. | False |
| AutoForwardSupplierID | string | ID of the auto forward supplier. | False |

**Response Status**: `201`

## Response Body
	{
	    "Active": false,
	    "AutoForwardSupplierID": "",
	    "DefaultPriceScheduleID": "",
	    "Description": "",
	    "ID": "",
	    "Inventory": {
	        "Enabled": false,
	        "LastUpdated": "2018-03-27T16:00:00+00:00",
	        "NotificationPoint": 0,
	        "OrderCanExceed": false,
	        "QuantityAvailable": 0,
	        "VariantLevelTracking": false
	    },
	    "Name": "",
	    "QuantityMultiplier": 0,
	    "ShipFromAddressID": "",
	    "ShipHeight": 0,
	    "ShipLength": 0,
	    "ShipWeight": 0,
	    "ShipWidth": 0,
	    "SpecCount": 0,
	    "VariantCount": 0,
	    "xp": {}
	}
| Name | Type | Description | Required | 
|---|---|---|---|
| DefaultPriceScheduleID | string | ID of the default price schedule. | False |
| ID | string | ID of the product. | False |
| Name | string | Name of the product. | True |
| Description | string | Description of the product. | False |
| QuantityMultiplier | integer | Quantity multiplier of the product. | True |
| ShipWeight | float | Ship weight of the product. | False |
| ShipHeight | float | Ship height of the product. | False |
| ShipWidth | float | Ship width of the product. | False |
| ShipLength | float | Ship length of the product. | False |
| Active | boolean | Active of the product. | False |
| SpecCount | integer | Spec count of the product. | False |
| xp | object | Container for extended (custom) properties of the product. | False |
| VariantCount | integer | Variant count of the product. | False |
| ShipFromAddressID | string | ID of the ship from address. | False |
| Inventory | object | Inventory of the product. | False |
| AutoForwardSupplierID | string | ID of the auto forward supplier. | False |

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

## Request Body
	{
	    "Active": false,
	    "AutoForwardSupplierID": "",
	    "DefaultPriceScheduleID": "",
	    "Description": "",
	    "ID": "",
	    "Inventory": {
	        "Enabled": false,
	        "NotificationPoint": 0,
	        "OrderCanExceed": false,
	        "QuantityAvailable": 0,
	        "VariantLevelTracking": false
	    },
	    "Name": "",
	    "QuantityMultiplier": 0,
	    "ShipFromAddressID": "",
	    "ShipHeight": 0,
	    "ShipLength": 0,
	    "ShipWeight": 0,
	    "ShipWidth": 0,
	    "xp": {}
	}
| Name | Type | Description | Required | 
|---|---|---|---|
| DefaultPriceScheduleID | string | ID of the default price schedule. | False |
| ID | string | ID of the product. Can only contain characters Aa-Zz, 0-9, -, and _. Searchable: priority level 1. Sortable: priority level 2. | False |
| Name | string | Name of the product. Required. Max length 100 characters. Searchable: priority level 2. Sortable: priority level 1. | True |
| Description | string | Description of the product. Max length 2000 characters. Searchable: priority level 3. | False |
| QuantityMultiplier | integer | Quantity multiplier of the product. Required. Must be at least 1. | True |
| ShipWeight | float | Ship weight of the product. | False |
| ShipHeight | float | Ship height of the product. | False |
| ShipWidth | float | Ship width of the product. | False |
| ShipLength | float | Ship length of the product. | False |
| Active | boolean | Active of the product. | False |
| xp | object | Container for extended (custom) properties of the product. | False |
| ShipFromAddressID | string | ID of the ship from address. | False |
| Inventory | object | Inventory of the product. | False |
| AutoForwardSupplierID | string | ID of the auto forward supplier. | False |

**Response Status**: `200`

## Response Body
	{
	    "Active": false,
	    "AutoForwardSupplierID": "",
	    "DefaultPriceScheduleID": "",
	    "Description": "",
	    "ID": "",
	    "Inventory": {
	        "Enabled": false,
	        "LastUpdated": "2018-03-27T16:00:00+00:00",
	        "NotificationPoint": 0,
	        "OrderCanExceed": false,
	        "QuantityAvailable": 0,
	        "VariantLevelTracking": false
	    },
	    "Name": "",
	    "QuantityMultiplier": 0,
	    "ShipFromAddressID": "",
	    "ShipHeight": 0,
	    "ShipLength": 0,
	    "ShipWeight": 0,
	    "ShipWidth": 0,
	    "SpecCount": 0,
	    "VariantCount": 0,
	    "xp": {}
	}
| Name | Type | Description | Required | 
|---|---|---|---|
| DefaultPriceScheduleID | string | ID of the default price schedule. | False |
| ID | string | ID of the product. | False |
| Name | string | Name of the product. | True |
| Description | string | Description of the product. | False |
| QuantityMultiplier | integer | Quantity multiplier of the product. | True |
| ShipWeight | float | Ship weight of the product. | False |
| ShipHeight | float | Ship height of the product. | False |
| ShipWidth | float | Ship width of the product. | False |
| ShipLength | float | Ship length of the product. | False |
| Active | boolean | Active of the product. | False |
| SpecCount | integer | Spec count of the product. | False |
| xp | object | Container for extended (custom) properties of the product. | False |
| VariantCount | integer | Variant count of the product. | False |
| ShipFromAddressID | string | ID of the ship from address. | False |
| Inventory | object | Inventory of the product. | False |
| AutoForwardSupplierID | string | ID of the auto forward supplier. | False |

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

## Request Body
**Response Status**: `204`

## Response Body
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

## Request Body
	{
	    "Active": false,
	    "AutoForwardSupplierID": "",
	    "DefaultPriceScheduleID": "",
	    "Description": "",
	    "ID": "",
	    "Inventory": {
	        "Enabled": false,
	        "NotificationPoint": 0,
	        "OrderCanExceed": false,
	        "QuantityAvailable": 0,
	        "VariantLevelTracking": false
	    },
	    "Name": "",
	    "QuantityMultiplier": 0,
	    "ShipFromAddressID": "",
	    "ShipHeight": 0,
	    "ShipLength": 0,
	    "ShipWeight": 0,
	    "ShipWidth": 0,
	    "xp": {}
	}
| Name | Type | Description | Required | 
|---|---|---|---|
| DefaultPriceScheduleID | string | ID of the default price schedule. | False |
| ID | string | ID of the product. Can only contain characters Aa-Zz, 0-9, -, and _. Searchable: priority level 1. Sortable: priority level 2. | False |
| Name | string | Name of the product. Required. Max length 100 characters. Searchable: priority level 2. Sortable: priority level 1. | True |
| Description | string | Description of the product. Max length 2000 characters. Searchable: priority level 3. | False |
| QuantityMultiplier | integer | Quantity multiplier of the product. Required. Must be at least 1. | True |
| ShipWeight | float | Ship weight of the product. | False |
| ShipHeight | float | Ship height of the product. | False |
| ShipWidth | float | Ship width of the product. | False |
| ShipLength | float | Ship length of the product. | False |
| Active | boolean | Active of the product. | False |
| xp | object | Container for extended (custom) properties of the product. | False |
| ShipFromAddressID | string | ID of the ship from address. | False |
| Inventory | object | Inventory of the product. | False |
| AutoForwardSupplierID | string | ID of the auto forward supplier. | False |

**Response Status**: `200`

## Response Body
	{
	    "Active": false,
	    "AutoForwardSupplierID": "",
	    "DefaultPriceScheduleID": "",
	    "Description": "",
	    "ID": "",
	    "Inventory": {
	        "Enabled": false,
	        "LastUpdated": "2018-03-27T16:00:00+00:00",
	        "NotificationPoint": 0,
	        "OrderCanExceed": false,
	        "QuantityAvailable": 0,
	        "VariantLevelTracking": false
	    },
	    "Name": "",
	    "QuantityMultiplier": 0,
	    "ShipFromAddressID": "",
	    "ShipHeight": 0,
	    "ShipLength": 0,
	    "ShipWeight": 0,
	    "ShipWidth": 0,
	    "SpecCount": 0,
	    "VariantCount": 0,
	    "xp": {}
	}
| Name | Type | Description | Required | 
|---|---|---|---|
| DefaultPriceScheduleID | string | ID of the default price schedule. | False |
| ID | string | ID of the product. | False |
| Name | string | Name of the product. | True |
| Description | string | Description of the product. | False |
| QuantityMultiplier | integer | Quantity multiplier of the product. | True |
| ShipWeight | float | Ship weight of the product. | False |
| ShipHeight | float | Ship height of the product. | False |
| ShipWidth | float | Ship width of the product. | False |
| ShipLength | float | Ship length of the product. | False |
| Active | boolean | Active of the product. | False |
| SpecCount | integer | Spec count of the product. | False |
| xp | object | Container for extended (custom) properties of the product. | False |
| VariantCount | integer | Variant count of the product. | False |
| ShipFromAddressID | string | ID of the ship from address. | False |
| Inventory | object | Inventory of the product. | False |
| AutoForwardSupplierID | string | ID of the auto forward supplier. | False |

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

## Request Body
**Response Status**: `201`

## Response Body
	{
	    "Active": false,
	    "AutoForwardSupplierID": "",
	    "DefaultPriceScheduleID": "",
	    "Description": "",
	    "ID": "",
	    "Inventory": {
	        "Enabled": false,
	        "LastUpdated": "2018-03-27T16:00:00+00:00",
	        "NotificationPoint": 0,
	        "OrderCanExceed": false,
	        "QuantityAvailable": 0,
	        "VariantLevelTracking": false
	    },
	    "Name": "",
	    "QuantityMultiplier": 0,
	    "ShipFromAddressID": "",
	    "ShipHeight": 0,
	    "ShipLength": 0,
	    "ShipWeight": 0,
	    "ShipWidth": 0,
	    "SpecCount": 0,
	    "VariantCount": 0,
	    "xp": {}
	}
| Name | Type | Description | Required | 
|---|---|---|---|
| DefaultPriceScheduleID | string | ID of the default price schedule. | False |
| ID | string | ID of the product. | False |
| Name | string | Name of the product. | True |
| Description | string | Description of the product. | False |
| QuantityMultiplier | integer | Quantity multiplier of the product. | True |
| ShipWeight | float | Ship weight of the product. | False |
| ShipHeight | float | Ship height of the product. | False |
| ShipWidth | float | Ship width of the product. | False |
| ShipLength | float | Ship length of the product. | False |
| Active | boolean | Active of the product. | False |
| SpecCount | integer | Spec count of the product. | False |
| xp | object | Container for extended (custom) properties of the product. | False |
| VariantCount | integer | Variant count of the product. | False |
| ShipFromAddressID | string | ID of the ship from address. | False |
| Inventory | object | Inventory of the product. | False |
| AutoForwardSupplierID | string | ID of the auto forward supplier. | False |

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

## Request Body
**Response Status**: `200`

## Response Body
	{
	    "Items": [
	        {
	            "Active": false,
	            "Description": "",
	            "ID": "",
	            "Name": "",
	            "xp": {}
	        }
	    ],
	    "Meta": {
	        "ItemRange": [
	            1,
	            20
	        ],
	        "Page": 1,
	        "PageSize": 20,
	        "TotalCount": 25,
	        "TotalPages": 2
	    }
	}
| Name | Type | Description | Required | 
|---|---|---|---|
| ID | string | ID of the variant. | False |
| Name | string | Name of the variant. | False |
| Description | string | Description of the variant. | False |
| Active | boolean | Active of the variant. | False |
| xp | object | Container for extended (custom) properties of the variant. | False |

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

## Request Body
	{
	    "Active": false,
	    "Description": "",
	    "ID": "",
	    "Name": "",
	    "xp": {}
	}
| Name | Type | Description | Required | 
|---|---|---|---|
| ID | string | ID of the variant. Can only contain characters Aa-Zz, 0-9, -, and _. Searchable: priority level 1. Sortable: priority level 1. | False |
| Name | string | Name of the variant. Searchable: priority level 2. Sortable: priority level 2. | False |
| Description | string | Description of the variant. Max length 2000 characters. Searchable: priority level 3. | False |
| Active | boolean | Active of the variant. | False |
| xp | object | Container for extended (custom) properties of the variant. | False |

**Response Status**: `200`

## Response Body
	{
	    "Active": false,
	    "Description": "",
	    "ID": "",
	    "Name": "",
	    "xp": {}
	}
| Name | Type | Description | Required | 
|---|---|---|---|
| ID | string | ID of the variant. | False |
| Name | string | Name of the variant. | False |
| Description | string | Description of the variant. | False |
| Active | boolean | Active of the variant. | False |
| xp | object | Container for extended (custom) properties of the variant. | False |

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

## Request Body
	{
	    "Active": false,
	    "Description": "",
	    "ID": "",
	    "Name": "",
	    "xp": {}
	}
| Name | Type | Description | Required | 
|---|---|---|---|
| ID | string | ID of the variant. Can only contain characters Aa-Zz, 0-9, -, and _. Searchable: priority level 1. Sortable: priority level 1. | False |
| Name | string | Name of the variant. Searchable: priority level 2. Sortable: priority level 2. | False |
| Description | string | Description of the variant. Max length 2000 characters. Searchable: priority level 3. | False |
| Active | boolean | Active of the variant. | False |
| xp | object | Container for extended (custom) properties of the variant. | False |

**Response Status**: `200`

## Response Body
	{
	    "Active": false,
	    "Description": "",
	    "ID": "",
	    "Name": "",
	    "xp": {}
	}
| Name | Type | Description | Required | 
|---|---|---|---|
| ID | string | ID of the variant. | False |
| Name | string | Name of the variant. | False |
| Description | string | Description of the variant. | False |
| Active | boolean | Active of the variant. | False |
| xp | object | Container for extended (custom) properties of the variant. | False |

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

## Request Body
**Response Status**: `200`

## Response Body
	{
	    "Active": false,
	    "Description": "",
	    "ID": "",
	    "Name": "",
	    "xp": {}
	}
| Name | Type | Description | Required | 
|---|---|---|---|
| ID | string | ID of the variant. | False |
| Name | string | Name of the variant. | False |
| Description | string | Description of the variant. | False |
| Active | boolean | Active of the variant. | False |
| xp | object | Container for extended (custom) properties of the variant. | False |

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

## Request Body
**Response Status**: `200`

## Response Body
	{
	    "Items": [
	        {
	            "Active": false,
	            "ID": "",
	            "Name": "",
	            "xp": {}
	        }
	    ],
	    "Meta": {
	        "ItemRange": [
	            1,
	            20
	        ],
	        "Page": 1,
	        "PageSize": 20,
	        "TotalCount": 25,
	        "TotalPages": 2
	    }
	}
| Name | Type | Description | Required | 
|---|---|---|---|
| ID | string | ID of the supplier. | False |
| Name | string | Name of the supplier. | True |
| Active | boolean | Active of the supplier. | False |
| xp | object | Container for extended (custom) properties of the supplier. | False |

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

## Request Body
**Response Status**: `204`

## Response Body
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

## Request Body
**Response Status**: `204`

## Response Body
## `POST` `v1/products/assignments`
Save a product assignment
## Request Body
	{
	    "BuyerID": "",
	    "PriceScheduleID": "",
	    "ProductID": "",
	    "UserGroupID": ""
	}
| Name | Type | Description | Required | 
|---|---|---|---|
| ProductID | string | ID of the product. Required. | True |
| BuyerID | string | ID of the buyer. Required. | True |
| UserGroupID | string | ID of the user group. | False |
| PriceScheduleID | string | ID of the price schedule. | False |

**Response Status**: `204`

## Response Body
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

## Request Body
**Response Status**: `200`

## Response Body
	{
	    "Items": [
	        {
	            "BuyerID": "",
	            "PriceScheduleID": "",
	            "ProductID": "",
	            "UserGroupID": ""
	        }
	    ],
	    "Meta": {
	        "ItemRange": [
	            1,
	            20
	        ],
	        "Page": 1,
	        "PageSize": 20,
	        "TotalCount": 25,
	        "TotalPages": 2
	    }
	}
| Name | Type | Description | Required | 
|---|---|---|---|
| ProductID | string | ID of the product. | True |
| BuyerID | string | ID of the buyer. | True |
| UserGroupID | string | ID of the user group. | False |
| PriceScheduleID | string | ID of the price schedule. | False |

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

## Request Body
**Response Status**: `204`

## Response Body