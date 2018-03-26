---
title: Credit Cards
date: 2018-03-26
category: API Reference
tags: Buyers
slug: Buyers-CreditCards
---
Credit cards are used as a payment method for an order. A user may have
access to one or many credit cards for personal spend or group spending.
Credit Cards may be saved and assigned to members of an organization for
use during purchase.

---

## `GET` `v1/buyers/{buyerID}/creditcards/{creditCardID}`
Get a single credit card

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
| Name            | creditCardID                   |
| Type            | string                         |
| Description     | ID of the credit card.         |
| Required        | True                           |

## Requestbody
**Responsestatus**: `200`

## Responsebody
```
{'ID': '', 'Token': '', 'DateCreated': '2018-03-21T23:00:00+00:00', 'CardType': '', 'PartialAccountNumber': '', 'CardholderName': '', 'ExpirationDate': '2018-03-21T23:00:00+00:00', 'xp': {}}
```


| Parameters      | Description                    |
|------------------|---------------------------------|
| Name            | ID                             |
| Type            | string                         |
| Description     | ID of the credit card.         |
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

## `GET` `v1/buyers/{buyerID}/creditcards`
Get a list of credit cards

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
{'Meta': {'Page': 1, 'PageSize': 20, 'TotalCount': 25, 'TotalPages': 2, 'ItemRange': [1, 20]}, 'Items': [{'ID': '', 'Token': '', 'DateCreated': '2018-03-21T23:00:00+00:00', 'CardType': '', 'PartialAccountNumber': '', 'CardholderName': '', 'ExpirationDate': '2018-03-21T23:00:00+00:00', 'xp': {}}]}
```


| Parameters      | Description                    |
|------------------|---------------------------------|
| Name            | ID                             |
| Type            | string                         |
| Description     | ID of the credit card.         |
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

## `POST` `v1/buyers/{buyerID}/creditcards`
Create a new credit card

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
{'ID': '', 'Token': '', 'CardType': '', 'PartialAccountNumber': '', 'CardholderName': '', 'ExpirationDate': '2018-03-21T23:00:00+00:00', 'xp': {}}
```

```
[{'Name': 'ID', 'Type': 'string', 'Description': 'ID of the credit card. Can only contain characters Aa-Zz, 0-9, -, and _. Searchable: priority level 1. Sortable: priority level 1.', 'Required': False}, {'Name': 'Token', 'Type': 'string', 'Description': 'Token of the credit card.', 'Required': False}, {'Name': 'CardType', 'Type': 'string', 'Description': 'Card type of the credit card. Searchable: priority level 3. Sortable: priority level 3.', 'Required': False}, {'Name': 'PartialAccountNumber', 'Type': 'string', 'Description': 'Partial account number of the credit card. Max length 5 characters.', 'Required': False}, {'Name': 'CardholderName', 'Type': 'string', 'Description': 'Cardholder name of the credit card. Searchable: priority level 2. Sortable: priority level 2.', 'Required': False}, {'Name': 'ExpirationDate', 'Type': 'date', 'Description': 'Expiration date of the credit card. Searchable: priority level 4. Sortable: priority level 4.', 'Required': False}, {'Name': 'xp', 'Type': 'object', 'Description': 'Container for extended (custom) properties of the credit card.', 'Required': False}]
```

**Responsestatus**: `201`

## Responsebody
```
{'ID': '', 'Token': '', 'DateCreated': '2018-03-21T23:00:00+00:00', 'CardType': '', 'PartialAccountNumber': '', 'CardholderName': '', 'ExpirationDate': '2018-03-21T23:00:00+00:00', 'xp': {}}
```


| Parameters      | Description                    |
|------------------|---------------------------------|
| Name            | ID                             |
| Type            | string                         |
| Description     | ID of the credit card.         |
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

## `PUT` `v1/buyers/{buyerID}/creditcards/{creditCardID}`
Create or update a credit card

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
| Name            | creditCardID                   |
| Type            | string                         |
| Description     | ID of the credit card.         |
| Required        | True                           |

## Requestbody
```
{'ID': '', 'Token': '', 'CardType': '', 'PartialAccountNumber': '', 'CardholderName': '', 'ExpirationDate': '2018-03-21T23:00:00+00:00', 'xp': {}}
```

```
[{'Name': 'ID', 'Type': 'string', 'Description': 'ID of the credit card. Can only contain characters Aa-Zz, 0-9, -, and _. Searchable: priority level 1. Sortable: priority level 1.', 'Required': False}, {'Name': 'Token', 'Type': 'string', 'Description': 'Token of the credit card.', 'Required': False}, {'Name': 'CardType', 'Type': 'string', 'Description': 'Card type of the credit card. Searchable: priority level 3. Sortable: priority level 3.', 'Required': False}, {'Name': 'PartialAccountNumber', 'Type': 'string', 'Description': 'Partial account number of the credit card. Max length 5 characters.', 'Required': False}, {'Name': 'CardholderName', 'Type': 'string', 'Description': 'Cardholder name of the credit card. Searchable: priority level 2. Sortable: priority level 2.', 'Required': False}, {'Name': 'ExpirationDate', 'Type': 'date', 'Description': 'Expiration date of the credit card. Searchable: priority level 4. Sortable: priority level 4.', 'Required': False}, {'Name': 'xp', 'Type': 'object', 'Description': 'Container for extended (custom) properties of the credit card.', 'Required': False}]
```

**Responsestatus**: `200`

## Responsebody
```
{'ID': '', 'Token': '', 'DateCreated': '2018-03-21T23:00:00+00:00', 'CardType': '', 'PartialAccountNumber': '', 'CardholderName': '', 'ExpirationDate': '2018-03-21T23:00:00+00:00', 'xp': {}}
```


| Parameters      | Description                    |
|------------------|---------------------------------|
| Name            | ID                             |
| Type            | string                         |
| Description     | ID of the credit card.         |
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

## `DELETE` `v1/buyers/{buyerID}/creditcards/{creditCardID}`
Delete a credit card

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
| Name            | creditCardID                   |
| Type            | string                         |
| Description     | ID of the credit card.         |
| Required        | True                           |

## Requestbody
**Responsestatus**: `204`

## Responsebody
## `PATCH` `v1/buyers/{buyerID}/creditcards/{creditCardID}`
Partially update a credit card

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
| Name            | creditCardID                   |
| Type            | string                         |
| Description     | ID of the credit card.         |
| Required        | True                           |

## Requestbody
```
{'ID': '', 'Token': '', 'CardType': '', 'PartialAccountNumber': '', 'CardholderName': '', 'ExpirationDate': '2018-03-21T23:00:00+00:00', 'xp': {}}
```

```
[{'Name': 'ID', 'Type': 'string', 'Description': 'ID of the credit card. Can only contain characters Aa-Zz, 0-9, -, and _. Searchable: priority level 1. Sortable: priority level 1.', 'Required': False}, {'Name': 'Token', 'Type': 'string', 'Description': 'Token of the credit card.', 'Required': False}, {'Name': 'CardType', 'Type': 'string', 'Description': 'Card type of the credit card. Searchable: priority level 3. Sortable: priority level 3.', 'Required': False}, {'Name': 'PartialAccountNumber', 'Type': 'string', 'Description': 'Partial account number of the credit card. Max length 5 characters.', 'Required': False}, {'Name': 'CardholderName', 'Type': 'string', 'Description': 'Cardholder name of the credit card. Searchable: priority level 2. Sortable: priority level 2.', 'Required': False}, {'Name': 'ExpirationDate', 'Type': 'date', 'Description': 'Expiration date of the credit card. Searchable: priority level 4. Sortable: priority level 4.', 'Required': False}, {'Name': 'xp', 'Type': 'object', 'Description': 'Container for extended (custom) properties of the credit card.', 'Required': False}]
```

**Responsestatus**: `200`

## Responsebody
```
{'ID': '', 'Token': '', 'DateCreated': '2018-03-21T23:00:00+00:00', 'CardType': '', 'PartialAccountNumber': '', 'CardholderName': '', 'ExpirationDate': '2018-03-21T23:00:00+00:00', 'xp': {}}
```


| Parameters      | Description                    |
|------------------|---------------------------------|
| Name            | ID                             |
| Type            | string                         |
| Description     | ID of the credit card.         |
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

## `GET` `v1/buyers/{buyerID}/creditcards/assignments`
Get a list of credit card assignments

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
| Name            | creditCardID                   |
| Type            | string                         |
| Description     | ID of the credit card.         |
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
| Description     | Level of the credit card assignment. Possible values: User, Group, Company. |
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
{'Meta': {'Page': 1, 'PageSize': 20, 'TotalCount': 25, 'TotalPages': 2, 'ItemRange': [1, 20]}, 'Items': [{'CreditCardID': '', 'UserID': '', 'UserGroupID': ''}]}
```


| Parameters      | Description                    |
|------------------|---------------------------------|
| Name            | CreditCardID                   |
| Type            | string                         |
| Description     | ID of the credit card.         |
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

## `POST` `v1/buyers/{buyerID}/creditcards/assignments`
Save a credit card assignment

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
{'CreditCardID': '', 'UserID': '', 'UserGroupID': ''}
```

```
[{'Name': 'CreditCardID', 'Type': 'string', 'Description': 'ID of the credit card. Required. Sortable: priority level 1.', 'Required': True}, {'Name': 'UserID', 'Type': 'string', 'Description': 'ID of the user. Sortable: priority level 2.', 'Required': False}, {'Name': 'UserGroupID', 'Type': 'string', 'Description': 'ID of the user group. Sortable: priority level 3.', 'Required': False}]
```

**Responsestatus**: `204`

## Responsebody
## `DELETE` `v1/buyers/{buyerID}/creditcards/{creditCardID}/assignments`
Delete a credit card assignment

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
| Name            | creditCardID                   |
| Type            | string                         |
| Description     | ID of the credit card.         |
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