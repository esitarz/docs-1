---
title: Core Concepts: Assignments
date: 2018-04-16
category: Core Concepts
---


## Overview

There are basic principles around how assignments work that are critical to
understanding our data model and more importantly how the data model can be
applied to solve the most complex ordering scenarios.

  * Assignments are used to define relationships
  * Assignments are inclusive
  * Assignments can be made at different levels depending on the resource
  * Assignments may include configuration data
  * Assignments cascade down higher levels to the individual user (except pricing)
  * Assignments are many to many

## Assignments are Used to Define Relationships

When you are saving an assignment you are creating a relationship between a
single resource (address, spending account, etc.) and a buyer party(user, user
group, or buyer company). There is one exception to this binary rule, which is
product assignment. The product assignment is a three-way association between
a product, a buyer party and a price schedule.

##  Assignments are Inclusive

When a buyer user is created they exist in a vacuum. The user will not have
access to any objects until an assignment is made to them directly, or through
a higher level party assignment.

##  Assignments Can be Made at Different Levels

Assignments can be made to either the entire buyer company, a specific group
of users (UserGroup) within that buyer company or for some resources a single
buyer user.

You may notice that some assignments contain configuration options. These
options allow you to provide additional information about the assignment. For
example, when assigning an address to a user, you can set IsShipping &
IsBilling, these properties control whether the address can be used as a
shipping and/or billing address on an order.

##  Assignments Cascade Down Higher Levels to the Individual User

When the platform is looking for what a given buyer user has access to, it is
checking for assignments. If an assignment is made to a buyer then all the
users that exist in that buyer organization have access to the assigned
object. The same principle applies to user groups and their constituent users.
Regardless of where an assignment is saved, all of these objects are presented
to the buyer user seamlessly and in a very flat structure.

The three-way product assignment is the exception to this, in that case the
most specific pricing assignment will apply. For example, if you have a
product assignment at the buyer level, but you would like a specific group of
users to have different pricing, you could make an additional product
assignment that included a UserGroupID and users assigned to that group would
no longer see the buyer level pricing.

The scenario youâll want to avoid is a user with multiple product
assignments of the same specificity party level (e.g. a user belonging to two
user groups, each with different product assignments). While the platform
wonât prohibit you from making these potentially problematic assignments,
the pricing returned for any user belonging to multiple pricing groups will
always be indeterminate.

##  Assignments are Many to Many

Resources can be assigned to many different buyer parties. Those buyer parties
can be assigned to many other resources. For example, one user can be assigned
to multiple address while one address can be assigned to multiple users.

