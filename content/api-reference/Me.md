---
title: Me
date: 2018-03-27
category: API Reference
tags: Me And My Stuff
slug: Me-And-My-Stuff-Me
---
"Me" is a container for read-only endpoints that return a filtered view
of things that the current buyer user is allowed to see, i.e. things
that they are assigned to either directly or as a member of a buyer
organization or user group. It also provides ways for a user to update
or change their own information.

---

## `GET` `v1/me`
Get the Current Authenticated User
## Request Body
**Response Status**: `200`

## Response Body
	{
	    "Active": false,
	    "AvailableRoles": [
	        ""
	    ],
	    "Buyer": {
	        "DefaultCatalogID": "",
	        "ID": ""
	    },
	    "Email": "",
	    "FirstName": "",
	    "ID": "",
	    "LastName": "",
	    "Phone": "",
	    "TermsAccepted": "2018-03-27T16:00:00+00:00",
	    "Username": "",
	    "xp": {}
	}
| Name | Type | Description | Required | 
|---|---|---|---|
| Buyer | object | Buyer of the user. | False |
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

## `PUT` `v1/me`
Update the Currently Authenticated User
## Request Body
	{
	    "Active": false,
	    "Email": "",
	    "FirstName": "",
	    "ID": "",
	    "LastName": "",
	    "Password": "",
	    "Phone": "",
	    "TermsAccepted": "2018-03-27T16:00:00+00:00",
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

**Response Status**: `200`

## Response Body
	{
	    "Active": false,
	    "AvailableRoles": [
	        ""
	    ],
	    "Buyer": {
	        "DefaultCatalogID": "",
	        "ID": ""
	    },
	    "Email": "",
	    "FirstName": "",
	    "ID": "",
	    "LastName": "",
	    "Phone": "",
	    "TermsAccepted": "2018-03-27T16:00:00+00:00",
	    "Username": "",
	    "xp": {}
	}
| Name | Type | Description | Required | 
|---|---|---|---|
| Buyer | object | Buyer of the user. | False |
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

## `PATCH` `v1/me`
Patch the Currently Authenticated User
## Request Body
	{
	    "Active": false,
	    "Email": "",
	    "FirstName": "",
	    "ID": "",
	    "LastName": "",
	    "Password": "",
	    "Phone": "",
	    "TermsAccepted": "2018-03-27T16:00:00+00:00",
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

**Response Status**: `200`

## Response Body
	{
	    "Active": false,
	    "AvailableRoles": [
	        ""
	    ],
	    "Buyer": {
	        "DefaultCatalogID": "",
	        "ID": ""
	    },
	    "Email": "",
	    "FirstName": "",
	    "ID": "",
	    "LastName": "",
	    "Phone": "",
	    "TermsAccepted": "2018-03-27T16:00:00+00:00",
	    "Username": "",
	    "xp": {}
	}
| Name | Type | Description | Required | 
|---|---|---|---|
| Buyer | object | Buyer of the user. | False |
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

## `PUT` `v1/me/register`
Register a register

| Parameters      | Description                    |
|------------------|---------------------------------|


| Parameters      | Description                    |
|------------------|---------------------------------|
| Name            | anonUserToken                  |
| Type            | string                         |
| Description     | Anon user token of the user.   |
| Required        | True                           |

## Request Body
	{
	    "Active": false,
	    "Email": "",
	    "FirstName": "",
	    "ID": "",
	    "LastName": "",
	    "Password": "",
	    "Phone": "",
	    "TermsAccepted": "2018-03-27T16:00:00+00:00",
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

**Response Status**: `200`

## Response Body
	{}
## `PUT` `v1/me/orders`
Transfer a anon user order

| Parameters      | Description                    |
|------------------|---------------------------------|


| Parameters      | Description                    |
|------------------|---------------------------------|
| Name            | anonUserToken                  |
| Type            | string                         |
| Description     | Anon user token of the me.     |
| Required        | True                           |

## Request Body
**Response Status**: `204`

## Response Body
## `POST` `v1/me/password`
Reset a password by token
## Request Body
	{
	    "NewPassword": ""
	}
| Name | Type | Description | Required | 
|---|---|---|---|
| NewPassword | string | New password of the token password reset. Required. | True |

**Response Status**: `204`

## Response Body