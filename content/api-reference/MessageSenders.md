---
title: Message Senders
date: 2018-03-23
category: API Reference
tags: Seller
slug: MessageSenders
---

## Get a single message sender
### `GET` `v1/messagesenders/{messageSenderID}`

| Parameters      | Description                    |
|------------------|---------------------------------|
| Name            | messageSenderID                |
| Type            | string                         |
| Description     | ID of the message sender.      |
| Required        | True                           |

 **Requestbody**: 
None
 **Responsestatus**: `200`

 **Responsebody**: 
{'Sample': '{\r\n  "ID": "",\r\n  "Name": "",\r\n  "MessageTypes": [\r\n    "OrderDeclined"\r\n  ],\r\n  "Description": ""\r\n}', 'Fields': [{'Name': 'ID', 'Type': 'string', 'Description': 'ID of the message sender.', 'Required': False}, {'Name': 'Name', 'Type': 'string', 'Description': 'Name of the message sender.', 'Required': False}, {'Name': 'MessageTypes', 'Type': 'array', 'Description': 'Message types of the message sender.', 'Required': True}, {'Name': 'Description', 'Type': 'string', 'Description': 'Description of the message sender.', 'Required': False}]}## Get a list of message senders
### `GET` `v1/messagesenders`

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
{'Sample': '{\r\n  "Meta": {\r\n    "Page": 1,\r\n    "PageSize": 20,\r\n    "TotalCount": 25,\r\n    "TotalPages": 2,\r\n    "ItemRange": [\r\n      1,\r\n      20\r\n    ]\r\n  },\r\n  "Items": [\r\n    {\r\n      "ID": "",\r\n      "Name": "",\r\n      "MessageTypes": [\r\n        "OrderDeclined"\r\n      ],\r\n      "Description": ""\r\n    }\r\n  ]\r\n}', 'Fields': [{'Name': 'ID', 'Type': 'string', 'Description': 'ID of the message sender.', 'Required': False}, {'Name': 'Name', 'Type': 'string', 'Description': 'Name of the message sender.', 'Required': False}, {'Name': 'MessageTypes', 'Type': 'array', 'Description': 'Message types of the message sender.', 'Required': True}, {'Name': 'Description', 'Type': 'string', 'Description': 'Description of the message sender.', 'Required': False}]}## Get a list of message sender assignments
### `GET` `v1/messagesenders/assignments`

| Parameters      | Description                    |
|------------------|---------------------------------|
| Name            | buyerID                        |
| Type            | string                         |
| Description     | ID of the buyer.               |
| Required        | False                          |
| Name            | messageSenderID                |
| Type            | string                         |
| Description     | ID of the message sender.      |
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
| Description     | Level of the message sender assignment. Possible values: User, Group, Company. |
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
{'Sample': '{\r\n  "Meta": {\r\n    "Page": 1,\r\n    "PageSize": 20,\r\n    "TotalCount": 25,\r\n    "TotalPages": 2,\r\n    "ItemRange": [\r\n      1,\r\n      20\r\n    ]\r\n  },\r\n  "Items": [\r\n    {\r\n      "MessageSenderID": "",\r\n      "BuyerID": "",\r\n      "UserGroupID": "",\r\n      "MessageConfigName": "",\r\n      "MessageConfigDescription": ""\r\n    }\r\n  ]\r\n}', 'Fields': [{'Name': 'MessageSenderID', 'Type': 'string', 'Description': 'ID of the message sender.', 'Required': True}, {'Name': 'BuyerID', 'Type': 'string', 'Description': 'ID of the buyer.', 'Required': False}, {'Name': 'UserGroupID', 'Type': 'string', 'Description': 'ID of the user group.', 'Required': False}, {'Name': 'MessageConfigName', 'Type': 'string', 'Description': 'Message config name of the message sender assignment.', 'Required': False}, {'Name': 'MessageConfigDescription', 'Type': 'string', 'Description': 'Message config description of the message sender assignment.', 'Required': False}]}## Delete a message sender assignment
### `DELETE` `v1/messagesenders/{messageSenderID}/assignments`

| Parameters      | Description                    |
|------------------|---------------------------------|
| Name            | messageSenderID                |
| Type            | string                         |
| Description     | ID of the message sender.      |
| Required        | True                           |
| Name            | buyerID                        |
| Type            | string                         |
| Description     | ID of the buyer.               |
| Required        | False                          |
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
None## Save a message sender assignment
### `POST` `v1/messagesenders/assignments`

| Parameters      | Description                    |
|------------------|---------------------------------|

 **Requestbody**: 
{'Sample': '{\r\n  "MessageSenderID": "",\r\n  "BuyerID": "",\r\n  "UserGroupID": ""\r\n}', 'Fields': [{'Name': 'MessageSenderID', 'Type': 'string', 'Description': 'ID of the message sender. Required. Sortable: priority level 1.', 'Required': True}, {'Name': 'BuyerID', 'Type': 'string', 'Description': 'ID of the buyer. Sortable: priority level 2.', 'Required': False}, {'Name': 'UserGroupID', 'Type': 'string', 'Description': 'ID of the user group. Sortable: priority level 3.', 'Required': False}]}
 **Responsestatus**: `204`

 **Responsebody**: 
None## Get a list of message sender cc listener assignments
### `GET` `v1/messagesenders/CCListenerAssignments`

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
{'Sample': '{\r\n  "Meta": {\r\n    "Page": 1,\r\n    "PageSize": 20,\r\n    "TotalCount": 25,\r\n    "TotalPages": 2,\r\n    "ItemRange": [\r\n      1,\r\n      20\r\n    ]\r\n  },\r\n  "Items": [\r\n    {\r\n      "MessageSenderAssignment": {\r\n        "MessageSenderID": "",\r\n        "BuyerID": "",\r\n        "UserGroupID": "",\r\n        "MessageConfigName": "",\r\n        "MessageConfigDescription": ""\r\n      },\r\n      "MessageConfigName": "",\r\n      "MessageConfigDescription": "",\r\n      "MessageType": "OrderDeclined",\r\n      "BuyerID": "",\r\n      "UserGroupID": "",\r\n      "UserID": ""\r\n    }\r\n  ]\r\n}', 'Fields': [{'Name': 'MessageSenderAssignment', 'Type': 'object', 'Description': 'Message sender assignment of the message cc listener assignment.', 'Required': False}, {'Name': 'MessageConfigName', 'Type': 'string', 'Description': 'Message config name of the message cc listener assignment.', 'Required': False}, {'Name': 'MessageConfigDescription', 'Type': 'string', 'Description': 'Message config description of the message cc listener assignment.', 'Required': False}, {'Name': 'MessageType', 'Type': 'string', 'Description': 'Message type of the message cc listener assignment. Possible values: OrderDeclined, OrderSubmitted, ShipmentCreated, ForgottenPassword, OrderSubmittedForYourApproval, OrderSubmittedForApproval, OrderApproved, OrderSubmittedForYourApprovalHasBeenApproved, OrderSubmittedForYourApprovalHasBeenDeclined, NewUserInvitation.', 'Required': False}, {'Name': 'BuyerID', 'Type': 'string', 'Description': 'ID of the buyer.', 'Required': False}, {'Name': 'UserGroupID', 'Type': 'string', 'Description': 'ID of the user group.', 'Required': False}, {'Name': 'UserID', 'Type': 'string', 'Description': 'ID of the user.', 'Required': False}]}## Save a message sender cc listener assignment
### `POST` `v1/messagesenders/CCListenerAssignments`

| Parameters      | Description                    |
|------------------|---------------------------------|

 **Requestbody**: 
{'Sample': '{\r\n  "MessageSenderAssignment": {\r\n    "MessageSenderID": "",\r\n    "BuyerID": "",\r\n    "UserGroupID": ""\r\n  },\r\n  "MessageType": "OrderDeclined",\r\n  "BuyerID": "",\r\n  "UserGroupID": "",\r\n  "UserID": ""\r\n}', 'Fields': [{'Name': 'MessageSenderAssignment', 'Type': 'object', 'Description': 'Message sender assignment of the message cc listener assignment.', 'Required': False}, {'Name': 'MessageType', 'Type': 'string', 'Description': 'Message type of the message cc listener assignment. Possible values: OrderDeclined, OrderSubmitted, ShipmentCreated, ForgottenPassword, OrderSubmittedForYourApproval, OrderSubmittedForApproval, OrderApproved, OrderSubmittedForYourApprovalHasBeenApproved, OrderSubmittedForYourApprovalHasBeenDeclined, NewUserInvitation.', 'Required': False}, {'Name': 'BuyerID', 'Type': 'string', 'Description': 'ID of the buyer. Searchable: priority level 0. Sortable: priority level 0.', 'Required': False}, {'Name': 'UserGroupID', 'Type': 'string', 'Description': 'ID of the user group. Searchable: priority level 1. Sortable: priority level 1.', 'Required': False}, {'Name': 'UserID', 'Type': 'string', 'Description': 'ID of the user. Searchable: priority level 2. Sortable: priority level 2.', 'Required': False}]}
 **Responsestatus**: `204`

 **Responsebody**: 
None