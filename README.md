# EMA Co. Recruitment Test <!-- omit in toc -->

EMA Co. is seeking for backend developers expert in python-django stack. For this purpose, the following document has been provided demonstrating the recruitment test task definitions, prerequisites.

## Table of contents <!-- omit in toc -->

- [General Concepts](#general-concepts)
- [Task Definition](#task-definition)
  - [Part 1](#part-1)
  - [Part 2](#part-2)


## General Concepts

This task is part of an accounting project related to registering vouchers. Each voucher has tow or more items with some properties, the *master* and the *subsidiary* are the main ones. A user selects a master account from a list of previously masters. Then a list of subsidiaries related to the selected master account will be shown to the user. There are more fields for each voucher item which is not at the scope of this assignment, so are ignored.

## Task Definition

You need to design tow tables, *master* and *slave* each with the following fields:
- #### Master:
  | Field | Desc |
  | -------- | ------- |
  | Title | - |
  | Code | - |
  | Created_Date | - |
  | Creator | A foreign key to Person table, simply put number in it. |

- #### Subsidiary:
  | Field | Desc |
  | -------- | ------- |
  | Title | - |
  | Code | - |
  | Created_Date | - |
  | Creator | - |
  | Master | A foreign key to Master table. |
  | Parent | A relation to another record in Subsidiary table. |

Please create a Github repository and give the access when the task is done.

### Part 1

The CRUD operation on these tables should be implemented with the following conditions:
- The Read operation should be paginated.
- The Delete operation should be soft delete operation.
- The Read APIs should implement filtering on *Title* and *Code* fields on both tables.
- Implement any validation you think there should be.

### Part 2

Create export-to-excel APIs for read operations.

Happy Coding :smiley:
