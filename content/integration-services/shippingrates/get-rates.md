---
title: Shipping Rates: Get Rates
date: 2018-04-16
category: Shipping Rates
---


##  Get Rates Overview

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
  * `ApplyShipping` is not set to true on the Product's Price Schedule

Also, if a `ShipWeight` (in lbs.) is not set on a Product, a weight of `0`
will be used when calculating rates, resulting in an inaccurate estimate.

##  Get Rates Request



```
    POST https://api.ordercloud.io/v1/integrationproxy/Shipping Rates HTTP/1.1
    Authorization: bearer insert_access_token_here
    Content-Type: application/json; charset=UTF-8
```

```    
{
    "BuyerID": "...",
    "TransactionType": "GetRates",
    "OrderID": "..."
}
```

##  Get Rates Response



```
    HTTP/1.1 200 OK
    Content-Type: application/json; charset=UTF-8
```

```    
{
    "Shipments": [
        {
            "Weight": 10,
            "ShipFromAddressID": "1234",
            "ShipToAddressID": "2345",
            "LineItemIDs": [
                "1",
                "2",
                "3"
            ],
            "Rates": [
                {
                    "Price": 6,
                    "Description": "UPS Standard"
                },
                {
                    "Price": 20,
                    "Description": "UPS Next Day Air"
                },
                {
                    "Price": 5,
                    "Description": "USPS Priority"
                },
                {
                    "Price": 15,
                    "Description": "USPS First-Class"
                }
            ]
        }
    ]
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
```

```    
{
    "ErrorCode": "...",
    "Message": "...",
    "Data": {
        "...Request Body...": null
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

</td> </tr>  
<tr>  
<td>

Shipping RatesValidation.LineItemsRequired

</td>  
<td>

At least one line item is required to get shipping rates.

</td>  
<td>

400

</td> </tr> </table>



