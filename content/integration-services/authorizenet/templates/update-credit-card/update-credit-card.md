

##  __Update Credit Card Overview

When a customer within your buyer application updates a credit card, the
integration endpoint can be called in order to update that card on
OrderCloud.io as well as Authorize.Net. The Customer Payment Profile will be
updated on Authorize.Net, followed by the card being patched on OrderCloud.io.
If either step fails, all changes will be reverted in order to keep each
system in sync. If the card is shared, meaning `Shared` was set to `true` when
the card was created, `Shared` must be passed as `true` when updating.

##  __Update Credit Card Request

##  __Update Credit Card Response

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

ErrorCode | Message | Status Code  
---|---|---  
UpdateCreditCard.CreditCardIDRequired | CardDetails.CreditCardID is required
to update a credit card. | 400  
  
### Authorize.Net Error Response

resultCode | message.code | message.text  
---|---|---  
Error | E00013 | Card Number is invalid.  
Error | E00013 | Expiration Date is invalid.  
Error | E00027 | The credit card has expired.  
  
### OrderCloud.io Error Response

If an incorrect `BuyerID` was provided:

If an incorrect `CardDetails.CreditCardID` was provided:

