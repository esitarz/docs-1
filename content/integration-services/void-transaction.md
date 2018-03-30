---
Title: Authorizenet: Void Transaction
author: OrderCloud.io 
Date: 2018-03-19 15:32:44.250255
Category: Integration Services
Tags: authorizenet
---


##  __Void Transaction Overview

Though this method is used most commonly by other methods when certain actions
fail, it can also be called directly through the integration. This method will
void a previous transaction on Authorize.Net, then create a transaction tied
to the original payment on OrderCloud.io.

##  __Void Transaction Request

This method requires either CardDetails.CreditCardID (for a previously created
card) or CardDetails.CardNumber and CardDetails.ExpirationDate (to create a
new card). It also requires CardDetails.PaymentID referencing the previously
created payment being voided.

##  __Void Transaction Response

##  __Error Handling

Errors will return the exact response directly from the Authorize.Net or
OrderCloud.io endpoint that failed. However, if any required fields are
missing, a 400 error will be returned before any of the update process is
executed.

### Validation Response

In the case that a required field is missing from your request, the following
response will be returned containing a unique ErrorCode and Message, as well
as the request body sent during the call. The possible ErrorCodes and Messages
are listed below.  
  

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

VoidTransaction.OrderIDRequired

</td>  
<td>

OrderID is required to void a transaction.

</td>  
<td>

400

</td> </tr>  
<tr>  
<td>

VoidTransaction.PaymentIDRequired

</td>  
<td>

CardDetails.PaymentID or refTransId (optional) is required to void a
transaction.

</td>  
<td>

400

</td> </tr>  
<tr>  
<td>

VoidTransaction.BuyerIDRequired

</td>  
<td>

BuyerID is required to void a transaction.

</td>  
<td>

400

</td> </tr>  
<tr>  
<td>

VoidTransaction.CardDetailsRequired

</td>  
<td>

CardDetails.CreditCardID OR CardDetails.CardNumber and
CardDetails.ExpirationDate are required to void a transaction.

</td>  
<td>

400

</td> </tr> </table>

### OrderCloud.io Error Response

If an incorrect `BuyerID` was provided:

If an incorrect `CardDetails.CreditCardID` was provided:

If an incorrect `CardDetails.PaymentID` was provided:

If an incorrect `OrderID` was provided:
