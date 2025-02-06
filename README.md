# EMA Co. Recruitment Test <!-- omit in toc -->

EMA Co. is seeking for backend developers expert in python-django stack. For this purpose, the following document has been provided demonstrating the recruitment test task definitions, prerequisites.

## Table of contents <!-- omit in toc -->

- [General Concepts](#general-concepts)
- [Task Definition](#task-definition)
  - [Part 1](#part-1)
  - [Part 2](#part-2)
  - [Part 3](#part-3)


## General Concepts

This task is part of an accounting project related to registering vouchers. Each voucher has tow or more items with some properties, the *master* and the *subsidiary* are the main ones. A user selects a master account from a list of previously masters. Then a list of subsidiaries related to the selected master account will be shown to the user. There are more fields for each voucher item which is not at the scope of this assignment, so are ignored.

## Task Definition

You need to design tow tables, *person*, *master* and *slave* each with the following fields:
- #### Person:
  | Field         | Desc                           |
  | ------------- | ------------------------------ |
  | First_Name    | -                              |
  | Last_Name     | -                              |
  | National_Code | -                              |
  | Phone_Number  | -                              |
  | Created_Date  | -                              |

- #### Master:
  | Field | Desc |
  | -------------| ------------------------------ |
  | Title        | -                              |
  | Code         | -                              |
  | Created_Date | -                              |
  | Creator      | A foreign key to Person table. |

- #### Subsidiary:
  | Field | Desc |
  | ------------- | ---------------------------------------------------------------------- |
  | Title         | -                                                                      |
  | Code          | -                                                                      |
  | Debit         | Has value only if this entity is last level.                           |
  | Credit        | Has value only if this entity is last level.                           |
  | Created_Date  | -                                                                      |
  | Creator       | A foreign key to Person table.                                         |
  | Master        | A foreign key to Master table.                                         |
  | Is_Last_Level | If true, no any other subsidiary references this entity as its parent. |
  | Parent        | A relation to another record in Subsidiary table.                      |

Please fork this repository and give the access when the task is done.

### Part 1

The CRUD operation on these tables should be implemented with the following conditions:
- The Read operation should be paginated.
- The Delete operation should be soft delete operation.
- The Read APIs should implement filtering on *Title* and *Code* fields on both *Master* and *Subsidiary* tables.
- Implement any validation you think there should be.

### Part 2

Create export-to-excel APIs for read operations.

### Part 3

Please fill the tables with acceptable large fake data, so we can measure the performance of your queries as well. You are suppose to provide us a hierarchical report for the amount of debit/credit each level has; which is the summation of debit/credit of all subsequences in each level.

E.g.:
Master <--- Sub1 <--- Sub2 <--- Sub3 (last level)  
- for Master, the given debit must be the summation of debit in all 3 Subs  
- for Sub1, the given debit must be the summation of debit in Sub2 and Sub3  
- for Sub12, the given debit must be the debit in Sub3

Happy Coding :smiley:
