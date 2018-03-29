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

| Name | Type | Description | Required | 
|---|---|---|---|
| productID | string | ID of the product. | True |

## Response Body
	:::json
	{
	    "Active": false,
	    "AutoForwardSupplierID": "",
	    "DefaultPriceScheduleID": "",
	    "Description": "",
	    "ID": "",
	    "Inventory": {
	        "Enabled": false,
	        "LastUpdated": "2018-03-27T19:00:00+00:00",
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

| Name | Type | Description | Required | 
|---|---|---|---|
| catalogID | string | ID of the catalog. | False |
| categoryID | string | ID of the category. | False |
| supplierID | string | ID of the supplier. | False |
| search | string | Word or phrase to search for. | False |
| searchOn | string | Comma-delimited list of fields to search on. | False |
| sortBy | string | Comma-delimited list of fields to sort by. | False |
| page | integer | Page of results to return. Default: 1 | False |
| pageSize | integer | Number of results to return per page. Default: 20, max: 100. | False |
| filters | object | Any additional key/value pairs passed in the query string are interpretted as filters. Valid keys are top-level properties of the returned model or 'xp.???' | False |

## Response Body
	:::json
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
	                "LastUpdated": "2018-03-27T19:00:00+00:00",
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
	:::json
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

## Response Body
	:::json
	{
	    "Active": false,
	    "AutoForwardSupplierID": "",
	    "DefaultPriceScheduleID": "",
	    "Description": "",
	    "ID": "",
	    "Inventory": {
	        "Enabled": false,
	        "LastUpdated": "2018-03-27T19:00:00+00:00",
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

| Name | Type | Description | Required | 
|---|---|---|---|
| productID | string | ID of the product. | True |

## Request Body
	:::json
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

## Response Body
	:::json
	{
	    "Active": false,
	    "AutoForwardSupplierID": "",
	    "DefaultPriceScheduleID": "",
	    "Description": "",
	    "ID": "",
	    "Inventory": {
	        "Enabled": false,
	        "LastUpdated": "2018-03-27T19:00:00+00:00",
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

| Name | Type | Description | Required | 
|---|---|---|---|
| productID | string | ID of the product. | True |

## Response Body
## `PATCH` `v1/products/{productID}`
Partially update a product

| Name | Type | Description | Required | 
|---|---|---|---|
| productID | string | ID of the product. | True |

## Request Body
	:::json
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

## Response Body
	:::json
	{
	    "Active": false,
	    "AutoForwardSupplierID": "",
	    "DefaultPriceScheduleID": "",
	    "Description": "",
	    "ID": "",
	    "Inventory": {
	        "Enabled": false,
	        "LastUpdated": "2018-03-27T19:00:00+00:00",
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

| Name | Type | Description | Required | 
|---|---|---|---|
| productID | string | ID of the product. | True |
| overwriteExisting | boolean | Overwrite existing of the product. | False |

## Response Body
	:::json
	{
	    "Active": false,
	    "AutoForwardSupplierID": "",
	    "DefaultPriceScheduleID": "",
	    "Description": "",
	    "ID": "",
	    "Inventory": {
	        "Enabled": false,
	        "LastUpdated": "2018-03-27T19:00:00+00:00",
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

| Name | Type | Description | Required | 
|---|---|---|---|
| productID | string | ID of the product. | True |
| search | string | Word or phrase to search for. | False |
| searchOn | string | Comma-delimited list of fields to search on. | False |
| sortBy | string | Comma-delimited list of fields to sort by. | False |
| page | integer | Page of results to return. Default: 1 | False |
| pageSize | integer | Number of results to return per page. Default: 20, max: 100. | False |
| filters | object | Any additional key/value pairs passed in the query string are interpretted as filters. Valid keys are top-level properties of the returned model or 'xp.???' | False |

## Response Body
	:::json
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

| Name | Type | Description | Required | 
|---|---|---|---|
| productID | string | ID of the product. | True |
| variantID | string | ID of the variant. | True |

## Request Body
	:::json
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

## Response Body
	:::json
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

| Name | Type | Description | Required | 
|---|---|---|---|
| productID | string | ID of the product. | True |
| variantID | string | ID of the variant. | True |

## Request Body
	:::json
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

## Response Body
	:::json
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

| Name | Type | Description | Required | 
|---|---|---|---|
| productID | string | ID of the product. | True |
| variantID | string | ID of the variant. | True |

## Response Body
	:::json
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

| Name | Type | Description | Required | 
|---|---|---|---|
| productID | string | ID of the product. | True |
| search | string | Word or phrase to search for. | False |
| searchOn | string | Comma-delimited list of fields to search on. | False |
| sortBy | string | Comma-delimited list of fields to sort by. | False |
| page | integer | Page of results to return. Default: 1 | False |
| pageSize | integer | Number of results to return per page. Default: 20, max: 100. | False |
| filters | object | Any additional key/value pairs passed in the query string are interpretted as filters. Valid keys are top-level properties of the returned model or 'xp.???' | False |

## Response Body
	:::json
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

| Name | Type | Description | Required | 
|---|---|---|---|
| productID | string | ID of the product. | True |
| supplierID | string | ID of the supplier. | True |

## Response Body
## `DELETE` `v1/products/{productID}/suppliers/{supplierID}`
Remove a supplier

| Name | Type | Description | Required | 
|---|---|---|---|
| productID | string | ID of the product. | True |
| supplierID | string | ID of the supplier. | True |

## Response Body
## `POST` `v1/products/assignments`
Save a product assignment
## Request Body
	:::json
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

## Response Body
## `GET` `v1/products/assignments`
Get a list of product assignments

| Name | Type | Description | Required | 
|---|---|---|---|
| productID | string | ID of the product. | False |
| priceScheduleID | string | ID of the price schedule. | False |
| buyerID | string | ID of the buyer. | False |
| userID | string | ID of the user. | False |
| userGroupID | string | ID of the user group. | False |
| level | string | Level of the product assignment. Possible values: User, Group, Company. | False |
| page | integer | Page of results to return. Default: 1 | False |
| pageSize | integer | Number of results to return per page. Default: 20, max: 100. | False |

## Response Body
	:::json
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

| Name | Type | Description | Required | 
|---|---|---|---|
| productID | string | ID of the product. | True |
| buyerID | string | ID of the buyer. | True |
| userID | string | ID of the user. | False |
| userGroupID | string | ID of the user group. | False |

## Response Body