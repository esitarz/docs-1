---
title: Products
date: 2018-03-27
category: API Reference
tags: Me And My Stuff
slug: Me-And-My-Stuff-MeProducts
---
"Me" is a container for read-only endpoints that return a filtered view
of things that the current buyer user is allowed to see, i.e. things
that they are assigned to either directly or as a member of a buyer
organization or user group. It also provides ways for a user to update
or change their own information.

---

## `GET` `v1/me/products`
Get a list of products visible to this user

| Name | Type | Description | Required | 
|---|---|---|---|
| catalogID | string | ID of the catalog. | False |
| categoryID | string | ID of the category. | False |
| depth | string | Depth of the product. | False |
| search | string | Word or phrase to search for. | False |
| searchOn | string | Comma-delimited list of fields to search on. | False |
| sortBy | string | Comma-delimited list of fields to sort by. | False |
| page | integer | Page of results to return. Default: 1 | False |
| pageSize | integer | Number of results to return per page. Default: 20, max: 100. | False |
| filters | object | Any additional key/value pairs passed in the query string are interpretted as filters. Valid keys are top-level properties of the returned model or 'xp.???' | False |

## Response Body
	{
	    "Items": [
	        {
	            "Active": false,
	            "AutoForwardSupplierID": "",
	            "Description": "",
	            "ID": "",
	            "Inventory": {
	                "Enabled": false,
	                "LastUpdated": "2018-03-21T23:00:00+00:00",
	                "NotificationPoint": 0,
	                "OrderCanExceed": false,
	                "QuantityAvailable": 0,
	                "VariantLevelTracking": false
	            },
	            "Name": "",
	            "PriceSchedule": {
	                "ApplyShipping": false,
	                "ApplyTax": false,
	                "ID": "",
	                "MaxQuantity": 0,
	                "MinQuantity": 0,
	                "Name": "",
	                "PriceBreaks": [
	                    {
	                        "Price": 0,
	                        "Quantity": 0
	                    }
	                ],
	                "RestrictedQuantity": false,
	                "UseCumulativeQuantity": false,
	                "xp": {}
	            },
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
| ID | string | ID of the product. | False |
| PriceSchedule | object | Price schedule of the product. | False |
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

## `GET` `v1/me/products/{productID}`
Get a single product

| Name | Type | Description | Required | 
|---|---|---|---|
| productID | string | ID of the product. | True |

## Response Body
	{
	    "Active": false,
	    "AutoForwardSupplierID": "",
	    "Description": "",
	    "ID": "",
	    "Inventory": {
	        "Enabled": false,
	        "LastUpdated": "2018-03-21T23:00:00+00:00",
	        "NotificationPoint": 0,
	        "OrderCanExceed": false,
	        "QuantityAvailable": 0,
	        "VariantLevelTracking": false
	    },
	    "Name": "",
	    "PriceSchedule": {
	        "ApplyShipping": false,
	        "ApplyTax": false,
	        "ID": "",
	        "MaxQuantity": 0,
	        "MinQuantity": 0,
	        "Name": "",
	        "PriceBreaks": [
	            {
	                "Price": 0,
	                "Quantity": 0
	            }
	        ],
	        "RestrictedQuantity": false,
	        "UseCumulativeQuantity": false,
	        "xp": {}
	    },
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
| ID | string | ID of the product. | False |
| PriceSchedule | object | Price schedule of the product. | False |
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

## `GET` `v1/me/products/{productID}/specs`
Get a list of specs visible to this user

| Name | Type | Description | Required | 
|---|---|---|---|
| productID | string | ID of the product. | True |
| catalogID | string | ID of the catalog. | False |
| search | string | Word or phrase to search for. | False |
| searchOn | string | Comma-delimited list of fields to search on. | False |
| sortBy | string | Comma-delimited list of fields to sort by. | False |
| page | integer | Page of results to return. Default: 1 | False |
| pageSize | integer | Number of results to return per page. Default: 20, max: 100. | False |
| filters | object | Any additional key/value pairs passed in the query string are interpretted as filters. Valid keys are top-level properties of the returned model or 'xp.???' | False |

## Response Body
	{
	    "Items": [
	        {
	            "AllowOpenText": false,
	            "DefaultOptionID": "",
	            "DefaultValue": "",
	            "DefinesVariant": false,
	            "ID": "",
	            "ListOrder": 1,
	            "Name": "",
	            "Options": [
	                {
	                    "ID": "",
	                    "IsOpenText": false,
	                    "ListOrder": 1,
	                    "PriceMarkup": 0,
	                    "PriceMarkupType": "NoMarkup",
	                    "Value": "",
	                    "xp": {}
	                }
	            ],
	            "Required": false,
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
| Options | array | Options of the spec. | False |
| ID | string | ID of the spec. | False |
| ListOrder | integer | List order of the spec. | False |
| Name | string | Name of the spec. | True |
| DefaultValue | string | Default value of the spec. | False |
| Required | boolean | Required of the spec. | False |
| AllowOpenText | boolean | Allow open text of the spec. | False |
| DefaultOptionID | string | ID of the default option. | False |
| DefinesVariant | boolean | True if each unique combinations of this Spec's Options map to unique Product Variants/SKUs. | False |
| xp | object | Container for extended (custom) properties of the spec. | False |

## `GET` `v1/me/products/{productID}/specs/{specID}`
Get a single spec

| Name | Type | Description | Required | 
|---|---|---|---|
| productID | string | ID of the product. | True |
| specID | string | ID of the spec. | True |
| catalogID | string | ID of the catalog. | False |

## Response Body
	{
	    "AllowOpenText": false,
	    "DefaultOptionID": "",
	    "DefaultValue": "",
	    "DefinesVariant": false,
	    "ID": "",
	    "ListOrder": 1,
	    "Name": "",
	    "Options": [
	        {
	            "ID": "",
	            "IsOpenText": false,
	            "ListOrder": 1,
	            "PriceMarkup": 0,
	            "PriceMarkupType": "NoMarkup",
	            "Value": "",
	            "xp": {}
	        }
	    ],
	    "Required": false,
	    "xp": {}
	}
| Name | Type | Description | Required | 
|---|---|---|---|
| Options | array | Options of the spec. | False |
| ID | string | ID of the spec. | False |
| ListOrder | integer | List order of the spec. | False |
| Name | string | Name of the spec. | True |
| DefaultValue | string | Default value of the spec. | False |
| Required | boolean | Required of the spec. | False |
| AllowOpenText | boolean | Allow open text of the spec. | False |
| DefaultOptionID | string | ID of the default option. | False |
| DefinesVariant | boolean | True if each unique combinations of this Spec's Options map to unique Product Variants/SKUs. | False |
| xp | object | Container for extended (custom) properties of the spec. | False |
