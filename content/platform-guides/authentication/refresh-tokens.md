---
title: Refresh Tokens
date: 2018-04-16
---






## __Overview





You will learn how to set-up and use refresh tokens which will allow your
users to remain signed in without having to reauthenticate. This guide assumes
you already know how to authenticate using one of the four workflows









##  __Understanding Tokens





A successful request to authenticate will return a response much like the
following.





```


    
    
    POST https://api.ordercloud.io/oauth/token HTTP/1.1
    Content-Type: application/json; charset=UTF-8
    

```



```


    
    
    {
    "access_token": "eyJ0eXAi0iJKV1QiLCJhbGci0iJ",
    "token_type" : "bearer",
    "expires_in" : 35999,
    "refresh_token": "878ca890-af6a-48b6-98a2-1e1cf4a.."
    }
    

```







In a typical workflow, you will use the access token in any request to the
OrderCloud.io API. When that token expires, you will need to re-authenticate.
The refresh token can be used to retrieve a new access token without needing
user credentials or a client secret.





If you are planning on retrieving a new access token using this method then
you will want to store that refresh token when first authenticating.





Although not visible from the response, the refresh token also has an
expiration duration. Once expired, you will no longer be able to request a new
access token using that refresh token. The expiration duration for both the
access and refresh tokens can be changed from the Applications view in the
Dashboard. A refresh token duration of `0` will not return a refresh token.









##  __Using a Refresh Token





The following information will be needed for the request:



  
<table>  
<tr>  
<th>

Variable

</th>  
<th>

Definition

</th> </tr>  
<tr>  
<td>

grant_type

</td>  
<td>

Value must be refresh_token

</td> </tr>  
<tr>  
<td>

client_id

</td>  
<td>

This will be the client ID used in the original request

</td> </tr>  
<tr>  
<td>

refresh_token

</td>  
<td>

This will be the refresh_token from the first response

</td> </tr> </table>





A successful request might look like this:





```


    
    
    POST https://auth.ordercloud.io/oauth/token HTTP/1.1
    Content-Type: text/html; charset=UTF-8
    
    client_id=xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx&grant_type=refresh_token&refresh_token=878ca890-af6a48b6-98a2-1e1cf4a&scope=FullAccess
    

```











##  __Conclusion





After reading this guide you should now be able to retrieve access tokens by
using refresh tokens. This will allow your users to remain signed in as long
as their refresh token has not expired.





