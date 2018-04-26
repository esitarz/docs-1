---
title: Authentication: Developer Access
date: 2018-04-16
category: Authentication
---


## Developer Access

In order to make it easier for developers to get in and start testing
applications, we made a unique role called `DevCenterImpersonate`. This role
allows you to log into your application with your DevCenter username and
password, so you don't have to go through the trouble of creating a user first.

To take advantage of this feature simply include the role
`DevCenterImpersonate` in your security profile and the scope of your authentication request:



```
    POST https://auth.ordercloud.io/oauth/token HTTP/1.1
    Content-Type: text/html; charset=UTF-8
```

```    
    client_id=xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx&grant_type=password&username=xxxxxxxx&password=xxxxxxxx&scope=FullAccess DevCenterImpersonate
```

