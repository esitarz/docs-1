---
title: Configuring Catalog
author: OrderCloud.io 
Date: 2018-03-16 12:35:35.774570
slug: /docs/content/integration-services/shippingrates configuring-catalog
---


##  __Configuring Catalog Overview

In order to be considered when estimating shipping rates, products and their
price schedules will need a few things set up first.

##  __ApplyShipping

First, `ApplyShipping` will need to be set to true on the price schedule
assigned to the product. Any Line Items containing Products without this value
set to true on its Price Schedule will be ignored when calculating shipping
rates. Here's a sample Price Schedule with this configuration set:

##  __ShipWeight

Next, a `ShipWeight` (in lbs.) should to be set on the Product being ordered
to provide accurate shipping rates. If a value is not set, the Product will
still be included in the calculation. However, a weight of `0` will be used
when calculating rates, resulting in inaccurate rates.

##  __ShipFromAddressID

Next, a `ShipFromAddressID` needs to be set on the Product being ordered to be
considered when estimating shipping rates. The value for this field should be
a previously created Admin Address ID. Each Product should have the
`ShipFromAddressID` set for the location it is being shipped from. Products
being shipped from separate locations will be considered a separate shipment
within OrderCloud.io, meaning Line Items will be grouped by these addresses
(as well as the item's Shipping Address) when calculating rates. Here's a
sample Admin Address and a Product containing that Admin Address' ID, as well
as a `ShipWeight`:

