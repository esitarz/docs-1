---
title: Credit Cards
date: 2018-03-27
category: API Reference
tags: Me And My Stuff
slug: Me-And-My-Stuff-MeCreditCards
---
"Me" is a container for read-only endpoints that return a filtered view
of things that the current buyer user is allowed to see, i.e. things
that they are assigned to either directly or as a member of a buyer
organization or user group. It also provides ways for a user to update
or change their own information.

---

## `POST` `v1/me/creditcards`
Create a new credit card
## Request Body
	{
	    "CardType": "",
	    "CardholderName": "",
	    "ExpirationDate": "2018-03-27T16:00:00+00:00",
	    "PartialAccountNumber": "",
	    "Token": "",
	    "xp": {}
	}
| Name | Type | Description | Required | 
|---|---|---|---|
| Token | string | Token of the credit card. | False |
| CardType | string | Card type of the credit card. Searchable: priority level 3. Sortable: priority level 3. | False |
| PartialAccountNumber | string | Partial account number of the credit card. Max length 5 characters. | False |
| CardholderName | string | Cardholder name of the credit card. Searchable: priority level 2. Sortable: priority level 2. | False |
| ExpirationDate | date | Expiration date of the credit card. Searchable: priority level 4. Sortable: priority level 4. | False |
| xp | object | Container for extended (custom) properties of the credit card. | False |

**Response Status**: `201`

## Response Body
	{
	    "CardType": "",
	    "CardholderName": "",
	    "DateCreated": "2018-03-27T16:00:00+00:00",
	    "Editable": false,
	    "ExpirationDate": "2018-03-27T16:00:00+00:00",
	    "ID": "",
	    "PartialAccountNumber": "",
	    "Token": "",
	    "xp": {}
	}
| Name | Type | Description | Required | 
|---|---|---|---|
| ID | string | ID of the credit card. | False |
| Editable | boolean | Editable of the credit card. | False |
| Token | string | Token of the credit card. | False |
| DateCreated | date | Date created of the credit card. | False |
| CardType | string | Card type of the credit card. | False |
| PartialAccountNumber | string | Partial account number of the credit card. | False |
| CardholderName | string | Cardholder name of the credit card. | False |
| ExpirationDate | date | Expiration date of the credit card. | False |
| xp | object | Container for extended (custom) properties of the credit card. | False |

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

## Request Body
**Response Status**: `200`

## Response Body
	{
	    "Items": [
	        {
	            "CardType": "",
	            "CardholderName": "",
	            "DateCreated": "2018-03-27T16:00:00+00:00",
	            "Editable": false,
	            "ExpirationDate": "2018-03-27T16:00:00+00:00",
	            "ID": "",
	            "PartialAccountNumber": "",
	            "Token": "",
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
| ID | string | ID of the credit card. | False |
| Editable | boolean | Editable of the credit card. | False |
| Token | string | Token of the credit card. | False |
| DateCreated | date | Date created of the credit card. | False |
| CardType | string | Card type of the credit card. | False |
| PartialAccountNumber | string | Partial account number of the credit card. | False |
| CardholderName | string | Cardholder name of the credit card. | False |
| ExpirationDate | date | Expiration date of the credit card. | False |
| xp | object | Container for extended (custom) properties of the credit card. | False |

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

## Request Body
**Response Status**: `200`

## Response Body
	{
	    "CardType": "",
	    "CardholderName": "",
	    "DateCreated": "2018-03-27T16:00:00+00:00",
	    "Editable": false,
	    "ExpirationDate": "2018-03-27T16:00:00+00:00",
	    "ID": "",
	    "PartialAccountNumber": "",
	    "Token": "",
	    "xp": {}
	}
| Name | Type | Description | Required | 
|---|---|---|---|
| ID | string | ID of the credit card. | False |
| Editable | boolean | Editable of the credit card. | False |
| Token | string | Token of the credit card. | False |
| DateCreated | date | Date created of the credit card. | False |
| CardType | string | Card type of the credit card. | False |
| PartialAccountNumber | string | Partial account number of the credit card. | False |
| CardholderName | string | Cardholder name of the credit card. | False |
| ExpirationDate | date | Expiration date of the credit card. | False |
| xp | object | Container for extended (custom) properties of the credit card. | False |

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

## Request Body
	{
	    "CardType": "",
	    "CardholderName": "",
	    "ExpirationDate": "2018-03-27T16:00:00+00:00",
	    "PartialAccountNumber": "",
	    "Token": "",
	    "xp": {}
	}
| Name | Type | Description | Required | 
|---|---|---|---|
| Token | string | Token of the credit card. | False |
| CardType | string | Card type of the credit card. Searchable: priority level 3. Sortable: priority level 3. | False |
| PartialAccountNumber | string | Partial account number of the credit card. Max length 5 characters. | False |
| CardholderName | string | Cardholder name of the credit card. Searchable: priority level 2. Sortable: priority level 2. | False |
| ExpirationDate | date | Expiration date of the credit card. Searchable: priority level 4. Sortable: priority level 4. | False |
| xp | object | Container for extended (custom) properties of the credit card. | False |

**Response Status**: `200`

## Response Body
	{
	    "CardType": "",
	    "CardholderName": "",
	    "DateCreated": "2018-03-27T16:00:00+00:00",
	    "Editable": false,
	    "ExpirationDate": "2018-03-27T16:00:00+00:00",
	    "ID": "",
	    "PartialAccountNumber": "",
	    "Token": "",
	    "xp": {}
	}
| Name | Type | Description | Required | 
|---|---|---|---|
| ID | string | ID of the credit card. | False |
| Editable | boolean | Editable of the credit card. | False |
| Token | string | Token of the credit card. | False |
| DateCreated | date | Date created of the credit card. | False |
| CardType | string | Card type of the credit card. | False |
| PartialAccountNumber | string | Partial account number of the credit card. | False |
| CardholderName | string | Cardholder name of the credit card. | False |
| ExpirationDate | date | Expiration date of the credit card. | False |
| xp | object | Container for extended (custom) properties of the credit card. | False |

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

## Request Body
	{
	    "CardType": "",
	    "CardholderName": "",
	    "ExpirationDate": "2018-03-27T16:00:00+00:00",
	    "PartialAccountNumber": "",
	    "Token": "",
	    "xp": {}
	}
| Name | Type | Description | Required | 
|---|---|---|---|
| Token | string | Token of the credit card. | False |
| CardType | string | Card type of the credit card. Searchable: priority level 3. Sortable: priority level 3. | False |
| PartialAccountNumber | string | Partial account number of the credit card. Max length 5 characters. | False |
| CardholderName | string | Cardholder name of the credit card. Searchable: priority level 2. Sortable: priority level 2. | False |
| ExpirationDate | date | Expiration date of the credit card. Searchable: priority level 4. Sortable: priority level 4. | False |
| xp | object | Container for extended (custom) properties of the credit card. | False |

**Response Status**: `204`

## Response Body
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

## Request Body
**Response Status**: `204`

## Response Body