---
title: Shipments
date: 2018-03-26
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

## Requestbody
**Responsestatus**: `200`

## Responsebody
```
{'ID': '', 'BuyerID': '', 'Shipper': '', 'DateShipped': '2018-03-21T23:00:00+00:00', 'DateDelivered': '2018-03-21T23:00:00+00:00', 'TrackingNumber': '', 'Cost': 0, 'xp': {}, 'Account': '', 'FromAddressID': '', 'ToAddressID': '', 'FromAddress': {'ID': '', 'DateCreated': '2018-03-21T23:00:00+00:00', 'CompanyName': '', 'FirstName': '', 'LastName': '', 'Street1': '', 'Street2': '', 'City': '', 'State': '', 'Zip': '', 'Country': '', 'Phone': '', 'AddressName': '', 'xp': {}}, 'ToAddress': {'ID': '', 'DateCreated': '2018-03-21T23:00:00+00:00', 'CompanyName': '', 'FirstName': '', 'LastName': '', 'Street1': '', 'Street2': '', 'City': '', 'State': '', 'Zip': '', 'Country': '', 'Phone': '', 'AddressName': '', 'xp': {}}}
```


| Parameters      | Description                    |
|------------------|---------------------------------|
| Name            | ID                             |
| Type            | string                         |
| Description     | ID of the shipment.            |
| Required        | False                          |


| Parameters      | Description                    |
|------------------|---------------------------------|
| Name            | BuyerID                        |
| Type            | string                         |
| Description     | ID of the buyer.               |
| Required        | False                          |


| Parameters      | Description                    |
|------------------|---------------------------------|
| Name            | Shipper                        |
| Type            | string                         |
| Description     | Shipper of the shipment.       |
| Required        | False                          |


| Parameters      | Description                    |
|------------------|---------------------------------|
| Name            | DateShipped                    |
| Type            | date                           |
| Description     | Date shipped of the shipment.  |
| Required        | False                          |


| Parameters      | Description                    |
|------------------|---------------------------------|
| Name            | DateDelivered                  |
| Type            | date                           |
| Description     | Date delivered of the shipment. |
| Required        | False                          |


| Parameters      | Description                    |
|------------------|---------------------------------|
| Name            | TrackingNumber                 |
| Type            | string                         |
| Description     | Tracking number of the shipment. |
| Required        | False                          |


| Parameters      | Description                    |
|------------------|---------------------------------|
| Name            | Cost                           |
| Type            | float                          |
| Description     | Cost of the shipment.          |
| Required        | False                          |


| Parameters      | Description                    |
|------------------|---------------------------------|
| Name            | xp                             |
| Type            | object                         |
| Description     | Container for extended (custom) properties of the shipment. |
| Required        | False                          |


| Parameters      | Description                    |
|------------------|---------------------------------|
| Name            | Account                        |
| Type            | string                         |
| Description     | Account of the shipment.       |
| Required        | False                          |


| Parameters      | Description                    |
|------------------|---------------------------------|
| Name            | FromAddressID                  |
| Type            | string                         |
| Description     | ID of the from address.        |
| Required        | False                          |


| Parameters      | Description                    |
|------------------|---------------------------------|
| Name            | ToAddressID                    |
| Type            | string                         |
| Description     | ID of the to address.          |
| Required        | False                          |


| Parameters      | Description                    |
|------------------|---------------------------------|
| Name            | FromAddress                    |
| Type            | object                         |
| Description     | From address of the shipment.  |
| Required        | False                          |


| Parameters      | Description                    |
|------------------|---------------------------------|
| Name            | ToAddress                      |
| Type            | object                         |
| Description     | To address of the shipment.    |
| Required        | False                          |

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

## Requestbody
**Responsestatus**: `200`

## Responsebody
```
{'Meta': {'Page': 1, 'PageSize': 20, 'TotalCount': 25, 'TotalPages': 2, 'ItemRange': [1, 20]}, 'Items': [{'ID': '', 'BuyerID': '', 'Shipper': '', 'DateShipped': '2018-03-21T23:00:00+00:00', 'DateDelivered': '2018-03-21T23:00:00+00:00', 'TrackingNumber': '', 'Cost': 0, 'xp': {}, 'Account': '', 'FromAddressID': '', 'ToAddressID': '', 'FromAddress': {'ID': '', 'DateCreated': '2018-03-21T23:00:00+00:00', 'CompanyName': '', 'FirstName': '', 'LastName': '', 'Street1': '', 'Street2': '', 'City': '', 'State': '', 'Zip': '', 'Country': '', 'Phone': '', 'AddressName': '', 'xp': {}}, 'ToAddress': {'ID': '', 'DateCreated': '2018-03-21T23:00:00+00:00', 'CompanyName': '', 'FirstName': '', 'LastName': '', 'Street1': '', 'Street2': '', 'City': '', 'State': '', 'Zip': '', 'Country': '', 'Phone': '', 'AddressName': '', 'xp': {}}}]}
```


| Parameters      | Description                    |
|------------------|---------------------------------|
| Name            | ID                             |
| Type            | string                         |
| Description     | ID of the shipment.            |
| Required        | False                          |


| Parameters      | Description                    |
|------------------|---------------------------------|
| Name            | BuyerID                        |
| Type            | string                         |
| Description     | ID of the buyer.               |
| Required        | False                          |


| Parameters      | Description                    |
|------------------|---------------------------------|
| Name            | Shipper                        |
| Type            | string                         |
| Description     | Shipper of the shipment.       |
| Required        | False                          |


| Parameters      | Description                    |
|------------------|---------------------------------|
| Name            | DateShipped                    |
| Type            | date                           |
| Description     | Date shipped of the shipment.  |
| Required        | False                          |


| Parameters      | Description                    |
|------------------|---------------------------------|
| Name            | DateDelivered                  |
| Type            | date                           |
| Description     | Date delivered of the shipment. |
| Required        | False                          |


| Parameters      | Description                    |
|------------------|---------------------------------|
| Name            | TrackingNumber                 |
| Type            | string                         |
| Description     | Tracking number of the shipment. |
| Required        | False                          |


| Parameters      | Description                    |
|------------------|---------------------------------|
| Name            | Cost                           |
| Type            | float                          |
| Description     | Cost of the shipment.          |
| Required        | False                          |


| Parameters      | Description                    |
|------------------|---------------------------------|
| Name            | xp                             |
| Type            | object                         |
| Description     | Container for extended (custom) properties of the shipment. |
| Required        | False                          |


| Parameters      | Description                    |
|------------------|---------------------------------|
| Name            | Account                        |
| Type            | string                         |
| Description     | Account of the shipment.       |
| Required        | False                          |


| Parameters      | Description                    |
|------------------|---------------------------------|
| Name            | FromAddressID                  |
| Type            | string                         |
| Description     | ID of the from address.        |
| Required        | False                          |


| Parameters      | Description                    |
|------------------|---------------------------------|
| Name            | ToAddressID                    |
| Type            | string                         |
| Description     | ID of the to address.          |
| Required        | False                          |


| Parameters      | Description                    |
|------------------|---------------------------------|
| Name            | FromAddress                    |
| Type            | object                         |
| Description     | From address of the shipment.  |
| Required        | False                          |


| Parameters      | Description                    |
|------------------|---------------------------------|
| Name            | ToAddress                      |
| Type            | object                         |
| Description     | To address of the shipment.    |
| Required        | False                          |

## `POST` `v1/shipments`
Create a new shipment
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
{'ID': '', 'BuyerID': '', 'Shipper': '', 'DateShipped': '2018-03-21T23:00:00+00:00', 'DateDelivered': '2018-03-21T23:00:00+00:00', 'TrackingNumber': '', 'Cost': 0, 'xp': {}, 'Account': '', 'FromAddressID': '', 'ToAddressID': '', 'FromAddress': {'ID': '', 'DateCreated': '2018-03-21T23:00:00+00:00', 'CompanyName': '', 'FirstName': '', 'LastName': '', 'Street1': '', 'Street2': '', 'City': '', 'State': '', 'Zip': '', 'Country': '', 'Phone': '', 'AddressName': '', 'xp': {}}, 'ToAddress': {'ID': '', 'DateCreated': '2018-03-21T23:00:00+00:00', 'CompanyName': '', 'FirstName': '', 'LastName': '', 'Street1': '', 'Street2': '', 'City': '', 'State': '', 'Zip': '', 'Country': '', 'Phone': '', 'AddressName': '', 'xp': {}}}
```


| Parameters      | Description                    |
|------------------|---------------------------------|
| Name            | ID                             |
| Type            | string                         |
| Description     | ID of the shipment.            |
| Required        | False                          |


| Parameters      | Description                    |
|------------------|---------------------------------|
| Name            | BuyerID                        |
| Type            | string                         |
| Description     | ID of the buyer.               |
| Required        | False                          |


| Parameters      | Description                    |
|------------------|---------------------------------|
| Name            | Shipper                        |
| Type            | string                         |
| Description     | Shipper of the shipment.       |
| Required        | False                          |


| Parameters      | Description                    |
|------------------|---------------------------------|
| Name            | DateShipped                    |
| Type            | date                           |
| Description     | Date shipped of the shipment.  |
| Required        | False                          |


| Parameters      | Description                    |
|------------------|---------------------------------|
| Name            | DateDelivered                  |
| Type            | date                           |
| Description     | Date delivered of the shipment. |
| Required        | False                          |


| Parameters      | Description                    |
|------------------|---------------------------------|
| Name            | TrackingNumber                 |
| Type            | string                         |
| Description     | Tracking number of the shipment. |
| Required        | False                          |


| Parameters      | Description                    |
|------------------|---------------------------------|
| Name            | Cost                           |
| Type            | float                          |
| Description     | Cost of the shipment.          |
| Required        | False                          |


| Parameters      | Description                    |
|------------------|---------------------------------|
| Name            | xp                             |
| Type            | object                         |
| Description     | Container for extended (custom) properties of the shipment. |
| Required        | False                          |


| Parameters      | Description                    |
|------------------|---------------------------------|
| Name            | Account                        |
| Type            | string                         |
| Description     | Account of the shipment.       |
| Required        | False                          |


| Parameters      | Description                    |
|------------------|---------------------------------|
| Name            | FromAddressID                  |
| Type            | string                         |
| Description     | ID of the from address.        |
| Required        | False                          |


| Parameters      | Description                    |
|------------------|---------------------------------|
| Name            | ToAddressID                    |
| Type            | string                         |
| Description     | ID of the to address.          |
| Required        | False                          |


| Parameters      | Description                    |
|------------------|---------------------------------|
| Name            | FromAddress                    |
| Type            | object                         |
| Description     | From address of the shipment.  |
| Required        | False                          |


| Parameters      | Description                    |
|------------------|---------------------------------|
| Name            | ToAddress                      |
| Type            | object                         |
| Description     | To address of the shipment.    |
| Required        | False                          |

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

## Requestbody
```
{'ID': '', 'BuyerID': '', 'Shipper': '', 'DateShipped': '2018-03-21T23:00:00+00:00', 'DateDelivered': '2018-03-21T23:00:00+00:00', 'TrackingNumber': '', 'Cost': 0, 'xp': {}, 'Account': '', 'FromAddressID': '', 'ToAddressID': ''}
```

```
[{'Name': 'ID', 'Type': 'string', 'Description': 'ID of the shipment. Can only contain characters Aa-Zz, 0-9, -, and _. Searchable: priority level 1. Sortable.', 'Required': False}, {'Name': 'BuyerID', 'Type': 'string', 'Description': 'ID of the buyer. Searchable: priority level 1. Sortable.', 'Required': False}, {'Name': 'Shipper', 'Type': 'string', 'Description': 'Shipper of the shipment. Searchable: priority level 2. Sortable.', 'Required': False}, {'Name': 'DateShipped', 'Type': 'date', 'Description': 'Date shipped of the shipment. Searchable: priority level 3. Sortable: priority level 1.', 'Required': False}, {'Name': 'DateDelivered', 'Type': 'date', 'Description': 'Date delivered of the shipment. Searchable: priority level 4. Sortable.', 'Required': False}, {'Name': 'TrackingNumber', 'Type': 'string', 'Description': 'Tracking number of the shipment. Max length 3000 characters. Searchable: priority level 4.', 'Required': False}, {'Name': 'Cost', 'Type': 'float', 'Description': 'Cost of the shipment. Sortable.', 'Required': False}, {'Name': 'xp', 'Type': 'object', 'Description': 'Container for extended (custom) properties of the shipment.', 'Required': False}, {'Name': 'Account', 'Type': 'string', 'Description': 'Account of the shipment.', 'Required': False}, {'Name': 'FromAddressID', 'Type': 'string', 'Description': 'ID of the from address.', 'Required': False}, {'Name': 'ToAddressID', 'Type': 'string', 'Description': 'ID of the to address.', 'Required': False}]
```

**Responsestatus**: `200`

## Responsebody
```
{'ID': '', 'BuyerID': '', 'Shipper': '', 'DateShipped': '2018-03-21T23:00:00+00:00', 'DateDelivered': '2018-03-21T23:00:00+00:00', 'TrackingNumber': '', 'Cost': 0, 'xp': {}, 'Account': '', 'FromAddressID': '', 'ToAddressID': '', 'FromAddress': {'ID': '', 'DateCreated': '2018-03-21T23:00:00+00:00', 'CompanyName': '', 'FirstName': '', 'LastName': '', 'Street1': '', 'Street2': '', 'City': '', 'State': '', 'Zip': '', 'Country': '', 'Phone': '', 'AddressName': '', 'xp': {}}, 'ToAddress': {'ID': '', 'DateCreated': '2018-03-21T23:00:00+00:00', 'CompanyName': '', 'FirstName': '', 'LastName': '', 'Street1': '', 'Street2': '', 'City': '', 'State': '', 'Zip': '', 'Country': '', 'Phone': '', 'AddressName': '', 'xp': {}}}
```


| Parameters      | Description                    |
|------------------|---------------------------------|
| Name            | ID                             |
| Type            | string                         |
| Description     | ID of the shipment.            |
| Required        | False                          |


| Parameters      | Description                    |
|------------------|---------------------------------|
| Name            | BuyerID                        |
| Type            | string                         |
| Description     | ID of the buyer.               |
| Required        | False                          |


| Parameters      | Description                    |
|------------------|---------------------------------|
| Name            | Shipper                        |
| Type            | string                         |
| Description     | Shipper of the shipment.       |
| Required        | False                          |


| Parameters      | Description                    |
|------------------|---------------------------------|
| Name            | DateShipped                    |
| Type            | date                           |
| Description     | Date shipped of the shipment.  |
| Required        | False                          |


| Parameters      | Description                    |
|------------------|---------------------------------|
| Name            | DateDelivered                  |
| Type            | date                           |
| Description     | Date delivered of the shipment. |
| Required        | False                          |


| Parameters      | Description                    |
|------------------|---------------------------------|
| Name            | TrackingNumber                 |
| Type            | string                         |
| Description     | Tracking number of the shipment. |
| Required        | False                          |


| Parameters      | Description                    |
|------------------|---------------------------------|
| Name            | Cost                           |
| Type            | float                          |
| Description     | Cost of the shipment.          |
| Required        | False                          |


| Parameters      | Description                    |
|------------------|---------------------------------|
| Name            | xp                             |
| Type            | object                         |
| Description     | Container for extended (custom) properties of the shipment. |
| Required        | False                          |


| Parameters      | Description                    |
|------------------|---------------------------------|
| Name            | Account                        |
| Type            | string                         |
| Description     | Account of the shipment.       |
| Required        | False                          |


| Parameters      | Description                    |
|------------------|---------------------------------|
| Name            | FromAddressID                  |
| Type            | string                         |
| Description     | ID of the from address.        |
| Required        | False                          |


| Parameters      | Description                    |
|------------------|---------------------------------|
| Name            | ToAddressID                    |
| Type            | string                         |
| Description     | ID of the to address.          |
| Required        | False                          |


| Parameters      | Description                    |
|------------------|---------------------------------|
| Name            | FromAddress                    |
| Type            | object                         |
| Description     | From address of the shipment.  |
| Required        | False                          |


| Parameters      | Description                    |
|------------------|---------------------------------|
| Name            | ToAddress                      |
| Type            | object                         |
| Description     | To address of the shipment.    |
| Required        | False                          |

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

## Requestbody
**Responsestatus**: `204`

## Responsebody
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

## Requestbody
```
{'ID': '', 'BuyerID': '', 'Shipper': '', 'DateShipped': '2018-03-21T23:00:00+00:00', 'DateDelivered': '2018-03-21T23:00:00+00:00', 'TrackingNumber': '', 'Cost': 0, 'xp': {}, 'Account': '', 'FromAddressID': '', 'ToAddressID': ''}
```

```
[{'Name': 'ID', 'Type': 'string', 'Description': 'ID of the shipment. Can only contain characters Aa-Zz, 0-9, -, and _. Searchable: priority level 1. Sortable.', 'Required': False}, {'Name': 'BuyerID', 'Type': 'string', 'Description': 'ID of the buyer. Searchable: priority level 1. Sortable.', 'Required': False}, {'Name': 'Shipper', 'Type': 'string', 'Description': 'Shipper of the shipment. Searchable: priority level 2. Sortable.', 'Required': False}, {'Name': 'DateShipped', 'Type': 'date', 'Description': 'Date shipped of the shipment. Searchable: priority level 3. Sortable: priority level 1.', 'Required': False}, {'Name': 'DateDelivered', 'Type': 'date', 'Description': 'Date delivered of the shipment. Searchable: priority level 4. Sortable.', 'Required': False}, {'Name': 'TrackingNumber', 'Type': 'string', 'Description': 'Tracking number of the shipment. Max length 3000 characters. Searchable: priority level 4.', 'Required': False}, {'Name': 'Cost', 'Type': 'float', 'Description': 'Cost of the shipment. Sortable.', 'Required': False}, {'Name': 'xp', 'Type': 'object', 'Description': 'Container for extended (custom) properties of the shipment.', 'Required': False}, {'Name': 'Account', 'Type': 'string', 'Description': 'Account of the shipment.', 'Required': False}, {'Name': 'FromAddressID', 'Type': 'string', 'Description': 'ID of the from address.', 'Required': False}, {'Name': 'ToAddressID', 'Type': 'string', 'Description': 'ID of the to address.', 'Required': False}]
```

**Responsestatus**: `200`

## Responsebody
```
{'ID': '', 'BuyerID': '', 'Shipper': '', 'DateShipped': '2018-03-21T23:00:00+00:00', 'DateDelivered': '2018-03-21T23:00:00+00:00', 'TrackingNumber': '', 'Cost': 0, 'xp': {}, 'Account': '', 'FromAddressID': '', 'ToAddressID': '', 'FromAddress': {'ID': '', 'DateCreated': '2018-03-21T23:00:00+00:00', 'CompanyName': '', 'FirstName': '', 'LastName': '', 'Street1': '', 'Street2': '', 'City': '', 'State': '', 'Zip': '', 'Country': '', 'Phone': '', 'AddressName': '', 'xp': {}}, 'ToAddress': {'ID': '', 'DateCreated': '2018-03-21T23:00:00+00:00', 'CompanyName': '', 'FirstName': '', 'LastName': '', 'Street1': '', 'Street2': '', 'City': '', 'State': '', 'Zip': '', 'Country': '', 'Phone': '', 'AddressName': '', 'xp': {}}}
```


| Parameters      | Description                    |
|------------------|---------------------------------|
| Name            | ID                             |
| Type            | string                         |
| Description     | ID of the shipment.            |
| Required        | False                          |


| Parameters      | Description                    |
|------------------|---------------------------------|
| Name            | BuyerID                        |
| Type            | string                         |
| Description     | ID of the buyer.               |
| Required        | False                          |


| Parameters      | Description                    |
|------------------|---------------------------------|
| Name            | Shipper                        |
| Type            | string                         |
| Description     | Shipper of the shipment.       |
| Required        | False                          |


| Parameters      | Description                    |
|------------------|---------------------------------|
| Name            | DateShipped                    |
| Type            | date                           |
| Description     | Date shipped of the shipment.  |
| Required        | False                          |


| Parameters      | Description                    |
|------------------|---------------------------------|
| Name            | DateDelivered                  |
| Type            | date                           |
| Description     | Date delivered of the shipment. |
| Required        | False                          |


| Parameters      | Description                    |
|------------------|---------------------------------|
| Name            | TrackingNumber                 |
| Type            | string                         |
| Description     | Tracking number of the shipment. |
| Required        | False                          |


| Parameters      | Description                    |
|------------------|---------------------------------|
| Name            | Cost                           |
| Type            | float                          |
| Description     | Cost of the shipment.          |
| Required        | False                          |


| Parameters      | Description                    |
|------------------|---------------------------------|
| Name            | xp                             |
| Type            | object                         |
| Description     | Container for extended (custom) properties of the shipment. |
| Required        | False                          |


| Parameters      | Description                    |
|------------------|---------------------------------|
| Name            | Account                        |
| Type            | string                         |
| Description     | Account of the shipment.       |
| Required        | False                          |


| Parameters      | Description                    |
|------------------|---------------------------------|
| Name            | FromAddressID                  |
| Type            | string                         |
| Description     | ID of the from address.        |
| Required        | False                          |


| Parameters      | Description                    |
|------------------|---------------------------------|
| Name            | ToAddressID                    |
| Type            | string                         |
| Description     | ID of the to address.          |
| Required        | False                          |


| Parameters      | Description                    |
|------------------|---------------------------------|
| Name            | FromAddress                    |
| Type            | object                         |
| Description     | From address of the shipment.  |
| Required        | False                          |


| Parameters      | Description                    |
|------------------|---------------------------------|
| Name            | ToAddress                      |
| Type            | object                         |
| Description     | To address of the shipment.    |
| Required        | False                          |

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

## Requestbody
**Responsestatus**: `200`

## Responsebody
```
{'Meta': {'Page': 1, 'PageSize': 20, 'TotalCount': 25, 'TotalPages': 2, 'ItemRange': [1, 20]}, 'Items': [{'OrderID': '', 'LineItemID': '', 'QuantityShipped': 0, 'UnitPrice': 0, 'CostCenter': '', 'DateNeeded': '2018-03-21T23:00:00+00:00', 'Product': {'ID': '', 'Name': '', 'Description': '', 'QuantityMultiplier': 0, 'ShipWeight': 0, 'ShipHeight': 0, 'ShipWidth': 0, 'ShipLength': 0, 'xp': {}}, 'Specs': [{'SpecID': '', 'Name': '', 'OptionID': '', 'Value': ''}], 'xp': {}}]}
```


| Parameters      | Description                    |
|------------------|---------------------------------|
| Name            | OrderID                        |
| Type            | string                         |
| Description     | ID of the order.               |
| Required        | True                           |


| Parameters      | Description                    |
|------------------|---------------------------------|
| Name            | LineItemID                     |
| Type            | string                         |
| Description     | ID of the line item.           |
| Required        | True                           |


| Parameters      | Description                    |
|------------------|---------------------------------|
| Name            | QuantityShipped                |
| Type            | integer                        |
| Description     | Quantity shipped of the shipment item. |
| Required        | True                           |


| Parameters      | Description                    |
|------------------|---------------------------------|
| Name            | UnitPrice                      |
| Type            | float                          |
| Description     | Unit price of the shipment item. |
| Required        | False                          |


| Parameters      | Description                    |
|------------------|---------------------------------|
| Name            | CostCenter                     |
| Type            | string                         |
| Description     | Cost center of the shipment item. |
| Required        | False                          |


| Parameters      | Description                    |
|------------------|---------------------------------|
| Name            | DateNeeded                     |
| Type            | date                           |
| Description     | Date needed of the shipment item. |
| Required        | False                          |


| Parameters      | Description                    |
|------------------|---------------------------------|
| Name            | Product                        |
| Type            | object                         |
| Description     | Product of the shipment item.  |
| Required        | False                          |


| Parameters      | Description                    |
|------------------|---------------------------------|
| Name            | Specs                          |
| Type            | array                          |
| Description     | Specs of the shipment item.    |
| Required        | False                          |


| Parameters      | Description                    |
|------------------|---------------------------------|
| Name            | xp                             |
| Type            | object                         |
| Description     | Container for extended (custom) properties of the shipment item. |
| Required        | False                          |

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

## Requestbody
**Responsestatus**: `200`

## Responsebody
```
{'OrderID': '', 'LineItemID': '', 'QuantityShipped': 0, 'UnitPrice': 0, 'CostCenter': '', 'DateNeeded': '2018-03-21T23:00:00+00:00', 'Product': {'ID': '', 'Name': '', 'Description': '', 'QuantityMultiplier': 0, 'ShipWeight': 0, 'ShipHeight': 0, 'ShipWidth': 0, 'ShipLength': 0, 'xp': {}}, 'Specs': [{'SpecID': '', 'Name': '', 'OptionID': '', 'Value': ''}], 'xp': {}}
```


| Parameters      | Description                    |
|------------------|---------------------------------|
| Name            | OrderID                        |
| Type            | string                         |
| Description     | ID of the order.               |
| Required        | True                           |


| Parameters      | Description                    |
|------------------|---------------------------------|
| Name            | LineItemID                     |
| Type            | string                         |
| Description     | ID of the line item.           |
| Required        | True                           |


| Parameters      | Description                    |
|------------------|---------------------------------|
| Name            | QuantityShipped                |
| Type            | integer                        |
| Description     | Quantity shipped of the shipment item. |
| Required        | True                           |


| Parameters      | Description                    |
|------------------|---------------------------------|
| Name            | UnitPrice                      |
| Type            | float                          |
| Description     | Unit price of the shipment item. |
| Required        | False                          |


| Parameters      | Description                    |
|------------------|---------------------------------|
| Name            | CostCenter                     |
| Type            | string                         |
| Description     | Cost center of the shipment item. |
| Required        | False                          |


| Parameters      | Description                    |
|------------------|---------------------------------|
| Name            | DateNeeded                     |
| Type            | date                           |
| Description     | Date needed of the shipment item. |
| Required        | False                          |


| Parameters      | Description                    |
|------------------|---------------------------------|
| Name            | Product                        |
| Type            | object                         |
| Description     | Product of the shipment item.  |
| Required        | False                          |


| Parameters      | Description                    |
|------------------|---------------------------------|
| Name            | Specs                          |
| Type            | array                          |
| Description     | Specs of the shipment item.    |
| Required        | False                          |


| Parameters      | Description                    |
|------------------|---------------------------------|
| Name            | xp                             |
| Type            | object                         |
| Description     | Container for extended (custom) properties of the shipment item. |
| Required        | False                          |

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

## Requestbody
```
{'OrderID': '', 'LineItemID': '', 'QuantityShipped': 0}
```

```
[{'Name': 'OrderID', 'Type': 'string', 'Description': 'ID of the order. Required.', 'Required': True}, {'Name': 'LineItemID', 'Type': 'string', 'Description': 'ID of the line item. Required.', 'Required': True}, {'Name': 'QuantityShipped', 'Type': 'integer', 'Description': 'Quantity shipped of the shipment item. Required.', 'Required': True}]
```

**Responsestatus**: `200`

## Responsebody
```
{'OrderID': '', 'LineItemID': '', 'QuantityShipped': 0, 'UnitPrice': 0, 'CostCenter': '', 'DateNeeded': '2018-03-21T23:00:00+00:00', 'Product': {'ID': '', 'Name': '', 'Description': '', 'QuantityMultiplier': 0, 'ShipWeight': 0, 'ShipHeight': 0, 'ShipWidth': 0, 'ShipLength': 0, 'xp': {}}, 'Specs': [{'SpecID': '', 'Name': '', 'OptionID': '', 'Value': ''}], 'xp': {}}
```


| Parameters      | Description                    |
|------------------|---------------------------------|
| Name            | OrderID                        |
| Type            | string                         |
| Description     | ID of the order.               |
| Required        | True                           |


| Parameters      | Description                    |
|------------------|---------------------------------|
| Name            | LineItemID                     |
| Type            | string                         |
| Description     | ID of the line item.           |
| Required        | True                           |


| Parameters      | Description                    |
|------------------|---------------------------------|
| Name            | QuantityShipped                |
| Type            | integer                        |
| Description     | Quantity shipped of the shipment item. |
| Required        | True                           |


| Parameters      | Description                    |
|------------------|---------------------------------|
| Name            | UnitPrice                      |
| Type            | float                          |
| Description     | Unit price of the shipment item. |
| Required        | False                          |


| Parameters      | Description                    |
|------------------|---------------------------------|
| Name            | CostCenter                     |
| Type            | string                         |
| Description     | Cost center of the shipment item. |
| Required        | False                          |


| Parameters      | Description                    |
|------------------|---------------------------------|
| Name            | DateNeeded                     |
| Type            | date                           |
| Description     | Date needed of the shipment item. |
| Required        | False                          |


| Parameters      | Description                    |
|------------------|---------------------------------|
| Name            | Product                        |
| Type            | object                         |
| Description     | Product of the shipment item.  |
| Required        | False                          |


| Parameters      | Description                    |
|------------------|---------------------------------|
| Name            | Specs                          |
| Type            | array                          |
| Description     | Specs of the shipment item.    |
| Required        | False                          |


| Parameters      | Description                    |
|------------------|---------------------------------|
| Name            | xp                             |
| Type            | object                         |
| Description     | Container for extended (custom) properties of the shipment item. |
| Required        | False                          |

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

## Requestbody
**Responsestatus**: `204`

## Responsebody