---
title: Message Senders
date: 2018-03-23
category: API Reference
tags: Seller
slug: MessageSenders
---


## `GET` `v1/messagesenders/{messageSenderID}`
Get a single message sender

| Parameters      | Description                    |
|------------------|---------------------------------|


| Parameters      | Description                    |
|------------------|---------------------------------|
| Name            | messageSenderID                |
| Type            | string                         |
| Description     | ID of the message sender.      |
| Required        | True                           |

## Requestbody
**Responsestatus**: `200`

## Responsebody
```
{'ID': '', 'Name': '', 'MessageTypes': ['OrderDeclined'], 'Description': ''}
```


| Parameters      | Description                    |
|------------------|---------------------------------|
| Name            | ID                             |
| Type            | string                         |
| Description     | ID of the message sender.      |
| Required        | False                          |


| Parameters      | Description                    |
|------------------|---------------------------------|
| Name            | Name                           |
| Type            | string                         |
| Description     | Name of the message sender.    |
| Required        | False                          |


| Parameters      | Description                    |
|------------------|---------------------------------|
| Name            | MessageTypes                   |
| Type            | array                          |
| Description     | Message types of the message sender. |
| Required        | True                           |


| Parameters      | Description                    |
|------------------|---------------------------------|
| Name            | Description                    |
| Type            | string                         |
| Description     | Description of the message sender. |
| Required        | False                          |

## `GET` `v1/messagesenders`
Get a list of message senders

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

## Requestbody
**Responsestatus**: `200`

## Responsebody
```
{'Meta': {'Page': 1, 'PageSize': 20, 'TotalCount': 25, 'TotalPages': 2, 'ItemRange': [1, 20]}, 'Items': [{'ID': '', 'Name': '', 'MessageTypes': ['OrderDeclined'], 'Description': ''}]}
```


| Parameters      | Description                    |
|------------------|---------------------------------|
| Name            | ID                             |
| Type            | string                         |
| Description     | ID of the message sender.      |
| Required        | False                          |


| Parameters      | Description                    |
|------------------|---------------------------------|
| Name            | Name                           |
| Type            | string                         |
| Description     | Name of the message sender.    |
| Required        | False                          |


| Parameters      | Description                    |
|------------------|---------------------------------|
| Name            | MessageTypes                   |
| Type            | array                          |
| Description     | Message types of the message sender. |
| Required        | True                           |


| Parameters      | Description                    |
|------------------|---------------------------------|
| Name            | Description                    |
| Type            | string                         |
| Description     | Description of the message sender. |
| Required        | False                          |

## `GET` `v1/messagesenders/assignments`
Get a list of message sender assignments

| Parameters      | Description                    |
|------------------|---------------------------------|


| Parameters      | Description                    |
|------------------|---------------------------------|
| Name            | buyerID                        |
| Type            | string                         |
| Description     | ID of the buyer.               |
| Required        | False                          |


| Parameters      | Description                    |
|------------------|---------------------------------|
| Name            | messageSenderID                |
| Type            | string                         |
| Description     | ID of the message sender.      |
| Required        | False                          |


| Parameters      | Description                    |
|------------------|---------------------------------|
| Name            | userID                         |
| Type            | string                         |
| Description     | ID of the user.                |
| Required        | False                          |


| Parameters      | Description                    |
|------------------|---------------------------------|
| Name            | userGroupID                    |
| Type            | string                         |
| Description     | ID of the user group.          |
| Required        | False                          |


| Parameters      | Description                    |
|------------------|---------------------------------|
| Name            | level                          |
| Type            | string                         |
| Description     | Level of the message sender assignment. Possible values: User, Group, Company. |
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

## Requestbody
**Responsestatus**: `200`

## Responsebody
```
{'Meta': {'Page': 1, 'PageSize': 20, 'TotalCount': 25, 'TotalPages': 2, 'ItemRange': [1, 20]}, 'Items': [{'MessageSenderID': '', 'BuyerID': '', 'UserGroupID': '', 'MessageConfigName': '', 'MessageConfigDescription': ''}]}
```


| Parameters      | Description                    |
|------------------|---------------------------------|
| Name            | MessageSenderID                |
| Type            | string                         |
| Description     | ID of the message sender.      |
| Required        | True                           |


| Parameters      | Description                    |
|------------------|---------------------------------|
| Name            | BuyerID                        |
| Type            | string                         |
| Description     | ID of the buyer.               |
| Required        | False                          |


| Parameters      | Description                    |
|------------------|---------------------------------|
| Name            | UserGroupID                    |
| Type            | string                         |
| Description     | ID of the user group.          |
| Required        | False                          |


| Parameters      | Description                    |
|------------------|---------------------------------|
| Name            | MessageConfigName              |
| Type            | string                         |
| Description     | Message config name of the message sender assignment. |
| Required        | False                          |


| Parameters      | Description                    |
|------------------|---------------------------------|
| Name            | MessageConfigDescription       |
| Type            | string                         |
| Description     | Message config description of the message sender assignment. |
| Required        | False                          |

## `DELETE` `v1/messagesenders/{messageSenderID}/assignments`
Delete a message sender assignment

| Parameters      | Description                    |
|------------------|---------------------------------|


| Parameters      | Description                    |
|------------------|---------------------------------|
| Name            | messageSenderID                |
| Type            | string                         |
| Description     | ID of the message sender.      |
| Required        | True                           |


| Parameters      | Description                    |
|------------------|---------------------------------|
| Name            | buyerID                        |
| Type            | string                         |
| Description     | ID of the buyer.               |
| Required        | False                          |


| Parameters      | Description                    |
|------------------|---------------------------------|
| Name            | userID                         |
| Type            | string                         |
| Description     | ID of the user.                |
| Required        | False                          |


| Parameters      | Description                    |
|------------------|---------------------------------|
| Name            | userGroupID                    |
| Type            | string                         |
| Description     | ID of the user group.          |
| Required        | False                          |

## Requestbody
**Responsestatus**: `204`

## Responsebody
## `POST` `v1/messagesenders/assignments`
Save a message sender assignment
## Requestbody
```
{'MessageSenderID': '', 'BuyerID': '', 'UserGroupID': ''}
```

```
[{'Name': 'MessageSenderID', 'Type': 'string', 'Description': 'ID of the message sender. Required. Sortable: priority level 1.', 'Required': True}, {'Name': 'BuyerID', 'Type': 'string', 'Description': 'ID of the buyer. Sortable: priority level 2.', 'Required': False}, {'Name': 'UserGroupID', 'Type': 'string', 'Description': 'ID of the user group. Sortable: priority level 3.', 'Required': False}]
```

**Responsestatus**: `204`

## Responsebody
## `GET` `v1/messagesenders/CCListenerAssignments`
Get a list of message sender cc listener assignments

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

## Requestbody
**Responsestatus**: `200`

## Responsebody
```
{'Meta': {'Page': 1, 'PageSize': 20, 'TotalCount': 25, 'TotalPages': 2, 'ItemRange': [1, 20]}, 'Items': [{'MessageSenderAssignment': {'MessageSenderID': '', 'BuyerID': '', 'UserGroupID': '', 'MessageConfigName': '', 'MessageConfigDescription': ''}, 'MessageConfigName': '', 'MessageConfigDescription': '', 'MessageType': 'OrderDeclined', 'BuyerID': '', 'UserGroupID': '', 'UserID': ''}]}
```


| Parameters      | Description                    |
|------------------|---------------------------------|
| Name            | MessageSenderAssignment        |
| Type            | object                         |
| Description     | Message sender assignment of the message cc listener assignment. |
| Required        | False                          |


| Parameters      | Description                    |
|------------------|---------------------------------|
| Name            | MessageConfigName              |
| Type            | string                         |
| Description     | Message config name of the message cc listener assignment. |
| Required        | False                          |


| Parameters      | Description                    |
|------------------|---------------------------------|
| Name            | MessageConfigDescription       |
| Type            | string                         |
| Description     | Message config description of the message cc listener assignment. |
| Required        | False                          |


| Parameters      | Description                    |
|------------------|---------------------------------|
| Name            | MessageType                    |
| Type            | string                         |
| Description     | Message type of the message cc listener assignment. Possible values: OrderDeclined, OrderSubmitted, ShipmentCreated, ForgottenPassword, OrderSubmittedForYourApproval, OrderSubmittedForApproval, OrderApproved, OrderSubmittedForYourApprovalHasBeenApproved, OrderSubmittedForYourApprovalHasBeenDeclined, NewUserInvitation. |
| Required        | False                          |


| Parameters      | Description                    |
|------------------|---------------------------------|
| Name            | BuyerID                        |
| Type            | string                         |
| Description     | ID of the buyer.               |
| Required        | False                          |


| Parameters      | Description                    |
|------------------|---------------------------------|
| Name            | UserGroupID                    |
| Type            | string                         |
| Description     | ID of the user group.          |
| Required        | False                          |


| Parameters      | Description                    |
|------------------|---------------------------------|
| Name            | UserID                         |
| Type            | string                         |
| Description     | ID of the user.                |
| Required        | False                          |

## `POST` `v1/messagesenders/CCListenerAssignments`
Save a message sender cc listener assignment
## Requestbody
```
{'MessageSenderAssignment': {'MessageSenderID': '', 'BuyerID': '', 'UserGroupID': ''}, 'MessageType': 'OrderDeclined', 'BuyerID': '', 'UserGroupID': '', 'UserID': ''}
```

```
[{'Name': 'MessageSenderAssignment', 'Type': 'object', 'Description': 'Message sender assignment of the message cc listener assignment.', 'Required': False}, {'Name': 'MessageType', 'Type': 'string', 'Description': 'Message type of the message cc listener assignment. Possible values: OrderDeclined, OrderSubmitted, ShipmentCreated, ForgottenPassword, OrderSubmittedForYourApproval, OrderSubmittedForApproval, OrderApproved, OrderSubmittedForYourApprovalHasBeenApproved, OrderSubmittedForYourApprovalHasBeenDeclined, NewUserInvitation.', 'Required': False}, {'Name': 'BuyerID', 'Type': 'string', 'Description': 'ID of the buyer. Searchable: priority level 0. Sortable: priority level 0.', 'Required': False}, {'Name': 'UserGroupID', 'Type': 'string', 'Description': 'ID of the user group. Searchable: priority level 1. Sortable: priority level 1.', 'Required': False}, {'Name': 'UserID', 'Type': 'string', 'Description': 'ID of the user. Searchable: priority level 2. Sortable: priority level 2.', 'Required': False}]
```

**Responsestatus**: `204`

## Responsebody