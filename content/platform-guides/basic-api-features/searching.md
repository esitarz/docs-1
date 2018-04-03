---
Title: Searching
author: OrderCloud.io 
Date: 2018-03-19 15:32:44.250255
Tags: basic api features
---


## __Overview

Searching data client side can be fine for smaller sets of data but can
quickly become unwieldy with large sets of data. To address this issue our API
supports server side search queries that do all of the heavy lifting for you.

## __Searching

For open-ended, Google-esque searches, simply provide a search term.

Request

This will return all results containing "smith", including "Smith",
"Smithers", and "McSmith". The fields searched include `FirstName`,`LastName`,
and `UserName`. (This of course varies from endpoint to endpoint. View each
endpoint's documentation for specific details). Fields marked “Searchable” in
the API reference will be searched.

You can optionally specify which fields (of the searchable fields available)
are searched by providing a `searchOn` parameter for any field available on
the resource you're searching.

## __Combining Queries

Searching can be mixed and matched with Sorting and Filtering to give you
ultimate control when defining what is returned from a list.

