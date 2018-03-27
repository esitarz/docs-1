---
title: Line Items
date: 2018-03-27
category: API Reference
tags: Orders And Fulfillment
slug: Orders-And-Fulfillment-LineItems
---
A Line Item represents a single line on an Order. At a minimum, it
contains a single Product SKU and a quantity. A line item may also
include Spec values, a Cost Center, shipping details, date needed, and
other custom information.

---

## `GET` `v1/orders/{direction}/{orderID}/lineitems/{lineItemID}`
Get a single line item

| Parameters      | Description                    |
|------------------|---------------------------------|


| Parameters      | Description                    |
|------------------|---------------------------------|
| Name            | direction                      |
| Type            | string                         |
| Description     | Direction of the order, from the current user's perspective. Possible values: incoming, outgoing. |
| Required        | True                           |


| Parameters      | Description                    |
|------------------|---------------------------------|
| Name            | orderID                        |
| Type            | string                         |
| Description     | ID of the order.               |
| Required        | True                           |


| Parameters      | Description                    |
|------------------|---------------------------------|
| Name            | lineItemID                     |
| Type            | string                         |
| Description     | ID of the line item.           |
| Required        | True                           |

## Request Body
**Response Status**: `200`

## Response Body
	{
	    "CostCenter": "",
	    "DateAdded": "2018-03-27T16:00:00+00:00",
	    "DateNeeded": "2018-03-27T16:00:00+00:00",
	    "ID": "",
	    "LineTotal": 0,
	    "Product": {
	        "Description": "",
	        "ID": "",
	        "Name": "",
	        "QuantityMultiplier": 0,
	        "ShipHeight": 0,
	        "ShipLength": 0,
	        "ShipWeight": 0,
	        "ShipWidth": 0,
	        "xp": {}
	    },
	    "ProductID": "",
	    "Quantity": 0,
	    "QuantityShipped": 0,
	    "ShipFromAddress": {
	        "AddressName": "",
	        "City": "",
	        "CompanyName": "",
	        "Country": "",
	        "DateCreated": "2018-03-27T16:00:00+00:00",
	        "FirstName": "",
	        "ID": "",
	        "LastName": "",
	        "Phone": "",
	        "State": "",
	        "Street1": "",
	        "Street2": "",
	        "Zip": "",
	        "xp": {}
	    },
	    "ShipFromAddressID": "",
	    "ShippingAccount": "",
	    "ShippingAddress": {
	        "AddressName": "",
	        "City": "",
	        "CompanyName": "",
	        "Country": "",
	        "DateCreated": "2018-03-27T16:00:00+00:00",
	        "FirstName": "",
	        "ID": "",
	        "LastName": "",
	        "Phone": "",
	        "State": "",
	        "Street1": "",
	        "Street2": "",
	        "Zip": "",
	        "xp": {}
	    },
	    "ShippingAddressID": "",
	    "Specs": [
	        {
	            "Name": "",
	            "OptionID": "",
	            "SpecID": "",
	            "Value": ""
	        }
	    ],
	    "UnitPrice": 0,
	    "xp": {}
	}
| Name | Type | Description | Required | 
|---|---|---|---|
| ID | string | ID of the line item. | False |
| ProductID | string | ID of the product. | True |
| Quantity | integer | Quantity of the line item. | True |
| DateAdded | date | Date added of the line item. | False |
| QuantityShipped | integer | Quantity shipped of the line item. | False |
| UnitPrice | float | Unit price of the line item. | False |
| LineTotal | float | Line total of the line item. | False |
| CostCenter | string | Cost center of the line item. | False |
| DateNeeded | date | Date needed of the line item. | False |
| ShippingAccount | string | Shipping account of the line item. | False |
| ShippingAddressID | string | ID of the shipping address. | False |
| ShipFromAddressID | string | ID of the ship from address. | False |
| Product | object | Product of the line item. | False |
| ShippingAddress | object | Shipping address of the line item. | False |
| ShipFromAddress | object | Ship from address of the line item. | False |
| Specs | array | Specs of the line item. | False |
| xp | object | Container for extended (custom) properties of the line item. | False |

## `GET` `v1/orders/{direction}/{orderID}/lineitems`
Get a list of line items

| Parameters      | Description                    |
|------------------|---------------------------------|


| Parameters      | Description                    |
|------------------|---------------------------------|
| Name            | direction                      |
| Type            | string                         |
| Description     | Direction of the order, from the current user's perspective. Possible values: incoming, outgoing. |
| Required        | True                           |


| Parameters      | Description                    |
|------------------|---------------------------------|
| Name            | orderID                        |
| Type            | string                         |
| Description     | ID of the order.               |
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
	            "CostCenter": "",
	            "DateAdded": "2018-03-27T16:00:00+00:00",
	            "DateNeeded": "2018-03-27T16:00:00+00:00",
	            "ID": "",
	            "LineTotal": 0,
	            "Product": {
	                "Description": "",
	                "ID": "",
	                "Name": "",
	                "QuantityMultiplier": 0,
	                "ShipHeight": 0,
	                "ShipLength": 0,
	                "ShipWeight": 0,
	                "ShipWidth": 0,
	                "xp": {}
	            },
	            "ProductID": "",
	            "Quantity": 0,
	            "QuantityShipped": 0,
	            "ShipFromAddress": {
	                "AddressName": "",
	                "City": "",
	                "CompanyName": "",
	                "Country": "",
	                "DateCreated": "2018-03-27T16:00:00+00:00",
	                "FirstName": "",
	                "ID": "",
	                "LastName": "",
	                "Phone": "",
	                "State": "",
	                "Street1": "",
	                "Street2": "",
	                "Zip": "",
	                "xp": {}
	            },
	            "ShipFromAddressID": "",
	            "ShippingAccount": "",
	            "ShippingAddress": {
	                "AddressName": "",
	                "City": "",
	                "CompanyName": "",
	                "Country": "",
	                "DateCreated": "2018-03-27T16:00:00+00:00",
	                "FirstName": "",
	                "ID": "",
	                "LastName": "",
	                "Phone": "",
	                "State": "",
	                "Street1": "",
	                "Street2": "",
	                "Zip": "",
	                "xp": {}
	            },
	            "ShippingAddressID": "",
	            "Specs": [
	                {
	                    "Name": "",
	                    "OptionID": "",
	                    "SpecID": "",
	                    "Value": ""
	                }
	            ],
	            "UnitPrice": 0,
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
| ID | string | ID of the line item. | False |
| ProductID | string | ID of the product. | True |
| Quantity | integer | Quantity of the line item. | True |
| DateAdded | date | Date added of the line item. | False |
| QuantityShipped | integer | Quantity shipped of the line item. | False |
| UnitPrice | float | Unit price of the line item. | False |
| LineTotal | float | Line total of the line item. | False |
| CostCenter | string | Cost center of the line item. | False |
| DateNeeded | date | Date needed of the line item. | False |
| ShippingAccount | string | Shipping account of the line item. | False |
| ShippingAddressID | string | ID of the shipping address. | False |
| ShipFromAddressID | string | ID of the ship from address. | False |
| Product | object | Product of the line item. | False |
| ShippingAddress | object | Shipping address of the line item. | False |
| ShipFromAddress | object | Ship from address of the line item. | False |
| Specs | array | Specs of the line item. | False |
| xp | object | Container for extended (custom) properties of the line item. | False |

## `POST` `v1/orders/{direction}/{orderID}/lineitems`
Create a new line item

| Parameters      | Description                    |
|------------------|---------------------------------|


| Parameters      | Description                    |
|------------------|---------------------------------|
| Name            | direction                      |
| Type            | string                         |
| Description     | Direction of the order, from the current user's perspective. Possible values: incoming, outgoing. |
| Required        | True                           |


| Parameters      | Description                    |
|------------------|---------------------------------|
| Name            | orderID                        |
| Type            | string                         |
| Description     | ID of the order.               |
| Required        | True                           |

## Request Body
	{
	    "CostCenter": "",
	    "DateNeeded": "2018-03-27T16:00:00+00:00",
	    "ID": "",
	    "ProductID": "",
	    "Quantity": 0,
	    "ShipFromAddressID": "",
	    "ShippingAccount": "",
	    "ShippingAddressID": "",
	    "Specs": [
	        {
	            "OptionID": "",
	            "SpecID": "",
	            "Value": ""
	        }
	    ],
	    "UnitPrice": 0,
	    "xp": {}
	}
| Name | Type | Description | Required | 
|---|---|---|---|
| ID | string | ID of the line item. Can only contain characters Aa-Zz, 0-9, -, and _. Searchable: priority level 1. Sortable. | False |
| ProductID | string | ID of the product. Required. Searchable: priority level 2. Sortable. | True |
| Quantity | integer | Quantity of the line item. Required. Must be at least 1. | True |
| UnitPrice | float | Unit price of the line item. Must be between -9999999999999 and 9999999999999. | False |
| CostCenter | string | Cost center of the line item. | False |
| DateNeeded | date | Date needed of the line item. | False |
| ShippingAccount | string | Shipping account of the line item. | False |
| ShippingAddressID | string | ID of the shipping address. | False |
| ShipFromAddressID | string | ID of the ship from address. | False |
| Specs | array | Specs of the line item. | False |
| xp | object | Container for extended (custom) properties of the line item. | False |

**Response Status**: `201`

## Response Body
	{
	    "CostCenter": "",
	    "DateAdded": "2018-03-27T16:00:00+00:00",
	    "DateNeeded": "2018-03-27T16:00:00+00:00",
	    "ID": "",
	    "LineTotal": 0,
	    "Product": {
	        "Description": "",
	        "ID": "",
	        "Name": "",
	        "QuantityMultiplier": 0,
	        "ShipHeight": 0,
	        "ShipLength": 0,
	        "ShipWeight": 0,
	        "ShipWidth": 0,
	        "xp": {}
	    },
	    "ProductID": "",
	    "Quantity": 0,
	    "QuantityShipped": 0,
	    "ShipFromAddress": {
	        "AddressName": "",
	        "City": "",
	        "CompanyName": "",
	        "Country": "",
	        "DateCreated": "2018-03-27T16:00:00+00:00",
	        "FirstName": "",
	        "ID": "",
	        "LastName": "",
	        "Phone": "",
	        "State": "",
	        "Street1": "",
	        "Street2": "",
	        "Zip": "",
	        "xp": {}
	    },
	    "ShipFromAddressID": "",
	    "ShippingAccount": "",
	    "ShippingAddress": {
	        "AddressName": "",
	        "City": "",
	        "CompanyName": "",
	        "Country": "",
	        "DateCreated": "2018-03-27T16:00:00+00:00",
	        "FirstName": "",
	        "ID": "",
	        "LastName": "",
	        "Phone": "",
	        "State": "",
	        "Street1": "",
	        "Street2": "",
	        "Zip": "",
	        "xp": {}
	    },
	    "ShippingAddressID": "",
	    "Specs": [
	        {
	            "Name": "",
	            "OptionID": "",
	            "SpecID": "",
	            "Value": ""
	        }
	    ],
	    "UnitPrice": 0,
	    "xp": {}
	}
| Name | Type | Description | Required | 
|---|---|---|---|
| ID | string | ID of the line item. | False |
| ProductID | string | ID of the product. | True |
| Quantity | integer | Quantity of the line item. | True |
| DateAdded | date | Date added of the line item. | False |
| QuantityShipped | integer | Quantity shipped of the line item. | False |
| UnitPrice | float | Unit price of the line item. | False |
| LineTotal | float | Line total of the line item. | False |
| CostCenter | string | Cost center of the line item. | False |
| DateNeeded | date | Date needed of the line item. | False |
| ShippingAccount | string | Shipping account of the line item. | False |
| ShippingAddressID | string | ID of the shipping address. | False |
| ShipFromAddressID | string | ID of the ship from address. | False |
| Product | object | Product of the line item. | False |
| ShippingAddress | object | Shipping address of the line item. | False |
| ShipFromAddress | object | Ship from address of the line item. | False |
| Specs | array | Specs of the line item. | False |
| xp | object | Container for extended (custom) properties of the line item. | False |

## `PUT` `v1/orders/{direction}/{orderID}/lineitems/{lineItemID}`
Create or update a line item

| Parameters      | Description                    |
|------------------|---------------------------------|


| Parameters      | Description                    |
|------------------|---------------------------------|
| Name            | direction                      |
| Type            | string                         |
| Description     | Direction of the order, from the current user's perspective. Possible values: incoming, outgoing. |
| Required        | True                           |


| Parameters      | Description                    |
|------------------|---------------------------------|
| Name            | orderID                        |
| Type            | string                         |
| Description     | ID of the order.               |
| Required        | True                           |


| Parameters      | Description                    |
|------------------|---------------------------------|
| Name            | lineItemID                     |
| Type            | string                         |
| Description     | ID of the line item.           |
| Required        | True                           |

## Request Body
	{
	    "CostCenter": "",
	    "DateNeeded": "2018-03-27T16:00:00+00:00",
	    "ID": "",
	    "ProductID": "",
	    "Quantity": 0,
	    "ShipFromAddressID": "",
	    "ShippingAccount": "",
	    "ShippingAddressID": "",
	    "Specs": [
	        {
	            "OptionID": "",
	            "SpecID": "",
	            "Value": ""
	        }
	    ],
	    "UnitPrice": 0,
	    "xp": {}
	}
| Name | Type | Description | Required | 
|---|---|---|---|
| ID | string | ID of the line item. Can only contain characters Aa-Zz, 0-9, -, and _. Searchable: priority level 1. Sortable. | False |
| ProductID | string | ID of the product. Required. Searchable: priority level 2. Sortable. | True |
| Quantity | integer | Quantity of the line item. Required. Must be at least 1. | True |
| UnitPrice | float | Unit price of the line item. Must be between -9999999999999 and 9999999999999. | False |
| CostCenter | string | Cost center of the line item. | False |
| DateNeeded | date | Date needed of the line item. | False |
| ShippingAccount | string | Shipping account of the line item. | False |
| ShippingAddressID | string | ID of the shipping address. | False |
| ShipFromAddressID | string | ID of the ship from address. | False |
| Specs | array | Specs of the line item. | False |
| xp | object | Container for extended (custom) properties of the line item. | False |

**Response Status**: `200`

## Response Body
	{
	    "CostCenter": "",
	    "DateAdded": "2018-03-27T16:00:00+00:00",
	    "DateNeeded": "2018-03-27T16:00:00+00:00",
	    "ID": "",
	    "LineTotal": 0,
	    "Product": {
	        "Description": "",
	        "ID": "",
	        "Name": "",
	        "QuantityMultiplier": 0,
	        "ShipHeight": 0,
	        "ShipLength": 0,
	        "ShipWeight": 0,
	        "ShipWidth": 0,
	        "xp": {}
	    },
	    "ProductID": "",
	    "Quantity": 0,
	    "QuantityShipped": 0,
	    "ShipFromAddress": {
	        "AddressName": "",
	        "City": "",
	        "CompanyName": "",
	        "Country": "",
	        "DateCreated": "2018-03-27T16:00:00+00:00",
	        "FirstName": "",
	        "ID": "",
	        "LastName": "",
	        "Phone": "",
	        "State": "",
	        "Street1": "",
	        "Street2": "",
	        "Zip": "",
	        "xp": {}
	    },
	    "ShipFromAddressID": "",
	    "ShippingAccount": "",
	    "ShippingAddress": {
	        "AddressName": "",
	        "City": "",
	        "CompanyName": "",
	        "Country": "",
	        "DateCreated": "2018-03-27T16:00:00+00:00",
	        "FirstName": "",
	        "ID": "",
	        "LastName": "",
	        "Phone": "",
	        "State": "",
	        "Street1": "",
	        "Street2": "",
	        "Zip": "",
	        "xp": {}
	    },
	    "ShippingAddressID": "",
	    "Specs": [
	        {
	            "Name": "",
	            "OptionID": "",
	            "SpecID": "",
	            "Value": ""
	        }
	    ],
	    "UnitPrice": 0,
	    "xp": {}
	}
| Name | Type | Description | Required | 
|---|---|---|---|
| ID | string | ID of the line item. | False |
| ProductID | string | ID of the product. | True |
| Quantity | integer | Quantity of the line item. | True |
| DateAdded | date | Date added of the line item. | False |
| QuantityShipped | integer | Quantity shipped of the line item. | False |
| UnitPrice | float | Unit price of the line item. | False |
| LineTotal | float | Line total of the line item. | False |
| CostCenter | string | Cost center of the line item. | False |
| DateNeeded | date | Date needed of the line item. | False |
| ShippingAccount | string | Shipping account of the line item. | False |
| ShippingAddressID | string | ID of the shipping address. | False |
| ShipFromAddressID | string | ID of the ship from address. | False |
| Product | object | Product of the line item. | False |
| ShippingAddress | object | Shipping address of the line item. | False |
| ShipFromAddress | object | Ship from address of the line item. | False |
| Specs | array | Specs of the line item. | False |
| xp | object | Container for extended (custom) properties of the line item. | False |

## `DELETE` `v1/orders/{direction}/{orderID}/lineitems/{lineItemID}`
Delete a line item

| Parameters      | Description                    |
|------------------|---------------------------------|


| Parameters      | Description                    |
|------------------|---------------------------------|
| Name            | direction                      |
| Type            | string                         |
| Description     | Direction of the order, from the current user's perspective. Possible values: incoming, outgoing. |
| Required        | True                           |


| Parameters      | Description                    |
|------------------|---------------------------------|
| Name            | orderID                        |
| Type            | string                         |
| Description     | ID of the order.               |
| Required        | True                           |


| Parameters      | Description                    |
|------------------|---------------------------------|
| Name            | lineItemID                     |
| Type            | string                         |
| Description     | ID of the line item.           |
| Required        | True                           |

## Request Body
**Response Status**: `204`

## Response Body
## `PATCH` `v1/orders/{direction}/{orderID}/lineitems/{lineItemID}`
Partially update a line item

| Parameters      | Description                    |
|------------------|---------------------------------|


| Parameters      | Description                    |
|------------------|---------------------------------|
| Name            | direction                      |
| Type            | string                         |
| Description     | Direction of the order, from the current user's perspective. Possible values: incoming, outgoing. |
| Required        | True                           |


| Parameters      | Description                    |
|------------------|---------------------------------|
| Name            | orderID                        |
| Type            | string                         |
| Description     | ID of the order.               |
| Required        | True                           |


| Parameters      | Description                    |
|------------------|---------------------------------|
| Name            | lineItemID                     |
| Type            | string                         |
| Description     | ID of the line item.           |
| Required        | True                           |

## Request Body
	{
	    "CostCenter": "",
	    "DateNeeded": "2018-03-27T16:00:00+00:00",
	    "ID": "",
	    "ProductID": "",
	    "Quantity": 0,
	    "ShipFromAddressID": "",
	    "ShippingAccount": "",
	    "ShippingAddressID": "",
	    "Specs": [
	        {
	            "OptionID": "",
	            "SpecID": "",
	            "Value": ""
	        }
	    ],
	    "UnitPrice": 0,
	    "xp": {}
	}
| Name | Type | Description | Required | 
|---|---|---|---|
| ID | string | ID of the line item. Can only contain characters Aa-Zz, 0-9, -, and _. Searchable: priority level 1. Sortable. | False |
| ProductID | string | ID of the product. Required. Searchable: priority level 2. Sortable. | True |
| Quantity | integer | Quantity of the line item. Required. Must be at least 1. | True |
| UnitPrice | float | Unit price of the line item. Must be between -9999999999999 and 9999999999999. | False |
| CostCenter | string | Cost center of the line item. | False |
| DateNeeded | date | Date needed of the line item. | False |
| ShippingAccount | string | Shipping account of the line item. | False |
| ShippingAddressID | string | ID of the shipping address. | False |
| ShipFromAddressID | string | ID of the ship from address. | False |
| Specs | array | Specs of the line item. | False |
| xp | object | Container for extended (custom) properties of the line item. | False |

**Response Status**: `200`

## Response Body
	{
	    "CostCenter": "",
	    "DateAdded": "2018-03-27T16:00:00+00:00",
	    "DateNeeded": "2018-03-27T16:00:00+00:00",
	    "ID": "",
	    "LineTotal": 0,
	    "Product": {
	        "Description": "",
	        "ID": "",
	        "Name": "",
	        "QuantityMultiplier": 0,
	        "ShipHeight": 0,
	        "ShipLength": 0,
	        "ShipWeight": 0,
	        "ShipWidth": 0,
	        "xp": {}
	    },
	    "ProductID": "",
	    "Quantity": 0,
	    "QuantityShipped": 0,
	    "ShipFromAddress": {
	        "AddressName": "",
	        "City": "",
	        "CompanyName": "",
	        "Country": "",
	        "DateCreated": "2018-03-27T16:00:00+00:00",
	        "FirstName": "",
	        "ID": "",
	        "LastName": "",
	        "Phone": "",
	        "State": "",
	        "Street1": "",
	        "Street2": "",
	        "Zip": "",
	        "xp": {}
	    },
	    "ShipFromAddressID": "",
	    "ShippingAccount": "",
	    "ShippingAddress": {
	        "AddressName": "",
	        "City": "",
	        "CompanyName": "",
	        "Country": "",
	        "DateCreated": "2018-03-27T16:00:00+00:00",
	        "FirstName": "",
	        "ID": "",
	        "LastName": "",
	        "Phone": "",
	        "State": "",
	        "Street1": "",
	        "Street2": "",
	        "Zip": "",
	        "xp": {}
	    },
	    "ShippingAddressID": "",
	    "Specs": [
	        {
	            "Name": "",
	            "OptionID": "",
	            "SpecID": "",
	            "Value": ""
	        }
	    ],
	    "UnitPrice": 0,
	    "xp": {}
	}
| Name | Type | Description | Required | 
|---|---|---|---|
| ID | string | ID of the line item. | False |
| ProductID | string | ID of the product. | True |
| Quantity | integer | Quantity of the line item. | True |
| DateAdded | date | Date added of the line item. | False |
| QuantityShipped | integer | Quantity shipped of the line item. | False |
| UnitPrice | float | Unit price of the line item. | False |
| LineTotal | float | Line total of the line item. | False |
| CostCenter | string | Cost center of the line item. | False |
| DateNeeded | date | Date needed of the line item. | False |
| ShippingAccount | string | Shipping account of the line item. | False |
| ShippingAddressID | string | ID of the shipping address. | False |
| ShipFromAddressID | string | ID of the ship from address. | False |
| Product | object | Product of the line item. | False |
| ShippingAddress | object | Shipping address of the line item. | False |
| ShipFromAddress | object | Ship from address of the line item. | False |
| Specs | array | Specs of the line item. | False |
| xp | object | Container for extended (custom) properties of the line item. | False |

## `PUT` `v1/orders/{direction}/{orderID}/lineitems/{lineItemID}/shipto`
Set a shipping address

| Parameters      | Description                    |
|------------------|---------------------------------|


| Parameters      | Description                    |
|------------------|---------------------------------|
| Name            | direction                      |
| Type            | string                         |
| Description     | Direction of the order, from the current user's perspective. Possible values: incoming, outgoing. |
| Required        | True                           |


| Parameters      | Description                    |
|------------------|---------------------------------|
| Name            | orderID                        |
| Type            | string                         |
| Description     | ID of the order.               |
| Required        | True                           |


| Parameters      | Description                    |
|------------------|---------------------------------|
| Name            | lineItemID                     |
| Type            | string                         |
| Description     | ID of the line item.           |
| Required        | True                           |

## Request Body
	{
	    "AddressName": "",
	    "City": "",
	    "CompanyName": "",
	    "Country": "",
	    "FirstName": "",
	    "ID": "",
	    "LastName": "",
	    "Phone": "",
	    "State": "",
	    "Street1": "",
	    "Street2": "",
	    "Zip": "",
	    "xp": {}
	}
| Name | Type | Description | Required | 
|---|---|---|---|
| ID | string | ID of the address. Can only contain characters Aa-Zz, 0-9, -, and _. Searchable: priority level 1. Sortable: priority level 2. | False |
| CompanyName | string | Company name of the address. Max length 100 characters. Sortable. | False |
| FirstName | string | First name of the address. Max length 100 characters. Searchable: priority level 7. Sortable. | False |
| LastName | string | Last name of the address. Max length 100 characters. Searchable: priority level 6. Sortable. | False |
| Street1 | string | Street 1 of the address. Required. Max length 100 characters. Searchable: priority level 4. Sortable. | True |
| Street2 | string | Street 2 of the address. Max length 100 characters. Searchable: priority level 5. Sortable. | False |
| City | string | City of the address. Required. Max length 100 characters. Searchable: priority level 3. Sortable. | True |
| State | string | State of the address. Required. Max length 100 characters. Searchable: priority level 7. Sortable. | True |
| Zip | string | Zip of the address. Required. Max length 100 characters. Searchable: priority level 6. Sortable. | True |
| Country | string | Country of the address. Required. Max length 2 characters. Sortable. | True |
| Phone | string | Phone of the address. Max length 100 characters. Sortable. | False |
| AddressName | string | Address name of the address. Max length 100 characters. Searchable: priority level 2. Sortable: priority level 1. | False |
| xp | object | Container for extended (custom) properties of the address. | False |

**Response Status**: `200`

## Response Body
	{
	    "CostCenter": "",
	    "DateAdded": "2018-03-27T16:00:00+00:00",
	    "DateNeeded": "2018-03-27T16:00:00+00:00",
	    "ID": "",
	    "LineTotal": 0,
	    "Product": {
	        "Description": "",
	        "ID": "",
	        "Name": "",
	        "QuantityMultiplier": 0,
	        "ShipHeight": 0,
	        "ShipLength": 0,
	        "ShipWeight": 0,
	        "ShipWidth": 0,
	        "xp": {}
	    },
	    "ProductID": "",
	    "Quantity": 0,
	    "QuantityShipped": 0,
	    "ShipFromAddress": {
	        "AddressName": "",
	        "City": "",
	        "CompanyName": "",
	        "Country": "",
	        "DateCreated": "2018-03-27T16:00:00+00:00",
	        "FirstName": "",
	        "ID": "",
	        "LastName": "",
	        "Phone": "",
	        "State": "",
	        "Street1": "",
	        "Street2": "",
	        "Zip": "",
	        "xp": {}
	    },
	    "ShipFromAddressID": "",
	    "ShippingAccount": "",
	    "ShippingAddress": {
	        "AddressName": "",
	        "City": "",
	        "CompanyName": "",
	        "Country": "",
	        "DateCreated": "2018-03-27T16:00:00+00:00",
	        "FirstName": "",
	        "ID": "",
	        "LastName": "",
	        "Phone": "",
	        "State": "",
	        "Street1": "",
	        "Street2": "",
	        "Zip": "",
	        "xp": {}
	    },
	    "ShippingAddressID": "",
	    "Specs": [
	        {
	            "Name": "",
	            "OptionID": "",
	            "SpecID": "",
	            "Value": ""
	        }
	    ],
	    "UnitPrice": 0,
	    "xp": {}
	}
| Name | Type | Description | Required | 
|---|---|---|---|
| ID | string | ID of the line item. | False |
| ProductID | string | ID of the product. | True |
| Quantity | integer | Quantity of the line item. | True |
| DateAdded | date | Date added of the line item. | False |
| QuantityShipped | integer | Quantity shipped of the line item. | False |
| UnitPrice | float | Unit price of the line item. | False |
| LineTotal | float | Line total of the line item. | False |
| CostCenter | string | Cost center of the line item. | False |
| DateNeeded | date | Date needed of the line item. | False |
| ShippingAccount | string | Shipping account of the line item. | False |
| ShippingAddressID | string | ID of the shipping address. | False |
| ShipFromAddressID | string | ID of the ship from address. | False |
| Product | object | Product of the line item. | False |
| ShippingAddress | object | Shipping address of the line item. | False |
| ShipFromAddress | object | Ship from address of the line item. | False |
| Specs | array | Specs of the line item. | False |
| xp | object | Container for extended (custom) properties of the line item. | False |

## `PATCH` `v1/orders/{direction}/{orderID}/lineitems/{lineItemID}/shipto`
Partially update a line item shipping address

| Parameters      | Description                    |
|------------------|---------------------------------|


| Parameters      | Description                    |
|------------------|---------------------------------|
| Name            | direction                      |
| Type            | string                         |
| Description     | Direction of the order, from the current user's perspective. Possible values: incoming, outgoing. |
| Required        | True                           |


| Parameters      | Description                    |
|------------------|---------------------------------|
| Name            | orderID                        |
| Type            | string                         |
| Description     | ID of the order.               |
| Required        | True                           |


| Parameters      | Description                    |
|------------------|---------------------------------|
| Name            | lineItemID                     |
| Type            | string                         |
| Description     | ID of the line item.           |
| Required        | True                           |

## Request Body
	{
	    "AddressName": "",
	    "City": "",
	    "CompanyName": "",
	    "Country": "",
	    "FirstName": "",
	    "ID": "",
	    "LastName": "",
	    "Phone": "",
	    "State": "",
	    "Street1": "",
	    "Street2": "",
	    "Zip": "",
	    "xp": {}
	}
| Name | Type | Description | Required | 
|---|---|---|---|
| ID | string | ID of the address. Can only contain characters Aa-Zz, 0-9, -, and _. Searchable: priority level 1. Sortable: priority level 2. | False |
| CompanyName | string | Company name of the address. Max length 100 characters. Sortable. | False |
| FirstName | string | First name of the address. Max length 100 characters. Searchable: priority level 7. Sortable. | False |
| LastName | string | Last name of the address. Max length 100 characters. Searchable: priority level 6. Sortable. | False |
| Street1 | string | Street 1 of the address. Required. Max length 100 characters. Searchable: priority level 4. Sortable. | True |
| Street2 | string | Street 2 of the address. Max length 100 characters. Searchable: priority level 5. Sortable. | False |
| City | string | City of the address. Required. Max length 100 characters. Searchable: priority level 3. Sortable. | True |
| State | string | State of the address. Required. Max length 100 characters. Searchable: priority level 7. Sortable. | True |
| Zip | string | Zip of the address. Required. Max length 100 characters. Searchable: priority level 6. Sortable. | True |
| Country | string | Country of the address. Required. Max length 2 characters. Sortable. | True |
| Phone | string | Phone of the address. Max length 100 characters. Sortable. | False |
| AddressName | string | Address name of the address. Max length 100 characters. Searchable: priority level 2. Sortable: priority level 1. | False |
| xp | object | Container for extended (custom) properties of the address. | False |

**Response Status**: `200`

## Response Body
	{
	    "CostCenter": "",
	    "DateAdded": "2018-03-27T16:00:00+00:00",
	    "DateNeeded": "2018-03-27T16:00:00+00:00",
	    "ID": "",
	    "LineTotal": 0,
	    "Product": {
	        "Description": "",
	        "ID": "",
	        "Name": "",
	        "QuantityMultiplier": 0,
	        "ShipHeight": 0,
	        "ShipLength": 0,
	        "ShipWeight": 0,
	        "ShipWidth": 0,
	        "xp": {}
	    },
	    "ProductID": "",
	    "Quantity": 0,
	    "QuantityShipped": 0,
	    "ShipFromAddress": {
	        "AddressName": "",
	        "City": "",
	        "CompanyName": "",
	        "Country": "",
	        "DateCreated": "2018-03-27T16:00:00+00:00",
	        "FirstName": "",
	        "ID": "",
	        "LastName": "",
	        "Phone": "",
	        "State": "",
	        "Street1": "",
	        "Street2": "",
	        "Zip": "",
	        "xp": {}
	    },
	    "ShipFromAddressID": "",
	    "ShippingAccount": "",
	    "ShippingAddress": {
	        "AddressName": "",
	        "City": "",
	        "CompanyName": "",
	        "Country": "",
	        "DateCreated": "2018-03-27T16:00:00+00:00",
	        "FirstName": "",
	        "ID": "",
	        "LastName": "",
	        "Phone": "",
	        "State": "",
	        "Street1": "",
	        "Street2": "",
	        "Zip": "",
	        "xp": {}
	    },
	    "ShippingAddressID": "",
	    "Specs": [
	        {
	            "Name": "",
	            "OptionID": "",
	            "SpecID": "",
	            "Value": ""
	        }
	    ],
	    "UnitPrice": 0,
	    "xp": {}
	}
| Name | Type | Description | Required | 
|---|---|---|---|
| ID | string | ID of the line item. | False |
| ProductID | string | ID of the product. | True |
| Quantity | integer | Quantity of the line item. | True |
| DateAdded | date | Date added of the line item. | False |
| QuantityShipped | integer | Quantity shipped of the line item. | False |
| UnitPrice | float | Unit price of the line item. | False |
| LineTotal | float | Line total of the line item. | False |
| CostCenter | string | Cost center of the line item. | False |
| DateNeeded | date | Date needed of the line item. | False |
| ShippingAccount | string | Shipping account of the line item. | False |
| ShippingAddressID | string | ID of the shipping address. | False |
| ShipFromAddressID | string | ID of the ship from address. | False |
| Product | object | Product of the line item. | False |
| ShippingAddress | object | Shipping address of the line item. | False |
| ShipFromAddress | object | Ship from address of the line item. | False |
| Specs | array | Specs of the line item. | False |
| xp | object | Container for extended (custom) properties of the line item. | False |
