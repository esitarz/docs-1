---
title: Addresses
date: 2018-03-27
category: API Reference
tags: Buyers
slug: Buyers-Addresses
---
Addresses are used for the purposes of billing and shipping an order. An
address may belong to a list that can be shared among many users if
appropriate.

---

## `GET` `v1/buyers/{buyerID}/addresses/{addressID}`
Get a single address

| Name | Type | Description | Required | 
|---|---|---|---|
| buyerID | string | ID of the buyer. | True |
| addressID | string | ID of the address. | True |

## Response Body
	{
	    "AddressName": "",
	    "City": "",
	    "CompanyName": "",
	    "Country": "",
	    "DateCreated": "2018-03-21T23:00:00+00:00",
	    "FirstName": "",
	    "ID": "",
	    "LastName": "",
	    "Phone": "",
	    "State": "",
	    "Street1": "",
	    "Street2": "",
	    "Zip": "",
	    "xp": {}
	}
| Name | Type | Description | Required | 
|---|---|---|---|
| ID | string | ID of the address. | False |
| DateCreated | date | Date created of the address. | False |
| CompanyName | string | Company name of the address. | False |
| FirstName | string | First name of the address. | False |
| LastName | string | Last name of the address. | False |
| Street1 | string | Street 1 of the address. | True |
| Street2 | string | Street 2 of the address. | False |
| City | string | City of the address. | True |
| State | string | State of the address. | True |
| Zip | string | Zip of the address. | True |
| Country | string | Country of the address. | True |
| Phone | string | Phone of the address. | False |
| AddressName | string | Address name of the address. | False |
| xp | object | Container for extended (custom) properties of the address. | False |

## `GET` `v1/buyers/{buyerID}/addresses`
Get a list of addresses

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
	{
	    "Items": [
	        {
	            "AddressName": "",
	            "City": "",
	            "CompanyName": "",
	            "Country": "",
	            "DateCreated": "2018-03-21T23:00:00+00:00",
	            "FirstName": "",
	            "ID": "",
	            "LastName": "",
	            "Phone": "",
	            "State": "",
	            "Street1": "",
	            "Street2": "",
	            "Zip": "",
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
| ID | string | ID of the address. | False |
| DateCreated | date | Date created of the address. | False |
| CompanyName | string | Company name of the address. | False |
| FirstName | string | First name of the address. | False |
| LastName | string | Last name of the address. | False |
| Street1 | string | Street 1 of the address. | True |
| Street2 | string | Street 2 of the address. | False |
| City | string | City of the address. | True |
| State | string | State of the address. | True |
| Zip | string | Zip of the address. | True |
| Country | string | Country of the address. | True |
| Phone | string | Phone of the address. | False |
| AddressName | string | Address name of the address. | False |
| xp | object | Container for extended (custom) properties of the address. | False |

## `POST` `v1/buyers/{buyerID}/addresses`
Create a new address

| Name | Type | Description | Required | 
|---|---|---|---|
| buyerID | string | ID of the buyer. | True |

## Request Body
	{
	    "AddressName": "",
	    "City": "",
	    "CompanyName": "",
	    "Country": "",
	    "FirstName": "",
	    "ID": "",
	    "LastName": "",
	    "Phone": "",
	    "State": "",
	    "Street1": "",
	    "Street2": "",
	    "Zip": "",
	    "xp": {}
	}
| Name | Type | Description | Required | 
|---|---|---|---|
| ID | string | ID of the address. Can only contain characters Aa-Zz, 0-9, -, and _. Searchable: priority level 1. Sortable: priority level 2. | False |
| CompanyName | string | Company name of the address. Max length 100 characters. Sortable. | False |
| FirstName | string | First name of the address. Max length 100 characters. Searchable: priority level 7. Sortable. | False |
| LastName | string | Last name of the address. Max length 100 characters. Searchable: priority level 6. Sortable. | False |
| Street1 | string | Street 1 of the address. Required. Max length 100 characters. Searchable: priority level 4. Sortable. | True |
| Street2 | string | Street 2 of the address. Max length 100 characters. Searchable: priority level 5. Sortable. | False |
| City | string | City of the address. Required. Max length 100 characters. Searchable: priority level 3. Sortable. | True |
| State | string | State of the address. Required. Max length 100 characters. Searchable: priority level 7. Sortable. | True |
| Zip | string | Zip of the address. Required. Max length 100 characters. Searchable: priority level 6. Sortable. | True |
| Country | string | Country of the address. Required. Max length 2 characters. Sortable. | True |
| Phone | string | Phone of the address. Max length 100 characters. Sortable. | False |
| AddressName | string | Address name of the address. Max length 100 characters. Searchable: priority level 2. Sortable: priority level 1. | False |
| xp | object | Container for extended (custom) properties of the address. | False |

## Response Body
	{
	    "AddressName": "",
	    "City": "",
	    "CompanyName": "",
	    "Country": "",
	    "DateCreated": "2018-03-21T23:00:00+00:00",
	    "FirstName": "",
	    "ID": "",
	    "LastName": "",
	    "Phone": "",
	    "State": "",
	    "Street1": "",
	    "Street2": "",
	    "Zip": "",
	    "xp": {}
	}
| Name | Type | Description | Required | 
|---|---|---|---|
| ID | string | ID of the address. | False |
| DateCreated | date | Date created of the address. | False |
| CompanyName | string | Company name of the address. | False |
| FirstName | string | First name of the address. | False |
| LastName | string | Last name of the address. | False |
| Street1 | string | Street 1 of the address. | True |
| Street2 | string | Street 2 of the address. | False |
| City | string | City of the address. | True |
| State | string | State of the address. | True |
| Zip | string | Zip of the address. | True |
| Country | string | Country of the address. | True |
| Phone | string | Phone of the address. | False |
| AddressName | string | Address name of the address. | False |
| xp | object | Container for extended (custom) properties of the address. | False |

## `PUT` `v1/buyers/{buyerID}/addresses/{addressID}`
Create or update an address

| Name | Type | Description | Required | 
|---|---|---|---|
| buyerID | string | ID of the buyer. | True |
| addressID | string | ID of the address. | True |

## Request Body
	{
	    "AddressName": "",
	    "City": "",
	    "CompanyName": "",
	    "Country": "",
	    "FirstName": "",
	    "ID": "",
	    "LastName": "",
	    "Phone": "",
	    "State": "",
	    "Street1": "",
	    "Street2": "",
	    "Zip": "",
	    "xp": {}
	}
| Name | Type | Description | Required | 
|---|---|---|---|
| ID | string | ID of the address. Can only contain characters Aa-Zz, 0-9, -, and _. Searchable: priority level 1. Sortable: priority level 2. | False |
| CompanyName | string | Company name of the address. Max length 100 characters. Sortable. | False |
| FirstName | string | First name of the address. Max length 100 characters. Searchable: priority level 7. Sortable. | False |
| LastName | string | Last name of the address. Max length 100 characters. Searchable: priority level 6. Sortable. | False |
| Street1 | string | Street 1 of the address. Required. Max length 100 characters. Searchable: priority level 4. Sortable. | True |
| Street2 | string | Street 2 of the address. Max length 100 characters. Searchable: priority level 5. Sortable. | False |
| City | string | City of the address. Required. Max length 100 characters. Searchable: priority level 3. Sortable. | True |
| State | string | State of the address. Required. Max length 100 characters. Searchable: priority level 7. Sortable. | True |
| Zip | string | Zip of the address. Required. Max length 100 characters. Searchable: priority level 6. Sortable. | True |
| Country | string | Country of the address. Required. Max length 2 characters. Sortable. | True |
| Phone | string | Phone of the address. Max length 100 characters. Sortable. | False |
| AddressName | string | Address name of the address. Max length 100 characters. Searchable: priority level 2. Sortable: priority level 1. | False |
| xp | object | Container for extended (custom) properties of the address. | False |

## Response Body
	{
	    "AddressName": "",
	    "City": "",
	    "CompanyName": "",
	    "Country": "",
	    "DateCreated": "2018-03-21T23:00:00+00:00",
	    "FirstName": "",
	    "ID": "",
	    "LastName": "",
	    "Phone": "",
	    "State": "",
	    "Street1": "",
	    "Street2": "",
	    "Zip": "",
	    "xp": {}
	}
| Name | Type | Description | Required | 
|---|---|---|---|
| ID | string | ID of the address. | False |
| DateCreated | date | Date created of the address. | False |
| CompanyName | string | Company name of the address. | False |
| FirstName | string | First name of the address. | False |
| LastName | string | Last name of the address. | False |
| Street1 | string | Street 1 of the address. | True |
| Street2 | string | Street 2 of the address. | False |
| City | string | City of the address. | True |
| State | string | State of the address. | True |
| Zip | string | Zip of the address. | True |
| Country | string | Country of the address. | True |
| Phone | string | Phone of the address. | False |
| AddressName | string | Address name of the address. | False |
| xp | object | Container for extended (custom) properties of the address. | False |

## `DELETE` `v1/buyers/{buyerID}/addresses/{addressID}`
Delete an address

| Name | Type | Description | Required | 
|---|---|---|---|
| buyerID | string | ID of the buyer. | True |
| addressID | string | ID of the address. | True |

## Response Body
## `PATCH` `v1/buyers/{buyerID}/addresses/{addressID}`
Partially update an address

| Name | Type | Description | Required | 
|---|---|---|---|
| buyerID | string | ID of the buyer. | True |
| addressID | string | ID of the address. | True |

## Request Body
	{
	    "AddressName": "",
	    "City": "",
	    "CompanyName": "",
	    "Country": "",
	    "FirstName": "",
	    "ID": "",
	    "LastName": "",
	    "Phone": "",
	    "State": "",
	    "Street1": "",
	    "Street2": "",
	    "Zip": "",
	    "xp": {}
	}
| Name | Type | Description | Required | 
|---|---|---|---|
| ID | string | ID of the address. Can only contain characters Aa-Zz, 0-9, -, and _. Searchable: priority level 1. Sortable: priority level 2. | False |
| CompanyName | string | Company name of the address. Max length 100 characters. Sortable. | False |
| FirstName | string | First name of the address. Max length 100 characters. Searchable: priority level 7. Sortable. | False |
| LastName | string | Last name of the address. Max length 100 characters. Searchable: priority level 6. Sortable. | False |
| Street1 | string | Street 1 of the address. Required. Max length 100 characters. Searchable: priority level 4. Sortable. | True |
| Street2 | string | Street 2 of the address. Max length 100 characters. Searchable: priority level 5. Sortable. | False |
| City | string | City of the address. Required. Max length 100 characters. Searchable: priority level 3. Sortable. | True |
| State | string | State of the address. Required. Max length 100 characters. Searchable: priority level 7. Sortable. | True |
| Zip | string | Zip of the address. Required. Max length 100 characters. Searchable: priority level 6. Sortable. | True |
| Country | string | Country of the address. Required. Max length 2 characters. Sortable. | True |
| Phone | string | Phone of the address. Max length 100 characters. Sortable. | False |
| AddressName | string | Address name of the address. Max length 100 characters. Searchable: priority level 2. Sortable: priority level 1. | False |
| xp | object | Container for extended (custom) properties of the address. | False |

## Response Body
	{
	    "AddressName": "",
	    "City": "",
	    "CompanyName": "",
	    "Country": "",
	    "DateCreated": "2018-03-21T23:00:00+00:00",
	    "FirstName": "",
	    "ID": "",
	    "LastName": "",
	    "Phone": "",
	    "State": "",
	    "Street1": "",
	    "Street2": "",
	    "Zip": "",
	    "xp": {}
	}
| Name | Type | Description | Required | 
|---|---|---|---|
| ID | string | ID of the address. | False |
| DateCreated | date | Date created of the address. | False |
| CompanyName | string | Company name of the address. | False |
| FirstName | string | First name of the address. | False |
| LastName | string | Last name of the address. | False |
| Street1 | string | Street 1 of the address. | True |
| Street2 | string | Street 2 of the address. | False |
| City | string | City of the address. | True |
| State | string | State of the address. | True |
| Zip | string | Zip of the address. | True |
| Country | string | Country of the address. | True |
| Phone | string | Phone of the address. | False |
| AddressName | string | Address name of the address. | False |
| xp | object | Container for extended (custom) properties of the address. | False |

## `GET` `v1/buyers/{buyerID}/addresses/assignments`
Get a list of address assignments

| Name | Type | Description | Required | 
|---|---|---|---|
| buyerID | string | ID of the buyer. | True |
| addressID | string | ID of the address. | False |
| userID | string | ID of the user. | False |
| userGroupID | string | ID of the user group. | False |
| level | string | Level of the address assignment. Possible values: User, Group, Company. | False |
| isShipping | boolean | Is shipping of the address assignment. | False |
| isBilling | boolean | Is billing of the address assignment. | False |
| page | integer | Page of results to return. Default: 1 | False |
| pageSize | integer | Number of results to return per page. Default: 20, max: 100. | False |

## Response Body
	{
	    "Items": [
	        {
	            "AddressID": "",
	            "IsBilling": false,
	            "IsShipping": false,
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
| AddressID | string | ID of the address. | True |
| UserID | string | ID of the user. | False |
| UserGroupID | string | ID of the user group. | False |
| IsShipping | boolean | Is shipping of the address assignment. | False |
| IsBilling | boolean | Is billing of the address assignment. | False |

## `DELETE` `v1/buyers/{buyerID}/addresses/{addressID}/assignments`
Delete an address assignment

| Name | Type | Description | Required | 
|---|---|---|---|
| buyerID | string | ID of the buyer. | True |
| addressID | string | ID of the address. | True |
| userID | string | ID of the user. | False |
| userGroupID | string | ID of the user group. | False |

## Response Body
## `POST` `v1/buyers/{buyerID}/addresses/assignments`
Save an address assignment

| Name | Type | Description | Required | 
|---|---|---|---|
| buyerID | string | ID of the buyer. | True |

## Request Body
	{
	    "AddressID": "",
	    "IsBilling": false,
	    "IsShipping": false,
	    "UserGroupID": "",
	    "UserID": ""
	}
| Name | Type | Description | Required | 
|---|---|---|---|
| AddressID | string | ID of the address. Required. Sortable: priority level 1. | True |
| UserID | string | ID of the user. Sortable: priority level 2. | False |
| UserGroupID | string | ID of the user group. Sortable: priority level 3. | False |
| IsShipping | boolean | Is shipping of the address assignment. | False |
| IsBilling | boolean | Is billing of the address assignment. | False |

## Response Body