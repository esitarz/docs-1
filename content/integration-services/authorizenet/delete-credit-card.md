---
title: Authorize.Net: Delete Credit Card
date: 2018-04-16
category: Authorize.Net
---


##  Delete Credit Card Overview

When a customer within your buyer application deletes a credit card, the **Delete Credit Card Overview** integration endpoint can be called in order to delete that card on OrderCloud.io as well as Authorize.Net. The Customer Payment Profile will be removed on Authorize.Net, followed by the card being deleted on OrderCloud.io.

If either call fails, the response from that particular call will be returned.
Otherwise, the response will simply be a `204` `No Content` HTTP status. If the card is shared, meaning `Shared` was set to `true` when the [card was created]({filename}create-credit-card.md), `Shared`
must be passed as `true` when deleting.

###  Delete Credit Card Request

```
    POST https://api.ordercloud.io/v1/integrationproxy/Authorize.Net HTTP/1.1
    Authorization: bearer insert_access_token_here
    Content-Type: application/json; charset=UTF-8
```

```    
{
    "BuyerID": "...",
    "TransactionType": "deleteCreditCard",
    "CardDetails": {
        "CreditCardID": "...",
        "Shared": false
    }
}
```

###  Delete Credit Card Response


```  
    HTTP/1.1 204 No Content
    Content-Type: application/json; charset=UTF-8
```

##  Error Handling

During the credit card delete process, the Authorize.Net Customer Payment
Profile will first be deleted. Next, the card will be deleted on
OrderCloud.io.

Errors will return the exact response directly from the Authorize.Net or
OrderCloud.io endpoint that failed. However, if any required fields are
missing, a 400 error will be returned before any of the update process is
executed.

### Validation Response

In the case that a required field is missing from your request, the following
response will be returned containing a unique `ErrorCode` and `Message`, as well as the request body sent during the call. The possible `ErrorCodes` and `Messages` are listed below.



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

DeleteCreditCard.CreditCardIDRequired

</td>  
<td>

CardDetails.CreditCardID is required to delete a credit card.

</td>  
<td>

400

</td> </tr> </table>



### OrderCloud.io Error Response

If an incorrect `BuyerID` was provided:

```  
    HTTP/1.1 404 Not Found
    Content-Type: application/json
```

```    
{
    "Errors": [
        {
            "ErrorCode": "NotFound",
            "Message": "Buyer not found: 1234",
            "Data": null
        }
    ]
}
```

If an incorrect `CardDetails.CreditCardID` was provided:



```
    HTTP/1.1 404 Not Found
    Content-Type: application/json
```
```    
{
    "Errors": [
        {
            "ErrorCode": "NotFound",
            "Message": "Credit Card not found: 2345",
            "Data": null
        }
    ]
}
```

