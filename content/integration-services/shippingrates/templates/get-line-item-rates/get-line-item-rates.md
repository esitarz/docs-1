

##  __Get Line Item Rates Overview

The next method available within the OrderCloud.io Shipping Rates integration
is _GetLineItemRates_. This method will obtain shipping rate estimates from
the carriers selected in your integration configuration for each individual
Line Item in your order based on the item’s product weight, but regardless of
the item’s `ShippingAddress` and `ShipFromAddressID`.

As mentioned in the Catalog Configuration, Line Items will not be included in
the shipping rate calculation for the following reasons:

  * No `ShippingAddress` is set on the Line Item
  * No `ShipFromAddressID` is set on the Product
  * `ApplyShipping` is not set to true on the Product’s Price Schedule

Also, if a `ShipWeight` (in lbs.) is not set on a Product, a weight of `0`
will be used when calculating rates, resulting in an inaccurate estimate.

##  __Get Line Item Rates Request

##  __Get Line Item Rates Response

##  __Error Handling

### Validation Response

In the case that a required field is missing from your request or there are
any issues with your Order, the following response will be returned containing
a unique ErrorCode and Message, as well as the request body sent during the
call. The possible ErrorCodes and Messages are listed below.

ErrorCode | Message | Status Code  
---|---|---  
ShippingRatesValidation.BuyerIDRequired | BuyerID is required to get shipping
rates. | 400  
ShippingRatesValidation.OrderIDRequired | OrderID is required to get shipping
rates. | 400  
ShippingRatesValidation.LineItemsRequired | At least one line item is required
to get shipping rates. | 400

