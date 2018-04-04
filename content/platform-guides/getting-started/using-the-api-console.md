---
Title: Using The Api Console
author: OrderCloud.io 
Date: 2018-03-19 15:32:44.250255
Tags: getting started
---


## __Introduction

The OrderCloud.io API Console provides instant access to your OrderCloud
applications. It is extremely useful for rapidly spinning up some data to
develop against or learning about all the different endpoints OrderCloud.io
has to offer.

## __Getting to the Console

The console is available at console.ordercloud.io and can be navigated to via
the top navigation or by clicking "Open API Console" when viewing an
application in the dashboard. If you navigate directly to the console via the
top navigation, you will be prompted to choose a Seller or Buyer application
before continuing.

![]({filename}/images/docs-guides/getting-started/using-the-api-console/seller-
and-buyer.png)

##  __Current User

When first opening the console, you will notice a black box in the top left
that lets you know the user your are currently authenticated as. By default,
the console will open the application using your developer profile - thereby
making you the seller organization's "Default contact user". **This is not a
real user** , it is simply there to allow developers access to the API before
any real users have been created.

![]({filename}/images/docs-guides/getting-started/using-the-api-console/current-
user.png)

##  __Current Context

Clicking on the Current User will reveal additional details about your current
"context". This includes the active Seller Organization, Buyer Organization
(if any), and application you currently have open in the console. You can
click the blue links to quickly jump back into the OrderCloud.io Dashboard for
each item.

By clicking "Change Context" you can open a different OrderCloud application
without ever leaving the API Console.

![]({filename}/images/docs-guides/getting-started/using-the-api-console/current-
context.png)

##  __Impersonation

Due to the limited capabilities of the Default Contact User, we have provided
a handy feature for impersonating a **buyer user** within your current
context. Within the Current User dropdown you can click "Impersonate User" and
fill out the form to find the buyer user you wish to perform API calls on
behalf of.

By clicking "Change Context" you can open a different OrderCloud application
without ever leaving the API Console.

##  __Lockable Parameters

Sometimes you will be making many successive requests with the same
parameters. To make this easier for you, we included the ability to lock
specific parameter values for the duration of your console session. If you
know you'll always be working with the same buyer, enter the Buyer ID
parameter once, click the lock button and forget about it!

![]({filename}/images/docs-guides/getting-started/using-the-api-console/lockable-
params.png)

## __Making Requests

Making a request in the API Console is relatively simple. Begin by choosing a
resource from the console menu on the left. Once the resource loads in the
second pane, you can choose the method (endpoint) you would like to use. If
you're not sure which endpoint to use, check out our API Reference for a full
list. If you're following along with our guides, each step will have a link to
the specific endpoint being used.

Depending on the endpoint, you will be required to fill out some parameters
and/or a request body. When all required parameters have been filled out,
click "Send" and the successful response or error message will appear in the
pane on the right. View previous responses by clicking on the response in the
list above the active response body.

## __Conclusion

The Console eliminates the headache of making authentication requests before
using the OrderCloud API. Use it to dive into your data quickly and make rapid
changes while developing your applications. We're always looking for ways to
improve the experience, so any feedback or suggestions you have as a user of
the platform are greatly appreciated!

