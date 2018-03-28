---
title: Price Schedules
date: 2018-03-27
category: API Reference
tags: Product Catalogs
slug: Product-Catalogs-PriceSchedules
---
Price schedules allow the same product to be sold across multiple
channels. A price schedule may include quantity price breaks, min and
max quantity per order, whether to apply tax or shipping calculations,
or to what type of order the price schedule applies.

---

## `GET` `v1/priceschedules/{priceScheduleID}`
Get a single price schedule

| Name | Type | Description | Required | 
|---|---|---|---|
| priceScheduleID | string | ID of the price schedule. | True |

## Response Body
	:::json
	{
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
	}


| Name | Type | Description | Required | 
|---|---|---|---|
| ID | string | ID of the price schedule. | False |
| Name | string | Name of the price schedule. | True |
| ApplyTax | boolean | Apply tax of the price schedule. | False |
| ApplyShipping | boolean | Apply shipping of the price schedule. | False |
| MinQuantity | integer | Min quantity of the price schedule. | False |
| MaxQuantity | integer | Max quantity of the price schedule. | False |
| UseCumulativeQuantity | boolean | Use cumulative quantity of the price schedule. | False |
| RestrictedQuantity | boolean | Restricted quantity of the price schedule. | False |
| PriceBreaks | array | Price breaks of the price schedule. | False |
| xp | object | Container for extended (custom) properties of the price schedule. | False |

## `GET` `v1/priceschedules`
Get a list of price schedules

| Name | Type | Description | Required | 
|---|---|---|---|
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
| ID | string | ID of the price schedule. | False |
| Name | string | Name of the price schedule. | True |
| ApplyTax | boolean | Apply tax of the price schedule. | False |
| ApplyShipping | boolean | Apply shipping of the price schedule. | False |
| MinQuantity | integer | Min quantity of the price schedule. | False |
| MaxQuantity | integer | Max quantity of the price schedule. | False |
| UseCumulativeQuantity | boolean | Use cumulative quantity of the price schedule. | False |
| RestrictedQuantity | boolean | Restricted quantity of the price schedule. | False |
| PriceBreaks | array | Price breaks of the price schedule. | False |
| xp | object | Container for extended (custom) properties of the price schedule. | False |

## `POST` `v1/priceschedules`
Create a new price schedule
## Request Body
	:::json
	{
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
	}


| Name | Type | Description | Required | 
|---|---|---|---|
| ID | string | ID of the price schedule. Can only contain characters Aa-Zz, 0-9, -, and _. Searchable: priority level 1. Sortable: priority level 2. | False |
| Name | string | Name of the price schedule. Required. Max length 100 characters. Searchable: priority level 2. Sortable: priority level 1. | True |
| ApplyTax | boolean | Apply tax of the price schedule. Searchable: priority level 3. | False |
| ApplyShipping | boolean | Apply shipping of the price schedule. | False |
| MinQuantity | integer | Min quantity of the price schedule. Must be at least 1. | False |
| MaxQuantity | integer | Max quantity of the price schedule. | False |
| UseCumulativeQuantity | boolean | Use cumulative quantity of the price schedule. | False |
| RestrictedQuantity | boolean | Restricted quantity of the price schedule. | False |
| PriceBreaks | array | Price breaks of the price schedule. | False |
| xp | object | Container for extended (custom) properties of the price schedule. | False |

## Response Body
	:::json
	{
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
	}


| Name | Type | Description | Required | 
|---|---|---|---|
| ID | string | ID of the price schedule. | False |
| Name | string | Name of the price schedule. | True |
| ApplyTax | boolean | Apply tax of the price schedule. | False |
| ApplyShipping | boolean | Apply shipping of the price schedule. | False |
| MinQuantity | integer | Min quantity of the price schedule. | False |
| MaxQuantity | integer | Max quantity of the price schedule. | False |
| UseCumulativeQuantity | boolean | Use cumulative quantity of the price schedule. | False |
| RestrictedQuantity | boolean | Restricted quantity of the price schedule. | False |
| PriceBreaks | array | Price breaks of the price schedule. | False |
| xp | object | Container for extended (custom) properties of the price schedule. | False |

## `PUT` `v1/priceschedules/{priceScheduleID}`
Create or update a price schedule

| Name | Type | Description | Required | 
|---|---|---|---|
| priceScheduleID | string | ID of the price schedule. | True |

## Request Body
	:::json
	{
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
	}


| Name | Type | Description | Required | 
|---|---|---|---|
| ID | string | ID of the price schedule. Can only contain characters Aa-Zz, 0-9, -, and _. Searchable: priority level 1. Sortable: priority level 2. | False |
| Name | string | Name of the price schedule. Required. Max length 100 characters. Searchable: priority level 2. Sortable: priority level 1. | True |
| ApplyTax | boolean | Apply tax of the price schedule. Searchable: priority level 3. | False |
| ApplyShipping | boolean | Apply shipping of the price schedule. | False |
| MinQuantity | integer | Min quantity of the price schedule. Must be at least 1. | False |
| MaxQuantity | integer | Max quantity of the price schedule. | False |
| UseCumulativeQuantity | boolean | Use cumulative quantity of the price schedule. | False |
| RestrictedQuantity | boolean | Restricted quantity of the price schedule. | False |
| PriceBreaks | array | Price breaks of the price schedule. | False |
| xp | object | Container for extended (custom) properties of the price schedule. | False |

## Response Body
	:::json
	{
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
	}


| Name | Type | Description | Required | 
|---|---|---|---|
| ID | string | ID of the price schedule. | False |
| Name | string | Name of the price schedule. | True |
| ApplyTax | boolean | Apply tax of the price schedule. | False |
| ApplyShipping | boolean | Apply shipping of the price schedule. | False |
| MinQuantity | integer | Min quantity of the price schedule. | False |
| MaxQuantity | integer | Max quantity of the price schedule. | False |
| UseCumulativeQuantity | boolean | Use cumulative quantity of the price schedule. | False |
| RestrictedQuantity | boolean | Restricted quantity of the price schedule. | False |
| PriceBreaks | array | Price breaks of the price schedule. | False |
| xp | object | Container for extended (custom) properties of the price schedule. | False |

## `DELETE` `v1/priceschedules/{priceScheduleID}`
Delete a price schedule

| Name | Type | Description | Required | 
|---|---|---|---|
| priceScheduleID | string | ID of the price schedule. | True |

## Response Body
## `PATCH` `v1/priceschedules/{priceScheduleID}`
Partially update a price schedule

| Name | Type | Description | Required | 
|---|---|---|---|
| priceScheduleID | string | ID of the price schedule. | True |

## Request Body
	:::json
	{
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
	}


| Name | Type | Description | Required | 
|---|---|---|---|
| ID | string | ID of the price schedule. Can only contain characters Aa-Zz, 0-9, -, and _. Searchable: priority level 1. Sortable: priority level 2. | False |
| Name | string | Name of the price schedule. Required. Max length 100 characters. Searchable: priority level 2. Sortable: priority level 1. | True |
| ApplyTax | boolean | Apply tax of the price schedule. Searchable: priority level 3. | False |
| ApplyShipping | boolean | Apply shipping of the price schedule. | False |
| MinQuantity | integer | Min quantity of the price schedule. Must be at least 1. | False |
| MaxQuantity | integer | Max quantity of the price schedule. | False |
| UseCumulativeQuantity | boolean | Use cumulative quantity of the price schedule. | False |
| RestrictedQuantity | boolean | Restricted quantity of the price schedule. | False |
| PriceBreaks | array | Price breaks of the price schedule. | False |
| xp | object | Container for extended (custom) properties of the price schedule. | False |

## Response Body
	:::json
	{
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
	}


| Name | Type | Description | Required | 
|---|---|---|---|
| ID | string | ID of the price schedule. | False |
| Name | string | Name of the price schedule. | True |
| ApplyTax | boolean | Apply tax of the price schedule. | False |
| ApplyShipping | boolean | Apply shipping of the price schedule. | False |
| MinQuantity | integer | Min quantity of the price schedule. | False |
| MaxQuantity | integer | Max quantity of the price schedule. | False |
| UseCumulativeQuantity | boolean | Use cumulative quantity of the price schedule. | False |
| RestrictedQuantity | boolean | Restricted quantity of the price schedule. | False |
| PriceBreaks | array | Price breaks of the price schedule. | False |
| xp | object | Container for extended (custom) properties of the price schedule. | False |

## `POST` `v1/priceschedules/{priceScheduleID}/PriceBreaks`
Save a price schedule price break

| Name | Type | Description | Required | 
|---|---|---|---|
| priceScheduleID | string | ID of the price schedule. | True |

## Request Body
	:::json
	{
	    "Price": 0,
	    "Quantity": 0
	}


| Name | Type | Description | Required | 
|---|---|---|---|
| Quantity | integer | Quantity of the price break. Required. Must be at least 0. | True |
| Price | float | Price of the price break. Required. | True |

## Response Body
	:::json
	{
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
	}


| Name | Type | Description | Required | 
|---|---|---|---|
| ID | string | ID of the price schedule. | False |
| Name | string | Name of the price schedule. | True |
| ApplyTax | boolean | Apply tax of the price schedule. | False |
| ApplyShipping | boolean | Apply shipping of the price schedule. | False |
| MinQuantity | integer | Min quantity of the price schedule. | False |
| MaxQuantity | integer | Max quantity of the price schedule. | False |
| UseCumulativeQuantity | boolean | Use cumulative quantity of the price schedule. | False |
| RestrictedQuantity | boolean | Restricted quantity of the price schedule. | False |
| PriceBreaks | array | Price breaks of the price schedule. | False |
| xp | object | Container for extended (custom) properties of the price schedule. | False |

## `DELETE` `v1/priceschedules/{priceScheduleID}/PriceBreaks`
Delete a price schedule price break

| Name | Type | Description | Required | 
|---|---|---|---|
| priceScheduleID | string | ID of the price schedule. | True |
| quantity | integer | Quantity of the price schedule. | True |

## Response Body