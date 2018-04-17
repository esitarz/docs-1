---
title: Basic Api Features: Errors
date: 2018-04-16
category:Basic Api Features
---






## __Overview





OrderCloud.io uses conventional HTTP response codes to indicate success or
failure of an API request. In general, codes in the `2xx` range indicate
success and codes in the `4xx` range indicate an error failed given the
information provided (e.g., a required parameter). Only when something goes
terribly wrong on our end will you receive a `500` response. As long as the
platform is responding you can count on the response body taking a standard
shape.









##  __HTTP Status Code Summary





  
<table>  
<tr>  
<th>

Status Code

</th>  
<th>

Suggested Course of Action

</th> </tr>  
<tr>  
<td>

200 - OK

</td>  
<td>

Everything worked as expected. No action required.

</td> </tr>  
<tr>  
<td>

201 - Created

</td>  
<td>

Something has been successfully created. No action required.

</td> </tr>  
<tr>  
<td>

204 - No Content

</td>  
<td>

The server has successfully fulfilled the request. No action required.

</td> </tr>  
<tr>  
<td>

401 - Unauthorized

</td>  
<td>

The user is not authorized to make a call to the API. Check that user
credentials are valid.

</td> </tr>  
<tr>  
<td>

403 - Forbidden

</td>  
<td>

The user's Security Profile does not have the necessary roles to make the API
call. Update Security Profile to include valid roles for the call.

</td> </tr>  
<tr>  
<td>

404 - Not Found

</td>  
<td>

The requested resource was not found. A common reason for this is a bad
request.

</td> </tr>  
<tr>  
<td>

500 - Internal Server Error

</td>  
<td>

There was a server-side issue. Please contact us if you encounter this error
code.

</td> </tr> </table>







