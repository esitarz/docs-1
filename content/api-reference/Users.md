---
title: Users
date: 2018-03-27
category: API Reference
tags: Buyers
slug: Buyers-Users
---
A user is a person with access to the application. The properties of a
user define who they are and what they are able to do with their login
to the application.

---

## `GET` `v1/buyers/{buyerID}/users/{userID}`
Get a single user

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
| Name            | userID                         |
| Type            | string                         |
| Description     | ID of the user.                |
| Required        | True                           |

## Request Body
**Response Status**: `200`

## Response Body
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
	    "TermsAccepted": "2018-03-27T16:00:00+00:00",
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

## `GET` `v1/buyers/{buyerID}/users`
Get a list of users

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
| Name            | userGroupID                    |
| Type            | string                         |
| Description     | ID of the user group.          |
| Required        | False                          |


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
	            "Active": false,
	            "AvailableRoles": [
	                ""
	            ],
	            "Email": "",
	            "FirstName": "",
	            "ID": "",
	            "LastName": "",
	            "Phone": "",
	            "TermsAccepted": "2018-03-27T16:00:00+00:00",
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

## `POST` `v1/buyers/{buyerID}/users`
Create a new user

| Parameters      | Description                    |
|------------------|---------------------------------|


| Parameters      | Description                    |
|------------------|---------------------------------|
| Name            | buyerID                        |
| Type            | string                         |
| Description     | ID of the buyer.               |
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

**Response Status**: `201`

## Response Body
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
	    "TermsAccepted": "2018-03-27T16:00:00+00:00",
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

## `PUT` `v1/buyers/{buyerID}/users/{userID}`
Create or update a user

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
| Name            | userID                         |
| Type            | string                         |
| Description     | ID of the user.                |
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
	    "TermsAccepted": "2018-03-27T16:00:00+00:00",
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

## `DELETE` `v1/buyers/{buyerID}/users/{userID}`
Delete a user

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
| Name            | userID                         |
| Type            | string                         |
| Description     | ID of the user.                |
| Required        | True                           |

## Request Body
**Response Status**: `204`

## Response Body
## `PATCH` `v1/buyers/{buyerID}/users/{userID}`
Partially update a user

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
| Name            | userID                         |
| Type            | string                         |
| Description     | ID of the user.                |
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
	    "TermsAccepted": "2018-03-27T16:00:00+00:00",
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

## `POST` `v1/buyers/{buyerID}/users/{userID}/moveto/{newBuyerID}`
Move a user to a different buyer

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
| Name            | userID                         |
| Type            | string                         |
| Description     | ID of the user.                |
| Required        | True                           |


| Parameters      | Description                    |
|------------------|---------------------------------|
| Name            | newBuyerID                     |
| Type            | string                         |
| Description     | ID of the new buyer.           |
| Required        | True                           |


| Parameters      | Description                    |
|------------------|---------------------------------|
| Name            | orders                         |
| Type            | string                         |
| Description     | Orders of the user. Possible values: None, Unsubmitted, All. |
| Required        | True                           |

## Request Body
**Response Status**: `201`

## Response Body
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
	    "TermsAccepted": "2018-03-27T16:00:00+00:00",
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

## `POST` `v1/buyers/{buyerID}/users/{userID}/accesstoken`
Get a single user access token

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
| Name            | userID                         |
| Type            | string                         |
| Description     | ID of the user.                |
| Required        | True                           |

## Request Body
	{
	    "ClientID": "",
	    "Roles": [
	        "DevCenterImpersonate"
	    ]
	}
| Name | Type | Description | Required | 
|---|---|---|---|
| ClientID | string | ID of the client. | False |
| Roles | array | Roles of the impersonate token request. | False |

**Response Status**: `200`

## Response Body
	{
	    "access_token": "",
	    "expires_in": 0,
	    "refresh_token": "",
	    "token_type": ""
	}
| Name | Type | Description | Required | 
|---|---|---|---|
| access_token | string | Access token of the access token. | False |
| expires_in | integer | Expires in of the access token. | False |
| token_type | string | Token type of the access token. | False |
| refresh_token | string | Refresh token of the access token. | False |
