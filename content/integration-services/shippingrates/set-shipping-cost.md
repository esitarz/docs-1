---
title: Set Shipping Cost
author: OrderCloud.io 
Date: 2018-03-16 12:35:35.774570
slug: /docs/content/integration-services/shippingrates set-shipping-cost
---


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

</td> </tr> </table>

