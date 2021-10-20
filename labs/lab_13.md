# Lab 13

*Lab 13 GitHub Classroom link: to be provided*

In this lab, we will learn how to create and manipulate Python containers, how to use for-loops with containers, and how to pass arguments to a Python script through Unix.

1. Containers
2. For-loops
3. Script arguments

To begin this lab, clone your GitHub assignment repository to your virtual machine, enter the newly cloned directory, then open the `ipython` command line interface.

---

## Containers

Containers are variables that *contain* multiple values, called *elements*. Just as there are different primitive datatypes (e.g. `int`, `float`, `str`, `bool`, etc.) there are different container datatypes. In this lab, we'll practice using the two most commonly used Python container types, lists and dictionaries. Lists and dictionaries are especially useful because they are (1) *indexed*, meaning that container elements may be retrieved by providing the "address" or index of an element using the index operator `[]`; and (2) they are *mutable*, meaning that the values of their elements, and even which elements each container contains, may changed after the container is first declared. (The tuple is an example of a list-like container that is *immutable*).

### Lists

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

### Dictionaries
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

## For-loops

For-loops are often used to apply a general code subroutine to all elements in a container. To accomplish this, for-loops can be designed to *iterate* over all elements in a container, using a temporary variable (called an *iterator*) to represent an element's value, then applying a *code block* for each iteration. For-loops in Python work very similarly to how they behave in Unix, but the syntax is different. Python for-loops may also be defined in various ways, depending on what container type you're working with and what code block you want to execute during iteration. We'll explore several for-loop architectures that are commonly used with lists and dictionaries.

For-loops in Python have the same general syntax, being
```python
[MAIN CODE]
for [ITERATOR(S)] in [ITERABLES]:
    [CODE BLOCK] using [ITERATOR(S)]
    ...
 
[MAIN CODE]
```
Note that the code block executed during each iteration (`[CODE BLOCK]`) is made distinct from the main code (`[MAIN CODE]`) through indented whitespace.

Perhaps the simplest for-loop involves directly iterating over the elements of a container
```python
In [1]: x = ['a', 'b', 'c']

In [2]: for i in x:
   ...:     print(i)
   ...:
a
b
c
```

An alternative is to use the `range(n)` function, which generates a list of integers, `[0, 1, ..., n-1]`. When iterating over `range(n)`, the iterator can then be used to index a list with `n` elements.

```python
In [1]: x = ['a', 'b', 'c']

In [2]: n = len(x)

In [3]: for i in range(n):
   ...:     print(i, x[i])
   ...:
0 a
1 b
2 c
```

When iterating over elements, sometimes it's useful to know how many times your loop has iterated. Using `enumerate(x)` on the container `x` will produce a list of paired values, where the first element is the iteration counter, and the second element is the iterator value

```python
In [1]: x = ['a', 'b', 'c']

In [2]: for i,v in enumerate(x):
   ...:     print(i,v)
   ...:
0 a
1 b
2 c

```

When iterating over elements in a dictionary, iterators will be equal to the value of the dictionary's keys. Those keys can then be used to index each value in the dictionary.

```python
In [1]: x = { 'a':10, 'b':20, 'c':30 }

In [2]: for k in x:
   ...:     print(k, x[k])
   ...:
a 10
b 20
c 30
```

We can also iterate over key-value *tuples* for a dictionary -- e.g. `(k,v)`. To do so, generate the container of key-value tuples with `x.items()`, then pass those iterables to the for-loop.

```python
In [1]: x = { 'a':10, 'b':20, 'c':30 }

In [2]: for k,v in x.items():
   ...:     print(k,v)
   ...:
a 10
b 20
c 30
```

As with lists, `enumerate` can be applied to dictionaries. In the below example, counter generated by `enumerate` becomes the first element in the tuple, and the key-value pair becomes the second tuple value (where the key-value pair is itself a tuple, nested within another tuple).

```python
In [1]: x = { 'a':10, 'b':20, 'c':30 }
In [2]: for i,(k,v) in enumerate(x.items()):
   ...:     print(i,k,v)
   ...:
0 a 10
1 b 20
2 c 30
```

Finally, for-loops can be nested with other control structures, including other for-loops and if-statements

```python
In [1]: x = [[1,2],[3,4]]
In [2]: for i in x:
   ...:   for j in i:
   ...:     if j % 2 == 0:
   ...:       print( str(j) + ' is even' )
   ...:     else:
   ...:       print( str(j) + ' is odd' )
   ...:
1 is odd
2 is even
3 is odd
4 is even
```

---

## Script arguments

In the previous lab, we hardcoded user input as variables within the Python script. This is less than ideal, because it would require potential users of the script to modify the Python code, which may be beyond a user's comfort level and/or compromise the integrity of the script itself. One way that Python scripts can accept user-defined input is through the *system argument vector* container, called `sys.argv`. The `sys.argv` variable is a list that captures the context of the operating system call in which the Python script was executed.

To understand how `sys.argv` works, create a Python script called `example.py` with the following content
```console
#!/usr/bin/python
import sys      # load a special library that defines sys.argv behavior
print('Contents of sys.argv, length = ' + len(sys.argv)) 
for i,x in enumerate(sys.argv):
    print( '  sys.argv['+str(i)+'] = ' + sys.argv[i])
```

then, return to the Unix shell, enable execute-permissions for the `example.py`, then execute the script while passing several arguments

```
$ chmod +x example.py
$ ./example.py hello world 3.14
Contents of sys.argv, length = 4
  sys.argv[0] = ./example.py
  sys.argv[1] = hello
  sys.argv[2] = world
  sys.argv[3] = 3.14
```

Study the content of `example.py` to understand how to access `sys.argv` elements by index.


---

## Exercises

You will create a separate Python script for each of the following problems. Name the script after which problem it solves, e.g. `problem1.py`.

**Problem 1.** Write a Python script that takes the following matrix, represented as a list (rows) of lists (columns). For the four nucleotides ('a', 'c', 'g', and 't'), each in turn, print out all row-column index pairs that correspond to a given nucleotide.

```
x = [ ['a', 'g', 'a', 't', 'c', 'g', 'a'],
      ['a', 'g', 'a', 'a', 'c', 'g', 'a'],
      ['c', 'a', 'a', 't', 'c', 'g', 'a'],
      ['a', 'g', 'a', 'a', 'c', 'g', 'a'],
      ['a', 't', 'g', 'c', 'c', 'g', 'a'],
      ['t', 'g', 'a', 'a', 'c', 'g', 'a'],
      ['c', 'c', 'a', 'c', 'c', 'g', 'a'] ]
```

For example, the output for nucleotide `t` would appear as
```
't' : (0,3), (2,3), (4,1), (5,0)
```
This problem can be solved in multiple ways. One way is to use three nested for-loops, with an if-statement in the innermost loop.

**Problem 2.** Write a Python script that prints all integers between the values of 1 and 100 that are evenly divisible by 2 but are *not* divisible by 3. The easiest way to solve this problem will use a for-loop, 1 or 2 if-statements, and the modulus (`%`) operator.

**Problem 3.** Write a Python script that converts a sequence of numbers into a sequence of alphabetical characters. The script expects any number of integers (valued 1 to 26) as an argument. Taking each number in the arguments, the script then converts that number into the letter in the corresponding position in the alphabet. For example, if the script was called as `./problem3.sh 3 1 20` would print `cat`, and `/problem3.sh 16 25 20 8 15 14` would print `python`.

To complete the lab, commit and push your three scripts and a log of your history to your GitHub repository.
