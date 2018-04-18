---
title: Basic API Features: Conventions
date: 2018-04-16
category: Basic API Features
---


## Overview

With few exceptions, the OrderCloud.io API adheres to a RESTful architectural
style. URIs, HTTP verbs, headers, payloads, and response codes all follow
consistent and predictable patterns. This guide will outline conventions that
permeate the entire platform.

##  SSL Everywhere

API access is only allowed via HTTPS; connections on port 80 are refused
entirely. This simplifies the token-based authentication.

##  JSON Everywhere

UTF-8 encoded JSON is currently the only supported data format for both
request and response payloads.

##  Date Format

Dates/times returned in the API are in UTC time and conform to [ISO
8601](http://en.wikipedia.org/wiki/ISO_8601).

##  OAuth 2

OrderCloud API authentication is based on the [OAuth 2
specification](http://tools.ietf.org/html/rfc6749) and supports four different
workflows, or, in OAuth terms, grant types. Check out our workflows guide to
learn more.

##  Writeable IDs

Writable IDs can be extremely useful for back-office integrations. They can
potentially eliminate the need for a mapping middleware layer.

Most resources that map to an entity of some sort (Orders, Users, Addresses,
etc.) contain an ID that is optionally writable on creation or update. If you
do not pass one, one will be auto-generated and returned in the response, and
will be guaranteed to be unique. If you choose to pass an ID, you are
responsible for ensuring uniqueness. Things that live under the context of a
single Buyer need only be unique within that context. Things that are shared
(such as products) must be unique across the entire Admin organization.

##  Error Handling

For all unsuccessful requests, we attempt to return the [most appropriate HTTP
status in the 400
range](http://en.wikipedia.org/wiki/List_of_HTTP_status_codes#4xx_Client_Error).
Only when something goes terribly wrong on our end will you get a 500
response. And so long as our platform is responding (i.e. returing anything in
the 4xx range or 500), you can count on the response body taking a standard
shape.

