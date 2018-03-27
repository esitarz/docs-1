---
title: Specs
date: 2018-03-27
category: API Reference
tags: Product Catalogs
slug: Product-Catalogs-Specs
---
Specs are used to capture user input when adding a Product to an Order.
At its simplest, a spec is a name/value pair. A spec value may have a
price markup or markdown associated with it. In more advanced scenarios,
specs can drive the product SKU. For example, a product may be available
in 3 colors and 3 sizes and therefore have a total of 9 SKUs. **The
OrderCloud platform will choose the correct SKU based on the
user-selected color and size specs**.

---

## `GET` `v1/specs/{specID}`
Get a single spec

| Name | Type | Description | Required | 
|---|---|---|---|
| specID | string | ID of the spec. | True |

## Response Body
	{
	    "AllowOpenText": false,
	    "DefaultOptionID": "",
	    "DefaultValue": "",
	    "DefinesVariant": false,
	    "ID": "",
	    "ListOrder": 1,
	    "Name": "",
	    "OptionCount": 0,
	    "Required": false,
	    "xp": {}
	}
| Name | Type | Description | Required | 
|---|---|---|---|
| OptionCount | integer | Option count of the spec. | False |
| ID | string | ID of the spec. | False |
| ListOrder | integer | List order of the spec. | False |
| Name | string | Name of the spec. | True |
| DefaultValue | string | Default value of the spec. | False |
| Required | boolean | Required of the spec. | False |
| AllowOpenText | boolean | Allow open text of the spec. | False |
| DefaultOptionID | string | ID of the default option. | False |
| DefinesVariant | boolean | True if each unique combinations of this Spec's Options map to unique Product Variants/SKUs. | False |
| xp | object | Container for extended (custom) properties of the spec. | False |

## `GET` `v1/specs`
Get a list of specs

| Name | Type | Description | Required | 
|---|---|---|---|
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
	            "OptionCount": 0,
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
| OptionCount | integer | Option count of the spec. | False |
| ID | string | ID of the spec. | False |
| ListOrder | integer | List order of the spec. | False |
| Name | string | Name of the spec. | True |
| DefaultValue | string | Default value of the spec. | False |
| Required | boolean | Required of the spec. | False |
| AllowOpenText | boolean | Allow open text of the spec. | False |
| DefaultOptionID | string | ID of the default option. | False |
| DefinesVariant | boolean | True if each unique combinations of this Spec's Options map to unique Product Variants/SKUs. | False |
| xp | object | Container for extended (custom) properties of the spec. | False |

## `POST` `v1/specs`
Create a new spec
## Request Body
	{
	    "AllowOpenText": false,
	    "DefaultOptionID": "",
	    "DefaultValue": "",
	    "DefinesVariant": false,
	    "ID": "",
	    "ListOrder": 1,
	    "Name": "",
	    "Required": false,
	    "xp": {}
	}
| Name | Type | Description | Required | 
|---|---|---|---|
| ID | string | ID of the spec. Can only contain characters Aa-Zz, 0-9, -, and _. Searchable: priority level 3. Sortable: priority level 3. | False |
| ListOrder | integer | List order of the spec. Searchable: priority level 2. Sortable: priority level 1. | False |
| Name | string | Name of the spec. Required. Searchable: priority level 1. Sortable: priority level 2. | True |
| DefaultValue | string | Default value of the spec. Max length 2000 characters. | False |
| Required | boolean | Required of the spec. Searchable: priority level 4. | False |
| AllowOpenText | boolean | Allow open text of the spec. Searchable: priority level 5. | False |
| DefaultOptionID | string | ID of the default option. | False |
| DefinesVariant | boolean | True if each unique combinations of this Spec's Options map to unique Product Variants/SKUs. | False |
| xp | object | Container for extended (custom) properties of the spec. | False |

## Response Body
	{
	    "AllowOpenText": false,
	    "DefaultOptionID": "",
	    "DefaultValue": "",
	    "DefinesVariant": false,
	    "ID": "",
	    "ListOrder": 1,
	    "Name": "",
	    "OptionCount": 0,
	    "Required": false,
	    "xp": {}
	}
| Name | Type | Description | Required | 
|---|---|---|---|
| OptionCount | integer | Option count of the spec. | False |
| ID | string | ID of the spec. | False |
| ListOrder | integer | List order of the spec. | False |
| Name | string | Name of the spec. | True |
| DefaultValue | string | Default value of the spec. | False |
| Required | boolean | Required of the spec. | False |
| AllowOpenText | boolean | Allow open text of the spec. | False |
| DefaultOptionID | string | ID of the default option. | False |
| DefinesVariant | boolean | True if each unique combinations of this Spec's Options map to unique Product Variants/SKUs. | False |
| xp | object | Container for extended (custom) properties of the spec. | False |

## `PUT` `v1/specs/{specID}`
Create or update a spec

| Name | Type | Description | Required | 
|---|---|---|---|
| specID | string | ID of the spec. | True |

## Request Body
	{
	    "AllowOpenText": false,
	    "DefaultOptionID": "",
	    "DefaultValue": "",
	    "DefinesVariant": false,
	    "ID": "",
	    "ListOrder": 1,
	    "Name": "",
	    "Required": false,
	    "xp": {}
	}
| Name | Type | Description | Required | 
|---|---|---|---|
| ID | string | ID of the spec. Can only contain characters Aa-Zz, 0-9, -, and _. Searchable: priority level 3. Sortable: priority level 3. | False |
| ListOrder | integer | List order of the spec. Searchable: priority level 2. Sortable: priority level 1. | False |
| Name | string | Name of the spec. Required. Searchable: priority level 1. Sortable: priority level 2. | True |
| DefaultValue | string | Default value of the spec. Max length 2000 characters. | False |
| Required | boolean | Required of the spec. Searchable: priority level 4. | False |
| AllowOpenText | boolean | Allow open text of the spec. Searchable: priority level 5. | False |
| DefaultOptionID | string | ID of the default option. | False |
| DefinesVariant | boolean | True if each unique combinations of this Spec's Options map to unique Product Variants/SKUs. | False |
| xp | object | Container for extended (custom) properties of the spec. | False |

## Response Body
	{
	    "AllowOpenText": false,
	    "DefaultOptionID": "",
	    "DefaultValue": "",
	    "DefinesVariant": false,
	    "ID": "",
	    "ListOrder": 1,
	    "Name": "",
	    "OptionCount": 0,
	    "Required": false,
	    "xp": {}
	}
| Name | Type | Description | Required | 
|---|---|---|---|
| OptionCount | integer | Option count of the spec. | False |
| ID | string | ID of the spec. | False |
| ListOrder | integer | List order of the spec. | False |
| Name | string | Name of the spec. | True |
| DefaultValue | string | Default value of the spec. | False |
| Required | boolean | Required of the spec. | False |
| AllowOpenText | boolean | Allow open text of the spec. | False |
| DefaultOptionID | string | ID of the default option. | False |
| DefinesVariant | boolean | True if each unique combinations of this Spec's Options map to unique Product Variants/SKUs. | False |
| xp | object | Container for extended (custom) properties of the spec. | False |

## `DELETE` `v1/specs/{specID}`
Delete a spec

| Name | Type | Description | Required | 
|---|---|---|---|
| specID | string | ID of the spec. | True |

## Response Body
## `PATCH` `v1/specs/{specID}`
Partially update a spec

| Name | Type | Description | Required | 
|---|---|---|---|
| specID | string | ID of the spec. | True |

## Request Body
	{
	    "AllowOpenText": false,
	    "DefaultOptionID": "",
	    "DefaultValue": "",
	    "DefinesVariant": false,
	    "ID": "",
	    "ListOrder": 1,
	    "Name": "",
	    "Required": false,
	    "xp": {}
	}
| Name | Type | Description | Required | 
|---|---|---|---|
| ID | string | ID of the spec. Can only contain characters Aa-Zz, 0-9, -, and _. Searchable: priority level 3. Sortable: priority level 3. | False |
| ListOrder | integer | List order of the spec. Searchable: priority level 2. Sortable: priority level 1. | False |
| Name | string | Name of the spec. Required. Searchable: priority level 1. Sortable: priority level 2. | True |
| DefaultValue | string | Default value of the spec. Max length 2000 characters. | False |
| Required | boolean | Required of the spec. Searchable: priority level 4. | False |
| AllowOpenText | boolean | Allow open text of the spec. Searchable: priority level 5. | False |
| DefaultOptionID | string | ID of the default option. | False |
| DefinesVariant | boolean | True if each unique combinations of this Spec's Options map to unique Product Variants/SKUs. | False |
| xp | object | Container for extended (custom) properties of the spec. | False |

## Response Body
	{
	    "AllowOpenText": false,
	    "DefaultOptionID": "",
	    "DefaultValue": "",
	    "DefinesVariant": false,
	    "ID": "",
	    "ListOrder": 1,
	    "Name": "",
	    "OptionCount": 0,
	    "Required": false,
	    "xp": {}
	}
| Name | Type | Description | Required | 
|---|---|---|---|
| OptionCount | integer | Option count of the spec. | False |
| ID | string | ID of the spec. | False |
| ListOrder | integer | List order of the spec. | False |
| Name | string | Name of the spec. | True |
| DefaultValue | string | Default value of the spec. | False |
| Required | boolean | Required of the spec. | False |
| AllowOpenText | boolean | Allow open text of the spec. | False |
| DefaultOptionID | string | ID of the default option. | False |
| DefinesVariant | boolean | True if each unique combinations of this Spec's Options map to unique Product Variants/SKUs. | False |
| xp | object | Container for extended (custom) properties of the spec. | False |

## `GET` `v1/specs/productassignments`
Get a list of spec product assignments

| Name | Type | Description | Required | 
|---|---|---|---|
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
	            "DefaultOptionID": "",
	            "DefaultValue": "",
	            "ProductID": "",
	            "SpecID": ""
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
| SpecID | string | ID of the spec. | False |
| ProductID | string | ID of the product. | False |
| DefaultValue | string | Optional. When defined, overrides the DefaultValue set on the Spec for just this Product. | False |
| DefaultOptionID | string | Optional. When defined, overrides the DefaultOptionID set on the Spec for just this Product. | False |

## `DELETE` `v1/specs/{specID}/productassignments/{productID}`
Delete a spec product assignment

| Name | Type | Description | Required | 
|---|---|---|---|
| specID | string | ID of the spec. | True |
| productID | string | ID of the product. | True |

## Response Body
## `POST` `v1/specs/productassignments`
Save a spec product assignment
## Request Body
	{
	    "DefaultOptionID": "",
	    "DefaultValue": "",
	    "ProductID": "",
	    "SpecID": ""
	}
| Name | Type | Description | Required | 
|---|---|---|---|
| SpecID | string | ID of the spec. Searchable: priority level 1. Sortable: priority level 1. | False |
| ProductID | string | ID of the product. Searchable: priority level 2. Sortable: priority level 2. | False |
| DefaultValue | string | Optional. When defined, overrides the DefaultValue set on the Spec for just this Product. | False |
| DefaultOptionID | string | Optional. When defined, overrides the DefaultOptionID set on the Spec for just this Product. | False |

## Response Body
## `POST` `v1/specs/{specID}/options`
Create a new spec option

| Name | Type | Description | Required | 
|---|---|---|---|
| specID | string | ID of the spec. | True |

## Request Body
	{
	    "ID": "",
	    "IsOpenText": false,
	    "ListOrder": 1,
	    "PriceMarkup": 0,
	    "PriceMarkupType": "NoMarkup",
	    "Value": "",
	    "xp": {}
	}
| Name | Type | Description | Required | 
|---|---|---|---|
| ID | string | ID of the spec option. Can only contain characters Aa-Zz, 0-9, -, and _. Searchable: priority level 2. Sortable: priority level 2. | False |
| Value | string | Value of the spec option. Required. Max length 2000 characters. Searchable: priority level 1. | True |
| ListOrder | integer | List order of the spec option. Searchable: priority level 4. Sortable: priority level 1. | False |
| IsOpenText | boolean | Is open text of the spec option. Searchable: priority level 3. | False |
| PriceMarkupType | string | Price markup type of the spec option. Searchable: priority level 5. Possible values: NoMarkup, AmountPerQuantity, AmountTotal, Percentage. | False |
| PriceMarkup | float | Price markup of the spec option. Searchable: priority level 6. | False |
| xp | object | Container for extended (custom) properties of the spec option. | False |

## Response Body
	{
	    "ID": "",
	    "IsOpenText": false,
	    "ListOrder": 1,
	    "PriceMarkup": 0,
	    "PriceMarkupType": "NoMarkup",
	    "Value": "",
	    "xp": {}
	}
| Name | Type | Description | Required | 
|---|---|---|---|
| ID | string | ID of the spec option. | False |
| Value | string | Value of the spec option. | True |
| ListOrder | integer | List order of the spec option. | False |
| IsOpenText | boolean | Is open text of the spec option. | False |
| PriceMarkupType | string | Price markup type of the spec option. Possible values: NoMarkup, AmountPerQuantity, AmountTotal, Percentage. | False |
| PriceMarkup | float | Price markup of the spec option. | False |
| xp | object | Container for extended (custom) properties of the spec option. | False |

## `GET` `v1/specs/{specID}/options`
Get a list of spec options

| Name | Type | Description | Required | 
|---|---|---|---|
| specID | string | ID of the spec. | True |
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
	            "ID": "",
	            "IsOpenText": false,
	            "ListOrder": 1,
	            "PriceMarkup": 0,
	            "PriceMarkupType": "NoMarkup",
	            "Value": "",
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
| ID | string | ID of the spec option. | False |
| Value | string | Value of the spec option. | True |
| ListOrder | integer | List order of the spec option. | False |
| IsOpenText | boolean | Is open text of the spec option. | False |
| PriceMarkupType | string | Price markup type of the spec option. Possible values: NoMarkup, AmountPerQuantity, AmountTotal, Percentage. | False |
| PriceMarkup | float | Price markup of the spec option. | False |
| xp | object | Container for extended (custom) properties of the spec option. | False |

## `PUT` `v1/specs/{specID}/options/{optionID}`
Create or update a spec option

| Name | Type | Description | Required | 
|---|---|---|---|
| specID | string | ID of the spec. | True |
| optionID | string | ID of the option. | True |

## Request Body
	{
	    "ID": "",
	    "IsOpenText": false,
	    "ListOrder": 1,
	    "PriceMarkup": 0,
	    "PriceMarkupType": "NoMarkup",
	    "Value": "",
	    "xp": {}
	}
| Name | Type | Description | Required | 
|---|---|---|---|
| ID | string | ID of the spec option. Can only contain characters Aa-Zz, 0-9, -, and _. Searchable: priority level 2. Sortable: priority level 2. | False |
| Value | string | Value of the spec option. Required. Max length 2000 characters. Searchable: priority level 1. | True |
| ListOrder | integer | List order of the spec option. Searchable: priority level 4. Sortable: priority level 1. | False |
| IsOpenText | boolean | Is open text of the spec option. Searchable: priority level 3. | False |
| PriceMarkupType | string | Price markup type of the spec option. Searchable: priority level 5. Possible values: NoMarkup, AmountPerQuantity, AmountTotal, Percentage. | False |
| PriceMarkup | float | Price markup of the spec option. Searchable: priority level 6. | False |
| xp | object | Container for extended (custom) properties of the spec option. | False |

## Response Body
	{
	    "ID": "",
	    "IsOpenText": false,
	    "ListOrder": 1,
	    "PriceMarkup": 0,
	    "PriceMarkupType": "NoMarkup",
	    "Value": "",
	    "xp": {}
	}
| Name | Type | Description | Required | 
|---|---|---|---|
| ID | string | ID of the spec option. | False |
| Value | string | Value of the spec option. | True |
| ListOrder | integer | List order of the spec option. | False |
| IsOpenText | boolean | Is open text of the spec option. | False |
| PriceMarkupType | string | Price markup type of the spec option. Possible values: NoMarkup, AmountPerQuantity, AmountTotal, Percentage. | False |
| PriceMarkup | float | Price markup of the spec option. | False |
| xp | object | Container for extended (custom) properties of the spec option. | False |

## `PATCH` `v1/specs/{specID}/options/{optionID}`
Partially update a spec option

| Name | Type | Description | Required | 
|---|---|---|---|
| specID | string | ID of the spec. | True |
| optionID | string | ID of the option. | True |

## Request Body
	{
	    "ID": "",
	    "IsOpenText": false,
	    "ListOrder": 1,
	    "PriceMarkup": 0,
	    "PriceMarkupType": "NoMarkup",
	    "Value": "",
	    "xp": {}
	}
| Name | Type | Description | Required | 
|---|---|---|---|
| ID | string | ID of the spec option. Can only contain characters Aa-Zz, 0-9, -, and _. Searchable: priority level 2. Sortable: priority level 2. | False |
| Value | string | Value of the spec option. Required. Max length 2000 characters. Searchable: priority level 1. | True |
| ListOrder | integer | List order of the spec option. Searchable: priority level 4. Sortable: priority level 1. | False |
| IsOpenText | boolean | Is open text of the spec option. Searchable: priority level 3. | False |
| PriceMarkupType | string | Price markup type of the spec option. Searchable: priority level 5. Possible values: NoMarkup, AmountPerQuantity, AmountTotal, Percentage. | False |
| PriceMarkup | float | Price markup of the spec option. Searchable: priority level 6. | False |
| xp | object | Container for extended (custom) properties of the spec option. | False |

## Response Body
	{
	    "ID": "",
	    "IsOpenText": false,
	    "ListOrder": 1,
	    "PriceMarkup": 0,
	    "PriceMarkupType": "NoMarkup",
	    "Value": "",
	    "xp": {}
	}
| Name | Type | Description | Required | 
|---|---|---|---|
| ID | string | ID of the spec option. | False |
| Value | string | Value of the spec option. | True |
| ListOrder | integer | List order of the spec option. | False |
| IsOpenText | boolean | Is open text of the spec option. | False |
| PriceMarkupType | string | Price markup type of the spec option. Possible values: NoMarkup, AmountPerQuantity, AmountTotal, Percentage. | False |
| PriceMarkup | float | Price markup of the spec option. | False |
| xp | object | Container for extended (custom) properties of the spec option. | False |

## `GET` `v1/specs/{specID}/options/{optionID}`
Get a single spec option

| Name | Type | Description | Required | 
|---|---|---|---|
| specID | string | ID of the spec. | True |
| optionID | string | ID of the option. | True |

## Response Body
	{
	    "ID": "",
	    "IsOpenText": false,
	    "ListOrder": 1,
	    "PriceMarkup": 0,
	    "PriceMarkupType": "NoMarkup",
	    "Value": "",
	    "xp": {}
	}
| Name | Type | Description | Required | 
|---|---|---|---|
| ID | string | ID of the spec option. | False |
| Value | string | Value of the spec option. | True |
| ListOrder | integer | List order of the spec option. | False |
| IsOpenText | boolean | Is open text of the spec option. | False |
| PriceMarkupType | string | Price markup type of the spec option. Possible values: NoMarkup, AmountPerQuantity, AmountTotal, Percentage. | False |
| PriceMarkup | float | Price markup of the spec option. | False |
| xp | object | Container for extended (custom) properties of the spec option. | False |

## `DELETE` `v1/specs/{specID}/options/{optionID}`
Delete a spec option

| Name | Type | Description | Required | 
|---|---|---|---|
| specID | string | ID of the spec. | True |
| optionID | string | ID of the option. | True |

## Response Body