---
title: Authorizenet: Prior Authorization Capture Transaction
date: 2018-04-16
category:Authorizenet
---






##  __Prior Authorization Capture Transaction Overview





In the case that Authorize Only was previously used for a payment, Prior
Authorization Capture Transaction can be used to actually capture the payment.
This method will first capture the payment on Authorize.Net, then create an
additional transaction on the previously created payment on OrderCloud.io.





If the capture transaction is successful, but there is an error while creating
the transaction on OrderCloud.io, the Authorize.Net transaction will be
voided.









##  __Prior Authorization Capture Transaction Request



```


    
    
    POST https://api.ordercloud.io/v1/integrationproxy/authorizenet HTTP/1.1
    Authorization: bearer insert_access_token_here
    Content-Type: application/json; charset=UTF-8
    
    {
    "BuyerID": "...",
    "OrderID": "...",
    "OrderDirection": "outgoing",
    "TransactionType": "priorAuthCaptureTransaction",
    "CardDetails": {
    "PaymentID": "..."
    }
    }
    
    

```









##  __Prior Authorization Capture Transaction Response



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





During the prior authorization capture process, the Authorize.Net payment
authorization will be captured, followed by the creation of the transaction on
OrderCloud.io. In the case that the OrderCloud.io step fails, the transaction
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

PriorAuthCaptureTransaction.OrderIDRequired

</td>  
<td>

OrderID is required to capture a prior authorization.

</td>  
<td>

400

</td> </tr>  
<tr>  
<td>

PriorAuthCaptureTransaction.PaymentIDRequired

</td>  
<td>

CardDetails.PaymentID is required to capture a prior authorization.

</td>  
<td>

400

</td> </tr>  
<tr>  
<td>

PriorAuthCaptureTransaction.BuyerIDRequired

</td>  
<td>

BuyerID is required to capture a prior authorization.

</td>  
<td>

400

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





If an incorrect `CardDetails.PaymentID` was provided:



```


    
    
    HTTP/1.1 404 Not Found
    Content-Type: application/json
    
    {
    "Errors": [
    {
    "ErrorCode": "NotFound",
    "Message": "Payment not found: 2345",
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





