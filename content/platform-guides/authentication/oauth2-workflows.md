---
Title: Oauth2 Workflows
author: OrderCloud.io 
Date: 2018-03-19 15:32:44.250255
Tags: authentication
---


## What is OAuth?

OAuth is an open standard for authorization commonly used as a way for users
to log into third party websites using Microsoft, Google, Facebook etc.
accounts without exposing their password. It is increasingly becoming an
industry standard for security and permission-based application experiences
and is what we use at OrderCloud.io. OAuth allows you to configure a total of
four different workflows all of which use the following Method and Request
URL.

    
    
    POST https://auth.ordercloud.io/oauth/token HTTP/1.1
    Content-Type: text/html; charset=UTF-8
    

## Required Information

All of the information required for an authentication request can be accessed
from your Dashboard.

## 1\. Password Grant Type

This workflow is most appropriate for client apps where the user is a human,
i.e, a registered OrderCloud.io Buyer or Admin user. A successful
authentication with this workflow requires the following information:

  1. Client ID
  2. Scope
  3. Username
  4. Password
  5. Grant Type: `grant_type=password`

    
    
    POST https://auth.ordercloud.io/oauth/token HTTP/1.1
    Content-Type: text/html; charset=UTF-8
    
    client_id=xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx&grant_type=password&username=xxxxxxxx&password=xxxxxxxx&scope=Shopper
    

## 2\. Client Credentials Grant Type

This configuration is best suited for an application where you need a way for
your backend system to log in. It is also appropriate when you are just
getting started and need to seed your application with users who can
subsequently authenticate using the Password Grant type. A successful
authentication with this workflow requires the following information:

  1. Client ID
  2. Client Secret
  3. Scope
  4. Grant Type: `grant_type=client_credentials`

    
    
    POST https://auth.ordercloud.io/oauth/token HTTP/1.1
    Content-Type: text/html; charset=UTF-8
    
    client_id=xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx&grant_type=client_credentials&client_secret=xxxxxxxxxxxxx&scope=FullAccess
    

## 3\. Anonymous Shopping or Guest Checkout

There are some B2B clients that will want to enable visitors to browse a
catalog of products and/or checkout without registering themselves. We call
this Anonymous Shopping or Guest Checkout. An in-depth guide for this workflow
is detailed here

## 4\. Elevated Password Grant Type

The final workflow is the same as the Password Grant Type workflow except that
it has an additional requirement of Client Secret. This type of workflow would
be used if you want to add an additional layer of security.

To use this workflow you will first need to set the Client Secret in the
Dashboard's app tab and include the Client Secret in each request

    
    
    POST https://auth.ordercloud.io/oauth/token HTTP/1.1
    Content-Type: text/html; charset=UTF-8
    
    client_id=xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx&grant_type=client_credentials&client_secret=xxxxxxxxxxxxx&scope=FullAccess
    

## Subsequent Requests

A successful authentication (using one of the four workflows) will yield the
following response:

    
    
    {
       "access_token": "eyJ0eXAi0iJKV1QiLCJhbGci0iJ",
       "token_type" : "bearer",
       "expires_in" : 35999,
       "refresh_token": "878ca890-af6a-48b6-98a2-1e1cf4a.."
    }
    

The `access_token` from the response will need to be included in each and
every OrderCloud.io API request as part of the Authorization header prefaced
by `Bearer`.

    
    
    GET https://api.ordercloud.io/v1/buyers HTTP/1.1
    Authentication: Bearer eyJ0eXAi0iJKV1QiLCJhbGci0iJ9...
    Content-Type: application/json; charset=UTF-8
    

## Conclusion

You should now have a basic understanding of the four different OAuth 2
workflows. Each of these workflows return a token which allows you to make
authenticated calls to OrderCloud.io.

