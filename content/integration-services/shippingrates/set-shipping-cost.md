---
title: Shipping Rates: Set Shipping Cost
date: 2018-04-16
category: Shipping Rates
---


##  Set Shipping Cost Overview

Once a user selects their desired shipper(s) for their order, the
`ShippingCost` on the Order can be set via the _SetShippingCost_ method. This
method will patch the Order with the provided `ShippingCost` value and return
the updated Order.

##  Set Shipping Cost Request



```


    
    
    POST https://api.ordercloud.io/v1/integrationproxy/Shipping Rates HTTP/1.1
    Authorization: bearer insert_access_token_here
    Content-Type: application/json; charset=UTF-8
    
    {
    "BuyerID": "...",
    "TransactionType": "SetShippingCost",
    "OrderID": "...",
    "ShippingCost": 6
    }
    
    

```

##  Set Shipping Cost Response



```


    
    
    HTTP/1.1 200 OK
    Content-Type: application/json; charset=UTF-8
    
    {
    "ID": "12345",
    "Type": "Standard",
    "FromUserID": "3456",
    "FromUserFirstName": "Sample",
    "FromUserLastName": "User",
    "BillingAddressID": null,
    "BillingAddress": null,
    "ShippingAddressID": â7654â,
    "Comments": null,
    "LineItemCount": 3,
    "Status": "Unsubmitted",
    "DateCreated": "2016-11-09T19:20:44.19+00:00",
    "DateSubmitted": null,
    "DateApproved": null,
    "DateDeclined": null,
    "DateCanceled": null,
    "DateCompleted": null,
    "Subtotal": 30,
    "ShippingCost": 6,
    "TaxCost": 0,
    "PromotionDiscount": 0,
    "Total": 36,
    "IsSubmitted": false,
    "xp": null
    }
    
    

```

##  Error Handling

### Validation Response

In the case that a required field is missing from your request or there are
any issues with your Order, the following response will be returned containing
a unique ErrorCode and Message, as well as the request body sent during the
call. The possible ErrorCodes and Messages are listed below.



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

Shipping RatesValidation.BuyerIDRequired

</td>  
<td>

BuyerID is required to get shipping rates.

</td>  
<td>

400

</td> </tr>  
<tr>  
<td>

Shipping RatesValidation.OrderIDRequired

</td>  
<td>

OrderID is required to get shipping rates.

</td>  
<td>

400

</td> </tr> </table>



