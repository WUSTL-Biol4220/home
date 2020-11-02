# Lab 08A

*Lab 08A GitHub Classroom link:* https://classroom.github.com/a/FoMNwPZq

In this lab, we will begin to learn how to program using the Python programming language. [Python](https://www.python.org/) is a general-purpose, interpreted, high-level, and scriptable programming language. Language features include a rich package management system, object-oriented design, dynamic typing, and garbage collection. 

1. Python interpreter
2. Variables, operators, if-statements, and functions
3. Exercises

---

## Python interpreter

Python is an *interpreted* language, where interpreted languages use a program called the interpreter to translate human-readable code into computer-readable commands. There are a variety of useful tools that Python programmers use to run their code. Any computer that has Python installed will also  have the `python` program for interpreting code. The `ipython` program ([link](https://ipython.readthedocs.io/en/stable/)) is another Python shell and interpreter that introduces several user-friendly features, including syntax highlighting, debugger integration, and improved object introspection. We will primarily use `python` and `ipython` in this course. However, many Python programmers prefer to develop using `jupyter` ([link](https://jupyter.org/)), which offers an elegant online interface for managing Python notebooks. Alternatively, many Python developers might prefer to use `conda` ([link](https://docs.conda.io/en/latest/)), which offers a flexible framework for managing and rapidly deploying development environments.

To begin the lab, log in to your virtual machine, clone the repo for this GitHub assignment, then enter the new directory for this lab. Once inside, open the interactive Python shell

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

Now, let's create a Python script. First create a new file call `example.py` that contains the following text
```
#!/usr/bin/python
# construct a string
'Ahem, can you hear me?'
# print a string
print('Hello, world!')
```

The first line contains a hashbang (`#!`) address that points to a Python interpreter, `/bin/python`. Line three simply constructs a string, while line five prints a string.

To run the script, we will set the file permissions to enable execution, then run the script using the same `./scriptname` as we have used with Unix scripts

```console
$ chmod +x example.py
$ ./example.py
Hello, world!
```

When run in this way, notice that the script only printed `Hello, world!` to standard output in the Unix shell, but the unassigned string value (`'Ahem, can you hear me?'`) does not produce any output.

In this course, we will generally prefer to write our code in source files (`.py`) so that code can be reused and shared, but the command-line interface of `ipython` is often useful for code design, development, and debugging.

---

##  Variables, operators, if-statements, and functions

In this section, we will explore how to use Python variables, operators, if-statements, and functions in combination to produce complex outcomes. First, we'll review how these four programming concepts work, and what syntax they follow in Python, using the `ipython` console. Then, you will be asked to demonstrate your proficiency implementing these concepts, by writing a Python script that prints responses to a series of simple questions.

### Variables

A variable is a named location in computer memory that stores a value (or values). Variables in Python are most often created through the assignment operator (`=`), where the variable name is given on the lefthandside and the variable's value is given on the righthandside.

```python
x = 1   # create variable x, and assign value of 1
x
y = 2   # create variable y, and assign value of 2
y
x = y   # assign value of y to existing variable x
x
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

Boolean conditions evaluate an equality statement, then return the boolean value `True` if that statement is true, and `False` otherwise.

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

Boolean operators are useful for designing complex statements of boolean logic
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

### If-statements

Python if-statements have two major features: the condition statements and each condition's code block. Python will only execute the code block for the first condition that evaluates as `True` (bool) in a standard if-statement. All if-statements begin with an `if` condition, then are followed by zero or more else-if (`elif`) blocks, and are terminated with zero or one `else` blocks, where the else block is executed only if no other conditions evaluate as `True`.

```python
a = 3
b = 2
if a > b:
    print('a > b')
elif a >= b:
    print('a >= b') 
elif a == b:
    print('a == b')
else:
    print('a < b')
```
Notice that the first condition (`a > b`) would test for "greater than" before attempting the second condition (`a >= b`), therefore we don't expect the second block to run unless `a==b`. However, if that was `True`, the third condition (`a==b`) would not be run. The fourth condition (`a < b`) is run if the first three conditions evaluate as `False`.

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
def my_function(a, b, c=10):
    '''
    Description:
    This function returns a+c if a>b and returns b+c if a<=b.
    
    Parameters:
    a (int) : first compared value
    b (int) : second compared value
    c (int) : added to larger value when returned
    '''
    if a > b:
        return a + c
    else:
        return b + c
        
# call custom function
x = my_function( 1, 2, 13 )
```
--

## Exercises

Write Python code to perform each of the following tasks. Save your solutions for each task in a separate Python script, titled e.g. `problem1.py` for Problem 1, `problem2.py` for Problem 2, and so forth.

- **Problem 1.**  Create a variable `x` with the string value `11.05` and the variable `y` with the value `9.95`. Convert the values into floating point representation, then print their sum to standard output.

- **Problem 2.** Create three variables: `duck`, `chicken`, and `turkey`. Assign each variable an animal sound. Create a fourth variable called `turducken` that concatenates the values of the three variables together, in any order.

- **Problem 3.**  Define a function called `rate()` that accepts parameters for `distance` and `time`, then returns the ratio of distance over time. Call `rate()` three times using the values `distance=3.0` and `time=1.0`, `distance=4.0` and `time=1.2`, and `distance=5.0` and `time=1.5`. Use an if-statement to find the fastest rate, then print the corresponding `distance`, `time`, and `rate()` values.

- **Problem 4.** Write two functions, one called `power(x,z)` and another called `root(x,z)`. Both functions should attempt to cast the `x` and `z` arguments as type float. The function `power(x,z)` should return the value `x` to the `z` power, while `root(x,z)` should return the `z`-th root of its argument `x`. Write a test to valid that the value returned by `power( root(x, z), z)` minus `x` is approximately equal to zero (i.e. within narrow error tolerance of <1E-9).

To complete the assignment, commit and push all of your Python scripts to your GitHub repository.
