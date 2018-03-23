---
title: Line Items
date: 2018-03-23
category: API Reference
tags: Orders And Fulfillment
slug: LineItems
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

## Requestbody
**Responsestatus**: `200`

## Responsebody
```
{'ID': '', 'ProductID': '', 'Quantity': 0, 'DateAdded': '2018-03-21T23:00:00+00:00', 'QuantityShipped': 0, 'UnitPrice': 0, 'LineTotal': 0, 'CostCenter': '', 'DateNeeded': '2018-03-21T23:00:00+00:00', 'ShippingAccount': '', 'ShippingAddressID': '', 'ShipFromAddressID': '', 'Product': {'ID': '', 'Name': '', 'Description': '', 'QuantityMultiplier': 0, 'ShipWeight': 0, 'ShipHeight': 0, 'ShipWidth': 0, 'ShipLength': 0, 'xp': {}}, 'ShippingAddress': {'ID': '', 'DateCreated': '2018-03-21T23:00:00+00:00', 'CompanyName': '', 'FirstName': '', 'LastName': '', 'Street1': '', 'Street2': '', 'City': '', 'State': '', 'Zip': '', 'Country': '', 'Phone': '', 'AddressName': '', 'xp': {}}, 'ShipFromAddress': {'ID': '', 'DateCreated': '2018-03-21T23:00:00+00:00', 'CompanyName': '', 'FirstName': '', 'LastName': '', 'Street1': '', 'Street2': '', 'City': '', 'State': '', 'Zip': '', 'Country': '', 'Phone': '', 'AddressName': '', 'xp': {}}, 'Specs': [{'SpecID': '', 'Name': '', 'OptionID': '', 'Value': ''}], 'xp': {}}
```


| Parameters      | Description                    |
|------------------|---------------------------------|
| Name            | ID                             |
| Type            | string                         |
| Description     | ID of the line item.           |
| Required        | False                          |


| Parameters      | Description                    |
|------------------|---------------------------------|
| Name            | ProductID                      |
| Type            | string                         |
| Description     | ID of the product.             |
| Required        | True                           |


| Parameters      | Description                    |
|------------------|---------------------------------|
| Name            | Quantity                       |
| Type            | integer                        |
| Description     | Quantity of the line item.     |
| Required        | True                           |


| Parameters      | Description                    |
|------------------|---------------------------------|
| Name            | DateAdded                      |
| Type            | date                           |
| Description     | Date added of the line item.   |
| Required        | False                          |


| Parameters      | Description                    |
|------------------|---------------------------------|
| Name            | QuantityShipped                |
| Type            | integer                        |
| Description     | Quantity shipped of the line item. |
| Required        | False                          |


| Parameters      | Description                    |
|------------------|---------------------------------|
| Name            | UnitPrice                      |
| Type            | float                          |
| Description     | Unit price of the line item.   |
| Required        | False                          |


| Parameters      | Description                    |
|------------------|---------------------------------|
| Name            | LineTotal                      |
| Type            | float                          |
| Description     | Line total of the line item.   |
| Required        | False                          |


| Parameters      | Description                    |
|------------------|---------------------------------|
| Name            | CostCenter                     |
| Type            | string                         |
| Description     | Cost center of the line item.  |
| Required        | False                          |


| Parameters      | Description                    |
|------------------|---------------------------------|
| Name            | DateNeeded                     |
| Type            | date                           |
| Description     | Date needed of the line item.  |
| Required        | False                          |


| Parameters      | Description                    |
|------------------|---------------------------------|
| Name            | ShippingAccount                |
| Type            | string                         |
| Description     | Shipping account of the line item. |
| Required        | False                          |


| Parameters      | Description                    |
|------------------|---------------------------------|
| Name            | ShippingAddressID              |
| Type            | string                         |
| Description     | ID of the shipping address.    |
| Required        | False                          |


| Parameters      | Description                    |
|------------------|---------------------------------|
| Name            | ShipFromAddressID              |
| Type            | string                         |
| Description     | ID of the ship from address.   |
| Required        | False                          |


| Parameters      | Description                    |
|------------------|---------------------------------|
| Name            | Product                        |
| Type            | object                         |
| Description     | Product of the line item.      |
| Required        | False                          |


| Parameters      | Description                    |
|------------------|---------------------------------|
| Name            | ShippingAddress                |
| Type            | object                         |
| Description     | Shipping address of the line item. |
| Required        | False                          |


| Parameters      | Description                    |
|------------------|---------------------------------|
| Name            | ShipFromAddress                |
| Type            | object                         |
| Description     | Ship from address of the line item. |
| Required        | False                          |


| Parameters      | Description                    |
|------------------|---------------------------------|
| Name            | Specs                          |
| Type            | array                          |
| Description     | Specs of the line item.        |
| Required        | False                          |


| Parameters      | Description                    |
|------------------|---------------------------------|
| Name            | xp                             |
| Type            | object                         |
| Description     | Container for extended (custom) properties of the line item. |
| Required        | False                          |

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

## Requestbody
**Responsestatus**: `200`

## Responsebody
```
{'Meta': {'Page': 1, 'PageSize': 20, 'TotalCount': 25, 'TotalPages': 2, 'ItemRange': [1, 20]}, 'Items': [{'ID': '', 'ProductID': '', 'Quantity': 0, 'DateAdded': '2018-03-21T23:00:00+00:00', 'QuantityShipped': 0, 'UnitPrice': 0, 'LineTotal': 0, 'CostCenter': '', 'DateNeeded': '2018-03-21T23:00:00+00:00', 'ShippingAccount': '', 'ShippingAddressID': '', 'ShipFromAddressID': '', 'Product': {'ID': '', 'Name': '', 'Description': '', 'QuantityMultiplier': 0, 'ShipWeight': 0, 'ShipHeight': 0, 'ShipWidth': 0, 'ShipLength': 0, 'xp': {}}, 'ShippingAddress': {'ID': '', 'DateCreated': '2018-03-21T23:00:00+00:00', 'CompanyName': '', 'FirstName': '', 'LastName': '', 'Street1': '', 'Street2': '', 'City': '', 'State': '', 'Zip': '', 'Country': '', 'Phone': '', 'AddressName': '', 'xp': {}}, 'ShipFromAddress': {'ID': '', 'DateCreated': '2018-03-21T23:00:00+00:00', 'CompanyName': '', 'FirstName': '', 'LastName': '', 'Street1': '', 'Street2': '', 'City': '', 'State': '', 'Zip': '', 'Country': '', 'Phone': '', 'AddressName': '', 'xp': {}}, 'Specs': [{'SpecID': '', 'Name': '', 'OptionID': '', 'Value': ''}], 'xp': {}}]}
```


| Parameters      | Description                    |
|------------------|---------------------------------|
| Name            | ID                             |
| Type            | string                         |
| Description     | ID of the line item.           |
| Required        | False                          |


| Parameters      | Description                    |
|------------------|---------------------------------|
| Name            | ProductID                      |
| Type            | string                         |
| Description     | ID of the product.             |
| Required        | True                           |


| Parameters      | Description                    |
|------------------|---------------------------------|
| Name            | Quantity                       |
| Type            | integer                        |
| Description     | Quantity of the line item.     |
| Required        | True                           |


| Parameters      | Description                    |
|------------------|---------------------------------|
| Name            | DateAdded                      |
| Type            | date                           |
| Description     | Date added of the line item.   |
| Required        | False                          |


| Parameters      | Description                    |
|------------------|---------------------------------|
| Name            | QuantityShipped                |
| Type            | integer                        |
| Description     | Quantity shipped of the line item. |
| Required        | False                          |


| Parameters      | Description                    |
|------------------|---------------------------------|
| Name            | UnitPrice                      |
| Type            | float                          |
| Description     | Unit price of the line item.   |
| Required        | False                          |


| Parameters      | Description                    |
|------------------|---------------------------------|
| Name            | LineTotal                      |
| Type            | float                          |
| Description     | Line total of the line item.   |
| Required        | False                          |


| Parameters      | Description                    |
|------------------|---------------------------------|
| Name            | CostCenter                     |
| Type            | string                         |
| Description     | Cost center of the line item.  |
| Required        | False                          |


| Parameters      | Description                    |
|------------------|---------------------------------|
| Name            | DateNeeded                     |
| Type            | date                           |
| Description     | Date needed of the line item.  |
| Required        | False                          |


| Parameters      | Description                    |
|------------------|---------------------------------|
| Name            | ShippingAccount                |
| Type            | string                         |
| Description     | Shipping account of the line item. |
| Required        | False                          |


| Parameters      | Description                    |
|------------------|---------------------------------|
| Name            | ShippingAddressID              |
| Type            | string                         |
| Description     | ID of the shipping address.    |
| Required        | False                          |


| Parameters      | Description                    |
|------------------|---------------------------------|
| Name            | ShipFromAddressID              |
| Type            | string                         |
| Description     | ID of the ship from address.   |
| Required        | False                          |


| Parameters      | Description                    |
|------------------|---------------------------------|
| Name            | Product                        |
| Type            | object                         |
| Description     | Product of the line item.      |
| Required        | False                          |


| Parameters      | Description                    |
|------------------|---------------------------------|
| Name            | ShippingAddress                |
| Type            | object                         |
| Description     | Shipping address of the line item. |
| Required        | False                          |


| Parameters      | Description                    |
|------------------|---------------------------------|
| Name            | ShipFromAddress                |
| Type            | object                         |
| Description     | Ship from address of the line item. |
| Required        | False                          |


| Parameters      | Description                    |
|------------------|---------------------------------|
| Name            | Specs                          |
| Type            | array                          |
| Description     | Specs of the line item.        |
| Required        | False                          |


| Parameters      | Description                    |
|------------------|---------------------------------|
| Name            | xp                             |
| Type            | object                         |
| Description     | Container for extended (custom) properties of the line item. |
| Required        | False                          |

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

## Requestbody
```
{'ID': '', 'ProductID': '', 'Quantity': 0, 'UnitPrice': 0, 'CostCenter': '', 'DateNeeded': '2018-03-21T23:00:00+00:00', 'ShippingAccount': '', 'ShippingAddressID': '', 'ShipFromAddressID': '', 'Specs': [{'SpecID': '', 'OptionID': '', 'Value': ''}], 'xp': {}}
```

```
[{'Name': 'ID', 'Type': 'string', 'Description': 'ID of the line item. Can only contain characters Aa-Zz, 0-9, -, and _. Searchable: priority level 1. Sortable.', 'Required': False}, {'Name': 'ProductID', 'Type': 'string', 'Description': 'ID of the product. Required. Searchable: priority level 2. Sortable.', 'Required': True}, {'Name': 'Quantity', 'Type': 'integer', 'Description': 'Quantity of the line item. Required. Must be at least 1.', 'Required': True}, {'Name': 'UnitPrice', 'Type': 'float', 'Description': 'Unit price of the line item. Must be between -9999999999999 and 9999999999999.', 'Required': False}, {'Name': 'CostCenter', 'Type': 'string', 'Description': 'Cost center of the line item.', 'Required': False}, {'Name': 'DateNeeded', 'Type': 'date', 'Description': 'Date needed of the line item.', 'Required': False}, {'Name': 'ShippingAccount', 'Type': 'string', 'Description': 'Shipping account of the line item.', 'Required': False}, {'Name': 'ShippingAddressID', 'Type': 'string', 'Description': 'ID of the shipping address.', 'Required': False}, {'Name': 'ShipFromAddressID', 'Type': 'string', 'Description': 'ID of the ship from address.', 'Required': False}, {'Name': 'Specs', 'Type': 'array', 'Description': 'Specs of the line item.', 'Required': False}, {'Name': 'xp', 'Type': 'object', 'Description': 'Container for extended (custom) properties of the line item.', 'Required': False}]
```

**Responsestatus**: `201`

## Responsebody
```
{'ID': '', 'ProductID': '', 'Quantity': 0, 'DateAdded': '2018-03-21T23:00:00+00:00', 'QuantityShipped': 0, 'UnitPrice': 0, 'LineTotal': 0, 'CostCenter': '', 'DateNeeded': '2018-03-21T23:00:00+00:00', 'ShippingAccount': '', 'ShippingAddressID': '', 'ShipFromAddressID': '', 'Product': {'ID': '', 'Name': '', 'Description': '', 'QuantityMultiplier': 0, 'ShipWeight': 0, 'ShipHeight': 0, 'ShipWidth': 0, 'ShipLength': 0, 'xp': {}}, 'ShippingAddress': {'ID': '', 'DateCreated': '2018-03-21T23:00:00+00:00', 'CompanyName': '', 'FirstName': '', 'LastName': '', 'Street1': '', 'Street2': '', 'City': '', 'State': '', 'Zip': '', 'Country': '', 'Phone': '', 'AddressName': '', 'xp': {}}, 'ShipFromAddress': {'ID': '', 'DateCreated': '2018-03-21T23:00:00+00:00', 'CompanyName': '', 'FirstName': '', 'LastName': '', 'Street1': '', 'Street2': '', 'City': '', 'State': '', 'Zip': '', 'Country': '', 'Phone': '', 'AddressName': '', 'xp': {}}, 'Specs': [{'SpecID': '', 'Name': '', 'OptionID': '', 'Value': ''}], 'xp': {}}
```


| Parameters      | Description                    |
|------------------|---------------------------------|
| Name            | ID                             |
| Type            | string                         |
| Description     | ID of the line item.           |
| Required        | False                          |


| Parameters      | Description                    |
|------------------|---------------------------------|
| Name            | ProductID                      |
| Type            | string                         |
| Description     | ID of the product.             |
| Required        | True                           |


| Parameters      | Description                    |
|------------------|---------------------------------|
| Name            | Quantity                       |
| Type            | integer                        |
| Description     | Quantity of the line item.     |
| Required        | True                           |


| Parameters      | Description                    |
|------------------|---------------------------------|
| Name            | DateAdded                      |
| Type            | date                           |
| Description     | Date added of the line item.   |
| Required        | False                          |


| Parameters      | Description                    |
|------------------|---------------------------------|
| Name            | QuantityShipped                |
| Type            | integer                        |
| Description     | Quantity shipped of the line item. |
| Required        | False                          |


| Parameters      | Description                    |
|------------------|---------------------------------|
| Name            | UnitPrice                      |
| Type            | float                          |
| Description     | Unit price of the line item.   |
| Required        | False                          |


| Parameters      | Description                    |
|------------------|---------------------------------|
| Name            | LineTotal                      |
| Type            | float                          |
| Description     | Line total of the line item.   |
| Required        | False                          |


| Parameters      | Description                    |
|------------------|---------------------------------|
| Name            | CostCenter                     |
| Type            | string                         |
| Description     | Cost center of the line item.  |
| Required        | False                          |


| Parameters      | Description                    |
|------------------|---------------------------------|
| Name            | DateNeeded                     |
| Type            | date                           |
| Description     | Date needed of the line item.  |
| Required        | False                          |


| Parameters      | Description                    |
|------------------|---------------------------------|
| Name            | ShippingAccount                |
| Type            | string                         |
| Description     | Shipping account of the line item. |
| Required        | False                          |


| Parameters      | Description                    |
|------------------|---------------------------------|
| Name            | ShippingAddressID              |
| Type            | string                         |
| Description     | ID of the shipping address.    |
| Required        | False                          |


| Parameters      | Description                    |
|------------------|---------------------------------|
| Name            | ShipFromAddressID              |
| Type            | string                         |
| Description     | ID of the ship from address.   |
| Required        | False                          |


| Parameters      | Description                    |
|------------------|---------------------------------|
| Name            | Product                        |
| Type            | object                         |
| Description     | Product of the line item.      |
| Required        | False                          |


| Parameters      | Description                    |
|------------------|---------------------------------|
| Name            | ShippingAddress                |
| Type            | object                         |
| Description     | Shipping address of the line item. |
| Required        | False                          |


| Parameters      | Description                    |
|------------------|---------------------------------|
| Name            | ShipFromAddress                |
| Type            | object                         |
| Description     | Ship from address of the line item. |
| Required        | False                          |


| Parameters      | Description                    |
|------------------|---------------------------------|
| Name            | Specs                          |
| Type            | array                          |
| Description     | Specs of the line item.        |
| Required        | False                          |


| Parameters      | Description                    |
|------------------|---------------------------------|
| Name            | xp                             |
| Type            | object                         |
| Description     | Container for extended (custom) properties of the line item. |
| Required        | False                          |

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

## Requestbody
```
{'ID': '', 'ProductID': '', 'Quantity': 0, 'UnitPrice': 0, 'CostCenter': '', 'DateNeeded': '2018-03-21T23:00:00+00:00', 'ShippingAccount': '', 'ShippingAddressID': '', 'ShipFromAddressID': '', 'Specs': [{'SpecID': '', 'OptionID': '', 'Value': ''}], 'xp': {}}
```

```
[{'Name': 'ID', 'Type': 'string', 'Description': 'ID of the line item. Can only contain characters Aa-Zz, 0-9, -, and _. Searchable: priority level 1. Sortable.', 'Required': False}, {'Name': 'ProductID', 'Type': 'string', 'Description': 'ID of the product. Required. Searchable: priority level 2. Sortable.', 'Required': True}, {'Name': 'Quantity', 'Type': 'integer', 'Description': 'Quantity of the line item. Required. Must be at least 1.', 'Required': True}, {'Name': 'UnitPrice', 'Type': 'float', 'Description': 'Unit price of the line item. Must be between -9999999999999 and 9999999999999.', 'Required': False}, {'Name': 'CostCenter', 'Type': 'string', 'Description': 'Cost center of the line item.', 'Required': False}, {'Name': 'DateNeeded', 'Type': 'date', 'Description': 'Date needed of the line item.', 'Required': False}, {'Name': 'ShippingAccount', 'Type': 'string', 'Description': 'Shipping account of the line item.', 'Required': False}, {'Name': 'ShippingAddressID', 'Type': 'string', 'Description': 'ID of the shipping address.', 'Required': False}, {'Name': 'ShipFromAddressID', 'Type': 'string', 'Description': 'ID of the ship from address.', 'Required': False}, {'Name': 'Specs', 'Type': 'array', 'Description': 'Specs of the line item.', 'Required': False}, {'Name': 'xp', 'Type': 'object', 'Description': 'Container for extended (custom) properties of the line item.', 'Required': False}]
```

**Responsestatus**: `200`

## Responsebody
```
{'ID': '', 'ProductID': '', 'Quantity': 0, 'DateAdded': '2018-03-21T23:00:00+00:00', 'QuantityShipped': 0, 'UnitPrice': 0, 'LineTotal': 0, 'CostCenter': '', 'DateNeeded': '2018-03-21T23:00:00+00:00', 'ShippingAccount': '', 'ShippingAddressID': '', 'ShipFromAddressID': '', 'Product': {'ID': '', 'Name': '', 'Description': '', 'QuantityMultiplier': 0, 'ShipWeight': 0, 'ShipHeight': 0, 'ShipWidth': 0, 'ShipLength': 0, 'xp': {}}, 'ShippingAddress': {'ID': '', 'DateCreated': '2018-03-21T23:00:00+00:00', 'CompanyName': '', 'FirstName': '', 'LastName': '', 'Street1': '', 'Street2': '', 'City': '', 'State': '', 'Zip': '', 'Country': '', 'Phone': '', 'AddressName': '', 'xp': {}}, 'ShipFromAddress': {'ID': '', 'DateCreated': '2018-03-21T23:00:00+00:00', 'CompanyName': '', 'FirstName': '', 'LastName': '', 'Street1': '', 'Street2': '', 'City': '', 'State': '', 'Zip': '', 'Country': '', 'Phone': '', 'AddressName': '', 'xp': {}}, 'Specs': [{'SpecID': '', 'Name': '', 'OptionID': '', 'Value': ''}], 'xp': {}}
```


| Parameters      | Description                    |
|------------------|---------------------------------|
| Name            | ID                             |
| Type            | string                         |
| Description     | ID of the line item.           |
| Required        | False                          |


| Parameters      | Description                    |
|------------------|---------------------------------|
| Name            | ProductID                      |
| Type            | string                         |
| Description     | ID of the product.             |
| Required        | True                           |


| Parameters      | Description                    |
|------------------|---------------------------------|
| Name            | Quantity                       |
| Type            | integer                        |
| Description     | Quantity of the line item.     |
| Required        | True                           |


| Parameters      | Description                    |
|------------------|---------------------------------|
| Name            | DateAdded                      |
| Type            | date                           |
| Description     | Date added of the line item.   |
| Required        | False                          |


| Parameters      | Description                    |
|------------------|---------------------------------|
| Name            | QuantityShipped                |
| Type            | integer                        |
| Description     | Quantity shipped of the line item. |
| Required        | False                          |


| Parameters      | Description                    |
|------------------|---------------------------------|
| Name            | UnitPrice                      |
| Type            | float                          |
| Description     | Unit price of the line item.   |
| Required        | False                          |


| Parameters      | Description                    |
|------------------|---------------------------------|
| Name            | LineTotal                      |
| Type            | float                          |
| Description     | Line total of the line item.   |
| Required        | False                          |


| Parameters      | Description                    |
|------------------|---------------------------------|
| Name            | CostCenter                     |
| Type            | string                         |
| Description     | Cost center of the line item.  |
| Required        | False                          |


| Parameters      | Description                    |
|------------------|---------------------------------|
| Name            | DateNeeded                     |
| Type            | date                           |
| Description     | Date needed of the line item.  |
| Required        | False                          |


| Parameters      | Description                    |
|------------------|---------------------------------|
| Name            | ShippingAccount                |
| Type            | string                         |
| Description     | Shipping account of the line item. |
| Required        | False                          |


| Parameters      | Description                    |
|------------------|---------------------------------|
| Name            | ShippingAddressID              |
| Type            | string                         |
| Description     | ID of the shipping address.    |
| Required        | False                          |


| Parameters      | Description                    |
|------------------|---------------------------------|
| Name            | ShipFromAddressID              |
| Type            | string                         |
| Description     | ID of the ship from address.   |
| Required        | False                          |


| Parameters      | Description                    |
|------------------|---------------------------------|
| Name            | Product                        |
| Type            | object                         |
| Description     | Product of the line item.      |
| Required        | False                          |


| Parameters      | Description                    |
|------------------|---------------------------------|
| Name            | ShippingAddress                |
| Type            | object                         |
| Description     | Shipping address of the line item. |
| Required        | False                          |


| Parameters      | Description                    |
|------------------|---------------------------------|
| Name            | ShipFromAddress                |
| Type            | object                         |
| Description     | Ship from address of the line item. |
| Required        | False                          |


| Parameters      | Description                    |
|------------------|---------------------------------|
| Name            | Specs                          |
| Type            | array                          |
| Description     | Specs of the line item.        |
| Required        | False                          |


| Parameters      | Description                    |
|------------------|---------------------------------|
| Name            | xp                             |
| Type            | object                         |
| Description     | Container for extended (custom) properties of the line item. |
| Required        | False                          |

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

## Requestbody
**Responsestatus**: `204`

## Responsebody
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

## Requestbody
```
{'ID': '', 'ProductID': '', 'Quantity': 0, 'UnitPrice': 0, 'CostCenter': '', 'DateNeeded': '2018-03-21T23:00:00+00:00', 'ShippingAccount': '', 'ShippingAddressID': '', 'ShipFromAddressID': '', 'Specs': [{'SpecID': '', 'OptionID': '', 'Value': ''}], 'xp': {}}
```

```
[{'Name': 'ID', 'Type': 'string', 'Description': 'ID of the line item. Can only contain characters Aa-Zz, 0-9, -, and _. Searchable: priority level 1. Sortable.', 'Required': False}, {'Name': 'ProductID', 'Type': 'string', 'Description': 'ID of the product. Required. Searchable: priority level 2. Sortable.', 'Required': True}, {'Name': 'Quantity', 'Type': 'integer', 'Description': 'Quantity of the line item. Required. Must be at least 1.', 'Required': True}, {'Name': 'UnitPrice', 'Type': 'float', 'Description': 'Unit price of the line item. Must be between -9999999999999 and 9999999999999.', 'Required': False}, {'Name': 'CostCenter', 'Type': 'string', 'Description': 'Cost center of the line item.', 'Required': False}, {'Name': 'DateNeeded', 'Type': 'date', 'Description': 'Date needed of the line item.', 'Required': False}, {'Name': 'ShippingAccount', 'Type': 'string', 'Description': 'Shipping account of the line item.', 'Required': False}, {'Name': 'ShippingAddressID', 'Type': 'string', 'Description': 'ID of the shipping address.', 'Required': False}, {'Name': 'ShipFromAddressID', 'Type': 'string', 'Description': 'ID of the ship from address.', 'Required': False}, {'Name': 'Specs', 'Type': 'array', 'Description': 'Specs of the line item.', 'Required': False}, {'Name': 'xp', 'Type': 'object', 'Description': 'Container for extended (custom) properties of the line item.', 'Required': False}]
```

**Responsestatus**: `200`

## Responsebody
```
{'ID': '', 'ProductID': '', 'Quantity': 0, 'DateAdded': '2018-03-21T23:00:00+00:00', 'QuantityShipped': 0, 'UnitPrice': 0, 'LineTotal': 0, 'CostCenter': '', 'DateNeeded': '2018-03-21T23:00:00+00:00', 'ShippingAccount': '', 'ShippingAddressID': '', 'ShipFromAddressID': '', 'Product': {'ID': '', 'Name': '', 'Description': '', 'QuantityMultiplier': 0, 'ShipWeight': 0, 'ShipHeight': 0, 'ShipWidth': 0, 'ShipLength': 0, 'xp': {}}, 'ShippingAddress': {'ID': '', 'DateCreated': '2018-03-21T23:00:00+00:00', 'CompanyName': '', 'FirstName': '', 'LastName': '', 'Street1': '', 'Street2': '', 'City': '', 'State': '', 'Zip': '', 'Country': '', 'Phone': '', 'AddressName': '', 'xp': {}}, 'ShipFromAddress': {'ID': '', 'DateCreated': '2018-03-21T23:00:00+00:00', 'CompanyName': '', 'FirstName': '', 'LastName': '', 'Street1': '', 'Street2': '', 'City': '', 'State': '', 'Zip': '', 'Country': '', 'Phone': '', 'AddressName': '', 'xp': {}}, 'Specs': [{'SpecID': '', 'Name': '', 'OptionID': '', 'Value': ''}], 'xp': {}}
```


| Parameters      | Description                    |
|------------------|---------------------------------|
| Name            | ID                             |
| Type            | string                         |
| Description     | ID of the line item.           |
| Required        | False                          |


| Parameters      | Description                    |
|------------------|---------------------------------|
| Name            | ProductID                      |
| Type            | string                         |
| Description     | ID of the product.             |
| Required        | True                           |


| Parameters      | Description                    |
|------------------|---------------------------------|
| Name            | Quantity                       |
| Type            | integer                        |
| Description     | Quantity of the line item.     |
| Required        | True                           |


| Parameters      | Description                    |
|------------------|---------------------------------|
| Name            | DateAdded                      |
| Type            | date                           |
| Description     | Date added of the line item.   |
| Required        | False                          |


| Parameters      | Description                    |
|------------------|---------------------------------|
| Name            | QuantityShipped                |
| Type            | integer                        |
| Description     | Quantity shipped of the line item. |
| Required        | False                          |


| Parameters      | Description                    |
|------------------|---------------------------------|
| Name            | UnitPrice                      |
| Type            | float                          |
| Description     | Unit price of the line item.   |
| Required        | False                          |


| Parameters      | Description                    |
|------------------|---------------------------------|
| Name            | LineTotal                      |
| Type            | float                          |
| Description     | Line total of the line item.   |
| Required        | False                          |


| Parameters      | Description                    |
|------------------|---------------------------------|
| Name            | CostCenter                     |
| Type            | string                         |
| Description     | Cost center of the line item.  |
| Required        | False                          |


| Parameters      | Description                    |
|------------------|---------------------------------|
| Name            | DateNeeded                     |
| Type            | date                           |
| Description     | Date needed of the line item.  |
| Required        | False                          |


| Parameters      | Description                    |
|------------------|---------------------------------|
| Name            | ShippingAccount                |
| Type            | string                         |
| Description     | Shipping account of the line item. |
| Required        | False                          |


| Parameters      | Description                    |
|------------------|---------------------------------|
| Name            | ShippingAddressID              |
| Type            | string                         |
| Description     | ID of the shipping address.    |
| Required        | False                          |


| Parameters      | Description                    |
|------------------|---------------------------------|
| Name            | ShipFromAddressID              |
| Type            | string                         |
| Description     | ID of the ship from address.   |
| Required        | False                          |


| Parameters      | Description                    |
|------------------|---------------------------------|
| Name            | Product                        |
| Type            | object                         |
| Description     | Product of the line item.      |
| Required        | False                          |


| Parameters      | Description                    |
|------------------|---------------------------------|
| Name            | ShippingAddress                |
| Type            | object                         |
| Description     | Shipping address of the line item. |
| Required        | False                          |


| Parameters      | Description                    |
|------------------|---------------------------------|
| Name            | ShipFromAddress                |
| Type            | object                         |
| Description     | Ship from address of the line item. |
| Required        | False                          |


| Parameters      | Description                    |
|------------------|---------------------------------|
| Name            | Specs                          |
| Type            | array                          |
| Description     | Specs of the line item.        |
| Required        | False                          |


| Parameters      | Description                    |
|------------------|---------------------------------|
| Name            | xp                             |
| Type            | object                         |
| Description     | Container for extended (custom) properties of the line item. |
| Required        | False                          |

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

## Requestbody
```
{'ID': '', 'CompanyName': '', 'FirstName': '', 'LastName': '', 'Street1': '', 'Street2': '', 'City': '', 'State': '', 'Zip': '', 'Country': '', 'Phone': '', 'AddressName': '', 'xp': {}}
```

```
[{'Name': 'ID', 'Type': 'string', 'Description': 'ID of the address. Can only contain characters Aa-Zz, 0-9, -, and _. Searchable: priority level 1. Sortable: priority level 2.', 'Required': False}, {'Name': 'CompanyName', 'Type': 'string', 'Description': 'Company name of the address. Max length 100 characters. Sortable.', 'Required': False}, {'Name': 'FirstName', 'Type': 'string', 'Description': 'First name of the address. Max length 100 characters. Searchable: priority level 7. Sortable.', 'Required': False}, {'Name': 'LastName', 'Type': 'string', 'Description': 'Last name of the address. Max length 100 characters. Searchable: priority level 6. Sortable.', 'Required': False}, {'Name': 'Street1', 'Type': 'string', 'Description': 'Street 1 of the address. Required. Max length 100 characters. Searchable: priority level 4. Sortable.', 'Required': True}, {'Name': 'Street2', 'Type': 'string', 'Description': 'Street 2 of the address. Max length 100 characters. Searchable: priority level 5. Sortable.', 'Required': False}, {'Name': 'City', 'Type': 'string', 'Description': 'City of the address. Required. Max length 100 characters. Searchable: priority level 3. Sortable.', 'Required': True}, {'Name': 'State', 'Type': 'string', 'Description': 'State of the address. Required. Max length 100 characters. Searchable: priority level 7. Sortable.', 'Required': True}, {'Name': 'Zip', 'Type': 'string', 'Description': 'Zip of the address. Required. Max length 100 characters. Searchable: priority level 6. Sortable.', 'Required': True}, {'Name': 'Country', 'Type': 'string', 'Description': 'Country of the address. Required. Max length 2 characters. Sortable.', 'Required': True}, {'Name': 'Phone', 'Type': 'string', 'Description': 'Phone of the address. Max length 100 characters. Sortable.', 'Required': False}, {'Name': 'AddressName', 'Type': 'string', 'Description': 'Address name of the address. Max length 100 characters. Searchable: priority level 2. Sortable: priority level 1.', 'Required': False}, {'Name': 'xp', 'Type': 'object', 'Description': 'Container for extended (custom) properties of the address.', 'Required': False}]
```

**Responsestatus**: `200`

## Responsebody
```
{'ID': '', 'ProductID': '', 'Quantity': 0, 'DateAdded': '2018-03-21T23:00:00+00:00', 'QuantityShipped': 0, 'UnitPrice': 0, 'LineTotal': 0, 'CostCenter': '', 'DateNeeded': '2018-03-21T23:00:00+00:00', 'ShippingAccount': '', 'ShippingAddressID': '', 'ShipFromAddressID': '', 'Product': {'ID': '', 'Name': '', 'Description': '', 'QuantityMultiplier': 0, 'ShipWeight': 0, 'ShipHeight': 0, 'ShipWidth': 0, 'ShipLength': 0, 'xp': {}}, 'ShippingAddress': {'ID': '', 'DateCreated': '2018-03-21T23:00:00+00:00', 'CompanyName': '', 'FirstName': '', 'LastName': '', 'Street1': '', 'Street2': '', 'City': '', 'State': '', 'Zip': '', 'Country': '', 'Phone': '', 'AddressName': '', 'xp': {}}, 'ShipFromAddress': {'ID': '', 'DateCreated': '2018-03-21T23:00:00+00:00', 'CompanyName': '', 'FirstName': '', 'LastName': '', 'Street1': '', 'Street2': '', 'City': '', 'State': '', 'Zip': '', 'Country': '', 'Phone': '', 'AddressName': '', 'xp': {}}, 'Specs': [{'SpecID': '', 'Name': '', 'OptionID': '', 'Value': ''}], 'xp': {}}
```


| Parameters      | Description                    |
|------------------|---------------------------------|
| Name            | ID                             |
| Type            | string                         |
| Description     | ID of the line item.           |
| Required        | False                          |


| Parameters      | Description                    |
|------------------|---------------------------------|
| Name            | ProductID                      |
| Type            | string                         |
| Description     | ID of the product.             |
| Required        | True                           |


| Parameters      | Description                    |
|------------------|---------------------------------|
| Name            | Quantity                       |
| Type            | integer                        |
| Description     | Quantity of the line item.     |
| Required        | True                           |


| Parameters      | Description                    |
|------------------|---------------------------------|
| Name            | DateAdded                      |
| Type            | date                           |
| Description     | Date added of the line item.   |
| Required        | False                          |


| Parameters      | Description                    |
|------------------|---------------------------------|
| Name            | QuantityShipped                |
| Type            | integer                        |
| Description     | Quantity shipped of the line item. |
| Required        | False                          |


| Parameters      | Description                    |
|------------------|---------------------------------|
| Name            | UnitPrice                      |
| Type            | float                          |
| Description     | Unit price of the line item.   |
| Required        | False                          |


| Parameters      | Description                    |
|------------------|---------------------------------|
| Name            | LineTotal                      |
| Type            | float                          |
| Description     | Line total of the line item.   |
| Required        | False                          |


| Parameters      | Description                    |
|------------------|---------------------------------|
| Name            | CostCenter                     |
| Type            | string                         |
| Description     | Cost center of the line item.  |
| Required        | False                          |


| Parameters      | Description                    |
|------------------|---------------------------------|
| Name            | DateNeeded                     |
| Type            | date                           |
| Description     | Date needed of the line item.  |
| Required        | False                          |


| Parameters      | Description                    |
|------------------|---------------------------------|
| Name            | ShippingAccount                |
| Type            | string                         |
| Description     | Shipping account of the line item. |
| Required        | False                          |


| Parameters      | Description                    |
|------------------|---------------------------------|
| Name            | ShippingAddressID              |
| Type            | string                         |
| Description     | ID of the shipping address.    |
| Required        | False                          |


| Parameters      | Description                    |
|------------------|---------------------------------|
| Name            | ShipFromAddressID              |
| Type            | string                         |
| Description     | ID of the ship from address.   |
| Required        | False                          |


| Parameters      | Description                    |
|------------------|---------------------------------|
| Name            | Product                        |
| Type            | object                         |
| Description     | Product of the line item.      |
| Required        | False                          |


| Parameters      | Description                    |
|------------------|---------------------------------|
| Name            | ShippingAddress                |
| Type            | object                         |
| Description     | Shipping address of the line item. |
| Required        | False                          |


| Parameters      | Description                    |
|------------------|---------------------------------|
| Name            | ShipFromAddress                |
| Type            | object                         |
| Description     | Ship from address of the line item. |
| Required        | False                          |


| Parameters      | Description                    |
|------------------|---------------------------------|
| Name            | Specs                          |
| Type            | array                          |
| Description     | Specs of the line item.        |
| Required        | False                          |


| Parameters      | Description                    |
|------------------|---------------------------------|
| Name            | xp                             |
| Type            | object                         |
| Description     | Container for extended (custom) properties of the line item. |
| Required        | False                          |

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

## Requestbody
```
{'ID': '', 'CompanyName': '', 'FirstName': '', 'LastName': '', 'Street1': '', 'Street2': '', 'City': '', 'State': '', 'Zip': '', 'Country': '', 'Phone': '', 'AddressName': '', 'xp': {}}
```

```
[{'Name': 'ID', 'Type': 'string', 'Description': 'ID of the address. Can only contain characters Aa-Zz, 0-9, -, and _. Searchable: priority level 1. Sortable: priority level 2.', 'Required': False}, {'Name': 'CompanyName', 'Type': 'string', 'Description': 'Company name of the address. Max length 100 characters. Sortable.', 'Required': False}, {'Name': 'FirstName', 'Type': 'string', 'Description': 'First name of the address. Max length 100 characters. Searchable: priority level 7. Sortable.', 'Required': False}, {'Name': 'LastName', 'Type': 'string', 'Description': 'Last name of the address. Max length 100 characters. Searchable: priority level 6. Sortable.', 'Required': False}, {'Name': 'Street1', 'Type': 'string', 'Description': 'Street 1 of the address. Required. Max length 100 characters. Searchable: priority level 4. Sortable.', 'Required': True}, {'Name': 'Street2', 'Type': 'string', 'Description': 'Street 2 of the address. Max length 100 characters. Searchable: priority level 5. Sortable.', 'Required': False}, {'Name': 'City', 'Type': 'string', 'Description': 'City of the address. Required. Max length 100 characters. Searchable: priority level 3. Sortable.', 'Required': True}, {'Name': 'State', 'Type': 'string', 'Description': 'State of the address. Required. Max length 100 characters. Searchable: priority level 7. Sortable.', 'Required': True}, {'Name': 'Zip', 'Type': 'string', 'Description': 'Zip of the address. Required. Max length 100 characters. Searchable: priority level 6. Sortable.', 'Required': True}, {'Name': 'Country', 'Type': 'string', 'Description': 'Country of the address. Required. Max length 2 characters. Sortable.', 'Required': True}, {'Name': 'Phone', 'Type': 'string', 'Description': 'Phone of the address. Max length 100 characters. Sortable.', 'Required': False}, {'Name': 'AddressName', 'Type': 'string', 'Description': 'Address name of the address. Max length 100 characters. Searchable: priority level 2. Sortable: priority level 1.', 'Required': False}, {'Name': 'xp', 'Type': 'object', 'Description': 'Container for extended (custom) properties of the address.', 'Required': False}]
```

**Responsestatus**: `200`

## Responsebody
```
{'ID': '', 'ProductID': '', 'Quantity': 0, 'DateAdded': '2018-03-21T23:00:00+00:00', 'QuantityShipped': 0, 'UnitPrice': 0, 'LineTotal': 0, 'CostCenter': '', 'DateNeeded': '2018-03-21T23:00:00+00:00', 'ShippingAccount': '', 'ShippingAddressID': '', 'ShipFromAddressID': '', 'Product': {'ID': '', 'Name': '', 'Description': '', 'QuantityMultiplier': 0, 'ShipWeight': 0, 'ShipHeight': 0, 'ShipWidth': 0, 'ShipLength': 0, 'xp': {}}, 'ShippingAddress': {'ID': '', 'DateCreated': '2018-03-21T23:00:00+00:00', 'CompanyName': '', 'FirstName': '', 'LastName': '', 'Street1': '', 'Street2': '', 'City': '', 'State': '', 'Zip': '', 'Country': '', 'Phone': '', 'AddressName': '', 'xp': {}}, 'ShipFromAddress': {'ID': '', 'DateCreated': '2018-03-21T23:00:00+00:00', 'CompanyName': '', 'FirstName': '', 'LastName': '', 'Street1': '', 'Street2': '', 'City': '', 'State': '', 'Zip': '', 'Country': '', 'Phone': '', 'AddressName': '', 'xp': {}}, 'Specs': [{'SpecID': '', 'Name': '', 'OptionID': '', 'Value': ''}], 'xp': {}}
```


| Parameters      | Description                    |
|------------------|---------------------------------|
| Name            | ID                             |
| Type            | string                         |
| Description     | ID of the line item.           |
| Required        | False                          |


| Parameters      | Description                    |
|------------------|---------------------------------|
| Name            | ProductID                      |
| Type            | string                         |
| Description     | ID of the product.             |
| Required        | True                           |


| Parameters      | Description                    |
|------------------|---------------------------------|
| Name            | Quantity                       |
| Type            | integer                        |
| Description     | Quantity of the line item.     |
| Required        | True                           |


| Parameters      | Description                    |
|------------------|---------------------------------|
| Name            | DateAdded                      |
| Type            | date                           |
| Description     | Date added of the line item.   |
| Required        | False                          |


| Parameters      | Description                    |
|------------------|---------------------------------|
| Name            | QuantityShipped                |
| Type            | integer                        |
| Description     | Quantity shipped of the line item. |
| Required        | False                          |


| Parameters      | Description                    |
|------------------|---------------------------------|
| Name            | UnitPrice                      |
| Type            | float                          |
| Description     | Unit price of the line item.   |
| Required        | False                          |


| Parameters      | Description                    |
|------------------|---------------------------------|
| Name            | LineTotal                      |
| Type            | float                          |
| Description     | Line total of the line item.   |
| Required        | False                          |


| Parameters      | Description                    |
|------------------|---------------------------------|
| Name            | CostCenter                     |
| Type            | string                         |
| Description     | Cost center of the line item.  |
| Required        | False                          |


| Parameters      | Description                    |
|------------------|---------------------------------|
| Name            | DateNeeded                     |
| Type            | date                           |
| Description     | Date needed of the line item.  |
| Required        | False                          |


| Parameters      | Description                    |
|------------------|---------------------------------|
| Name            | ShippingAccount                |
| Type            | string                         |
| Description     | Shipping account of the line item. |
| Required        | False                          |


| Parameters      | Description                    |
|------------------|---------------------------------|
| Name            | ShippingAddressID              |
| Type            | string                         |
| Description     | ID of the shipping address.    |
| Required        | False                          |


| Parameters      | Description                    |
|------------------|---------------------------------|
| Name            | ShipFromAddressID              |
| Type            | string                         |
| Description     | ID of the ship from address.   |
| Required        | False                          |


| Parameters      | Description                    |
|------------------|---------------------------------|
| Name            | Product                        |
| Type            | object                         |
| Description     | Product of the line item.      |
| Required        | False                          |


| Parameters      | Description                    |
|------------------|---------------------------------|
| Name            | ShippingAddress                |
| Type            | object                         |
| Description     | Shipping address of the line item. |
| Required        | False                          |


| Parameters      | Description                    |
|------------------|---------------------------------|
| Name            | ShipFromAddress                |
| Type            | object                         |
| Description     | Ship from address of the line item. |
| Required        | False                          |


| Parameters      | Description                    |
|------------------|---------------------------------|
| Name            | Specs                          |
| Type            | array                          |
| Description     | Specs of the line item.        |
| Required        | False                          |


| Parameters      | Description                    |
|------------------|---------------------------------|
| Name            | xp                             |
| Type            | object                         |
| Description     | Container for extended (custom) properties of the line item. |
| Required        | False                          |
