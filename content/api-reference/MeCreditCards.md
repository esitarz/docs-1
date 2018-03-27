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
	    "ExpirationDate": "2018-03-21T23:00:00+00:00",
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

## Response Body
	{
	    "CardType": "",
	    "CardholderName": "",
	    "DateCreated": "2018-03-21T23:00:00+00:00",
	    "Editable": false,
	    "ExpirationDate": "2018-03-21T23:00:00+00:00",
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

| Name | Type | Description | Required | 
|---|---|---|---|
| search | string | Word or phrase to search for. | False |
| searchOn | string | Comma-delimited list of fields to search on. | False |
| sortBy | string | Comma-delimited list of fields to sort by. | False |
| page | integer | Page of results to return. Default: 1 | False |
| pageSize | integer | Number of results to return per page. Default: 20, max: 100. | False |
| filters | object | Any additional key/value pairs passed in the query string are interpretted as filters. Valid keys are top-level properties of the returned model or 'xp.???' | False |

## Response Body
	{
	    "Items": [
	        {
	            "CardType": "",
	            "CardholderName": "",
	            "DateCreated": "2018-03-21T23:00:00+00:00",
	            "Editable": false,
	            "ExpirationDate": "2018-03-21T23:00:00+00:00",
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

| Name | Type | Description | Required | 
|---|---|---|---|
| creditcardID | string | ID of the creditcard. | True |

## Response Body
	{
	    "CardType": "",
	    "CardholderName": "",
	    "DateCreated": "2018-03-21T23:00:00+00:00",
	    "Editable": false,
	    "ExpirationDate": "2018-03-21T23:00:00+00:00",
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

| Name | Type | Description | Required | 
|---|---|---|---|
| creditcardID | string | ID of the creditcard. | True |

## Request Body
	{
	    "CardType": "",
	    "CardholderName": "",
	    "ExpirationDate": "2018-03-21T23:00:00+00:00",
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

## Response Body
	{
	    "CardType": "",
	    "CardholderName": "",
	    "DateCreated": "2018-03-21T23:00:00+00:00",
	    "Editable": false,
	    "ExpirationDate": "2018-03-21T23:00:00+00:00",
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

| Name | Type | Description | Required | 
|---|---|---|---|
| creditcardID | string | ID of the creditcard. | True |

## Request Body
	{
	    "CardType": "",
	    "CardholderName": "",
	    "ExpirationDate": "2018-03-21T23:00:00+00:00",
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

## Response Body
## `DELETE` `v1/me/creditcards/{creditcardID}`
Delete a credit card

| Name | Type | Description | Required | 
|---|---|---|---|
| creditcardID | string | ID of the creditcard. | True |

## Response Body