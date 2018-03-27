---
title: Spending Accounts
date: 2018-03-27
category: API Reference
tags: Me And My Stuff
slug: Me-And-My-Stuff-MeSpendingAccounts
---
"Me" is a container for read-only endpoints that return a filtered view
of things that the current buyer user is allowed to see, i.e. things
that they are assigned to either directly or as a member of a buyer
organization or user group. It also provides ways for a user to update
or change their own information.

---

## `GET` `v1/me/spendingAccounts`
Get a list of spending accounts visible to this user

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
	            "AllowAsPaymentMethod": false,
	            "Balance": 0,
	            "EndDate": "2018-03-27T16:00:00+00:00",
	            "ID": "",
	            "Name": "",
	            "RedemptionCode": "",
	            "StartDate": "2018-03-27T16:00:00+00:00",
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
| ID | string | ID of the spending account. | False |
| Name | string | Name of the spending account. | True |
| Balance | float | Balance of the spending account. | True |
| AllowAsPaymentMethod | boolean | Allow as payment method of the spending account. | False |
| RedemptionCode | string | If specified, matching code must be provided on redemption in order for the transaction to be successful. Most commonly used to implement Gift Cards. | False |
| StartDate | date | Start date of the spending account. | False |
| EndDate | date | End date of the spending account. | False |
| xp | object | Container for extended (custom) properties of the spending account. | False |

## `GET` `v1/me/spendingaccounts/{spendingAccountID}`
Get a single spending account

| Parameters      | Description                    |
|------------------|---------------------------------|


| Parameters      | Description                    |
|------------------|---------------------------------|
| Name            | spendingAccountID              |
| Type            | string                         |
| Description     | ID of the spending account.    |
| Required        | True                           |

## Request Body
**Response Status**: `200`

## Response Body
	{
	    "AllowAsPaymentMethod": false,
	    "Balance": 0,
	    "EndDate": "2018-03-27T16:00:00+00:00",
	    "ID": "",
	    "Name": "",
	    "RedemptionCode": "",
	    "StartDate": "2018-03-27T16:00:00+00:00",
	    "xp": {}
	}
| Name | Type | Description | Required | 
|---|---|---|---|
| ID | string | ID of the spending account. | False |
| Name | string | Name of the spending account. | True |
| Balance | float | Balance of the spending account. | True |
| AllowAsPaymentMethod | boolean | Allow as payment method of the spending account. | False |
| RedemptionCode | string | If specified, matching code must be provided on redemption in order for the transaction to be successful. Most commonly used to implement Gift Cards. | False |
| StartDate | date | Start date of the spending account. | False |
| EndDate | date | End date of the spending account. | False |
| xp | object | Container for extended (custom) properties of the spending account. | False |
