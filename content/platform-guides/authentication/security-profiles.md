---
title: Authentication: Security Profiles
date: 2018-04-16
category: Authentication
---


## Overview

Security Profiles are an assortment of roles that give access to specific
endpoints in the OrderCloud.io API. Profiles can be assigned to the users of
your Seller or Buyer application. If a request is made by a user without
sufficient roles they will receive 403 Forbidden response. Configuration of
these profiles is possible within the Security Profiles view in the
OrderCloud.io Dashboard.

##  Roles

Security Profiles are made up of a list of roles which fall into one of two
categories: Admin and Reader. An **Admin** role allows read and write access
while a **Reader** role type allows only read access.



![Screenshot of Security Roles selection]({attach}/images/docs-guides/authentication/security-profiles.roles.png)

## Assigning Profiles

Security Profiles are assigned at the party level (User, User Group, Buyer
Organization or Admin Organization).



```
    POST https://api.ordercloud.io/v1/securityprofiles/assignments HTTP/1.1
    Authentication: Bearer put_access_token_here
    Content-Type: application/json; charset=UTF-8
```

```   
    {
    "SecurityProfileID": "ID_OF_YOUR_USER_SECURITY_PROFILE",
    "BuyerID": null,
    "UserGroupID": null,
    "UserID": null
    }
```

If more than one Security Profile is inherited, the roles will be a union of
the roles from every inherited Security Profile.


## Scope: Accessing A User's Roles

Having a role in a user's assigned security profile will not mean the user automatically has access to it -- instead, their authentication has to request the nessecary roles.

In the [OAuth Authentication Guide]({filename}/platform-guides/authentication/oauth2-workflows.md), `scope` is mentioned. This is where the user must request the roles assigned to them, in order to be able to use them. The `scope` can be any subset of roles available in the user's security profile. If any roles are requested that the user does not have in their security profile, the requested roles are silently ignored.