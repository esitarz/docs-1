---
title: Spending Accounts
date: 2018-03-27
category: API Reference
tags: Buyers
slug: Buyers-SpendingAccounts
---
Spending Accounts are funds given to users by a managing entity and are
managed as part of a user's account. These funds are generally used as
"corporate dollars", "rewards dollars", or "gift cards".
 They can be used to pay for all of or part of an order with parameters
that control account expiration, balance available, balance renewal,
user access and overdraft.
 Multiple spending accounts can be assigned to a member of an
organization and applied to all transactions, but only one can be used
as a payment method.
 When multiple Spending Accounts are used on a transaction each is
deducted individually.

---

## `GET` `v1/buyers/{buyerID}/spendingaccounts/{spendingAccountID}`
Get a single spending account

| Name | Type | Description | Required | 
|---|---|---|---|
| buyerID | string | ID of the buyer. | True |
| spendingAccountID | string | ID of the spending account. | True |

## Response Body
	{
	    "AllowAsPaymentMethod": false,
	    "Balance": 0,
	    "EndDate": "2018-03-21T23:00:00+00:00",
	    "ID": "",
	    "Name": "",
	    "RedemptionCode": "",
	    "StartDate": "2018-03-21T23:00:00+00:00",
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

## `GET` `v1/buyers/{buyerID}/spendingaccounts`
Get a list of spending accounts

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
	            "AllowAsPaymentMethod": false,
	            "Balance": 0,
	            "EndDate": "2018-03-21T23:00:00+00:00",
	            "ID": "",
	            "Name": "",
	            "RedemptionCode": "",
	            "StartDate": "2018-03-21T23:00:00+00:00",
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

## `POST` `v1/buyers/{buyerID}/spendingaccounts`
Create a new spending account

| Name | Type | Description | Required | 
|---|---|---|---|
| buyerID | string | ID of the buyer. | True |

## Request Body
	{
	    "AllowAsPaymentMethod": false,
	    "Balance": 0,
	    "EndDate": "2018-03-21T23:00:00+00:00",
	    "ID": "",
	    "Name": "",
	    "RedemptionCode": "",
	    "StartDate": "2018-03-21T23:00:00+00:00",
	    "xp": {}
	}
| Name | Type | Description | Required | 
|---|---|---|---|
| ID | string | ID of the spending account. Can only contain characters Aa-Zz, 0-9, -, and _. Searchable: priority level 1. Sortable: priority level 2. | False |
| Name | string | Name of the spending account. Required. Max length 100 characters. Searchable: priority level 2. Sortable: priority level 1. | True |
| Balance | float | Balance of the spending account. Required. | True |
| AllowAsPaymentMethod | boolean | Allow as payment method of the spending account. | False |
| RedemptionCode | string | If specified, matching code must be provided on redemption in order for the transaction to be successful. Most commonly used to implement Gift Cards. | False |
| StartDate | date | Start date of the spending account. | False |
| EndDate | date | End date of the spending account. | False |
| xp | object | Container for extended (custom) properties of the spending account. | False |

## Response Body
	{
	    "AllowAsPaymentMethod": false,
	    "Balance": 0,
	    "EndDate": "2018-03-21T23:00:00+00:00",
	    "ID": "",
	    "Name": "",
	    "RedemptionCode": "",
	    "StartDate": "2018-03-21T23:00:00+00:00",
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

## `PUT` `v1/buyers/{buyerID}/spendingaccounts/{spendingAccountID}`
Create or update a spending account

| Name | Type | Description | Required | 
|---|---|---|---|
| buyerID | string | ID of the buyer. | True |
| spendingAccountID | string | ID of the spending account. | True |

## Request Body
	{
	    "AllowAsPaymentMethod": false,
	    "Balance": 0,
	    "EndDate": "2018-03-21T23:00:00+00:00",
	    "ID": "",
	    "Name": "",
	    "RedemptionCode": "",
	    "StartDate": "2018-03-21T23:00:00+00:00",
	    "xp": {}
	}
| Name | Type | Description | Required | 
|---|---|---|---|
| ID | string | ID of the spending account. Can only contain characters Aa-Zz, 0-9, -, and _. Searchable: priority level 1. Sortable: priority level 2. | False |
| Name | string | Name of the spending account. Required. Max length 100 characters. Searchable: priority level 2. Sortable: priority level 1. | True |
| Balance | float | Balance of the spending account. Required. | True |
| AllowAsPaymentMethod | boolean | Allow as payment method of the spending account. | False |
| RedemptionCode | string | If specified, matching code must be provided on redemption in order for the transaction to be successful. Most commonly used to implement Gift Cards. | False |
| StartDate | date | Start date of the spending account. | False |
| EndDate | date | End date of the spending account. | False |
| xp | object | Container for extended (custom) properties of the spending account. | False |

## Response Body
	{
	    "AllowAsPaymentMethod": false,
	    "Balance": 0,
	    "EndDate": "2018-03-21T23:00:00+00:00",
	    "ID": "",
	    "Name": "",
	    "RedemptionCode": "",
	    "StartDate": "2018-03-21T23:00:00+00:00",
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

## `DELETE` `v1/buyers/{buyerID}/spendingaccounts/{spendingAccountID}`
Delete a spending account

| Name | Type | Description | Required | 
|---|---|---|---|
| buyerID | string | ID of the buyer. | True |
| spendingAccountID | string | ID of the spending account. | True |

## Response Body
## `PATCH` `v1/buyers/{buyerID}/spendingaccounts/{spendingAccountID}`
Partially update a spending account

| Name | Type | Description | Required | 
|---|---|---|---|
| buyerID | string | ID of the buyer. | True |
| spendingAccountID | string | ID of the spending account. | True |

## Request Body
	{
	    "AllowAsPaymentMethod": false,
	    "Balance": 0,
	    "EndDate": "2018-03-21T23:00:00+00:00",
	    "ID": "",
	    "Name": "",
	    "RedemptionCode": "",
	    "StartDate": "2018-03-21T23:00:00+00:00",
	    "xp": {}
	}
| Name | Type | Description | Required | 
|---|---|---|---|
| ID | string | ID of the spending account. Can only contain characters Aa-Zz, 0-9, -, and _. Searchable: priority level 1. Sortable: priority level 2. | False |
| Name | string | Name of the spending account. Required. Max length 100 characters. Searchable: priority level 2. Sortable: priority level 1. | True |
| Balance | float | Balance of the spending account. Required. | True |
| AllowAsPaymentMethod | boolean | Allow as payment method of the spending account. | False |
| RedemptionCode | string | If specified, matching code must be provided on redemption in order for the transaction to be successful. Most commonly used to implement Gift Cards. | False |
| StartDate | date | Start date of the spending account. | False |
| EndDate | date | End date of the spending account. | False |
| xp | object | Container for extended (custom) properties of the spending account. | False |

## Response Body
	{
	    "AllowAsPaymentMethod": false,
	    "Balance": 0,
	    "EndDate": "2018-03-21T23:00:00+00:00",
	    "ID": "",
	    "Name": "",
	    "RedemptionCode": "",
	    "StartDate": "2018-03-21T23:00:00+00:00",
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

## `GET` `v1/buyers/{buyerID}/spendingaccounts/assignments`
Get a list of spending account assignments

| Name | Type | Description | Required | 
|---|---|---|---|
| buyerID | string | ID of the buyer. | True |
| spendingAccountID | string | ID of the spending account. | False |
| userID | string | ID of the user. | False |
| userGroupID | string | ID of the user group. | False |
| level | string | Level of the spending account assignment. Possible values: User, Group, Company. | False |
| page | integer | Page of results to return. Default: 1 | False |
| pageSize | integer | Number of results to return per page. Default: 20, max: 100. | False |

## Response Body
	{
	    "Items": [
	        {
	            "AllowExceed": false,
	            "SpendingAccountID": "",
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
| SpendingAccountID | string | ID of the spending account. | True |
| UserID | string | ID of the user. | False |
| UserGroupID | string | ID of the user group. | False |
| AllowExceed | boolean | Allow exceed of the spending account assignment. | False |

## `POST` `v1/buyers/{buyerID}/spendingaccounts/assignments`
Save a spending account assignment

| Name | Type | Description | Required | 
|---|---|---|---|
| buyerID | string | ID of the buyer. | True |

## Request Body
	{
	    "AllowExceed": false,
	    "SpendingAccountID": "",
	    "UserGroupID": "",
	    "UserID": ""
	}
| Name | Type | Description | Required | 
|---|---|---|---|
| SpendingAccountID | string | ID of the spending account. Required. Sortable: priority level 1. | True |
| UserID | string | ID of the user. Sortable: priority level 2. | False |
| UserGroupID | string | ID of the user group. Sortable: priority level 3. | False |
| AllowExceed | boolean | Allow exceed of the spending account assignment. | False |

## Response Body
## `DELETE` `v1/buyers/{buyerID}/spendingaccounts/{spendingAccountID}/assignments`
Delete a spending account assignment

| Name | Type | Description | Required | 
|---|---|---|---|
| buyerID | string | ID of the buyer. | True |
| spendingAccountID | string | ID of the spending account. | True |
| userID | string | ID of the user. | False |
| userGroupID | string | ID of the user group. | False |

## Response Body