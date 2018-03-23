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

## `GET` `v1/buyers/{buyerID}/approvalrules/{approvalRuleID}`
Get a single approval rule

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
| Name            | approvalRuleID                 |
| Type            | string                         |
| Description     | ID of the approval rule.       |
| Required        | True                           |

## Requestbody
**Responsestatus**: `200`

## Responsebody
```
{'ID': '', 'Name': '', 'Description': '', 'ApprovingGroupID': '', 'RuleExpression': '', 'xp': {}}
```


| Parameters      | Description                    |
|------------------|---------------------------------|
| Name            | ID                             |
| Type            | string                         |
| Description     | ID of the approval rule.       |
| Required        | False                          |


| Parameters      | Description                    |
|------------------|---------------------------------|
| Name            | Name                           |
| Type            | string                         |
| Description     | Name of the approval rule.     |
| Required        | False                          |


| Parameters      | Description                    |
|------------------|---------------------------------|
| Name            | Description                    |
| Type            | string                         |
| Description     | Description of the approval rule. |
| Required        | False                          |


| Parameters      | Description                    |
|------------------|---------------------------------|
| Name            | ApprovingGroupID               |
| Type            | string                         |
| Description     | ID of the approving group.     |
| Required        | True                           |


| Parameters      | Description                    |
|------------------|---------------------------------|
| Name            | RuleExpression                 |
| Type            | string                         |
| Description     | Rule expression of the approval rule. |
| Required        | True                           |


| Parameters      | Description                    |
|------------------|---------------------------------|
| Name            | xp                             |
| Type            | object                         |
| Description     | Container for extended (custom) properties of the approval rule. |
| Required        | False                          |

## `GET` `v1/buyers/{buyerID}/approvalrules`
Get a list of approval rules

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

## Requestbody
**Responsestatus**: `200`

## Responsebody
```
{'Meta': {'Page': 1, 'PageSize': 20, 'TotalCount': 25, 'TotalPages': 2, 'ItemRange': [1, 20]}, 'Items': [{'ID': '', 'Name': '', 'Description': '', 'ApprovingGroupID': '', 'RuleExpression': '', 'xp': {}}]}
```


| Parameters      | Description                    |
|------------------|---------------------------------|
| Name            | ID                             |
| Type            | string                         |
| Description     | ID of the approval rule.       |
| Required        | False                          |


| Parameters      | Description                    |
|------------------|---------------------------------|
| Name            | Name                           |
| Type            | string                         |
| Description     | Name of the approval rule.     |
| Required        | False                          |


| Parameters      | Description                    |
|------------------|---------------------------------|
| Name            | Description                    |
| Type            | string                         |
| Description     | Description of the approval rule. |
| Required        | False                          |


| Parameters      | Description                    |
|------------------|---------------------------------|
| Name            | ApprovingGroupID               |
| Type            | string                         |
| Description     | ID of the approving group.     |
| Required        | True                           |


| Parameters      | Description                    |
|------------------|---------------------------------|
| Name            | RuleExpression                 |
| Type            | string                         |
| Description     | Rule expression of the approval rule. |
| Required        | True                           |


| Parameters      | Description                    |
|------------------|---------------------------------|
| Name            | xp                             |
| Type            | object                         |
| Description     | Container for extended (custom) properties of the approval rule. |
| Required        | False                          |

## `POST` `v1/buyers/{buyerID}/approvalrules`
Create a new approval rule

| Parameters      | Description                    |
|------------------|---------------------------------|


| Parameters      | Description                    |
|------------------|---------------------------------|
| Name            | buyerID                        |
| Type            | string                         |
| Description     | ID of the buyer.               |
| Required        | True                           |

## Requestbody
```
{'ID': '', 'Name': '', 'Description': '', 'ApprovingGroupID': '', 'RuleExpression': '', 'xp': {}}
```

```
[{'Name': 'ID', 'Type': 'string', 'Description': 'ID of the approval rule. Can only contain characters Aa-Zz, 0-9, -, and _. Searchable: priority level 1. Sortable: priority level 2.', 'Required': False}, {'Name': 'Name', 'Type': 'string', 'Description': 'Name of the approval rule. Max length 100 characters. Searchable: priority level 2. Sortable: priority level 1.', 'Required': False}, {'Name': 'Description', 'Type': 'string', 'Description': 'Description of the approval rule. Max length 2000 characters. Searchable: priority level 3.', 'Required': False}, {'Name': 'ApprovingGroupID', 'Type': 'string', 'Description': 'ID of the approving group. Required. Sortable.', 'Required': True}, {'Name': 'RuleExpression', 'Type': 'string', 'Description': 'Rule expression of the approval rule. Required. Max length 400 characters. Searchable: priority level 4. Sortable.', 'Required': True}, {'Name': 'xp', 'Type': 'object', 'Description': 'Container for extended (custom) properties of the approval rule.', 'Required': False}]
```

**Responsestatus**: `201`

## Responsebody
```
{'ID': '', 'Name': '', 'Description': '', 'ApprovingGroupID': '', 'RuleExpression': '', 'xp': {}}
```


| Parameters      | Description                    |
|------------------|---------------------------------|
| Name            | ID                             |
| Type            | string                         |
| Description     | ID of the approval rule.       |
| Required        | False                          |


| Parameters      | Description                    |
|------------------|---------------------------------|
| Name            | Name                           |
| Type            | string                         |
| Description     | Name of the approval rule.     |
| Required        | False                          |


| Parameters      | Description                    |
|------------------|---------------------------------|
| Name            | Description                    |
| Type            | string                         |
| Description     | Description of the approval rule. |
| Required        | False                          |


| Parameters      | Description                    |
|------------------|---------------------------------|
| Name            | ApprovingGroupID               |
| Type            | string                         |
| Description     | ID of the approving group.     |
| Required        | True                           |


| Parameters      | Description                    |
|------------------|---------------------------------|
| Name            | RuleExpression                 |
| Type            | string                         |
| Description     | Rule expression of the approval rule. |
| Required        | True                           |


| Parameters      | Description                    |
|------------------|---------------------------------|
| Name            | xp                             |
| Type            | object                         |
| Description     | Container for extended (custom) properties of the approval rule. |
| Required        | False                          |

## `PUT` `v1/buyers/{buyerID}/approvalrules/{approvalRuleID}`
Create or update an approval rule

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
| Name            | approvalRuleID                 |
| Type            | string                         |
| Description     | ID of the approval rule.       |
| Required        | True                           |

## Requestbody
```
{'ID': '', 'Name': '', 'Description': '', 'ApprovingGroupID': '', 'RuleExpression': '', 'xp': {}}
```

```
[{'Name': 'ID', 'Type': 'string', 'Description': 'ID of the approval rule. Can only contain characters Aa-Zz, 0-9, -, and _. Searchable: priority level 1. Sortable: priority level 2.', 'Required': False}, {'Name': 'Name', 'Type': 'string', 'Description': 'Name of the approval rule. Max length 100 characters. Searchable: priority level 2. Sortable: priority level 1.', 'Required': False}, {'Name': 'Description', 'Type': 'string', 'Description': 'Description of the approval rule. Max length 2000 characters. Searchable: priority level 3.', 'Required': False}, {'Name': 'ApprovingGroupID', 'Type': 'string', 'Description': 'ID of the approving group. Required. Sortable.', 'Required': True}, {'Name': 'RuleExpression', 'Type': 'string', 'Description': 'Rule expression of the approval rule. Required. Max length 400 characters. Searchable: priority level 4. Sortable.', 'Required': True}, {'Name': 'xp', 'Type': 'object', 'Description': 'Container for extended (custom) properties of the approval rule.', 'Required': False}]
```

**Responsestatus**: `200`

## Responsebody
```
{'ID': '', 'Name': '', 'Description': '', 'ApprovingGroupID': '', 'RuleExpression': '', 'xp': {}}
```


| Parameters      | Description                    |
|------------------|---------------------------------|
| Name            | ID                             |
| Type            | string                         |
| Description     | ID of the approval rule.       |
| Required        | False                          |


| Parameters      | Description                    |
|------------------|---------------------------------|
| Name            | Name                           |
| Type            | string                         |
| Description     | Name of the approval rule.     |
| Required        | False                          |


| Parameters      | Description                    |
|------------------|---------------------------------|
| Name            | Description                    |
| Type            | string                         |
| Description     | Description of the approval rule. |
| Required        | False                          |


| Parameters      | Description                    |
|------------------|---------------------------------|
| Name            | ApprovingGroupID               |
| Type            | string                         |
| Description     | ID of the approving group.     |
| Required        | True                           |


| Parameters      | Description                    |
|------------------|---------------------------------|
| Name            | RuleExpression                 |
| Type            | string                         |
| Description     | Rule expression of the approval rule. |
| Required        | True                           |


| Parameters      | Description                    |
|------------------|---------------------------------|
| Name            | xp                             |
| Type            | object                         |
| Description     | Container for extended (custom) properties of the approval rule. |
| Required        | False                          |

## `DELETE` `v1/buyers/{buyerID}/approvalrules/{approvalRuleID}`
Delete an approval rule

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
| Name            | approvalRuleID                 |
| Type            | string                         |
| Description     | ID of the approval rule.       |
| Required        | True                           |

## Requestbody
**Responsestatus**: `204`

## Responsebody
## `PATCH` `v1/buyers/{buyerID}/approvalrules/{approvalRuleID}`
Partially update an approval rule

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
| Name            | approvalRuleID                 |
| Type            | string                         |
| Description     | ID of the approval rule.       |
| Required        | True                           |

## Requestbody
```
{'ID': '', 'Name': '', 'Description': '', 'ApprovingGroupID': '', 'RuleExpression': '', 'xp': {}}
```

```
[{'Name': 'ID', 'Type': 'string', 'Description': 'ID of the approval rule. Can only contain characters Aa-Zz, 0-9, -, and _. Searchable: priority level 1. Sortable: priority level 2.', 'Required': False}, {'Name': 'Name', 'Type': 'string', 'Description': 'Name of the approval rule. Max length 100 characters. Searchable: priority level 2. Sortable: priority level 1.', 'Required': False}, {'Name': 'Description', 'Type': 'string', 'Description': 'Description of the approval rule. Max length 2000 characters. Searchable: priority level 3.', 'Required': False}, {'Name': 'ApprovingGroupID', 'Type': 'string', 'Description': 'ID of the approving group. Required. Sortable.', 'Required': True}, {'Name': 'RuleExpression', 'Type': 'string', 'Description': 'Rule expression of the approval rule. Required. Max length 400 characters. Searchable: priority level 4. Sortable.', 'Required': True}, {'Name': 'xp', 'Type': 'object', 'Description': 'Container for extended (custom) properties of the approval rule.', 'Required': False}]
```

**Responsestatus**: `200`

## Responsebody
```
{'ID': '', 'Name': '', 'Description': '', 'ApprovingGroupID': '', 'RuleExpression': '', 'xp': {}}
```


| Parameters      | Description                    |
|------------------|---------------------------------|
| Name            | ID                             |
| Type            | string                         |
| Description     | ID of the approval rule.       |
| Required        | False                          |


| Parameters      | Description                    |
|------------------|---------------------------------|
| Name            | Name                           |
| Type            | string                         |
| Description     | Name of the approval rule.     |
| Required        | False                          |


| Parameters      | Description                    |
|------------------|---------------------------------|
| Name            | Description                    |
| Type            | string                         |
| Description     | Description of the approval rule. |
| Required        | False                          |


| Parameters      | Description                    |
|------------------|---------------------------------|
| Name            | ApprovingGroupID               |
| Type            | string                         |
| Description     | ID of the approving group.     |
| Required        | True                           |


| Parameters      | Description                    |
|------------------|---------------------------------|
| Name            | RuleExpression                 |
| Type            | string                         |
| Description     | Rule expression of the approval rule. |
| Required        | True                           |


| Parameters      | Description                    |
|------------------|---------------------------------|
| Name            | xp                             |
| Type            | object                         |
| Description     | Container for extended (custom) properties of the approval rule. |
| Required        | False                          |
