---
title: Forgotten Password
date: 2018-03-27
category: API Reference
tags: Authentication And Authorization
slug: Authentication-And-Authorization-PasswordResets
---


## `POST` `v1/password/reset`
Send a verification code
## Request Body
	{
	    "ClientID": "",
	    "Email": "",
	    "URL": "",
	    "Username": ""
	}
| Name | Type | Description | Required | 
|---|---|---|---|
| ClientID | string | ID of the client. Required. | True |
| Email | string | Email of the password reset request. | False |
| Username | string | Username of the password reset request. | False |
| URL | string | URL of the password reset request. | False |

## Response Body
## `PUT` `v1/password/reset/{verificationCode}`
Reset a password by verification code

| Name | Type | Description | Required | 
|---|---|---|---|
| verificationCode | string | Verification code of the password reset. | True |

## Request Body
	{
	    "ClientID": "",
	    "Password": "",
	    "Username": ""
	}
| Name | Type | Description | Required | 
|---|---|---|---|
| ClientID | string | ID of the client. Required. | True |
| Username | string | Username of the password reset. | False |
| Password | string | Password of the password reset. | False |

## Response Body