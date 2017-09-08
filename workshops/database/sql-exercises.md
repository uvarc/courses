# SQL Exercises

## Basic SQL Syntax

1. Case does not matter
2. Each statement must be a SELECT, INSERT, UPDATE, DELETE statement. You can perform multiple statements at the same time.
3. Statements must end with `;` in order to be executed.
4. SQL has special characters that help to order, filter, etc.
    * The `*` (wildcard) character means ALL.
    * The `%` character helps with matching portions of strings.
5. Something else.

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

Or we could find all rows where `flavor` contains the letter `C`:

    SELECT * FROM labusers WHERE flavor LIKE '%c%';

## Describe a table

    DESCRIBE labusers;

Gives us output something like this:

    +---------+--------------+------+-----+-------------------+----------------+
    | Field   | Type         | Null | Key | Default           | Extra          |
    +---------+--------------+------+-----+-------------------+----------------+
    | id      | int(11)      | NO   | PRI | NULL              | auto_increment |
    | fname   | varchar(50)  | YES  |     | NULL              |                |
    | flavor  | varchar(20)  | YES  |     | NULL              |                |
    | host    | varchar(100) | YES  |     | NULL              |                |
    | updated | datetime     | NO   |     | CURRENT_TIMESTAMP |                |
    +---------+--------------+------+-----+-------------------+----------------+
