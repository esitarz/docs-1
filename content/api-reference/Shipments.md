---
title: Shipments
date: 2018-03-27
category: API Reference
tags: Orders And Fulfillment
slug: Orders-And-Fulfillment-Shipments
---
A Shipment is a grouping of one or more Line Items from one or more
Orders that is physically packaged and delivered to the Buyer as a
single unit. It is typically created by the Seller after the Order is
submitted as part of the fulfillment process.

---

## `GET` `v1/shipments/{shipmentID}`
Get a single shipment

| Parameters      | Description                    |
|------------------|---------------------------------|


| Parameters      | Description                    |
|------------------|---------------------------------|
| Name            | shipmentID                     |
| Type            | string                         |
| Description     | ID of the shipment.            |
| Required        | True                           |

## Request Body
**Response Status**: `200`

## Response Body
	{
	    "Account": "",
	    "BuyerID": "",
	    "Cost": 0,
	    "DateDelivered": "2018-03-27T16:00:00+00:00",
	    "DateShipped": "2018-03-27T16:00:00+00:00",
	    "FromAddress": {
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
	    "FromAddressID": "",
	    "ID": "",
	    "Shipper": "",
	    "ToAddress": {
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
	    "ToAddressID": "",
	    "TrackingNumber": "",
	    "xp": {}
	}
| Name | Type | Description | Required | 
|---|---|---|---|
| ID | string | ID of the shipment. | False |
| BuyerID | string | ID of the buyer. | False |
| Shipper | string | Shipper of the shipment. | False |
| DateShipped | date | Date shipped of the shipment. | False |
| DateDelivered | date | Date delivered of the shipment. | False |
| TrackingNumber | string | Tracking number of the shipment. | False |
| Cost | float | Cost of the shipment. | False |
| xp | object | Container for extended (custom) properties of the shipment. | False |
| Account | string | Account of the shipment. | False |
| FromAddressID | string | ID of the from address. | False |
| ToAddressID | string | ID of the to address. | False |
| FromAddress | object | From address of the shipment. | False |
| ToAddress | object | To address of the shipment. | False |

## `GET` `v1/shipments`
Get a list of shipments

| Parameters      | Description                    |
|------------------|---------------------------------|


| Parameters      | Description                    |
|------------------|---------------------------------|
| Name            | orderID                        |
| Type            | string                         |
| Description     | ID of the order.               |
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
	            "Account": "",
	            "BuyerID": "",
	            "Cost": 0,
	            "DateDelivered": "2018-03-27T16:00:00+00:00",
	            "DateShipped": "2018-03-27T16:00:00+00:00",
	            "FromAddress": {
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
	            "FromAddressID": "",
	            "ID": "",
	            "Shipper": "",
	            "ToAddress": {
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
	            "ToAddressID": "",
	            "TrackingNumber": "",
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
| ID | string | ID of the shipment. | False |
| BuyerID | string | ID of the buyer. | False |
| Shipper | string | Shipper of the shipment. | False |
| DateShipped | date | Date shipped of the shipment. | False |
| DateDelivered | date | Date delivered of the shipment. | False |
| TrackingNumber | string | Tracking number of the shipment. | False |
| Cost | float | Cost of the shipment. | False |
| xp | object | Container for extended (custom) properties of the shipment. | False |
| Account | string | Account of the shipment. | False |
| FromAddressID | string | ID of the from address. | False |
| ToAddressID | string | ID of the to address. | False |
| FromAddress | object | From address of the shipment. | False |
| ToAddress | object | To address of the shipment. | False |

## `POST` `v1/shipments`
Create a new shipment
## Request Body
	{
	    "Account": "",
	    "BuyerID": "",
	    "Cost": 0,
	    "DateDelivered": "2018-03-27T16:00:00+00:00",
	    "DateShipped": "2018-03-27T16:00:00+00:00",
	    "FromAddressID": "",
	    "ID": "",
	    "Shipper": "",
	    "ToAddressID": "",
	    "TrackingNumber": "",
	    "xp": {}
	}
| Name | Type | Description | Required | 
|---|---|---|---|
| ID | string | ID of the shipment. Can only contain characters Aa-Zz, 0-9, -, and _. Searchable: priority level 1. Sortable. | False |
| BuyerID | string | ID of the buyer. Searchable: priority level 1. Sortable. | False |
| Shipper | string | Shipper of the shipment. Searchable: priority level 2. Sortable. | False |
| DateShipped | date | Date shipped of the shipment. Searchable: priority level 3. Sortable: priority level 1. | False |
| DateDelivered | date | Date delivered of the shipment. Searchable: priority level 4. Sortable. | False |
| TrackingNumber | string | Tracking number of the shipment. Max length 3000 characters. Searchable: priority level 4. | False |
| Cost | float | Cost of the shipment. Sortable. | False |
| xp | object | Container for extended (custom) properties of the shipment. | False |
| Account | string | Account of the shipment. | False |
| FromAddressID | string | ID of the from address. | False |
| ToAddressID | string | ID of the to address. | False |

**Response Status**: `201`

## Response Body
	{
	    "Account": "",
	    "BuyerID": "",
	    "Cost": 0,
	    "DateDelivered": "2018-03-27T16:00:00+00:00",
	    "DateShipped": "2018-03-27T16:00:00+00:00",
	    "FromAddress": {
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
	    "FromAddressID": "",
	    "ID": "",
	    "Shipper": "",
	    "ToAddress": {
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
	    "ToAddressID": "",
	    "TrackingNumber": "",
	    "xp": {}
	}
| Name | Type | Description | Required | 
|---|---|---|---|
| ID | string | ID of the shipment. | False |
| BuyerID | string | ID of the buyer. | False |
| Shipper | string | Shipper of the shipment. | False |
| DateShipped | date | Date shipped of the shipment. | False |
| DateDelivered | date | Date delivered of the shipment. | False |
| TrackingNumber | string | Tracking number of the shipment. | False |
| Cost | float | Cost of the shipment. | False |
| xp | object | Container for extended (custom) properties of the shipment. | False |
| Account | string | Account of the shipment. | False |
| FromAddressID | string | ID of the from address. | False |
| ToAddressID | string | ID of the to address. | False |
| FromAddress | object | From address of the shipment. | False |
| ToAddress | object | To address of the shipment. | False |

## `PUT` `v1/shipments/{shipmentID}`
Create or update a shipment

| Parameters      | Description                    |
|------------------|---------------------------------|


| Parameters      | Description                    |
|------------------|---------------------------------|
| Name            | shipmentID                     |
| Type            | string                         |
| Description     | ID of the shipment.            |
| Required        | True                           |

## Request Body
	{
	    "Account": "",
	    "BuyerID": "",
	    "Cost": 0,
	    "DateDelivered": "2018-03-27T16:00:00+00:00",
	    "DateShipped": "2018-03-27T16:00:00+00:00",
	    "FromAddressID": "",
	    "ID": "",
	    "Shipper": "",
	    "ToAddressID": "",
	    "TrackingNumber": "",
	    "xp": {}
	}
| Name | Type | Description | Required | 
|---|---|---|---|
| ID | string | ID of the shipment. Can only contain characters Aa-Zz, 0-9, -, and _. Searchable: priority level 1. Sortable. | False |
| BuyerID | string | ID of the buyer. Searchable: priority level 1. Sortable. | False |
| Shipper | string | Shipper of the shipment. Searchable: priority level 2. Sortable. | False |
| DateShipped | date | Date shipped of the shipment. Searchable: priority level 3. Sortable: priority level 1. | False |
| DateDelivered | date | Date delivered of the shipment. Searchable: priority level 4. Sortable. | False |
| TrackingNumber | string | Tracking number of the shipment. Max length 3000 characters. Searchable: priority level 4. | False |
| Cost | float | Cost of the shipment. Sortable. | False |
| xp | object | Container for extended (custom) properties of the shipment. | False |
| Account | string | Account of the shipment. | False |
| FromAddressID | string | ID of the from address. | False |
| ToAddressID | string | ID of the to address. | False |

**Response Status**: `200`

## Response Body
	{
	    "Account": "",
	    "BuyerID": "",
	    "Cost": 0,
	    "DateDelivered": "2018-03-27T16:00:00+00:00",
	    "DateShipped": "2018-03-27T16:00:00+00:00",
	    "FromAddress": {
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
	    "FromAddressID": "",
	    "ID": "",
	    "Shipper": "",
	    "ToAddress": {
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
	    "ToAddressID": "",
	    "TrackingNumber": "",
	    "xp": {}
	}
| Name | Type | Description | Required | 
|---|---|---|---|
| ID | string | ID of the shipment. | False |
| BuyerID | string | ID of the buyer. | False |
| Shipper | string | Shipper of the shipment. | False |
| DateShipped | date | Date shipped of the shipment. | False |
| DateDelivered | date | Date delivered of the shipment. | False |
| TrackingNumber | string | Tracking number of the shipment. | False |
| Cost | float | Cost of the shipment. | False |
| xp | object | Container for extended (custom) properties of the shipment. | False |
| Account | string | Account of the shipment. | False |
| FromAddressID | string | ID of the from address. | False |
| ToAddressID | string | ID of the to address. | False |
| FromAddress | object | From address of the shipment. | False |
| ToAddress | object | To address of the shipment. | False |

## `DELETE` `v1/shipments/{shipmentID}`
Delete a shipment

| Parameters      | Description                    |
|------------------|---------------------------------|


| Parameters      | Description                    |
|------------------|---------------------------------|
| Name            | shipmentID                     |
| Type            | string                         |
| Description     | ID of the shipment.            |
| Required        | True                           |

## Request Body
**Response Status**: `204`

## Response Body
## `PATCH` `v1/shipments/{shipmentID}`
Partially update a shipment

| Parameters      | Description                    |
|------------------|---------------------------------|


| Parameters      | Description                    |
|------------------|---------------------------------|
| Name            | shipmentID                     |
| Type            | string                         |
| Description     | ID of the shipment.            |
| Required        | True                           |

## Request Body
	{
	    "Account": "",
	    "BuyerID": "",
	    "Cost": 0,
	    "DateDelivered": "2018-03-27T16:00:00+00:00",
	    "DateShipped": "2018-03-27T16:00:00+00:00",
	    "FromAddressID": "",
	    "ID": "",
	    "Shipper": "",
	    "ToAddressID": "",
	    "TrackingNumber": "",
	    "xp": {}
	}
| Name | Type | Description | Required | 
|---|---|---|---|
| ID | string | ID of the shipment. Can only contain characters Aa-Zz, 0-9, -, and _. Searchable: priority level 1. Sortable. | False |
| BuyerID | string | ID of the buyer. Searchable: priority level 1. Sortable. | False |
| Shipper | string | Shipper of the shipment. Searchable: priority level 2. Sortable. | False |
| DateShipped | date | Date shipped of the shipment. Searchable: priority level 3. Sortable: priority level 1. | False |
| DateDelivered | date | Date delivered of the shipment. Searchable: priority level 4. Sortable. | False |
| TrackingNumber | string | Tracking number of the shipment. Max length 3000 characters. Searchable: priority level 4. | False |
| Cost | float | Cost of the shipment. Sortable. | False |
| xp | object | Container for extended (custom) properties of the shipment. | False |
| Account | string | Account of the shipment. | False |
| FromAddressID | string | ID of the from address. | False |
| ToAddressID | string | ID of the to address. | False |

**Response Status**: `200`

## Response Body
	{
	    "Account": "",
	    "BuyerID": "",
	    "Cost": 0,
	    "DateDelivered": "2018-03-27T16:00:00+00:00",
	    "DateShipped": "2018-03-27T16:00:00+00:00",
	    "FromAddress": {
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
	    "FromAddressID": "",
	    "ID": "",
	    "Shipper": "",
	    "ToAddress": {
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
	    "ToAddressID": "",
	    "TrackingNumber": "",
	    "xp": {}
	}
| Name | Type | Description | Required | 
|---|---|---|---|
| ID | string | ID of the shipment. | False |
| BuyerID | string | ID of the buyer. | False |
| Shipper | string | Shipper of the shipment. | False |
| DateShipped | date | Date shipped of the shipment. | False |
| DateDelivered | date | Date delivered of the shipment. | False |
| TrackingNumber | string | Tracking number of the shipment. | False |
| Cost | float | Cost of the shipment. | False |
| xp | object | Container for extended (custom) properties of the shipment. | False |
| Account | string | Account of the shipment. | False |
| FromAddressID | string | ID of the from address. | False |
| ToAddressID | string | ID of the to address. | False |
| FromAddress | object | From address of the shipment. | False |
| ToAddress | object | To address of the shipment. | False |

## `GET` `v1/shipments/{shipmentID}/items`
Get a list of shipment items

| Parameters      | Description                    |
|------------------|---------------------------------|


| Parameters      | Description                    |
|------------------|---------------------------------|
| Name            | shipmentID                     |
| Type            | string                         |
| Description     | ID of the shipment.            |
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
	            "DateNeeded": "2018-03-27T16:00:00+00:00",
	            "LineItemID": "",
	            "OrderID": "",
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
	            "QuantityShipped": 0,
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
| OrderID | string | ID of the order. | True |
| LineItemID | string | ID of the line item. | True |
| QuantityShipped | integer | Quantity shipped of the shipment item. | True |
| UnitPrice | float | Unit price of the shipment item. | False |
| CostCenter | string | Cost center of the shipment item. | False |
| DateNeeded | date | Date needed of the shipment item. | False |
| Product | object | Product of the shipment item. | False |
| Specs | array | Specs of the shipment item. | False |
| xp | object | Container for extended (custom) properties of the shipment item. | False |

## `GET` `v1/shipments/{shipmentID}/items/{orderID}/{lineItemID}`
Get a single shipment item

| Parameters      | Description                    |
|------------------|---------------------------------|


| Parameters      | Description                    |
|------------------|---------------------------------|
| Name            | shipmentID                     |
| Type            | string                         |
| Description     | ID of the shipment.            |
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
	    "DateNeeded": "2018-03-27T16:00:00+00:00",
	    "LineItemID": "",
	    "OrderID": "",
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
	    "QuantityShipped": 0,
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
| OrderID | string | ID of the order. | True |
| LineItemID | string | ID of the line item. | True |
| QuantityShipped | integer | Quantity shipped of the shipment item. | True |
| UnitPrice | float | Unit price of the shipment item. | False |
| CostCenter | string | Cost center of the shipment item. | False |
| DateNeeded | date | Date needed of the shipment item. | False |
| Product | object | Product of the shipment item. | False |
| Specs | array | Specs of the shipment item. | False |
| xp | object | Container for extended (custom) properties of the shipment item. | False |

## `POST` `v1/shipments/{shipmentID}/items`
Save a shipment item

| Parameters      | Description                    |
|------------------|---------------------------------|


| Parameters      | Description                    |
|------------------|---------------------------------|
| Name            | shipmentID                     |
| Type            | string                         |
| Description     | ID of the shipment.            |
| Required        | True                           |

## Request Body
	{
	    "LineItemID": "",
	    "OrderID": "",
	    "QuantityShipped": 0
	}
| Name | Type | Description | Required | 
|---|---|---|---|
| OrderID | string | ID of the order. Required. | True |
| LineItemID | string | ID of the line item. Required. | True |
| QuantityShipped | integer | Quantity shipped of the shipment item. Required. | True |

**Response Status**: `200`

## Response Body
	{
	    "CostCenter": "",
	    "DateNeeded": "2018-03-27T16:00:00+00:00",
	    "LineItemID": "",
	    "OrderID": "",
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
	    "QuantityShipped": 0,
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
| OrderID | string | ID of the order. | True |
| LineItemID | string | ID of the line item. | True |
| QuantityShipped | integer | Quantity shipped of the shipment item. | True |
| UnitPrice | float | Unit price of the shipment item. | False |
| CostCenter | string | Cost center of the shipment item. | False |
| DateNeeded | date | Date needed of the shipment item. | False |
| Product | object | Product of the shipment item. | False |
| Specs | array | Specs of the shipment item. | False |
| xp | object | Container for extended (custom) properties of the shipment item. | False |

## `DELETE` `v1/shipments/{shipmentID}/items/{orderID}/{lineItemID}`
Delete a shipment item

| Parameters      | Description                    |
|------------------|---------------------------------|


| Parameters      | Description                    |
|------------------|---------------------------------|
| Name            | shipmentID                     |
| Type            | string                         |
| Description     | ID of the shipment.            |
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