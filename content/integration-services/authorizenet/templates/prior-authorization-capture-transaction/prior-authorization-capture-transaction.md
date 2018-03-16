

##  __Prior Authorization Capture Transaction Overview

In the case that Authorize Only was previously used for a payment, Prior
Authorization Capture Transaction can be used to actually capture the payment.
This method will first capture the payment on Authorize.Net, then create an
additional transaction on the previously created payment on OrderCloud.io.

If the capture transaction is successful, but there is an error while creating
the transaction on OrderCloud.io, the Authorize.Net transaction will be
voided.

##  __Prior Authorization Capture Transaction Request

##  __Prior Authorization Capture Transaction Response

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

ErrorCode | Message | Status Code  
---|---|---  
PriorAuthCaptureTransaction.OrderIDRequired | OrderID is required to capture a
prior authorization. | 400  
PriorAuthCaptureTransaction.PaymentIDRequired | CardDetails.PaymentID is
required to capture a prior authorization. | 400  
PriorAuthCaptureTransaction.BuyerIDRequired | BuyerID is required to capture a
prior authorization. | 400  
  
### OrderCloud.io Error Response

If an incorrect `BuyerID` was provided:

If an incorrect `CardDetails.PaymentID` was provided:

If an incorrect `OrderID` was provided:

