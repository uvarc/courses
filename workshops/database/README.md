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
    ...                       ...

Here is an example of a single entry written in JSON. Note that the entire entry (or "document") breaks down into a
hierarchy of data: variables and their values, dictionaries of multiple values, 

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

### Aggregate-Oriented

* Key-Value
* Document
* Column-Family

### Node-Arc

* Graph
