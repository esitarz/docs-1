

##  __Get Rates Overview

The first method available within the OrderCloud.io Shipping Rates integration
is _GetRates_. This method will group together Line Items on an Order based on
the Line Items' `ShippingAddress` and the Line Item Products'
`ShipFromAddressID`, calculate the total weight of each shipment based on the
included Products' `ShipWeight`, and obtain shipping rate estimates from the
carriers selected in your integration configuration.

As mentioned in the Catalog Configuration, Line Items will not be included in
the shipping rate calculation for the following reasons:

  * No `ShippingAddress` is set on the Line Item
  * No `ShipFromAddressID` is set on the Product
  * `ApplyShipping` is not set to true on the Product’s Price Schedule

Also, if a `ShipWeight` (in lbs.) is not set on a Product, a weight of `0`
will be used when calculating rates, resulting in an inaccurate estimate.

##  __Get Rates Request

##  __Get Rates Response

##  __Error Handling

### Validation Response

In the case that a required field is missing from your request or there are
any issues with your Order, the following response will be returned containing
a unique ErrorCode and Message, as well as the request body sent during the
call. The possible ErrorCodes and Messages are listed below.  
  

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

ShippingRatesValidation.BuyerIDRequired

</td>  
<td>

BuyerID is required to get shipping rates.

</td>  
<td>

400

</td> </tr>  
<tr>  
<td>

ShippingRatesValidation.OrderIDRequired

</td>  
<td>

OrderID is required to get shipping rates.

</td>  
<td>

400

</td> </tr>  
<tr>  
<td>

ShippingRatesValidation.LineItemsRequired

</td>  
<td>

At least one line item is required to get shipping rates.

</td>  
<td>

400

</td> </tr> </table>

