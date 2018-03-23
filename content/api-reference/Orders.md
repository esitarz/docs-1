---
title: Orders
date: 2018-03-23
category: API Reference
tags: Orders And Fulfillment
slug: Orders
---
An Order represents a business transaction between two parties. It
typically consists of a collection of Line Items, a Payment Method, Tax
and Shipping information, etc. The OrderCloud platform defines various
"actions" that can be performed against Orders, such as Submit, Approve,
Ship, etc. These actions transform the state of the order and often
trigger external events such as financial transactions.

---

## `GET` `v1/orders/{direction}/{orderID}`
Get a single order

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
**Responsestatus**: `200`

## Responsebody
```
{'ID': '', 'FromUser': {'ID': '', 'Username': '', 'FirstName': '', 'LastName': '', 'Email': '', 'Phone': '', 'TermsAccepted': '2018-03-21T23:00:00+00:00', 'Active': False, 'xp': {}, 'AvailableRoles': ['']}, 'FromCompanyID': '', 'FromUserID': '', 'BillingAddressID': '', 'BillingAddress': {'ID': '', 'DateCreated': '2018-03-21T23:00:00+00:00', 'CompanyName': '', 'FirstName': '', 'LastName': '', 'Street1': '', 'Street2': '', 'City': '', 'State': '', 'Zip': '', 'Country': '', 'Phone': '', 'AddressName': '', 'xp': {}}, 'ShippingAddressID': '', 'Comments': '', 'LineItemCount': 0, 'Status': 'Unsubmitted', 'DateCreated': '2018-03-21T23:00:00+00:00', 'DateSubmitted': '2018-03-21T23:00:00+00:00', 'DateApproved': '2018-03-21T23:00:00+00:00', 'DateDeclined': '2018-03-21T23:00:00+00:00', 'DateCanceled': '2018-03-21T23:00:00+00:00', 'DateCompleted': '2018-03-21T23:00:00+00:00', 'Subtotal': 0, 'ShippingCost': 0, 'TaxCost': 0, 'PromotionDiscount': 0, 'Total': 0, 'IsSubmitted': False, 'xp': {}}
```


| Parameters      | Description                    |
|------------------|---------------------------------|
| Name            | ID                             |
| Type            | string                         |
| Description     | ID of the order.               |
| Required        | False                          |


| Parameters      | Description                    |
|------------------|---------------------------------|
| Name            | FromUser                       |
| Type            | object                         |
| Description     | From user of the order.        |
| Required        | False                          |


| Parameters      | Description                    |
|------------------|---------------------------------|
| Name            | FromCompanyID                  |
| Type            | string                         |
| Description     | ID of the from company.        |
| Required        | False                          |


| Parameters      | Description                    |
|------------------|---------------------------------|
| Name            | FromUserID                     |
| Type            | string                         |
| Description     | ID of the from user.           |
| Required        | False                          |


| Parameters      | Description                    |
|------------------|---------------------------------|
| Name            | BillingAddressID               |
| Type            | string                         |
| Description     | ID of the billing address.     |
| Required        | False                          |


| Parameters      | Description                    |
|------------------|---------------------------------|
| Name            | BillingAddress                 |
| Type            | object                         |
| Description     | Billing address of the order.  |
| Required        | False                          |


| Parameters      | Description                    |
|------------------|---------------------------------|
| Name            | ShippingAddressID              |
| Type            | string                         |
| Description     | ID of the Shipping Address for all LineItems on the Order. Null when there are multiple Shipping Addresses involved. |
| Required        | False                          |


| Parameters      | Description                    |
|------------------|---------------------------------|
| Name            | Comments                       |
| Type            | string                         |
| Description     | Comments of the order.         |
| Required        | False                          |


| Parameters      | Description                    |
|------------------|---------------------------------|
| Name            | LineItemCount                  |
| Type            | integer                        |
| Description     | Line item count of the order.  |
| Required        | False                          |


| Parameters      | Description                    |
|------------------|---------------------------------|
| Name            | Status                         |
| Type            | string                         |
| Description     | Status of the order. Possible values: Unsubmitted, AwaitingApproval, Declined, Open, Completed, Canceled. |
| Required        | False                          |


| Parameters      | Description                    |
|------------------|---------------------------------|
| Name            | DateCreated                    |
| Type            | date                           |
| Description     | Date created of the order.     |
| Required        | False                          |


| Parameters      | Description                    |
|------------------|---------------------------------|
| Name            | DateSubmitted                  |
| Type            | date                           |
| Description     | Date submitted of the order.   |
| Required        | False                          |


| Parameters      | Description                    |
|------------------|---------------------------------|
| Name            | DateApproved                   |
| Type            | date                           |
| Description     | Date approved of the order.    |
| Required        | False                          |


| Parameters      | Description                    |
|------------------|---------------------------------|
| Name            | DateDeclined                   |
| Type            | date                           |
| Description     | Date declined of the order.    |
| Required        | False                          |


| Parameters      | Description                    |
|------------------|---------------------------------|
| Name            | DateCanceled                   |
| Type            | date                           |
| Description     | Date canceled of the order.    |
| Required        | False                          |


| Parameters      | Description                    |
|------------------|---------------------------------|
| Name            | DateCompleted                  |
| Type            | date                           |
| Description     | Date completed of the order.   |
| Required        | False                          |


| Parameters      | Description                    |
|------------------|---------------------------------|
| Name            | Subtotal                       |
| Type            | float                          |
| Description     | Subtotal of the order.         |
| Required        | False                          |


| Parameters      | Description                    |
|------------------|---------------------------------|
| Name            | ShippingCost                   |
| Type            | float                          |
| Description     | Shipping cost of the order.    |
| Required        | False                          |


| Parameters      | Description                    |
|------------------|---------------------------------|
| Name            | TaxCost                        |
| Type            | float                          |
| Description     | Tax cost of the order.         |
| Required        | False                          |


| Parameters      | Description                    |
|------------------|---------------------------------|
| Name            | PromotionDiscount              |
| Type            | float                          |
| Description     | Promotion discount of the order. |
| Required        | False                          |


| Parameters      | Description                    |
|------------------|---------------------------------|
| Name            | Total                          |
| Type            | float                          |
| Description     | Total of the order.            |
| Required        | False                          |


| Parameters      | Description                    |
|------------------|---------------------------------|
| Name            | IsSubmitted                    |
| Type            | boolean                        |
| Description     | True if this Order has been passed from the Buyer to the Seller. |
| Required        | False                          |


| Parameters      | Description                    |
|------------------|---------------------------------|
| Name            | xp                             |
| Type            | object                         |
| Description     | Container for extended (custom) properties of the order. |
| Required        | False                          |

## `GET` `v1/orders/{direction}`
Get a list of orders

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
| Name            | buyerID                        |
| Type            | string                         |
| Description     | ID of the buyer.               |
| Required        | False                          |


| Parameters      | Description                    |
|------------------|---------------------------------|
| Name            | supplierID                     |
| Type            | string                         |
| Description     | ID of the supplier.            |
| Required        | False                          |


| Parameters      | Description                    |
|------------------|---------------------------------|
| Name            | from                           |
| Type            | date                           |
| Description     | Lower bound of date range that the order was created. |
| Required        | False                          |


| Parameters      | Description                    |
|------------------|---------------------------------|
| Name            | to                             |
| Type            | date                           |
| Description     | Upper bound of date range that the order was created. |
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
{'Meta': {'Page': 1, 'PageSize': 20, 'TotalCount': 25, 'TotalPages': 2, 'ItemRange': [1, 20]}, 'Items': [{'ID': '', 'FromUser': {'ID': '', 'Username': '', 'FirstName': '', 'LastName': '', 'Email': '', 'Phone': '', 'TermsAccepted': '2018-03-21T23:00:00+00:00', 'Active': False, 'xp': {}, 'AvailableRoles': ['']}, 'FromCompanyID': '', 'FromUserID': '', 'BillingAddressID': '', 'BillingAddress': {'ID': '', 'DateCreated': '2018-03-21T23:00:00+00:00', 'CompanyName': '', 'FirstName': '', 'LastName': '', 'Street1': '', 'Street2': '', 'City': '', 'State': '', 'Zip': '', 'Country': '', 'Phone': '', 'AddressName': '', 'xp': {}}, 'ShippingAddressID': '', 'Comments': '', 'LineItemCount': 0, 'Status': 'Unsubmitted', 'DateCreated': '2018-03-21T23:00:00+00:00', 'DateSubmitted': '2018-03-21T23:00:00+00:00', 'DateApproved': '2018-03-21T23:00:00+00:00', 'DateDeclined': '2018-03-21T23:00:00+00:00', 'DateCanceled': '2018-03-21T23:00:00+00:00', 'DateCompleted': '2018-03-21T23:00:00+00:00', 'Subtotal': 0, 'ShippingCost': 0, 'TaxCost': 0, 'PromotionDiscount': 0, 'Total': 0, 'IsSubmitted': False, 'xp': {}}]}
```


| Parameters      | Description                    |
|------------------|---------------------------------|
| Name            | ID                             |
| Type            | string                         |
| Description     | ID of the order.               |
| Required        | False                          |


| Parameters      | Description                    |
|------------------|---------------------------------|
| Name            | FromUser                       |
| Type            | object                         |
| Description     | From user of the order.        |
| Required        | False                          |


| Parameters      | Description                    |
|------------------|---------------------------------|
| Name            | FromCompanyID                  |
| Type            | string                         |
| Description     | ID of the from company.        |
| Required        | False                          |


| Parameters      | Description                    |
|------------------|---------------------------------|
| Name            | FromUserID                     |
| Type            | string                         |
| Description     | ID of the from user.           |
| Required        | False                          |


| Parameters      | Description                    |
|------------------|---------------------------------|
| Name            | BillingAddressID               |
| Type            | string                         |
| Description     | ID of the billing address.     |
| Required        | False                          |


| Parameters      | Description                    |
|------------------|---------------------------------|
| Name            | BillingAddress                 |
| Type            | object                         |
| Description     | Billing address of the order.  |
| Required        | False                          |


| Parameters      | Description                    |
|------------------|---------------------------------|
| Name            | ShippingAddressID              |
| Type            | string                         |
| Description     | ID of the Shipping Address for all LineItems on the Order. Null when there are multiple Shipping Addresses involved. |
| Required        | False                          |


| Parameters      | Description                    |
|------------------|---------------------------------|
| Name            | Comments                       |
| Type            | string                         |
| Description     | Comments of the order.         |
| Required        | False                          |


| Parameters      | Description                    |
|------------------|---------------------------------|
| Name            | LineItemCount                  |
| Type            | integer                        |
| Description     | Line item count of the order.  |
| Required        | False                          |


| Parameters      | Description                    |
|------------------|---------------------------------|
| Name            | Status                         |
| Type            | string                         |
| Description     | Status of the order. Possible values: Unsubmitted, AwaitingApproval, Declined, Open, Completed, Canceled. |
| Required        | False                          |


| Parameters      | Description                    |
|------------------|---------------------------------|
| Name            | DateCreated                    |
| Type            | date                           |
| Description     | Date created of the order.     |
| Required        | False                          |


| Parameters      | Description                    |
|------------------|---------------------------------|
| Name            | DateSubmitted                  |
| Type            | date                           |
| Description     | Date submitted of the order.   |
| Required        | False                          |


| Parameters      | Description                    |
|------------------|---------------------------------|
| Name            | DateApproved                   |
| Type            | date                           |
| Description     | Date approved of the order.    |
| Required        | False                          |


| Parameters      | Description                    |
|------------------|---------------------------------|
| Name            | DateDeclined                   |
| Type            | date                           |
| Description     | Date declined of the order.    |
| Required        | False                          |


| Parameters      | Description                    |
|------------------|---------------------------------|
| Name            | DateCanceled                   |
| Type            | date                           |
| Description     | Date canceled of the order.    |
| Required        | False                          |


| Parameters      | Description                    |
|------------------|---------------------------------|
| Name            | DateCompleted                  |
| Type            | date                           |
| Description     | Date completed of the order.   |
| Required        | False                          |


| Parameters      | Description                    |
|------------------|---------------------------------|
| Name            | Subtotal                       |
| Type            | float                          |
| Description     | Subtotal of the order.         |
| Required        | False                          |


| Parameters      | Description                    |
|------------------|---------------------------------|
| Name            | ShippingCost                   |
| Type            | float                          |
| Description     | Shipping cost of the order.    |
| Required        | False                          |


| Parameters      | Description                    |
|------------------|---------------------------------|
| Name            | TaxCost                        |
| Type            | float                          |
| Description     | Tax cost of the order.         |
| Required        | False                          |


| Parameters      | Description                    |
|------------------|---------------------------------|
| Name            | PromotionDiscount              |
| Type            | float                          |
| Description     | Promotion discount of the order. |
| Required        | False                          |


| Parameters      | Description                    |
|------------------|---------------------------------|
| Name            | Total                          |
| Type            | float                          |
| Description     | Total of the order.            |
| Required        | False                          |


| Parameters      | Description                    |
|------------------|---------------------------------|
| Name            | IsSubmitted                    |
| Type            | boolean                        |
| Description     | True if this Order has been passed from the Buyer to the Seller. |
| Required        | False                          |


| Parameters      | Description                    |
|------------------|---------------------------------|
| Name            | xp                             |
| Type            | object                         |
| Description     | Container for extended (custom) properties of the order. |
| Required        | False                          |

## `POST` `v1/orders/{direction}`
Create a new order

| Parameters      | Description                    |
|------------------|---------------------------------|


| Parameters      | Description                    |
|------------------|---------------------------------|
| Name            | direction                      |
| Type            | string                         |
| Description     | Direction of the order, from the current user's perspective. Possible values: incoming, outgoing. |
| Required        | True                           |

## Requestbody
```
{'ID': '', 'FromCompanyID': '', 'FromUserID': '', 'BillingAddressID': '', 'ShippingAddressID': '', 'Comments': '', 'ShippingCost': 0, 'TaxCost': 0, 'xp': {}}
```

```
[{'Name': 'ID', 'Type': 'string', 'Description': 'ID of the order. Can only contain characters Aa-Zz, 0-9, -, and _. Searchable: priority level 1. Sortable.', 'Required': False}, {'Name': 'FromCompanyID', 'Type': 'string', 'Description': 'ID of the from company. Searchable: priority level 2. Sortable.', 'Required': False}, {'Name': 'FromUserID', 'Type': 'string', 'Description': 'ID of the from user. Sortable.', 'Required': False}, {'Name': 'BillingAddressID', 'Type': 'string', 'Description': 'ID of the billing address.', 'Required': False}, {'Name': 'ShippingAddressID', 'Type': 'string', 'Description': 'ID of the Shipping Address for all LineItems on the Order. Null when there are multiple Shipping Addresses involved.', 'Required': False}, {'Name': 'Comments', 'Type': 'string', 'Description': 'Comments of the order. Max length 2000 characters. Searchable: priority level 4.', 'Required': False}, {'Name': 'ShippingCost', 'Type': 'float', 'Description': 'Shipping cost of the order. Sortable.', 'Required': False}, {'Name': 'TaxCost', 'Type': 'float', 'Description': 'Tax cost of the order. Sortable.', 'Required': False}, {'Name': 'xp', 'Type': 'object', 'Description': 'Container for extended (custom) properties of the order.', 'Required': False}]
```

**Responsestatus**: `201`

## Responsebody
```
{'ID': '', 'FromUser': {'ID': '', 'Username': '', 'FirstName': '', 'LastName': '', 'Email': '', 'Phone': '', 'TermsAccepted': '2018-03-21T23:00:00+00:00', 'Active': False, 'xp': {}, 'AvailableRoles': ['']}, 'FromCompanyID': '', 'FromUserID': '', 'BillingAddressID': '', 'BillingAddress': {'ID': '', 'DateCreated': '2018-03-21T23:00:00+00:00', 'CompanyName': '', 'FirstName': '', 'LastName': '', 'Street1': '', 'Street2': '', 'City': '', 'State': '', 'Zip': '', 'Country': '', 'Phone': '', 'AddressName': '', 'xp': {}}, 'ShippingAddressID': '', 'Comments': '', 'LineItemCount': 0, 'Status': 'Unsubmitted', 'DateCreated': '2018-03-21T23:00:00+00:00', 'DateSubmitted': '2018-03-21T23:00:00+00:00', 'DateApproved': '2018-03-21T23:00:00+00:00', 'DateDeclined': '2018-03-21T23:00:00+00:00', 'DateCanceled': '2018-03-21T23:00:00+00:00', 'DateCompleted': '2018-03-21T23:00:00+00:00', 'Subtotal': 0, 'ShippingCost': 0, 'TaxCost': 0, 'PromotionDiscount': 0, 'Total': 0, 'IsSubmitted': False, 'xp': {}}
```


| Parameters      | Description                    |
|------------------|---------------------------------|
| Name            | ID                             |
| Type            | string                         |
| Description     | ID of the order.               |
| Required        | False                          |


| Parameters      | Description                    |
|------------------|---------------------------------|
| Name            | FromUser                       |
| Type            | object                         |
| Description     | From user of the order.        |
| Required        | False                          |


| Parameters      | Description                    |
|------------------|---------------------------------|
| Name            | FromCompanyID                  |
| Type            | string                         |
| Description     | ID of the from company.        |
| Required        | False                          |


| Parameters      | Description                    |
|------------------|---------------------------------|
| Name            | FromUserID                     |
| Type            | string                         |
| Description     | ID of the from user.           |
| Required        | False                          |


| Parameters      | Description                    |
|------------------|---------------------------------|
| Name            | BillingAddressID               |
| Type            | string                         |
| Description     | ID of the billing address.     |
| Required        | False                          |


| Parameters      | Description                    |
|------------------|---------------------------------|
| Name            | BillingAddress                 |
| Type            | object                         |
| Description     | Billing address of the order.  |
| Required        | False                          |


| Parameters      | Description                    |
|------------------|---------------------------------|
| Name            | ShippingAddressID              |
| Type            | string                         |
| Description     | ID of the Shipping Address for all LineItems on the Order. Null when there are multiple Shipping Addresses involved. |
| Required        | False                          |


| Parameters      | Description                    |
|------------------|---------------------------------|
| Name            | Comments                       |
| Type            | string                         |
| Description     | Comments of the order.         |
| Required        | False                          |


| Parameters      | Description                    |
|------------------|---------------------------------|
| Name            | LineItemCount                  |
| Type            | integer                        |
| Description     | Line item count of the order.  |
| Required        | False                          |


| Parameters      | Description                    |
|------------------|---------------------------------|
| Name            | Status                         |
| Type            | string                         |
| Description     | Status of the order. Possible values: Unsubmitted, AwaitingApproval, Declined, Open, Completed, Canceled. |
| Required        | False                          |


| Parameters      | Description                    |
|------------------|---------------------------------|
| Name            | DateCreated                    |
| Type            | date                           |
| Description     | Date created of the order.     |
| Required        | False                          |


| Parameters      | Description                    |
|------------------|---------------------------------|
| Name            | DateSubmitted                  |
| Type            | date                           |
| Description     | Date submitted of the order.   |
| Required        | False                          |


| Parameters      | Description                    |
|------------------|---------------------------------|
| Name            | DateApproved                   |
| Type            | date                           |
| Description     | Date approved of the order.    |
| Required        | False                          |


| Parameters      | Description                    |
|------------------|---------------------------------|
| Name            | DateDeclined                   |
| Type            | date                           |
| Description     | Date declined of the order.    |
| Required        | False                          |


| Parameters      | Description                    |
|------------------|---------------------------------|
| Name            | DateCanceled                   |
| Type            | date                           |
| Description     | Date canceled of the order.    |
| Required        | False                          |


| Parameters      | Description                    |
|------------------|---------------------------------|
| Name            | DateCompleted                  |
| Type            | date                           |
| Description     | Date completed of the order.   |
| Required        | False                          |


| Parameters      | Description                    |
|------------------|---------------------------------|
| Name            | Subtotal                       |
| Type            | float                          |
| Description     | Subtotal of the order.         |
| Required        | False                          |


| Parameters      | Description                    |
|------------------|---------------------------------|
| Name            | ShippingCost                   |
| Type            | float                          |
| Description     | Shipping cost of the order.    |
| Required        | False                          |


| Parameters      | Description                    |
|------------------|---------------------------------|
| Name            | TaxCost                        |
| Type            | float                          |
| Description     | Tax cost of the order.         |
| Required        | False                          |


| Parameters      | Description                    |
|------------------|---------------------------------|
| Name            | PromotionDiscount              |
| Type            | float                          |
| Description     | Promotion discount of the order. |
| Required        | False                          |


| Parameters      | Description                    |
|------------------|---------------------------------|
| Name            | Total                          |
| Type            | float                          |
| Description     | Total of the order.            |
| Required        | False                          |


| Parameters      | Description                    |
|------------------|---------------------------------|
| Name            | IsSubmitted                    |
| Type            | boolean                        |
| Description     | True if this Order has been passed from the Buyer to the Seller. |
| Required        | False                          |


| Parameters      | Description                    |
|------------------|---------------------------------|
| Name            | xp                             |
| Type            | object                         |
| Description     | Container for extended (custom) properties of the order. |
| Required        | False                          |

## `PUT` `v1/orders/{direction}/{orderID}`
Create or update an order

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
{'ID': '', 'FromCompanyID': '', 'FromUserID': '', 'BillingAddressID': '', 'ShippingAddressID': '', 'Comments': '', 'ShippingCost': 0, 'TaxCost': 0, 'xp': {}}
```

```
[{'Name': 'ID', 'Type': 'string', 'Description': 'ID of the order. Can only contain characters Aa-Zz, 0-9, -, and _. Searchable: priority level 1. Sortable.', 'Required': False}, {'Name': 'FromCompanyID', 'Type': 'string', 'Description': 'ID of the from company. Searchable: priority level 2. Sortable.', 'Required': False}, {'Name': 'FromUserID', 'Type': 'string', 'Description': 'ID of the from user. Sortable.', 'Required': False}, {'Name': 'BillingAddressID', 'Type': 'string', 'Description': 'ID of the billing address.', 'Required': False}, {'Name': 'ShippingAddressID', 'Type': 'string', 'Description': 'ID of the Shipping Address for all LineItems on the Order. Null when there are multiple Shipping Addresses involved.', 'Required': False}, {'Name': 'Comments', 'Type': 'string', 'Description': 'Comments of the order. Max length 2000 characters. Searchable: priority level 4.', 'Required': False}, {'Name': 'ShippingCost', 'Type': 'float', 'Description': 'Shipping cost of the order. Sortable.', 'Required': False}, {'Name': 'TaxCost', 'Type': 'float', 'Description': 'Tax cost of the order. Sortable.', 'Required': False}, {'Name': 'xp', 'Type': 'object', 'Description': 'Container for extended (custom) properties of the order.', 'Required': False}]
```

**Responsestatus**: `200`

## Responsebody
```
{'ID': '', 'FromUser': {'ID': '', 'Username': '', 'FirstName': '', 'LastName': '', 'Email': '', 'Phone': '', 'TermsAccepted': '2018-03-21T23:00:00+00:00', 'Active': False, 'xp': {}, 'AvailableRoles': ['']}, 'FromCompanyID': '', 'FromUserID': '', 'BillingAddressID': '', 'BillingAddress': {'ID': '', 'DateCreated': '2018-03-21T23:00:00+00:00', 'CompanyName': '', 'FirstName': '', 'LastName': '', 'Street1': '', 'Street2': '', 'City': '', 'State': '', 'Zip': '', 'Country': '', 'Phone': '', 'AddressName': '', 'xp': {}}, 'ShippingAddressID': '', 'Comments': '', 'LineItemCount': 0, 'Status': 'Unsubmitted', 'DateCreated': '2018-03-21T23:00:00+00:00', 'DateSubmitted': '2018-03-21T23:00:00+00:00', 'DateApproved': '2018-03-21T23:00:00+00:00', 'DateDeclined': '2018-03-21T23:00:00+00:00', 'DateCanceled': '2018-03-21T23:00:00+00:00', 'DateCompleted': '2018-03-21T23:00:00+00:00', 'Subtotal': 0, 'ShippingCost': 0, 'TaxCost': 0, 'PromotionDiscount': 0, 'Total': 0, 'IsSubmitted': False, 'xp': {}}
```


| Parameters      | Description                    |
|------------------|---------------------------------|
| Name            | ID                             |
| Type            | string                         |
| Description     | ID of the order.               |
| Required        | False                          |


| Parameters      | Description                    |
|------------------|---------------------------------|
| Name            | FromUser                       |
| Type            | object                         |
| Description     | From user of the order.        |
| Required        | False                          |


| Parameters      | Description                    |
|------------------|---------------------------------|
| Name            | FromCompanyID                  |
| Type            | string                         |
| Description     | ID of the from company.        |
| Required        | False                          |


| Parameters      | Description                    |
|------------------|---------------------------------|
| Name            | FromUserID                     |
| Type            | string                         |
| Description     | ID of the from user.           |
| Required        | False                          |


| Parameters      | Description                    |
|------------------|---------------------------------|
| Name            | BillingAddressID               |
| Type            | string                         |
| Description     | ID of the billing address.     |
| Required        | False                          |


| Parameters      | Description                    |
|------------------|---------------------------------|
| Name            | BillingAddress                 |
| Type            | object                         |
| Description     | Billing address of the order.  |
| Required        | False                          |


| Parameters      | Description                    |
|------------------|---------------------------------|
| Name            | ShippingAddressID              |
| Type            | string                         |
| Description     | ID of the Shipping Address for all LineItems on the Order. Null when there are multiple Shipping Addresses involved. |
| Required        | False                          |


| Parameters      | Description                    |
|------------------|---------------------------------|
| Name            | Comments                       |
| Type            | string                         |
| Description     | Comments of the order.         |
| Required        | False                          |


| Parameters      | Description                    |
|------------------|---------------------------------|
| Name            | LineItemCount                  |
| Type            | integer                        |
| Description     | Line item count of the order.  |
| Required        | False                          |


| Parameters      | Description                    |
|------------------|---------------------------------|
| Name            | Status                         |
| Type            | string                         |
| Description     | Status of the order. Possible values: Unsubmitted, AwaitingApproval, Declined, Open, Completed, Canceled. |
| Required        | False                          |


| Parameters      | Description                    |
|------------------|---------------------------------|
| Name            | DateCreated                    |
| Type            | date                           |
| Description     | Date created of the order.     |
| Required        | False                          |


| Parameters      | Description                    |
|------------------|---------------------------------|
| Name            | DateSubmitted                  |
| Type            | date                           |
| Description     | Date submitted of the order.   |
| Required        | False                          |


| Parameters      | Description                    |
|------------------|---------------------------------|
| Name            | DateApproved                   |
| Type            | date                           |
| Description     | Date approved of the order.    |
| Required        | False                          |


| Parameters      | Description                    |
|------------------|---------------------------------|
| Name            | DateDeclined                   |
| Type            | date                           |
| Description     | Date declined of the order.    |
| Required        | False                          |


| Parameters      | Description                    |
|------------------|---------------------------------|
| Name            | DateCanceled                   |
| Type            | date                           |
| Description     | Date canceled of the order.    |
| Required        | False                          |


| Parameters      | Description                    |
|------------------|---------------------------------|
| Name            | DateCompleted                  |
| Type            | date                           |
| Description     | Date completed of the order.   |
| Required        | False                          |


| Parameters      | Description                    |
|------------------|---------------------------------|
| Name            | Subtotal                       |
| Type            | float                          |
| Description     | Subtotal of the order.         |
| Required        | False                          |


| Parameters      | Description                    |
|------------------|---------------------------------|
| Name            | ShippingCost                   |
| Type            | float                          |
| Description     | Shipping cost of the order.    |
| Required        | False                          |


| Parameters      | Description                    |
|------------------|---------------------------------|
| Name            | TaxCost                        |
| Type            | float                          |
| Description     | Tax cost of the order.         |
| Required        | False                          |


| Parameters      | Description                    |
|------------------|---------------------------------|
| Name            | PromotionDiscount              |
| Type            | float                          |
| Description     | Promotion discount of the order. |
| Required        | False                          |


| Parameters      | Description                    |
|------------------|---------------------------------|
| Name            | Total                          |
| Type            | float                          |
| Description     | Total of the order.            |
| Required        | False                          |


| Parameters      | Description                    |
|------------------|---------------------------------|
| Name            | IsSubmitted                    |
| Type            | boolean                        |
| Description     | True if this Order has been passed from the Buyer to the Seller. |
| Required        | False                          |


| Parameters      | Description                    |
|------------------|---------------------------------|
| Name            | xp                             |
| Type            | object                         |
| Description     | Container for extended (custom) properties of the order. |
| Required        | False                          |

## `DELETE` `v1/orders/{direction}/{orderID}`
Delete an order

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
**Responsestatus**: `204`

## Responsebody
## `GET` `v1/orders/{direction}/{orderID}/approvals`
Get a list of order approvals

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
{'Meta': {'Page': 1, 'PageSize': 20, 'TotalCount': 25, 'TotalPages': 2, 'ItemRange': [1, 20]}, 'Items': [{'ApprovalRuleID': '', 'ApprovingGroupID': '', 'Status': 'Pending', 'DateCreated': '2018-03-21T23:00:00+00:00', 'DateCompleted': '2018-03-21T23:00:00+00:00', 'Approver': {'ID': '', 'Username': '', 'FirstName': '', 'LastName': '', 'Email': '', 'Phone': '', 'TermsAccepted': '2018-03-21T23:00:00+00:00', 'Active': False, 'xp': {}, 'AvailableRoles': ['']}, 'Comments': ''}]}
```


| Parameters      | Description                    |
|------------------|---------------------------------|
| Name            | ApprovalRuleID                 |
| Type            | string                         |
| Description     | ID of the approval rule.       |
| Required        | False                          |


| Parameters      | Description                    |
|------------------|---------------------------------|
| Name            | ApprovingGroupID               |
| Type            | string                         |
| Description     | ID of the approving group.     |
| Required        | False                          |


| Parameters      | Description                    |
|------------------|---------------------------------|
| Name            | Status                         |
| Type            | string                         |
| Description     | Status of the order approval. Possible values: Pending, Approved, Declined. |
| Required        | False                          |


| Parameters      | Description                    |
|------------------|---------------------------------|
| Name            | DateCreated                    |
| Type            | date                           |
| Description     | Date created of the order approval. |
| Required        | False                          |


| Parameters      | Description                    |
|------------------|---------------------------------|
| Name            | DateCompleted                  |
| Type            | date                           |
| Description     | Date completed of the order approval. |
| Required        | False                          |


| Parameters      | Description                    |
|------------------|---------------------------------|
| Name            | Approver                       |
| Type            | object                         |
| Description     | Approver of the order approval. |
| Required        | False                          |


| Parameters      | Description                    |
|------------------|---------------------------------|
| Name            | Comments                       |
| Type            | string                         |
| Description     | Comments of the order approval. |
| Required        | False                          |

## `GET` `v1/orders/{direction}/{orderID}/eligibleapprovers`
Get a list of order eligible approvers

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
{'Meta': {'Page': 1, 'PageSize': 20, 'TotalCount': 25, 'TotalPages': 2, 'ItemRange': [1, 20]}, 'Items': [{'ID': '', 'Username': '', 'FirstName': '', 'LastName': '', 'Email': '', 'Phone': '', 'TermsAccepted': '2018-03-21T23:00:00+00:00', 'Active': False, 'xp': {}, 'AvailableRoles': ['']}]}
```


| Parameters      | Description                    |
|------------------|---------------------------------|
| Name            | ID                             |
| Type            | string                         |
| Description     | ID of the user.                |
| Required        | False                          |


| Parameters      | Description                    |
|------------------|---------------------------------|
| Name            | Username                       |
| Type            | string                         |
| Description     | Username of the user.          |
| Required        | True                           |


| Parameters      | Description                    |
|------------------|---------------------------------|
| Name            | FirstName                      |
| Type            | string                         |
| Description     | First name of the user.        |
| Required        | True                           |


| Parameters      | Description                    |
|------------------|---------------------------------|
| Name            | LastName                       |
| Type            | string                         |
| Description     | Last name of the user.         |
| Required        | True                           |


| Parameters      | Description                    |
|------------------|---------------------------------|
| Name            | Email                          |
| Type            | string                         |
| Description     | Email of the user.             |
| Required        | True                           |


| Parameters      | Description                    |
|------------------|---------------------------------|
| Name            | Phone                          |
| Type            | string                         |
| Description     | Phone of the user.             |
| Required        | False                          |


| Parameters      | Description                    |
|------------------|---------------------------------|
| Name            | TermsAccepted                  |
| Type            | date                           |
| Description     | Terms accepted of the user.    |
| Required        | False                          |


| Parameters      | Description                    |
|------------------|---------------------------------|
| Name            | Active                         |
| Type            | boolean                        |
| Description     | Active of the user.            |
| Required        | True                           |


| Parameters      | Description                    |
|------------------|---------------------------------|
| Name            | xp                             |
| Type            | object                         |
| Description     | Container for extended (custom) properties of the user. |
| Required        | False                          |


| Parameters      | Description                    |
|------------------|---------------------------------|
| Name            | AvailableRoles                 |
| Type            | array                          |
| Description     | Available roles of the user.   |
| Required        | False                          |

## `PATCH` `v1/orders/{direction}/{orderID}`
Partially update an order

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
{'ID': '', 'FromCompanyID': '', 'FromUserID': '', 'BillingAddressID': '', 'ShippingAddressID': '', 'Comments': '', 'ShippingCost': 0, 'TaxCost': 0, 'xp': {}}
```

```
[{'Name': 'ID', 'Type': 'string', 'Description': 'ID of the order. Can only contain characters Aa-Zz, 0-9, -, and _. Searchable: priority level 1. Sortable.', 'Required': False}, {'Name': 'FromCompanyID', 'Type': 'string', 'Description': 'ID of the from company. Searchable: priority level 2. Sortable.', 'Required': False}, {'Name': 'FromUserID', 'Type': 'string', 'Description': 'ID of the from user. Sortable.', 'Required': False}, {'Name': 'BillingAddressID', 'Type': 'string', 'Description': 'ID of the billing address.', 'Required': False}, {'Name': 'ShippingAddressID', 'Type': 'string', 'Description': 'ID of the Shipping Address for all LineItems on the Order. Null when there are multiple Shipping Addresses involved.', 'Required': False}, {'Name': 'Comments', 'Type': 'string', 'Description': 'Comments of the order. Max length 2000 characters. Searchable: priority level 4.', 'Required': False}, {'Name': 'ShippingCost', 'Type': 'float', 'Description': 'Shipping cost of the order. Sortable.', 'Required': False}, {'Name': 'TaxCost', 'Type': 'float', 'Description': 'Tax cost of the order. Sortable.', 'Required': False}, {'Name': 'xp', 'Type': 'object', 'Description': 'Container for extended (custom) properties of the order.', 'Required': False}]
```

**Responsestatus**: `200`

## Responsebody
```
{'ID': '', 'FromUser': {'ID': '', 'Username': '', 'FirstName': '', 'LastName': '', 'Email': '', 'Phone': '', 'TermsAccepted': '2018-03-21T23:00:00+00:00', 'Active': False, 'xp': {}, 'AvailableRoles': ['']}, 'FromCompanyID': '', 'FromUserID': '', 'BillingAddressID': '', 'BillingAddress': {'ID': '', 'DateCreated': '2018-03-21T23:00:00+00:00', 'CompanyName': '', 'FirstName': '', 'LastName': '', 'Street1': '', 'Street2': '', 'City': '', 'State': '', 'Zip': '', 'Country': '', 'Phone': '', 'AddressName': '', 'xp': {}}, 'ShippingAddressID': '', 'Comments': '', 'LineItemCount': 0, 'Status': 'Unsubmitted', 'DateCreated': '2018-03-21T23:00:00+00:00', 'DateSubmitted': '2018-03-21T23:00:00+00:00', 'DateApproved': '2018-03-21T23:00:00+00:00', 'DateDeclined': '2018-03-21T23:00:00+00:00', 'DateCanceled': '2018-03-21T23:00:00+00:00', 'DateCompleted': '2018-03-21T23:00:00+00:00', 'Subtotal': 0, 'ShippingCost': 0, 'TaxCost': 0, 'PromotionDiscount': 0, 'Total': 0, 'IsSubmitted': False, 'xp': {}}
```


| Parameters      | Description                    |
|------------------|---------------------------------|
| Name            | ID                             |
| Type            | string                         |
| Description     | ID of the order.               |
| Required        | False                          |


| Parameters      | Description                    |
|------------------|---------------------------------|
| Name            | FromUser                       |
| Type            | object                         |
| Description     | From user of the order.        |
| Required        | False                          |


| Parameters      | Description                    |
|------------------|---------------------------------|
| Name            | FromCompanyID                  |
| Type            | string                         |
| Description     | ID of the from company.        |
| Required        | False                          |


| Parameters      | Description                    |
|------------------|---------------------------------|
| Name            | FromUserID                     |
| Type            | string                         |
| Description     | ID of the from user.           |
| Required        | False                          |


| Parameters      | Description                    |
|------------------|---------------------------------|
| Name            | BillingAddressID               |
| Type            | string                         |
| Description     | ID of the billing address.     |
| Required        | False                          |


| Parameters      | Description                    |
|------------------|---------------------------------|
| Name            | BillingAddress                 |
| Type            | object                         |
| Description     | Billing address of the order.  |
| Required        | False                          |


| Parameters      | Description                    |
|------------------|---------------------------------|
| Name            | ShippingAddressID              |
| Type            | string                         |
| Description     | ID of the Shipping Address for all LineItems on the Order. Null when there are multiple Shipping Addresses involved. |
| Required        | False                          |


| Parameters      | Description                    |
|------------------|---------------------------------|
| Name            | Comments                       |
| Type            | string                         |
| Description     | Comments of the order.         |
| Required        | False                          |


| Parameters      | Description                    |
|------------------|---------------------------------|
| Name            | LineItemCount                  |
| Type            | integer                        |
| Description     | Line item count of the order.  |
| Required        | False                          |


| Parameters      | Description                    |
|------------------|---------------------------------|
| Name            | Status                         |
| Type            | string                         |
| Description     | Status of the order. Possible values: Unsubmitted, AwaitingApproval, Declined, Open, Completed, Canceled. |
| Required        | False                          |


| Parameters      | Description                    |
|------------------|---------------------------------|
| Name            | DateCreated                    |
| Type            | date                           |
| Description     | Date created of the order.     |
| Required        | False                          |


| Parameters      | Description                    |
|------------------|---------------------------------|
| Name            | DateSubmitted                  |
| Type            | date                           |
| Description     | Date submitted of the order.   |
| Required        | False                          |


| Parameters      | Description                    |
|------------------|---------------------------------|
| Name            | DateApproved                   |
| Type            | date                           |
| Description     | Date approved of the order.    |
| Required        | False                          |


| Parameters      | Description                    |
|------------------|---------------------------------|
| Name            | DateDeclined                   |
| Type            | date                           |
| Description     | Date declined of the order.    |
| Required        | False                          |


| Parameters      | Description                    |
|------------------|---------------------------------|
| Name            | DateCanceled                   |
| Type            | date                           |
| Description     | Date canceled of the order.    |
| Required        | False                          |


| Parameters      | Description                    |
|------------------|---------------------------------|
| Name            | DateCompleted                  |
| Type            | date                           |
| Description     | Date completed of the order.   |
| Required        | False                          |


| Parameters      | Description                    |
|------------------|---------------------------------|
| Name            | Subtotal                       |
| Type            | float                          |
| Description     | Subtotal of the order.         |
| Required        | False                          |


| Parameters      | Description                    |
|------------------|---------------------------------|
| Name            | ShippingCost                   |
| Type            | float                          |
| Description     | Shipping cost of the order.    |
| Required        | False                          |


| Parameters      | Description                    |
|------------------|---------------------------------|
| Name            | TaxCost                        |
| Type            | float                          |
| Description     | Tax cost of the order.         |
| Required        | False                          |


| Parameters      | Description                    |
|------------------|---------------------------------|
| Name            | PromotionDiscount              |
| Type            | float                          |
| Description     | Promotion discount of the order. |
| Required        | False                          |


| Parameters      | Description                    |
|------------------|---------------------------------|
| Name            | Total                          |
| Type            | float                          |
| Description     | Total of the order.            |
| Required        | False                          |


| Parameters      | Description                    |
|------------------|---------------------------------|
| Name            | IsSubmitted                    |
| Type            | boolean                        |
| Description     | True if this Order has been passed from the Buyer to the Seller. |
| Required        | False                          |


| Parameters      | Description                    |
|------------------|---------------------------------|
| Name            | xp                             |
| Type            | object                         |
| Description     | Container for extended (custom) properties of the order. |
| Required        | False                          |

## `POST` `v1/orders/{direction}/{orderID}/submit`
Submit an order submit

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
**Responsestatus**: `201`

## Responsebody
```
{'ID': '', 'FromUser': {'ID': '', 'Username': '', 'FirstName': '', 'LastName': '', 'Email': '', 'Phone': '', 'TermsAccepted': '2018-03-21T23:00:00+00:00', 'Active': False, 'xp': {}, 'AvailableRoles': ['']}, 'FromCompanyID': '', 'FromUserID': '', 'BillingAddressID': '', 'BillingAddress': {'ID': '', 'DateCreated': '2018-03-21T23:00:00+00:00', 'CompanyName': '', 'FirstName': '', 'LastName': '', 'Street1': '', 'Street2': '', 'City': '', 'State': '', 'Zip': '', 'Country': '', 'Phone': '', 'AddressName': '', 'xp': {}}, 'ShippingAddressID': '', 'Comments': '', 'LineItemCount': 0, 'Status': 'Unsubmitted', 'DateCreated': '2018-03-21T23:00:00+00:00', 'DateSubmitted': '2018-03-21T23:00:00+00:00', 'DateApproved': '2018-03-21T23:00:00+00:00', 'DateDeclined': '2018-03-21T23:00:00+00:00', 'DateCanceled': '2018-03-21T23:00:00+00:00', 'DateCompleted': '2018-03-21T23:00:00+00:00', 'Subtotal': 0, 'ShippingCost': 0, 'TaxCost': 0, 'PromotionDiscount': 0, 'Total': 0, 'IsSubmitted': False, 'xp': {}}
```


| Parameters      | Description                    |
|------------------|---------------------------------|
| Name            | ID                             |
| Type            | string                         |
| Description     | ID of the order.               |
| Required        | False                          |


| Parameters      | Description                    |
|------------------|---------------------------------|
| Name            | FromUser                       |
| Type            | object                         |
| Description     | From user of the order.        |
| Required        | False                          |


| Parameters      | Description                    |
|------------------|---------------------------------|
| Name            | FromCompanyID                  |
| Type            | string                         |
| Description     | ID of the from company.        |
| Required        | False                          |


| Parameters      | Description                    |
|------------------|---------------------------------|
| Name            | FromUserID                     |
| Type            | string                         |
| Description     | ID of the from user.           |
| Required        | False                          |


| Parameters      | Description                    |
|------------------|---------------------------------|
| Name            | BillingAddressID               |
| Type            | string                         |
| Description     | ID of the billing address.     |
| Required        | False                          |


| Parameters      | Description                    |
|------------------|---------------------------------|
| Name            | BillingAddress                 |
| Type            | object                         |
| Description     | Billing address of the order.  |
| Required        | False                          |


| Parameters      | Description                    |
|------------------|---------------------------------|
| Name            | ShippingAddressID              |
| Type            | string                         |
| Description     | ID of the Shipping Address for all LineItems on the Order. Null when there are multiple Shipping Addresses involved. |
| Required        | False                          |


| Parameters      | Description                    |
|------------------|---------------------------------|
| Name            | Comments                       |
| Type            | string                         |
| Description     | Comments of the order.         |
| Required        | False                          |


| Parameters      | Description                    |
|------------------|---------------------------------|
| Name            | LineItemCount                  |
| Type            | integer                        |
| Description     | Line item count of the order.  |
| Required        | False                          |


| Parameters      | Description                    |
|------------------|---------------------------------|
| Name            | Status                         |
| Type            | string                         |
| Description     | Status of the order. Possible values: Unsubmitted, AwaitingApproval, Declined, Open, Completed, Canceled. |
| Required        | False                          |


| Parameters      | Description                    |
|------------------|---------------------------------|
| Name            | DateCreated                    |
| Type            | date                           |
| Description     | Date created of the order.     |
| Required        | False                          |


| Parameters      | Description                    |
|------------------|---------------------------------|
| Name            | DateSubmitted                  |
| Type            | date                           |
| Description     | Date submitted of the order.   |
| Required        | False                          |


| Parameters      | Description                    |
|------------------|---------------------------------|
| Name            | DateApproved                   |
| Type            | date                           |
| Description     | Date approved of the order.    |
| Required        | False                          |


| Parameters      | Description                    |
|------------------|---------------------------------|
| Name            | DateDeclined                   |
| Type            | date                           |
| Description     | Date declined of the order.    |
| Required        | False                          |


| Parameters      | Description                    |
|------------------|---------------------------------|
| Name            | DateCanceled                   |
| Type            | date                           |
| Description     | Date canceled of the order.    |
| Required        | False                          |


| Parameters      | Description                    |
|------------------|---------------------------------|
| Name            | DateCompleted                  |
| Type            | date                           |
| Description     | Date completed of the order.   |
| Required        | False                          |


| Parameters      | Description                    |
|------------------|---------------------------------|
| Name            | Subtotal                       |
| Type            | float                          |
| Description     | Subtotal of the order.         |
| Required        | False                          |


| Parameters      | Description                    |
|------------------|---------------------------------|
| Name            | ShippingCost                   |
| Type            | float                          |
| Description     | Shipping cost of the order.    |
| Required        | False                          |


| Parameters      | Description                    |
|------------------|---------------------------------|
| Name            | TaxCost                        |
| Type            | float                          |
| Description     | Tax cost of the order.         |
| Required        | False                          |


| Parameters      | Description                    |
|------------------|---------------------------------|
| Name            | PromotionDiscount              |
| Type            | float                          |
| Description     | Promotion discount of the order. |
| Required        | False                          |


| Parameters      | Description                    |
|------------------|---------------------------------|
| Name            | Total                          |
| Type            | float                          |
| Description     | Total of the order.            |
| Required        | False                          |


| Parameters      | Description                    |
|------------------|---------------------------------|
| Name            | IsSubmitted                    |
| Type            | boolean                        |
| Description     | True if this Order has been passed from the Buyer to the Seller. |
| Required        | False                          |


| Parameters      | Description                    |
|------------------|---------------------------------|
| Name            | xp                             |
| Type            | object                         |
| Description     | Container for extended (custom) properties of the order. |
| Required        | False                          |

## `POST` `v1/orders/{direction}/{orderID}/approve`
Approve an order approve

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
{'Comments': '', 'AllowResubmit': False}
```

```
[{'Name': 'Comments', 'Type': 'string', 'Description': 'Comments of the order approval info. Max length 2000 characters.', 'Required': False}, {'Name': 'AllowResubmit', 'Type': 'boolean', 'Description': 'Allow resubmit of the order approval info.', 'Required': False}]
```

**Responsestatus**: `201`

## Responsebody
```
{'ID': '', 'FromUser': {'ID': '', 'Username': '', 'FirstName': '', 'LastName': '', 'Email': '', 'Phone': '', 'TermsAccepted': '2018-03-21T23:00:00+00:00', 'Active': False, 'xp': {}, 'AvailableRoles': ['']}, 'FromCompanyID': '', 'FromUserID': '', 'BillingAddressID': '', 'BillingAddress': {'ID': '', 'DateCreated': '2018-03-21T23:00:00+00:00', 'CompanyName': '', 'FirstName': '', 'LastName': '', 'Street1': '', 'Street2': '', 'City': '', 'State': '', 'Zip': '', 'Country': '', 'Phone': '', 'AddressName': '', 'xp': {}}, 'ShippingAddressID': '', 'Comments': '', 'LineItemCount': 0, 'Status': 'Unsubmitted', 'DateCreated': '2018-03-21T23:00:00+00:00', 'DateSubmitted': '2018-03-21T23:00:00+00:00', 'DateApproved': '2018-03-21T23:00:00+00:00', 'DateDeclined': '2018-03-21T23:00:00+00:00', 'DateCanceled': '2018-03-21T23:00:00+00:00', 'DateCompleted': '2018-03-21T23:00:00+00:00', 'Subtotal': 0, 'ShippingCost': 0, 'TaxCost': 0, 'PromotionDiscount': 0, 'Total': 0, 'IsSubmitted': False, 'xp': {}}
```


| Parameters      | Description                    |
|------------------|---------------------------------|
| Name            | ID                             |
| Type            | string                         |
| Description     | ID of the order.               |
| Required        | False                          |


| Parameters      | Description                    |
|------------------|---------------------------------|
| Name            | FromUser                       |
| Type            | object                         |
| Description     | From user of the order.        |
| Required        | False                          |


| Parameters      | Description                    |
|------------------|---------------------------------|
| Name            | FromCompanyID                  |
| Type            | string                         |
| Description     | ID of the from company.        |
| Required        | False                          |


| Parameters      | Description                    |
|------------------|---------------------------------|
| Name            | FromUserID                     |
| Type            | string                         |
| Description     | ID of the from user.           |
| Required        | False                          |


| Parameters      | Description                    |
|------------------|---------------------------------|
| Name            | BillingAddressID               |
| Type            | string                         |
| Description     | ID of the billing address.     |
| Required        | False                          |


| Parameters      | Description                    |
|------------------|---------------------------------|
| Name            | BillingAddress                 |
| Type            | object                         |
| Description     | Billing address of the order.  |
| Required        | False                          |


| Parameters      | Description                    |
|------------------|---------------------------------|
| Name            | ShippingAddressID              |
| Type            | string                         |
| Description     | ID of the Shipping Address for all LineItems on the Order. Null when there are multiple Shipping Addresses involved. |
| Required        | False                          |


| Parameters      | Description                    |
|------------------|---------------------------------|
| Name            | Comments                       |
| Type            | string                         |
| Description     | Comments of the order.         |
| Required        | False                          |


| Parameters      | Description                    |
|------------------|---------------------------------|
| Name            | LineItemCount                  |
| Type            | integer                        |
| Description     | Line item count of the order.  |
| Required        | False                          |


| Parameters      | Description                    |
|------------------|---------------------------------|
| Name            | Status                         |
| Type            | string                         |
| Description     | Status of the order. Possible values: Unsubmitted, AwaitingApproval, Declined, Open, Completed, Canceled. |
| Required        | False                          |


| Parameters      | Description                    |
|------------------|---------------------------------|
| Name            | DateCreated                    |
| Type            | date                           |
| Description     | Date created of the order.     |
| Required        | False                          |


| Parameters      | Description                    |
|------------------|---------------------------------|
| Name            | DateSubmitted                  |
| Type            | date                           |
| Description     | Date submitted of the order.   |
| Required        | False                          |


| Parameters      | Description                    |
|------------------|---------------------------------|
| Name            | DateApproved                   |
| Type            | date                           |
| Description     | Date approved of the order.    |
| Required        | False                          |


| Parameters      | Description                    |
|------------------|---------------------------------|
| Name            | DateDeclined                   |
| Type            | date                           |
| Description     | Date declined of the order.    |
| Required        | False                          |


| Parameters      | Description                    |
|------------------|---------------------------------|
| Name            | DateCanceled                   |
| Type            | date                           |
| Description     | Date canceled of the order.    |
| Required        | False                          |


| Parameters      | Description                    |
|------------------|---------------------------------|
| Name            | DateCompleted                  |
| Type            | date                           |
| Description     | Date completed of the order.   |
| Required        | False                          |


| Parameters      | Description                    |
|------------------|---------------------------------|
| Name            | Subtotal                       |
| Type            | float                          |
| Description     | Subtotal of the order.         |
| Required        | False                          |


| Parameters      | Description                    |
|------------------|---------------------------------|
| Name            | ShippingCost                   |
| Type            | float                          |
| Description     | Shipping cost of the order.    |
| Required        | False                          |


| Parameters      | Description                    |
|------------------|---------------------------------|
| Name            | TaxCost                        |
| Type            | float                          |
| Description     | Tax cost of the order.         |
| Required        | False                          |


| Parameters      | Description                    |
|------------------|---------------------------------|
| Name            | PromotionDiscount              |
| Type            | float                          |
| Description     | Promotion discount of the order. |
| Required        | False                          |


| Parameters      | Description                    |
|------------------|---------------------------------|
| Name            | Total                          |
| Type            | float                          |
| Description     | Total of the order.            |
| Required        | False                          |


| Parameters      | Description                    |
|------------------|---------------------------------|
| Name            | IsSubmitted                    |
| Type            | boolean                        |
| Description     | True if this Order has been passed from the Buyer to the Seller. |
| Required        | False                          |


| Parameters      | Description                    |
|------------------|---------------------------------|
| Name            | xp                             |
| Type            | object                         |
| Description     | Container for extended (custom) properties of the order. |
| Required        | False                          |

## `POST` `v1/orders/{direction}/{orderID}/decline`
Decline an order decline

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
{'Comments': '', 'AllowResubmit': False}
```

```
[{'Name': 'Comments', 'Type': 'string', 'Description': 'Comments of the order approval info. Max length 2000 characters.', 'Required': False}, {'Name': 'AllowResubmit', 'Type': 'boolean', 'Description': 'Allow resubmit of the order approval info.', 'Required': False}]
```

**Responsestatus**: `201`

## Responsebody
```
{'ID': '', 'FromUser': {'ID': '', 'Username': '', 'FirstName': '', 'LastName': '', 'Email': '', 'Phone': '', 'TermsAccepted': '2018-03-21T23:00:00+00:00', 'Active': False, 'xp': {}, 'AvailableRoles': ['']}, 'FromCompanyID': '', 'FromUserID': '', 'BillingAddressID': '', 'BillingAddress': {'ID': '', 'DateCreated': '2018-03-21T23:00:00+00:00', 'CompanyName': '', 'FirstName': '', 'LastName': '', 'Street1': '', 'Street2': '', 'City': '', 'State': '', 'Zip': '', 'Country': '', 'Phone': '', 'AddressName': '', 'xp': {}}, 'ShippingAddressID': '', 'Comments': '', 'LineItemCount': 0, 'Status': 'Unsubmitted', 'DateCreated': '2018-03-21T23:00:00+00:00', 'DateSubmitted': '2018-03-21T23:00:00+00:00', 'DateApproved': '2018-03-21T23:00:00+00:00', 'DateDeclined': '2018-03-21T23:00:00+00:00', 'DateCanceled': '2018-03-21T23:00:00+00:00', 'DateCompleted': '2018-03-21T23:00:00+00:00', 'Subtotal': 0, 'ShippingCost': 0, 'TaxCost': 0, 'PromotionDiscount': 0, 'Total': 0, 'IsSubmitted': False, 'xp': {}}
```


| Parameters      | Description                    |
|------------------|---------------------------------|
| Name            | ID                             |
| Type            | string                         |
| Description     | ID of the order.               |
| Required        | False                          |


| Parameters      | Description                    |
|------------------|---------------------------------|
| Name            | FromUser                       |
| Type            | object                         |
| Description     | From user of the order.        |
| Required        | False                          |


| Parameters      | Description                    |
|------------------|---------------------------------|
| Name            | FromCompanyID                  |
| Type            | string                         |
| Description     | ID of the from company.        |
| Required        | False                          |


| Parameters      | Description                    |
|------------------|---------------------------------|
| Name            | FromUserID                     |
| Type            | string                         |
| Description     | ID of the from user.           |
| Required        | False                          |


| Parameters      | Description                    |
|------------------|---------------------------------|
| Name            | BillingAddressID               |
| Type            | string                         |
| Description     | ID of the billing address.     |
| Required        | False                          |


| Parameters      | Description                    |
|------------------|---------------------------------|
| Name            | BillingAddress                 |
| Type            | object                         |
| Description     | Billing address of the order.  |
| Required        | False                          |


| Parameters      | Description                    |
|------------------|---------------------------------|
| Name            | ShippingAddressID              |
| Type            | string                         |
| Description     | ID of the Shipping Address for all LineItems on the Order. Null when there are multiple Shipping Addresses involved. |
| Required        | False                          |


| Parameters      | Description                    |
|------------------|---------------------------------|
| Name            | Comments                       |
| Type            | string                         |
| Description     | Comments of the order.         |
| Required        | False                          |


| Parameters      | Description                    |
|------------------|---------------------------------|
| Name            | LineItemCount                  |
| Type            | integer                        |
| Description     | Line item count of the order.  |
| Required        | False                          |


| Parameters      | Description                    |
|------------------|---------------------------------|
| Name            | Status                         |
| Type            | string                         |
| Description     | Status of the order. Possible values: Unsubmitted, AwaitingApproval, Declined, Open, Completed, Canceled. |
| Required        | False                          |


| Parameters      | Description                    |
|------------------|---------------------------------|
| Name            | DateCreated                    |
| Type            | date                           |
| Description     | Date created of the order.     |
| Required        | False                          |


| Parameters      | Description                    |
|------------------|---------------------------------|
| Name            | DateSubmitted                  |
| Type            | date                           |
| Description     | Date submitted of the order.   |
| Required        | False                          |


| Parameters      | Description                    |
|------------------|---------------------------------|
| Name            | DateApproved                   |
| Type            | date                           |
| Description     | Date approved of the order.    |
| Required        | False                          |


| Parameters      | Description                    |
|------------------|---------------------------------|
| Name            | DateDeclined                   |
| Type            | date                           |
| Description     | Date declined of the order.    |
| Required        | False                          |


| Parameters      | Description                    |
|------------------|---------------------------------|
| Name            | DateCanceled                   |
| Type            | date                           |
| Description     | Date canceled of the order.    |
| Required        | False                          |


| Parameters      | Description                    |
|------------------|---------------------------------|
| Name            | DateCompleted                  |
| Type            | date                           |
| Description     | Date completed of the order.   |
| Required        | False                          |


| Parameters      | Description                    |
|------------------|---------------------------------|
| Name            | Subtotal                       |
| Type            | float                          |
| Description     | Subtotal of the order.         |
| Required        | False                          |


| Parameters      | Description                    |
|------------------|---------------------------------|
| Name            | ShippingCost                   |
| Type            | float                          |
| Description     | Shipping cost of the order.    |
| Required        | False                          |


| Parameters      | Description                    |
|------------------|---------------------------------|
| Name            | TaxCost                        |
| Type            | float                          |
| Description     | Tax cost of the order.         |
| Required        | False                          |


| Parameters      | Description                    |
|------------------|---------------------------------|
| Name            | PromotionDiscount              |
| Type            | float                          |
| Description     | Promotion discount of the order. |
| Required        | False                          |


| Parameters      | Description                    |
|------------------|---------------------------------|
| Name            | Total                          |
| Type            | float                          |
| Description     | Total of the order.            |
| Required        | False                          |


| Parameters      | Description                    |
|------------------|---------------------------------|
| Name            | IsSubmitted                    |
| Type            | boolean                        |
| Description     | True if this Order has been passed from the Buyer to the Seller. |
| Required        | False                          |


| Parameters      | Description                    |
|------------------|---------------------------------|
| Name            | xp                             |
| Type            | object                         |
| Description     | Container for extended (custom) properties of the order. |
| Required        | False                          |

## `POST` `v1/orders/{direction}/{orderID}/cancel`
Cancel an order cancel

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
**Responsestatus**: `201`

## Responsebody
```
{'ID': '', 'FromUser': {'ID': '', 'Username': '', 'FirstName': '', 'LastName': '', 'Email': '', 'Phone': '', 'TermsAccepted': '2018-03-21T23:00:00+00:00', 'Active': False, 'xp': {}, 'AvailableRoles': ['']}, 'FromCompanyID': '', 'FromUserID': '', 'BillingAddressID': '', 'BillingAddress': {'ID': '', 'DateCreated': '2018-03-21T23:00:00+00:00', 'CompanyName': '', 'FirstName': '', 'LastName': '', 'Street1': '', 'Street2': '', 'City': '', 'State': '', 'Zip': '', 'Country': '', 'Phone': '', 'AddressName': '', 'xp': {}}, 'ShippingAddressID': '', 'Comments': '', 'LineItemCount': 0, 'Status': 'Unsubmitted', 'DateCreated': '2018-03-21T23:00:00+00:00', 'DateSubmitted': '2018-03-21T23:00:00+00:00', 'DateApproved': '2018-03-21T23:00:00+00:00', 'DateDeclined': '2018-03-21T23:00:00+00:00', 'DateCanceled': '2018-03-21T23:00:00+00:00', 'DateCompleted': '2018-03-21T23:00:00+00:00', 'Subtotal': 0, 'ShippingCost': 0, 'TaxCost': 0, 'PromotionDiscount': 0, 'Total': 0, 'IsSubmitted': False, 'xp': {}}
```


| Parameters      | Description                    |
|------------------|---------------------------------|
| Name            | ID                             |
| Type            | string                         |
| Description     | ID of the order.               |
| Required        | False                          |


| Parameters      | Description                    |
|------------------|---------------------------------|
| Name            | FromUser                       |
| Type            | object                         |
| Description     | From user of the order.        |
| Required        | False                          |


| Parameters      | Description                    |
|------------------|---------------------------------|
| Name            | FromCompanyID                  |
| Type            | string                         |
| Description     | ID of the from company.        |
| Required        | False                          |


| Parameters      | Description                    |
|------------------|---------------------------------|
| Name            | FromUserID                     |
| Type            | string                         |
| Description     | ID of the from user.           |
| Required        | False                          |


| Parameters      | Description                    |
|------------------|---------------------------------|
| Name            | BillingAddressID               |
| Type            | string                         |
| Description     | ID of the billing address.     |
| Required        | False                          |


| Parameters      | Description                    |
|------------------|---------------------------------|
| Name            | BillingAddress                 |
| Type            | object                         |
| Description     | Billing address of the order.  |
| Required        | False                          |


| Parameters      | Description                    |
|------------------|---------------------------------|
| Name            | ShippingAddressID              |
| Type            | string                         |
| Description     | ID of the Shipping Address for all LineItems on the Order. Null when there are multiple Shipping Addresses involved. |
| Required        | False                          |


| Parameters      | Description                    |
|------------------|---------------------------------|
| Name            | Comments                       |
| Type            | string                         |
| Description     | Comments of the order.         |
| Required        | False                          |


| Parameters      | Description                    |
|------------------|---------------------------------|
| Name            | LineItemCount                  |
| Type            | integer                        |
| Description     | Line item count of the order.  |
| Required        | False                          |


| Parameters      | Description                    |
|------------------|---------------------------------|
| Name            | Status                         |
| Type            | string                         |
| Description     | Status of the order. Possible values: Unsubmitted, AwaitingApproval, Declined, Open, Completed, Canceled. |
| Required        | False                          |


| Parameters      | Description                    |
|------------------|---------------------------------|
| Name            | DateCreated                    |
| Type            | date                           |
| Description     | Date created of the order.     |
| Required        | False                          |


| Parameters      | Description                    |
|------------------|---------------------------------|
| Name            | DateSubmitted                  |
| Type            | date                           |
| Description     | Date submitted of the order.   |
| Required        | False                          |


| Parameters      | Description                    |
|------------------|---------------------------------|
| Name            | DateApproved                   |
| Type            | date                           |
| Description     | Date approved of the order.    |
| Required        | False                          |


| Parameters      | Description                    |
|------------------|---------------------------------|
| Name            | DateDeclined                   |
| Type            | date                           |
| Description     | Date declined of the order.    |
| Required        | False                          |


| Parameters      | Description                    |
|------------------|---------------------------------|
| Name            | DateCanceled                   |
| Type            | date                           |
| Description     | Date canceled of the order.    |
| Required        | False                          |


| Parameters      | Description                    |
|------------------|---------------------------------|
| Name            | DateCompleted                  |
| Type            | date                           |
| Description     | Date completed of the order.   |
| Required        | False                          |


| Parameters      | Description                    |
|------------------|---------------------------------|
| Name            | Subtotal                       |
| Type            | float                          |
| Description     | Subtotal of the order.         |
| Required        | False                          |


| Parameters      | Description                    |
|------------------|---------------------------------|
| Name            | ShippingCost                   |
| Type            | float                          |
| Description     | Shipping cost of the order.    |
| Required        | False                          |


| Parameters      | Description                    |
|------------------|---------------------------------|
| Name            | TaxCost                        |
| Type            | float                          |
| Description     | Tax cost of the order.         |
| Required        | False                          |


| Parameters      | Description                    |
|------------------|---------------------------------|
| Name            | PromotionDiscount              |
| Type            | float                          |
| Description     | Promotion discount of the order. |
| Required        | False                          |


| Parameters      | Description                    |
|------------------|---------------------------------|
| Name            | Total                          |
| Type            | float                          |
| Description     | Total of the order.            |
| Required        | False                          |


| Parameters      | Description                    |
|------------------|---------------------------------|
| Name            | IsSubmitted                    |
| Type            | boolean                        |
| Description     | True if this Order has been passed from the Buyer to the Seller. |
| Required        | False                          |


| Parameters      | Description                    |
|------------------|---------------------------------|
| Name            | xp                             |
| Type            | object                         |
| Description     | Container for extended (custom) properties of the order. |
| Required        | False                          |

## `POST` `v1/orders/{direction}/{orderID}/ship`
Ship an order ship

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
{'ID': '', 'BuyerID': '', 'Shipper': '', 'DateShipped': '2018-03-21T23:00:00+00:00', 'DateDelivered': '2018-03-21T23:00:00+00:00', 'TrackingNumber': '', 'Cost': 0, 'xp': {}, 'Account': '', 'FromAddressID': '', 'ToAddressID': ''}
```

```
[{'Name': 'ID', 'Type': 'string', 'Description': 'ID of the shipment. Can only contain characters Aa-Zz, 0-9, -, and _. Searchable: priority level 1. Sortable.', 'Required': False}, {'Name': 'BuyerID', 'Type': 'string', 'Description': 'ID of the buyer. Searchable: priority level 1. Sortable.', 'Required': False}, {'Name': 'Shipper', 'Type': 'string', 'Description': 'Shipper of the shipment. Searchable: priority level 2. Sortable.', 'Required': False}, {'Name': 'DateShipped', 'Type': 'date', 'Description': 'Date shipped of the shipment. Searchable: priority level 3. Sortable: priority level 1.', 'Required': False}, {'Name': 'DateDelivered', 'Type': 'date', 'Description': 'Date delivered of the shipment. Searchable: priority level 4. Sortable.', 'Required': False}, {'Name': 'TrackingNumber', 'Type': 'string', 'Description': 'Tracking number of the shipment. Max length 3000 characters. Searchable: priority level 4.', 'Required': False}, {'Name': 'Cost', 'Type': 'float', 'Description': 'Cost of the shipment. Sortable.', 'Required': False}, {'Name': 'xp', 'Type': 'object', 'Description': 'Container for extended (custom) properties of the shipment.', 'Required': False}, {'Name': 'Account', 'Type': 'string', 'Description': 'Account of the shipment.', 'Required': False}, {'Name': 'FromAddressID', 'Type': 'string', 'Description': 'ID of the from address.', 'Required': False}, {'Name': 'ToAddressID', 'Type': 'string', 'Description': 'ID of the to address.', 'Required': False}]
```

**Responsestatus**: `201`

## Responsebody
```
{'ID': '', 'FromUser': {'ID': '', 'Username': '', 'FirstName': '', 'LastName': '', 'Email': '', 'Phone': '', 'TermsAccepted': '2018-03-21T23:00:00+00:00', 'Active': False, 'xp': {}, 'AvailableRoles': ['']}, 'FromCompanyID': '', 'FromUserID': '', 'BillingAddressID': '', 'BillingAddress': {'ID': '', 'DateCreated': '2018-03-21T23:00:00+00:00', 'CompanyName': '', 'FirstName': '', 'LastName': '', 'Street1': '', 'Street2': '', 'City': '', 'State': '', 'Zip': '', 'Country': '', 'Phone': '', 'AddressName': '', 'xp': {}}, 'ShippingAddressID': '', 'Comments': '', 'LineItemCount': 0, 'Status': 'Unsubmitted', 'DateCreated': '2018-03-21T23:00:00+00:00', 'DateSubmitted': '2018-03-21T23:00:00+00:00', 'DateApproved': '2018-03-21T23:00:00+00:00', 'DateDeclined': '2018-03-21T23:00:00+00:00', 'DateCanceled': '2018-03-21T23:00:00+00:00', 'DateCompleted': '2018-03-21T23:00:00+00:00', 'Subtotal': 0, 'ShippingCost': 0, 'TaxCost': 0, 'PromotionDiscount': 0, 'Total': 0, 'IsSubmitted': False, 'xp': {}}
```


| Parameters      | Description                    |
|------------------|---------------------------------|
| Name            | ID                             |
| Type            | string                         |
| Description     | ID of the order.               |
| Required        | False                          |


| Parameters      | Description                    |
|------------------|---------------------------------|
| Name            | FromUser                       |
| Type            | object                         |
| Description     | From user of the order.        |
| Required        | False                          |


| Parameters      | Description                    |
|------------------|---------------------------------|
| Name            | FromCompanyID                  |
| Type            | string                         |
| Description     | ID of the from company.        |
| Required        | False                          |


| Parameters      | Description                    |
|------------------|---------------------------------|
| Name            | FromUserID                     |
| Type            | string                         |
| Description     | ID of the from user.           |
| Required        | False                          |


| Parameters      | Description                    |
|------------------|---------------------------------|
| Name            | BillingAddressID               |
| Type            | string                         |
| Description     | ID of the billing address.     |
| Required        | False                          |


| Parameters      | Description                    |
|------------------|---------------------------------|
| Name            | BillingAddress                 |
| Type            | object                         |
| Description     | Billing address of the order.  |
| Required        | False                          |


| Parameters      | Description                    |
|------------------|---------------------------------|
| Name            | ShippingAddressID              |
| Type            | string                         |
| Description     | ID of the Shipping Address for all LineItems on the Order. Null when there are multiple Shipping Addresses involved. |
| Required        | False                          |


| Parameters      | Description                    |
|------------------|---------------------------------|
| Name            | Comments                       |
| Type            | string                         |
| Description     | Comments of the order.         |
| Required        | False                          |


| Parameters      | Description                    |
|------------------|---------------------------------|
| Name            | LineItemCount                  |
| Type            | integer                        |
| Description     | Line item count of the order.  |
| Required        | False                          |


| Parameters      | Description                    |
|------------------|---------------------------------|
| Name            | Status                         |
| Type            | string                         |
| Description     | Status of the order. Possible values: Unsubmitted, AwaitingApproval, Declined, Open, Completed, Canceled. |
| Required        | False                          |


| Parameters      | Description                    |
|------------------|---------------------------------|
| Name            | DateCreated                    |
| Type            | date                           |
| Description     | Date created of the order.     |
| Required        | False                          |


| Parameters      | Description                    |
|------------------|---------------------------------|
| Name            | DateSubmitted                  |
| Type            | date                           |
| Description     | Date submitted of the order.   |
| Required        | False                          |


| Parameters      | Description                    |
|------------------|---------------------------------|
| Name            | DateApproved                   |
| Type            | date                           |
| Description     | Date approved of the order.    |
| Required        | False                          |


| Parameters      | Description                    |
|------------------|---------------------------------|
| Name            | DateDeclined                   |
| Type            | date                           |
| Description     | Date declined of the order.    |
| Required        | False                          |


| Parameters      | Description                    |
|------------------|---------------------------------|
| Name            | DateCanceled                   |
| Type            | date                           |
| Description     | Date canceled of the order.    |
| Required        | False                          |


| Parameters      | Description                    |
|------------------|---------------------------------|
| Name            | DateCompleted                  |
| Type            | date                           |
| Description     | Date completed of the order.   |
| Required        | False                          |


| Parameters      | Description                    |
|------------------|---------------------------------|
| Name            | Subtotal                       |
| Type            | float                          |
| Description     | Subtotal of the order.         |
| Required        | False                          |


| Parameters      | Description                    |
|------------------|---------------------------------|
| Name            | ShippingCost                   |
| Type            | float                          |
| Description     | Shipping cost of the order.    |
| Required        | False                          |


| Parameters      | Description                    |
|------------------|---------------------------------|
| Name            | TaxCost                        |
| Type            | float                          |
| Description     | Tax cost of the order.         |
| Required        | False                          |


| Parameters      | Description                    |
|------------------|---------------------------------|
| Name            | PromotionDiscount              |
| Type            | float                          |
| Description     | Promotion discount of the order. |
| Required        | False                          |


| Parameters      | Description                    |
|------------------|---------------------------------|
| Name            | Total                          |
| Type            | float                          |
| Description     | Total of the order.            |
| Required        | False                          |


| Parameters      | Description                    |
|------------------|---------------------------------|
| Name            | IsSubmitted                    |
| Type            | boolean                        |
| Description     | True if this Order has been passed from the Buyer to the Seller. |
| Required        | False                          |


| Parameters      | Description                    |
|------------------|---------------------------------|
| Name            | xp                             |
| Type            | object                         |
| Description     | Container for extended (custom) properties of the order. |
| Required        | False                          |

## `PUT` `v1/orders/{direction}/{orderID}/shipto`
Set an shipping address

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
{'ID': '', 'CompanyName': '', 'FirstName': '', 'LastName': '', 'Street1': '', 'Street2': '', 'City': '', 'State': '', 'Zip': '', 'Country': '', 'Phone': '', 'AddressName': '', 'xp': {}}
```

```
[{'Name': 'ID', 'Type': 'string', 'Description': 'ID of the address. Can only contain characters Aa-Zz, 0-9, -, and _. Searchable: priority level 1. Sortable: priority level 2.', 'Required': False}, {'Name': 'CompanyName', 'Type': 'string', 'Description': 'Company name of the address. Max length 100 characters. Sortable.', 'Required': False}, {'Name': 'FirstName', 'Type': 'string', 'Description': 'First name of the address. Max length 100 characters. Searchable: priority level 7. Sortable.', 'Required': False}, {'Name': 'LastName', 'Type': 'string', 'Description': 'Last name of the address. Max length 100 characters. Searchable: priority level 6. Sortable.', 'Required': False}, {'Name': 'Street1', 'Type': 'string', 'Description': 'Street 1 of the address. Required. Max length 100 characters. Searchable: priority level 4. Sortable.', 'Required': True}, {'Name': 'Street2', 'Type': 'string', 'Description': 'Street 2 of the address. Max length 100 characters. Searchable: priority level 5. Sortable.', 'Required': False}, {'Name': 'City', 'Type': 'string', 'Description': 'City of the address. Required. Max length 100 characters. Searchable: priority level 3. Sortable.', 'Required': True}, {'Name': 'State', 'Type': 'string', 'Description': 'State of the address. Required. Max length 100 characters. Searchable: priority level 7. Sortable.', 'Required': True}, {'Name': 'Zip', 'Type': 'string', 'Description': 'Zip of the address. Required. Max length 100 characters. Searchable: priority level 6. Sortable.', 'Required': True}, {'Name': 'Country', 'Type': 'string', 'Description': 'Country of the address. Required. Max length 2 characters. Sortable.', 'Required': True}, {'Name': 'Phone', 'Type': 'string', 'Description': 'Phone of the address. Max length 100 characters. Sortable.', 'Required': False}, {'Name': 'AddressName', 'Type': 'string', 'Description': 'Address name of the address. Max length 100 characters. Searchable: priority level 2. Sortable: priority level 1.', 'Required': False}, {'Name': 'xp', 'Type': 'object', 'Description': 'Container for extended (custom) properties of the address.', 'Required': False}]
```

**Responsestatus**: `200`

## Responsebody
```
{'ID': '', 'FromUser': {'ID': '', 'Username': '', 'FirstName': '', 'LastName': '', 'Email': '', 'Phone': '', 'TermsAccepted': '2018-03-21T23:00:00+00:00', 'Active': False, 'xp': {}, 'AvailableRoles': ['']}, 'FromCompanyID': '', 'FromUserID': '', 'BillingAddressID': '', 'BillingAddress': {'ID': '', 'DateCreated': '2018-03-21T23:00:00+00:00', 'CompanyName': '', 'FirstName': '', 'LastName': '', 'Street1': '', 'Street2': '', 'City': '', 'State': '', 'Zip': '', 'Country': '', 'Phone': '', 'AddressName': '', 'xp': {}}, 'ShippingAddressID': '', 'Comments': '', 'LineItemCount': 0, 'Status': 'Unsubmitted', 'DateCreated': '2018-03-21T23:00:00+00:00', 'DateSubmitted': '2018-03-21T23:00:00+00:00', 'DateApproved': '2018-03-21T23:00:00+00:00', 'DateDeclined': '2018-03-21T23:00:00+00:00', 'DateCanceled': '2018-03-21T23:00:00+00:00', 'DateCompleted': '2018-03-21T23:00:00+00:00', 'Subtotal': 0, 'ShippingCost': 0, 'TaxCost': 0, 'PromotionDiscount': 0, 'Total': 0, 'IsSubmitted': False, 'xp': {}}
```


| Parameters      | Description                    |
|------------------|---------------------------------|
| Name            | ID                             |
| Type            | string                         |
| Description     | ID of the order.               |
| Required        | False                          |


| Parameters      | Description                    |
|------------------|---------------------------------|
| Name            | FromUser                       |
| Type            | object                         |
| Description     | From user of the order.        |
| Required        | False                          |


| Parameters      | Description                    |
|------------------|---------------------------------|
| Name            | FromCompanyID                  |
| Type            | string                         |
| Description     | ID of the from company.        |
| Required        | False                          |


| Parameters      | Description                    |
|------------------|---------------------------------|
| Name            | FromUserID                     |
| Type            | string                         |
| Description     | ID of the from user.           |
| Required        | False                          |


| Parameters      | Description                    |
|------------------|---------------------------------|
| Name            | BillingAddressID               |
| Type            | string                         |
| Description     | ID of the billing address.     |
| Required        | False                          |


| Parameters      | Description                    |
|------------------|---------------------------------|
| Name            | BillingAddress                 |
| Type            | object                         |
| Description     | Billing address of the order.  |
| Required        | False                          |


| Parameters      | Description                    |
|------------------|---------------------------------|
| Name            | ShippingAddressID              |
| Type            | string                         |
| Description     | ID of the Shipping Address for all LineItems on the Order. Null when there are multiple Shipping Addresses involved. |
| Required        | False                          |


| Parameters      | Description                    |
|------------------|---------------------------------|
| Name            | Comments                       |
| Type            | string                         |
| Description     | Comments of the order.         |
| Required        | False                          |


| Parameters      | Description                    |
|------------------|---------------------------------|
| Name            | LineItemCount                  |
| Type            | integer                        |
| Description     | Line item count of the order.  |
| Required        | False                          |


| Parameters      | Description                    |
|------------------|---------------------------------|
| Name            | Status                         |
| Type            | string                         |
| Description     | Status of the order. Possible values: Unsubmitted, AwaitingApproval, Declined, Open, Completed, Canceled. |
| Required        | False                          |


| Parameters      | Description                    |
|------------------|---------------------------------|
| Name            | DateCreated                    |
| Type            | date                           |
| Description     | Date created of the order.     |
| Required        | False                          |


| Parameters      | Description                    |
|------------------|---------------------------------|
| Name            | DateSubmitted                  |
| Type            | date                           |
| Description     | Date submitted of the order.   |
| Required        | False                          |


| Parameters      | Description                    |
|------------------|---------------------------------|
| Name            | DateApproved                   |
| Type            | date                           |
| Description     | Date approved of the order.    |
| Required        | False                          |


| Parameters      | Description                    |
|------------------|---------------------------------|
| Name            | DateDeclined                   |
| Type            | date                           |
| Description     | Date declined of the order.    |
| Required        | False                          |


| Parameters      | Description                    |
|------------------|---------------------------------|
| Name            | DateCanceled                   |
| Type            | date                           |
| Description     | Date canceled of the order.    |
| Required        | False                          |


| Parameters      | Description                    |
|------------------|---------------------------------|
| Name            | DateCompleted                  |
| Type            | date                           |
| Description     | Date completed of the order.   |
| Required        | False                          |


| Parameters      | Description                    |
|------------------|---------------------------------|
| Name            | Subtotal                       |
| Type            | float                          |
| Description     | Subtotal of the order.         |
| Required        | False                          |


| Parameters      | Description                    |
|------------------|---------------------------------|
| Name            | ShippingCost                   |
| Type            | float                          |
| Description     | Shipping cost of the order.    |
| Required        | False                          |


| Parameters      | Description                    |
|------------------|---------------------------------|
| Name            | TaxCost                        |
| Type            | float                          |
| Description     | Tax cost of the order.         |
| Required        | False                          |


| Parameters      | Description                    |
|------------------|---------------------------------|
| Name            | PromotionDiscount              |
| Type            | float                          |
| Description     | Promotion discount of the order. |
| Required        | False                          |


| Parameters      | Description                    |
|------------------|---------------------------------|
| Name            | Total                          |
| Type            | float                          |
| Description     | Total of the order.            |
| Required        | False                          |


| Parameters      | Description                    |
|------------------|---------------------------------|
| Name            | IsSubmitted                    |
| Type            | boolean                        |
| Description     | True if this Order has been passed from the Buyer to the Seller. |
| Required        | False                          |


| Parameters      | Description                    |
|------------------|---------------------------------|
| Name            | xp                             |
| Type            | object                         |
| Description     | Container for extended (custom) properties of the order. |
| Required        | False                          |

## `PATCH` `v1/orders/{direction}/{orderID}/shipto`
Partially update an order shipping address

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
{'ID': '', 'CompanyName': '', 'FirstName': '', 'LastName': '', 'Street1': '', 'Street2': '', 'City': '', 'State': '', 'Zip': '', 'Country': '', 'Phone': '', 'AddressName': '', 'xp': {}}
```

```
[{'Name': 'ID', 'Type': 'string', 'Description': 'ID of the address. Can only contain characters Aa-Zz, 0-9, -, and _. Searchable: priority level 1. Sortable: priority level 2.', 'Required': False}, {'Name': 'CompanyName', 'Type': 'string', 'Description': 'Company name of the address. Max length 100 characters. Sortable.', 'Required': False}, {'Name': 'FirstName', 'Type': 'string', 'Description': 'First name of the address. Max length 100 characters. Searchable: priority level 7. Sortable.', 'Required': False}, {'Name': 'LastName', 'Type': 'string', 'Description': 'Last name of the address. Max length 100 characters. Searchable: priority level 6. Sortable.', 'Required': False}, {'Name': 'Street1', 'Type': 'string', 'Description': 'Street 1 of the address. Required. Max length 100 characters. Searchable: priority level 4. Sortable.', 'Required': True}, {'Name': 'Street2', 'Type': 'string', 'Description': 'Street 2 of the address. Max length 100 characters. Searchable: priority level 5. Sortable.', 'Required': False}, {'Name': 'City', 'Type': 'string', 'Description': 'City of the address. Required. Max length 100 characters. Searchable: priority level 3. Sortable.', 'Required': True}, {'Name': 'State', 'Type': 'string', 'Description': 'State of the address. Required. Max length 100 characters. Searchable: priority level 7. Sortable.', 'Required': True}, {'Name': 'Zip', 'Type': 'string', 'Description': 'Zip of the address. Required. Max length 100 characters. Searchable: priority level 6. Sortable.', 'Required': True}, {'Name': 'Country', 'Type': 'string', 'Description': 'Country of the address. Required. Max length 2 characters. Sortable.', 'Required': True}, {'Name': 'Phone', 'Type': 'string', 'Description': 'Phone of the address. Max length 100 characters. Sortable.', 'Required': False}, {'Name': 'AddressName', 'Type': 'string', 'Description': 'Address name of the address. Max length 100 characters. Searchable: priority level 2. Sortable: priority level 1.', 'Required': False}, {'Name': 'xp', 'Type': 'object', 'Description': 'Container for extended (custom) properties of the address.', 'Required': False}]
```

**Responsestatus**: `200`

## Responsebody
```
{'ID': '', 'FromUser': {'ID': '', 'Username': '', 'FirstName': '', 'LastName': '', 'Email': '', 'Phone': '', 'TermsAccepted': '2018-03-21T23:00:00+00:00', 'Active': False, 'xp': {}, 'AvailableRoles': ['']}, 'FromCompanyID': '', 'FromUserID': '', 'BillingAddressID': '', 'BillingAddress': {'ID': '', 'DateCreated': '2018-03-21T23:00:00+00:00', 'CompanyName': '', 'FirstName': '', 'LastName': '', 'Street1': '', 'Street2': '', 'City': '', 'State': '', 'Zip': '', 'Country': '', 'Phone': '', 'AddressName': '', 'xp': {}}, 'ShippingAddressID': '', 'Comments': '', 'LineItemCount': 0, 'Status': 'Unsubmitted', 'DateCreated': '2018-03-21T23:00:00+00:00', 'DateSubmitted': '2018-03-21T23:00:00+00:00', 'DateApproved': '2018-03-21T23:00:00+00:00', 'DateDeclined': '2018-03-21T23:00:00+00:00', 'DateCanceled': '2018-03-21T23:00:00+00:00', 'DateCompleted': '2018-03-21T23:00:00+00:00', 'Subtotal': 0, 'ShippingCost': 0, 'TaxCost': 0, 'PromotionDiscount': 0, 'Total': 0, 'IsSubmitted': False, 'xp': {}}
```


| Parameters      | Description                    |
|------------------|---------------------------------|
| Name            | ID                             |
| Type            | string                         |
| Description     | ID of the order.               |
| Required        | False                          |


| Parameters      | Description                    |
|------------------|---------------------------------|
| Name            | FromUser                       |
| Type            | object                         |
| Description     | From user of the order.        |
| Required        | False                          |


| Parameters      | Description                    |
|------------------|---------------------------------|
| Name            | FromCompanyID                  |
| Type            | string                         |
| Description     | ID of the from company.        |
| Required        | False                          |


| Parameters      | Description                    |
|------------------|---------------------------------|
| Name            | FromUserID                     |
| Type            | string                         |
| Description     | ID of the from user.           |
| Required        | False                          |


| Parameters      | Description                    |
|------------------|---------------------------------|
| Name            | BillingAddressID               |
| Type            | string                         |
| Description     | ID of the billing address.     |
| Required        | False                          |


| Parameters      | Description                    |
|------------------|---------------------------------|
| Name            | BillingAddress                 |
| Type            | object                         |
| Description     | Billing address of the order.  |
| Required        | False                          |


| Parameters      | Description                    |
|------------------|---------------------------------|
| Name            | ShippingAddressID              |
| Type            | string                         |
| Description     | ID of the Shipping Address for all LineItems on the Order. Null when there are multiple Shipping Addresses involved. |
| Required        | False                          |


| Parameters      | Description                    |
|------------------|---------------------------------|
| Name            | Comments                       |
| Type            | string                         |
| Description     | Comments of the order.         |
| Required        | False                          |


| Parameters      | Description                    |
|------------------|---------------------------------|
| Name            | LineItemCount                  |
| Type            | integer                        |
| Description     | Line item count of the order.  |
| Required        | False                          |


| Parameters      | Description                    |
|------------------|---------------------------------|
| Name            | Status                         |
| Type            | string                         |
| Description     | Status of the order. Possible values: Unsubmitted, AwaitingApproval, Declined, Open, Completed, Canceled. |
| Required        | False                          |


| Parameters      | Description                    |
|------------------|---------------------------------|
| Name            | DateCreated                    |
| Type            | date                           |
| Description     | Date created of the order.     |
| Required        | False                          |


| Parameters      | Description                    |
|------------------|---------------------------------|
| Name            | DateSubmitted                  |
| Type            | date                           |
| Description     | Date submitted of the order.   |
| Required        | False                          |


| Parameters      | Description                    |
|------------------|---------------------------------|
| Name            | DateApproved                   |
| Type            | date                           |
| Description     | Date approved of the order.    |
| Required        | False                          |


| Parameters      | Description                    |
|------------------|---------------------------------|
| Name            | DateDeclined                   |
| Type            | date                           |
| Description     | Date declined of the order.    |
| Required        | False                          |


| Parameters      | Description                    |
|------------------|---------------------------------|
| Name            | DateCanceled                   |
| Type            | date                           |
| Description     | Date canceled of the order.    |
| Required        | False                          |


| Parameters      | Description                    |
|------------------|---------------------------------|
| Name            | DateCompleted                  |
| Type            | date                           |
| Description     | Date completed of the order.   |
| Required        | False                          |


| Parameters      | Description                    |
|------------------|---------------------------------|
| Name            | Subtotal                       |
| Type            | float                          |
| Description     | Subtotal of the order.         |
| Required        | False                          |


| Parameters      | Description                    |
|------------------|---------------------------------|
| Name            | ShippingCost                   |
| Type            | float                          |
| Description     | Shipping cost of the order.    |
| Required        | False                          |


| Parameters      | Description                    |
|------------------|---------------------------------|
| Name            | TaxCost                        |
| Type            | float                          |
| Description     | Tax cost of the order.         |
| Required        | False                          |


| Parameters      | Description                    |
|------------------|---------------------------------|
| Name            | PromotionDiscount              |
| Type            | float                          |
| Description     | Promotion discount of the order. |
| Required        | False                          |


| Parameters      | Description                    |
|------------------|---------------------------------|
| Name            | Total                          |
| Type            | float                          |
| Description     | Total of the order.            |
| Required        | False                          |


| Parameters      | Description                    |
|------------------|---------------------------------|
| Name            | IsSubmitted                    |
| Type            | boolean                        |
| Description     | True if this Order has been passed from the Buyer to the Seller. |
| Required        | False                          |


| Parameters      | Description                    |
|------------------|---------------------------------|
| Name            | xp                             |
| Type            | object                         |
| Description     | Container for extended (custom) properties of the order. |
| Required        | False                          |

## `PUT` `v1/orders/{direction}/{orderID}/billto`
Set an billing address

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
{'ID': '', 'CompanyName': '', 'FirstName': '', 'LastName': '', 'Street1': '', 'Street2': '', 'City': '', 'State': '', 'Zip': '', 'Country': '', 'Phone': '', 'AddressName': '', 'xp': {}}
```

```
[{'Name': 'ID', 'Type': 'string', 'Description': 'ID of the address. Can only contain characters Aa-Zz, 0-9, -, and _. Searchable: priority level 1. Sortable: priority level 2.', 'Required': False}, {'Name': 'CompanyName', 'Type': 'string', 'Description': 'Company name of the address. Max length 100 characters. Sortable.', 'Required': False}, {'Name': 'FirstName', 'Type': 'string', 'Description': 'First name of the address. Max length 100 characters. Searchable: priority level 7. Sortable.', 'Required': False}, {'Name': 'LastName', 'Type': 'string', 'Description': 'Last name of the address. Max length 100 characters. Searchable: priority level 6. Sortable.', 'Required': False}, {'Name': 'Street1', 'Type': 'string', 'Description': 'Street 1 of the address. Required. Max length 100 characters. Searchable: priority level 4. Sortable.', 'Required': True}, {'Name': 'Street2', 'Type': 'string', 'Description': 'Street 2 of the address. Max length 100 characters. Searchable: priority level 5. Sortable.', 'Required': False}, {'Name': 'City', 'Type': 'string', 'Description': 'City of the address. Required. Max length 100 characters. Searchable: priority level 3. Sortable.', 'Required': True}, {'Name': 'State', 'Type': 'string', 'Description': 'State of the address. Required. Max length 100 characters. Searchable: priority level 7. Sortable.', 'Required': True}, {'Name': 'Zip', 'Type': 'string', 'Description': 'Zip of the address. Required. Max length 100 characters. Searchable: priority level 6. Sortable.', 'Required': True}, {'Name': 'Country', 'Type': 'string', 'Description': 'Country of the address. Required. Max length 2 characters. Sortable.', 'Required': True}, {'Name': 'Phone', 'Type': 'string', 'Description': 'Phone of the address. Max length 100 characters. Sortable.', 'Required': False}, {'Name': 'AddressName', 'Type': 'string', 'Description': 'Address name of the address. Max length 100 characters. Searchable: priority level 2. Sortable: priority level 1.', 'Required': False}, {'Name': 'xp', 'Type': 'object', 'Description': 'Container for extended (custom) properties of the address.', 'Required': False}]
```

**Responsestatus**: `200`

## Responsebody
```
{'ID': '', 'FromUser': {'ID': '', 'Username': '', 'FirstName': '', 'LastName': '', 'Email': '', 'Phone': '', 'TermsAccepted': '2018-03-21T23:00:00+00:00', 'Active': False, 'xp': {}, 'AvailableRoles': ['']}, 'FromCompanyID': '', 'FromUserID': '', 'BillingAddressID': '', 'BillingAddress': {'ID': '', 'DateCreated': '2018-03-21T23:00:00+00:00', 'CompanyName': '', 'FirstName': '', 'LastName': '', 'Street1': '', 'Street2': '', 'City': '', 'State': '', 'Zip': '', 'Country': '', 'Phone': '', 'AddressName': '', 'xp': {}}, 'ShippingAddressID': '', 'Comments': '', 'LineItemCount': 0, 'Status': 'Unsubmitted', 'DateCreated': '2018-03-21T23:00:00+00:00', 'DateSubmitted': '2018-03-21T23:00:00+00:00', 'DateApproved': '2018-03-21T23:00:00+00:00', 'DateDeclined': '2018-03-21T23:00:00+00:00', 'DateCanceled': '2018-03-21T23:00:00+00:00', 'DateCompleted': '2018-03-21T23:00:00+00:00', 'Subtotal': 0, 'ShippingCost': 0, 'TaxCost': 0, 'PromotionDiscount': 0, 'Total': 0, 'IsSubmitted': False, 'xp': {}}
```


| Parameters      | Description                    |
|------------------|---------------------------------|
| Name            | ID                             |
| Type            | string                         |
| Description     | ID of the order.               |
| Required        | False                          |


| Parameters      | Description                    |
|------------------|---------------------------------|
| Name            | FromUser                       |
| Type            | object                         |
| Description     | From user of the order.        |
| Required        | False                          |


| Parameters      | Description                    |
|------------------|---------------------------------|
| Name            | FromCompanyID                  |
| Type            | string                         |
| Description     | ID of the from company.        |
| Required        | False                          |


| Parameters      | Description                    |
|------------------|---------------------------------|
| Name            | FromUserID                     |
| Type            | string                         |
| Description     | ID of the from user.           |
| Required        | False                          |


| Parameters      | Description                    |
|------------------|---------------------------------|
| Name            | BillingAddressID               |
| Type            | string                         |
| Description     | ID of the billing address.     |
| Required        | False                          |


| Parameters      | Description                    |
|------------------|---------------------------------|
| Name            | BillingAddress                 |
| Type            | object                         |
| Description     | Billing address of the order.  |
| Required        | False                          |


| Parameters      | Description                    |
|------------------|---------------------------------|
| Name            | ShippingAddressID              |
| Type            | string                         |
| Description     | ID of the Shipping Address for all LineItems on the Order. Null when there are multiple Shipping Addresses involved. |
| Required        | False                          |


| Parameters      | Description                    |
|------------------|---------------------------------|
| Name            | Comments                       |
| Type            | string                         |
| Description     | Comments of the order.         |
| Required        | False                          |


| Parameters      | Description                    |
|------------------|---------------------------------|
| Name            | LineItemCount                  |
| Type            | integer                        |
| Description     | Line item count of the order.  |
| Required        | False                          |


| Parameters      | Description                    |
|------------------|---------------------------------|
| Name            | Status                         |
| Type            | string                         |
| Description     | Status of the order. Possible values: Unsubmitted, AwaitingApproval, Declined, Open, Completed, Canceled. |
| Required        | False                          |


| Parameters      | Description                    |
|------------------|---------------------------------|
| Name            | DateCreated                    |
| Type            | date                           |
| Description     | Date created of the order.     |
| Required        | False                          |


| Parameters      | Description                    |
|------------------|---------------------------------|
| Name            | DateSubmitted                  |
| Type            | date                           |
| Description     | Date submitted of the order.   |
| Required        | False                          |


| Parameters      | Description                    |
|------------------|---------------------------------|
| Name            | DateApproved                   |
| Type            | date                           |
| Description     | Date approved of the order.    |
| Required        | False                          |


| Parameters      | Description                    |
|------------------|---------------------------------|
| Name            | DateDeclined                   |
| Type            | date                           |
| Description     | Date declined of the order.    |
| Required        | False                          |


| Parameters      | Description                    |
|------------------|---------------------------------|
| Name            | DateCanceled                   |
| Type            | date                           |
| Description     | Date canceled of the order.    |
| Required        | False                          |


| Parameters      | Description                    |
|------------------|---------------------------------|
| Name            | DateCompleted                  |
| Type            | date                           |
| Description     | Date completed of the order.   |
| Required        | False                          |


| Parameters      | Description                    |
|------------------|---------------------------------|
| Name            | Subtotal                       |
| Type            | float                          |
| Description     | Subtotal of the order.         |
| Required        | False                          |


| Parameters      | Description                    |
|------------------|---------------------------------|
| Name            | ShippingCost                   |
| Type            | float                          |
| Description     | Shipping cost of the order.    |
| Required        | False                          |


| Parameters      | Description                    |
|------------------|---------------------------------|
| Name            | TaxCost                        |
| Type            | float                          |
| Description     | Tax cost of the order.         |
| Required        | False                          |


| Parameters      | Description                    |
|------------------|---------------------------------|
| Name            | PromotionDiscount              |
| Type            | float                          |
| Description     | Promotion discount of the order. |
| Required        | False                          |


| Parameters      | Description                    |
|------------------|---------------------------------|
| Name            | Total                          |
| Type            | float                          |
| Description     | Total of the order.            |
| Required        | False                          |


| Parameters      | Description                    |
|------------------|---------------------------------|
| Name            | IsSubmitted                    |
| Type            | boolean                        |
| Description     | True if this Order has been passed from the Buyer to the Seller. |
| Required        | False                          |


| Parameters      | Description                    |
|------------------|---------------------------------|
| Name            | xp                             |
| Type            | object                         |
| Description     | Container for extended (custom) properties of the order. |
| Required        | False                          |

## `PATCH` `v1/orders/{direction}/{orderID}/billto`
Partially update an order billing address

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
{'ID': '', 'CompanyName': '', 'FirstName': '', 'LastName': '', 'Street1': '', 'Street2': '', 'City': '', 'State': '', 'Zip': '', 'Country': '', 'Phone': '', 'AddressName': '', 'xp': {}}
```

```
[{'Name': 'ID', 'Type': 'string', 'Description': 'ID of the address. Can only contain characters Aa-Zz, 0-9, -, and _. Searchable: priority level 1. Sortable: priority level 2.', 'Required': False}, {'Name': 'CompanyName', 'Type': 'string', 'Description': 'Company name of the address. Max length 100 characters. Sortable.', 'Required': False}, {'Name': 'FirstName', 'Type': 'string', 'Description': 'First name of the address. Max length 100 characters. Searchable: priority level 7. Sortable.', 'Required': False}, {'Name': 'LastName', 'Type': 'string', 'Description': 'Last name of the address. Max length 100 characters. Searchable: priority level 6. Sortable.', 'Required': False}, {'Name': 'Street1', 'Type': 'string', 'Description': 'Street 1 of the address. Required. Max length 100 characters. Searchable: priority level 4. Sortable.', 'Required': True}, {'Name': 'Street2', 'Type': 'string', 'Description': 'Street 2 of the address. Max length 100 characters. Searchable: priority level 5. Sortable.', 'Required': False}, {'Name': 'City', 'Type': 'string', 'Description': 'City of the address. Required. Max length 100 characters. Searchable: priority level 3. Sortable.', 'Required': True}, {'Name': 'State', 'Type': 'string', 'Description': 'State of the address. Required. Max length 100 characters. Searchable: priority level 7. Sortable.', 'Required': True}, {'Name': 'Zip', 'Type': 'string', 'Description': 'Zip of the address. Required. Max length 100 characters. Searchable: priority level 6. Sortable.', 'Required': True}, {'Name': 'Country', 'Type': 'string', 'Description': 'Country of the address. Required. Max length 2 characters. Sortable.', 'Required': True}, {'Name': 'Phone', 'Type': 'string', 'Description': 'Phone of the address. Max length 100 characters. Sortable.', 'Required': False}, {'Name': 'AddressName', 'Type': 'string', 'Description': 'Address name of the address. Max length 100 characters. Searchable: priority level 2. Sortable: priority level 1.', 'Required': False}, {'Name': 'xp', 'Type': 'object', 'Description': 'Container for extended (custom) properties of the address.', 'Required': False}]
```

**Responsestatus**: `200`

## Responsebody
```
{'ID': '', 'FromUser': {'ID': '', 'Username': '', 'FirstName': '', 'LastName': '', 'Email': '', 'Phone': '', 'TermsAccepted': '2018-03-21T23:00:00+00:00', 'Active': False, 'xp': {}, 'AvailableRoles': ['']}, 'FromCompanyID': '', 'FromUserID': '', 'BillingAddressID': '', 'BillingAddress': {'ID': '', 'DateCreated': '2018-03-21T23:00:00+00:00', 'CompanyName': '', 'FirstName': '', 'LastName': '', 'Street1': '', 'Street2': '', 'City': '', 'State': '', 'Zip': '', 'Country': '', 'Phone': '', 'AddressName': '', 'xp': {}}, 'ShippingAddressID': '', 'Comments': '', 'LineItemCount': 0, 'Status': 'Unsubmitted', 'DateCreated': '2018-03-21T23:00:00+00:00', 'DateSubmitted': '2018-03-21T23:00:00+00:00', 'DateApproved': '2018-03-21T23:00:00+00:00', 'DateDeclined': '2018-03-21T23:00:00+00:00', 'DateCanceled': '2018-03-21T23:00:00+00:00', 'DateCompleted': '2018-03-21T23:00:00+00:00', 'Subtotal': 0, 'ShippingCost': 0, 'TaxCost': 0, 'PromotionDiscount': 0, 'Total': 0, 'IsSubmitted': False, 'xp': {}}
```


| Parameters      | Description                    |
|------------------|---------------------------------|
| Name            | ID                             |
| Type            | string                         |
| Description     | ID of the order.               |
| Required        | False                          |


| Parameters      | Description                    |
|------------------|---------------------------------|
| Name            | FromUser                       |
| Type            | object                         |
| Description     | From user of the order.        |
| Required        | False                          |


| Parameters      | Description                    |
|------------------|---------------------------------|
| Name            | FromCompanyID                  |
| Type            | string                         |
| Description     | ID of the from company.        |
| Required        | False                          |


| Parameters      | Description                    |
|------------------|---------------------------------|
| Name            | FromUserID                     |
| Type            | string                         |
| Description     | ID of the from user.           |
| Required        | False                          |


| Parameters      | Description                    |
|------------------|---------------------------------|
| Name            | BillingAddressID               |
| Type            | string                         |
| Description     | ID of the billing address.     |
| Required        | False                          |


| Parameters      | Description                    |
|------------------|---------------------------------|
| Name            | BillingAddress                 |
| Type            | object                         |
| Description     | Billing address of the order.  |
| Required        | False                          |


| Parameters      | Description                    |
|------------------|---------------------------------|
| Name            | ShippingAddressID              |
| Type            | string                         |
| Description     | ID of the Shipping Address for all LineItems on the Order. Null when there are multiple Shipping Addresses involved. |
| Required        | False                          |


| Parameters      | Description                    |
|------------------|---------------------------------|
| Name            | Comments                       |
| Type            | string                         |
| Description     | Comments of the order.         |
| Required        | False                          |


| Parameters      | Description                    |
|------------------|---------------------------------|
| Name            | LineItemCount                  |
| Type            | integer                        |
| Description     | Line item count of the order.  |
| Required        | False                          |


| Parameters      | Description                    |
|------------------|---------------------------------|
| Name            | Status                         |
| Type            | string                         |
| Description     | Status of the order. Possible values: Unsubmitted, AwaitingApproval, Declined, Open, Completed, Canceled. |
| Required        | False                          |


| Parameters      | Description                    |
|------------------|---------------------------------|
| Name            | DateCreated                    |
| Type            | date                           |
| Description     | Date created of the order.     |
| Required        | False                          |


| Parameters      | Description                    |
|------------------|---------------------------------|
| Name            | DateSubmitted                  |
| Type            | date                           |
| Description     | Date submitted of the order.   |
| Required        | False                          |


| Parameters      | Description                    |
|------------------|---------------------------------|
| Name            | DateApproved                   |
| Type            | date                           |
| Description     | Date approved of the order.    |
| Required        | False                          |


| Parameters      | Description                    |
|------------------|---------------------------------|
| Name            | DateDeclined                   |
| Type            | date                           |
| Description     | Date declined of the order.    |
| Required        | False                          |


| Parameters      | Description                    |
|------------------|---------------------------------|
| Name            | DateCanceled                   |
| Type            | date                           |
| Description     | Date canceled of the order.    |
| Required        | False                          |


| Parameters      | Description                    |
|------------------|---------------------------------|
| Name            | DateCompleted                  |
| Type            | date                           |
| Description     | Date completed of the order.   |
| Required        | False                          |


| Parameters      | Description                    |
|------------------|---------------------------------|
| Name            | Subtotal                       |
| Type            | float                          |
| Description     | Subtotal of the order.         |
| Required        | False                          |


| Parameters      | Description                    |
|------------------|---------------------------------|
| Name            | ShippingCost                   |
| Type            | float                          |
| Description     | Shipping cost of the order.    |
| Required        | False                          |


| Parameters      | Description                    |
|------------------|---------------------------------|
| Name            | TaxCost                        |
| Type            | float                          |
| Description     | Tax cost of the order.         |
| Required        | False                          |


| Parameters      | Description                    |
|------------------|---------------------------------|
| Name            | PromotionDiscount              |
| Type            | float                          |
| Description     | Promotion discount of the order. |
| Required        | False                          |


| Parameters      | Description                    |
|------------------|---------------------------------|
| Name            | Total                          |
| Type            | float                          |
| Description     | Total of the order.            |
| Required        | False                          |


| Parameters      | Description                    |
|------------------|---------------------------------|
| Name            | IsSubmitted                    |
| Type            | boolean                        |
| Description     | True if this Order has been passed from the Buyer to the Seller. |
| Required        | False                          |


| Parameters      | Description                    |
|------------------|---------------------------------|
| Name            | xp                             |
| Type            | object                         |
| Description     | Container for extended (custom) properties of the order. |
| Required        | False                          |

## `PATCH` `v1/orders/{direction}/{orderID}/fromuser`
Partially update an order from user

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
{'ID': '', 'Username': '', 'Password': '', 'FirstName': '', 'LastName': '', 'Email': '', 'Phone': '', 'TermsAccepted': '2018-03-21T23:00:00+00:00', 'Active': False, 'xp': {}}
```

```
[{'Name': 'ID', 'Type': 'string', 'Description': 'ID of the user. Can only contain characters Aa-Zz, 0-9, -, and _. Searchable: priority level 1. Sortable.', 'Required': False}, {'Name': 'Username', 'Type': 'string', 'Description': 'Username of the user. Required. Max length 100 characters. Searchable: priority level 2. Sortable: priority level 3.', 'Required': True}, {'Name': 'Password', 'Type': 'string', 'Description': 'Password of the user.', 'Required': False}, {'Name': 'FirstName', 'Type': 'string', 'Description': 'First name of the user. Required. Max length 100 characters. Searchable: priority level 4. Sortable: priority level 2.', 'Required': True}, {'Name': 'LastName', 'Type': 'string', 'Description': 'Last name of the user. Required. Max length 100 characters. Searchable: priority level 3. Sortable: priority level 1.', 'Required': True}, {'Name': 'Email', 'Type': 'string', 'Description': 'Email of the user. Required. Max length 200 characters. Searchable: priority level 5. Sortable.', 'Required': True}, {'Name': 'Phone', 'Type': 'string', 'Description': 'Phone of the user. Max length 100 characters.', 'Required': False}, {'Name': 'TermsAccepted', 'Type': 'date', 'Description': 'Terms accepted of the user.', 'Required': False}, {'Name': 'Active', 'Type': 'boolean', 'Description': 'Active of the user. Required.', 'Required': True}, {'Name': 'xp', 'Type': 'object', 'Description': 'Container for extended (custom) properties of the user.', 'Required': False}]
```

**Responsestatus**: `200`

## Responsebody
```
{'ID': '', 'FromUser': {'ID': '', 'Username': '', 'FirstName': '', 'LastName': '', 'Email': '', 'Phone': '', 'TermsAccepted': '2018-03-21T23:00:00+00:00', 'Active': False, 'xp': {}, 'AvailableRoles': ['']}, 'FromCompanyID': '', 'FromUserID': '', 'BillingAddressID': '', 'BillingAddress': {'ID': '', 'DateCreated': '2018-03-21T23:00:00+00:00', 'CompanyName': '', 'FirstName': '', 'LastName': '', 'Street1': '', 'Street2': '', 'City': '', 'State': '', 'Zip': '', 'Country': '', 'Phone': '', 'AddressName': '', 'xp': {}}, 'ShippingAddressID': '', 'Comments': '', 'LineItemCount': 0, 'Status': 'Unsubmitted', 'DateCreated': '2018-03-21T23:00:00+00:00', 'DateSubmitted': '2018-03-21T23:00:00+00:00', 'DateApproved': '2018-03-21T23:00:00+00:00', 'DateDeclined': '2018-03-21T23:00:00+00:00', 'DateCanceled': '2018-03-21T23:00:00+00:00', 'DateCompleted': '2018-03-21T23:00:00+00:00', 'Subtotal': 0, 'ShippingCost': 0, 'TaxCost': 0, 'PromotionDiscount': 0, 'Total': 0, 'IsSubmitted': False, 'xp': {}}
```


| Parameters      | Description                    |
|------------------|---------------------------------|
| Name            | ID                             |
| Type            | string                         |
| Description     | ID of the order.               |
| Required        | False                          |


| Parameters      | Description                    |
|------------------|---------------------------------|
| Name            | FromUser                       |
| Type            | object                         |
| Description     | From user of the order.        |
| Required        | False                          |


| Parameters      | Description                    |
|------------------|---------------------------------|
| Name            | FromCompanyID                  |
| Type            | string                         |
| Description     | ID of the from company.        |
| Required        | False                          |


| Parameters      | Description                    |
|------------------|---------------------------------|
| Name            | FromUserID                     |
| Type            | string                         |
| Description     | ID of the from user.           |
| Required        | False                          |


| Parameters      | Description                    |
|------------------|---------------------------------|
| Name            | BillingAddressID               |
| Type            | string                         |
| Description     | ID of the billing address.     |
| Required        | False                          |


| Parameters      | Description                    |
|------------------|---------------------------------|
| Name            | BillingAddress                 |
| Type            | object                         |
| Description     | Billing address of the order.  |
| Required        | False                          |


| Parameters      | Description                    |
|------------------|---------------------------------|
| Name            | ShippingAddressID              |
| Type            | string                         |
| Description     | ID of the Shipping Address for all LineItems on the Order. Null when there are multiple Shipping Addresses involved. |
| Required        | False                          |


| Parameters      | Description                    |
|------------------|---------------------------------|
| Name            | Comments                       |
| Type            | string                         |
| Description     | Comments of the order.         |
| Required        | False                          |


| Parameters      | Description                    |
|------------------|---------------------------------|
| Name            | LineItemCount                  |
| Type            | integer                        |
| Description     | Line item count of the order.  |
| Required        | False                          |


| Parameters      | Description                    |
|------------------|---------------------------------|
| Name            | Status                         |
| Type            | string                         |
| Description     | Status of the order. Possible values: Unsubmitted, AwaitingApproval, Declined, Open, Completed, Canceled. |
| Required        | False                          |


| Parameters      | Description                    |
|------------------|---------------------------------|
| Name            | DateCreated                    |
| Type            | date                           |
| Description     | Date created of the order.     |
| Required        | False                          |


| Parameters      | Description                    |
|------------------|---------------------------------|
| Name            | DateSubmitted                  |
| Type            | date                           |
| Description     | Date submitted of the order.   |
| Required        | False                          |


| Parameters      | Description                    |
|------------------|---------------------------------|
| Name            | DateApproved                   |
| Type            | date                           |
| Description     | Date approved of the order.    |
| Required        | False                          |


| Parameters      | Description                    |
|------------------|---------------------------------|
| Name            | DateDeclined                   |
| Type            | date                           |
| Description     | Date declined of the order.    |
| Required        | False                          |


| Parameters      | Description                    |
|------------------|---------------------------------|
| Name            | DateCanceled                   |
| Type            | date                           |
| Description     | Date canceled of the order.    |
| Required        | False                          |


| Parameters      | Description                    |
|------------------|---------------------------------|
| Name            | DateCompleted                  |
| Type            | date                           |
| Description     | Date completed of the order.   |
| Required        | False                          |


| Parameters      | Description                    |
|------------------|---------------------------------|
| Name            | Subtotal                       |
| Type            | float                          |
| Description     | Subtotal of the order.         |
| Required        | False                          |


| Parameters      | Description                    |
|------------------|---------------------------------|
| Name            | ShippingCost                   |
| Type            | float                          |
| Description     | Shipping cost of the order.    |
| Required        | False                          |


| Parameters      | Description                    |
|------------------|---------------------------------|
| Name            | TaxCost                        |
| Type            | float                          |
| Description     | Tax cost of the order.         |
| Required        | False                          |


| Parameters      | Description                    |
|------------------|---------------------------------|
| Name            | PromotionDiscount              |
| Type            | float                          |
| Description     | Promotion discount of the order. |
| Required        | False                          |


| Parameters      | Description                    |
|------------------|---------------------------------|
| Name            | Total                          |
| Type            | float                          |
| Description     | Total of the order.            |
| Required        | False                          |


| Parameters      | Description                    |
|------------------|---------------------------------|
| Name            | IsSubmitted                    |
| Type            | boolean                        |
| Description     | True if this Order has been passed from the Buyer to the Seller. |
| Required        | False                          |


| Parameters      | Description                    |
|------------------|---------------------------------|
| Name            | xp                             |
| Type            | object                         |
| Description     | Container for extended (custom) properties of the order. |
| Required        | False                          |

## `POST` `v1/orders/{direction}/{orderID}/promotions/{promoCode}`
Add an promotion

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
| Name            | promoCode                      |
| Type            | string                         |
| Description     | Promo code of the promotion.   |
| Required        | True                           |

## Requestbody
**Responsestatus**: `201`

## Responsebody
```
{'ID': '', 'Code': '', 'Name': '', 'RedemptionLimit': 0, 'RedemptionLimitPerUser': 0, 'RedemptionCount': 0, 'Description': '', 'FinePrint': '', 'StartDate': '2018-03-21T23:00:00+00:00', 'ExpirationDate': '2018-03-21T23:00:00+00:00', 'EligibleExpression': '', 'ValueExpression': '', 'CanCombine': False, 'xp': {}}
```


| Parameters      | Description                    |
|------------------|---------------------------------|
| Name            | ID                             |
| Type            | string                         |
| Description     | ID of the promotion.           |
| Required        | False                          |


| Parameters      | Description                    |
|------------------|---------------------------------|
| Name            | Code                           |
| Type            | string                         |
| Description     | Must be unique. Entered by buyer when adding promo to order. |
| Required        | True                           |


| Parameters      | Description                    |
|------------------|---------------------------------|
| Name            | Name                           |
| Type            | string                         |
| Description     | Name of the promotion.         |
| Required        | False                          |


| Parameters      | Description                    |
|------------------|---------------------------------|
| Name            | RedemptionLimit                |
| Type            | integer                        |
| Description     | Redemption limit of the promotion. |
| Required        | False                          |


| Parameters      | Description                    |
|------------------|---------------------------------|
| Name            | RedemptionLimitPerUser         |
| Type            | integer                        |
| Description     | Redemption limit per user of the promotion. |
| Required        | False                          |


| Parameters      | Description                    |
|------------------|---------------------------------|
| Name            | RedemptionCount                |
| Type            | integer                        |
| Description     | Redemption count of the promotion. |
| Required        | False                          |


| Parameters      | Description                    |
|------------------|---------------------------------|
| Name            | Description                    |
| Type            | string                         |
| Description     | Description of the promotion.  |
| Required        | False                          |


| Parameters      | Description                    |
|------------------|---------------------------------|
| Name            | FinePrint                      |
| Type            | string                         |
| Description     | Terms, conditions, and other legal jargon. |
| Required        | False                          |


| Parameters      | Description                    |
|------------------|---------------------------------|
| Name            | StartDate                      |
| Type            | date                           |
| Description     | Start date of the promotion.   |
| Required        | False                          |


| Parameters      | Description                    |
|------------------|---------------------------------|
| Name            | ExpirationDate                 |
| Type            | date                           |
| Description     | Expiration date of the promotion. |
| Required        | False                          |


| Parameters      | Description                    |
|------------------|---------------------------------|
| Name            | EligibleExpression             |
| Type            | string                         |
| Description     | Eligible expression of the promotion. |
| Required        | True                           |


| Parameters      | Description                    |
|------------------|---------------------------------|
| Name            | ValueExpression                |
| Type            | string                         |
| Description     | Value expression of the promotion. |
| Required        | True                           |


| Parameters      | Description                    |
|------------------|---------------------------------|
| Name            | CanCombine                     |
| Type            | boolean                        |
| Description     | Can combine of the promotion.  |
| Required        | False                          |


| Parameters      | Description                    |
|------------------|---------------------------------|
| Name            | xp                             |
| Type            | object                         |
| Description     | Container for extended (custom) properties of the promotion. |
| Required        | False                          |

## `GET` `v1/orders/{direction}/{orderID}/promotions`
Get a list of order promotions

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
{'Meta': {'Page': 1, 'PageSize': 20, 'TotalCount': 25, 'TotalPages': 2, 'ItemRange': [1, 20]}, 'Items': [{'Amount': 0, 'ID': '', 'Code': '', 'Name': '', 'RedemptionLimit': 0, 'RedemptionLimitPerUser': 0, 'RedemptionCount': 0, 'Description': '', 'FinePrint': '', 'StartDate': '2018-03-21T23:00:00+00:00', 'ExpirationDate': '2018-03-21T23:00:00+00:00', 'EligibleExpression': '', 'ValueExpression': '', 'CanCombine': False, 'xp': {}}]}
```


| Parameters      | Description                    |
|------------------|---------------------------------|
| Name            | Amount                         |
| Type            | float                          |
| Description     | Amount of the order promotion. |
| Required        | False                          |


| Parameters      | Description                    |
|------------------|---------------------------------|
| Name            | ID                             |
| Type            | string                         |
| Description     | ID of the order promotion.     |
| Required        | False                          |


| Parameters      | Description                    |
|------------------|---------------------------------|
| Name            | Code                           |
| Type            | string                         |
| Description     | Must be unique. Entered by buyer when adding promo to order. |
| Required        | True                           |


| Parameters      | Description                    |
|------------------|---------------------------------|
| Name            | Name                           |
| Type            | string                         |
| Description     | Name of the order promotion.   |
| Required        | False                          |


| Parameters      | Description                    |
|------------------|---------------------------------|
| Name            | RedemptionLimit                |
| Type            | integer                        |
| Description     | Redemption limit of the order promotion. |
| Required        | False                          |


| Parameters      | Description                    |
|------------------|---------------------------------|
| Name            | RedemptionLimitPerUser         |
| Type            | integer                        |
| Description     | Redemption limit per user of the order promotion. |
| Required        | False                          |


| Parameters      | Description                    |
|------------------|---------------------------------|
| Name            | RedemptionCount                |
| Type            | integer                        |
| Description     | Redemption count of the order promotion. |
| Required        | False                          |


| Parameters      | Description                    |
|------------------|---------------------------------|
| Name            | Description                    |
| Type            | string                         |
| Description     | Description of the order promotion. |
| Required        | False                          |


| Parameters      | Description                    |
|------------------|---------------------------------|
| Name            | FinePrint                      |
| Type            | string                         |
| Description     | Terms, conditions, and other legal jargon. |
| Required        | False                          |


| Parameters      | Description                    |
|------------------|---------------------------------|
| Name            | StartDate                      |
| Type            | date                           |
| Description     | Start date of the order promotion. |
| Required        | False                          |


| Parameters      | Description                    |
|------------------|---------------------------------|
| Name            | ExpirationDate                 |
| Type            | date                           |
| Description     | Expiration date of the order promotion. |
| Required        | False                          |


| Parameters      | Description                    |
|------------------|---------------------------------|
| Name            | EligibleExpression             |
| Type            | string                         |
| Description     | Eligible expression of the order promotion. |
| Required        | True                           |


| Parameters      | Description                    |
|------------------|---------------------------------|
| Name            | ValueExpression                |
| Type            | string                         |
| Description     | Value expression of the order promotion. |
| Required        | True                           |


| Parameters      | Description                    |
|------------------|---------------------------------|
| Name            | CanCombine                     |
| Type            | boolean                        |
| Description     | Can combine of the order promotion. |
| Required        | False                          |


| Parameters      | Description                    |
|------------------|---------------------------------|
| Name            | xp                             |
| Type            | object                         |
| Description     | Container for extended (custom) properties of the order promotion. |
| Required        | False                          |

## `DELETE` `v1/orders/{direction}/{orderID}/promotions/{promoCode}`
Remove an promotion

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
| Name            | promoCode                      |
| Type            | string                         |
| Description     | Promo code of the order.       |
| Required        | True                           |

## Requestbody
**Responsestatus**: `200`

## Responsebody
```
{'ID': '', 'FromUser': {'ID': '', 'Username': '', 'FirstName': '', 'LastName': '', 'Email': '', 'Phone': '', 'TermsAccepted': '2018-03-21T23:00:00+00:00', 'Active': False, 'xp': {}, 'AvailableRoles': ['']}, 'FromCompanyID': '', 'FromUserID': '', 'BillingAddressID': '', 'BillingAddress': {'ID': '', 'DateCreated': '2018-03-21T23:00:00+00:00', 'CompanyName': '', 'FirstName': '', 'LastName': '', 'Street1': '', 'Street2': '', 'City': '', 'State': '', 'Zip': '', 'Country': '', 'Phone': '', 'AddressName': '', 'xp': {}}, 'ShippingAddressID': '', 'Comments': '', 'LineItemCount': 0, 'Status': 'Unsubmitted', 'DateCreated': '2018-03-21T23:00:00+00:00', 'DateSubmitted': '2018-03-21T23:00:00+00:00', 'DateApproved': '2018-03-21T23:00:00+00:00', 'DateDeclined': '2018-03-21T23:00:00+00:00', 'DateCanceled': '2018-03-21T23:00:00+00:00', 'DateCompleted': '2018-03-21T23:00:00+00:00', 'Subtotal': 0, 'ShippingCost': 0, 'TaxCost': 0, 'PromotionDiscount': 0, 'Total': 0, 'IsSubmitted': False, 'xp': {}}
```


| Parameters      | Description                    |
|------------------|---------------------------------|
| Name            | ID                             |
| Type            | string                         |
| Description     | ID of the order.               |
| Required        | False                          |


| Parameters      | Description                    |
|------------------|---------------------------------|
| Name            | FromUser                       |
| Type            | object                         |
| Description     | From user of the order.        |
| Required        | False                          |


| Parameters      | Description                    |
|------------------|---------------------------------|
| Name            | FromCompanyID                  |
| Type            | string                         |
| Description     | ID of the from company.        |
| Required        | False                          |


| Parameters      | Description                    |
|------------------|---------------------------------|
| Name            | FromUserID                     |
| Type            | string                         |
| Description     | ID of the from user.           |
| Required        | False                          |


| Parameters      | Description                    |
|------------------|---------------------------------|
| Name            | BillingAddressID               |
| Type            | string                         |
| Description     | ID of the billing address.     |
| Required        | False                          |


| Parameters      | Description                    |
|------------------|---------------------------------|
| Name            | BillingAddress                 |
| Type            | object                         |
| Description     | Billing address of the order.  |
| Required        | False                          |


| Parameters      | Description                    |
|------------------|---------------------------------|
| Name            | ShippingAddressID              |
| Type            | string                         |
| Description     | ID of the Shipping Address for all LineItems on the Order. Null when there are multiple Shipping Addresses involved. |
| Required        | False                          |


| Parameters      | Description                    |
|------------------|---------------------------------|
| Name            | Comments                       |
| Type            | string                         |
| Description     | Comments of the order.         |
| Required        | False                          |


| Parameters      | Description                    |
|------------------|---------------------------------|
| Name            | LineItemCount                  |
| Type            | integer                        |
| Description     | Line item count of the order.  |
| Required        | False                          |


| Parameters      | Description                    |
|------------------|---------------------------------|
| Name            | Status                         |
| Type            | string                         |
| Description     | Status of the order. Possible values: Unsubmitted, AwaitingApproval, Declined, Open, Completed, Canceled. |
| Required        | False                          |


| Parameters      | Description                    |
|------------------|---------------------------------|
| Name            | DateCreated                    |
| Type            | date                           |
| Description     | Date created of the order.     |
| Required        | False                          |


| Parameters      | Description                    |
|------------------|---------------------------------|
| Name            | DateSubmitted                  |
| Type            | date                           |
| Description     | Date submitted of the order.   |
| Required        | False                          |


| Parameters      | Description                    |
|------------------|---------------------------------|
| Name            | DateApproved                   |
| Type            | date                           |
| Description     | Date approved of the order.    |
| Required        | False                          |


| Parameters      | Description                    |
|------------------|---------------------------------|
| Name            | DateDeclined                   |
| Type            | date                           |
| Description     | Date declined of the order.    |
| Required        | False                          |


| Parameters      | Description                    |
|------------------|---------------------------------|
| Name            | DateCanceled                   |
| Type            | date                           |
| Description     | Date canceled of the order.    |
| Required        | False                          |


| Parameters      | Description                    |
|------------------|---------------------------------|
| Name            | DateCompleted                  |
| Type            | date                           |
| Description     | Date completed of the order.   |
| Required        | False                          |


| Parameters      | Description                    |
|------------------|---------------------------------|
| Name            | Subtotal                       |
| Type            | float                          |
| Description     | Subtotal of the order.         |
| Required        | False                          |


| Parameters      | Description                    |
|------------------|---------------------------------|
| Name            | ShippingCost                   |
| Type            | float                          |
| Description     | Shipping cost of the order.    |
| Required        | False                          |


| Parameters      | Description                    |
|------------------|---------------------------------|
| Name            | TaxCost                        |
| Type            | float                          |
| Description     | Tax cost of the order.         |
| Required        | False                          |


| Parameters      | Description                    |
|------------------|---------------------------------|
| Name            | PromotionDiscount              |
| Type            | float                          |
| Description     | Promotion discount of the order. |
| Required        | False                          |


| Parameters      | Description                    |
|------------------|---------------------------------|
| Name            | Total                          |
| Type            | float                          |
| Description     | Total of the order.            |
| Required        | False                          |


| Parameters      | Description                    |
|------------------|---------------------------------|
| Name            | IsSubmitted                    |
| Type            | boolean                        |
| Description     | True if this Order has been passed from the Buyer to the Seller. |
| Required        | False                          |


| Parameters      | Description                    |
|------------------|---------------------------------|
| Name            | xp                             |
| Type            | object                         |
| Description     | Container for extended (custom) properties of the order. |
| Required        | False                          |
