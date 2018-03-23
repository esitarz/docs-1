---
title: Addresses
date: 2018-03-23
category: API Reference
tags: Me And My Stuff
slug: MeAddresses
---
"Me" is a container for read-only endpoints that return a filtered view
of things that the current buyer user is allowed to see, i.e. things
that they are assigned to either directly or as a member of a buyer
organization or user group. It also provides ways for a user to update
or change their own information.

---

## `GET` `v1/me/addresses`
Get a list of addresses visible to this user

| Parameters      | Description                    |
|------------------|---------------------------------|


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
{'Meta': {'Page': 1, 'PageSize': 20, 'TotalCount': 25, 'TotalPages': 2, 'ItemRange': [1, 20]}, 'Items': [{'ID': '', 'Shipping': False, 'Billing': False, 'Editable': False, 'DateCreated': '2018-03-21T23:00:00+00:00', 'CompanyName': '', 'FirstName': '', 'LastName': '', 'Street1': '', 'Street2': '', 'City': '', 'State': '', 'Zip': '', 'Country': '', 'Phone': '', 'AddressName': '', 'xp': {}}]}
```


| Parameters      | Description                    |
|------------------|---------------------------------|
| Name            | ID                             |
| Type            | string                         |
| Description     | ID of the address.             |
| Required        | False                          |


| Parameters      | Description                    |
|------------------|---------------------------------|
| Name            | Shipping                       |
| Type            | boolean                        |
| Description     | Shipping of the address.       |
| Required        | False                          |


| Parameters      | Description                    |
|------------------|---------------------------------|
| Name            | Billing                        |
| Type            | boolean                        |
| Description     | Billing of the address.        |
| Required        | False                          |


| Parameters      | Description                    |
|------------------|---------------------------------|
| Name            | Editable                       |
| Type            | boolean                        |
| Description     | Editable of the address.       |
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

## `POST` `v1/me/addresses`
Create a new address
## Requestbody
```
{'Shipping': False, 'Billing': False, 'CompanyName': '', 'FirstName': '', 'LastName': '', 'Street1': '', 'Street2': '', 'City': '', 'State': '', 'Zip': '', 'Country': '', 'Phone': '', 'AddressName': '', 'xp': {}}
```

```
[{'Name': 'Shipping', 'Type': 'boolean', 'Description': 'Shipping of the address. Searchable: priority level 6.', 'Required': False}, {'Name': 'Billing', 'Type': 'boolean', 'Description': 'Billing of the address. Searchable: priority level 7.', 'Required': False}, {'Name': 'CompanyName', 'Type': 'string', 'Description': 'Company name of the address. Max length 100 characters. Sortable.', 'Required': False}, {'Name': 'FirstName', 'Type': 'string', 'Description': 'First name of the address. Max length 100 characters. Searchable: priority level 7. Sortable.', 'Required': False}, {'Name': 'LastName', 'Type': 'string', 'Description': 'Last name of the address. Max length 100 characters. Searchable: priority level 6. Sortable.', 'Required': False}, {'Name': 'Street1', 'Type': 'string', 'Description': 'Street 1 of the address. Required. Max length 100 characters. Searchable: priority level 4. Sortable.', 'Required': True}, {'Name': 'Street2', 'Type': 'string', 'Description': 'Street 2 of the address. Max length 100 characters. Searchable: priority level 5. Sortable.', 'Required': False}, {'Name': 'City', 'Type': 'string', 'Description': 'City of the address. Required. Max length 100 characters. Searchable: priority level 3. Sortable.', 'Required': True}, {'Name': 'State', 'Type': 'string', 'Description': 'State of the address. Required. Max length 100 characters. Searchable: priority level 7. Sortable.', 'Required': True}, {'Name': 'Zip', 'Type': 'string', 'Description': 'Zip of the address. Required. Max length 100 characters. Searchable: priority level 6. Sortable.', 'Required': True}, {'Name': 'Country', 'Type': 'string', 'Description': 'Country of the address. Required. Max length 2 characters. Sortable.', 'Required': True}, {'Name': 'Phone', 'Type': 'string', 'Description': 'Phone of the address. Max length 100 characters. Sortable.', 'Required': False}, {'Name': 'AddressName', 'Type': 'string', 'Description': 'Address name of the address. Max length 100 characters. Searchable: priority level 2. Sortable: priority level 1.', 'Required': False}, {'Name': 'xp', 'Type': 'object', 'Description': 'Container for extended (custom) properties of the address.', 'Required': False}]
```

**Responsestatus**: `201`

## Responsebody
```
{'ID': '', 'Shipping': False, 'Billing': False, 'Editable': False, 'DateCreated': '2018-03-21T23:00:00+00:00', 'CompanyName': '', 'FirstName': '', 'LastName': '', 'Street1': '', 'Street2': '', 'City': '', 'State': '', 'Zip': '', 'Country': '', 'Phone': '', 'AddressName': '', 'xp': {}}
```


| Parameters      | Description                    |
|------------------|---------------------------------|
| Name            | ID                             |
| Type            | string                         |
| Description     | ID of the address.             |
| Required        | False                          |


| Parameters      | Description                    |
|------------------|---------------------------------|
| Name            | Shipping                       |
| Type            | boolean                        |
| Description     | Shipping of the address.       |
| Required        | False                          |


| Parameters      | Description                    |
|------------------|---------------------------------|
| Name            | Billing                        |
| Type            | boolean                        |
| Description     | Billing of the address.        |
| Required        | False                          |


| Parameters      | Description                    |
|------------------|---------------------------------|
| Name            | Editable                       |
| Type            | boolean                        |
| Description     | Editable of the address.       |
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

## `GET` `v1/me/addresses/{addressID}`
Get a single address

| Parameters      | Description                    |
|------------------|---------------------------------|


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
{'ID': '', 'Shipping': False, 'Billing': False, 'Editable': False, 'DateCreated': '2018-03-21T23:00:00+00:00', 'CompanyName': '', 'FirstName': '', 'LastName': '', 'Street1': '', 'Street2': '', 'City': '', 'State': '', 'Zip': '', 'Country': '', 'Phone': '', 'AddressName': '', 'xp': {}}
```


| Parameters      | Description                    |
|------------------|---------------------------------|
| Name            | ID                             |
| Type            | string                         |
| Description     | ID of the address.             |
| Required        | False                          |


| Parameters      | Description                    |
|------------------|---------------------------------|
| Name            | Shipping                       |
| Type            | boolean                        |
| Description     | Shipping of the address.       |
| Required        | False                          |


| Parameters      | Description                    |
|------------------|---------------------------------|
| Name            | Billing                        |
| Type            | boolean                        |
| Description     | Billing of the address.        |
| Required        | False                          |


| Parameters      | Description                    |
|------------------|---------------------------------|
| Name            | Editable                       |
| Type            | boolean                        |
| Description     | Editable of the address.       |
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

## `PUT` `v1/me/addresses/{addressID}`
Create or update an address

| Parameters      | Description                    |
|------------------|---------------------------------|


| Parameters      | Description                    |
|------------------|---------------------------------|
| Name            | addressID                      |
| Type            | string                         |
| Description     | ID of the address.             |
| Required        | True                           |

## Requestbody
```
{'Shipping': False, 'Billing': False, 'CompanyName': '', 'FirstName': '', 'LastName': '', 'Street1': '', 'Street2': '', 'City': '', 'State': '', 'Zip': '', 'Country': '', 'Phone': '', 'AddressName': '', 'xp': {}}
```

```
[{'Name': 'Shipping', 'Type': 'boolean', 'Description': 'Shipping of the address. Searchable: priority level 6.', 'Required': False}, {'Name': 'Billing', 'Type': 'boolean', 'Description': 'Billing of the address. Searchable: priority level 7.', 'Required': False}, {'Name': 'CompanyName', 'Type': 'string', 'Description': 'Company name of the address. Max length 100 characters. Sortable.', 'Required': False}, {'Name': 'FirstName', 'Type': 'string', 'Description': 'First name of the address. Max length 100 characters. Searchable: priority level 7. Sortable.', 'Required': False}, {'Name': 'LastName', 'Type': 'string', 'Description': 'Last name of the address. Max length 100 characters. Searchable: priority level 6. Sortable.', 'Required': False}, {'Name': 'Street1', 'Type': 'string', 'Description': 'Street 1 of the address. Required. Max length 100 characters. Searchable: priority level 4. Sortable.', 'Required': True}, {'Name': 'Street2', 'Type': 'string', 'Description': 'Street 2 of the address. Max length 100 characters. Searchable: priority level 5. Sortable.', 'Required': False}, {'Name': 'City', 'Type': 'string', 'Description': 'City of the address. Required. Max length 100 characters. Searchable: priority level 3. Sortable.', 'Required': True}, {'Name': 'State', 'Type': 'string', 'Description': 'State of the address. Required. Max length 100 characters. Searchable: priority level 7. Sortable.', 'Required': True}, {'Name': 'Zip', 'Type': 'string', 'Description': 'Zip of the address. Required. Max length 100 characters. Searchable: priority level 6. Sortable.', 'Required': True}, {'Name': 'Country', 'Type': 'string', 'Description': 'Country of the address. Required. Max length 2 characters. Sortable.', 'Required': True}, {'Name': 'Phone', 'Type': 'string', 'Description': 'Phone of the address. Max length 100 characters. Sortable.', 'Required': False}, {'Name': 'AddressName', 'Type': 'string', 'Description': 'Address name of the address. Max length 100 characters. Searchable: priority level 2. Sortable: priority level 1.', 'Required': False}, {'Name': 'xp', 'Type': 'object', 'Description': 'Container for extended (custom) properties of the address.', 'Required': False}]
```

**Responsestatus**: `200`

## Responsebody
```
{'ID': '', 'Shipping': False, 'Billing': False, 'Editable': False, 'DateCreated': '2018-03-21T23:00:00+00:00', 'CompanyName': '', 'FirstName': '', 'LastName': '', 'Street1': '', 'Street2': '', 'City': '', 'State': '', 'Zip': '', 'Country': '', 'Phone': '', 'AddressName': '', 'xp': {}}
```


| Parameters      | Description                    |
|------------------|---------------------------------|
| Name            | ID                             |
| Type            | string                         |
| Description     | ID of the address.             |
| Required        | False                          |


| Parameters      | Description                    |
|------------------|---------------------------------|
| Name            | Shipping                       |
| Type            | boolean                        |
| Description     | Shipping of the address.       |
| Required        | False                          |


| Parameters      | Description                    |
|------------------|---------------------------------|
| Name            | Billing                        |
| Type            | boolean                        |
| Description     | Billing of the address.        |
| Required        | False                          |


| Parameters      | Description                    |
|------------------|---------------------------------|
| Name            | Editable                       |
| Type            | boolean                        |
| Description     | Editable of the address.       |
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

## `PATCH` `v1/me/addresses/{addressID}`
Partially update an address

| Parameters      | Description                    |
|------------------|---------------------------------|


| Parameters      | Description                    |
|------------------|---------------------------------|
| Name            | addressID                      |
| Type            | string                         |
| Description     | ID of the address.             |
| Required        | True                           |

## Requestbody
```
{'Shipping': False, 'Billing': False, 'CompanyName': '', 'FirstName': '', 'LastName': '', 'Street1': '', 'Street2': '', 'City': '', 'State': '', 'Zip': '', 'Country': '', 'Phone': '', 'AddressName': '', 'xp': {}}
```

```
[{'Name': 'Shipping', 'Type': 'boolean', 'Description': 'Shipping of the address. Searchable: priority level 6.', 'Required': False}, {'Name': 'Billing', 'Type': 'boolean', 'Description': 'Billing of the address. Searchable: priority level 7.', 'Required': False}, {'Name': 'CompanyName', 'Type': 'string', 'Description': 'Company name of the address. Max length 100 characters. Sortable.', 'Required': False}, {'Name': 'FirstName', 'Type': 'string', 'Description': 'First name of the address. Max length 100 characters. Searchable: priority level 7. Sortable.', 'Required': False}, {'Name': 'LastName', 'Type': 'string', 'Description': 'Last name of the address. Max length 100 characters. Searchable: priority level 6. Sortable.', 'Required': False}, {'Name': 'Street1', 'Type': 'string', 'Description': 'Street 1 of the address. Required. Max length 100 characters. Searchable: priority level 4. Sortable.', 'Required': True}, {'Name': 'Street2', 'Type': 'string', 'Description': 'Street 2 of the address. Max length 100 characters. Searchable: priority level 5. Sortable.', 'Required': False}, {'Name': 'City', 'Type': 'string', 'Description': 'City of the address. Required. Max length 100 characters. Searchable: priority level 3. Sortable.', 'Required': True}, {'Name': 'State', 'Type': 'string', 'Description': 'State of the address. Required. Max length 100 characters. Searchable: priority level 7. Sortable.', 'Required': True}, {'Name': 'Zip', 'Type': 'string', 'Description': 'Zip of the address. Required. Max length 100 characters. Searchable: priority level 6. Sortable.', 'Required': True}, {'Name': 'Country', 'Type': 'string', 'Description': 'Country of the address. Required. Max length 2 characters. Sortable.', 'Required': True}, {'Name': 'Phone', 'Type': 'string', 'Description': 'Phone of the address. Max length 100 characters. Sortable.', 'Required': False}, {'Name': 'AddressName', 'Type': 'string', 'Description': 'Address name of the address. Max length 100 characters. Searchable: priority level 2. Sortable: priority level 1.', 'Required': False}, {'Name': 'xp', 'Type': 'object', 'Description': 'Container for extended (custom) properties of the address.', 'Required': False}]
```

**Responsestatus**: `204`

## Responsebody
## `DELETE` `v1/me/addresses/{addressID}`
Delete an address

| Parameters      | Description                    |
|------------------|---------------------------------|


| Parameters      | Description                    |
|------------------|---------------------------------|
| Name            | addressID                      |
| Type            | string                         |
| Description     | ID of the address.             |
| Required        | True                           |

## Requestbody
**Responsestatus**: `204`

## Responsebody