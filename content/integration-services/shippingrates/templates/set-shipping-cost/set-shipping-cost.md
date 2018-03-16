

##  __Set Shipping Cost Overview

Once a user selects their desired shipper(s) for their order, the
`ShippingCost` on the Order can be set via the _SetShippingCost_ method. This
method will patch the Order with the provided `ShippingCost` value and return
the updated Order.

##  __Set Shipping Cost Request

##  __Set Shipping Cost Response

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

