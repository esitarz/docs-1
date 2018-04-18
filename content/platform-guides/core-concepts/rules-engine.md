---
title: Core Concepts: Rules Engine
date: 2018-04-16
category: Core Concepts
---


## Introduction

Whatâs a rules engine? Itâs a system that executes rules. Okay...so
whatâs a rule? In its simplest form, itâs an if-then statement that is
provided from the outside, rather than being âbaked inâ to the engine
itself. In the case of OrderCloud.io, weâll define the âthensâ (starting
with âorder requires approvalâ) and allow you to define the âifsâ via
custom **logic expressions**. Effectively, weâre going to allow you to
extend platform behavior in much the same way xp allows you to extend the data
model.

Here is an example:

Say you want every order over $200 with some specific xp value to require
approval from a manager. You would first create a UserGroup containing all
approving managers, then create a new ApprovalRule, set the ApprovingGroupID,
and set the Expression to this:



```


    
    
    order.Total > 200 and order.xp.MyCustomProperty = "XYZ""
    

```

##  Supported Operations

  * `order` supports the same properties as the Order model returned from /orders API endpoints, including xp.
  * `= `, `< `, `>`, `<=`, `>=` comparison operators are supported.
  * `and`, `or` and `not` logical operators are supported
  * `+`, `-`,`*` and `/` mathematical operators are supported
  * String values must be enclosed in single quotes.
  * Date values must be enclosed in # symbols, i.e #5/15/2016#
  * Parentheses may be used to enclose sub-expressions and control order of execution.

## Line Item Control

What about line items? Glad you asked, because which products are being
purchased, in what quantities, charged against which cost centers, etc, are
very common in the world of approval rules. But line items are a collection,
so we turn to aggregate functions to inspect them. Hereâs how you would
require approval on all orders over $200 charged to cost center ABC:



```


    
    
    order.Total > 200 and items.any(CostCenter = "ABC"")
    

```

Thatâs pretty powerful, but itâs more likely that you only care about the
_subtotal_ of just the line items matching your CostCenter condition. For this
you can use the `items.total` function:



```


    
    
    items.total(CostCenter = "ABC") > 200
    

```

The condition inside the function (called a filter) can be more complex and
contain `and`, `or`, etc. just like other parts of the expression:



```


    
    
    items.quantity(ProductID = "P1" or ProductID = "P2") > 5
    

```

It also has access to a special filter that allows you check whether a product
is in a certain category:



```


    
    
    items.any(product.incategory("Toys""))
    

```



`items`

supports a total of four functions:



  * `items.any` (true if any item matches filter)
  * `items.all` (true if all item matches filter)
  * `items.quantity` (compare result to a number)
  * `items.total` (compare result to a dollar amount)

and one special filter:


  * `product.incategory('mycustomcategory')`

## ComplexApprovals

Speaking of functions, there is one defined on `order`:



```


    
    
    order.approved("id_of_some_other_rule"")
    

```

This oneâs powerful, because it allows you to set up multi-level approval
workflows by chaining rules together. For example, in a larger organization,
getting the approval from a department manager might not be enough, and a
higher-level VP must also sign off.

All valid elements of rule expressions can be mixed & matched as needed,
allowing for very sophisticated rules to be supported:



```


    
    
    (order.Total > 20 and order.approved("rule_id_1")) or (not item.any(ProductID = "QQQ") and approved("rule_id_2"))
    

```

A word of caution: Rules are easy to write and very powerful, but can be very
tricky to debug when they donât work quite like you thought they would.
Donât get more fancy with them than you need to. As always, weâre here to
help if you need guidance.

##  Where to go from here?

You can also leverage the power of the rules engine to create custom
Promotions. Both the promotion EligibleExpression and ValueExpression accept
expressions just like the ones described above. Here are some other things we
may leverage the rules engine for in the future:

  * Custom validation (upon creating/editing things)
  * Time-based approval rules (aggregated totals over past week/month/quarter, etc.)
  * Applying discounts/markups
  * Replenish inventory
  * Fire off a notification via webhooks

Weâd love to get your thoughts on these ideas. Look for significant
enhancements to the rules engine and new applications of it in the months
ahead.

