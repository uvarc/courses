# Introduction to Databases

## Requirements

## Content

## Concepts

Term | Definition
---- | ----------
Data schema | A pre-set definition for data to be stored in. This is made of fields and data types.
Data types | The specific kind of data being handled. This might be a date, a time, a number, a decimal, a string, a boolean value, etc.
Key | A unique, identifying value in a single database entry.
Relation | The way that two or more tables join in an RDBMS.
Table | A listing of specific sets of data in an RDBMS which, when joined with other tables, forms a larger data view.

## Relational Databases (RDBMS)

Many users have at least heard of relational databases like:

* MySQL / MariaDB
* PostgreSQL
* Microsoft SQL Server
* Oracle

Relational databases operate on the concepts of tables, relations, indexes, SQL, CRUD operations, and joins.

    C = Create   (Insert)
    R = Read     (Select)
    U = Update   (Update)
    D = Delete   (Delete)

Take the example of an online store, where data revolves around the ideas of items, orders and customers.
When a customer makes a purchase in our store, the data from the transaction is actually broken apart into
tables of related data. Here's one way of seeing that process:

![Relational DB Tables](https://s3.amazonaws.com/uvasom-resources/courses/aggregate-split.png)

But this "breaking apart" process is actually an intensive, time-consuming process. Data being sent off to
any particular table has to be validated by data type (strings, integers, dates, decimals, binary, etc.), length,
and NULL before it can be inserted into a particular data table. This is going on across multiple tables at
the same time, and ensures that the entire transaction completes successfully or is rolled back.

> **Impedance Mismatch** - a set of conceptual and technical difficulties that are often encountered when interacting with a relational database management system.



## NoSQL Databases



### Aggregate-Oriented

* Key-Value
* Document
* Column-Family

NoSQL databases share very few common characteristics. Perhaps the only one is that they are **schema-less**. Typical
aggregate-oriented NoSQL databases will store an aggregation in the form of strings or entire documents. That is usually in
plain text, often in a specific format or notation, such as JSON or XML.

Here are some sample entries from a simple Key-Value datastore:

    Key                       Value
    ----------------------------------------------------------
    access_key                ABCDEfghijklmnop123456789xyzabc
    secret_key                23481283852384128328a
    current_count             472
    jobs_remaining            13
    last-winner               Darla Johnson
    last-winner-date          08/17/2014 08:42:13.015 UTC
    ...                       ...

In the case of document NoSQL databases, the "value" portion of the entry can get much larger.
Here is an example of an entry in JSON. Note that the entire entry (or "document") breaks down into a
hierarchy of data: fields and their values, and dictionaries of multiple values, 

    {
        "success": {
            "total": 1
        },
        "contents": {
            "quotes": [
                {
                    "quote": "Remove the temptation to settle for anything short of what you deserve.",
                    "length": "71",
                    "author": "Lorii Myers",
                    "tags": [
                        "expectation",
                        "inspire",
                        "perfection"
                    ],
                    "category": "inspire",
                    "date": "2017-09-08",
                    "permalink": "https://theysaidso.com/quote/ZWrV624xU_q6_KYYlrQpYgeF/lorii-myers-remove-the-temptation-to-settle-for-anything-short-of-what-you-deser",
                    "title": "Inspiring Quote of the day",
                    "background": "https://theysaidso.com/img/bgs/man_on_the_mountain.jpg",
                    "id": "ZWrV624xU_q6_KYYlrQpYgeF"
                }
            ],
            "copyright": "2017-19 theysaidso.com"
        }
    }

### Node-Arc

* Graph

![Graph DB 2](https://s3.amazonaws.com/uvasom-resources/courses/graph-nodes.png)

![Graph DB 1](https://upload.wikimedia.org/wikipedia/commons/3/3a/GraphDatabase_PropertyGraph.png)

## Other Resources

[![Martin Fowler - NoSQL - YouTube](https://img.youtube.com/vi/qI_g07C_Q5I/0.jpg)](https://www.youtube.com/watch?v=qI_g07C_Q5I)
