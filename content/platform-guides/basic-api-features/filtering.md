---
Title: Filtering
author: OrderCloud.io 
Date: 2018-03-19 15:32:44.250255
Tags: basic api features
---


## __Overview

Most OrderCloud.io Resources include a method for listing items from that
Resource. The items from such a call could very well be in the thousands so
being able to narrow down the range of the items returned is critical, this
can be done with the use of filters.

## __Filtering On XP

Let's examine a common scenario of filtering on an extended property (XP)
field. Suppose our XP field looks like this:

We can use dot notation to access deeply nested values. The following call
will return all buyers with team name "Tigers"

## __Fuzzy Searches

Fuzzy matches are supported using the `*` wildcard character.

This will return both "John Smith" and "Johnny McSmooth".

## __Logical OR

You can also use `|` as a logical OR.

This will return "John Smith", "Johnny Jones", and "John Johnson". Maybe you
want "John Smith" but not "John Jones".

## __Negate and Logical AND

You can negate your conditions by prefixing them with `!`, and logically `AND`
them together by simply providing the same parameter multiple times.

This will return all users _except_ those with last name "Smith" or "Jones".

## __Comparison Operators

Dates and numeric values support `>` (greater than) and `<` (less than)
prefixes.

For a more advanced example, let's say you want users whose ID is the range of
0 to 9 inclusive. Ranges are not directly supported, but you can use the
existing features to achieve this.

Of course that's not going to be feasible if the range is very large or you're
dealing with floating-point numbers. A better way would be to leverage `>` and
`<`, but we want the range to be inclusive, and there are no `>=` or `<=`
operators. We can however leverage the `!` operator.

Here we're saying "give me all users whose ID is not less than 0 and not
greater than 9", which is effectively equivalent to our 0-9 range.

## __Performance Considerations

Your data is highly indexed for fast retrieval using any of the methods above,
including deep XP object graphs. However, there are a few things to keep in
mind to keep search and listing functionality efficient. Filters with many
`OR` conditions or with values that start with the `*` wildcard character may
be particularly performance-sensitive. The larger the set of data, the more
likely you are to notice any performance impact. It pays to know the data
model well, and use grouping constructs like User Groups and Categories
effectively.

## __Combining Queries

Filtering can be mixed and matched with Searching and Sorting to give you
ultimate control when defining what is returned from a list.

