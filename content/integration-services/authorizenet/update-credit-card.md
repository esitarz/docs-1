---
title: Authorizenet: Update Credit Card
date: 2018-04-16
category:Authorizenet
---






##  __Update Credit Card Overview





When a customer within your buyer application updates a credit card, the
integration endpoint can be called in order to update that card on
OrderCloud.io as well as Authorize.Net. The Customer Payment Profile will be
updated on Authorize.Net, followed by the card being patched on OrderCloud.io.
If either step fails, all changes will be reverted in order to keep each
system in sync. If the card is shared, meaning `Shared` was set to `true` when
the card was created, `Shared` must be passed as `true` when updating.









##  __Update Credit Card Request



```


    
    
    POST https://api.ordercloud.io/v1/integrationproxy/authorizenet HTTP/1.1
    Authorization: bearer insert_access_token_here
    Content-Type: application/json; charset=UTF-8
    
    {
    "BuyerID": "...",
    "TransactionType": "updateCreditCard",
    "CardDetails": {
    "CreditCardID": "...",
    "CardholderName": "...",
    "CardType": "...",
    "CardNumber": "...",
    "ExpirationDate": "...",
    "CardCode": "...",
    "Shared": false
    }
    }
    
    

```









##  __Update Credit Card Response



```


    
    
    HTTP/1.1 200 OK
    Content-Type: application/json; charset=UTF-8
    
    {
    "ID": "â¦",
    "Token": "â¦",
    "DateCreated": null,
    "CardType": "â¦",
    "PartialAccountNumber": "â¦",
    "CardholderName": "â¦",
    "ExpirationDate": null,
    "xp": null
    }
    
    

```









##  __Error Handling





During the credit card update process, the Authorize.Net Customer Payment
Profile will first be updated. Next, the card will be updated on
OrderCloud.io. In the case that either step fails, the card data will be
reverted in both locations, ensuring the data is accurate in each system.





Errors will return the exact response directly from the Authorize.Net or
OrderCloud.io endpoint that failed. However, if any required fields are
missing, a 400 error will be returned before any of the update process is
executed.





### Validation Response





In the case that a required field is missing from your request, the following
response will be returned containing a unique ErrorCode and Message, as well
as the request body sent during the call. The possible ErrorCodes and Messages
are listed below.



```


    
    
    HTTP/1.1 400 Bad Request
    Content-Type: application/json
    
    {
    "ErrorCode": "...",
    "Message": "...",
    "Data": {
    "...Request Body..."
    }
    }
    
    

```





  
<table>  
<tr>  
<th>

ErrorCode

</th>  
<th>

Message

</th>  
<th>

Status Code

</th> </tr>  
<tr>  
<td>

UpdateCreditCard.CreditCardIDRequired

</td>  
<td>

CardDetails.CreditCardID is required to update a credit card.

</td>  
<td>

400

</td> </tr> </table>







### Authorize.Net Error Response



```


    
    
    HTTP/1.1 200 OK
    Content-Type: application/json
    
    {
    "messages": {
    "resultCode": "...",
    "message": [
    {
    "code": "...",
    "text": "..."
    }
    ]
    }
    }
    
    

```





  
<table>  
<tr>  
<th>

resultCode

</th>  
<th>

message.code

</th>  
<th>

message.text

</th> </tr>  
<tr>  
<td>

Error

</td>  
<td>

E00013

</td>  
<td>

Card Number is invalid.

</td> </tr>  
<tr>  
<td>

Error

</td>  
<td>

E00013

</td>  
<td>

Expiration Date is invalid.

</td> </tr>  
<tr>  
<td>

Error

</td>  
<td>

E00027

</td>  
<td>

The credit card has expired.

</td> </tr> </table>







### OrderCloud.io Error Response





If an incorrect `BuyerID` was provided:



```


    
    
    HTTP/1.1 404 Not Found
    Content-Type: application/json
    
    {
    "Errors": [
    {
    "ErrorCode": "NotFound",
    "Message": "Buyer not found: 1234",
    "Data": null
    }
    ]
    }
    
    

```





If an incorrect `CardDetails.CreditCardID` was provided:



```


    
    
    HTTP/1.1 404 Not Found
    Content-Type: application/json
    
    {
    "Errors": [
    {
    "ErrorCode": "NotFound",
    "Message": "Credit Card not found: 2345",
    "Data": null
    }
    ]
    }
    
    

```





