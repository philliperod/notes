## Section 3: Data Types & Variables

**Data types**: types of values <br>
**Variables**: names given to associate each value

***Additional Note***: <br> 
*You can use the console (python interpreter shell) for temporary testing as it won't save into the file. Not necessary to use `print()` to output the results.*

![](/Users/PhillipeRodriguez/Documents/Notes/python/megaCourse/megaNotes/img/sec3_1.png)
<br>

---

### Built-In Types

Most programming languages use **explicit declarations** to define the data type a variable is storing. A user must define the data type before the variable name - `let x`.

Python uses **implicit declarations** by using ***built-in types***. These data types are built into the interpreter and do not need to be declared before the variable name. The standard built-in types are:

- numeric: `int`, `complex`, `float`
- string: `str`
- sequence: `list`, `tuple`
- mapping: `dict`
- classes: `class`
- instances: `objects` in `class` statement
- exceptions: `SyntaxError`, `TypeError`, `ValueError`, `IndexError`, `KeyError` 

*Additional Note:* <br>
*You can use `type()` function to return the data type of the `object` or `argument`.*

![](/Users/PhillipeRodriguez/Documents/Notes/python/megaCourse/megaNotes/img/sec3_3.png)
<br>
<br>

---

**Numeric**: numbers created by numeric literals.

| Type            | Defined                                | Example      |
|-----------------|----------------------------------------|--------------|
| `int(x)`        | whole numbers                          | `x = 3`      |
| `float(x)`      | integer that contains a decimal number | `x = 4.3`    |
| `complex(re, im)` | contains a real and imaginary number   | `x = 2 + 6j` |

*Additional Note*: <br>
1. Integers in Python have **arbitrary precision** -- the amount of digits is limited only by the available memory of the host system. **Precision** is level of exactness, so `int` is less precise than a `float`.
2. **Underscores** can be used as commas for big numbers to improve readability - example: `3_500_00.00`

<br>

**String**: textual data created by string literals.

| Type      | Defined  | Example     |
|-----------|----------|-------------|
| `str(x)`  | string   | `x = 'hello'` |

<br>

**Sequence**: mutuable; used to store collections of data

| Type                       | Defined                                   | Example                      |
|----------------------------|-------------------------------------------|------------------------------|
| `list([iterable])`         | stores homogeneous data in a list `[]`    | `list('ab') = ['a','b']`     |
| `tuple([iterable])`        | stores heterogeneous data in a tuple `()` | `tuple('ab') = ('a', 'b')`   |
| `range(stop)`              | used for looping a specific # of times    | `range(5) = (0, 1, 2, 3, 4)` |
| `range(start,stop[,step])` | used for looping a specific # of times    | `range(0,15,5) = (0, 5, 10)` |

*Additional Note*: the comma is what makes a `tuple`, not the parenthesis

<br>

**Mapping**: maps hashable values to arbitary objects

| Type                | Defined                       | Example                                                                                                        |
|---------------------|-------------------------------|----------------------------------------------------------------------------------------------------------------|
| `dict({key:value})` | key:value pairs within braces | `dict(one=1,` <br> `{'two' : 2},` <br> `('three', 3)` <br> `= {'one' : 1,` <br> `'two' : 2,` <br> `'three': 3}` |

<br>

**Classes/Instances**: used to create objects; determines attributes and functionalities of an object

| Type                       | Defined                             | Example          |
|----------------------------|-------------------------------------|------------------|
| `class Class_Name(object)` | user-defined blueprint of an object | `class Person()` |

*Additional Note*: <br>
**Instances** are attributes - *defining an object* - or methods - *functions* - in a class. This is an **OOP concept**.

<br>

**Exceptions**: reports an error condition "just like" the situation in which the interpreter raises the same exception

<br>


