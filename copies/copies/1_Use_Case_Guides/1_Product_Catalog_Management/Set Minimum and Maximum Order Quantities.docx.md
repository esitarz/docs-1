### \#\# Introduction

There are many business use cases which require a minimum or maximum
order quantity to be set for certain products, including economic order
quantity and inventory management. This guide will explain how to set a
minimum and/or maximum order quantity for a specific product.

\#\# Prerequisites

-   \[Create and Assign a
    > Product\](https://documentation.ordercloud.io/use-case-guides/product-catalog-management/create-and-assign-a-product)

\#\# Understanding MaxQuantity and MinQuantity

On the OrderCloud.io platform, minimum and maximum order quantities are
controlled within a product's Price Schedule. A \`MaxQuantity\` can be
set directly, whereas a \`MinQuantity\` will be derived from a Price
Schedule's Price Breaks.

Since Price Schedules are the connection between a Product and the
party(via Product Assignment), different minimum/maximum quantities can
be assigned to different parties (like User Groups, Organizations) by
creating multiple Price Schedules and assigning them accordingly.

In OrderCloud.io, you have two options when it comes to setting Minimum
and Maximum Order Quantities: Restricted Quantity Price Schedule or an
Open Quantity Price Schedule. We'll walk through both of these in this
guide.

\#\# 1. Creating a Restricted Quantity Price Schedule
-----------------------------------------------------

One way to limit a user to both a minimum and maximum quantity value is
to use a Restricted Quantity Price Schedule. In this model, the user is
restricted to ordering a product at preconfigured quantity intervals
(Price Breaks) set within the Price Schedule assigned to them.

Within a user facing application, this type of Price Schedule model
typically calls for a select/dropdown quantity control, rather than an
open text field.

\<div class=\"api-reference\"\>API Reference: \[Create New Price
Schedule\](https://documentation.ordercloud.io/api-reference\#PriceSchedules\_Create)\</div\>

\`\`\`

POST https://api.ordercloud.io/v1/priceschedules HTTP/1.1\
Authentication: Bearer put\_access\_token\_here\
Content-Type: application/json\
\
{\
\"ID\": \"PriceScheduleID123\",\
\"Name\": \"Restricted Price Schedule X\",\
\"MaxQuantity\": 100,\
\"UseCumulativeQuantity\": false,\
\
\"PriceBreaks\": \[\
{\
\"Quantity\": 25,\
\"Price\": 10.0\
},\
{\
\"Quantity\": 50,\
\"Price\": 10.0\
},\
{\
\"Quantity\": 75,\
\"Price\": 10.0\
},\
{\
\"Quantity\": 100,\
\"Price\": 10.0\
}\
\],\
\"xp\": null\
}

\`\`\`

\#\# 2. Creating an Open Quantity Price Schedule with MaxQuantity and (derived) MinQuantity
-------------------------------------------------------------------------------------------

Rather than restricting the user to predefined quantity intervals, an
Open Quantity Price Schedule can be used instead. However, minimum and
maximum quantities can still be enforced within this model.

Set the \`MaxQuantity\` value on the Price Schedule in order to set a
maximum quantity for a particular product:

\<div class=\"api-reference\"\>API Reference: \[Create New Price
Schedule\](https://documentation.ordercloud.io/api-reference\#PriceSchedules\_Create)\</div\>

\`\`\`

POST https://api.ordercloud.io/v1/priceschedules HTTP/1.1\
Authentication: Bearer put\_access\_token\_here\
Content-Type: application/json

{

\"ID\": \"PriceScheduleID123\",

\"Name\": \"Maximum Quantity Price Schedule X\",

\"MaxQuantity\": 100,

\"UseCumulativeQuantity\": false,

,

\"PriceBreaks\": \[

{

\"Quantity\": 1,

\"Price\": 10.0

}

\],

\"xp\": null

}

\`\`\`

Set the Quantity of the first Price Break to your desired minimum
quantity. In order to set a minimum quantity for a particular product,
simply:

\`\`\`

POST https://api.ordercloud.io/v1/priceschedules HTTP/1.1\
Authentication: Bearer put\_access\_token\_here\
Content-Type: application/json

{\
\"ID\": \"PriceScheduleID123\",\
\"Name\": \"Minimum Quantity Price Schedule X\",\
\"MaxQuantity\": null,\
\"UseCumulativeQuantity\": false,\
\
\"PriceBreaks\": \[\
{\
\"Quantity\": 50,\
\"Price\": 10.0\
}\
\],\
\"xp\": null\
}

\`\`\`

These methods can be combined within the same price schedule in order to
restrict the user to ordering within the range derived from your minimum
and maximum quantity values.

\<div class=\"note\"\>When restricting the user to a certain quantity
range, it is recommended to keep the experience as user friendly as
possible. Displaying the minimum and/or maximum quantity when ordering
and disabling any "Add to Order" controls until a valid quantity is met
are effective ways to ensure this.\</div\>

\#\# 3. Using UseCumulativeQuantity to Enforce Maximum Order Quantity
Across an Entire Order's Line Items

By default, minimum and maximum quantities take effect at the Line Item
level, meaning the user is restricted to a particular quantity range per
Line Item. However, UseCumulativeQuantity can be set on the Price
Schedule in order to limit the user to specific quantities across the
entire order.

Set UseCumulativeQuantity to true when creating or updating a Price
Schedule in order to enforce a maximum order quantity for a product
across the sum of an entire order's line items.

\#\# Conclusion

Congratulations! You should know have enough information to set minimum
and maximum quantities on priceschedules with fixed and open quantities
You should also know be able to set Min/Max across an entire order.
