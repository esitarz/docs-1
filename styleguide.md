

## Style Guide 

HTTP Requests

If you're showing an HTTP request/response, and want to include the headers, the reccomended way to display it is the following:

Request:

Request URL and headers are a separate code block from the request body.

    {http verb} {request url} {http version}
    {headers and auth}


    :::json
    {request body}


Response:

## Pelican Cheat Sheet

### Linking to internal content

If you are linking to another article within the Docs site, use the following and link to the article in the /content folder, not the /output folder or the live URL page.

    [I'm A Link!]({filename}folder/article.md)

Note that the root that this is using is the /content folder, not the repo root.

To include an image, pdf, or other sort of file, the trick is very simular.

    ![Image Alt Text]({attach}images/image.jpg)

Using the {attach} means that the file attached will be put in the same directory as the article in the output directory.