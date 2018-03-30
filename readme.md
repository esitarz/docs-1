# OrderCloud.io Documentation

This is the repository for the [OrderCloud.io]() platform's [documentation site](). We use [pelican]() to generate this site. 

## Contributions

We welcome additions, edits, and corrections to our documentation, with a few caveats.

First, our API documentation is generated based on our platform code -- reflection is used *heavily*. So, if there is a change you would like made to our [API Reference content](), please do not edit the documentation here, but instead raise a [ticket]() in this repo.

Second, all content changes or additions require a pull request to be approved by the OrderCloud maintainers. We may decline a pull request with comments asking for the content to align more closely with our [style guide](), or just decline changes.

### How to Contribute

All the documentation content can be found in the [`content`]() folder as markdown files. They are organized into folders by category.

#### Docs `Content` Folder Structure

| Folder                  | Description                                                                                                                 |
|:------------------------|:----------------------------------------------------------------------------------------------------------------------------|
| `api-reference`         | Contains automatically generated markdown files from the platform's generated API docs. **Please do not edit these files.** |
| `frameworks-and-sdks`   | Documentation pertaining to frameworks and SDKs for the OrderCloud.io API platform.                                         |
| `images`                | Image directory for documentation. Loosely organized by category sub-folders.                                               |
| `integration-services ` | Documentation for officially supported third party integrations for the OrderCloud.io API platform.                         |
| `pages`                 | A Pelican infrastructure-related directory, this is currently used for landing page content.                                |
| `platform-guides  `     | Documentation to get a user up and running with OrderCloud.io quickly, including recommended best practices.                |

#### Documentation File Structure

We use largely [Github-flavored Markdown](). Each markdown file needs a header block, like the following:

```
---
Title: Angularjs: Application Files
Author: OrderCloud.io
Date: 2018-03-19 15:32:44.250255
Category: Frameworks And Sdks
Tags: angularjs
---
```

For more information about formatting Markdown files for Pelican, see the [Pelican Documentation]()
