---
title: Create Credit Card
date: 2018-04-16
---






##  __Create Credit Card Overview





When a customer within your buyer application creates a credit card, the
integration endpoint can be called in order to create that card within
OrderCloud.io as well as Authorize.Net. The card will created as a personal
card by default. However, passing `true` for `Shared` assign the card to the
entire Buyer Organization provided in the `BuyerID`. This endpoint will create
a Customer Profile within Authorize.Net if one does not already exist
(Authorize.Net Customer Profile ID will be saved as xp.AuthorizeNetProfileID
on the User), create a Customer Payment Profile within Authorize.Net that
securely stores the tokenized data for the card, and finally create and assign
the card on OrderCloud.io to the authenticate user.









##  __Create Credit Card Request



```


    
    
    POST https://api.ordercloud.io/v1/integrationproxy/authorizenet HTTP/1.1
    Authorization: bearer insert_access_token_here
    Content-Type: application/json; charset=UTF-8
    
    {
    "BuyerID": "...",
    "TransactionType": "createCreditCard",
    "CardDetails": {
    "CardholderName": "...",
    "CardType": "...",
    "CardNumber": "...",
    "ExpirationDate": "...",
    "CardCode": "...",
    "Shared": false
    }   
    }
    
    

```









##  __Create Credit Card Response



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





During the credit card create process, the Authorize.Net Customer Profile and
Customer Payment Profile are created (if necessary) first, followed by the
creation of the card on OrderCloud.io. Therefore, if any errors occur, they
will occur in that order. Errors will return the exact response directly from
the Authorize.Net or OrderCloud.io endpoint that failed. However, if any
required fields are missing, a 400 error will be returned before any of the
creation process is executed.





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

CreateCreditCard.CardNumberRequired

</td>  
<td>

CardDetails.CardNumber is required to create a new credit card.

</td>  
<td>

400

</td> </tr>  
<tr>  
<td>

CreateCreditCard.ExpirationDateRequired

</td>  
<td>

CardDetails.ExpirationDate is required to create a new credit card.

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





