---
title: Message Senders
date: 2018-03-27
category: API Reference
tags: Seller
slug: Seller-MessageSenders
---


## `GET` `v1/messagesenders/{messageSenderID}`
Get a single message sender

| Name | Type | Description | Required | 
|---|---|---|---|
| messageSenderID | string | ID of the message sender. | True |

## Response Body
	:::json
	{
	    "Description": "",
	    "ID": "",
	    "MessageTypes": [
	        "OrderDeclined"
	    ],
	    "Name": ""
	}


| Name | Type | Description | Required | 
|---|---|---|---|
| ID | string | ID of the message sender. | False |
| Name | string | Name of the message sender. | False |
| MessageTypes | array | Message types of the message sender. | True |
| Description | string | Description of the message sender. | False |

## `GET` `v1/messagesenders`
Get a list of message senders

| Name | Type | Description | Required | 
|---|---|---|---|
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
	            "Description": "",
	            "ID": "",
	            "MessageTypes": [
	                "OrderDeclined"
	            ],
	            "Name": ""
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
| ID | string | ID of the message sender. | False |
| Name | string | Name of the message sender. | False |
| MessageTypes | array | Message types of the message sender. | True |
| Description | string | Description of the message sender. | False |

## `GET` `v1/messagesenders/assignments`
Get a list of message sender assignments

| Name | Type | Description | Required | 
|---|---|---|---|
| buyerID | string | ID of the buyer. | False |
| messageSenderID | string | ID of the message sender. | False |
| userID | string | ID of the user. | False |
| userGroupID | string | ID of the user group. | False |
| level | string | Level of the message sender assignment. Possible values: User, Group, Company. | False |
| page | integer | Page of results to return. Default: 1 | False |
| pageSize | integer | Number of results to return per page. Default: 20, max: 100. | False |

## Response Body
	:::json
	{
	    "Items": [
	        {
	            "BuyerID": "",
	            "MessageConfigDescription": "",
	            "MessageConfigName": "",
	            "MessageSenderID": "",
	            "UserGroupID": ""
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
| MessageSenderID | string | ID of the message sender. | True |
| BuyerID | string | ID of the buyer. | False |
| UserGroupID | string | ID of the user group. | False |
| MessageConfigName | string | Message config name of the message sender assignment. | False |
| MessageConfigDescription | string | Message config description of the message sender assignment. | False |

## `DELETE` `v1/messagesenders/{messageSenderID}/assignments`
Delete a message sender assignment

| Name | Type | Description | Required | 
|---|---|---|---|
| messageSenderID | string | ID of the message sender. | True |
| buyerID | string | ID of the buyer. | False |
| userID | string | ID of the user. | False |
| userGroupID | string | ID of the user group. | False |

## Response Body
## `POST` `v1/messagesenders/assignments`
Save a message sender assignment
## Request Body
	:::json
	{
	    "BuyerID": "",
	    "MessageSenderID": "",
	    "UserGroupID": ""
	}


| Name | Type | Description | Required | 
|---|---|---|---|
| MessageSenderID | string | ID of the message sender. Required. Sortable: priority level 1. | True |
| BuyerID | string | ID of the buyer. Sortable: priority level 2. | False |
| UserGroupID | string | ID of the user group. Sortable: priority level 3. | False |

## Response Body
## `GET` `v1/messagesenders/CCListenerAssignments`
Get a list of message sender cc listener assignments

| Name | Type | Description | Required | 
|---|---|---|---|
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
	            "BuyerID": "",
	            "MessageConfigDescription": "",
	            "MessageConfigName": "",
	            "MessageSenderAssignment": {
	                "BuyerID": "",
	                "MessageConfigDescription": "",
	                "MessageConfigName": "",
	                "MessageSenderID": "",
	                "UserGroupID": ""
	            },
	            "MessageType": "OrderDeclined",
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
| MessageSenderAssignment | object | Message sender assignment of the message cc listener assignment. | False |
| MessageConfigName | string | Message config name of the message cc listener assignment. | False |
| MessageConfigDescription | string | Message config description of the message cc listener assignment. | False |
| MessageType | string | Message type of the message cc listener assignment. Possible values: OrderDeclined, OrderSubmitted, ShipmentCreated, ForgottenPassword, OrderSubmittedForYourApproval, OrderSubmittedForApproval, OrderApproved, OrderSubmittedForYourApprovalHasBeenApproved, OrderSubmittedForYourApprovalHasBeenDeclined, NewUserInvitation. | False |
| BuyerID | string | ID of the buyer. | False |
| UserGroupID | string | ID of the user group. | False |
| UserID | string | ID of the user. | False |

## `POST` `v1/messagesenders/CCListenerAssignments`
Save a message sender cc listener assignment
## Request Body
	:::json
	{
	    "BuyerID": "",
	    "MessageSenderAssignment": {
	        "BuyerID": "",
	        "MessageSenderID": "",
	        "UserGroupID": ""
	    },
	    "MessageType": "OrderDeclined",
	    "UserGroupID": "",
	    "UserID": ""
	}


| Name | Type | Description | Required | 
|---|---|---|---|
| MessageSenderAssignment | object | Message sender assignment of the message cc listener assignment. | False |
| MessageType | string | Message type of the message cc listener assignment. Possible values: OrderDeclined, OrderSubmitted, ShipmentCreated, ForgottenPassword, OrderSubmittedForYourApproval, OrderSubmittedForApproval, OrderApproved, OrderSubmittedForYourApprovalHasBeenApproved, OrderSubmittedForYourApprovalHasBeenDeclined, NewUserInvitation. | False |
| BuyerID | string | ID of the buyer. Searchable: priority level 0. Sortable: priority level 0. | False |
| UserGroupID | string | ID of the user group. Searchable: priority level 1. Sortable: priority level 1. | False |
| UserID | string | ID of the user. Searchable: priority level 2. Sortable: priority level 2. | False |

## Response Body