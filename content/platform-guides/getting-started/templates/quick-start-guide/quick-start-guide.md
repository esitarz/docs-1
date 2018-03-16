

## __Getting Started with OrderCloud.io

OrderCloud.io is a RESTful API that enables you to create complex, custom B2B
eCommerce solutions.

This guide is meant to get you started with OrderCloud.io as quickly as
possible. In order to accomplish this, we’ve stripped away some of the detail,
so keep an eye out for links to relevant guides that provide much more in-
depth explanations.

## __Creating an Account

The first thing you will need to do is create an account. Registration is free
and gives you access to the entire OrderCloud.io platform.

After you submit your email address, you will be sent a verification code
which will be required to complete the registration process.

## __Your First Seller Organization

Now that you have an OrderCloud.io account you can navigate to your
[dashboard](https://dashboard.ordercloud.io) and access your first seller
organization.

It is the highest level container that encompasses everything else in
OrderCloud.io (applications, products, pricing, users, etc.). You can have
multiple Seller Organizations; however, data is not shared between them.

Newly created Seller Organizations come with a "default access" application
giving you immediate access to the API however you can also create your own.
To do this first click on the seller applications pane on the left and then
click the  __New button located in the upper right hand corner.

Using the API Console is the simplest way to start exploring OrderCloud.io;
however, understanding the fundamentals of how to access and use the API on
it's own is extremely important for any OrderCloud.io developer.

## __Authentication

Before you are able to interact with the OrderCloud.io API you will need to
get an `access_token` from the auth server. The following sections will
include raw request and response examples to the OAuth API.

The first thing you need is the `ClientID`. This unique identifier represents
a single application on OrderCloud.io. Feel free to use the ClientID from the
"default access" application that was automatically created on your first
Seller Organization.

![](/assets/images/docs-guides/getting-started/quick-start-guide/quick-start-
guide-1.jpg)

The second thing you will need is a list of roles, or in OAuth terms, scope.
For this example you are not authenticating as an actual user (because we
haven't created one yet). Instead, you will be taking advantage of a useful
developer role, `DevCenterImpersonate`". This role will allow you to use the
password grant type workflow with your own Dev Center username and password.

Along with our special DevCenterImpersonate role we will also request
"FullAccess". Being the owners of this Organization it's safe to say we can
access and change any data related to it. Giving real users "FullAccess" is
highly discouraged, a subset of roles helps protect your application from
malicious attacks or oblivious users.

Using your ClientID, roles list, and Dev Center username/password, request an
access token following the example below:

  
Request

  
Response

## __Subsequent Requests

Using the access_token from the OAuth response make your first `GET` request
to the UserPerspecive -> Me -> Get endpoint. This will return the details for
the currently authenticated user. (In this case, you will appear as the
default user because we authenticated as a developer). Make sure you put your
`access_token` in the Authentication header before making the request.

  
Request

  
Response

