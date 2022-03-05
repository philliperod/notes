#### SQL Lesson 3: Queries with constraints (Part 2)

When writing `WHERE` clauses with columns containing text, SQL supports other useful operators like case-insensitive string comparison and wildcard pattern matching. Below is a list of text-data specific operators:

| Operator       | Condition                                                                                                 | Example                                                              |
| -------------- | --------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------- |
| `=`            | case sensitive exact string comparison (**notice the single equals**)                                     | `col_name = 'abc'`                                                   |
| `!= or <>`     | case senstive exact string inequality comparison                                                          | `col_name != 'abcd'`                                                 |
| `LIKE`         | case insensitive exact string comparison                                                                  | `col_name LIKE 'ABC'`                                                |
| `NOT LIKE`     | case insenstive exact string inequality comparison                                                        | `col_name NOT LIKE 'ABCD'`                                           |
| `%`            | used anywhere in a string to match a sequence of zero or more characters (only with `LIKE` or `NOT LIKE`) | `col_name LIKE '%AT%'` (matches 'AT', 'ATTIC', 'CAT' or even 'BATS') |
| `-`            | used anywhere ina string to match a single character (only with `LIKE` or `NOT LIKE`)                     | `col_name LIKE 'AN_'` (matches 'AND', but not 'AN')                  |
| `IN (...)`     | string exists in a list                                                                                   | `col_name IN ('A', 'B', 'C')`                                        |
| `NOT IN (...)` | string does not exist in a list                                                                           | `col_name NOT IN ('D', 'E', 'F')`                                    |

<br/>

> All strings must be quoted so that the query parser can distinguish words in the string from SQL keywords

While most database implementations are efficient when using these operators, full-text search is best left to libraries like **_Apache Lucene_** or **_Sphinx_**. They also support a variety of search features including internationalization and advanced queries.
