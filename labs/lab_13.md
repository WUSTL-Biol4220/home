# Lab 13

*Lab 13 GitHub Classroom link:* https://classroom.github.com/a/Oc0PeqPh

In this lab, we will begin to learn how to program using the Python programming language. [Python](https://www.python.org/) is a general-purpose, interpreted, high-level, and scriptable programming language. Language features include a rich package management system, object-oriented design, dynamic typing, and garbage collection. 

1. Python interpreter
2. Variables
3. Operators
4. Containers
5. Functions
6. Exercises

---

## Python interpreter

Python is an *interpreted* language, where interpreted languages use a program called the interpreter to translate human-readable code into computer-readable commands. There are a variety of useful tools that Python programmers use to run their code. Any computer that has Python installed will also  have the `python` program for interpreting code. The `ipython` program ([link](https://ipython.readthedocs.io/en/stable/)) is another Python shell and interpreter that introduces several user-friendly features, including syntax highlighting, debugger integration, and improved object introspection. We will primarily use `python` in this course. However, many Python programmers prefer to develop using `jupyter` ([link](https://jupyter.org/)), which offers an elegant online interface for managing Python notebooks. Alternatively, many Python developers might prefer to use `conda` ([link](https://docs.conda.io/en/latest/)), which offers a flexible framework for managing and rapidly deploying development environments.

On our virtual machines, the name of the Python executable is `python3`, not `python`:
```console
$ which python
# ... no output
$ which python3
/usr/bin/python3
```

Let's make a symbolic link for our user account so `python` acts as a shortcut to `/usr/bin/python3`:
```
$ cd ~/.local/bin
$ ln -s /usr/bin/python3 python
/usr/bin/python3
$ which python
```

To begin the lab, log into your virtual machine and open the `python` console:

```python
>>> 'Hello, world!'           # report value of string in console
'Hello, world!'
>>> print('Hello, world!')    # print string literal value to standard output
Hello, world!
```

To exit the Python console, type:
```python
>>> quit()
mlandis@ip-172-30-14-77:~$     # returns you to shell command line
```

<!--
To begin the lab, log in to your virtual machine. From your home directory, use the package installer for Python (`pip`) to install the interactive Python shell, `ipython`

```console
$ pip install ipython
Defaulting to user installation because normal site-packages is not writeable
Requirement already satisfied: ipython in /home/mlandis/.local/lib/python3.8/site-packages (7.17.0)
Requirement already satisfied: setuptools>=18.5 in /usr/lib/python3/dist-packages (from ipython) (45.2.0)
...
```

Once `pip` completes the installation of `ipython`, clone your GitHub assignment repository, enter the newly cloned directory, and open the `ipython` console

```console
$ ipython
Python 3.8.5 (default, Jul 28 2020, 12:59:40)
Type 'copyright', 'credits' or 'license' for more information
IPython 7.17.0 -- An enhanced Interactive Python. Type '?' for help.

In [1]:
```

Each line of code you enter into the `ipython` shell will then be executed by the interpreter. Let's begin with the `print()` function.

```
In [1]: 'Hello, world!'
Out[1]: 'Hello, world!'

In [2]: print('Hello, world!')
Hello, world!
```

The first command constructs a string with the literal value `Hello, world!`. When we hit enter, that value is declared, but left unassigned, hence it is received by the `Out` prompt. The second command instead calls `print('Hello, world!')`, where `print()` is the function name, and `Hello, world!` is the argument passed to the function (i.e. enclosed by `(...)`); in this second case, the value of `Hello, world!` is printed through standard output, rather than returned to the console.

We can learn more about a function using the `?` or `help()` command

```
In [3]: ?print
Docstring:
print(value, ..., sep=' ', end='\n', file=sys.stdout, flush=False)

Prints the values to a stream, or to sys.stdout by default.
Optional keyword arguments:
file:  a file-like object (stream); defaults to the current sys.stdout.
sep:   string inserted between values, default a space.
end:   string appended after the last value, default a newline.
flush: whether to forcibly flush the stream.
Type:      builtin_function_or_method
```

To exit `ipython` (or `python`), simply execute `quit()` and you will return to your Unix shell session

```
In [4]: quit()
$
```

-->

Now, let's create a Python script. First create a new file call `example.py` that contains the following text
```
#!/usr/bin/python3
# construct a string
'Ahem, can you hear me?'
# print a string
print('Hello, world!')
```

The first line contains a hashbang (`#!`) address that points to a Python interpreter, `/bin/python`. Line three simply constructs a string, while line five prints a string.

You can run the script either by calling `python` as a program and passing the script as an argument
```console
$ python example.py
Hello, world!
```

Alternatively, you can set set execution permissions for the script, then run the script using the same `./scriptname` as we have used with Unix scripts

```console
$ chmod +x example.py
$ ./example.py
Hello, world!
```

When run in this way, notice that the script only printed `Hello, world!` to standard output in the Unix shell, but the unassigned string value (`'Ahem, can you hear me?'`) does not produce any output.

```console
$ ./example.py | wc -2     # should expect that standard output contains two words!
2
```

In this course, we will generally prefer to write our code in source files (`.py`) so that code can be reused and shared, but the command-line interface of `python` is often useful for code design, development, and debugging.

---

##  Variables, operators, containers, and functions

In this section, we will explore how to use Python variables, operators, if-statements, and functions in combination to produce complex outcomes. First, we'll review how these four programming concepts work, and what syntax they follow in Python, using the `ipython` console. Then, you will be asked to demonstrate your proficiency implementing these concepts, by writing a Python script that prints responses to a series of simple questions.

### Variables

A variable is a named location in computer memory that stores a value (or values). Variables in Python are most often created through the assignment operator (`=`), where the variable name is given on the lefthandside and the variable's value is given on the righthandside.

```python
x = 1   # create variable x, and assign value of 1
print(x)
y = 2   # create variable y, and assign value of 2
print(y)
x = y   # assign value of y to existing variable x
print(x)
```

The type of any variable is determined by the type of the assigned value. How functions, operators, and other Python features interact with a variable often depends on the type of said variable.

The four types we will explore in this lab are integers (`int`), floating-point numbers (`float`), strings (`str`), and boolean values (`bool`); these are sometimes called primitive types. Call `type(x)` to learn the type of variable `x`.
```python
x = 10
type(x)        # int
f = 10.01
type(f)        # float
s = '10.01'
type(s)        # str
b = True
type(b)        # bool
```

Variables with simple types can be casted as a new type by passing the variable as an argument to a function named after the desired type (e.g. `int()` for integer, `str()` for string).
```python
x = 10        # int with value 10
f = float(x)  # float with value 10.0
s = str(x)    # str with value '10'
```

### Operators

In this section, we will explore the default operators that are commonly used in Python for simple variable types. An operator may be applied to one or more variables (called operands) to produce a new return value. That new value may be used in a variety of ways, such as being assigned to a variable, passed to a function as a parameter, or written to file. Operators are classified in several ways. One way operators are classified is by the number of operands: unary operators operate on only one operand, while binary operators require two operands as arguments. (Ternary operators in Python are essentially non-existent.) Operators also differ based on the type of their operands (`int` vs. `float` vs. `bool` vs. `str`).

Arithmetic operators accept `int` and `float` operands as input, and return values of the same type. If one `int` and one `float` are given as operands, the return value will generally be typed as a `float`. (Why would that be?)

```python
x = 5    # assignment
y = 2    # assignment
x + y    # addition
x - y    # subtraction
x * y    # multiplication
x / y    # division
x % y    # modulus
x ** y   # exponent
((x * y) - 2 * y)**2
```

Assignment operators prefixed with an arithmetic operator (e.g. `+=`, `*=`) will assign a new value to the variable on the lefthandside, assuming that the lefthand variable is the first operand, with the second operand appearing on the righthandside. For example

```python
x = 5    # assignment
x += 1   # equivalent to x = x + 1
x *= 2   # equivalent to x = x * 2
```

Boolean conditions evaluate an equality statement, then return the boolean value `True` if that statement is true, and `False` otherwise. In the future, we'll use these inequalities as conditions in if-statements.

```python
x = 5       # assignment
y = 2       # assignment
x == y      # is equal?
x != y      # is not equal?
x < y       # less than?
x > y       # greater than?
x <= (y+3)  # less than or equal to?
(x-3) >= y  # greater than or equal to?
```

Boolean operators are useful for designing complex statements of boolean logic. 
```python
True and True   # AND operator
True and False  # AND operator
True or False   # OR operator
False or False  # OR operator
not False       # NOT operator
not True        # NOT operator
(True or False) and not (True and False)
```

String operators allow for the concatenation and repetition of strings; more advanced forms of string manipulation will be covered in future labs.
```python
x = 'hello, '
y = 'world!'
x + y           # concatenates 'hello, world!'
z = x * 3       # repeats 'hello, hello, hello, '
```

---

### Containers

Containers are variables that *contain* multiple values, called *elements*. Just as there are different primitive datatypes (e.g. `int`, `float`, `str`, `bool`, etc.) there are different container datatypes. In this lab, we'll practice using the two most commonly used Python container types, lists and dictionaries. Lists and dictionaries are especially useful because they are (1) *indexed*, meaning that container elements may be retrieved by providing the "address" or index of an element using the index operator `[]`; and (2) they are *mutable*, meaning that the values of their elements, and even which elements each container contains, may changed after the container is first declared. (The tuple is an example of a list-like container that is *immutable*).

#### Lists

Let's begin by exploring the properties of list variables. A list is a container whose elements are indexed by consecutive integers. From the `ipython` shell, create a new list, then access and modify its contents.
```python
In [1]: x = [ 0, 1, 2 ]      # creates new list

In [2]: x[0]                 # returns value of (first) element at index 0
Out[2]: 0

In [3]: print(x[0])          # prints element to stdout
0

In [4]: x[0:2]               # returns values for indices 0 and 1 (not 2)
Out[4]: [0, 1]

In [5]: x[0] = 10            # assign new value to index-0 element

In [6]: x[1:3] = [ 20, 30 ]  # assign new values to indices 1 and 2 (not 3)

In [7]: x                    # return new values for list
Out[7]: [10, 20, 30]

In [8]: x[-1]                # return the last value in the list
Out[8]: 30
```

One thing to note is that Python indexes elements in a list starting with the number zero (`0`). This is called *base-0* indexing, and is used in languages including C, C++, and Java.

You will also have noticed that we can access a *range* of list elements using the index-slicing notation, `x[n:m]`. In this case, `n` indexes the first element in the returned range, and `m-1` indexes the final element in the returned range -- i.e. *not* the element at index `m`.

The number of list elements may also be modified with the following commands
```python
In [1]: x = ['a', 'b', 'c']

In [2]: x.append('d')     # appends value onto end of list

In [3]: x
Out[3]: ['a', 'b', 'c', 'd']

In [4]: x.insert(2, 'e')  # inserts value ('e') into index (2)

In [5]: x
Out[5]: ['a', 'b', 'e', 'c', 'd']

In [6]: x.remove('b')     # removes first variable with value

In [7]: x
Out[7]: ['a', 'e', 'c', 'd']

In [8]: x.pop(3)          # returns value AND modifies container
Out[8]: 'd'

In [9]: x
Out[9]: ['a', 'e', 'c']
```

Finally, list elements may be rearranged
```python
In [1]: x = [ 3, 6, 5, 1, 2 ]

In [2]: x.reverse()       # reverses order of list elements by index

In [3]: x
Out[3]: [2, 1, 5, 6, 3]

In [4]: x.sort()          # sorts order of list elements by value

In [5]: x
Out[5]: [1, 2, 3, 5, 6]

In [6]: x.index(5)        # returns index of first element with target value
Out[6]: 3

In [7]: x.clear()         # erase all elements from container

In [8]: x
Out[8]: []

```

#### Dictionaries
Dictionaries (or *dicts*) are containers whose elements are accessed through *key-value* pairs. Dictionaries differ from lists in two important ways: (1) the keys provided to index elements do not need to be integers (`int`); and (2) new dictionary elements are added as-needed during assignment (i.e. no insert or append necessary). 

```python
In [1]: x = {'a':1, 'b':2, 'c':3}   # create a new dictionary

In [2]: x
Out[2]: {'a': 1, 'b': 2, 'c': 3}

In [3]: x['a']                      # access the value with key 'a'
Out[3]: 1

In [4]: x['d'] = 4                  # create a new value 4 with key 'd'

In [5]: x
Out[5]: {'a': 1, 'b': 2, 'c': 3, 'd': 4}

In [6]: x['a'] = 0                  # assign 0 to the value with key 'a'

In [7]: x
Out[7]: {'a': 0, 'b': 2, 'c': 3, 'd': 4}

In [8]: del x['b']                  # delete the first element with key 'b'

In [9]: x
Out[9]: {'a': 0, 'c': 3, 'd': 4}
```

To view ordered lists of a dictionary's keys and values
```python
In [1]: x = { 'a':1, 'b':2, 'c':3 }

In [2]: x.keys()                     # return ordered dictionary keys
Out[2]: dict_keys(['a', 'b', 'c'])

In [3]: x.values()                   # return ordered dictionary values
Out[3]: dict_values([1, 2, 3])

In [4]: type(x.values())
Out[4]: dict_values

In [5]: list(x.values())             # convert `dict_values` into type `list`
Out[5]: [1, 2, 3]

In [6]: type(list(x.values()))
Out[6]: list
```

Dictionaries are extremely flexible, but it comes at some cost. Compared with lists, dictionaries may require greater memory usage and induce slower processing times, depending on the task. Code to manipulate and access dictionaries can also be more cumbersome than similar code for lists, because dictionaries impose less internal structure on variables. For example, the dictionaries do not have a compact notation for slicing subsets of elements from the container; for lists, it's quite elegant (e.g. `x[3:6]`).

Finally, containers may treat other containers as elements, making it easy to construct high-dimensional data structures
```python
In [1]: x = [[1,2], [3,4]]

In [2]: x[0][1]
2

In [3]: y = {'a':[1,2], 'b':[3,4]}

In [4]: y['a'][1]
Out[4]: 2
```

---

### Functions

Functions are named computational recipes that accept parameters as inputs, undertakes some computational procedure based on the values of those parameters, then returns a value for further use once the function has completed its computation. When calling a function, the function name is listed first, with function parameters passed as a comma-separated list inside of a pair of parentheses -- e.g. `print('Hello,', 'world!')`.

Python provides a large number of built-in functions, that are natively available across Python installations. The complete of Python v3's built-in functions may be found [here](https://docs.python.org/3/library/functions.html). We'll only use a subset of the built-in functions for this lab:

```python
abs(-1)                 # absolute value of number
bool(0)                 # converts type to boolean
float(1)                # converts type to float
int(20.2)               # converts type to integer
print('hi')             # prints value to standard output
round(0.12, ndigits=1)  # rounds number to `ndigits` places
str(10)                 # converts type to string
type(x)                 # reports type of variable
```

As we'll learn in future labs, programmers may also import functions from packages and libraries. Finally, programmers may define custom functions in their programs.

Programmers may define their own custom functions, as follows

```python
# define custom function
def my_function(a, b):
    '''
    Description:
    This function returns a + b^2
    
    Parameters:
    a (float) : first compared value
    b (float) : second compared value
    '''
    return a + b**2 
        
# call custom function
x = my_function( 1.3, 2.2 )
```
---

## Exercises

Write Python code to perform each of the following tasks. Save your solutions for each task in a separate Python script, titled e.g. `problem1.py` for Problem 1, `problem2.py` for Problem 2, and so forth.

- **Problem 1.**  Create a variable `x` with the string value `'11.05'` and the numerical variable `y` with the value `9.95`. Convert the values into floating point representation, then print their sum to standard output.

- **Problem 2.** Create three variables: `duck`, `chicken`, and `turkey`. Assign each variable an animal sound. Create a fourth variable called `turducken` that concatenates the values of the three variables together, in any order.

-  **Problem 3.** Using a single command, create a dictionary that contains the following information:
   ```console
   human  GATTACA
   mouse  GCCTATC
   fly    CAGTTAT
   worm   CGTATCA
   ```
   where the keys are species names and values are sequence data, and sequence data are stored as lists of length-1 strings. Once you have created the dictionary, make two modifications. Add a new entry for `chimp` with the value `AATGCTA`. Change the middle character for fly and worm to a gap, `-`. Print the list of keys to standard output, then print the list of values to standard output.

- **Problem 4.** Create a list with the lengths of five genes (in base pairs). Use the values 391, 852, 172, 1414, and 742. Write code to calculate and print the total length of all the genes combined, the average gene length, and the difference between the longest and shortest genes.
Hint: Use the `sum`, `max`, and `min` functions. Use the `help` function to learn how other functions work, e.g. `help(sum)`.

---

To complete the assignment, commit and push all of your Python scripts to your GitHub repository.
