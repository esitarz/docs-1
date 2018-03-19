---
Title: Authentication: Anonymous Shopping
author: OrderCloud.io 
Date: 2018-03-19 15:32:44.250255
Category: Platform Guides
Tags: authentication
---


## Overview

Anonymous Shopping, or Guest Checkout, is when a user is enabled to browse a
catalog of products and/or checkout without registering themselves.
Accomplishing this requires OrderCloud.io developers to pull together a lot of
platform knowledge. We'll summarize that information here.

## Configuring the Application

An anonymous buyer experience must work within a given buyer user perspective
- otherwise OrderCloud.io has no context for determining data the anonymous
user has access to, like product and pricing information. Therefore, you will
need an active buyer user before we can proceed.

Once you've done that, navigate to the Dashboard and click on the **Buyer
Organizations** tab from the left hand nav and select your buyer organization
by clicking on the name. From there click on the application associated with
your Buyer Organization.

Next, we will add an **Anonymous Template User**. This will be the user that
all anonymous users will inherit security and assignments from.

![Anonymous-Template-User]({filename}/images/docs-guides/authentication/anonymous-
template-user.jpg)

## Authenticating Anonymous Users

Once your application is set up with a template user, we're ready to
authenticate anonymously. Using the Client Credentials grant-type and only a
client_id, make a request to the OrderCloud.io OAuth server:

    
    
    POST https://auth.ordercloud.io/oauth/token HTTP/1.1
    client_id=xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx&scope=ProductReader CategoryReader MeAddressAdmin MeCreditCardAdmin&grant_type=client_credentials
    

You will receive a standard OAuth response that contains an access_token you
can use for the duration of the anonymous shopping experience.

Anonymous access_tokens have a fixed duration of **1 week** , access token
duration has no affect on anonymous users. Refresh tokens **are not
available** to anonymous users.

It is important to note that while it is possible to fully submit an order
using this token, there isn't a secure way to let the anonymous user view
historical order data. If this is required for your project, you should
consider profiling your users at some point before submitting an order.

## Profiling Anonymous Users

Prompting your anonymous shoppers to profile themselves before checking out
ensures that historical order data can be captured so the user can view it
when they return to your site. When you choose to profile users doesn't
matter, it can happen before or after they create an order. Order information
created during the anonymous access_token's life-cycle will transfer to the
newly profiled user automatically.

The request is relatively simple: provide the anonymous access_token for the
`tempUserToken` and the request body should contain the profile information
filled out by the anonymous user:

    
    
    POST https://api.ordercloud.io/v1/me/register HTTP/1.1
    Authentication: Bearer put_access_token_here
    Content-Type: application/json
    
    
    {
      "ID": "NewUserName",
      "Username": "MyUserName",
      "FirstName": "John",
      "LastName": "Doe",
      "Email": "user@email.com",
      "Phone": "555-555-5555",
      "TermsAccepted": true,
      "Active": true,
      "xp": null
    }
    

Similar to the OAuth 2.0 Response, you will receive an access_token after
profiling the user. At this point, remove the anonymous access_token and
continue forward with the profiled user's access_token.

