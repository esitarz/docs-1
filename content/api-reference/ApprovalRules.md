---
title: Approval Rules
date: 2018-03-27
category: API Reference
tags: Buyers
slug: Buyers-ApprovalRules
---
Approval rules are used to verify the integrity of an order. Common
examples include orders requiring managerial approval, approval for
orders that contain a specific product category, approval for quantity
thresholds or approval for orders that exceed a specific price.
Properties are also available to control the triggers and timing for
processing approvals whether parallel to another rule, or in succession
of a previous rule.

---

## `GET` `v1/buyers/{buyerID}/approvalrules/{approvalRuleID}`
Get a single approval rule

| Name | Type | Description | Required | 
|---|---|---|---|
| buyerID | string | ID of the buyer. | True |
| approvalRuleID | string | ID of the approval rule. | True |

## Response Body
	:::json
	{
	    "ApprovingGroupID": "",
	    "Description": "",
	    "ID": "",
	    "Name": "",
	    "RuleExpression": "",
	    "xp": {}
	}


| Name | Type | Description | Required | 
|---|---|---|---|
| ID | string | ID of the approval rule. | False |
| Name | string | Name of the approval rule. | False |
| Description | string | Description of the approval rule. | False |
| ApprovingGroupID | string | ID of the approving group. | True |
| RuleExpression | string | Rule expression of the approval rule. | True |
| xp | object | Container for extended (custom) properties of the approval rule. | False |

## `GET` `v1/buyers/{buyerID}/approvalrules`
Get a list of approval rules

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
	            "ApprovingGroupID": "",
	            "Description": "",
	            "ID": "",
	            "Name": "",
	            "RuleExpression": "",
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
| ID | string | ID of the approval rule. | False |
| Name | string | Name of the approval rule. | False |
| Description | string | Description of the approval rule. | False |
| ApprovingGroupID | string | ID of the approving group. | True |
| RuleExpression | string | Rule expression of the approval rule. | True |
| xp | object | Container for extended (custom) properties of the approval rule. | False |

## `POST` `v1/buyers/{buyerID}/approvalrules`
Create a new approval rule

| Name | Type | Description | Required | 
|---|---|---|---|
| buyerID | string | ID of the buyer. | True |

## Request Body
	:::json
	{
	    "ApprovingGroupID": "",
	    "Description": "",
	    "ID": "",
	    "Name": "",
	    "RuleExpression": "",
	    "xp": {}
	}


| Name | Type | Description | Required | 
|---|---|---|---|
| ID | string | ID of the approval rule. Can only contain characters Aa-Zz, 0-9, -, and _. Searchable: priority level 1. Sortable: priority level 2. | False |
| Name | string | Name of the approval rule. Max length 100 characters. Searchable: priority level 2. Sortable: priority level 1. | False |
| Description | string | Description of the approval rule. Max length 2000 characters. Searchable: priority level 3. | False |
| ApprovingGroupID | string | ID of the approving group. Required. Sortable. | True |
| RuleExpression | string | Rule expression of the approval rule. Required. Max length 400 characters. Searchable: priority level 4. Sortable. | True |
| xp | object | Container for extended (custom) properties of the approval rule. | False |

## Response Body
	:::json
	{
	    "ApprovingGroupID": "",
	    "Description": "",
	    "ID": "",
	    "Name": "",
	    "RuleExpression": "",
	    "xp": {}
	}


| Name | Type | Description | Required | 
|---|---|---|---|
| ID | string | ID of the approval rule. | False |
| Name | string | Name of the approval rule. | False |
| Description | string | Description of the approval rule. | False |
| ApprovingGroupID | string | ID of the approving group. | True |
| RuleExpression | string | Rule expression of the approval rule. | True |
| xp | object | Container for extended (custom) properties of the approval rule. | False |

## `PUT` `v1/buyers/{buyerID}/approvalrules/{approvalRuleID}`
Create or update an approval rule

| Name | Type | Description | Required | 
|---|---|---|---|
| buyerID | string | ID of the buyer. | True |
| approvalRuleID | string | ID of the approval rule. | True |

## Request Body
	:::json
	{
	    "ApprovingGroupID": "",
	    "Description": "",
	    "ID": "",
	    "Name": "",
	    "RuleExpression": "",
	    "xp": {}
	}


| Name | Type | Description | Required | 
|---|---|---|---|
| ID | string | ID of the approval rule. Can only contain characters Aa-Zz, 0-9, -, and _. Searchable: priority level 1. Sortable: priority level 2. | False |
| Name | string | Name of the approval rule. Max length 100 characters. Searchable: priority level 2. Sortable: priority level 1. | False |
| Description | string | Description of the approval rule. Max length 2000 characters. Searchable: priority level 3. | False |
| ApprovingGroupID | string | ID of the approving group. Required. Sortable. | True |
| RuleExpression | string | Rule expression of the approval rule. Required. Max length 400 characters. Searchable: priority level 4. Sortable. | True |
| xp | object | Container for extended (custom) properties of the approval rule. | False |

## Response Body
	:::json
	{
	    "ApprovingGroupID": "",
	    "Description": "",
	    "ID": "",
	    "Name": "",
	    "RuleExpression": "",
	    "xp": {}
	}


| Name | Type | Description | Required | 
|---|---|---|---|
| ID | string | ID of the approval rule. | False |
| Name | string | Name of the approval rule. | False |
| Description | string | Description of the approval rule. | False |
| ApprovingGroupID | string | ID of the approving group. | True |
| RuleExpression | string | Rule expression of the approval rule. | True |
| xp | object | Container for extended (custom) properties of the approval rule. | False |

## `DELETE` `v1/buyers/{buyerID}/approvalrules/{approvalRuleID}`
Delete an approval rule

| Name | Type | Description | Required | 
|---|---|---|---|
| buyerID | string | ID of the buyer. | True |
| approvalRuleID | string | ID of the approval rule. | True |

## Response Body
## `PATCH` `v1/buyers/{buyerID}/approvalrules/{approvalRuleID}`
Partially update an approval rule

| Name | Type | Description | Required | 
|---|---|---|---|
| buyerID | string | ID of the buyer. | True |
| approvalRuleID | string | ID of the approval rule. | True |

## Request Body
	:::json
	{
	    "ApprovingGroupID": "",
	    "Description": "",
	    "ID": "",
	    "Name": "",
	    "RuleExpression": "",
	    "xp": {}
	}


| Name | Type | Description | Required | 
|---|---|---|---|
| ID | string | ID of the approval rule. Can only contain characters Aa-Zz, 0-9, -, and _. Searchable: priority level 1. Sortable: priority level 2. | False |
| Name | string | Name of the approval rule. Max length 100 characters. Searchable: priority level 2. Sortable: priority level 1. | False |
| Description | string | Description of the approval rule. Max length 2000 characters. Searchable: priority level 3. | False |
| ApprovingGroupID | string | ID of the approving group. Required. Sortable. | True |
| RuleExpression | string | Rule expression of the approval rule. Required. Max length 400 characters. Searchable: priority level 4. Sortable. | True |
| xp | object | Container for extended (custom) properties of the approval rule. | False |

## Response Body
	:::json
	{
	    "ApprovingGroupID": "",
	    "Description": "",
	    "ID": "",
	    "Name": "",
	    "RuleExpression": "",
	    "xp": {}
	}


| Name | Type | Description | Required | 
|---|---|---|---|
| ID | string | ID of the approval rule. | False |
| Name | string | Name of the approval rule. | False |
| Description | string | Description of the approval rule. | False |
| ApprovingGroupID | string | ID of the approving group. | True |
| RuleExpression | string | Rule expression of the approval rule. | True |
| xp | object | Container for extended (custom) properties of the approval rule. | False |
