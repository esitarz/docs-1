---
Title: Developer Access
author: OrderCloud.io 
Date: 2018-03-19 15:32:44.250255
Tags: authentication
---


## __Developer Access

In order to make it easier for developers to get in and start testing
applications we made a unique role called `DevCenterImpersonate`. This role
allows you to log into your application with your Dev Center username and
password so you don't have to go through the trouble of creating a user first.

To take advantage of this feature simply include the role
`DevCenterImpersonate` in the scope of your authentication request:

