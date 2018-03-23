---
title: Approval Rules
date: 2018-03-23
category: API Reference
tags: Buyers
slug: ApprovalRules
---
Approval rules are used to verify the integrity of an order. Common
examples include orders requiring managerial approval, approval for
orders that contain a specific product category, approval for quantity
thresholds or approval for orders that exceed a specific price.
Properties are also available to control the triggers and timing for
processing approvals whether parallel to another rule, or in succession
of a previous rule.

---
## Get a single approval rule
### `GET` `v1/buyers/{buyerID}/approvalrules/{approvalRuleID}`

| Parameters      | Description                    |
|------------------|---------------------------------|
| Name            | buyerID                        |
| Type            | string                         |
| Description     | ID of the buyer.               |
| Required        | True                           |
| Name            | approvalRuleID                 |
| Type            | string                         |
| Description     | ID of the approval rule.       |
| Required        | True                           |

 **Requestbody**: 
None
 **Responsestatus**: `200`

 **Responsebody**: 
{'Sample': '{\r\n  "ID": "",\r\n  "Name": "",\r\n  "Description": "",\r\n  "ApprovingGroupID": "",\r\n  "RuleExpression": "",\r\n  "xp": {}\r\n}', 'Fields': [{'Name': 'ID', 'Type': 'string', 'Description': 'ID of the approval rule.', 'Required': False}, {'Name': 'Name', 'Type': 'string', 'Description': 'Name of the approval rule.', 'Required': False}, {'Name': 'Description', 'Type': 'string', 'Description': 'Description of the approval rule.', 'Required': False}, {'Name': 'ApprovingGroupID', 'Type': 'string', 'Description': 'ID of the approving group.', 'Required': True}, {'Name': 'RuleExpression', 'Type': 'string', 'Description': 'Rule expression of the approval rule.', 'Required': True}, {'Name': 'xp', 'Type': 'object', 'Description': 'Container for extended (custom) properties of the approval rule.', 'Required': False}]}## Get a list of approval rules
### `GET` `v1/buyers/{buyerID}/approvalrules`

| Parameters      | Description                    |
|------------------|---------------------------------|
| Name            | buyerID                        |
| Type            | string                         |
| Description     | ID of the buyer.               |
| Required        | True                           |
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
{'Sample': '{\r\n  "Meta": {\r\n    "Page": 1,\r\n    "PageSize": 20,\r\n    "TotalCount": 25,\r\n    "TotalPages": 2,\r\n    "ItemRange": [\r\n      1,\r\n      20\r\n    ]\r\n  },\r\n  "Items": [\r\n    {\r\n      "ID": "",\r\n      "Name": "",\r\n      "Description": "",\r\n      "ApprovingGroupID": "",\r\n      "RuleExpression": "",\r\n      "xp": {}\r\n    }\r\n  ]\r\n}', 'Fields': [{'Name': 'ID', 'Type': 'string', 'Description': 'ID of the approval rule.', 'Required': False}, {'Name': 'Name', 'Type': 'string', 'Description': 'Name of the approval rule.', 'Required': False}, {'Name': 'Description', 'Type': 'string', 'Description': 'Description of the approval rule.', 'Required': False}, {'Name': 'ApprovingGroupID', 'Type': 'string', 'Description': 'ID of the approving group.', 'Required': True}, {'Name': 'RuleExpression', 'Type': 'string', 'Description': 'Rule expression of the approval rule.', 'Required': True}, {'Name': 'xp', 'Type': 'object', 'Description': 'Container for extended (custom) properties of the approval rule.', 'Required': False}]}## Create a new approval rule
### `POST` `v1/buyers/{buyerID}/approvalrules`

| Parameters      | Description                    |
|------------------|---------------------------------|
| Name            | buyerID                        |
| Type            | string                         |
| Description     | ID of the buyer.               |
| Required        | True                           |

 **Requestbody**: 
{'Sample': '{\r\n  "ID": "",\r\n  "Name": "",\r\n  "Description": "",\r\n  "ApprovingGroupID": "",\r\n  "RuleExpression": "",\r\n  "xp": {}\r\n}', 'Fields': [{'Name': 'ID', 'Type': 'string', 'Description': 'ID of the approval rule. Can only contain characters Aa-Zz, 0-9, -, and _. Searchable: priority level 1. Sortable: priority level 2.', 'Required': False}, {'Name': 'Name', 'Type': 'string', 'Description': 'Name of the approval rule. Max length 100 characters. Searchable: priority level 2. Sortable: priority level 1.', 'Required': False}, {'Name': 'Description', 'Type': 'string', 'Description': 'Description of the approval rule. Max length 2000 characters. Searchable: priority level 3.', 'Required': False}, {'Name': 'ApprovingGroupID', 'Type': 'string', 'Description': 'ID of the approving group. Required. Sortable.', 'Required': True}, {'Name': 'RuleExpression', 'Type': 'string', 'Description': 'Rule expression of the approval rule. Required. Max length 400 characters. Searchable: priority level 4. Sortable.', 'Required': True}, {'Name': 'xp', 'Type': 'object', 'Description': 'Container for extended (custom) properties of the approval rule.', 'Required': False}]}
 **Responsestatus**: `201`

 **Responsebody**: 
{'Sample': '{\r\n  "ID": "",\r\n  "Name": "",\r\n  "Description": "",\r\n  "ApprovingGroupID": "",\r\n  "RuleExpression": "",\r\n  "xp": {}\r\n}', 'Fields': [{'Name': 'ID', 'Type': 'string', 'Description': 'ID of the approval rule.', 'Required': False}, {'Name': 'Name', 'Type': 'string', 'Description': 'Name of the approval rule.', 'Required': False}, {'Name': 'Description', 'Type': 'string', 'Description': 'Description of the approval rule.', 'Required': False}, {'Name': 'ApprovingGroupID', 'Type': 'string', 'Description': 'ID of the approving group.', 'Required': True}, {'Name': 'RuleExpression', 'Type': 'string', 'Description': 'Rule expression of the approval rule.', 'Required': True}, {'Name': 'xp', 'Type': 'object', 'Description': 'Container for extended (custom) properties of the approval rule.', 'Required': False}]}## Create or update an approval rule
### `PUT` `v1/buyers/{buyerID}/approvalrules/{approvalRuleID}`

| Parameters      | Description                    |
|------------------|---------------------------------|
| Name            | buyerID                        |
| Type            | string                         |
| Description     | ID of the buyer.               |
| Required        | True                           |
| Name            | approvalRuleID                 |
| Type            | string                         |
| Description     | ID of the approval rule.       |
| Required        | True                           |

 **Requestbody**: 
{'Sample': '{\r\n  "ID": "",\r\n  "Name": "",\r\n  "Description": "",\r\n  "ApprovingGroupID": "",\r\n  "RuleExpression": "",\r\n  "xp": {}\r\n}', 'Fields': [{'Name': 'ID', 'Type': 'string', 'Description': 'ID of the approval rule. Can only contain characters Aa-Zz, 0-9, -, and _. Searchable: priority level 1. Sortable: priority level 2.', 'Required': False}, {'Name': 'Name', 'Type': 'string', 'Description': 'Name of the approval rule. Max length 100 characters. Searchable: priority level 2. Sortable: priority level 1.', 'Required': False}, {'Name': 'Description', 'Type': 'string', 'Description': 'Description of the approval rule. Max length 2000 characters. Searchable: priority level 3.', 'Required': False}, {'Name': 'ApprovingGroupID', 'Type': 'string', 'Description': 'ID of the approving group. Required. Sortable.', 'Required': True}, {'Name': 'RuleExpression', 'Type': 'string', 'Description': 'Rule expression of the approval rule. Required. Max length 400 characters. Searchable: priority level 4. Sortable.', 'Required': True}, {'Name': 'xp', 'Type': 'object', 'Description': 'Container for extended (custom) properties of the approval rule.', 'Required': False}]}
 **Responsestatus**: `200`

 **Responsebody**: 
{'Sample': '{\r\n  "ID": "",\r\n  "Name": "",\r\n  "Description": "",\r\n  "ApprovingGroupID": "",\r\n  "RuleExpression": "",\r\n  "xp": {}\r\n}', 'Fields': [{'Name': 'ID', 'Type': 'string', 'Description': 'ID of the approval rule.', 'Required': False}, {'Name': 'Name', 'Type': 'string', 'Description': 'Name of the approval rule.', 'Required': False}, {'Name': 'Description', 'Type': 'string', 'Description': 'Description of the approval rule.', 'Required': False}, {'Name': 'ApprovingGroupID', 'Type': 'string', 'Description': 'ID of the approving group.', 'Required': True}, {'Name': 'RuleExpression', 'Type': 'string', 'Description': 'Rule expression of the approval rule.', 'Required': True}, {'Name': 'xp', 'Type': 'object', 'Description': 'Container for extended (custom) properties of the approval rule.', 'Required': False}]}## Delete an approval rule
### `DELETE` `v1/buyers/{buyerID}/approvalrules/{approvalRuleID}`

| Parameters      | Description                    |
|------------------|---------------------------------|
| Name            | buyerID                        |
| Type            | string                         |
| Description     | ID of the buyer.               |
| Required        | True                           |
| Name            | approvalRuleID                 |
| Type            | string                         |
| Description     | ID of the approval rule.       |
| Required        | True                           |

 **Requestbody**: 
None
 **Responsestatus**: `204`

 **Responsebody**: 
None## Partially update an approval rule
### `PATCH` `v1/buyers/{buyerID}/approvalrules/{approvalRuleID}`

| Parameters      | Description                    |
|------------------|---------------------------------|
| Name            | buyerID                        |
| Type            | string                         |
| Description     | ID of the buyer.               |
| Required        | True                           |
| Name            | approvalRuleID                 |
| Type            | string                         |
| Description     | ID of the approval rule.       |
| Required        | True                           |

 **Requestbody**: 
{'Sample': '{\r\n  "ID": "",\r\n  "Name": "",\r\n  "Description": "",\r\n  "ApprovingGroupID": "",\r\n  "RuleExpression": "",\r\n  "xp": {}\r\n}', 'Fields': [{'Name': 'ID', 'Type': 'string', 'Description': 'ID of the approval rule. Can only contain characters Aa-Zz, 0-9, -, and _. Searchable: priority level 1. Sortable: priority level 2.', 'Required': False}, {'Name': 'Name', 'Type': 'string', 'Description': 'Name of the approval rule. Max length 100 characters. Searchable: priority level 2. Sortable: priority level 1.', 'Required': False}, {'Name': 'Description', 'Type': 'string', 'Description': 'Description of the approval rule. Max length 2000 characters. Searchable: priority level 3.', 'Required': False}, {'Name': 'ApprovingGroupID', 'Type': 'string', 'Description': 'ID of the approving group. Required. Sortable.', 'Required': True}, {'Name': 'RuleExpression', 'Type': 'string', 'Description': 'Rule expression of the approval rule. Required. Max length 400 characters. Searchable: priority level 4. Sortable.', 'Required': True}, {'Name': 'xp', 'Type': 'object', 'Description': 'Container for extended (custom) properties of the approval rule.', 'Required': False}]}
 **Responsestatus**: `200`

 **Responsebody**: 
{'Sample': '{\r\n  "ID": "",\r\n  "Name": "",\r\n  "Description": "",\r\n  "ApprovingGroupID": "",\r\n  "RuleExpression": "",\r\n  "xp": {}\r\n}', 'Fields': [{'Name': 'ID', 'Type': 'string', 'Description': 'ID of the approval rule.', 'Required': False}, {'Name': 'Name', 'Type': 'string', 'Description': 'Name of the approval rule.', 'Required': False}, {'Name': 'Description', 'Type': 'string', 'Description': 'Description of the approval rule.', 'Required': False}, {'Name': 'ApprovingGroupID', 'Type': 'string', 'Description': 'ID of the approving group.', 'Required': True}, {'Name': 'RuleExpression', 'Type': 'string', 'Description': 'Rule expression of the approval rule.', 'Required': True}, {'Name': 'xp', 'Type': 'object', 'Description': 'Container for extended (custom) properties of the approval rule.', 'Required': False}]}