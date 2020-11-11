# Lab 09B

*Lab 09B GitHub Classroom link:* https://classroom.github.com/a/crLHFc1i

In this lab, we will learn how to use Python modules, how to execute system commands from within the Python shell, and new ways to interact with containers.

1. Modules
2. System calls
3. Containers, revisited
4. Exercises

To begin this lab, clone your GitHub assignment repository to your virtual machine, enter the newly cloned directory, then open the `python` or `ipython` command line interface.

---

## Modules

A module is an importable object that defines any number of functions in your current Python environment. Module files may be installed with Python package managers, like `pip` or `easy_install`, or the module files may simply be `.py` files in your filesystem.

Importing and using module functions in Python is very easy. A simple example
```python
>>> import math
>>> math.pi                # pi, the mathematical constant
3.141592653589793
>>> math.floor( math.pi )  # round pi down to next integer
3
```

Write a Python script called `talk.py` that defines the following function
```python
def yell(x,n):
    return( str(x).upper() + '!'*n )
    
def ask(x,n):
    return( str(x).capitalize() + '?'*n )
```

Then use that function as a module with the following code
```python
>>> import talk
>>> talk.yell('what', 2)
'WHAT!!'
>>> talk.ask('what', 2)
'What??'
```

Future labs will explore new modules that specialize in defining data structures, statistical analyses, visualization, and working with molecular datasets.


---

## System calls

Python provides several libraries with methods for dispatching commands to the operating system for execution. The two approaches we will consider are `os.popen` and `subprocess.Popen`. In both cases "popen" refers to opening a pipe to or from a command. In this sense, *popen* commands behave in a similar manner as piped Unix commands, in that they accept text as input, and return text as output. Any command passed to `os.popen` or `subprocess.Popen` would be executed, just as a command would be executed from your used account thorugh the operating system shell.

For most purposes, `os.popen` and `subprocess.Popen` behave in an equivalent manner. In terms of usability, a major difference is that `os.popen` has less features, and therefore a simpler interface, while `subprocess.Popen` has more features, and therefore more complex behavior. Although `subprocess.Popen` is often considered the superior tool, either method is adequate for most simple tasks.

To run a command using `os.open`, we will need to import the `os` module

```python
>>> import os
>>> cmd = 'ls -lart'
>>> out = os.popen(cmd).readlines()
>>> print(''.join(out))
total 12
drwxrwxr-x 10 mlandis mlandis 4096 Nov 10 10:17 ..
-rwxrwxr-x  1 mlandis mlandis  305 Nov 10 12:54 babymath.py
drwxrwxr-x  2 mlandis mlandis 4096 Nov 10 13:38 .
```

To run the same command using `subprocess.Popen`, we'll import the `subprocess` module
```python
>>> import subprocess
>>> cmd = 'ls -lart'
>>> p = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE)
>>> out = p.stdout.readlines()
>>> for i,o in out:
...     out[i] = o.decode('UTF-8')  # subprocess.Popen stdout needs to be converted from bytes to text
...
>>> print( ''.join(out) )
total 12
drwxrwxr-x 10 mlandis mlandis 4096 Nov 10 10:17 ..
-rwxrwxr-x  1 mlandis mlandis  305 Nov 10 12:54 babymath.py
drwxrwxr-x  2 mlandis mlandis 4096 Nov 10 13:38 .
```

---

## Containers, revisited

Python containers have many features. Here, we'll explore more-advanced features that weren't introduced when we first learned about containers.


The `in` keyword tests to see whether a specific value is equal to the value of any element in a container. This works for lists

```python
>>> x = [ 1, 2, 3 ]
>>> y = 1
>>> if y in x:
...     print(f'{y} is in {x}')
...
1 is in [1, 2, 3]
```

and for strings

```python
>>> x = 'turducken'
>>> y = 'duck'
>>> if y in x:
...     print(f'{y} is in {x}')
...
duck in turducken
```

We learned in a previous class that strings may be concatenated using the `+` operator. Lists may also be concatenated using the `+` operator, like so

```python
>>> turkey = 'gobble'
>>> duck = 'quack'
>>> turkey + duck + 'bock'
'gobblequackbock'
>>> x = [ 1, 2 ]
>>> y = [ 3, 4 ]
>>> x + y + [ 5, 6 ]
[1, 2, 3, 4, 5, 6]
```

Dictionaries, however, cannot be concatenated with `+`. Instead, the keys and values of one dictionary may be merged into another dictionary, using the syntax `x.update(y)`. If both dictionaries have an item for the same key, that value in the receiving dictionary will be overwritten with the new dictionary's value.

```python
>>> x = { 'cat':'meow', 'dog':'woof' }
>>> y = { 'cow':'moo', 'horse':'neigh' }
>>> x + y
>>> x + y
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: unsupported operand type(s) for +: 'dict' and 'dict'
>>> x.update(y)
>>> x
{'cat': 'meow', 'dog': 'woof', 'cow': 'moo', 'horse': 'neigh'}
```

List comprehensions allow you to compactly iterate over a container, as you would with a for-loop, while returning a list as a result. List comprehensions are largely useful for making code appear more clean and readable.

```python
>>> # example with list
>>> x = [ 1, 2, 3, 4, 5 ]
>>> # simple list comprehension
>>> y = [ (i**2) for i in x ]
[1, 4, 9, 16, 25]
>>> # list comprehension with if-statement
>>> z = [ (i**2) for i in x if i > 3 ]
[16, 25]
>>> # list comprehension for dictionary
>>> d = {'a':1, 'b':2, 'c':3}
>>> [ f'key={k},val={v}' for k,v in d.items() ]
['key=a,val=1', 'key=b,val=2', 'key=c,val=3']
```

Often times, we want to use a function that accepts multiple arguments as input, but our desired input is stored in a list. A list can be "unpacked" when passed as an argument to a function by preceding the list's name with an asterisk (`*`). This causes each element in the list to be passed as a separate argument, in order, rather than the entire list being passed as a single argument.

```python
>>> def add(a,b):
...     return a + b
...
>>> x = [ 1, 2 ]
>>> # do not unpack `x`
>>> add(x)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: add() missing 1 required positional argument: 'b'
>>> # unpack `x` with `*x`
>>> add(*x)
3
```

Multiple lists can be combined into a single list of tuples using the `zip()` function. Then, retrieving element `i` of the zipped container will produce a tuple of element `i` for each of the lists that were zipped together.

```python
>>> x = [ 'a', 'b', 'c' ]
>>> y = [ 1, 2, 3 ]
>>> zip(x,y)
<zip object at 0x7f3da6b93880>
>>> list(zip(x,y))
[('a', 1), ('b', 2), ('c', 3)]
>>> for i,j in zip(x,y):
...     print(f'zipped pair {i} and {j}')
zipped pair a and 1
zipped pair b and 2
zipped pair c and 3
```

Finally, we learned about the basic use of the index-slice operator in a previous class. For example calling `x[i:j]` will retrieve elements `i` through `j-1` from the list `x`. The index-slice operator allows for a third number, which indicates how many elements to skip when indexing. By default, third number has the value of 1. However, replacing that number with something greater than 1 will let the slice skip intermediate elements. Using a negative value will essentially reverse the list.

```python
>>> x = list(range(10))
>>> x
[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
>>> x[::-1]
[9, 8, 7, 6, 5, 4, 3, 2, 1, 0]
>>> x[3:8:2]
[3, 5, 7]
>>> x[8:3:-2]
[8, 6, 4]
```

These slide-index operators can also be used to reverse strings and extract substrings from strings.
```python
>>> y = 'syzygy'
>>> y[1:3]
'yz'
>>> y[::2]
'szg'
>>> y[::-2]
'yyy'
```

---

## Exercises

You will create a separate Python script for each of the following problems.

**Problem 1.** 
Write a module file called `word.py`. This code will define a function called `mutate(s)` which accepts the string `s` as input and returns a string as output. The `mutate()` function will take the input string, convert it to a list of single-character strings, randomize the order of elements in the character-list using `random.shuffle()`, convert the now-shuffled character-list back into a string, then return that string. The script will also define a `__main__()` function that accepts a string as an argument, calls `mutate()` for that string, then prints the shuffled string to standard output.

You will need to import `random` to use `random.shuffle()` and `sys` to support the argument vector, `sys.argv`.

If done correctly, you should be able to `import word` and call `word.mutate('elephant')` within a Python shell, which might return `'phleetna'` as a randomly shuffled string. Or the module could be called as a Unix script from the command line with `$ ./word.py elephant`, which might return `'taelephn'` as another randomly shuffled string. 

**Problem 2.**
Write a module file called `seq.py`. The code will be able to launch alignment software using `os.popen` and extract some basic information from the resultant alignment. This code will define two functions. The first function will be called `align(filename)`, which will issue a system call to align the fasta file (`filename`) using an alignment program of your choice (e.g. Muscle). The second function will be called `site(i)` which returns a dictionary for the characters found at site-index `i` in the alignment.

For example, if the fasta file `test.fasta` contained
```
> Species_A
ACGTT
> Species_B
ACTTC
```
and if `seq.align(test.fasta)` produced the alignment file `test.align.fasta`

```
> Species_A
ACGTT-
> Species_B
AC-TTC
```
then `seq.site(0)` would return `{'Species_A':'A', 'Species_B':'A'}` and `seq.site(2)` would return `{'Species_A':'G', 'Species_B':'-'}`.

To complete the lab, commit and push your two scripts to your GitHub repository.
