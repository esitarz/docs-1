---
title: Admin Users
date: 2018-03-27
category: API Reference
tags: Seller
slug: Seller-AdminUsers
---
Users on an Organization level are users that have administrative access
to things like adding users, creating catalogs, processing orders or
creating products. These users are not specific to a buyer company.

---

## `GET` `v1/adminusers/{userID}`
Get a single admin user

| Name | Type | Description | Required | 
|---|---|---|---|
| userID | string | ID of the user. | True |

## Response Body
	:::json
	{
	    "Active": false,
	    "AvailableRoles": [
	        ""
	    ],
	    "Email": "",
	    "FirstName": "",
	    "ID": "",
	    "LastName": "",
	    "Phone": "",
	    "TermsAccepted": "2018-03-27T19:00:00+00:00",
	    "Username": "",
	    "xp": {}
	}


| Name | Type | Description | Required | 
|---|---|---|---|
| ID | string | ID of the user. | False |
| Username | string | Username of the user. | True |
| FirstName | string | First name of the user. | True |
| LastName | string | Last name of the user. | True |
| Email | string | Email of the user. | True |
| Phone | string | Phone of the user. | False |
| TermsAccepted | date | Terms accepted of the user. | False |
| Active | boolean | Active of the user. | True |
| xp | object | Container for extended (custom) properties of the user. | False |
| AvailableRoles | array | Available roles of the user. | False |

## `GET` `v1/adminusers`
Get a list of admin users

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
	            "Active": false,
	            "AvailableRoles": [
	                ""
	            ],
	            "Email": "",
	            "FirstName": "",
	            "ID": "",
	            "LastName": "",
	            "Phone": "",
	            "TermsAccepted": "2018-03-27T19:00:00+00:00",
	            "Username": "",
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
| ID | string | ID of the user. | False |
| Username | string | Username of the user. | True |
| FirstName | string | First name of the user. | True |
| LastName | string | Last name of the user. | True |
| Email | string | Email of the user. | True |
| Phone | string | Phone of the user. | False |
| TermsAccepted | date | Terms accepted of the user. | False |
| Active | boolean | Active of the user. | True |
| xp | object | Container for extended (custom) properties of the user. | False |
| AvailableRoles | array | Available roles of the user. | False |

## `POST` `v1/adminusers`
Create a new admin user
## Request Body
	:::json
	{
	    "Active": false,
	    "Email": "",
	    "FirstName": "",
	    "ID": "",
	    "LastName": "",
	    "Password": "",
	    "Phone": "",
	    "TermsAccepted": "2018-03-27T19:00:00+00:00",
	    "Username": "",
	    "xp": {}
	}


| Name | Type | Description | Required | 
|---|---|---|---|
| ID | string | ID of the user. Can only contain characters Aa-Zz, 0-9, -, and _. Searchable: priority level 1. Sortable. | False |
| Username | string | Username of the user. Required. Max length 100 characters. Searchable: priority level 2. Sortable: priority level 3. | True |
| Password | string | Password of the user. | False |
| FirstName | string | First name of the user. Required. Max length 100 characters. Searchable: priority level 4. Sortable: priority level 2. | True |
| LastName | string | Last name of the user. Required. Max length 100 characters. Searchable: priority level 3. Sortable: priority level 1. | True |
| Email | string | Email of the user. Required. Max length 200 characters. Searchable: priority level 5. Sortable. | True |
| Phone | string | Phone of the user. Max length 100 characters. | False |
| TermsAccepted | date | Terms accepted of the user. | False |
| Active | boolean | Active of the user. Required. | True |
| xp | object | Container for extended (custom) properties of the user. | False |

## Response Body
	:::json
	{
	    "Active": false,
	    "AvailableRoles": [
	        ""
	    ],
	    "Email": "",
	    "FirstName": "",
	    "ID": "",
	    "LastName": "",
	    "Phone": "",
	    "TermsAccepted": "2018-03-27T19:00:00+00:00",
	    "Username": "",
	    "xp": {}
	}


| Name | Type | Description | Required | 
|---|---|---|---|
| ID | string | ID of the user. | False |
| Username | string | Username of the user. | True |
| FirstName | string | First name of the user. | True |
| LastName | string | Last name of the user. | True |
| Email | string | Email of the user. | True |
| Phone | string | Phone of the user. | False |
| TermsAccepted | date | Terms accepted of the user. | False |
| Active | boolean | Active of the user. | True |
| xp | object | Container for extended (custom) properties of the user. | False |
| AvailableRoles | array | Available roles of the user. | False |

## `PUT` `v1/adminusers/{userID}`
Create or update an admin user

| Name | Type | Description | Required | 
|---|---|---|---|
| userID | string | ID of the user. | True |

## Request Body
	:::json
	{
	    "Active": false,
	    "Email": "",
	    "FirstName": "",
	    "ID": "",
	    "LastName": "",
	    "Password": "",
	    "Phone": "",
	    "TermsAccepted": "2018-03-27T19:00:00+00:00",
	    "Username": "",
	    "xp": {}
	}


| Name | Type | Description | Required | 
|---|---|---|---|
| ID | string | ID of the user. Can only contain characters Aa-Zz, 0-9, -, and _. Searchable: priority level 1. Sortable. | False |
| Username | string | Username of the user. Required. Max length 100 characters. Searchable: priority level 2. Sortable: priority level 3. | True |
| Password | string | Password of the user. | False |
| FirstName | string | First name of the user. Required. Max length 100 characters. Searchable: priority level 4. Sortable: priority level 2. | True |
| LastName | string | Last name of the user. Required. Max length 100 characters. Searchable: priority level 3. Sortable: priority level 1. | True |
| Email | string | Email of the user. Required. Max length 200 characters. Searchable: priority level 5. Sortable. | True |
| Phone | string | Phone of the user. Max length 100 characters. | False |
| TermsAccepted | date | Terms accepted of the user. | False |
| Active | boolean | Active of the user. Required. | True |
| xp | object | Container for extended (custom) properties of the user. | False |

## Response Body
	:::json
	{
	    "Active": false,
	    "AvailableRoles": [
	        ""
	    ],
	    "Email": "",
	    "FirstName": "",
	    "ID": "",
	    "LastName": "",
	    "Phone": "",
	    "TermsAccepted": "2018-03-27T19:00:00+00:00",
	    "Username": "",
	    "xp": {}
	}


| Name | Type | Description | Required | 
|---|---|---|---|
| ID | string | ID of the user. | False |
| Username | string | Username of the user. | True |
| FirstName | string | First name of the user. | True |
| LastName | string | Last name of the user. | True |
| Email | string | Email of the user. | True |
| Phone | string | Phone of the user. | False |
| TermsAccepted | date | Terms accepted of the user. | False |
| Active | boolean | Active of the user. | True |
| xp | object | Container for extended (custom) properties of the user. | False |
| AvailableRoles | array | Available roles of the user. | False |

## `DELETE` `v1/adminusers/{userID}`
Delete an admin user

| Name | Type | Description | Required | 
|---|---|---|---|
| userID | string | ID of the user. | True |

## Response Body
## `PATCH` `v1/adminusers/{userID}`
Partially update an admin user

| Name | Type | Description | Required | 
|---|---|---|---|
| userID | string | ID of the user. | True |

## Request Body
	:::json
	{
	    "Active": false,
	    "Email": "",
	    "FirstName": "",
	    "ID": "",
	    "LastName": "",
	    "Password": "",
	    "Phone": "",
	    "TermsAccepted": "2018-03-27T19:00:00+00:00",
	    "Username": "",
	    "xp": {}
	}


| Name | Type | Description | Required | 
|---|---|---|---|
| ID | string | ID of the user. Can only contain characters Aa-Zz, 0-9, -, and _. Searchable: priority level 1. Sortable. | False |
| Username | string | Username of the user. Required. Max length 100 characters. Searchable: priority level 2. Sortable: priority level 3. | True |
| Password | string | Password of the user. | False |
| FirstName | string | First name of the user. Required. Max length 100 characters. Searchable: priority level 4. Sortable: priority level 2. | True |
| LastName | string | Last name of the user. Required. Max length 100 characters. Searchable: priority level 3. Sortable: priority level 1. | True |
| Email | string | Email of the user. Required. Max length 200 characters. Searchable: priority level 5. Sortable. | True |
| Phone | string | Phone of the user. Max length 100 characters. | False |
| TermsAccepted | date | Terms accepted of the user. | False |
| Active | boolean | Active of the user. Required. | True |
| xp | object | Container for extended (custom) properties of the user. | False |

## Response Body
	:::json
	{
	    "Active": false,
	    "AvailableRoles": [
	        ""
	    ],
	    "Email": "",
	    "FirstName": "",
	    "ID": "",
	    "LastName": "",
	    "Phone": "",
	    "TermsAccepted": "2018-03-27T19:00:00+00:00",
	    "Username": "",
	    "xp": {}
	}


| Name | Type | Description | Required | 
|---|---|---|---|
| ID | string | ID of the user. | False |
| Username | string | Username of the user. | True |
| FirstName | string | First name of the user. | True |
| LastName | string | Last name of the user. | True |
| Email | string | Email of the user. | True |
| Phone | string | Phone of the user. | False |
| TermsAccepted | date | Terms accepted of the user. | False |
| Active | boolean | Active of the user. | True |
| xp | object | Container for extended (custom) properties of the user. | False |
| AvailableRoles | array | Available roles of the user. | False |
