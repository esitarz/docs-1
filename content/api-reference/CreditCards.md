---
title: Credit Cards
date: 2018-03-27
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

| Name | Type | Description | Required | 
|---|---|---|---|
| buyerID | string | ID of the buyer. | True |
| creditCardID | string | ID of the credit card. | True |

## Response Body
	:::json
	{
	    "CardType": "",
	    "CardholderName": "",
	    "DateCreated": "2018-03-27T19:00:00+00:00",
	    "ExpirationDate": "2018-03-27T19:00:00+00:00",
	    "ID": "",
	    "PartialAccountNumber": "",
	    "Token": "",
	    "xp": {}
	}


| Name | Type | Description | Required | 
|---|---|---|---|
| ID | string | ID of the credit card. | False |
| Token | string | Token of the credit card. | False |
| DateCreated | date | Date created of the credit card. | False |
| CardType | string | Card type of the credit card. | False |
| PartialAccountNumber | string | Partial account number of the credit card. | False |
| CardholderName | string | Cardholder name of the credit card. | False |
| ExpirationDate | date | Expiration date of the credit card. | False |
| xp | object | Container for extended (custom) properties of the credit card. | False |

## `GET` `v1/buyers/{buyerID}/creditcards`
Get a list of credit cards

| Name | Type | Description | Required | 
|---|---|---|---|
| buyerID | string | ID of the buyer. | True |
| search | string | Word or phrase to search for. | False |
| searchOn | string | Comma-delimited list of fields to search on. | False |
| sortBy | string | Comma-delimited list of fields to sort by. | False |
| page | integer | Page of results to return. Default: 1 | False |
| pageSize | integer | Number of results to return per page. Default: 20, max: 100. | False |
| filters | object | Any additional key/value pairs passed in the query string are interpretted as filters. Valid keys are top-level properties of the returned model or 'xp.???' | False |

## Response Body
	:::json
	{
	    "Items": [
	        {
	            "CardType": "",
	            "CardholderName": "",
	            "DateCreated": "2018-03-27T19:00:00+00:00",
	            "ExpirationDate": "2018-03-27T19:00:00+00:00",
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
| Token | string | Token of the credit card. | False |
| DateCreated | date | Date created of the credit card. | False |
| CardType | string | Card type of the credit card. | False |
| PartialAccountNumber | string | Partial account number of the credit card. | False |
| CardholderName | string | Cardholder name of the credit card. | False |
| ExpirationDate | date | Expiration date of the credit card. | False |
| xp | object | Container for extended (custom) properties of the credit card. | False |

## `POST` `v1/buyers/{buyerID}/creditcards`
Create a new credit card

| Name | Type | Description | Required | 
|---|---|---|---|
| buyerID | string | ID of the buyer. | True |

## Request Body
	:::json
	{
	    "CardType": "",
	    "CardholderName": "",
	    "ExpirationDate": "2018-03-27T19:00:00+00:00",
	    "ID": "",
	    "PartialAccountNumber": "",
	    "Token": "",
	    "xp": {}
	}


| Name | Type | Description | Required | 
|---|---|---|---|
| ID | string | ID of the credit card. Can only contain characters Aa-Zz, 0-9, -, and _. Searchable: priority level 1. Sortable: priority level 1. | False |
| Token | string | Token of the credit card. | False |
| CardType | string | Card type of the credit card. Searchable: priority level 3. Sortable: priority level 3. | False |
| PartialAccountNumber | string | Partial account number of the credit card. Max length 5 characters. | False |
| CardholderName | string | Cardholder name of the credit card. Searchable: priority level 2. Sortable: priority level 2. | False |
| ExpirationDate | date | Expiration date of the credit card. Searchable: priority level 4. Sortable: priority level 4. | False |
| xp | object | Container for extended (custom) properties of the credit card. | False |

## Response Body
	:::json
	{
	    "CardType": "",
	    "CardholderName": "",
	    "DateCreated": "2018-03-27T19:00:00+00:00",
	    "ExpirationDate": "2018-03-27T19:00:00+00:00",
	    "ID": "",
	    "PartialAccountNumber": "",
	    "Token": "",
	    "xp": {}
	}


| Name | Type | Description | Required | 
|---|---|---|---|
| ID | string | ID of the credit card. | False |
| Token | string | Token of the credit card. | False |
| DateCreated | date | Date created of the credit card. | False |
| CardType | string | Card type of the credit card. | False |
| PartialAccountNumber | string | Partial account number of the credit card. | False |
| CardholderName | string | Cardholder name of the credit card. | False |
| ExpirationDate | date | Expiration date of the credit card. | False |
| xp | object | Container for extended (custom) properties of the credit card. | False |

## `PUT` `v1/buyers/{buyerID}/creditcards/{creditCardID}`
Create or update a credit card

| Name | Type | Description | Required | 
|---|---|---|---|
| buyerID | string | ID of the buyer. | True |
| creditCardID | string | ID of the credit card. | True |

## Request Body
	:::json
	{
	    "CardType": "",
	    "CardholderName": "",
	    "ExpirationDate": "2018-03-27T19:00:00+00:00",
	    "ID": "",
	    "PartialAccountNumber": "",
	    "Token": "",
	    "xp": {}
	}


| Name | Type | Description | Required | 
|---|---|---|---|
| ID | string | ID of the credit card. Can only contain characters Aa-Zz, 0-9, -, and _. Searchable: priority level 1. Sortable: priority level 1. | False |
| Token | string | Token of the credit card. | False |
| CardType | string | Card type of the credit card. Searchable: priority level 3. Sortable: priority level 3. | False |
| PartialAccountNumber | string | Partial account number of the credit card. Max length 5 characters. | False |
| CardholderName | string | Cardholder name of the credit card. Searchable: priority level 2. Sortable: priority level 2. | False |
| ExpirationDate | date | Expiration date of the credit card. Searchable: priority level 4. Sortable: priority level 4. | False |
| xp | object | Container for extended (custom) properties of the credit card. | False |

## Response Body
	:::json
	{
	    "CardType": "",
	    "CardholderName": "",
	    "DateCreated": "2018-03-27T19:00:00+00:00",
	    "ExpirationDate": "2018-03-27T19:00:00+00:00",
	    "ID": "",
	    "PartialAccountNumber": "",
	    "Token": "",
	    "xp": {}
	}


| Name | Type | Description | Required | 
|---|---|---|---|
| ID | string | ID of the credit card. | False |
| Token | string | Token of the credit card. | False |
| DateCreated | date | Date created of the credit card. | False |
| CardType | string | Card type of the credit card. | False |
| PartialAccountNumber | string | Partial account number of the credit card. | False |
| CardholderName | string | Cardholder name of the credit card. | False |
| ExpirationDate | date | Expiration date of the credit card. | False |
| xp | object | Container for extended (custom) properties of the credit card. | False |

## `DELETE` `v1/buyers/{buyerID}/creditcards/{creditCardID}`
Delete a credit card

| Name | Type | Description | Required | 
|---|---|---|---|
| buyerID | string | ID of the buyer. | True |
| creditCardID | string | ID of the credit card. | True |

## Response Body
## `PATCH` `v1/buyers/{buyerID}/creditcards/{creditCardID}`
Partially update a credit card

| Name | Type | Description | Required | 
|---|---|---|---|
| buyerID | string | ID of the buyer. | True |
| creditCardID | string | ID of the credit card. | True |

## Request Body
	:::json
	{
	    "CardType": "",
	    "CardholderName": "",
	    "ExpirationDate": "2018-03-27T19:00:00+00:00",
	    "ID": "",
	    "PartialAccountNumber": "",
	    "Token": "",
	    "xp": {}
	}


| Name | Type | Description | Required | 
|---|---|---|---|
| ID | string | ID of the credit card. Can only contain characters Aa-Zz, 0-9, -, and _. Searchable: priority level 1. Sortable: priority level 1. | False |
| Token | string | Token of the credit card. | False |
| CardType | string | Card type of the credit card. Searchable: priority level 3. Sortable: priority level 3. | False |
| PartialAccountNumber | string | Partial account number of the credit card. Max length 5 characters. | False |
| CardholderName | string | Cardholder name of the credit card. Searchable: priority level 2. Sortable: priority level 2. | False |
| ExpirationDate | date | Expiration date of the credit card. Searchable: priority level 4. Sortable: priority level 4. | False |
| xp | object | Container for extended (custom) properties of the credit card. | False |

## Response Body
	:::json
	{
	    "CardType": "",
	    "CardholderName": "",
	    "DateCreated": "2018-03-27T19:00:00+00:00",
	    "ExpirationDate": "2018-03-27T19:00:00+00:00",
	    "ID": "",
	    "PartialAccountNumber": "",
	    "Token": "",
	    "xp": {}
	}


| Name | Type | Description | Required | 
|---|---|---|---|
| ID | string | ID of the credit card. | False |
| Token | string | Token of the credit card. | False |
| DateCreated | date | Date created of the credit card. | False |
| CardType | string | Card type of the credit card. | False |
| PartialAccountNumber | string | Partial account number of the credit card. | False |
| CardholderName | string | Cardholder name of the credit card. | False |
| ExpirationDate | date | Expiration date of the credit card. | False |
| xp | object | Container for extended (custom) properties of the credit card. | False |

## `GET` `v1/buyers/{buyerID}/creditcards/assignments`
Get a list of credit card assignments

| Name | Type | Description | Required | 
|---|---|---|---|
| buyerID | string | ID of the buyer. | True |
| creditCardID | string | ID of the credit card. | False |
| userID | string | ID of the user. | False |
| userGroupID | string | ID of the user group. | False |
| level | string | Level of the credit card assignment. Possible values: User, Group, Company. | False |
| page | integer | Page of results to return. Default: 1 | False |
| pageSize | integer | Number of results to return per page. Default: 20, max: 100. | False |

## Response Body
	:::json
	{
	    "Items": [
	        {
	            "CreditCardID": "",
	            "UserGroupID": "",
	            "UserID": ""
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
| CreditCardID | string | ID of the credit card. | True |
| UserID | string | ID of the user. | False |
| UserGroupID | string | ID of the user group. | False |

## `POST` `v1/buyers/{buyerID}/creditcards/assignments`
Save a credit card assignment

| Name | Type | Description | Required | 
|---|---|---|---|
| buyerID | string | ID of the buyer. | True |

## Request Body
	:::json
	{
	    "CreditCardID": "",
	    "UserGroupID": "",
	    "UserID": ""
	}


| Name | Type | Description | Required | 
|---|---|---|---|
| CreditCardID | string | ID of the credit card. Required. Sortable: priority level 1. | True |
| UserID | string | ID of the user. Sortable: priority level 2. | False |
| UserGroupID | string | ID of the user group. Sortable: priority level 3. | False |

## Response Body
## `DELETE` `v1/buyers/{buyerID}/creditcards/{creditCardID}/assignments`
Delete a credit card assignment

| Name | Type | Description | Required | 
|---|---|---|---|
| buyerID | string | ID of the buyer. | True |
| creditCardID | string | ID of the credit card. | True |
| userID | string | ID of the user. | False |
| userGroupID | string | ID of the user group. | False |

## Response Body