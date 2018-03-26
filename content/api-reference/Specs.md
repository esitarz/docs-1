---
title: Specs
date: 2018-03-26
category: API Reference
tags: Product Catalogs
slug: Product-Catalogs-Specs
---
Specs are used to capture user input when adding a Product to an Order.
At its simplest, a spec is a name/value pair. A spec value may have a
price markup or markdown associated with it. In more advanced scenarios,
specs can drive the product SKU. For example, a product may be available
in 3 colors and 3 sizes and therefore have a total of 9 SKUs. **The
OrderCloud platform will choose the correct SKU based on the
user-selected color and size specs**.

---

## `GET` `v1/specs/{specID}`
Get a single spec

| Parameters      | Description                    |
|------------------|---------------------------------|


| Parameters      | Description                    |
|------------------|---------------------------------|
| Name            | specID                         |
| Type            | string                         |
| Description     | ID of the spec.                |
| Required        | True                           |

## Requestbody
**Responsestatus**: `200`

## Responsebody
```
{'OptionCount': 0, 'ID': '', 'ListOrder': 1, 'Name': '', 'DefaultValue': '', 'Required': False, 'AllowOpenText': False, 'DefaultOptionID': '', 'DefinesVariant': False, 'xp': {}}
```


| Parameters      | Description                    |
|------------------|---------------------------------|
| Name            | OptionCount                    |
| Type            | integer                        |
| Description     | Option count of the spec.      |
| Required        | False                          |


| Parameters      | Description                    |
|------------------|---------------------------------|
| Name            | ID                             |
| Type            | string                         |
| Description     | ID of the spec.                |
| Required        | False                          |


| Parameters      | Description                    |
|------------------|---------------------------------|
| Name            | ListOrder                      |
| Type            | integer                        |
| Description     | List order of the spec.        |
| Required        | False                          |


| Parameters      | Description                    |
|------------------|---------------------------------|
| Name            | Name                           |
| Type            | string                         |
| Description     | Name of the spec.              |
| Required        | True                           |


| Parameters      | Description                    |
|------------------|---------------------------------|
| Name            | DefaultValue                   |
| Type            | string                         |
| Description     | Default value of the spec.     |
| Required        | False                          |


| Parameters      | Description                    |
|------------------|---------------------------------|
| Name            | Required                       |
| Type            | boolean                        |
| Description     | Required of the spec.          |
| Required        | False                          |


| Parameters      | Description                    |
|------------------|---------------------------------|
| Name            | AllowOpenText                  |
| Type            | boolean                        |
| Description     | Allow open text of the spec.   |
| Required        | False                          |


| Parameters      | Description                    |
|------------------|---------------------------------|
| Name            | DefaultOptionID                |
| Type            | string                         |
| Description     | ID of the default option.      |
| Required        | False                          |


| Parameters      | Description                    |
|------------------|---------------------------------|
| Name            | DefinesVariant                 |
| Type            | boolean                        |
| Description     | True if each unique combinations of this Spec's Options map to unique Product Variants/SKUs. |
| Required        | False                          |


| Parameters      | Description                    |
|------------------|---------------------------------|
| Name            | xp                             |
| Type            | object                         |
| Description     | Container for extended (custom) properties of the spec. |
| Required        | False                          |

## `GET` `v1/specs`
Get a list of specs

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
{'Meta': {'Page': 1, 'PageSize': 20, 'TotalCount': 25, 'TotalPages': 2, 'ItemRange': [1, 20]}, 'Items': [{'OptionCount': 0, 'ID': '', 'ListOrder': 1, 'Name': '', 'DefaultValue': '', 'Required': False, 'AllowOpenText': False, 'DefaultOptionID': '', 'DefinesVariant': False, 'xp': {}}]}
```


| Parameters      | Description                    |
|------------------|---------------------------------|
| Name            | OptionCount                    |
| Type            | integer                        |
| Description     | Option count of the spec.      |
| Required        | False                          |


| Parameters      | Description                    |
|------------------|---------------------------------|
| Name            | ID                             |
| Type            | string                         |
| Description     | ID of the spec.                |
| Required        | False                          |


| Parameters      | Description                    |
|------------------|---------------------------------|
| Name            | ListOrder                      |
| Type            | integer                        |
| Description     | List order of the spec.        |
| Required        | False                          |


| Parameters      | Description                    |
|------------------|---------------------------------|
| Name            | Name                           |
| Type            | string                         |
| Description     | Name of the spec.              |
| Required        | True                           |


| Parameters      | Description                    |
|------------------|---------------------------------|
| Name            | DefaultValue                   |
| Type            | string                         |
| Description     | Default value of the spec.     |
| Required        | False                          |


| Parameters      | Description                    |
|------------------|---------------------------------|
| Name            | Required                       |
| Type            | boolean                        |
| Description     | Required of the spec.          |
| Required        | False                          |


| Parameters      | Description                    |
|------------------|---------------------------------|
| Name            | AllowOpenText                  |
| Type            | boolean                        |
| Description     | Allow open text of the spec.   |
| Required        | False                          |


| Parameters      | Description                    |
|------------------|---------------------------------|
| Name            | DefaultOptionID                |
| Type            | string                         |
| Description     | ID of the default option.      |
| Required        | False                          |


| Parameters      | Description                    |
|------------------|---------------------------------|
| Name            | DefinesVariant                 |
| Type            | boolean                        |
| Description     | True if each unique combinations of this Spec's Options map to unique Product Variants/SKUs. |
| Required        | False                          |


| Parameters      | Description                    |
|------------------|---------------------------------|
| Name            | xp                             |
| Type            | object                         |
| Description     | Container for extended (custom) properties of the spec. |
| Required        | False                          |

## `POST` `v1/specs`
Create a new spec
## Requestbody
```
{'ID': '', 'ListOrder': 1, 'Name': '', 'DefaultValue': '', 'Required': False, 'AllowOpenText': False, 'DefaultOptionID': '', 'DefinesVariant': False, 'xp': {}}
```

```
[{'Name': 'ID', 'Type': 'string', 'Description': 'ID of the spec. Can only contain characters Aa-Zz, 0-9, -, and _. Searchable: priority level 3. Sortable: priority level 3.', 'Required': False}, {'Name': 'ListOrder', 'Type': 'integer', 'Description': 'List order of the spec. Searchable: priority level 2. Sortable: priority level 1.', 'Required': False}, {'Name': 'Name', 'Type': 'string', 'Description': 'Name of the spec. Required. Searchable: priority level 1. Sortable: priority level 2.', 'Required': True}, {'Name': 'DefaultValue', 'Type': 'string', 'Description': 'Default value of the spec. Max length 2000 characters.', 'Required': False}, {'Name': 'Required', 'Type': 'boolean', 'Description': 'Required of the spec. Searchable: priority level 4.', 'Required': False}, {'Name': 'AllowOpenText', 'Type': 'boolean', 'Description': 'Allow open text of the spec. Searchable: priority level 5.', 'Required': False}, {'Name': 'DefaultOptionID', 'Type': 'string', 'Description': 'ID of the default option.', 'Required': False}, {'Name': 'DefinesVariant', 'Type': 'boolean', 'Description': "True if each unique combinations of this Spec's Options map to unique Product Variants/SKUs.", 'Required': False}, {'Name': 'xp', 'Type': 'object', 'Description': 'Container for extended (custom) properties of the spec.', 'Required': False}]
```

**Responsestatus**: `201`

## Responsebody
```
{'OptionCount': 0, 'ID': '', 'ListOrder': 1, 'Name': '', 'DefaultValue': '', 'Required': False, 'AllowOpenText': False, 'DefaultOptionID': '', 'DefinesVariant': False, 'xp': {}}
```


| Parameters      | Description                    |
|------------------|---------------------------------|
| Name            | OptionCount                    |
| Type            | integer                        |
| Description     | Option count of the spec.      |
| Required        | False                          |


| Parameters      | Description                    |
|------------------|---------------------------------|
| Name            | ID                             |
| Type            | string                         |
| Description     | ID of the spec.                |
| Required        | False                          |


| Parameters      | Description                    |
|------------------|---------------------------------|
| Name            | ListOrder                      |
| Type            | integer                        |
| Description     | List order of the spec.        |
| Required        | False                          |


| Parameters      | Description                    |
|------------------|---------------------------------|
| Name            | Name                           |
| Type            | string                         |
| Description     | Name of the spec.              |
| Required        | True                           |


| Parameters      | Description                    |
|------------------|---------------------------------|
| Name            | DefaultValue                   |
| Type            | string                         |
| Description     | Default value of the spec.     |
| Required        | False                          |


| Parameters      | Description                    |
|------------------|---------------------------------|
| Name            | Required                       |
| Type            | boolean                        |
| Description     | Required of the spec.          |
| Required        | False                          |


| Parameters      | Description                    |
|------------------|---------------------------------|
| Name            | AllowOpenText                  |
| Type            | boolean                        |
| Description     | Allow open text of the spec.   |
| Required        | False                          |


| Parameters      | Description                    |
|------------------|---------------------------------|
| Name            | DefaultOptionID                |
| Type            | string                         |
| Description     | ID of the default option.      |
| Required        | False                          |


| Parameters      | Description                    |
|------------------|---------------------------------|
| Name            | DefinesVariant                 |
| Type            | boolean                        |
| Description     | True if each unique combinations of this Spec's Options map to unique Product Variants/SKUs. |
| Required        | False                          |


| Parameters      | Description                    |
|------------------|---------------------------------|
| Name            | xp                             |
| Type            | object                         |
| Description     | Container for extended (custom) properties of the spec. |
| Required        | False                          |

## `PUT` `v1/specs/{specID}`
Create or update a spec

| Parameters      | Description                    |
|------------------|---------------------------------|


| Parameters      | Description                    |
|------------------|---------------------------------|
| Name            | specID                         |
| Type            | string                         |
| Description     | ID of the spec.                |
| Required        | True                           |

## Requestbody
```
{'ID': '', 'ListOrder': 1, 'Name': '', 'DefaultValue': '', 'Required': False, 'AllowOpenText': False, 'DefaultOptionID': '', 'DefinesVariant': False, 'xp': {}}
```

```
[{'Name': 'ID', 'Type': 'string', 'Description': 'ID of the spec. Can only contain characters Aa-Zz, 0-9, -, and _. Searchable: priority level 3. Sortable: priority level 3.', 'Required': False}, {'Name': 'ListOrder', 'Type': 'integer', 'Description': 'List order of the spec. Searchable: priority level 2. Sortable: priority level 1.', 'Required': False}, {'Name': 'Name', 'Type': 'string', 'Description': 'Name of the spec. Required. Searchable: priority level 1. Sortable: priority level 2.', 'Required': True}, {'Name': 'DefaultValue', 'Type': 'string', 'Description': 'Default value of the spec. Max length 2000 characters.', 'Required': False}, {'Name': 'Required', 'Type': 'boolean', 'Description': 'Required of the spec. Searchable: priority level 4.', 'Required': False}, {'Name': 'AllowOpenText', 'Type': 'boolean', 'Description': 'Allow open text of the spec. Searchable: priority level 5.', 'Required': False}, {'Name': 'DefaultOptionID', 'Type': 'string', 'Description': 'ID of the default option.', 'Required': False}, {'Name': 'DefinesVariant', 'Type': 'boolean', 'Description': "True if each unique combinations of this Spec's Options map to unique Product Variants/SKUs.", 'Required': False}, {'Name': 'xp', 'Type': 'object', 'Description': 'Container for extended (custom) properties of the spec.', 'Required': False}]
```

**Responsestatus**: `200`

## Responsebody
```
{'OptionCount': 0, 'ID': '', 'ListOrder': 1, 'Name': '', 'DefaultValue': '', 'Required': False, 'AllowOpenText': False, 'DefaultOptionID': '', 'DefinesVariant': False, 'xp': {}}
```


| Parameters      | Description                    |
|------------------|---------------------------------|
| Name            | OptionCount                    |
| Type            | integer                        |
| Description     | Option count of the spec.      |
| Required        | False                          |


| Parameters      | Description                    |
|------------------|---------------------------------|
| Name            | ID                             |
| Type            | string                         |
| Description     | ID of the spec.                |
| Required        | False                          |


| Parameters      | Description                    |
|------------------|---------------------------------|
| Name            | ListOrder                      |
| Type            | integer                        |
| Description     | List order of the spec.        |
| Required        | False                          |


| Parameters      | Description                    |
|------------------|---------------------------------|
| Name            | Name                           |
| Type            | string                         |
| Description     | Name of the spec.              |
| Required        | True                           |


| Parameters      | Description                    |
|------------------|---------------------------------|
| Name            | DefaultValue                   |
| Type            | string                         |
| Description     | Default value of the spec.     |
| Required        | False                          |


| Parameters      | Description                    |
|------------------|---------------------------------|
| Name            | Required                       |
| Type            | boolean                        |
| Description     | Required of the spec.          |
| Required        | False                          |


| Parameters      | Description                    |
|------------------|---------------------------------|
| Name            | AllowOpenText                  |
| Type            | boolean                        |
| Description     | Allow open text of the spec.   |
| Required        | False                          |


| Parameters      | Description                    |
|------------------|---------------------------------|
| Name            | DefaultOptionID                |
| Type            | string                         |
| Description     | ID of the default option.      |
| Required        | False                          |


| Parameters      | Description                    |
|------------------|---------------------------------|
| Name            | DefinesVariant                 |
| Type            | boolean                        |
| Description     | True if each unique combinations of this Spec's Options map to unique Product Variants/SKUs. |
| Required        | False                          |


| Parameters      | Description                    |
|------------------|---------------------------------|
| Name            | xp                             |
| Type            | object                         |
| Description     | Container for extended (custom) properties of the spec. |
| Required        | False                          |

## `DELETE` `v1/specs/{specID}`
Delete a spec

| Parameters      | Description                    |
|------------------|---------------------------------|


| Parameters      | Description                    |
|------------------|---------------------------------|
| Name            | specID                         |
| Type            | string                         |
| Description     | ID of the spec.                |
| Required        | True                           |

## Requestbody
**Responsestatus**: `204`

## Responsebody
## `PATCH` `v1/specs/{specID}`
Partially update a spec

| Parameters      | Description                    |
|------------------|---------------------------------|


| Parameters      | Description                    |
|------------------|---------------------------------|
| Name            | specID                         |
| Type            | string                         |
| Description     | ID of the spec.                |
| Required        | True                           |

## Requestbody
```
{'ID': '', 'ListOrder': 1, 'Name': '', 'DefaultValue': '', 'Required': False, 'AllowOpenText': False, 'DefaultOptionID': '', 'DefinesVariant': False, 'xp': {}}
```

```
[{'Name': 'ID', 'Type': 'string', 'Description': 'ID of the spec. Can only contain characters Aa-Zz, 0-9, -, and _. Searchable: priority level 3. Sortable: priority level 3.', 'Required': False}, {'Name': 'ListOrder', 'Type': 'integer', 'Description': 'List order of the spec. Searchable: priority level 2. Sortable: priority level 1.', 'Required': False}, {'Name': 'Name', 'Type': 'string', 'Description': 'Name of the spec. Required. Searchable: priority level 1. Sortable: priority level 2.', 'Required': True}, {'Name': 'DefaultValue', 'Type': 'string', 'Description': 'Default value of the spec. Max length 2000 characters.', 'Required': False}, {'Name': 'Required', 'Type': 'boolean', 'Description': 'Required of the spec. Searchable: priority level 4.', 'Required': False}, {'Name': 'AllowOpenText', 'Type': 'boolean', 'Description': 'Allow open text of the spec. Searchable: priority level 5.', 'Required': False}, {'Name': 'DefaultOptionID', 'Type': 'string', 'Description': 'ID of the default option.', 'Required': False}, {'Name': 'DefinesVariant', 'Type': 'boolean', 'Description': "True if each unique combinations of this Spec's Options map to unique Product Variants/SKUs.", 'Required': False}, {'Name': 'xp', 'Type': 'object', 'Description': 'Container for extended (custom) properties of the spec.', 'Required': False}]
```

**Responsestatus**: `200`

## Responsebody
```
{'OptionCount': 0, 'ID': '', 'ListOrder': 1, 'Name': '', 'DefaultValue': '', 'Required': False, 'AllowOpenText': False, 'DefaultOptionID': '', 'DefinesVariant': False, 'xp': {}}
```


| Parameters      | Description                    |
|------------------|---------------------------------|
| Name            | OptionCount                    |
| Type            | integer                        |
| Description     | Option count of the spec.      |
| Required        | False                          |


| Parameters      | Description                    |
|------------------|---------------------------------|
| Name            | ID                             |
| Type            | string                         |
| Description     | ID of the spec.                |
| Required        | False                          |


| Parameters      | Description                    |
|------------------|---------------------------------|
| Name            | ListOrder                      |
| Type            | integer                        |
| Description     | List order of the spec.        |
| Required        | False                          |


| Parameters      | Description                    |
|------------------|---------------------------------|
| Name            | Name                           |
| Type            | string                         |
| Description     | Name of the spec.              |
| Required        | True                           |


| Parameters      | Description                    |
|------------------|---------------------------------|
| Name            | DefaultValue                   |
| Type            | string                         |
| Description     | Default value of the spec.     |
| Required        | False                          |


| Parameters      | Description                    |
|------------------|---------------------------------|
| Name            | Required                       |
| Type            | boolean                        |
| Description     | Required of the spec.          |
| Required        | False                          |


| Parameters      | Description                    |
|------------------|---------------------------------|
| Name            | AllowOpenText                  |
| Type            | boolean                        |
| Description     | Allow open text of the spec.   |
| Required        | False                          |


| Parameters      | Description                    |
|------------------|---------------------------------|
| Name            | DefaultOptionID                |
| Type            | string                         |
| Description     | ID of the default option.      |
| Required        | False                          |


| Parameters      | Description                    |
|------------------|---------------------------------|
| Name            | DefinesVariant                 |
| Type            | boolean                        |
| Description     | True if each unique combinations of this Spec's Options map to unique Product Variants/SKUs. |
| Required        | False                          |


| Parameters      | Description                    |
|------------------|---------------------------------|
| Name            | xp                             |
| Type            | object                         |
| Description     | Container for extended (custom) properties of the spec. |
| Required        | False                          |

## `GET` `v1/specs/productassignments`
Get a list of spec product assignments

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
{'Meta': {'Page': 1, 'PageSize': 20, 'TotalCount': 25, 'TotalPages': 2, 'ItemRange': [1, 20]}, 'Items': [{'SpecID': '', 'ProductID': '', 'DefaultValue': '', 'DefaultOptionID': ''}]}
```


| Parameters      | Description                    |
|------------------|---------------------------------|
| Name            | SpecID                         |
| Type            | string                         |
| Description     | ID of the spec.                |
| Required        | False                          |


| Parameters      | Description                    |
|------------------|---------------------------------|
| Name            | ProductID                      |
| Type            | string                         |
| Description     | ID of the product.             |
| Required        | False                          |


| Parameters      | Description                    |
|------------------|---------------------------------|
| Name            | DefaultValue                   |
| Type            | string                         |
| Description     | Optional. When defined, overrides the DefaultValue set on the Spec for just this Product. |
| Required        | False                          |


| Parameters      | Description                    |
|------------------|---------------------------------|
| Name            | DefaultOptionID                |
| Type            | string                         |
| Description     | Optional. When defined, overrides the DefaultOptionID set on the Spec for just this Product. |
| Required        | False                          |

## `DELETE` `v1/specs/{specID}/productassignments/{productID}`
Delete a spec product assignment

| Parameters      | Description                    |
|------------------|---------------------------------|


| Parameters      | Description                    |
|------------------|---------------------------------|
| Name            | specID                         |
| Type            | string                         |
| Description     | ID of the spec.                |
| Required        | True                           |


| Parameters      | Description                    |
|------------------|---------------------------------|
| Name            | productID                      |
| Type            | string                         |
| Description     | ID of the product.             |
| Required        | True                           |

## Requestbody
**Responsestatus**: `204`

## Responsebody
## `POST` `v1/specs/productassignments`
Save a spec product assignment
## Requestbody
```
{'SpecID': '', 'ProductID': '', 'DefaultValue': '', 'DefaultOptionID': ''}
```

```
[{'Name': 'SpecID', 'Type': 'string', 'Description': 'ID of the spec. Searchable: priority level 1. Sortable: priority level 1.', 'Required': False}, {'Name': 'ProductID', 'Type': 'string', 'Description': 'ID of the product. Searchable: priority level 2. Sortable: priority level 2.', 'Required': False}, {'Name': 'DefaultValue', 'Type': 'string', 'Description': 'Optional. When defined, overrides the DefaultValue set on the Spec for just this Product.', 'Required': False}, {'Name': 'DefaultOptionID', 'Type': 'string', 'Description': 'Optional. When defined, overrides the DefaultOptionID set on the Spec for just this Product.', 'Required': False}]
```

**Responsestatus**: `204`

## Responsebody
## `POST` `v1/specs/{specID}/options`
Create a new spec option

| Parameters      | Description                    |
|------------------|---------------------------------|


| Parameters      | Description                    |
|------------------|---------------------------------|
| Name            | specID                         |
| Type            | string                         |
| Description     | ID of the spec.                |
| Required        | True                           |

## Requestbody
```
{'ID': '', 'Value': '', 'ListOrder': 1, 'IsOpenText': False, 'PriceMarkupType': 'NoMarkup', 'PriceMarkup': 0, 'xp': {}}
```

```
[{'Name': 'ID', 'Type': 'string', 'Description': 'ID of the spec option. Can only contain characters Aa-Zz, 0-9, -, and _. Searchable: priority level 2. Sortable: priority level 2.', 'Required': False}, {'Name': 'Value', 'Type': 'string', 'Description': 'Value of the spec option. Required. Max length 2000 characters. Searchable: priority level 1.', 'Required': True}, {'Name': 'ListOrder', 'Type': 'integer', 'Description': 'List order of the spec option. Searchable: priority level 4. Sortable: priority level 1.', 'Required': False}, {'Name': 'IsOpenText', 'Type': 'boolean', 'Description': 'Is open text of the spec option. Searchable: priority level 3.', 'Required': False}, {'Name': 'PriceMarkupType', 'Type': 'string', 'Description': 'Price markup type of the spec option. Searchable: priority level 5. Possible values: NoMarkup, AmountPerQuantity, AmountTotal, Percentage.', 'Required': False}, {'Name': 'PriceMarkup', 'Type': 'float', 'Description': 'Price markup of the spec option. Searchable: priority level 6.', 'Required': False}, {'Name': 'xp', 'Type': 'object', 'Description': 'Container for extended (custom) properties of the spec option.', 'Required': False}]
```

**Responsestatus**: `201`

## Responsebody
```
{'ID': '', 'Value': '', 'ListOrder': 1, 'IsOpenText': False, 'PriceMarkupType': 'NoMarkup', 'PriceMarkup': 0, 'xp': {}}
```


| Parameters      | Description                    |
|------------------|---------------------------------|
| Name            | ID                             |
| Type            | string                         |
| Description     | ID of the spec option.         |
| Required        | False                          |


| Parameters      | Description                    |
|------------------|---------------------------------|
| Name            | Value                          |
| Type            | string                         |
| Description     | Value of the spec option.      |
| Required        | True                           |


| Parameters      | Description                    |
|------------------|---------------------------------|
| Name            | ListOrder                      |
| Type            | integer                        |
| Description     | List order of the spec option. |
| Required        | False                          |


| Parameters      | Description                    |
|------------------|---------------------------------|
| Name            | IsOpenText                     |
| Type            | boolean                        |
| Description     | Is open text of the spec option. |
| Required        | False                          |


| Parameters      | Description                    |
|------------------|---------------------------------|
| Name            | PriceMarkupType                |
| Type            | string                         |
| Description     | Price markup type of the spec option. Possible values: NoMarkup, AmountPerQuantity, AmountTotal, Percentage. |
| Required        | False                          |


| Parameters      | Description                    |
|------------------|---------------------------------|
| Name            | PriceMarkup                    |
| Type            | float                          |
| Description     | Price markup of the spec option. |
| Required        | False                          |


| Parameters      | Description                    |
|------------------|---------------------------------|
| Name            | xp                             |
| Type            | object                         |
| Description     | Container for extended (custom) properties of the spec option. |
| Required        | False                          |

## `GET` `v1/specs/{specID}/options`
Get a list of spec options

| Parameters      | Description                    |
|------------------|---------------------------------|


| Parameters      | Description                    |
|------------------|---------------------------------|
| Name            | specID                         |
| Type            | string                         |
| Description     | ID of the spec.                |
| Required        | True                           |


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
{'Meta': {'Page': 1, 'PageSize': 20, 'TotalCount': 25, 'TotalPages': 2, 'ItemRange': [1, 20]}, 'Items': [{'ID': '', 'Value': '', 'ListOrder': 1, 'IsOpenText': False, 'PriceMarkupType': 'NoMarkup', 'PriceMarkup': 0, 'xp': {}}]}
```


| Parameters      | Description                    |
|------------------|---------------------------------|
| Name            | ID                             |
| Type            | string                         |
| Description     | ID of the spec option.         |
| Required        | False                          |


| Parameters      | Description                    |
|------------------|---------------------------------|
| Name            | Value                          |
| Type            | string                         |
| Description     | Value of the spec option.      |
| Required        | True                           |


| Parameters      | Description                    |
|------------------|---------------------------------|
| Name            | ListOrder                      |
| Type            | integer                        |
| Description     | List order of the spec option. |
| Required        | False                          |


| Parameters      | Description                    |
|------------------|---------------------------------|
| Name            | IsOpenText                     |
| Type            | boolean                        |
| Description     | Is open text of the spec option. |
| Required        | False                          |


| Parameters      | Description                    |
|------------------|---------------------------------|
| Name            | PriceMarkupType                |
| Type            | string                         |
| Description     | Price markup type of the spec option. Possible values: NoMarkup, AmountPerQuantity, AmountTotal, Percentage. |
| Required        | False                          |


| Parameters      | Description                    |
|------------------|---------------------------------|
| Name            | PriceMarkup                    |
| Type            | float                          |
| Description     | Price markup of the spec option. |
| Required        | False                          |


| Parameters      | Description                    |
|------------------|---------------------------------|
| Name            | xp                             |
| Type            | object                         |
| Description     | Container for extended (custom) properties of the spec option. |
| Required        | False                          |

## `PUT` `v1/specs/{specID}/options/{optionID}`
Create or update a spec option

| Parameters      | Description                    |
|------------------|---------------------------------|


| Parameters      | Description                    |
|------------------|---------------------------------|
| Name            | specID                         |
| Type            | string                         |
| Description     | ID of the spec.                |
| Required        | True                           |


| Parameters      | Description                    |
|------------------|---------------------------------|
| Name            | optionID                       |
| Type            | string                         |
| Description     | ID of the option.              |
| Required        | True                           |

## Requestbody
```
{'ID': '', 'Value': '', 'ListOrder': 1, 'IsOpenText': False, 'PriceMarkupType': 'NoMarkup', 'PriceMarkup': 0, 'xp': {}}
```

```
[{'Name': 'ID', 'Type': 'string', 'Description': 'ID of the spec option. Can only contain characters Aa-Zz, 0-9, -, and _. Searchable: priority level 2. Sortable: priority level 2.', 'Required': False}, {'Name': 'Value', 'Type': 'string', 'Description': 'Value of the spec option. Required. Max length 2000 characters. Searchable: priority level 1.', 'Required': True}, {'Name': 'ListOrder', 'Type': 'integer', 'Description': 'List order of the spec option. Searchable: priority level 4. Sortable: priority level 1.', 'Required': False}, {'Name': 'IsOpenText', 'Type': 'boolean', 'Description': 'Is open text of the spec option. Searchable: priority level 3.', 'Required': False}, {'Name': 'PriceMarkupType', 'Type': 'string', 'Description': 'Price markup type of the spec option. Searchable: priority level 5. Possible values: NoMarkup, AmountPerQuantity, AmountTotal, Percentage.', 'Required': False}, {'Name': 'PriceMarkup', 'Type': 'float', 'Description': 'Price markup of the spec option. Searchable: priority level 6.', 'Required': False}, {'Name': 'xp', 'Type': 'object', 'Description': 'Container for extended (custom) properties of the spec option.', 'Required': False}]
```

**Responsestatus**: `200`

## Responsebody
```
{'ID': '', 'Value': '', 'ListOrder': 1, 'IsOpenText': False, 'PriceMarkupType': 'NoMarkup', 'PriceMarkup': 0, 'xp': {}}
```


| Parameters      | Description                    |
|------------------|---------------------------------|
| Name            | ID                             |
| Type            | string                         |
| Description     | ID of the spec option.         |
| Required        | False                          |


| Parameters      | Description                    |
|------------------|---------------------------------|
| Name            | Value                          |
| Type            | string                         |
| Description     | Value of the spec option.      |
| Required        | True                           |


| Parameters      | Description                    |
|------------------|---------------------------------|
| Name            | ListOrder                      |
| Type            | integer                        |
| Description     | List order of the spec option. |
| Required        | False                          |


| Parameters      | Description                    |
|------------------|---------------------------------|
| Name            | IsOpenText                     |
| Type            | boolean                        |
| Description     | Is open text of the spec option. |
| Required        | False                          |


| Parameters      | Description                    |
|------------------|---------------------------------|
| Name            | PriceMarkupType                |
| Type            | string                         |
| Description     | Price markup type of the spec option. Possible values: NoMarkup, AmountPerQuantity, AmountTotal, Percentage. |
| Required        | False                          |


| Parameters      | Description                    |
|------------------|---------------------------------|
| Name            | PriceMarkup                    |
| Type            | float                          |
| Description     | Price markup of the spec option. |
| Required        | False                          |


| Parameters      | Description                    |
|------------------|---------------------------------|
| Name            | xp                             |
| Type            | object                         |
| Description     | Container for extended (custom) properties of the spec option. |
| Required        | False                          |

## `PATCH` `v1/specs/{specID}/options/{optionID}`
Partially update a spec option

| Parameters      | Description                    |
|------------------|---------------------------------|


| Parameters      | Description                    |
|------------------|---------------------------------|
| Name            | specID                         |
| Type            | string                         |
| Description     | ID of the spec.                |
| Required        | True                           |


| Parameters      | Description                    |
|------------------|---------------------------------|
| Name            | optionID                       |
| Type            | string                         |
| Description     | ID of the option.              |
| Required        | True                           |

## Requestbody
```
{'ID': '', 'Value': '', 'ListOrder': 1, 'IsOpenText': False, 'PriceMarkupType': 'NoMarkup', 'PriceMarkup': 0, 'xp': {}}
```

```
[{'Name': 'ID', 'Type': 'string', 'Description': 'ID of the spec option. Can only contain characters Aa-Zz, 0-9, -, and _. Searchable: priority level 2. Sortable: priority level 2.', 'Required': False}, {'Name': 'Value', 'Type': 'string', 'Description': 'Value of the spec option. Required. Max length 2000 characters. Searchable: priority level 1.', 'Required': True}, {'Name': 'ListOrder', 'Type': 'integer', 'Description': 'List order of the spec option. Searchable: priority level 4. Sortable: priority level 1.', 'Required': False}, {'Name': 'IsOpenText', 'Type': 'boolean', 'Description': 'Is open text of the spec option. Searchable: priority level 3.', 'Required': False}, {'Name': 'PriceMarkupType', 'Type': 'string', 'Description': 'Price markup type of the spec option. Searchable: priority level 5. Possible values: NoMarkup, AmountPerQuantity, AmountTotal, Percentage.', 'Required': False}, {'Name': 'PriceMarkup', 'Type': 'float', 'Description': 'Price markup of the spec option. Searchable: priority level 6.', 'Required': False}, {'Name': 'xp', 'Type': 'object', 'Description': 'Container for extended (custom) properties of the spec option.', 'Required': False}]
```

**Responsestatus**: `200`

## Responsebody
```
{'ID': '', 'Value': '', 'ListOrder': 1, 'IsOpenText': False, 'PriceMarkupType': 'NoMarkup', 'PriceMarkup': 0, 'xp': {}}
```


| Parameters      | Description                    |
|------------------|---------------------------------|
| Name            | ID                             |
| Type            | string                         |
| Description     | ID of the spec option.         |
| Required        | False                          |


| Parameters      | Description                    |
|------------------|---------------------------------|
| Name            | Value                          |
| Type            | string                         |
| Description     | Value of the spec option.      |
| Required        | True                           |


| Parameters      | Description                    |
|------------------|---------------------------------|
| Name            | ListOrder                      |
| Type            | integer                        |
| Description     | List order of the spec option. |
| Required        | False                          |


| Parameters      | Description                    |
|------------------|---------------------------------|
| Name            | IsOpenText                     |
| Type            | boolean                        |
| Description     | Is open text of the spec option. |
| Required        | False                          |


| Parameters      | Description                    |
|------------------|---------------------------------|
| Name            | PriceMarkupType                |
| Type            | string                         |
| Description     | Price markup type of the spec option. Possible values: NoMarkup, AmountPerQuantity, AmountTotal, Percentage. |
| Required        | False                          |


| Parameters      | Description                    |
|------------------|---------------------------------|
| Name            | PriceMarkup                    |
| Type            | float                          |
| Description     | Price markup of the spec option. |
| Required        | False                          |


| Parameters      | Description                    |
|------------------|---------------------------------|
| Name            | xp                             |
| Type            | object                         |
| Description     | Container for extended (custom) properties of the spec option. |
| Required        | False                          |

## `GET` `v1/specs/{specID}/options/{optionID}`
Get a single spec option

| Parameters      | Description                    |
|------------------|---------------------------------|


| Parameters      | Description                    |
|------------------|---------------------------------|
| Name            | specID                         |
| Type            | string                         |
| Description     | ID of the spec.                |
| Required        | True                           |


| Parameters      | Description                    |
|------------------|---------------------------------|
| Name            | optionID                       |
| Type            | string                         |
| Description     | ID of the option.              |
| Required        | True                           |

## Requestbody
**Responsestatus**: `200`

## Responsebody
```
{'ID': '', 'Value': '', 'ListOrder': 1, 'IsOpenText': False, 'PriceMarkupType': 'NoMarkup', 'PriceMarkup': 0, 'xp': {}}
```


| Parameters      | Description                    |
|------------------|---------------------------------|
| Name            | ID                             |
| Type            | string                         |
| Description     | ID of the spec option.         |
| Required        | False                          |


| Parameters      | Description                    |
|------------------|---------------------------------|
| Name            | Value                          |
| Type            | string                         |
| Description     | Value of the spec option.      |
| Required        | True                           |


| Parameters      | Description                    |
|------------------|---------------------------------|
| Name            | ListOrder                      |
| Type            | integer                        |
| Description     | List order of the spec option. |
| Required        | False                          |


| Parameters      | Description                    |
|------------------|---------------------------------|
| Name            | IsOpenText                     |
| Type            | boolean                        |
| Description     | Is open text of the spec option. |
| Required        | False                          |


| Parameters      | Description                    |
|------------------|---------------------------------|
| Name            | PriceMarkupType                |
| Type            | string                         |
| Description     | Price markup type of the spec option. Possible values: NoMarkup, AmountPerQuantity, AmountTotal, Percentage. |
| Required        | False                          |


| Parameters      | Description                    |
|------------------|---------------------------------|
| Name            | PriceMarkup                    |
| Type            | float                          |
| Description     | Price markup of the spec option. |
| Required        | False                          |


| Parameters      | Description                    |
|------------------|---------------------------------|
| Name            | xp                             |
| Type            | object                         |
| Description     | Container for extended (custom) properties of the spec option. |
| Required        | False                          |

## `DELETE` `v1/specs/{specID}/options/{optionID}`
Delete a spec option

| Parameters      | Description                    |
|------------------|---------------------------------|


| Parameters      | Description                    |
|------------------|---------------------------------|
| Name            | specID                         |
| Type            | string                         |
| Description     | ID of the spec.                |
| Required        | True                           |


| Parameters      | Description                    |
|------------------|---------------------------------|
| Name            | optionID                       |
| Type            | string                         |
| Description     | ID of the option.              |
| Required        | True                           |

## Requestbody
**Responsestatus**: `204`

## Responsebody