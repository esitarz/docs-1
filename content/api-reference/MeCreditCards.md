---
title: Credit Cards
date: 2018-03-23
category: API Reference
tags: Me And My Stuff
slug: MeCreditCards
---
"Me" is a container for read-only endpoints that return a filtered view
of things that the current buyer user is allowed to see, i.e. things
that they are assigned to either directly or as a member of a buyer
organization or user group. It also provides ways for a user to update
or change their own information.

---

## `POST` `v1/me/creditcards`
Create a new credit card
## Requestbody
```
{'Token': '', 'CardType': '', 'PartialAccountNumber': '', 'CardholderName': '', 'ExpirationDate': '2018-03-21T23:00:00+00:00', 'xp': {}}
```

```
[{'Name': 'Token', 'Type': 'string', 'Description': 'Token of the credit card.', 'Required': False}, {'Name': 'CardType', 'Type': 'string', 'Description': 'Card type of the credit card. Searchable: priority level 3. Sortable: priority level 3.', 'Required': False}, {'Name': 'PartialAccountNumber', 'Type': 'string', 'Description': 'Partial account number of the credit card. Max length 5 characters.', 'Required': False}, {'Name': 'CardholderName', 'Type': 'string', 'Description': 'Cardholder name of the credit card. Searchable: priority level 2. Sortable: priority level 2.', 'Required': False}, {'Name': 'ExpirationDate', 'Type': 'date', 'Description': 'Expiration date of the credit card. Searchable: priority level 4. Sortable: priority level 4.', 'Required': False}, {'Name': 'xp', 'Type': 'object', 'Description': 'Container for extended (custom) properties of the credit card.', 'Required': False}]
```

**Responsestatus**: `201`

## Responsebody
```
{'ID': '', 'Editable': False, 'Token': '', 'DateCreated': '2018-03-21T23:00:00+00:00', 'CardType': '', 'PartialAccountNumber': '', 'CardholderName': '', 'ExpirationDate': '2018-03-21T23:00:00+00:00', 'xp': {}}
```


| Parameters      | Description                    |
|------------------|---------------------------------|
| Name            | ID                             |
| Type            | string                         |
| Description     | ID of the credit card.         |
| Required        | False                          |


| Parameters      | Description                    |
|------------------|---------------------------------|
| Name            | Editable                       |
| Type            | boolean                        |
| Description     | Editable of the credit card.   |
| Required        | False                          |


| Parameters      | Description                    |
|------------------|---------------------------------|
| Name            | Token                          |
| Type            | string                         |
| Description     | Token of the credit card.      |
| Required        | False                          |


| Parameters      | Description                    |
|------------------|---------------------------------|
| Name            | DateCreated                    |
| Type            | date                           |
| Description     | Date created of the credit card. |
| Required        | False                          |


| Parameters      | Description                    |
|------------------|---------------------------------|
| Name            | CardType                       |
| Type            | string                         |
| Description     | Card type of the credit card.  |
| Required        | False                          |


| Parameters      | Description                    |
|------------------|---------------------------------|
| Name            | PartialAccountNumber           |
| Type            | string                         |
| Description     | Partial account number of the credit card. |
| Required        | False                          |


| Parameters      | Description                    |
|------------------|---------------------------------|
| Name            | CardholderName                 |
| Type            | string                         |
| Description     | Cardholder name of the credit card. |
| Required        | False                          |


| Parameters      | Description                    |
|------------------|---------------------------------|
| Name            | ExpirationDate                 |
| Type            | date                           |
| Description     | Expiration date of the credit card. |
| Required        | False                          |


| Parameters      | Description                    |
|------------------|---------------------------------|
| Name            | xp                             |
| Type            | object                         |
| Description     | Container for extended (custom) properties of the credit card. |
| Required        | False                          |

## `GET` `v1/me/creditcards`
Get a list of credit cards visible to this user

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
{'Meta': {'Page': 1, 'PageSize': 20, 'TotalCount': 25, 'TotalPages': 2, 'ItemRange': [1, 20]}, 'Items': [{'ID': '', 'Editable': False, 'Token': '', 'DateCreated': '2018-03-21T23:00:00+00:00', 'CardType': '', 'PartialAccountNumber': '', 'CardholderName': '', 'ExpirationDate': '2018-03-21T23:00:00+00:00', 'xp': {}}]}
```


| Parameters      | Description                    |
|------------------|---------------------------------|
| Name            | ID                             |
| Type            | string                         |
| Description     | ID of the credit card.         |
| Required        | False                          |


| Parameters      | Description                    |
|------------------|---------------------------------|
| Name            | Editable                       |
| Type            | boolean                        |
| Description     | Editable of the credit card.   |
| Required        | False                          |


| Parameters      | Description                    |
|------------------|---------------------------------|
| Name            | Token                          |
| Type            | string                         |
| Description     | Token of the credit card.      |
| Required        | False                          |


| Parameters      | Description                    |
|------------------|---------------------------------|
| Name            | DateCreated                    |
| Type            | date                           |
| Description     | Date created of the credit card. |
| Required        | False                          |


| Parameters      | Description                    |
|------------------|---------------------------------|
| Name            | CardType                       |
| Type            | string                         |
| Description     | Card type of the credit card.  |
| Required        | False                          |


| Parameters      | Description                    |
|------------------|---------------------------------|
| Name            | PartialAccountNumber           |
| Type            | string                         |
| Description     | Partial account number of the credit card. |
| Required        | False                          |


| Parameters      | Description                    |
|------------------|---------------------------------|
| Name            | CardholderName                 |
| Type            | string                         |
| Description     | Cardholder name of the credit card. |
| Required        | False                          |


| Parameters      | Description                    |
|------------------|---------------------------------|
| Name            | ExpirationDate                 |
| Type            | date                           |
| Description     | Expiration date of the credit card. |
| Required        | False                          |


| Parameters      | Description                    |
|------------------|---------------------------------|
| Name            | xp                             |
| Type            | object                         |
| Description     | Container for extended (custom) properties of the credit card. |
| Required        | False                          |

## `GET` `v1/me/creditcards/{creditcardID}`
Get a single credit card

| Parameters      | Description                    |
|------------------|---------------------------------|


| Parameters      | Description                    |
|------------------|---------------------------------|
| Name            | creditcardID                   |
| Type            | string                         |
| Description     | ID of the creditcard.          |
| Required        | True                           |

## Requestbody
**Responsestatus**: `200`

## Responsebody
```
{'ID': '', 'Editable': False, 'Token': '', 'DateCreated': '2018-03-21T23:00:00+00:00', 'CardType': '', 'PartialAccountNumber': '', 'CardholderName': '', 'ExpirationDate': '2018-03-21T23:00:00+00:00', 'xp': {}}
```


| Parameters      | Description                    |
|------------------|---------------------------------|
| Name            | ID                             |
| Type            | string                         |
| Description     | ID of the credit card.         |
| Required        | False                          |


| Parameters      | Description                    |
|------------------|---------------------------------|
| Name            | Editable                       |
| Type            | boolean                        |
| Description     | Editable of the credit card.   |
| Required        | False                          |


| Parameters      | Description                    |
|------------------|---------------------------------|
| Name            | Token                          |
| Type            | string                         |
| Description     | Token of the credit card.      |
| Required        | False                          |


| Parameters      | Description                    |
|------------------|---------------------------------|
| Name            | DateCreated                    |
| Type            | date                           |
| Description     | Date created of the credit card. |
| Required        | False                          |


| Parameters      | Description                    |
|------------------|---------------------------------|
| Name            | CardType                       |
| Type            | string                         |
| Description     | Card type of the credit card.  |
| Required        | False                          |


| Parameters      | Description                    |
|------------------|---------------------------------|
| Name            | PartialAccountNumber           |
| Type            | string                         |
| Description     | Partial account number of the credit card. |
| Required        | False                          |


| Parameters      | Description                    |
|------------------|---------------------------------|
| Name            | CardholderName                 |
| Type            | string                         |
| Description     | Cardholder name of the credit card. |
| Required        | False                          |


| Parameters      | Description                    |
|------------------|---------------------------------|
| Name            | ExpirationDate                 |
| Type            | date                           |
| Description     | Expiration date of the credit card. |
| Required        | False                          |


| Parameters      | Description                    |
|------------------|---------------------------------|
| Name            | xp                             |
| Type            | object                         |
| Description     | Container for extended (custom) properties of the credit card. |
| Required        | False                          |

## `PUT` `v1/me/creditcards/{creditcardID}`
Create or update a credit card

| Parameters      | Description                    |
|------------------|---------------------------------|


| Parameters      | Description                    |
|------------------|---------------------------------|
| Name            | creditcardID                   |
| Type            | string                         |
| Description     | ID of the creditcard.          |
| Required        | True                           |

## Requestbody
```
{'Token': '', 'CardType': '', 'PartialAccountNumber': '', 'CardholderName': '', 'ExpirationDate': '2018-03-21T23:00:00+00:00', 'xp': {}}
```

```
[{'Name': 'Token', 'Type': 'string', 'Description': 'Token of the credit card.', 'Required': False}, {'Name': 'CardType', 'Type': 'string', 'Description': 'Card type of the credit card. Searchable: priority level 3. Sortable: priority level 3.', 'Required': False}, {'Name': 'PartialAccountNumber', 'Type': 'string', 'Description': 'Partial account number of the credit card. Max length 5 characters.', 'Required': False}, {'Name': 'CardholderName', 'Type': 'string', 'Description': 'Cardholder name of the credit card. Searchable: priority level 2. Sortable: priority level 2.', 'Required': False}, {'Name': 'ExpirationDate', 'Type': 'date', 'Description': 'Expiration date of the credit card. Searchable: priority level 4. Sortable: priority level 4.', 'Required': False}, {'Name': 'xp', 'Type': 'object', 'Description': 'Container for extended (custom) properties of the credit card.', 'Required': False}]
```

**Responsestatus**: `200`

## Responsebody
```
{'ID': '', 'Editable': False, 'Token': '', 'DateCreated': '2018-03-21T23:00:00+00:00', 'CardType': '', 'PartialAccountNumber': '', 'CardholderName': '', 'ExpirationDate': '2018-03-21T23:00:00+00:00', 'xp': {}}
```


| Parameters      | Description                    |
|------------------|---------------------------------|
| Name            | ID                             |
| Type            | string                         |
| Description     | ID of the credit card.         |
| Required        | False                          |


| Parameters      | Description                    |
|------------------|---------------------------------|
| Name            | Editable                       |
| Type            | boolean                        |
| Description     | Editable of the credit card.   |
| Required        | False                          |


| Parameters      | Description                    |
|------------------|---------------------------------|
| Name            | Token                          |
| Type            | string                         |
| Description     | Token of the credit card.      |
| Required        | False                          |


| Parameters      | Description                    |
|------------------|---------------------------------|
| Name            | DateCreated                    |
| Type            | date                           |
| Description     | Date created of the credit card. |
| Required        | False                          |


| Parameters      | Description                    |
|------------------|---------------------------------|
| Name            | CardType                       |
| Type            | string                         |
| Description     | Card type of the credit card.  |
| Required        | False                          |


| Parameters      | Description                    |
|------------------|---------------------------------|
| Name            | PartialAccountNumber           |
| Type            | string                         |
| Description     | Partial account number of the credit card. |
| Required        | False                          |


| Parameters      | Description                    |
|------------------|---------------------------------|
| Name            | CardholderName                 |
| Type            | string                         |
| Description     | Cardholder name of the credit card. |
| Required        | False                          |


| Parameters      | Description                    |
|------------------|---------------------------------|
| Name            | ExpirationDate                 |
| Type            | date                           |
| Description     | Expiration date of the credit card. |
| Required        | False                          |


| Parameters      | Description                    |
|------------------|---------------------------------|
| Name            | xp                             |
| Type            | object                         |
| Description     | Container for extended (custom) properties of the credit card. |
| Required        | False                          |

## `PATCH` `v1/me/creditcards/{creditcardID}`
Partially update a credit card

| Parameters      | Description                    |
|------------------|---------------------------------|


| Parameters      | Description                    |
|------------------|---------------------------------|
| Name            | creditcardID                   |
| Type            | string                         |
| Description     | ID of the creditcard.          |
| Required        | True                           |

## Requestbody
```
{'Token': '', 'CardType': '', 'PartialAccountNumber': '', 'CardholderName': '', 'ExpirationDate': '2018-03-21T23:00:00+00:00', 'xp': {}}
```

```
[{'Name': 'Token', 'Type': 'string', 'Description': 'Token of the credit card.', 'Required': False}, {'Name': 'CardType', 'Type': 'string', 'Description': 'Card type of the credit card. Searchable: priority level 3. Sortable: priority level 3.', 'Required': False}, {'Name': 'PartialAccountNumber', 'Type': 'string', 'Description': 'Partial account number of the credit card. Max length 5 characters.', 'Required': False}, {'Name': 'CardholderName', 'Type': 'string', 'Description': 'Cardholder name of the credit card. Searchable: priority level 2. Sortable: priority level 2.', 'Required': False}, {'Name': 'ExpirationDate', 'Type': 'date', 'Description': 'Expiration date of the credit card. Searchable: priority level 4. Sortable: priority level 4.', 'Required': False}, {'Name': 'xp', 'Type': 'object', 'Description': 'Container for extended (custom) properties of the credit card.', 'Required': False}]
```

**Responsestatus**: `204`

## Responsebody
## `DELETE` `v1/me/creditcards/{creditcardID}`
Delete a credit card

| Parameters      | Description                    |
|------------------|---------------------------------|


| Parameters      | Description                    |
|------------------|---------------------------------|
| Name            | creditcardID                   |
| Type            | string                         |
| Description     | ID of the creditcard.          |
| Required        | True                           |

## Requestbody
**Responsestatus**: `204`

## Responsebody