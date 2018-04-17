---
title: Basic Api Features: Sorting
date: 2018-04-16
category:Basic Api Features
---






## __Overview





Most OrderCloud.io Resources include a method for listing items from that
Resource. The results returned from a list method have a default sort order,
but you can also specify a sort order. Properties marked as âSortableâ in
the API Reference can be sorted on.









## __Sorting





Perhaps you want to sort the results by the Last Name of the person who placed
an order. To do this you can simply include the `sortBy` parameter for the
field you would like to sort by.



```


    
    
    GET https://api.ordercloud.io/me/orders/incoming?sortBy=!LastName HTTP/1.1
    

```









##  __Combining Queries





Sorting can be mixed and matched with Searching and Filtering to give you
ultimate control when defining what is returned from a list.





