---
title: Basic Api Features: Searching
date: 2018-04-16
category:Basic Api Features
---






## __Overview





Searching data client side can be fine for smaller sets of data but can
quickly become unwieldy with large sets of data. To address this issue our API
supports server side search queries that do all of the heavy lifting for you.









##  __Searching





For open-ended, Google-esque searches, simply provide a search term.

Request

```


    
    
    GET https://api.ordercloud.io/buyers/xyz/users?search=smith HTTP/1.1
    

```





This will return all results containing "smith", including "Smith",
"Smithers", and "McSmith". The fields searched include `FirstName`,`LastName`,
and `UserName`. (This of course varies from endpoint to endpoint. View each
endpoint's documentation for specific details). Fields marked âSearchableâ
in the API reference will be searched.





You can optionally specify which fields (of the searchable fields available)
are searched by providing a `searchOn` parameter for any field available on
the resource you're searching.



```


    
    
    GET https://api.ordercloud.io/buyers/xyz/users?search=smith&searchOn=LastName,UserName HTTP/1.1
    

```









##  __Combining Queries





Searching can be mixed and matched with Sorting and Filtering to give you
ultimate control when defining what is returned from a list.





