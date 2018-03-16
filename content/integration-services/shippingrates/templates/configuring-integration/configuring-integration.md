

##  __Creating Configuration

To configure your integration, navigate to the Dashboard Dashboard
Integrations page within OrderCloud.io and select Shipping Rates.

###  Selecting Carriers

First, select which carriers you would like shipping rate estimates returned
from. Current options include USPS and UPS. If UPS or FedEx are selected, you
have the option to enter your account credentials in order to receive shipping
rates specific to your account.

![](assets/images/docs-guides/integrations/shippingrates/shippingrates-
configuration-carriers.png)

###  Rate Adjustments

Next, shipping rate estimates can be configured to be automatically increased
or decreased based on a percentage or flat rate. These adjustments can be made
at a global level (all carriers) or at the carrier level.

![](assets/images/docs-guides/integrations/shippingrates/shippingrates-
configuration-rate-adjustment.png)

###  Manual Shippers

Finally, manual shippers can be configured to be returned for both _GetRates_
and _GetLineItemRates_ methods. Manual shippers consist of a Name and a flat
rate Price. This Price will not be adjusted using the Rate Adjustments
explained above, so enter the exact value you would like to charge the user
for that specific shipper. You can configure each manual shipper to always be
returned or only be returned when no rate estimates are obtained from your
selected carrier(s).

![](assets/images/docs-guides/integrations/shippingrates/shippingrates-
configuration-manual-shippers.png)

##  __Assigning Configuration

After your configuration has been created, navigate to a Buyer Application
that will be using the integration. Select the Integrations tab, then click
Add. Since you previously created the Shipping Rates configuration, it should
be available within the modal. Simply click Enable and your Buyer Application
will be ready to use the Shipping Rates integration.

![](assets/images/docs-guides/integrations/shippingrates/shippingrates-
assignment.png)

