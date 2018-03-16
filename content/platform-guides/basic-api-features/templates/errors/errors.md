

## __Overview

OrderCloud.io uses conventional HTTP response codes to indicate success or
failure of an API request. In general, codes in the `2xx` range indicate
success and codes in the `4xx` range indicate an error failed given the
information provided (e.g., a required parameter). Only when something goes
terribly wrong on our end will you receive a `500` response. As long as the
platform is responding you can count on the response body taking a standard
shape.

## __HTTP Status Code Summary

Status Code | Suggested Course of Action  
---|---  
200 - OK | Everything worked as expected. No action required.  
201 - Created | Something has been successfully created. No action required.  
204 - No Content | The server has successfully fulfilled the request. No
action required.  
401 - Unauthorized | The user is not authorized to make a call to the API.
Check that user credentials are valid.  
403 - Forbidden | The user's Security Profile does not have the necessary
roles to make the API call. Update Security Profile to include valid roles for
the call.  
404 - Not Found | The requested resource was not found. A common reason for
this is a bad request.  
500 - Internal Server Error | There was a server-side issue. Please contact us
if you encounter this error code.

