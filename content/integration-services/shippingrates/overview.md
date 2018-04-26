---
title: Shipping Rates: Overview
date: 2018-04-16
category: Shipping Rates
---


##  Shipping Rates Overview

OrderCloud.io offers the ability to provide weight-based shipping rate
estimates within your storefronts based on the commercial shipping rates.
Supported carriers within this integration currently include USPS, UPS, and
FedEx.

Once configured, the OrderCloud.io Shipping Rates integration offers three
methods: _GetRates_ , _GetLineItemRates_ , and _SetShippingCost_.

GetRates will automatically separate the Order's Line Items into shipments
based on their `ShippingAddress` and the Line Item Product's
`ShipFromAddress`. Rates will be returned based on these determined shipments.

GetLineItemRates will obtain shipping rates for each Line Item individually,
regardless of the item's `ShippingAddress` and the Line Item Product's
`ShipFromAddress`.

SetShippingCost simply allows your application to set an Order's
`ShippingCost` value once the user has selected their desired shipper(s) for
their Order.

Additional configuration options include rate adjustments and manual shippers.
Rate adjustments allows you to automatically increase or decrease the
estimated shipping rates by a percentage or flat rate. This can be configured
at a global or carrier level.

Manual shippers allows you to configure shipper options with a Name and flat
rate Price. This price will not be adjusted using the rate adjustments
described above. Manual shippers can be configured to always be returned or to
only be returned when no shipping rate estimates are returned. This may be
caused by a determined shipment with a weight greater than 150 lbs., invalid
addresses, or simply because the carrier's web services are not functioning
properly.

OrderCloud.io's Shipping Rates integration not only requires configuration for
the [integration endpoint]({filename}configuring-integration.md) itself, but also for [the products that will be included]({filename}configuring-catalog.md) for shipping rate estimates as well. 

