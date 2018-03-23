---
title: Categories
date: 2018-03-23
category: API Reference
tags: Product Catalogs
slug: Categories
---
Categories are used within a catalog to group and place content for a
specific audience. Content can be in the form of another category,
nested categories, products or HTML.

---

## `GET` `v1/catalogs/{catalogID}/categories/{categoryID}`
Get a single category

| Parameters      | Description                    |
|------------------|---------------------------------|


| Parameters      | Description                    |
|------------------|---------------------------------|
| Name            | catalogID                      |
| Type            | string                         |
| Description     | ID of the catalog.             |
| Required        | True                           |


| Parameters      | Description                    |
|------------------|---------------------------------|
| Name            | categoryID                     |
| Type            | string                         |
| Description     | ID of the category.            |
| Required        | True                           |

## Requestbody
**Responsestatus**: `200`

## Responsebody
```
{'ID': '', 'Name': '', 'Description': '', 'ListOrder': 1, 'Active': False, 'ParentID': '', 'ChildCount': 0, 'xp': {}}
```


| Parameters      | Description                    |
|------------------|---------------------------------|
| Name            | ID                             |
| Type            | string                         |
| Description     | ID of the category.            |
| Required        | False                          |


| Parameters      | Description                    |
|------------------|---------------------------------|
| Name            | Name                           |
| Type            | string                         |
| Description     | Name of the category.          |
| Required        | True                           |


| Parameters      | Description                    |
|------------------|---------------------------------|
| Name            | Description                    |
| Type            | string                         |
| Description     | Description of the category.   |
| Required        | False                          |


| Parameters      | Description                    |
|------------------|---------------------------------|
| Name            | ListOrder                      |
| Type            | integer                        |
| Description     | Order that the category appears within its parent or catalog (if root level). |
| Required        | False                          |


| Parameters      | Description                    |
|------------------|---------------------------------|
| Name            | Active                         |
| Type            | boolean                        |
| Description     | If false, buyers cannot see this Category or any Categories or Products under it. |
| Required        | False                          |


| Parameters      | Description                    |
|------------------|---------------------------------|
| Name            | ParentID                       |
| Type            | string                         |
| Description     | ID of the parent category.     |
| Required        | False                          |


| Parameters      | Description                    |
|------------------|---------------------------------|
| Name            | ChildCount                     |
| Type            | integer                        |
| Description     | Number of categories that are *immediate* children of this category. |
| Required        | False                          |


| Parameters      | Description                    |
|------------------|---------------------------------|
| Name            | xp                             |
| Type            | object                         |
| Description     | Container for extended (custom) properties of the category. |
| Required        | False                          |

## `GET` `v1/catalogs/{catalogID}/categories`
Get a list of categories

| Parameters      | Description                    |
|------------------|---------------------------------|


| Parameters      | Description                    |
|------------------|---------------------------------|
| Name            | catalogID                      |
| Type            | string                         |
| Description     | ID of the catalog.             |
| Required        | True                           |


| Parameters      | Description                    |
|------------------|---------------------------------|
| Name            | depth                          |
| Type            | string                         |
| Description     | Depth of the category.         |
| Required        | False                          |


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
{'Meta': {'Page': 1, 'PageSize': 20, 'TotalCount': 25, 'TotalPages': 2, 'ItemRange': [1, 20]}, 'Items': [{'ID': '', 'Name': '', 'Description': '', 'ListOrder': 1, 'Active': False, 'ParentID': '', 'ChildCount': 0, 'xp': {}}]}
```


| Parameters      | Description                    |
|------------------|---------------------------------|
| Name            | ID                             |
| Type            | string                         |
| Description     | ID of the category.            |
| Required        | False                          |


| Parameters      | Description                    |
|------------------|---------------------------------|
| Name            | Name                           |
| Type            | string                         |
| Description     | Name of the category.          |
| Required        | True                           |


| Parameters      | Description                    |
|------------------|---------------------------------|
| Name            | Description                    |
| Type            | string                         |
| Description     | Description of the category.   |
| Required        | False                          |


| Parameters      | Description                    |
|------------------|---------------------------------|
| Name            | ListOrder                      |
| Type            | integer                        |
| Description     | Order that the category appears within its parent or catalog (if root level). |
| Required        | False                          |


| Parameters      | Description                    |
|------------------|---------------------------------|
| Name            | Active                         |
| Type            | boolean                        |
| Description     | If false, buyers cannot see this Category or any Categories or Products under it. |
| Required        | False                          |


| Parameters      | Description                    |
|------------------|---------------------------------|
| Name            | ParentID                       |
| Type            | string                         |
| Description     | ID of the parent category.     |
| Required        | False                          |


| Parameters      | Description                    |
|------------------|---------------------------------|
| Name            | ChildCount                     |
| Type            | integer                        |
| Description     | Number of categories that are *immediate* children of this category. |
| Required        | False                          |


| Parameters      | Description                    |
|------------------|---------------------------------|
| Name            | xp                             |
| Type            | object                         |
| Description     | Container for extended (custom) properties of the category. |
| Required        | False                          |

## `POST` `v1/catalogs/{catalogID}/categories`
Create a new category

| Parameters      | Description                    |
|------------------|---------------------------------|


| Parameters      | Description                    |
|------------------|---------------------------------|
| Name            | catalogID                      |
| Type            | string                         |
| Description     | ID of the catalog.             |
| Required        | True                           |

## Requestbody
```
{'ID': '', 'Name': '', 'Description': '', 'ListOrder': 1, 'Active': False, 'ParentID': '', 'xp': {}}
```

```
[{'Name': 'ID', 'Type': 'string', 'Description': 'ID of the category. Can only contain characters Aa-Zz, 0-9, -, and _. Searchable: priority level 1. Sortable.', 'Required': False}, {'Name': 'Name', 'Type': 'string', 'Description': 'Name of the category. Required. Max length 100 characters. Searchable: priority level 2. Sortable.', 'Required': True}, {'Name': 'Description', 'Type': 'string', 'Description': 'Description of the category. Max length 2000 characters. Searchable: priority level 3.', 'Required': False}, {'Name': 'ListOrder', 'Type': 'integer', 'Description': 'Order that the category appears within its parent or catalog (if root level).', 'Required': False}, {'Name': 'Active', 'Type': 'boolean', 'Description': 'If false, buyers cannot see this Category or any Categories or Products under it.', 'Required': False}, {'Name': 'ParentID', 'Type': 'string', 'Description': 'ID of the parent category.', 'Required': False}, {'Name': 'xp', 'Type': 'object', 'Description': 'Container for extended (custom) properties of the category.', 'Required': False}]
```

**Responsestatus**: `201`

## Responsebody
```
{'ID': '', 'Name': '', 'Description': '', 'ListOrder': 1, 'Active': False, 'ParentID': '', 'ChildCount': 0, 'xp': {}}
```


| Parameters      | Description                    |
|------------------|---------------------------------|
| Name            | ID                             |
| Type            | string                         |
| Description     | ID of the category.            |
| Required        | False                          |


| Parameters      | Description                    |
|------------------|---------------------------------|
| Name            | Name                           |
| Type            | string                         |
| Description     | Name of the category.          |
| Required        | True                           |


| Parameters      | Description                    |
|------------------|---------------------------------|
| Name            | Description                    |
| Type            | string                         |
| Description     | Description of the category.   |
| Required        | False                          |


| Parameters      | Description                    |
|------------------|---------------------------------|
| Name            | ListOrder                      |
| Type            | integer                        |
| Description     | Order that the category appears within its parent or catalog (if root level). |
| Required        | False                          |


| Parameters      | Description                    |
|------------------|---------------------------------|
| Name            | Active                         |
| Type            | boolean                        |
| Description     | If false, buyers cannot see this Category or any Categories or Products under it. |
| Required        | False                          |


| Parameters      | Description                    |
|------------------|---------------------------------|
| Name            | ParentID                       |
| Type            | string                         |
| Description     | ID of the parent category.     |
| Required        | False                          |


| Parameters      | Description                    |
|------------------|---------------------------------|
| Name            | ChildCount                     |
| Type            | integer                        |
| Description     | Number of categories that are *immediate* children of this category. |
| Required        | False                          |


| Parameters      | Description                    |
|------------------|---------------------------------|
| Name            | xp                             |
| Type            | object                         |
| Description     | Container for extended (custom) properties of the category. |
| Required        | False                          |

## `PUT` `v1/catalogs/{catalogID}/categories/{categoryID}`
Create or update a category

| Parameters      | Description                    |
|------------------|---------------------------------|


| Parameters      | Description                    |
|------------------|---------------------------------|
| Name            | catalogID                      |
| Type            | string                         |
| Description     | ID of the catalog.             |
| Required        | True                           |


| Parameters      | Description                    |
|------------------|---------------------------------|
| Name            | categoryID                     |
| Type            | string                         |
| Description     | ID of the category.            |
| Required        | True                           |

## Requestbody
```
{'ID': '', 'Name': '', 'Description': '', 'ListOrder': 1, 'Active': False, 'ParentID': '', 'xp': {}}
```

```
[{'Name': 'ID', 'Type': 'string', 'Description': 'ID of the category. Can only contain characters Aa-Zz, 0-9, -, and _. Searchable: priority level 1. Sortable.', 'Required': False}, {'Name': 'Name', 'Type': 'string', 'Description': 'Name of the category. Required. Max length 100 characters. Searchable: priority level 2. Sortable.', 'Required': True}, {'Name': 'Description', 'Type': 'string', 'Description': 'Description of the category. Max length 2000 characters. Searchable: priority level 3.', 'Required': False}, {'Name': 'ListOrder', 'Type': 'integer', 'Description': 'Order that the category appears within its parent or catalog (if root level).', 'Required': False}, {'Name': 'Active', 'Type': 'boolean', 'Description': 'If false, buyers cannot see this Category or any Categories or Products under it.', 'Required': False}, {'Name': 'ParentID', 'Type': 'string', 'Description': 'ID of the parent category.', 'Required': False}, {'Name': 'xp', 'Type': 'object', 'Description': 'Container for extended (custom) properties of the category.', 'Required': False}]
```

**Responsestatus**: `200`

## Responsebody
```
{'ID': '', 'Name': '', 'Description': '', 'ListOrder': 1, 'Active': False, 'ParentID': '', 'ChildCount': 0, 'xp': {}}
```


| Parameters      | Description                    |
|------------------|---------------------------------|
| Name            | ID                             |
| Type            | string                         |
| Description     | ID of the category.            |
| Required        | False                          |


| Parameters      | Description                    |
|------------------|---------------------------------|
| Name            | Name                           |
| Type            | string                         |
| Description     | Name of the category.          |
| Required        | True                           |


| Parameters      | Description                    |
|------------------|---------------------------------|
| Name            | Description                    |
| Type            | string                         |
| Description     | Description of the category.   |
| Required        | False                          |


| Parameters      | Description                    |
|------------------|---------------------------------|
| Name            | ListOrder                      |
| Type            | integer                        |
| Description     | Order that the category appears within its parent or catalog (if root level). |
| Required        | False                          |


| Parameters      | Description                    |
|------------------|---------------------------------|
| Name            | Active                         |
| Type            | boolean                        |
| Description     | If false, buyers cannot see this Category or any Categories or Products under it. |
| Required        | False                          |


| Parameters      | Description                    |
|------------------|---------------------------------|
| Name            | ParentID                       |
| Type            | string                         |
| Description     | ID of the parent category.     |
| Required        | False                          |


| Parameters      | Description                    |
|------------------|---------------------------------|
| Name            | ChildCount                     |
| Type            | integer                        |
| Description     | Number of categories that are *immediate* children of this category. |
| Required        | False                          |


| Parameters      | Description                    |
|------------------|---------------------------------|
| Name            | xp                             |
| Type            | object                         |
| Description     | Container for extended (custom) properties of the category. |
| Required        | False                          |

## `DELETE` `v1/catalogs/{catalogID}/categories/{categoryID}`
Delete a category

| Parameters      | Description                    |
|------------------|---------------------------------|


| Parameters      | Description                    |
|------------------|---------------------------------|
| Name            | catalogID                      |
| Type            | string                         |
| Description     | ID of the catalog.             |
| Required        | True                           |


| Parameters      | Description                    |
|------------------|---------------------------------|
| Name            | categoryID                     |
| Type            | string                         |
| Description     | ID of the category.            |
| Required        | True                           |

## Requestbody
**Responsestatus**: `204`

## Responsebody
## `PATCH` `v1/catalogs/{catalogID}/categories/{categoryID}`
Partially update a category

| Parameters      | Description                    |
|------------------|---------------------------------|


| Parameters      | Description                    |
|------------------|---------------------------------|
| Name            | catalogID                      |
| Type            | string                         |
| Description     | ID of the catalog.             |
| Required        | True                           |


| Parameters      | Description                    |
|------------------|---------------------------------|
| Name            | categoryID                     |
| Type            | string                         |
| Description     | ID of the category.            |
| Required        | True                           |

## Requestbody
```
{'ID': '', 'Name': '', 'Description': '', 'ListOrder': 1, 'Active': False, 'ParentID': '', 'xp': {}}
```

```
[{'Name': 'ID', 'Type': 'string', 'Description': 'ID of the category. Can only contain characters Aa-Zz, 0-9, -, and _. Searchable: priority level 1. Sortable.', 'Required': False}, {'Name': 'Name', 'Type': 'string', 'Description': 'Name of the category. Required. Max length 100 characters. Searchable: priority level 2. Sortable.', 'Required': True}, {'Name': 'Description', 'Type': 'string', 'Description': 'Description of the category. Max length 2000 characters. Searchable: priority level 3.', 'Required': False}, {'Name': 'ListOrder', 'Type': 'integer', 'Description': 'Order that the category appears within its parent or catalog (if root level).', 'Required': False}, {'Name': 'Active', 'Type': 'boolean', 'Description': 'If false, buyers cannot see this Category or any Categories or Products under it.', 'Required': False}, {'Name': 'ParentID', 'Type': 'string', 'Description': 'ID of the parent category.', 'Required': False}, {'Name': 'xp', 'Type': 'object', 'Description': 'Container for extended (custom) properties of the category.', 'Required': False}]
```

**Responsestatus**: `200`

## Responsebody
```
{'ID': '', 'Name': '', 'Description': '', 'ListOrder': 1, 'Active': False, 'ParentID': '', 'ChildCount': 0, 'xp': {}}
```


| Parameters      | Description                    |
|------------------|---------------------------------|
| Name            | ID                             |
| Type            | string                         |
| Description     | ID of the category.            |
| Required        | False                          |


| Parameters      | Description                    |
|------------------|---------------------------------|
| Name            | Name                           |
| Type            | string                         |
| Description     | Name of the category.          |
| Required        | True                           |


| Parameters      | Description                    |
|------------------|---------------------------------|
| Name            | Description                    |
| Type            | string                         |
| Description     | Description of the category.   |
| Required        | False                          |


| Parameters      | Description                    |
|------------------|---------------------------------|
| Name            | ListOrder                      |
| Type            | integer                        |
| Description     | Order that the category appears within its parent or catalog (if root level). |
| Required        | False                          |


| Parameters      | Description                    |
|------------------|---------------------------------|
| Name            | Active                         |
| Type            | boolean                        |
| Description     | If false, buyers cannot see this Category or any Categories or Products under it. |
| Required        | False                          |


| Parameters      | Description                    |
|------------------|---------------------------------|
| Name            | ParentID                       |
| Type            | string                         |
| Description     | ID of the parent category.     |
| Required        | False                          |


| Parameters      | Description                    |
|------------------|---------------------------------|
| Name            | ChildCount                     |
| Type            | integer                        |
| Description     | Number of categories that are *immediate* children of this category. |
| Required        | False                          |


| Parameters      | Description                    |
|------------------|---------------------------------|
| Name            | xp                             |
| Type            | object                         |
| Description     | Container for extended (custom) properties of the category. |
| Required        | False                          |

## `GET` `v1/catalogs/{catalogID}/categories/assignments`
Get a list of category assignments

| Parameters      | Description                    |
|------------------|---------------------------------|


| Parameters      | Description                    |
|------------------|---------------------------------|
| Name            | catalogID                      |
| Type            | string                         |
| Description     | ID of the catalog.             |
| Required        | True                           |


| Parameters      | Description                    |
|------------------|---------------------------------|
| Name            | categoryID                     |
| Type            | string                         |
| Description     | ID of the category.            |
| Required        | False                          |


| Parameters      | Description                    |
|------------------|---------------------------------|
| Name            | buyerID                        |
| Type            | string                         |
| Description     | ID of the buyer.               |
| Required        | False                          |


| Parameters      | Description                    |
|------------------|---------------------------------|
| Name            | userID                         |
| Type            | string                         |
| Description     | ID of the user.                |
| Required        | False                          |


| Parameters      | Description                    |
|------------------|---------------------------------|
| Name            | userGroupID                    |
| Type            | string                         |
| Description     | ID of the user group.          |
| Required        | False                          |


| Parameters      | Description                    |
|------------------|---------------------------------|
| Name            | level                          |
| Type            | string                         |
| Description     | Level of the category assignment. Possible values: User, Group, Company. |
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

## Requestbody
**Responsestatus**: `200`

## Responsebody
```
{'Meta': {'Page': 1, 'PageSize': 20, 'TotalCount': 25, 'TotalPages': 2, 'ItemRange': [1, 20]}, 'Items': [{'CategoryID': '', 'BuyerID': '', 'UserGroupID': '', 'Visible': False, 'ViewAllProducts': False}]}
```


| Parameters      | Description                    |
|------------------|---------------------------------|
| Name            | CategoryID                     |
| Type            | string                         |
| Description     | ID of the category.            |
| Required        | True                           |


| Parameters      | Description                    |
|------------------|---------------------------------|
| Name            | BuyerID                        |
| Type            | string                         |
| Description     | ID of the buyer.               |
| Required        | True                           |


| Parameters      | Description                    |
|------------------|---------------------------------|
| Name            | UserGroupID                    |
| Type            | string                         |
| Description     | ID of the user group.          |
| Required        | False                          |


| Parameters      | Description                    |
|------------------|---------------------------------|
| Name            | Visible                        |
| Type            | boolean                        |
| Description     | Optional. Set to null to inherit from parent category or catlog level. |
| Required        | False                          |


| Parameters      | Description                    |
|------------------|---------------------------------|
| Name            | ViewAllProducts                |
| Type            | boolean                        |
| Description     | Optional. Set to null to inherit from parent category or catlog level. |
| Required        | False                          |

## `DELETE` `v1/catalogs/{catalogID}/categories/{categoryID}/assignments`
Delete a category assignment

| Parameters      | Description                    |
|------------------|---------------------------------|


| Parameters      | Description                    |
|------------------|---------------------------------|
| Name            | catalogID                      |
| Type            | string                         |
| Description     | ID of the catalog.             |
| Required        | True                           |


| Parameters      | Description                    |
|------------------|---------------------------------|
| Name            | categoryID                     |
| Type            | string                         |
| Description     | ID of the category.            |
| Required        | True                           |


| Parameters      | Description                    |
|------------------|---------------------------------|
| Name            | buyerID                        |
| Type            | string                         |
| Description     | ID of the buyer.               |
| Required        | True                           |


| Parameters      | Description                    |
|------------------|---------------------------------|
| Name            | userID                         |
| Type            | string                         |
| Description     | ID of the user.                |
| Required        | False                          |


| Parameters      | Description                    |
|------------------|---------------------------------|
| Name            | userGroupID                    |
| Type            | string                         |
| Description     | ID of the user group.          |
| Required        | False                          |

## Requestbody
**Responsestatus**: `204`

## Responsebody
## `POST` `v1/catalogs/{catalogID}/categories/assignments`
Save a category assignment

| Parameters      | Description                    |
|------------------|---------------------------------|


| Parameters      | Description                    |
|------------------|---------------------------------|
| Name            | catalogID                      |
| Type            | string                         |
| Description     | ID of the catalog.             |
| Required        | True                           |

## Requestbody
```
{'CategoryID': '', 'BuyerID': '', 'UserGroupID': '', 'Visible': False, 'ViewAllProducts': False}
```

```
[{'Name': 'CategoryID', 'Type': 'string', 'Description': 'ID of the category. Required. Sortable: priority level 1.', 'Required': True}, {'Name': 'BuyerID', 'Type': 'string', 'Description': 'ID of the buyer. Required. Sortable: priority level 2.', 'Required': True}, {'Name': 'UserGroupID', 'Type': 'string', 'Description': 'ID of the user group.', 'Required': False}, {'Name': 'Visible', 'Type': 'boolean', 'Description': 'Optional. Set to null to inherit from parent category or catlog level.', 'Required': False}, {'Name': 'ViewAllProducts', 'Type': 'boolean', 'Description': 'Optional. Set to null to inherit from parent category or catlog level.', 'Required': False}]
```

**Responsestatus**: `204`

## Responsebody
## `GET` `v1/catalogs/{catalogID}/categories/productassignments`
Get a list of category product assignments

| Parameters      | Description                    |
|------------------|---------------------------------|


| Parameters      | Description                    |
|------------------|---------------------------------|
| Name            | catalogID                      |
| Type            | string                         |
| Description     | ID of the catalog.             |
| Required        | True                           |


| Parameters      | Description                    |
|------------------|---------------------------------|
| Name            | categoryID                     |
| Type            | string                         |
| Description     | ID of the category.            |
| Required        | False                          |


| Parameters      | Description                    |
|------------------|---------------------------------|
| Name            | productID                      |
| Type            | string                         |
| Description     | ID of the product.             |
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

## Requestbody
**Responsestatus**: `200`

## Responsebody
```
{'Meta': {'Page': 1, 'PageSize': 20, 'TotalCount': 25, 'TotalPages': 2, 'ItemRange': [1, 20]}, 'Items': [{'CategoryID': '', 'ProductID': '', 'ListOrder': 1}]}
```


| Parameters      | Description                    |
|------------------|---------------------------------|
| Name            | CategoryID                     |
| Type            | string                         |
| Description     | ID of the category.            |
| Required        | True                           |


| Parameters      | Description                    |
|------------------|---------------------------------|
| Name            | ProductID                      |
| Type            | string                         |
| Description     | ID of the product.             |
| Required        | True                           |


| Parameters      | Description                    |
|------------------|---------------------------------|
| Name            | ListOrder                      |
| Type            | integer                        |
| Description     | List order of the category product assignment. |
| Required        | False                          |

## `POST` `v1/catalogs/{catalogID}/categories/productassignments`
Save a category product assignment

| Parameters      | Description                    |
|------------------|---------------------------------|


| Parameters      | Description                    |
|------------------|---------------------------------|
| Name            | catalogID                      |
| Type            | string                         |
| Description     | ID of the catalog.             |
| Required        | True                           |

## Requestbody
```
{'CategoryID': '', 'ProductID': '', 'ListOrder': 1}
```

```
[{'Name': 'CategoryID', 'Type': 'string', 'Description': 'ID of the category. Required.', 'Required': True}, {'Name': 'ProductID', 'Type': 'string', 'Description': 'ID of the product. Required.', 'Required': True}, {'Name': 'ListOrder', 'Type': 'integer', 'Description': 'List order of the category product assignment.', 'Required': False}]
```

**Responsestatus**: `204`

## Responsebody
## `DELETE` `v1/catalogs/{catalogID}/categories/{categoryID}/productassignments/{productID}`
Delete a category product assignment

| Parameters      | Description                    |
|------------------|---------------------------------|


| Parameters      | Description                    |
|------------------|---------------------------------|
| Name            | catalogID                      |
| Type            | string                         |
| Description     | ID of the catalog.             |
| Required        | True                           |


| Parameters      | Description                    |
|------------------|---------------------------------|
| Name            | categoryID                     |
| Type            | string                         |
| Description     | ID of the category.            |
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