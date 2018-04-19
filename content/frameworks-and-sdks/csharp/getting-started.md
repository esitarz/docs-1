---
title: Csharp: Getting Started
date: 2018-04-16
category:Csharp
---


# We are currently updating and enhancing our C# SDK. When that work is
complete, we'll publish an updated guide here. In the meantime, you can still
use our [existing C# SDK](https://github.com/ordercloud-api/OrderCloud-CSharp-
SDK). Please don't hesitate to contact us with any questions.



## Requirements

  * .NET 4.0 or later
  * Windows Phone 7.1 (Mango)

## Installation

Run the following command in Nuget

## Configuration

Before you can make any API calls, you will first need to define the ClientID
and scopes.

**client_id** identifies the Organization or Buyer Organization you will be
interacting with. It can be found in the application tab of your Dashboard.
Check out this guide for more information.

**scopes** is an array of roles the app will request from the Oauth server.
Roles are unique for each API Client and can be limited further via each
user's Security Profile. Our example is using the `FullAccess` and
`DevCenterImpersonate` roles. Check out this guide for more information on
roles and Security Profiles.

Set your client_id and scopes:

    
    
    

## Authentication

To authenticate, you will need the username and a password of a user created
in the API Console.

The following function will retrieve the access token and set it in the header
of every subsequent request.

The full example is shown here:

    
    
    

## Impersonation

The SDK also supports making an API call on behalf of (impersonation) a user.

You will first need to set the impersonation token by providing the BuyerID,
UserID and the roles.

    
    
    

Then you can use the following function to start Impersonation

and the following function to stop Impersonation

Even though impersonation stopped, the original access token was saved. Now
the function can be called with no arguments and it will use the previously
saved access token. If you need to change who you are impersonating you can
provide new parameters.

The full example is shown here:

    
    
    

## Example

Letâs see how you might use the C# SDK to get a list of products. First
weâll need to create a new instance of Products.

Now we can use the ListProducts endpoint to get a list of products and print
the result

    
    
    

The full example is shown here:

    
    
    

For more API usage examples take a look at our [C# SDK
repository](https://github.com/ordercloud-api/csharp-sdk).

## Conclusion

You should now have enough information to get started building on our
platform! The API reference should be your go-to guide for working with the
API but be sure to check out the API guides and the [C# SDK
repository](https://github.com/ordercloud-api/csharp-sdk) as well.

If you notice anything wrong with this guide or have any questions please
don't hesitate to reach out to our Developer community on
[Slack](http://community.ordercloud.io/) or post your question on [Stack
Overflow](http://stackoverflow.com/) \- just use the tag `ordercloud`.



