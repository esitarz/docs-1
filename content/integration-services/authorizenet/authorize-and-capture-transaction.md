---
title: Authorizenet: Authorize And Capture Transaction
date: 2018-04-16
category:Authorizenet
---






##  __Authorize and Capture Transaction Overview





Authorizing and Capturing a credit card transaction is one of the most
involved methods included in this integration. This method will create a new
Customer Payment Profile on Authorize.Net and credit card on OrderCloud.io if
one does not already exist, authorize and capture a payment transaction on
Authorize.Net, create a payment on OrderCloud.io tied to the authenticated
userâs current Order (if a payment already exists, simply pass the ID in
`PaymentID`), and also create a transaction tied to that payment.





If the transaction authorization and capture are successful, but there is an
error while creating the payment or transaction on OrderCloud.io, the
Authorize.Net transaction will be voided.









##  __Authorize and Capture Transaction Request





This method requires either CardDetails.CreditCardID (for a previously created
card) or CardDetails.CardNumber and CardDetails.ExpirationDate (to create a
new card).



```


    
    
    POST https://api.ordercloud.io/v1/integrationproxy/authorizenet HTTP/1.1
    Authorization: bearer insert_access_token_here
    Content-Type: application/json; charset=UTF-8
    
    {
    "BuyerID": "...",
    "OrderID": "...",
    "OrderDirection": "outgoing",
    "Amount": 0.00,
    "TransactionType": "authCaptureTransaction",
    "CardDetails": {
    "PaymentID": "...",
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









##  __Authorize and Capture Transaction Response



```


    
    
    HTTP/1.1 200 OK
    Content-Type: application/json; charset=UTF-8
    
    {
    "ChargeStatus": "...",
    "CreditCardID": "...",
    "PaymentID": "...",
    "TransactionID": "...",
    "Messages": [
    {
    "code": "1",
    "description": "..."
    }
    ]
    }
    
    

```









##  __Error Handling





During the authorization and capture process, the Authorize.Net payment
transaction will be created first, followed by the payment and transaction on
OrderCloud.io. In the case that the OrderCloud.io steps fail, the transaction
will be voided automatically on Authorize.Net.





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

AuthCaptureTransaction.OrderIDRequired

</td>  
<td>

OrderID is required to authorize and capture a credit card.

</td>  
<td>

400

</td> </tr>  
<tr>  
<td>

AuthCaptureTransaction.AmountRequired

</td>  
<td>

Amount is required to authorize and capture a credit card.

</td>  
<td>

400

</td> </tr>  
<tr>  
<td>

AuthCaptureTransaction.BuyerIDRequired

</td>  
<td>

BuyerID is required to authorize and capture a credit card.

</td>  
<td>

400

</td> </tr>  
<tr>  
<td>

AuthCaptureTransaction.CardDetailsRequired

</td>  
<td>

CardDetails.CreditCardID OR CardDetails.CardNumber and
CardDetails.ExpirationDate are required to authorize and capture a credit
card.

</td>  
<td>

400

</td> </tr> </table>







### Authorize.Net Error Response



```


    
    
    HTTP/1.1 200 OK
    Content-Type: application/json
    
    {
    "transactionResponse": {
    "responseCode": "3",
    "authCode": "",
    "avsResultCode": "...",
    "cvvResultCode": "",
    "cavvResultCode": "",
    "transId": "0",
    "refTransID": "",
    "transHash": "...",
    "testRequest": "0",
    "accountNumber": "...",
    "accountType": "",
    "errors": [
    {
    "errorCode": "...",
    "errorText": "..."
    }
    ],
    "transHashSha2": ""
    },
    "refId": "...",
    "messages": {
    "resultCode": "Error",
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

responseCode

</th>  
<th>

errorCode

</th>  
<th>

errorText

</th>  
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

3

</td>  
<td>

5

</td>  
<td>

A valid amount is required.

</td>  
<td>

Error

</td>  
<td>

E00027

</td>  
<td>

The transaction was unsuccessful.

</td> </tr>  
<tr>  
<td>

3

</td>  
<td>

6

</td>  
<td>

The credit card number is invalid.

</td>  
<td>

Error

</td>  
<td>

E00027

</td>  
<td>

The transaction was unsuccessful.

</td> </tr>  
<tr>  
<td>

3

</td>  
<td>

7

</td>  
<td>

Credit card expiration date is invalid.

</td>  
<td>

Error

</td>  
<td>

E00027

</td>  
<td>

The transaction was unsuccessful.

</td> </tr>  
<tr>  
<td>

3

</td>  
<td>

8

</td>  
<td>

The credit card has expired.

</td>  
<td>

Error

</td>  
<td>

E00027

</td>  
<td>

The transaction was unsuccessful.

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





If an incorrect `OrderID` was provided:



```


    
    
    HTTP/1.1 404 Not Found
    Content-Type: application/json
    
    {
    "Errors": [
    {
    "ErrorCode": "NotFound",
    "Message": "Order not found: 3456",
    "Data": null
    }
    ]
    }
    
    

```





