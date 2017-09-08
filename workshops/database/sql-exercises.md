# SQL Exercises

## Basic SQL Syntax

1. Case does not matter
2. Each statement must be a SELECT, INSERT, UPDATE, DELETE statement. You can perform multiple statements at the same time.
3. Statements must end with `;` in order to be executed.
4. SQL has special characters that help to order, filter, etc.
  * The `*` (wildcard) character means ALL.
  * The `%` character helps with matching portions of strings.


## Selecting Records

The most basic SQL operation is the SELECT function. This retrieves records from a table. Here's a simple example:

    SELECT * FROM labusers;

This is called a query, and it selects ALL columns of all records from a specific table.

### Ordering a Query

We can then take this query and modify it slightly so that the results are put in a specific order.
In this case, let's order them by the `updated` date, in ascending order:

    SELECT * FROM labusers ORDER BY updated ASC;

### Selecting Specific Columns

We can modify our query so that we retrieve only specific columns of all those records:

    SELECT fname, flavor, updated FROM labusers;

The query pulls only the `fname`, `flavor`, and `updated` columns.

### Selecting Specific Rows

We can also modify the query so that we retrieve only specific rows of records, based on any
number of filters -- by date, by value of a specific column

    SELECT * FROM labusers WHERE fname = 'Neal';

## Describe a table

    DESCRIBE <table-name>;
