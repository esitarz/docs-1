---
title: Authentication: Anonymous Shopping
date: 2018-04-16
category: Authentication
---


## Overview

Anonymous Shopping, or Guest Checkout, is when a user is enabled to browse a
catalog of products and/or checkout without registering themselves.

Accomplishing this requires OrderCloud.io developers to pull together a lot of
platform knowledge. We'll summarize that information here.

## Configuring the Application

An anonymous buyer experience must work within a given buyer user perspective
-- otherwise OrderCloud.io has no context for determining data the anonymous
user has access to. A template user provides the context for anonymous users, such as availible products, pricing, or promotions.

Use the [Create And Assign Users And User Groups]({filename}/platform-guides/core-concepts/assignments.md) guide if you need a reminder on how to set up a template user for anonymous shopping.

Once you have a template user, navigate to the Buyer Organizations Dashboard. From there, select the buyer application you want to allow anonymous shopping in. 

Next, we will take that template user and assign them as the application's **Anonymous Template User**. This is the user that all anonymous users will inherit security and assignments from.

![Anonymous-Template-User]({attach}/images/docs-guides/authentication/anonymous-template-user.jpg)

## Authenticating Anonymous Users

Once your application is set up with a template user, we're ready to
authenticate anonymously. Using the Client Credentials grant-type and only the
`client_id` of the buyer application you're using, make a request to the OrderCloud.io OAuth server:



```
    POST https://auth.ordercloud.io/oauth/token HTTP/1.1
    client_id=xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx&scope=Shopper  MeAddressAdmin MeCreditCardAdmin&grant_type=client_credentials

```

Obviously, what roles your anonymous template user has might be different, but `Shopper` is generally the least an anonymous template user needs. If you want anonymous users to be able to create their own shipping addresses and credit cards, they'll need `MeAddressAdmin` and `MeCreditCardAdmin`, in both this request's scope and the template user's security profile.

You will receive a standard OAuth response that contains an `access_token` you
can use for the duration of the anonymous shopping experience.

If you [decode](https://jwt.io/) the `access_token` that you recieve in this token request, you'll see something like the following:

```
{
  "usr": "anon-template",
  "cid": "1aa9b54e-b31d-48e6-94e2-7454208d82e0",
  "orderid": "iEYOUdiVuEKbhEfK3QrRIA",
  "usrtype": "buyer",
  "role": [
    "Shopper",
    "MeAdmin"
  ],
  "iss": "https://auth.ordercloud.io",
  "aud": "https://api.ordercloud.io",
  "exp": 1525123397,
  "nbf": 1524518597
}
```

Note the `orderid` in the token -- this is used if an anonymous user registers themself during the checkout process. 

> Anonymous `access_tokens` have a fixed duration of **1 week**, access token duration has no affect on anonymous users. Refresh tokens **are not available** to anonymous users.

It is important to note that while it is possible to fully submit an order
using this token, there is not a secure way to let the anonymous user view
historical order data. If this is required for your project, you should
consider profiling your users at some point before submitting an order.

## Profiling Anonymous Users

Prompting your anonymous shoppers to register themselves before checking out
ensures that historical order data can be captured so the user can view it
when they return to your site. When you choose to profile users doesn't
matter, it can happen before or after they create an order. Order information
created during the anonymous `access_token`'s life-cycle will transfer to the
newly profiled user automatically. This is where that `orderid` in the user token comes into play.

To register an anonymous user is relatively simple. There is a `register` endpoint, and the anonymous user's `access_token` is used to transfer the user from anonymous to a profiled use.

The request is relatively simple: include the anonymous user's `access_token`  and the request body should contain the profile information filled out by the anonymous user.

> NOTE: You really do have to provide the access_token in *both* the register endpoint URL and in the Authentication header.


```
    POST https://api.ordercloud.io/v1/me/register?anonUserToken=put_access_token_here HTTP/1.1
    Authentication: Bearer put_access_token_here
    Content-Type: application/json
```

```
    
    {
    "ID": "NewUserName",
    "Username": "MyUserName",
    "FirstName": "John",
    "LastName": "Doe",
    "Password" : "NewPassword!22"
    "Email": "user@email.com",
    "Phone": "555-555-5555",
    "TermsAccepted": true,
    "Active": true,
    "xp": null
    }
    

```

Similar to the OAuth 2.0 Response, you will receive an `access_token` after
profiling the user. At this point, remove the anonymous `access_token` and
continue forward with the profiled user's `access_token`.

