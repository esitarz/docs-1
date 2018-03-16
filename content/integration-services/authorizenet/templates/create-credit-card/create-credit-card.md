

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

##  __Create Credit Card Response

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

ErrorCode | Message | Status Code  
---|---|---  
CreateCreditCard.CardNumberRequired | CardDetails.CardNumber is required to
create a new credit card. | 400  
CreateCreditCard.ExpirationDateRequired | CardDetails.ExpirationDate is
required to create a new credit card. | 400  
  
### Authorize.Net Error Response

resultCode | message.code | message.text  
---|---|---  
Error | E00013 | Card Number is invalid.  
Error | E00013 | Expiration Date is invalid.  
Error | E00027 | The credit card has expired.  
  
### OrderCloud.io Error Response

If an incorrect `BuyerID` was provided:

