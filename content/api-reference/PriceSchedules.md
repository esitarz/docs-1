---
title: Price Schedules
date: 2018-03-23
category: API Reference
tags: Product Catalogs
slug: PriceSchedules
---
Price schedules allow the same product to be sold across multiple
channels. A price schedule may include quantity price breaks, min and
max quantity per order, whether to apply tax or shipping calculations,
or to what type of order the price schedule applies.

---

## `GET` `v1/priceschedules/{priceScheduleID}`
Get a single price schedule

| Parameters      | Description                    |
|------------------|---------------------------------|


| Parameters      | Description                    |
|------------------|---------------------------------|
| Name            | priceScheduleID                |
| Type            | string                         |
| Description     | ID of the price schedule.      |
| Required        | True                           |

## Requestbody
**Responsestatus**: `200`

## Responsebody
```
{'ID': '', 'Name': '', 'ApplyTax': False, 'ApplyShipping': False, 'MinQuantity': 0, 'MaxQuantity': 0, 'UseCumulativeQuantity': False, 'RestrictedQuantity': False, 'PriceBreaks': [{'Quantity': 0, 'Price': 0}], 'xp': {}}
```


| Parameters      | Description                    |
|------------------|---------------------------------|
| Name            | ID                             |
| Type            | string                         |
| Description     | ID of the price schedule.      |
| Required        | False                          |


| Parameters      | Description                    |
|------------------|---------------------------------|
| Name            | Name                           |
| Type            | string                         |
| Description     | Name of the price schedule.    |
| Required        | True                           |


| Parameters      | Description                    |
|------------------|---------------------------------|
| Name            | ApplyTax                       |
| Type            | boolean                        |
| Description     | Apply tax of the price schedule. |
| Required        | False                          |


| Parameters      | Description                    |
|------------------|---------------------------------|
| Name            | ApplyShipping                  |
| Type            | boolean                        |
| Description     | Apply shipping of the price schedule. |
| Required        | False                          |


| Parameters      | Description                    |
|------------------|---------------------------------|
| Name            | MinQuantity                    |
| Type            | integer                        |
| Description     | Min quantity of the price schedule. |
| Required        | False                          |


| Parameters      | Description                    |
|------------------|---------------------------------|
| Name            | MaxQuantity                    |
| Type            | integer                        |
| Description     | Max quantity of the price schedule. |
| Required        | False                          |


| Parameters      | Description                    |
|------------------|---------------------------------|
| Name            | UseCumulativeQuantity          |
| Type            | boolean                        |
| Description     | Use cumulative quantity of the price schedule. |
| Required        | False                          |


| Parameters      | Description                    |
|------------------|---------------------------------|
| Name            | RestrictedQuantity             |
| Type            | boolean                        |
| Description     | Restricted quantity of the price schedule. |
| Required        | False                          |


| Parameters      | Description                    |
|------------------|---------------------------------|
| Name            | PriceBreaks                    |
| Type            | array                          |
| Description     | Price breaks of the price schedule. |
| Required        | False                          |


| Parameters      | Description                    |
|------------------|---------------------------------|
| Name            | xp                             |
| Type            | object                         |
| Description     | Container for extended (custom) properties of the price schedule. |
| Required        | False                          |

## `GET` `v1/priceschedules`
Get a list of price schedules

| Parameters      | Description                    |
|------------------|---------------------------------|


| Parameters      | Description                    |
|------------------|---------------------------------|
| Name            | search                         |
| Type            | string                         |
| Description     | Word or phrase to search for.  |
| Required        | False                          |


| Parameters      | Description                    |
|------------------|---------------------------------|
| Name            | searchOn                       |
| Type            | string                         |
| Description     | Comma-delimited list of fields to search on. |
| Required        | False                          |


| Parameters      | Description                    |
|------------------|---------------------------------|
| Name            | sortBy                         |
| Type            | string                         |
| Description     | Comma-delimited list of fields to sort by. |
| Required        | False                          |


| Parameters      | Description                    |
|------------------|---------------------------------|
| Name            | page                           |
| Type            | integer                        |
| Description     | Page of results to return. Default: 1 |
| Required        | False                          |


| Parameters      | Description                    |
|------------------|---------------------------------|
| Name            | pageSize                       |
| Type            | integer                        |
| Description     | Number of results to return per page. Default: 20, max: 100. |
| Required        | False                          |


| Parameters      | Description                    |
|------------------|---------------------------------|
| Name            | filters                        |
| Type            | object                         |
| Description     | Any additional key/value pairs passed in the query string are interpretted as filters. Valid keys are top-level properties of the returned model or 'xp.???' |
| Required        | False                          |

## Requestbody
**Responsestatus**: `200`

## Responsebody
```
{'Meta': {'Page': 1, 'PageSize': 20, 'TotalCount': 25, 'TotalPages': 2, 'ItemRange': [1, 20]}, 'Items': [{'ID': '', 'Name': '', 'ApplyTax': False, 'ApplyShipping': False, 'MinQuantity': 0, 'MaxQuantity': 0, 'UseCumulativeQuantity': False, 'RestrictedQuantity': False, 'PriceBreaks': [{'Quantity': 0, 'Price': 0}], 'xp': {}}]}
```


| Parameters      | Description                    |
|------------------|---------------------------------|
| Name            | ID                             |
| Type            | string                         |
| Description     | ID of the price schedule.      |
| Required        | False                          |


| Parameters      | Description                    |
|------------------|---------------------------------|
| Name            | Name                           |
| Type            | string                         |
| Description     | Name of the price schedule.    |
| Required        | True                           |


| Parameters      | Description                    |
|------------------|---------------------------------|
| Name            | ApplyTax                       |
| Type            | boolean                        |
| Description     | Apply tax of the price schedule. |
| Required        | False                          |


| Parameters      | Description                    |
|------------------|---------------------------------|
| Name            | ApplyShipping                  |
| Type            | boolean                        |
| Description     | Apply shipping of the price schedule. |
| Required        | False                          |


| Parameters      | Description                    |
|------------------|---------------------------------|
| Name            | MinQuantity                    |
| Type            | integer                        |
| Description     | Min quantity of the price schedule. |
| Required        | False                          |


| Parameters      | Description                    |
|------------------|---------------------------------|
| Name            | MaxQuantity                    |
| Type            | integer                        |
| Description     | Max quantity of the price schedule. |
| Required        | False                          |


| Parameters      | Description                    |
|------------------|---------------------------------|
| Name            | UseCumulativeQuantity          |
| Type            | boolean                        |
| Description     | Use cumulative quantity of the price schedule. |
| Required        | False                          |


| Parameters      | Description                    |
|------------------|---------------------------------|
| Name            | RestrictedQuantity             |
| Type            | boolean                        |
| Description     | Restricted quantity of the price schedule. |
| Required        | False                          |


| Parameters      | Description                    |
|------------------|---------------------------------|
| Name            | PriceBreaks                    |
| Type            | array                          |
| Description     | Price breaks of the price schedule. |
| Required        | False                          |


| Parameters      | Description                    |
|------------------|---------------------------------|
| Name            | xp                             |
| Type            | object                         |
| Description     | Container for extended (custom) properties of the price schedule. |
| Required        | False                          |

## `POST` `v1/priceschedules`
Create a new price schedule
## Requestbody
```
{'ID': '', 'Name': '', 'ApplyTax': False, 'ApplyShipping': False, 'MinQuantity': 0, 'MaxQuantity': 0, 'UseCumulativeQuantity': False, 'RestrictedQuantity': False, 'PriceBreaks': [{'Quantity': 0, 'Price': 0}], 'xp': {}}
```

```
[{'Name': 'ID', 'Type': 'string', 'Description': 'ID of the price schedule. Can only contain characters Aa-Zz, 0-9, -, and _. Searchable: priority level 1. Sortable: priority level 2.', 'Required': False}, {'Name': 'Name', 'Type': 'string', 'Description': 'Name of the price schedule. Required. Max length 100 characters. Searchable: priority level 2. Sortable: priority level 1.', 'Required': True}, {'Name': 'ApplyTax', 'Type': 'boolean', 'Description': 'Apply tax of the price schedule. Searchable: priority level 3.', 'Required': False}, {'Name': 'ApplyShipping', 'Type': 'boolean', 'Description': 'Apply shipping of the price schedule.', 'Required': False}, {'Name': 'MinQuantity', 'Type': 'integer', 'Description': 'Min quantity of the price schedule. Must be at least 1.', 'Required': False}, {'Name': 'MaxQuantity', 'Type': 'integer', 'Description': 'Max quantity of the price schedule.', 'Required': False}, {'Name': 'UseCumulativeQuantity', 'Type': 'boolean', 'Description': 'Use cumulative quantity of the price schedule.', 'Required': False}, {'Name': 'RestrictedQuantity', 'Type': 'boolean', 'Description': 'Restricted quantity of the price schedule.', 'Required': False}, {'Name': 'PriceBreaks', 'Type': 'array', 'Description': 'Price breaks of the price schedule.', 'Required': False}, {'Name': 'xp', 'Type': 'object', 'Description': 'Container for extended (custom) properties of the price schedule.', 'Required': False}]
```

**Responsestatus**: `201`

## Responsebody
```
{'ID': '', 'Name': '', 'ApplyTax': False, 'ApplyShipping': False, 'MinQuantity': 0, 'MaxQuantity': 0, 'UseCumulativeQuantity': False, 'RestrictedQuantity': False, 'PriceBreaks': [{'Quantity': 0, 'Price': 0}], 'xp': {}}
```


| Parameters      | Description                    |
|------------------|---------------------------------|
| Name            | ID                             |
| Type            | string                         |
| Description     | ID of the price schedule.      |
| Required        | False                          |


| Parameters      | Description                    |
|------------------|---------------------------------|
| Name            | Name                           |
| Type            | string                         |
| Description     | Name of the price schedule.    |
| Required        | True                           |


| Parameters      | Description                    |
|------------------|---------------------------------|
| Name            | ApplyTax                       |
| Type            | boolean                        |
| Description     | Apply tax of the price schedule. |
| Required        | False                          |


| Parameters      | Description                    |
|------------------|---------------------------------|
| Name            | ApplyShipping                  |
| Type            | boolean                        |
| Description     | Apply shipping of the price schedule. |
| Required        | False                          |


| Parameters      | Description                    |
|------------------|---------------------------------|
| Name            | MinQuantity                    |
| Type            | integer                        |
| Description     | Min quantity of the price schedule. |
| Required        | False                          |


| Parameters      | Description                    |
|------------------|---------------------------------|
| Name            | MaxQuantity                    |
| Type            | integer                        |
| Description     | Max quantity of the price schedule. |
| Required        | False                          |


| Parameters      | Description                    |
|------------------|---------------------------------|
| Name            | UseCumulativeQuantity          |
| Type            | boolean                        |
| Description     | Use cumulative quantity of the price schedule. |
| Required        | False                          |


| Parameters      | Description                    |
|------------------|---------------------------------|
| Name            | RestrictedQuantity             |
| Type            | boolean                        |
| Description     | Restricted quantity of the price schedule. |
| Required        | False                          |


| Parameters      | Description                    |
|------------------|---------------------------------|
| Name            | PriceBreaks                    |
| Type            | array                          |
| Description     | Price breaks of the price schedule. |
| Required        | False                          |


| Parameters      | Description                    |
|------------------|---------------------------------|
| Name            | xp                             |
| Type            | object                         |
| Description     | Container for extended (custom) properties of the price schedule. |
| Required        | False                          |

## `PUT` `v1/priceschedules/{priceScheduleID}`
Create or update a price schedule

| Parameters      | Description                    |
|------------------|---------------------------------|


| Parameters      | Description                    |
|------------------|---------------------------------|
| Name            | priceScheduleID                |
| Type            | string                         |
| Description     | ID of the price schedule.      |
| Required        | True                           |

## Requestbody
```
{'ID': '', 'Name': '', 'ApplyTax': False, 'ApplyShipping': False, 'MinQuantity': 0, 'MaxQuantity': 0, 'UseCumulativeQuantity': False, 'RestrictedQuantity': False, 'PriceBreaks': [{'Quantity': 0, 'Price': 0}], 'xp': {}}
```

```
[{'Name': 'ID', 'Type': 'string', 'Description': 'ID of the price schedule. Can only contain characters Aa-Zz, 0-9, -, and _. Searchable: priority level 1. Sortable: priority level 2.', 'Required': False}, {'Name': 'Name', 'Type': 'string', 'Description': 'Name of the price schedule. Required. Max length 100 characters. Searchable: priority level 2. Sortable: priority level 1.', 'Required': True}, {'Name': 'ApplyTax', 'Type': 'boolean', 'Description': 'Apply tax of the price schedule. Searchable: priority level 3.', 'Required': False}, {'Name': 'ApplyShipping', 'Type': 'boolean', 'Description': 'Apply shipping of the price schedule.', 'Required': False}, {'Name': 'MinQuantity', 'Type': 'integer', 'Description': 'Min quantity of the price schedule. Must be at least 1.', 'Required': False}, {'Name': 'MaxQuantity', 'Type': 'integer', 'Description': 'Max quantity of the price schedule.', 'Required': False}, {'Name': 'UseCumulativeQuantity', 'Type': 'boolean', 'Description': 'Use cumulative quantity of the price schedule.', 'Required': False}, {'Name': 'RestrictedQuantity', 'Type': 'boolean', 'Description': 'Restricted quantity of the price schedule.', 'Required': False}, {'Name': 'PriceBreaks', 'Type': 'array', 'Description': 'Price breaks of the price schedule.', 'Required': False}, {'Name': 'xp', 'Type': 'object', 'Description': 'Container for extended (custom) properties of the price schedule.', 'Required': False}]
```

**Responsestatus**: `200`

## Responsebody
```
{'ID': '', 'Name': '', 'ApplyTax': False, 'ApplyShipping': False, 'MinQuantity': 0, 'MaxQuantity': 0, 'UseCumulativeQuantity': False, 'RestrictedQuantity': False, 'PriceBreaks': [{'Quantity': 0, 'Price': 0}], 'xp': {}}
```


| Parameters      | Description                    |
|------------------|---------------------------------|
| Name            | ID                             |
| Type            | string                         |
| Description     | ID of the price schedule.      |
| Required        | False                          |


| Parameters      | Description                    |
|------------------|---------------------------------|
| Name            | Name                           |
| Type            | string                         |
| Description     | Name of the price schedule.    |
| Required        | True                           |


| Parameters      | Description                    |
|------------------|---------------------------------|
| Name            | ApplyTax                       |
| Type            | boolean                        |
| Description     | Apply tax of the price schedule. |
| Required        | False                          |


| Parameters      | Description                    |
|------------------|---------------------------------|
| Name            | ApplyShipping                  |
| Type            | boolean                        |
| Description     | Apply shipping of the price schedule. |
| Required        | False                          |


| Parameters      | Description                    |
|------------------|---------------------------------|
| Name            | MinQuantity                    |
| Type            | integer                        |
| Description     | Min quantity of the price schedule. |
| Required        | False                          |


| Parameters      | Description                    |
|------------------|---------------------------------|
| Name            | MaxQuantity                    |
| Type            | integer                        |
| Description     | Max quantity of the price schedule. |
| Required        | False                          |


| Parameters      | Description                    |
|------------------|---------------------------------|
| Name            | UseCumulativeQuantity          |
| Type            | boolean                        |
| Description     | Use cumulative quantity of the price schedule. |
| Required        | False                          |


| Parameters      | Description                    |
|------------------|---------------------------------|
| Name            | RestrictedQuantity             |
| Type            | boolean                        |
| Description     | Restricted quantity of the price schedule. |
| Required        | False                          |


| Parameters      | Description                    |
|------------------|---------------------------------|
| Name            | PriceBreaks                    |
| Type            | array                          |
| Description     | Price breaks of the price schedule. |
| Required        | False                          |


| Parameters      | Description                    |
|------------------|---------------------------------|
| Name            | xp                             |
| Type            | object                         |
| Description     | Container for extended (custom) properties of the price schedule. |
| Required        | False                          |

## `DELETE` `v1/priceschedules/{priceScheduleID}`
Delete a price schedule

| Parameters      | Description                    |
|------------------|---------------------------------|


| Parameters      | Description                    |
|------------------|---------------------------------|
| Name            | priceScheduleID                |
| Type            | string                         |
| Description     | ID of the price schedule.      |
| Required        | True                           |

## Requestbody
**Responsestatus**: `204`

## Responsebody
## `PATCH` `v1/priceschedules/{priceScheduleID}`
Partially update a price schedule

| Parameters      | Description                    |
|------------------|---------------------------------|


| Parameters      | Description                    |
|------------------|---------------------------------|
| Name            | priceScheduleID                |
| Type            | string                         |
| Description     | ID of the price schedule.      |
| Required        | True                           |

## Requestbody
```
{'ID': '', 'Name': '', 'ApplyTax': False, 'ApplyShipping': False, 'MinQuantity': 0, 'MaxQuantity': 0, 'UseCumulativeQuantity': False, 'RestrictedQuantity': False, 'PriceBreaks': [{'Quantity': 0, 'Price': 0}], 'xp': {}}
```

```
[{'Name': 'ID', 'Type': 'string', 'Description': 'ID of the price schedule. Can only contain characters Aa-Zz, 0-9, -, and _. Searchable: priority level 1. Sortable: priority level 2.', 'Required': False}, {'Name': 'Name', 'Type': 'string', 'Description': 'Name of the price schedule. Required. Max length 100 characters. Searchable: priority level 2. Sortable: priority level 1.', 'Required': True}, {'Name': 'ApplyTax', 'Type': 'boolean', 'Description': 'Apply tax of the price schedule. Searchable: priority level 3.', 'Required': False}, {'Name': 'ApplyShipping', 'Type': 'boolean', 'Description': 'Apply shipping of the price schedule.', 'Required': False}, {'Name': 'MinQuantity', 'Type': 'integer', 'Description': 'Min quantity of the price schedule. Must be at least 1.', 'Required': False}, {'Name': 'MaxQuantity', 'Type': 'integer', 'Description': 'Max quantity of the price schedule.', 'Required': False}, {'Name': 'UseCumulativeQuantity', 'Type': 'boolean', 'Description': 'Use cumulative quantity of the price schedule.', 'Required': False}, {'Name': 'RestrictedQuantity', 'Type': 'boolean', 'Description': 'Restricted quantity of the price schedule.', 'Required': False}, {'Name': 'PriceBreaks', 'Type': 'array', 'Description': 'Price breaks of the price schedule.', 'Required': False}, {'Name': 'xp', 'Type': 'object', 'Description': 'Container for extended (custom) properties of the price schedule.', 'Required': False}]
```

**Responsestatus**: `200`

## Responsebody
```
{'ID': '', 'Name': '', 'ApplyTax': False, 'ApplyShipping': False, 'MinQuantity': 0, 'MaxQuantity': 0, 'UseCumulativeQuantity': False, 'RestrictedQuantity': False, 'PriceBreaks': [{'Quantity': 0, 'Price': 0}], 'xp': {}}
```


| Parameters      | Description                    |
|------------------|---------------------------------|
| Name            | ID                             |
| Type            | string                         |
| Description     | ID of the price schedule.      |
| Required        | False                          |


| Parameters      | Description                    |
|------------------|---------------------------------|
| Name            | Name                           |
| Type            | string                         |
| Description     | Name of the price schedule.    |
| Required        | True                           |


| Parameters      | Description                    |
|------------------|---------------------------------|
| Name            | ApplyTax                       |
| Type            | boolean                        |
| Description     | Apply tax of the price schedule. |
| Required        | False                          |


| Parameters      | Description                    |
|------------------|---------------------------------|
| Name            | ApplyShipping                  |
| Type            | boolean                        |
| Description     | Apply shipping of the price schedule. |
| Required        | False                          |


| Parameters      | Description                    |
|------------------|---------------------------------|
| Name            | MinQuantity                    |
| Type            | integer                        |
| Description     | Min quantity of the price schedule. |
| Required        | False                          |


| Parameters      | Description                    |
|------------------|---------------------------------|
| Name            | MaxQuantity                    |
| Type            | integer                        |
| Description     | Max quantity of the price schedule. |
| Required        | False                          |


| Parameters      | Description                    |
|------------------|---------------------------------|
| Name            | UseCumulativeQuantity          |
| Type            | boolean                        |
| Description     | Use cumulative quantity of the price schedule. |
| Required        | False                          |


| Parameters      | Description                    |
|------------------|---------------------------------|
| Name            | RestrictedQuantity             |
| Type            | boolean                        |
| Description     | Restricted quantity of the price schedule. |
| Required        | False                          |


| Parameters      | Description                    |
|------------------|---------------------------------|
| Name            | PriceBreaks                    |
| Type            | array                          |
| Description     | Price breaks of the price schedule. |
| Required        | False                          |


| Parameters      | Description                    |
|------------------|---------------------------------|
| Name            | xp                             |
| Type            | object                         |
| Description     | Container for extended (custom) properties of the price schedule. |
| Required        | False                          |

## `POST` `v1/priceschedules/{priceScheduleID}/PriceBreaks`
Save a price schedule price break

| Parameters      | Description                    |
|------------------|---------------------------------|


| Parameters      | Description                    |
|------------------|---------------------------------|
| Name            | priceScheduleID                |
| Type            | string                         |
| Description     | ID of the price schedule.      |
| Required        | True                           |

## Requestbody
```
{'Quantity': 0, 'Price': 0}
```

```
[{'Name': 'Quantity', 'Type': 'integer', 'Description': 'Quantity of the price break. Required. Must be at least 0.', 'Required': True}, {'Name': 'Price', 'Type': 'float', 'Description': 'Price of the price break. Required.', 'Required': True}]
```

**Responsestatus**: `201`

## Responsebody
```
{'ID': '', 'Name': '', 'ApplyTax': False, 'ApplyShipping': False, 'MinQuantity': 0, 'MaxQuantity': 0, 'UseCumulativeQuantity': False, 'RestrictedQuantity': False, 'PriceBreaks': [{'Quantity': 0, 'Price': 0}], 'xp': {}}
```


| Parameters      | Description                    |
|------------------|---------------------------------|
| Name            | ID                             |
| Type            | string                         |
| Description     | ID of the price schedule.      |
| Required        | False                          |


| Parameters      | Description                    |
|------------------|---------------------------------|
| Name            | Name                           |
| Type            | string                         |
| Description     | Name of the price schedule.    |
| Required        | True                           |


| Parameters      | Description                    |
|------------------|---------------------------------|
| Name            | ApplyTax                       |
| Type            | boolean                        |
| Description     | Apply tax of the price schedule. |
| Required        | False                          |


| Parameters      | Description                    |
|------------------|---------------------------------|
| Name            | ApplyShipping                  |
| Type            | boolean                        |
| Description     | Apply shipping of the price schedule. |
| Required        | False                          |


| Parameters      | Description                    |
|------------------|---------------------------------|
| Name            | MinQuantity                    |
| Type            | integer                        |
| Description     | Min quantity of the price schedule. |
| Required        | False                          |


| Parameters      | Description                    |
|------------------|---------------------------------|
| Name            | MaxQuantity                    |
| Type            | integer                        |
| Description     | Max quantity of the price schedule. |
| Required        | False                          |


| Parameters      | Description                    |
|------------------|---------------------------------|
| Name            | UseCumulativeQuantity          |
| Type            | boolean                        |
| Description     | Use cumulative quantity of the price schedule. |
| Required        | False                          |


| Parameters      | Description                    |
|------------------|---------------------------------|
| Name            | RestrictedQuantity             |
| Type            | boolean                        |
| Description     | Restricted quantity of the price schedule. |
| Required        | False                          |


| Parameters      | Description                    |
|------------------|---------------------------------|
| Name            | PriceBreaks                    |
| Type            | array                          |
| Description     | Price breaks of the price schedule. |
| Required        | False                          |


| Parameters      | Description                    |
|------------------|---------------------------------|
| Name            | xp                             |
| Type            | object                         |
| Description     | Container for extended (custom) properties of the price schedule. |
| Required        | False                          |

## `DELETE` `v1/priceschedules/{priceScheduleID}/PriceBreaks`
Delete a price schedule price break

| Parameters      | Description                    |
|------------------|---------------------------------|


| Parameters      | Description                    |
|------------------|---------------------------------|
| Name            | priceScheduleID                |
| Type            | string                         |
| Description     | ID of the price schedule.      |
| Required        | True                           |


| Parameters      | Description                    |
|------------------|---------------------------------|
| Name            | quantity                       |
| Type            | integer                        |
| Description     | Quantity of the price schedule. |
| Required        | True                           |

## Requestbody
**Responsestatus**: `204`

## Responsebody