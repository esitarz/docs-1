---
title: Forgotten Password
date: 2018-03-23
category: API Reference
tags: Authentication And Authorization
slug: PasswordResets
---


## Send a verification code
### `POST` `v1/password/reset`

| Parameters      | Description                    |
|------------------|---------------------------------|

 **Requestbody**: 
{'Sample': '{\r\n  "ClientID": "",\r\n  "Email": "",\r\n  "Username": "",\r\n  "URL": ""\r\n}', 'Fields': [{'Name': 'ClientID', 'Type': 'string', 'Description': 'ID of the client. Required.', 'Required': True}, {'Name': 'Email', 'Type': 'string', 'Description': 'Email of the password reset request.', 'Required': False}, {'Name': 'Username', 'Type': 'string', 'Description': 'Username of the password reset request.', 'Required': False}, {'Name': 'URL', 'Type': 'string', 'Description': 'URL of the password reset request.', 'Required': False}]}
 **Responsestatus**: `204`

 **Responsebody**: 
None
## Reset a password by verification code
### `PUT` `v1/password/reset/{verificationCode}`

| Parameters      | Description                    |
|------------------|---------------------------------|
| Name            | verificationCode               |
| Type            | string                         |
| Description     | Verification code of the password reset. |
| Required        | True                           |

 **Requestbody**: 
{'Sample': '{\r\n  "ClientID": "",\r\n  "Username": "",\r\n  "Password": ""\r\n}', 'Fields': [{'Name': 'ClientID', 'Type': 'string', 'Description': 'ID of the client. Required.', 'Required': True}, {'Name': 'Username', 'Type': 'string', 'Description': 'Username of the password reset.', 'Required': False}, {'Name': 'Password', 'Type': 'string', 'Description': 'Password of the password reset.', 'Required': False}]}
 **Responsestatus**: `204`

 **Responsebody**: 
None