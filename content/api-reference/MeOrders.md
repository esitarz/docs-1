---
title: Orders
date: 2018-03-23
category: API Reference
tags: Me And My Stuff
slug: MeOrders
---
"Me" is a container for read-only endpoints that return a filtered view
of things that the current buyer user is allowed to see, i.e. things
that they are assigned to either directly or as a member of a buyer
organization or user group. It also provides ways for a user to update
or change their own information.

---

## `GET` `v1/me/orders`
Get a list of orders visible to this user

| Parameters      | Description                    |
|------------------|---------------------------------|


| Parameters      | Description                    |
|------------------|---------------------------------|
| Name            | from                           |
| Type            | date                           |
| Description     | Lower bound of date range that the order was created (if outgoing) or submitted (if incoming). |
| Required        | False                          |


| Parameters      | Description                    |
|------------------|---------------------------------|
| Name            | to                             |
| Type            | date                           |
| Description     | Upper bound of date range that the order was created (if outgoing) or submitted (if incoming). |
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

## `GET` `v1/me/orders/approvable`
Get a list of orders that this user can approve

| Parameters      | Description                    |
|------------------|---------------------------------|


| Parameters      | Description                    |
|------------------|---------------------------------|
| Name            | from                           |
| Type            | date                           |
| Description     | Lower bound of date range that the order was created (if outgoing) or submitted (if incoming). |
| Required        | False                          |


| Parameters      | Description                    |
|------------------|---------------------------------|
| Name            | to                             |
| Type            | date                           |
| Description     | Upper bound of date range that the order was created (if outgoing) or submitted (if incoming). |
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
