

##  __Authorize Only Transaction Overview

Though a payment is not actually being captured, the Authorize Only
transaction method involves just as many integration calls as Authorizing and
Capturing a credit card transaction. This method will create a new Customer
Payment Profile on Authorize.Net and credit card on OrderCloud.io if one does
not already exist, authorize a payment transaction on Authorize.Net, create a
payment on OrderCloud.io tied to the authenticated user’s current Order (if a
payment already exists, simply pass the ID in `PaymentID`), and also create a
transaction tied to that payment. The main differences are that the payment
will not be captured on Authorize.Net and the transaction on OrderCloud.io
will only reference that authorization.

If the authorization transaction is successful, but there is an error while
creating the payment or transaction on OrderCloud.io, the Authorize.Net
transaction will be voided.

##  __Authorize Only Request

This method requires either CardDetails.CreditCardID (for a previously created
card) or CardDetails.CardNumber and CardDetails.ExpirationDate (to create a
new card).

##  __Authorize Only Response

##  __Error Handling

During the authorization only process, the Authorize.Net payment authorization
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

ErrorCode | Message | Status Code  
---|---|---  
AuthOnlyTransaction.OrderIDRequired | OrderID is required to authorize a
credit card. | 400  
AuthOnlyTransaction.AmountRequired | Amount is required to authorize a credit
card. | 400  
AuthOnlyTransaction.BuyerIDRequired | BuyerID is required to authorize a
credit card. | 400  
AuthOnlyTransaction.CardDetailsRequired | CardDetails.CreditCardID OR
CardDetails.CardNumber and CardDetails.ExpirationDate are required to
authorize a credit card. | 400  
  
### Authorize.Net Error Response

responseCode | errorCode | errorText | resultCode | message.code |
message.text  
---|---|---|---|---|---  
3 | 5 | A valid amount is required. | Error | E00027 | The transaction was
unsuccessful.  
3 | 6 | The credit card number is invalid. | Error | E00027 | The transaction
was unsuccessful.  
3 | 7 | Credit card expiration date is invalid. | Error | E00027 | The
transaction was unsuccessful.  
3 | 8 | The credit card has expired. | Error | E00027 | The transaction was
unsuccessful.  
  
### OrderCloud.io Error Response

If an incorrect `BuyerID` was provided:

If an incorrect `CardDetails.CreditCardID` was provided:

If an incorrect `OrderID` was provided:

