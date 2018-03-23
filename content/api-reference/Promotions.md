---
title: Promotions
date: 2018-03-23
category: API Reference
tags: Orders And Fulfillment
slug: Promotions
---
Promotions are used to reduce the cost of a line item or an order.
Promotions can have redemption rules that can be applied for available
dates, occurences and value.
Promotions can be assigned to Products, Categories, Buyers, UserGroups
and Users for redemption.

---

## Get a single promotion
### `GET` `v1/promotions/{promotionID}`

| Parameters      | Description                    |
|------------------|---------------------------------|
| Name            | promotionID                    |
| Type            | string                         |
| Description     | ID of the promotion.           |
| Required        | True                           |

 **Requestbody**: 
None
 **Responsestatus**: `200`

 **Responsebody**: 
{'Sample': '{\r\n  "ID": "",\r\n  "Code": "",\r\n  "Name": "",\r\n  "RedemptionLimit": 0,\r\n  "RedemptionLimitPerUser": 0,\r\n  "RedemptionCount": 0,\r\n  "Description": "",\r\n  "FinePrint": "",\r\n  "StartDate": "2018-03-21T23:00:00+00:00",\r\n  "ExpirationDate": "2018-03-21T23:00:00+00:00",\r\n  "EligibleExpression": "",\r\n  "ValueExpression": "",\r\n  "CanCombine": false,\r\n  "xp": {}\r\n}', 'Fields': [{'Name': 'ID', 'Type': 'string', 'Description': 'ID of the promotion.', 'Required': False}, {'Name': 'Code', 'Type': 'string', 'Description': 'Must be unique. Entered by buyer when adding promo to order.', 'Required': True}, {'Name': 'Name', 'Type': 'string', 'Description': 'Name of the promotion.', 'Required': False}, {'Name': 'RedemptionLimit', 'Type': 'integer', 'Description': 'Redemption limit of the promotion.', 'Required': False}, {'Name': 'RedemptionLimitPerUser', 'Type': 'integer', 'Description': 'Redemption limit per user of the promotion.', 'Required': False}, {'Name': 'RedemptionCount', 'Type': 'integer', 'Description': 'Redemption count of the promotion.', 'Required': False}, {'Name': 'Description', 'Type': 'string', 'Description': 'Description of the promotion.', 'Required': False}, {'Name': 'FinePrint', 'Type': 'string', 'Description': 'Terms, conditions, and other legal jargon.', 'Required': False}, {'Name': 'StartDate', 'Type': 'date', 'Description': 'Start date of the promotion.', 'Required': False}, {'Name': 'ExpirationDate', 'Type': 'date', 'Description': 'Expiration date of the promotion.', 'Required': False}, {'Name': 'EligibleExpression', 'Type': 'string', 'Description': 'Eligible expression of the promotion.', 'Required': True}, {'Name': 'ValueExpression', 'Type': 'string', 'Description': 'Value expression of the promotion.', 'Required': True}, {'Name': 'CanCombine', 'Type': 'boolean', 'Description': 'Can combine of the promotion.', 'Required': False}, {'Name': 'xp', 'Type': 'object', 'Description': 'Container for extended (custom) properties of the promotion.', 'Required': False}]}
## Get a list of promotions
### `GET` `v1/promotions`

| Parameters      | Description                    |
|------------------|---------------------------------|
| Name            | search                         |
| Type            | string                         |
| Description     | Word or phrase to search for.  |
| Required        | False                          |
| Name            | searchOn                       |
| Type            | string                         |
| Description     | Comma-delimited list of fields to search on. |
| Required        | False                          |
| Name            | sortBy                         |
| Type            | string                         |
| Description     | Comma-delimited list of fields to sort by. |
| Required        | False                          |
| Name            | page                           |
| Type            | integer                        |
| Description     | Page of results to return. Default: 1 |
| Required        | False                          |
| Name            | pageSize                       |
| Type            | integer                        |
| Description     | Number of results to return per page. Default: 20, max: 100. |
| Required        | False                          |
| Name            | filters                        |
| Type            | object                         |
| Description     | Any additional key/value pairs passed in the query string are interpretted as filters. Valid keys are top-level properties of the returned model or 'xp.???' |
| Required        | False                          |

 **Requestbody**: 
None
 **Responsestatus**: `200`

 **Responsebody**: 
{'Sample': '{\r\n  "Meta": {\r\n    "Page": 1,\r\n    "PageSize": 20,\r\n    "TotalCount": 25,\r\n    "TotalPages": 2,\r\n    "ItemRange": [\r\n      1,\r\n      20\r\n    ]\r\n  },\r\n  "Items": [\r\n    {\r\n      "ID": "",\r\n      "Code": "",\r\n      "Name": "",\r\n      "RedemptionLimit": 0,\r\n      "RedemptionLimitPerUser": 0,\r\n      "RedemptionCount": 0,\r\n      "Description": "",\r\n      "FinePrint": "",\r\n      "StartDate": "2018-03-21T23:00:00+00:00",\r\n      "ExpirationDate": "2018-03-21T23:00:00+00:00",\r\n      "EligibleExpression": "",\r\n      "ValueExpression": "",\r\n      "CanCombine": false,\r\n      "xp": {}\r\n    }\r\n  ]\r\n}', 'Fields': [{'Name': 'ID', 'Type': 'string', 'Description': 'ID of the promotion.', 'Required': False}, {'Name': 'Code', 'Type': 'string', 'Description': 'Must be unique. Entered by buyer when adding promo to order.', 'Required': True}, {'Name': 'Name', 'Type': 'string', 'Description': 'Name of the promotion.', 'Required': False}, {'Name': 'RedemptionLimit', 'Type': 'integer', 'Description': 'Redemption limit of the promotion.', 'Required': False}, {'Name': 'RedemptionLimitPerUser', 'Type': 'integer', 'Description': 'Redemption limit per user of the promotion.', 'Required': False}, {'Name': 'RedemptionCount', 'Type': 'integer', 'Description': 'Redemption count of the promotion.', 'Required': False}, {'Name': 'Description', 'Type': 'string', 'Description': 'Description of the promotion.', 'Required': False}, {'Name': 'FinePrint', 'Type': 'string', 'Description': 'Terms, conditions, and other legal jargon.', 'Required': False}, {'Name': 'StartDate', 'Type': 'date', 'Description': 'Start date of the promotion.', 'Required': False}, {'Name': 'ExpirationDate', 'Type': 'date', 'Description': 'Expiration date of the promotion.', 'Required': False}, {'Name': 'EligibleExpression', 'Type': 'string', 'Description': 'Eligible expression of the promotion.', 'Required': True}, {'Name': 'ValueExpression', 'Type': 'string', 'Description': 'Value expression of the promotion.', 'Required': True}, {'Name': 'CanCombine', 'Type': 'boolean', 'Description': 'Can combine of the promotion.', 'Required': False}, {'Name': 'xp', 'Type': 'object', 'Description': 'Container for extended (custom) properties of the promotion.', 'Required': False}]}
## Create a new promotion
### `POST` `v1/promotions`

| Parameters      | Description                    |
|------------------|---------------------------------|

 **Requestbody**: 
{'Sample': '{\r\n  "ID": "",\r\n  "Code": "",\r\n  "Name": "",\r\n  "RedemptionLimit": 0,\r\n  "RedemptionLimitPerUser": 0,\r\n  "Description": "",\r\n  "FinePrint": "",\r\n  "StartDate": "2018-03-21T23:00:00+00:00",\r\n  "ExpirationDate": "2018-03-21T23:00:00+00:00",\r\n  "EligibleExpression": "",\r\n  "ValueExpression": "",\r\n  "CanCombine": false,\r\n  "xp": {}\r\n}', 'Fields': [{'Name': 'ID', 'Type': 'string', 'Description': 'ID of the promotion. Can only contain characters Aa-Zz, 0-9, -, and _. Searchable: priority level 1. Sortable: priority level 2.', 'Required': False}, {'Name': 'Code', 'Type': 'string', 'Description': 'Must be unique. Entered by buyer when adding promo to order.', 'Required': True}, {'Name': 'Name', 'Type': 'string', 'Description': 'Name of the promotion. Max length 100 characters. Searchable: priority level 2. Sortable: priority level 1.', 'Required': False}, {'Name': 'RedemptionLimit', 'Type': 'integer', 'Description': 'Redemption limit of the promotion.', 'Required': False}, {'Name': 'RedemptionLimitPerUser', 'Type': 'integer', 'Description': 'Redemption limit per user of the promotion.', 'Required': False}, {'Name': 'Description', 'Type': 'string', 'Description': 'Description of the promotion. Max length 2000 characters. Searchable: priority level 4.', 'Required': False}, {'Name': 'FinePrint', 'Type': 'string', 'Description': 'Terms, conditions, and other legal jargon.', 'Required': False}, {'Name': 'StartDate', 'Type': 'date', 'Description': 'Start date of the promotion. Sortable.', 'Required': False}, {'Name': 'ExpirationDate', 'Type': 'date', 'Description': 'Expiration date of the promotion. Sortable.', 'Required': False}, {'Name': 'EligibleExpression', 'Type': 'string', 'Description': 'Eligible expression of the promotion. Required. Max length 400 characters. Searchable: priority level 6. Sortable.', 'Required': True}, {'Name': 'ValueExpression', 'Type': 'string', 'Description': 'Value expression of the promotion. Required. Max length 400 characters. Searchable: priority level 7. Sortable.', 'Required': True}, {'Name': 'CanCombine', 'Type': 'boolean', 'Description': 'Can combine of the promotion. Sortable.', 'Required': False}, {'Name': 'xp', 'Type': 'object', 'Description': 'Container for extended (custom) properties of the promotion.', 'Required': False}]}
 **Responsestatus**: `201`

 **Responsebody**: 
{'Sample': '{\r\n  "ID": "",\r\n  "Code": "",\r\n  "Name": "",\r\n  "RedemptionLimit": 0,\r\n  "RedemptionLimitPerUser": 0,\r\n  "RedemptionCount": 0,\r\n  "Description": "",\r\n  "FinePrint": "",\r\n  "StartDate": "2018-03-21T23:00:00+00:00",\r\n  "ExpirationDate": "2018-03-21T23:00:00+00:00",\r\n  "EligibleExpression": "",\r\n  "ValueExpression": "",\r\n  "CanCombine": false,\r\n  "xp": {}\r\n}', 'Fields': [{'Name': 'ID', 'Type': 'string', 'Description': 'ID of the promotion.', 'Required': False}, {'Name': 'Code', 'Type': 'string', 'Description': 'Must be unique. Entered by buyer when adding promo to order.', 'Required': True}, {'Name': 'Name', 'Type': 'string', 'Description': 'Name of the promotion.', 'Required': False}, {'Name': 'RedemptionLimit', 'Type': 'integer', 'Description': 'Redemption limit of the promotion.', 'Required': False}, {'Name': 'RedemptionLimitPerUser', 'Type': 'integer', 'Description': 'Redemption limit per user of the promotion.', 'Required': False}, {'Name': 'RedemptionCount', 'Type': 'integer', 'Description': 'Redemption count of the promotion.', 'Required': False}, {'Name': 'Description', 'Type': 'string', 'Description': 'Description of the promotion.', 'Required': False}, {'Name': 'FinePrint', 'Type': 'string', 'Description': 'Terms, conditions, and other legal jargon.', 'Required': False}, {'Name': 'StartDate', 'Type': 'date', 'Description': 'Start date of the promotion.', 'Required': False}, {'Name': 'ExpirationDate', 'Type': 'date', 'Description': 'Expiration date of the promotion.', 'Required': False}, {'Name': 'EligibleExpression', 'Type': 'string', 'Description': 'Eligible expression of the promotion.', 'Required': True}, {'Name': 'ValueExpression', 'Type': 'string', 'Description': 'Value expression of the promotion.', 'Required': True}, {'Name': 'CanCombine', 'Type': 'boolean', 'Description': 'Can combine of the promotion.', 'Required': False}, {'Name': 'xp', 'Type': 'object', 'Description': 'Container for extended (custom) properties of the promotion.', 'Required': False}]}
## Create or update a promotion
### `PUT` `v1/promotions/{promotionID}`

| Parameters      | Description                    |
|------------------|---------------------------------|
| Name            | promotionID                    |
| Type            | string                         |
| Description     | ID of the promotion.           |
| Required        | True                           |

 **Requestbody**: 
{'Sample': '{\r\n  "ID": "",\r\n  "Code": "",\r\n  "Name": "",\r\n  "RedemptionLimit": 0,\r\n  "RedemptionLimitPerUser": 0,\r\n  "Description": "",\r\n  "FinePrint": "",\r\n  "StartDate": "2018-03-21T23:00:00+00:00",\r\n  "ExpirationDate": "2018-03-21T23:00:00+00:00",\r\n  "EligibleExpression": "",\r\n  "ValueExpression": "",\r\n  "CanCombine": false,\r\n  "xp": {}\r\n}', 'Fields': [{'Name': 'ID', 'Type': 'string', 'Description': 'ID of the promotion. Can only contain characters Aa-Zz, 0-9, -, and _. Searchable: priority level 1. Sortable: priority level 2.', 'Required': False}, {'Name': 'Code', 'Type': 'string', 'Description': 'Must be unique. Entered by buyer when adding promo to order.', 'Required': True}, {'Name': 'Name', 'Type': 'string', 'Description': 'Name of the promotion. Max length 100 characters. Searchable: priority level 2. Sortable: priority level 1.', 'Required': False}, {'Name': 'RedemptionLimit', 'Type': 'integer', 'Description': 'Redemption limit of the promotion.', 'Required': False}, {'Name': 'RedemptionLimitPerUser', 'Type': 'integer', 'Description': 'Redemption limit per user of the promotion.', 'Required': False}, {'Name': 'Description', 'Type': 'string', 'Description': 'Description of the promotion. Max length 2000 characters. Searchable: priority level 4.', 'Required': False}, {'Name': 'FinePrint', 'Type': 'string', 'Description': 'Terms, conditions, and other legal jargon.', 'Required': False}, {'Name': 'StartDate', 'Type': 'date', 'Description': 'Start date of the promotion. Sortable.', 'Required': False}, {'Name': 'ExpirationDate', 'Type': 'date', 'Description': 'Expiration date of the promotion. Sortable.', 'Required': False}, {'Name': 'EligibleExpression', 'Type': 'string', 'Description': 'Eligible expression of the promotion. Required. Max length 400 characters. Searchable: priority level 6. Sortable.', 'Required': True}, {'Name': 'ValueExpression', 'Type': 'string', 'Description': 'Value expression of the promotion. Required. Max length 400 characters. Searchable: priority level 7. Sortable.', 'Required': True}, {'Name': 'CanCombine', 'Type': 'boolean', 'Description': 'Can combine of the promotion. Sortable.', 'Required': False}, {'Name': 'xp', 'Type': 'object', 'Description': 'Container for extended (custom) properties of the promotion.', 'Required': False}]}
 **Responsestatus**: `200`

 **Responsebody**: 
{'Sample': '{\r\n  "ID": "",\r\n  "Code": "",\r\n  "Name": "",\r\n  "RedemptionLimit": 0,\r\n  "RedemptionLimitPerUser": 0,\r\n  "RedemptionCount": 0,\r\n  "Description": "",\r\n  "FinePrint": "",\r\n  "StartDate": "2018-03-21T23:00:00+00:00",\r\n  "ExpirationDate": "2018-03-21T23:00:00+00:00",\r\n  "EligibleExpression": "",\r\n  "ValueExpression": "",\r\n  "CanCombine": false,\r\n  "xp": {}\r\n}', 'Fields': [{'Name': 'ID', 'Type': 'string', 'Description': 'ID of the promotion.', 'Required': False}, {'Name': 'Code', 'Type': 'string', 'Description': 'Must be unique. Entered by buyer when adding promo to order.', 'Required': True}, {'Name': 'Name', 'Type': 'string', 'Description': 'Name of the promotion.', 'Required': False}, {'Name': 'RedemptionLimit', 'Type': 'integer', 'Description': 'Redemption limit of the promotion.', 'Required': False}, {'Name': 'RedemptionLimitPerUser', 'Type': 'integer', 'Description': 'Redemption limit per user of the promotion.', 'Required': False}, {'Name': 'RedemptionCount', 'Type': 'integer', 'Description': 'Redemption count of the promotion.', 'Required': False}, {'Name': 'Description', 'Type': 'string', 'Description': 'Description of the promotion.', 'Required': False}, {'Name': 'FinePrint', 'Type': 'string', 'Description': 'Terms, conditions, and other legal jargon.', 'Required': False}, {'Name': 'StartDate', 'Type': 'date', 'Description': 'Start date of the promotion.', 'Required': False}, {'Name': 'ExpirationDate', 'Type': 'date', 'Description': 'Expiration date of the promotion.', 'Required': False}, {'Name': 'EligibleExpression', 'Type': 'string', 'Description': 'Eligible expression of the promotion.', 'Required': True}, {'Name': 'ValueExpression', 'Type': 'string', 'Description': 'Value expression of the promotion.', 'Required': True}, {'Name': 'CanCombine', 'Type': 'boolean', 'Description': 'Can combine of the promotion.', 'Required': False}, {'Name': 'xp', 'Type': 'object', 'Description': 'Container for extended (custom) properties of the promotion.', 'Required': False}]}
## Delete a promotion
### `DELETE` `v1/promotions/{promotionID}`

| Parameters      | Description                    |
|------------------|---------------------------------|
| Name            | promotionID                    |
| Type            | string                         |
| Description     | ID of the promotion.           |
| Required        | True                           |

 **Requestbody**: 
None
 **Responsestatus**: `204`

 **Responsebody**: 
None
## Partially update a promotion
### `PATCH` `v1/promotions/{promotionID}`

| Parameters      | Description                    |
|------------------|---------------------------------|
| Name            | promotionID                    |
| Type            | string                         |
| Description     | ID of the promotion.           |
| Required        | True                           |

 **Requestbody**: 
{'Sample': '{\r\n  "ID": "",\r\n  "Code": "",\r\n  "Name": "",\r\n  "RedemptionLimit": 0,\r\n  "RedemptionLimitPerUser": 0,\r\n  "Description": "",\r\n  "FinePrint": "",\r\n  "StartDate": "2018-03-21T23:00:00+00:00",\r\n  "ExpirationDate": "2018-03-21T23:00:00+00:00",\r\n  "EligibleExpression": "",\r\n  "ValueExpression": "",\r\n  "CanCombine": false,\r\n  "xp": {}\r\n}', 'Fields': [{'Name': 'ID', 'Type': 'string', 'Description': 'ID of the promotion. Can only contain characters Aa-Zz, 0-9, -, and _. Searchable: priority level 1. Sortable: priority level 2.', 'Required': False}, {'Name': 'Code', 'Type': 'string', 'Description': 'Must be unique. Entered by buyer when adding promo to order.', 'Required': True}, {'Name': 'Name', 'Type': 'string', 'Description': 'Name of the promotion. Max length 100 characters. Searchable: priority level 2. Sortable: priority level 1.', 'Required': False}, {'Name': 'RedemptionLimit', 'Type': 'integer', 'Description': 'Redemption limit of the promotion.', 'Required': False}, {'Name': 'RedemptionLimitPerUser', 'Type': 'integer', 'Description': 'Redemption limit per user of the promotion.', 'Required': False}, {'Name': 'Description', 'Type': 'string', 'Description': 'Description of the promotion. Max length 2000 characters. Searchable: priority level 4.', 'Required': False}, {'Name': 'FinePrint', 'Type': 'string', 'Description': 'Terms, conditions, and other legal jargon.', 'Required': False}, {'Name': 'StartDate', 'Type': 'date', 'Description': 'Start date of the promotion. Sortable.', 'Required': False}, {'Name': 'ExpirationDate', 'Type': 'date', 'Description': 'Expiration date of the promotion. Sortable.', 'Required': False}, {'Name': 'EligibleExpression', 'Type': 'string', 'Description': 'Eligible expression of the promotion. Required. Max length 400 characters. Searchable: priority level 6. Sortable.', 'Required': True}, {'Name': 'ValueExpression', 'Type': 'string', 'Description': 'Value expression of the promotion. Required. Max length 400 characters. Searchable: priority level 7. Sortable.', 'Required': True}, {'Name': 'CanCombine', 'Type': 'boolean', 'Description': 'Can combine of the promotion. Sortable.', 'Required': False}, {'Name': 'xp', 'Type': 'object', 'Description': 'Container for extended (custom) properties of the promotion.', 'Required': False}]}
 **Responsestatus**: `200`

 **Responsebody**: 
{'Sample': '{\r\n  "ID": "",\r\n  "Code": "",\r\n  "Name": "",\r\n  "RedemptionLimit": 0,\r\n  "RedemptionLimitPerUser": 0,\r\n  "RedemptionCount": 0,\r\n  "Description": "",\r\n  "FinePrint": "",\r\n  "StartDate": "2018-03-21T23:00:00+00:00",\r\n  "ExpirationDate": "2018-03-21T23:00:00+00:00",\r\n  "EligibleExpression": "",\r\n  "ValueExpression": "",\r\n  "CanCombine": false,\r\n  "xp": {}\r\n}', 'Fields': [{'Name': 'ID', 'Type': 'string', 'Description': 'ID of the promotion.', 'Required': False}, {'Name': 'Code', 'Type': 'string', 'Description': 'Must be unique. Entered by buyer when adding promo to order.', 'Required': True}, {'Name': 'Name', 'Type': 'string', 'Description': 'Name of the promotion.', 'Required': False}, {'Name': 'RedemptionLimit', 'Type': 'integer', 'Description': 'Redemption limit of the promotion.', 'Required': False}, {'Name': 'RedemptionLimitPerUser', 'Type': 'integer', 'Description': 'Redemption limit per user of the promotion.', 'Required': False}, {'Name': 'RedemptionCount', 'Type': 'integer', 'Description': 'Redemption count of the promotion.', 'Required': False}, {'Name': 'Description', 'Type': 'string', 'Description': 'Description of the promotion.', 'Required': False}, {'Name': 'FinePrint', 'Type': 'string', 'Description': 'Terms, conditions, and other legal jargon.', 'Required': False}, {'Name': 'StartDate', 'Type': 'date', 'Description': 'Start date of the promotion.', 'Required': False}, {'Name': 'ExpirationDate', 'Type': 'date', 'Description': 'Expiration date of the promotion.', 'Required': False}, {'Name': 'EligibleExpression', 'Type': 'string', 'Description': 'Eligible expression of the promotion.', 'Required': True}, {'Name': 'ValueExpression', 'Type': 'string', 'Description': 'Value expression of the promotion.', 'Required': True}, {'Name': 'CanCombine', 'Type': 'boolean', 'Description': 'Can combine of the promotion.', 'Required': False}, {'Name': 'xp', 'Type': 'object', 'Description': 'Container for extended (custom) properties of the promotion.', 'Required': False}]}
## Get a list of promotion assignments
### `GET` `v1/promotions/assignments`

| Parameters      | Description                    |
|------------------|---------------------------------|
| Name            | buyerID                        |
| Type            | string                         |
| Description     | ID of the buyer.               |
| Required        | False                          |
| Name            | promotionID                    |
| Type            | string                         |
| Description     | ID of the promotion.           |
| Required        | False                          |
| Name            | userID                         |
| Type            | string                         |
| Description     | ID of the user.                |
| Required        | False                          |
| Name            | userGroupID                    |
| Type            | string                         |
| Description     | ID of the user group.          |
| Required        | False                          |
| Name            | level                          |
| Type            | string                         |
| Description     | Level of the promotion assignment. Possible values: User, Group, Company. |
| Required        | False                          |
| Name            | page                           |
| Type            | integer                        |
| Description     | Page of results to return. Default: 1 |
| Required        | False                          |
| Name            | pageSize                       |
| Type            | integer                        |
| Description     | Number of results to return per page. Default: 20, max: 100. |
| Required        | False                          |

 **Requestbody**: 
None
 **Responsestatus**: `200`

 **Responsebody**: 
{'Sample': '{\r\n  "Meta": {\r\n    "Page": 1,\r\n    "PageSize": 20,\r\n    "TotalCount": 25,\r\n    "TotalPages": 2,\r\n    "ItemRange": [\r\n      1,\r\n      20\r\n    ]\r\n  },\r\n  "Items": [\r\n    {\r\n      "PromotionID": "",\r\n      "BuyerID": "",\r\n      "UserGroupID": ""\r\n    }\r\n  ]\r\n}', 'Fields': [{'Name': 'PromotionID', 'Type': 'string', 'Description': 'ID of the promotion.', 'Required': True}, {'Name': 'BuyerID', 'Type': 'string', 'Description': 'ID of the buyer.', 'Required': True}, {'Name': 'UserGroupID', 'Type': 'string', 'Description': 'ID of the user group.', 'Required': False}]}
## Save a promotion assignment
### `POST` `v1/promotions/assignments`

| Parameters      | Description                    |
|------------------|---------------------------------|

 **Requestbody**: 
{'Sample': '{\r\n  "PromotionID": "",\r\n  "BuyerID": "",\r\n  "UserGroupID": ""\r\n}', 'Fields': [{'Name': 'PromotionID', 'Type': 'string', 'Description': 'ID of the promotion. Required. Sortable: priority level 1.', 'Required': True}, {'Name': 'BuyerID', 'Type': 'string', 'Description': 'ID of the buyer. Required. Sortable: priority level 2.', 'Required': True}, {'Name': 'UserGroupID', 'Type': 'string', 'Description': 'ID of the user group. Sortable: priority level 4.', 'Required': False}]}
 **Responsestatus**: `204`

 **Responsebody**: 
None
## Delete a promotion assignment
### `DELETE` `v1/promotions/{promotionID}/assignments`

| Parameters      | Description                    |
|------------------|---------------------------------|
| Name            | promotionID                    |
| Type            | string                         |
| Description     | ID of the promotion.           |
| Required        | True                           |
| Name            | buyerID                        |
| Type            | string                         |
| Description     | ID of the buyer.               |
| Required        | True                           |
| Name            | userID                         |
| Type            | string                         |
| Description     | ID of the user.                |
| Required        | False                          |
| Name            | userGroupID                    |
| Type            | string                         |
| Description     | ID of the user group.          |
| Required        | False                          |

 **Requestbody**: 
None
 **Responsestatus**: `204`

 **Responsebody**: 
None