---
title: Catalogs
date: 2018-03-23
category: API Reference
tags: Product Catalogs
slug: Catalogs
---
A Catalog represents a group of categories used to group and place
content for a specific audience. All buyers are issued and assigned a
default catalog upon creation. Catalogs can be shared between buyers
using assignments.

---

## `GET` `v1/catalogs/{catalogID}`
Get a single catalog

| Parameters      | Description                    |
|------------------|---------------------------------|


| Parameters      | Description                    |
|------------------|---------------------------------|
| Name            | catalogID                      |
| Type            | string                         |
| Description     | ID of the catalog.             |
| Required        | True                           |

## Requestbody
**Responsestatus**: `200`

## Responsebody
```
{'ID': '', 'Name': '', 'Description': '', 'Active': False, 'CategoryCount': 0, 'xp': {}}
```


| Parameters      | Description                    |
|------------------|---------------------------------|
| Name            | ID                             |
| Type            | string                         |
| Description     | ID of the catalog.             |
| Required        | False                          |


| Parameters      | Description                    |
|------------------|---------------------------------|
| Name            | Name                           |
| Type            | string                         |
| Description     | Name of the catalog.           |
| Required        | True                           |


| Parameters      | Description                    |
|------------------|---------------------------------|
| Name            | Description                    |
| Type            | string                         |
| Description     | Description of the catalog.    |
| Required        | False                          |


| Parameters      | Description                    |
|------------------|---------------------------------|
| Name            | Active                         |
| Type            | boolean                        |
| Description     | Active of the catalog.         |
| Required        | False                          |


| Parameters      | Description                    |
|------------------|---------------------------------|
| Name            | CategoryCount                  |
| Type            | integer                        |
| Description     | Category count of the catalog. |
| Required        | False                          |


| Parameters      | Description                    |
|------------------|---------------------------------|
| Name            | xp                             |
| Type            | object                         |
| Description     | Container for extended (custom) properties of the catalog. |
| Required        | False                          |

## `GET` `v1/catalogs`
Get a list of catalogs

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
{'Meta': {'Page': 1, 'PageSize': 20, 'TotalCount': 25, 'TotalPages': 2, 'ItemRange': [1, 20]}, 'Items': [{'ID': '', 'Name': '', 'Description': '', 'Active': False, 'CategoryCount': 0, 'xp': {}}]}
```


| Parameters      | Description                    |
|------------------|---------------------------------|
| Name            | ID                             |
| Type            | string                         |
| Description     | ID of the catalog.             |
| Required        | False                          |


| Parameters      | Description                    |
|------------------|---------------------------------|
| Name            | Name                           |
| Type            | string                         |
| Description     | Name of the catalog.           |
| Required        | True                           |


| Parameters      | Description                    |
|------------------|---------------------------------|
| Name            | Description                    |
| Type            | string                         |
| Description     | Description of the catalog.    |
| Required        | False                          |


| Parameters      | Description                    |
|------------------|---------------------------------|
| Name            | Active                         |
| Type            | boolean                        |
| Description     | Active of the catalog.         |
| Required        | False                          |


| Parameters      | Description                    |
|------------------|---------------------------------|
| Name            | CategoryCount                  |
| Type            | integer                        |
| Description     | Category count of the catalog. |
| Required        | False                          |


| Parameters      | Description                    |
|------------------|---------------------------------|
| Name            | xp                             |
| Type            | object                         |
| Description     | Container for extended (custom) properties of the catalog. |
| Required        | False                          |

## `POST` `v1/catalogs`
Create a new catalog
## Requestbody
```
{'ID': '', 'Name': '', 'Description': '', 'Active': False, 'xp': {}}
```

```
[{'Name': 'ID', 'Type': 'string', 'Description': 'ID of the catalog. Can only contain characters Aa-Zz, 0-9, -, and _. Searchable: priority level 1. Sortable: priority level 2.', 'Required': False}, {'Name': 'Name', 'Type': 'string', 'Description': 'Name of the catalog. Required. Max length 100 characters. Searchable: priority level 2. Sortable: priority level 1.', 'Required': True}, {'Name': 'Description', 'Type': 'string', 'Description': 'Description of the catalog. Max length 2000 characters. Searchable: priority level 3.', 'Required': False}, {'Name': 'Active', 'Type': 'boolean', 'Description': 'Active of the catalog.', 'Required': False}, {'Name': 'xp', 'Type': 'object', 'Description': 'Container for extended (custom) properties of the catalog.', 'Required': False}]
```

**Responsestatus**: `201`

## Responsebody
```
{'ID': '', 'Name': '', 'Description': '', 'Active': False, 'CategoryCount': 0, 'xp': {}}
```


| Parameters      | Description                    |
|------------------|---------------------------------|
| Name            | ID                             |
| Type            | string                         |
| Description     | ID of the catalog.             |
| Required        | False                          |


| Parameters      | Description                    |
|------------------|---------------------------------|
| Name            | Name                           |
| Type            | string                         |
| Description     | Name of the catalog.           |
| Required        | True                           |


| Parameters      | Description                    |
|------------------|---------------------------------|
| Name            | Description                    |
| Type            | string                         |
| Description     | Description of the catalog.    |
| Required        | False                          |


| Parameters      | Description                    |
|------------------|---------------------------------|
| Name            | Active                         |
| Type            | boolean                        |
| Description     | Active of the catalog.         |
| Required        | False                          |


| Parameters      | Description                    |
|------------------|---------------------------------|
| Name            | CategoryCount                  |
| Type            | integer                        |
| Description     | Category count of the catalog. |
| Required        | False                          |


| Parameters      | Description                    |
|------------------|---------------------------------|
| Name            | xp                             |
| Type            | object                         |
| Description     | Container for extended (custom) properties of the catalog. |
| Required        | False                          |

## `PUT` `v1/catalogs/{catalogID}`
Create or update a catalog

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
{'ID': '', 'Name': '', 'Description': '', 'Active': False, 'xp': {}}
```

```
[{'Name': 'ID', 'Type': 'string', 'Description': 'ID of the catalog. Can only contain characters Aa-Zz, 0-9, -, and _. Searchable: priority level 1. Sortable: priority level 2.', 'Required': False}, {'Name': 'Name', 'Type': 'string', 'Description': 'Name of the catalog. Required. Max length 100 characters. Searchable: priority level 2. Sortable: priority level 1.', 'Required': True}, {'Name': 'Description', 'Type': 'string', 'Description': 'Description of the catalog. Max length 2000 characters. Searchable: priority level 3.', 'Required': False}, {'Name': 'Active', 'Type': 'boolean', 'Description': 'Active of the catalog.', 'Required': False}, {'Name': 'xp', 'Type': 'object', 'Description': 'Container for extended (custom) properties of the catalog.', 'Required': False}]
```

**Responsestatus**: `200`

## Responsebody
```
{'ID': '', 'Name': '', 'Description': '', 'Active': False, 'CategoryCount': 0, 'xp': {}}
```


| Parameters      | Description                    |
|------------------|---------------------------------|
| Name            | ID                             |
| Type            | string                         |
| Description     | ID of the catalog.             |
| Required        | False                          |


| Parameters      | Description                    |
|------------------|---------------------------------|
| Name            | Name                           |
| Type            | string                         |
| Description     | Name of the catalog.           |
| Required        | True                           |


| Parameters      | Description                    |
|------------------|---------------------------------|
| Name            | Description                    |
| Type            | string                         |
| Description     | Description of the catalog.    |
| Required        | False                          |


| Parameters      | Description                    |
|------------------|---------------------------------|
| Name            | Active                         |
| Type            | boolean                        |
| Description     | Active of the catalog.         |
| Required        | False                          |


| Parameters      | Description                    |
|------------------|---------------------------------|
| Name            | CategoryCount                  |
| Type            | integer                        |
| Description     | Category count of the catalog. |
| Required        | False                          |


| Parameters      | Description                    |
|------------------|---------------------------------|
| Name            | xp                             |
| Type            | object                         |
| Description     | Container for extended (custom) properties of the catalog. |
| Required        | False                          |

## `DELETE` `v1/catalogs/{catalogID}`
Delete a catalog

| Parameters      | Description                    |
|------------------|---------------------------------|


| Parameters      | Description                    |
|------------------|---------------------------------|
| Name            | catalogID                      |
| Type            | string                         |
| Description     | ID of the catalog.             |
| Required        | True                           |

## Requestbody
**Responsestatus**: `204`

## Responsebody
## `PATCH` `v1/catalogs/{catalogID}`
Partially update a catalog

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
{'ID': '', 'Name': '', 'Description': '', 'Active': False, 'xp': {}}
```

```
[{'Name': 'ID', 'Type': 'string', 'Description': 'ID of the catalog. Can only contain characters Aa-Zz, 0-9, -, and _. Searchable: priority level 1. Sortable: priority level 2.', 'Required': False}, {'Name': 'Name', 'Type': 'string', 'Description': 'Name of the catalog. Required. Max length 100 characters. Searchable: priority level 2. Sortable: priority level 1.', 'Required': True}, {'Name': 'Description', 'Type': 'string', 'Description': 'Description of the catalog. Max length 2000 characters. Searchable: priority level 3.', 'Required': False}, {'Name': 'Active', 'Type': 'boolean', 'Description': 'Active of the catalog.', 'Required': False}, {'Name': 'xp', 'Type': 'object', 'Description': 'Container for extended (custom) properties of the catalog.', 'Required': False}]
```

**Responsestatus**: `200`

## Responsebody
```
{'ID': '', 'Name': '', 'Description': '', 'Active': False, 'CategoryCount': 0, 'xp': {}}
```


| Parameters      | Description                    |
|------------------|---------------------------------|
| Name            | ID                             |
| Type            | string                         |
| Description     | ID of the catalog.             |
| Required        | False                          |


| Parameters      | Description                    |
|------------------|---------------------------------|
| Name            | Name                           |
| Type            | string                         |
| Description     | Name of the catalog.           |
| Required        | True                           |


| Parameters      | Description                    |
|------------------|---------------------------------|
| Name            | Description                    |
| Type            | string                         |
| Description     | Description of the catalog.    |
| Required        | False                          |


| Parameters      | Description                    |
|------------------|---------------------------------|
| Name            | Active                         |
| Type            | boolean                        |
| Description     | Active of the catalog.         |
| Required        | False                          |


| Parameters      | Description                    |
|------------------|---------------------------------|
| Name            | CategoryCount                  |
| Type            | integer                        |
| Description     | Category count of the catalog. |
| Required        | False                          |


| Parameters      | Description                    |
|------------------|---------------------------------|
| Name            | xp                             |
| Type            | object                         |
| Description     | Container for extended (custom) properties of the catalog. |
| Required        | False                          |

## `GET` `v1/catalogs/assignments`
Get a list of catalog assignments

| Parameters      | Description                    |
|------------------|---------------------------------|


| Parameters      | Description                    |
|------------------|---------------------------------|
| Name            | catalogID                      |
| Type            | string                         |
| Description     | ID of the catalog.             |
| Required        | False                          |


| Parameters      | Description                    |
|------------------|---------------------------------|
| Name            | buyerID                        |
| Type            | string                         |
| Description     | ID of the buyer.               |
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
{'Meta': {'Page': 1, 'PageSize': 20, 'TotalCount': 25, 'TotalPages': 2, 'ItemRange': [1, 20]}, 'Items': [{'CatalogID': '', 'BuyerID': '', 'ViewAllCategories': False, 'ViewAllProducts': False}]}
```


| Parameters      | Description                    |
|------------------|---------------------------------|
| Name            | CatalogID                      |
| Type            | string                         |
| Description     | ID of the catalog.             |
| Required        | True                           |


| Parameters      | Description                    |
|------------------|---------------------------------|
| Name            | BuyerID                        |
| Type            | string                         |
| Description     | ID of the buyer.               |
| Required        | True                           |


| Parameters      | Description                    |
|------------------|---------------------------------|
| Name            | ViewAllCategories              |
| Type            | boolean                        |
| Description     | View all categories of the catalog assignment. |
| Required        | False                          |


| Parameters      | Description                    |
|------------------|---------------------------------|
| Name            | ViewAllProducts                |
| Type            | boolean                        |
| Description     | View all products of the catalog assignment. |
| Required        | False                          |

## `POST` `v1/catalogs/assignments`
Save a catalog assignment
## Requestbody
```
{'CatalogID': '', 'BuyerID': '', 'ViewAllCategories': False, 'ViewAllProducts': False}
```

```
[{'Name': 'CatalogID', 'Type': 'string', 'Description': 'ID of the catalog. Required. Sortable: priority level 1.', 'Required': True}, {'Name': 'BuyerID', 'Type': 'string', 'Description': 'ID of the buyer. Required.', 'Required': True}, {'Name': 'ViewAllCategories', 'Type': 'boolean', 'Description': 'View all categories of the catalog assignment.', 'Required': False}, {'Name': 'ViewAllProducts', 'Type': 'boolean', 'Description': 'View all products of the catalog assignment.', 'Required': False}]
```

**Responsestatus**: `204`

## Responsebody
## `DELETE` `v1/catalogs/{catalogID}/assignments`
Delete a catalog assignment

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
| Name            | buyerID                        |
| Type            | string                         |
| Description     | ID of the buyer.               |
| Required        | True                           |

## Requestbody
**Responsestatus**: `204`

## Responsebody
## `GET` `v1/catalogs/productassignments`
Get a list of catalog product assignments

| Parameters      | Description                    |
|------------------|---------------------------------|


| Parameters      | Description                    |
|------------------|---------------------------------|
| Name            | catalogID                      |
| Type            | string                         |
| Description     | ID of the catalog.             |
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
{'Meta': {'Page': 1, 'PageSize': 20, 'TotalCount': 25, 'TotalPages': 2, 'ItemRange': [1, 20]}, 'Items': [{'CatalogID': '', 'ProductID': ''}]}
```


| Parameters      | Description                    |
|------------------|---------------------------------|
| Name            | CatalogID                      |
| Type            | string                         |
| Description     | ID of the catalog.             |
| Required        | True                           |


| Parameters      | Description                    |
|------------------|---------------------------------|
| Name            | ProductID                      |
| Type            | string                         |
| Description     | ID of the product.             |
| Required        | True                           |

## `POST` `v1/catalogs/productassignments`
Save a catalog product assignment
## Requestbody
```
{'CatalogID': '', 'ProductID': ''}
```

```
[{'Name': 'CatalogID', 'Type': 'string', 'Description': 'ID of the catalog. Required.', 'Required': True}, {'Name': 'ProductID', 'Type': 'string', 'Description': 'ID of the product. Required.', 'Required': True}]
```

**Responsestatus**: `204`

## Responsebody
## `DELETE` `v1/catalogs/{catalogID}/productassignments/{productID}`
Delete a catalog product assignment

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
| Name            | productID                      |
| Type            | string                         |
| Description     | ID of the product.             |
| Required        | True                           |

## Requestbody
**Responsestatus**: `204`

## Responsebody