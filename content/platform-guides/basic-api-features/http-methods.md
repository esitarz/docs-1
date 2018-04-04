---
Title: Http Methods
author: OrderCloud.io 
Date: 2018-03-19 15:32:44.250255
Tags: basic api features
---


## __Overview

A resource is a set of endpoints used to interact with an object of that same
name. OrderCloud.io adheres to RESTful conventions in its usage of HTTP verbs.
You can expect a subset of the following methods to exist on every Resource.

## __HTTP Methods  
  
<table>  
<tr>  
<th>

OrderCloud.io Verb

</th>  
<th>

HTTP Verb

</th>  
<th>

Meaning

</th>  
<th>

Example

</th> </tr>  
<tr>  
<td>

GET

</td>  
<td>

GET

</td>  
<td>

Returns a specific item

</td>  
<td>

Get a single address

</td> </tr>  
<tr>  
<td>

CREATE/REPLACE

</td>  
<td>

PUT

</td>  
<td>

Create or replace an item, you provide a unique ID

</td>  
<td>

Create address ABC, overwriting it if it already exists

</td> </tr>  
<tr>  
<td>

UPDATE

</td>  
<td>

PATCH

</td>  
<td>

Use it for updating items

</td>  
<td>

Update the name on an address by providing the new name

</td> </tr>  
<tr>  
<td>

LIST

</td>  
<td>

GET

</td>  
<td>

Returns a list of items

</td>  
<td>

Get a list of addresses

</td> </tr>  
<tr>  
<td>

CREATE

</td>  
<td>

POST

</td>  
<td>

Creates a new item, we generate a unique ID if no ID is provided

</td>  
<td>

Create a new address

</td> </tr>  
<tr>  
<td>

DELETE

</td>  
<td>

DELETE

</td>  
<td>

Deletes an item

</td>  
<td>

Delete address ABC from the database

</td> </tr> </table>

