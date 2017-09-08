# Introduction to Databases

## Requirements

## Content

## Relational Databases

Relational databases operate on the concept of tables, relations, indexes, SQL, and joins.

Take the example of an online store, where data revolves around the ideas of items, orders and customers.
When a customer makes a purchase in our store, the data from the transaction is actually broken apart into
tables of related data. Here's one way of seeing that process:

![Relational DB Tables](https://s3.amazonaws.com/uvasom-resources/courses/aggregate-split.png)

But this "breaking apart" process is actually an intensive, time-consuming process. Data being sent off to
any particular table has to be validated by data type (strings, integers, dates, decimals, binary, etc.), length,
and NULL before it can be inserted into a particular data table. This is going on across multiple tables at
the same time, and ensures that the entire transaction completes successfully or is rolled back.

> **Impedance Mismatch** - a set of conceptual and technical difficulties that are often encountered when a relational database management system.



## NoSQL Databases

NoSQL databases share very few common characteristics. Perhaps the only one is that they are **schema-less**.

https://gist.github.com/nmagee/1bece00a989f95411af423c940cac883

### Aggregate-Oriented
* Key-Value
* Document
* Column-Family


* Graph
