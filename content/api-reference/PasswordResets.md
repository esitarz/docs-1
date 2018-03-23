---
title: Forgotten Password
date: 2018-03-23
category: API Reference
tags: Authentication And Authorization
slug: PasswordResets
---


## `POST` `v1/password/reset`
Send a verification code
## Requestbody
```
{'ClientID': '', 'Email': '', 'Username': '', 'URL': ''}
```

```
[{'Name': 'ClientID', 'Type': 'string', 'Description': 'ID of the client. Required.', 'Required': True}, {'Name': 'Email', 'Type': 'string', 'Description': 'Email of the password reset request.', 'Required': False}, {'Name': 'Username', 'Type': 'string', 'Description': 'Username of the password reset request.', 'Required': False}, {'Name': 'URL', 'Type': 'string', 'Description': 'URL of the password reset request.', 'Required': False}]
```

**Responsestatus**: `204`

## Responsebody
## `PUT` `v1/password/reset/{verificationCode}`
Reset a password by verification code

| Parameters      | Description                    |
|------------------|---------------------------------|


| Parameters      | Description                    |
|------------------|---------------------------------|
| Name            | verificationCode               |
| Type            | string                         |
| Description     | Verification code of the password reset. |
| Required        | True                           |

## Requestbody
```
{'ClientID': '', 'Username': '', 'Password': ''}
```

```
[{'Name': 'ClientID', 'Type': 'string', 'Description': 'ID of the client. Required.', 'Required': True}, {'Name': 'Username', 'Type': 'string', 'Description': 'Username of the password reset.', 'Required': False}, {'Name': 'Password', 'Type': 'string', 'Description': 'Password of the password reset.', 'Required': False}]
```

**Responsestatus**: `204`

## Responsebody