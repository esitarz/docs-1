---
title: Admin Addresses
date: 2018-03-27
category: API Reference
tags: Seller
slug: Seller-AdminAddresses
---


## `GET` `v1/addresses/{addressID}`
Get a single admin address

| Name | Type | Description | Required | 
|---|---|---|---|
| addressID | string | ID of the address. | True |

## Response Body
	:::json
	{
	    "AddressName": "",
	    "City": "",
	    "CompanyName": "",
	    "Country": "",
	    "DateCreated": "2018-03-27T19:00:00+00:00",
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

## `GET` `v1/addresses`
Get a list of admin addresses

| Name | Type | Description | Required | 
|---|---|---|---|
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
	            "AddressName": "",
	            "City": "",
	            "CompanyName": "",
	            "Country": "",
	            "DateCreated": "2018-03-27T19:00:00+00:00",
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

## `POST` `v1/addresses`
Create a new admin address
## Request Body
	:::json
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
	:::json
	{
	    "AddressName": "",
	    "City": "",
	    "CompanyName": "",
	    "Country": "",
	    "DateCreated": "2018-03-27T19:00:00+00:00",
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

## `PUT` `v1/addresses/{addressID}`
Create or update an admin address

| Name | Type | Description | Required | 
|---|---|---|---|
| addressID | string | ID of the address. | True |

## Request Body
	:::json
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
	:::json
	{
	    "AddressName": "",
	    "City": "",
	    "CompanyName": "",
	    "Country": "",
	    "DateCreated": "2018-03-27T19:00:00+00:00",
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

## `DELETE` `v1/addresses/{addressID}`
Delete an admin address

| Name | Type | Description | Required | 
|---|---|---|---|
| addressID | string | ID of the address. | True |

## Response Body
## `PATCH` `v1/addresses/{addressID}`
Partially update an admin address

| Name | Type | Description | Required | 
|---|---|---|---|
| addressID | string | ID of the address. | True |

## Request Body
	:::json
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
	:::json
	{
	    "AddressName": "",
	    "City": "",
	    "CompanyName": "",
	    "Country": "",
	    "DateCreated": "2018-03-27T19:00:00+00:00",
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
