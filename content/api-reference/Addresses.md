---
title: Addresses
date: 2018-03-23
category: API Reference
tags: Buyers
slug: Addresses
---
Addresses are used for the purposes of billing and shipping an order. An
address may belong to a list that can be shared among many users if
appropriate.

---

## `GET` `v1/buyers/{buyerID}/addresses/{addressID}`
Get a single address

| Parameters      | Description                    |
|------------------|---------------------------------|


| Parameters      | Description                    |
|------------------|---------------------------------|
| Name            | buyerID                        |
| Type            | string                         |
| Description     | ID of the buyer.               |
| Required        | True                           |


| Parameters      | Description                    |
|------------------|---------------------------------|
| Name            | addressID                      |
| Type            | string                         |
| Description     | ID of the address.             |
| Required        | True                           |

## Requestbody
**Responsestatus**: `200`

## Responsebody
```
{'ID': '', 'DateCreated': '2018-03-21T23:00:00+00:00', 'CompanyName': '', 'FirstName': '', 'LastName': '', 'Street1': '', 'Street2': '', 'City': '', 'State': '', 'Zip': '', 'Country': '', 'Phone': '', 'AddressName': '', 'xp': {}}
```


| Parameters      | Description                    |
|------------------|---------------------------------|
| Name            | ID                             |
| Type            | string                         |
| Description     | ID of the address.             |
| Required        | False                          |


| Parameters      | Description                    |
|------------------|---------------------------------|
| Name            | DateCreated                    |
| Type            | date                           |
| Description     | Date created of the address.   |
| Required        | False                          |


| Parameters      | Description                    |
|------------------|---------------------------------|
| Name            | CompanyName                    |
| Type            | string                         |
| Description     | Company name of the address.   |
| Required        | False                          |


| Parameters      | Description                    |
|------------------|---------------------------------|
| Name            | FirstName                      |
| Type            | string                         |
| Description     | First name of the address.     |
| Required        | False                          |


| Parameters      | Description                    |
|------------------|---------------------------------|
| Name            | LastName                       |
| Type            | string                         |
| Description     | Last name of the address.      |
| Required        | False                          |


| Parameters      | Description                    |
|------------------|---------------------------------|
| Name            | Street1                        |
| Type            | string                         |
| Description     | Street 1 of the address.       |
| Required        | True                           |


| Parameters      | Description                    |
|------------------|---------------------------------|
| Name            | Street2                        |
| Type            | string                         |
| Description     | Street 2 of the address.       |
| Required        | False                          |


| Parameters      | Description                    |
|------------------|---------------------------------|
| Name            | City                           |
| Type            | string                         |
| Description     | City of the address.           |
| Required        | True                           |


| Parameters      | Description                    |
|------------------|---------------------------------|
| Name            | State                          |
| Type            | string                         |
| Description     | State of the address.          |
| Required        | True                           |


| Parameters      | Description                    |
|------------------|---------------------------------|
| Name            | Zip                            |
| Type            | string                         |
| Description     | Zip of the address.            |
| Required        | True                           |


| Parameters      | Description                    |
|------------------|---------------------------------|
| Name            | Country                        |
| Type            | string                         |
| Description     | Country of the address.        |
| Required        | True                           |


| Parameters      | Description                    |
|------------------|---------------------------------|
| Name            | Phone                          |
| Type            | string                         |
| Description     | Phone of the address.          |
| Required        | False                          |


| Parameters      | Description                    |
|------------------|---------------------------------|
| Name            | AddressName                    |
| Type            | string                         |
| Description     | Address name of the address.   |
| Required        | False                          |


| Parameters      | Description                    |
|------------------|---------------------------------|
| Name            | xp                             |
| Type            | object                         |
| Description     | Container for extended (custom) properties of the address. |
| Required        | False                          |

## `GET` `v1/buyers/{buyerID}/addresses`
Get a list of addresses

| Parameters      | Description                    |
|------------------|---------------------------------|


| Parameters      | Description                    |
|------------------|---------------------------------|
| Name            | buyerID                        |
| Type            | string                         |
| Description     | ID of the buyer.               |
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
{'Meta': {'Page': 1, 'PageSize': 20, 'TotalCount': 25, 'TotalPages': 2, 'ItemRange': [1, 20]}, 'Items': [{'ID': '', 'DateCreated': '2018-03-21T23:00:00+00:00', 'CompanyName': '', 'FirstName': '', 'LastName': '', 'Street1': '', 'Street2': '', 'City': '', 'State': '', 'Zip': '', 'Country': '', 'Phone': '', 'AddressName': '', 'xp': {}}]}
```


| Parameters      | Description                    |
|------------------|---------------------------------|
| Name            | ID                             |
| Type            | string                         |
| Description     | ID of the address.             |
| Required        | False                          |


| Parameters      | Description                    |
|------------------|---------------------------------|
| Name            | DateCreated                    |
| Type            | date                           |
| Description     | Date created of the address.   |
| Required        | False                          |


| Parameters      | Description                    |
|------------------|---------------------------------|
| Name            | CompanyName                    |
| Type            | string                         |
| Description     | Company name of the address.   |
| Required        | False                          |


| Parameters      | Description                    |
|------------------|---------------------------------|
| Name            | FirstName                      |
| Type            | string                         |
| Description     | First name of the address.     |
| Required        | False                          |


| Parameters      | Description                    |
|------------------|---------------------------------|
| Name            | LastName                       |
| Type            | string                         |
| Description     | Last name of the address.      |
| Required        | False                          |


| Parameters      | Description                    |
|------------------|---------------------------------|
| Name            | Street1                        |
| Type            | string                         |
| Description     | Street 1 of the address.       |
| Required        | True                           |


| Parameters      | Description                    |
|------------------|---------------------------------|
| Name            | Street2                        |
| Type            | string                         |
| Description     | Street 2 of the address.       |
| Required        | False                          |


| Parameters      | Description                    |
|------------------|---------------------------------|
| Name            | City                           |
| Type            | string                         |
| Description     | City of the address.           |
| Required        | True                           |


| Parameters      | Description                    |
|------------------|---------------------------------|
| Name            | State                          |
| Type            | string                         |
| Description     | State of the address.          |
| Required        | True                           |


| Parameters      | Description                    |
|------------------|---------------------------------|
| Name            | Zip                            |
| Type            | string                         |
| Description     | Zip of the address.            |
| Required        | True                           |


| Parameters      | Description                    |
|------------------|---------------------------------|
| Name            | Country                        |
| Type            | string                         |
| Description     | Country of the address.        |
| Required        | True                           |


| Parameters      | Description                    |
|------------------|---------------------------------|
| Name            | Phone                          |
| Type            | string                         |
| Description     | Phone of the address.          |
| Required        | False                          |


| Parameters      | Description                    |
|------------------|---------------------------------|
| Name            | AddressName                    |
| Type            | string                         |
| Description     | Address name of the address.   |
| Required        | False                          |


| Parameters      | Description                    |
|------------------|---------------------------------|
| Name            | xp                             |
| Type            | object                         |
| Description     | Container for extended (custom) properties of the address. |
| Required        | False                          |

## `POST` `v1/buyers/{buyerID}/addresses`
Create a new address

| Parameters      | Description                    |
|------------------|---------------------------------|


| Parameters      | Description                    |
|------------------|---------------------------------|
| Name            | buyerID                        |
| Type            | string                         |
| Description     | ID of the buyer.               |
| Required        | True                           |

## Requestbody
```
{'ID': '', 'CompanyName': '', 'FirstName': '', 'LastName': '', 'Street1': '', 'Street2': '', 'City': '', 'State': '', 'Zip': '', 'Country': '', 'Phone': '', 'AddressName': '', 'xp': {}}
```

```
[{'Name': 'ID', 'Type': 'string', 'Description': 'ID of the address. Can only contain characters Aa-Zz, 0-9, -, and _. Searchable: priority level 1. Sortable: priority level 2.', 'Required': False}, {'Name': 'CompanyName', 'Type': 'string', 'Description': 'Company name of the address. Max length 100 characters. Sortable.', 'Required': False}, {'Name': 'FirstName', 'Type': 'string', 'Description': 'First name of the address. Max length 100 characters. Searchable: priority level 7. Sortable.', 'Required': False}, {'Name': 'LastName', 'Type': 'string', 'Description': 'Last name of the address. Max length 100 characters. Searchable: priority level 6. Sortable.', 'Required': False}, {'Name': 'Street1', 'Type': 'string', 'Description': 'Street 1 of the address. Required. Max length 100 characters. Searchable: priority level 4. Sortable.', 'Required': True}, {'Name': 'Street2', 'Type': 'string', 'Description': 'Street 2 of the address. Max length 100 characters. Searchable: priority level 5. Sortable.', 'Required': False}, {'Name': 'City', 'Type': 'string', 'Description': 'City of the address. Required. Max length 100 characters. Searchable: priority level 3. Sortable.', 'Required': True}, {'Name': 'State', 'Type': 'string', 'Description': 'State of the address. Required. Max length 100 characters. Searchable: priority level 7. Sortable.', 'Required': True}, {'Name': 'Zip', 'Type': 'string', 'Description': 'Zip of the address. Required. Max length 100 characters. Searchable: priority level 6. Sortable.', 'Required': True}, {'Name': 'Country', 'Type': 'string', 'Description': 'Country of the address. Required. Max length 2 characters. Sortable.', 'Required': True}, {'Name': 'Phone', 'Type': 'string', 'Description': 'Phone of the address. Max length 100 characters. Sortable.', 'Required': False}, {'Name': 'AddressName', 'Type': 'string', 'Description': 'Address name of the address. Max length 100 characters. Searchable: priority level 2. Sortable: priority level 1.', 'Required': False}, {'Name': 'xp', 'Type': 'object', 'Description': 'Container for extended (custom) properties of the address.', 'Required': False}]
```

**Responsestatus**: `201`

## Responsebody
```
{'ID': '', 'DateCreated': '2018-03-21T23:00:00+00:00', 'CompanyName': '', 'FirstName': '', 'LastName': '', 'Street1': '', 'Street2': '', 'City': '', 'State': '', 'Zip': '', 'Country': '', 'Phone': '', 'AddressName': '', 'xp': {}}
```


| Parameters      | Description                    |
|------------------|---------------------------------|
| Name            | ID                             |
| Type            | string                         |
| Description     | ID of the address.             |
| Required        | False                          |


| Parameters      | Description                    |
|------------------|---------------------------------|
| Name            | DateCreated                    |
| Type            | date                           |
| Description     | Date created of the address.   |
| Required        | False                          |


| Parameters      | Description                    |
|------------------|---------------------------------|
| Name            | CompanyName                    |
| Type            | string                         |
| Description     | Company name of the address.   |
| Required        | False                          |


| Parameters      | Description                    |
|------------------|---------------------------------|
| Name            | FirstName                      |
| Type            | string                         |
| Description     | First name of the address.     |
| Required        | False                          |


| Parameters      | Description                    |
|------------------|---------------------------------|
| Name            | LastName                       |
| Type            | string                         |
| Description     | Last name of the address.      |
| Required        | False                          |


| Parameters      | Description                    |
|------------------|---------------------------------|
| Name            | Street1                        |
| Type            | string                         |
| Description     | Street 1 of the address.       |
| Required        | True                           |


| Parameters      | Description                    |
|------------------|---------------------------------|
| Name            | Street2                        |
| Type            | string                         |
| Description     | Street 2 of the address.       |
| Required        | False                          |


| Parameters      | Description                    |
|------------------|---------------------------------|
| Name            | City                           |
| Type            | string                         |
| Description     | City of the address.           |
| Required        | True                           |


| Parameters      | Description                    |
|------------------|---------------------------------|
| Name            | State                          |
| Type            | string                         |
| Description     | State of the address.          |
| Required        | True                           |


| Parameters      | Description                    |
|------------------|---------------------------------|
| Name            | Zip                            |
| Type            | string                         |
| Description     | Zip of the address.            |
| Required        | True                           |


| Parameters      | Description                    |
|------------------|---------------------------------|
| Name            | Country                        |
| Type            | string                         |
| Description     | Country of the address.        |
| Required        | True                           |


| Parameters      | Description                    |
|------------------|---------------------------------|
| Name            | Phone                          |
| Type            | string                         |
| Description     | Phone of the address.          |
| Required        | False                          |


| Parameters      | Description                    |
|------------------|---------------------------------|
| Name            | AddressName                    |
| Type            | string                         |
| Description     | Address name of the address.   |
| Required        | False                          |


| Parameters      | Description                    |
|------------------|---------------------------------|
| Name            | xp                             |
| Type            | object                         |
| Description     | Container for extended (custom) properties of the address. |
| Required        | False                          |

## `PUT` `v1/buyers/{buyerID}/addresses/{addressID}`
Create or update an address

| Parameters      | Description                    |
|------------------|---------------------------------|


| Parameters      | Description                    |
|------------------|---------------------------------|
| Name            | buyerID                        |
| Type            | string                         |
| Description     | ID of the buyer.               |
| Required        | True                           |


| Parameters      | Description                    |
|------------------|---------------------------------|
| Name            | addressID                      |
| Type            | string                         |
| Description     | ID of the address.             |
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
{'ID': '', 'DateCreated': '2018-03-21T23:00:00+00:00', 'CompanyName': '', 'FirstName': '', 'LastName': '', 'Street1': '', 'Street2': '', 'City': '', 'State': '', 'Zip': '', 'Country': '', 'Phone': '', 'AddressName': '', 'xp': {}}
```


| Parameters      | Description                    |
|------------------|---------------------------------|
| Name            | ID                             |
| Type            | string                         |
| Description     | ID of the address.             |
| Required        | False                          |


| Parameters      | Description                    |
|------------------|---------------------------------|
| Name            | DateCreated                    |
| Type            | date                           |
| Description     | Date created of the address.   |
| Required        | False                          |


| Parameters      | Description                    |
|------------------|---------------------------------|
| Name            | CompanyName                    |
| Type            | string                         |
| Description     | Company name of the address.   |
| Required        | False                          |


| Parameters      | Description                    |
|------------------|---------------------------------|
| Name            | FirstName                      |
| Type            | string                         |
| Description     | First name of the address.     |
| Required        | False                          |


| Parameters      | Description                    |
|------------------|---------------------------------|
| Name            | LastName                       |
| Type            | string                         |
| Description     | Last name of the address.      |
| Required        | False                          |


| Parameters      | Description                    |
|------------------|---------------------------------|
| Name            | Street1                        |
| Type            | string                         |
| Description     | Street 1 of the address.       |
| Required        | True                           |


| Parameters      | Description                    |
|------------------|---------------------------------|
| Name            | Street2                        |
| Type            | string                         |
| Description     | Street 2 of the address.       |
| Required        | False                          |


| Parameters      | Description                    |
|------------------|---------------------------------|
| Name            | City                           |
| Type            | string                         |
| Description     | City of the address.           |
| Required        | True                           |


| Parameters      | Description                    |
|------------------|---------------------------------|
| Name            | State                          |
| Type            | string                         |
| Description     | State of the address.          |
| Required        | True                           |


| Parameters      | Description                    |
|------------------|---------------------------------|
| Name            | Zip                            |
| Type            | string                         |
| Description     | Zip of the address.            |
| Required        | True                           |


| Parameters      | Description                    |
|------------------|---------------------------------|
| Name            | Country                        |
| Type            | string                         |
| Description     | Country of the address.        |
| Required        | True                           |


| Parameters      | Description                    |
|------------------|---------------------------------|
| Name            | Phone                          |
| Type            | string                         |
| Description     | Phone of the address.          |
| Required        | False                          |


| Parameters      | Description                    |
|------------------|---------------------------------|
| Name            | AddressName                    |
| Type            | string                         |
| Description     | Address name of the address.   |
| Required        | False                          |


| Parameters      | Description                    |
|------------------|---------------------------------|
| Name            | xp                             |
| Type            | object                         |
| Description     | Container for extended (custom) properties of the address. |
| Required        | False                          |

## `DELETE` `v1/buyers/{buyerID}/addresses/{addressID}`
Delete an address

| Parameters      | Description                    |
|------------------|---------------------------------|


| Parameters      | Description                    |
|------------------|---------------------------------|
| Name            | buyerID                        |
| Type            | string                         |
| Description     | ID of the buyer.               |
| Required        | True                           |


| Parameters      | Description                    |
|------------------|---------------------------------|
| Name            | addressID                      |
| Type            | string                         |
| Description     | ID of the address.             |
| Required        | True                           |

## Requestbody
**Responsestatus**: `204`

## Responsebody
## `PATCH` `v1/buyers/{buyerID}/addresses/{addressID}`
Partially update an address

| Parameters      | Description                    |
|------------------|---------------------------------|


| Parameters      | Description                    |
|------------------|---------------------------------|
| Name            | buyerID                        |
| Type            | string                         |
| Description     | ID of the buyer.               |
| Required        | True                           |


| Parameters      | Description                    |
|------------------|---------------------------------|
| Name            | addressID                      |
| Type            | string                         |
| Description     | ID of the address.             |
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
{'ID': '', 'DateCreated': '2018-03-21T23:00:00+00:00', 'CompanyName': '', 'FirstName': '', 'LastName': '', 'Street1': '', 'Street2': '', 'City': '', 'State': '', 'Zip': '', 'Country': '', 'Phone': '', 'AddressName': '', 'xp': {}}
```


| Parameters      | Description                    |
|------------------|---------------------------------|
| Name            | ID                             |
| Type            | string                         |
| Description     | ID of the address.             |
| Required        | False                          |


| Parameters      | Description                    |
|------------------|---------------------------------|
| Name            | DateCreated                    |
| Type            | date                           |
| Description     | Date created of the address.   |
| Required        | False                          |


| Parameters      | Description                    |
|------------------|---------------------------------|
| Name            | CompanyName                    |
| Type            | string                         |
| Description     | Company name of the address.   |
| Required        | False                          |


| Parameters      | Description                    |
|------------------|---------------------------------|
| Name            | FirstName                      |
| Type            | string                         |
| Description     | First name of the address.     |
| Required        | False                          |


| Parameters      | Description                    |
|------------------|---------------------------------|
| Name            | LastName                       |
| Type            | string                         |
| Description     | Last name of the address.      |
| Required        | False                          |


| Parameters      | Description                    |
|------------------|---------------------------------|
| Name            | Street1                        |
| Type            | string                         |
| Description     | Street 1 of the address.       |
| Required        | True                           |


| Parameters      | Description                    |
|------------------|---------------------------------|
| Name            | Street2                        |
| Type            | string                         |
| Description     | Street 2 of the address.       |
| Required        | False                          |


| Parameters      | Description                    |
|------------------|---------------------------------|
| Name            | City                           |
| Type            | string                         |
| Description     | City of the address.           |
| Required        | True                           |


| Parameters      | Description                    |
|------------------|---------------------------------|
| Name            | State                          |
| Type            | string                         |
| Description     | State of the address.          |
| Required        | True                           |


| Parameters      | Description                    |
|------------------|---------------------------------|
| Name            | Zip                            |
| Type            | string                         |
| Description     | Zip of the address.            |
| Required        | True                           |


| Parameters      | Description                    |
|------------------|---------------------------------|
| Name            | Country                        |
| Type            | string                         |
| Description     | Country of the address.        |
| Required        | True                           |


| Parameters      | Description                    |
|------------------|---------------------------------|
| Name            | Phone                          |
| Type            | string                         |
| Description     | Phone of the address.          |
| Required        | False                          |


| Parameters      | Description                    |
|------------------|---------------------------------|
| Name            | AddressName                    |
| Type            | string                         |
| Description     | Address name of the address.   |
| Required        | False                          |


| Parameters      | Description                    |
|------------------|---------------------------------|
| Name            | xp                             |
| Type            | object                         |
| Description     | Container for extended (custom) properties of the address. |
| Required        | False                          |

## `GET` `v1/buyers/{buyerID}/addresses/assignments`
Get a list of address assignments

| Parameters      | Description                    |
|------------------|---------------------------------|


| Parameters      | Description                    |
|------------------|---------------------------------|
| Name            | buyerID                        |
| Type            | string                         |
| Description     | ID of the buyer.               |
| Required        | True                           |


| Parameters      | Description                    |
|------------------|---------------------------------|
| Name            | addressID                      |
| Type            | string                         |
| Description     | ID of the address.             |
| Required        | False                          |


| Parameters      | Description                    |
|------------------|---------------------------------|
| Name            | userID                         |
| Type            | string                         |
| Description     | ID of the user.                |
| Required        | False                          |


| Parameters      | Description                    |
|------------------|---------------------------------|
| Name            | userGroupID                    |
| Type            | string                         |
| Description     | ID of the user group.          |
| Required        | False                          |


| Parameters      | Description                    |
|------------------|---------------------------------|
| Name            | level                          |
| Type            | string                         |
| Description     | Level of the address assignment. Possible values: User, Group, Company. |
| Required        | False                          |


| Parameters      | Description                    |
|------------------|---------------------------------|
| Name            | isShipping                     |
| Type            | boolean                        |
| Description     | Is shipping of the address assignment. |
| Required        | False                          |


| Parameters      | Description                    |
|------------------|---------------------------------|
| Name            | isBilling                      |
| Type            | boolean                        |
| Description     | Is billing of the address assignment. |
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

## Requestbody
**Responsestatus**: `200`

## Responsebody
```
{'Meta': {'Page': 1, 'PageSize': 20, 'TotalCount': 25, 'TotalPages': 2, 'ItemRange': [1, 20]}, 'Items': [{'AddressID': '', 'UserID': '', 'UserGroupID': '', 'IsShipping': False, 'IsBilling': False}]}
```


| Parameters      | Description                    |
|------------------|---------------------------------|
| Name            | AddressID                      |
| Type            | string                         |
| Description     | ID of the address.             |
| Required        | True                           |


| Parameters      | Description                    |
|------------------|---------------------------------|
| Name            | UserID                         |
| Type            | string                         |
| Description     | ID of the user.                |
| Required        | False                          |


| Parameters      | Description                    |
|------------------|---------------------------------|
| Name            | UserGroupID                    |
| Type            | string                         |
| Description     | ID of the user group.          |
| Required        | False                          |


| Parameters      | Description                    |
|------------------|---------------------------------|
| Name            | IsShipping                     |
| Type            | boolean                        |
| Description     | Is shipping of the address assignment. |
| Required        | False                          |


| Parameters      | Description                    |
|------------------|---------------------------------|
| Name            | IsBilling                      |
| Type            | boolean                        |
| Description     | Is billing of the address assignment. |
| Required        | False                          |

## `DELETE` `v1/buyers/{buyerID}/addresses/{addressID}/assignments`
Delete an address assignment

| Parameters      | Description                    |
|------------------|---------------------------------|


| Parameters      | Description                    |
|------------------|---------------------------------|
| Name            | buyerID                        |
| Type            | string                         |
| Description     | ID of the buyer.               |
| Required        | True                           |


| Parameters      | Description                    |
|------------------|---------------------------------|
| Name            | addressID                      |
| Type            | string                         |
| Description     | ID of the address.             |
| Required        | True                           |


| Parameters      | Description                    |
|------------------|---------------------------------|
| Name            | userID                         |
| Type            | string                         |
| Description     | ID of the user.                |
| Required        | False                          |


| Parameters      | Description                    |
|------------------|---------------------------------|
| Name            | userGroupID                    |
| Type            | string                         |
| Description     | ID of the user group.          |
| Required        | False                          |

## Requestbody
**Responsestatus**: `204`

## Responsebody
## `POST` `v1/buyers/{buyerID}/addresses/assignments`
Save an address assignment

| Parameters      | Description                    |
|------------------|---------------------------------|


| Parameters      | Description                    |
|------------------|---------------------------------|
| Name            | buyerID                        |
| Type            | string                         |
| Description     | ID of the buyer.               |
| Required        | True                           |

## Requestbody
```
{'AddressID': '', 'UserID': '', 'UserGroupID': '', 'IsShipping': False, 'IsBilling': False}
```

```
[{'Name': 'AddressID', 'Type': 'string', 'Description': 'ID of the address. Required. Sortable: priority level 1.', 'Required': True}, {'Name': 'UserID', 'Type': 'string', 'Description': 'ID of the user. Sortable: priority level 2.', 'Required': False}, {'Name': 'UserGroupID', 'Type': 'string', 'Description': 'ID of the user group. Sortable: priority level 3.', 'Required': False}, {'Name': 'IsShipping', 'Type': 'boolean', 'Description': 'Is shipping of the address assignment.', 'Required': False}, {'Name': 'IsBilling', 'Type': 'boolean', 'Description': 'Is billing of the address assignment.', 'Required': False}]
```

**Responsestatus**: `204`

## Responsebody