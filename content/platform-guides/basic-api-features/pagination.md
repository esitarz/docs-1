---
title: Basic API Features: Pagination
date: 2018-04-16
Category: Basic API Features
---


## Overview

Most OrderCloud.io Resources include a method for listing items from that
Resource. These resources can potentially include thousands of items so
restricting the data that is returned from such a request is not only
practical but necessary. OrderCloud.io offers server-side pagination that
partitions the data returned from these requests into manageable chunks to
optimize client-side performance

##  Listing

A request to list a resource will return an object with two values: `Meta` and
`Items`. The `Meta` value returns important information regarding your query,
such as total results, how many results are shown in the Items array, how many
more pages of results there are, and what page you are currently on. The Items
array stores the actual results of the resource you are querying.



```


    
    
    HTTP/1.1 201 CREATED
    Content-Type: application/json; charset=UTF-8
    
    {
    "Meta": {
    "Page": 1,
    "PageSize": 20,
    "TotalCount": 25,
    "TotalPages": 2,
    "ItemRange": [1, 20]
    },
    "Items": ["..."]
    }
    
    

```

Lists default to 20 items per page, but you can set the `pageSize` up to 100.
If you have more results than the page count, you will have multiple pages.
You can use the `Page` and `PageSize` values from the `Meta` object to specify
the page (starting at 1) and items per page. Note that unlike the page
parameter, `ItemRange` values are zero-based.

