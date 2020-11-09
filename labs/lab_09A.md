# Lab 09A

*Lab 09A GitHub Classroom link:* https://classroom.github.com/a/vl1D1K1i

In this lab, we will learn how to use Python's built-in string manipulation methods, and how to read and write to the filesystem through Python.

1. Strings, revisited
2. Filesystem
3. Exercises

To begin this lab, clone your GitHub assignment repository to your virtual machine, enter the newly cloned directory, then open the `python` or `ipython` command line interface.

---

## Strings, revisited

We initially learned about Python string objects in the earlier Lecture & Lab 08A. Compared to most programming languages, Python strings are extremely easy to work with, in part because Python offers a rich platform of built-in string manipulation tools. We'll learn about some of those tools now.

Strings are a Python data type used for representing text. However, in many ways, they also have features that resemble containers of single-character strings. For example, substrings in a Python string may be accessed using the index operator (`x[0]`). Explore how to access single characters and substrings from string objects with the following index operations:

```python
>>> x = 'Cookie Monster'
>>> x[0]             # return first character
'C'
>>> x[0:6]           # return characters 0 to 6
'Cookie'
>>> x[:2]            # return up to character before index 6
'Cookie'
>>> x[7:]            # return character at index 7 through end
'Monster'
>>> x[0:2] + x[7:9]  # concatenate two substrings
'CoMo'
>>> x[ [0,1,2] ]     # cannot index string with an index list
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: string indices must be integers
```

Any string can make use of a suite of built-in string *methods*. To call a method for the string variable (say) `x`, we use the syntax `x.method_name(arg1, arg2)`, where `.method_name()` is replaced with the name of the actual method being used, and `arg1` and `arg2` represent any arguments you pass into the method. When called, object methods generally either modify the value of `x` itself, or return output that depends on the initial value of `x`.

The following examples demonstrate have various string methods behave. Each set methods uses 1-2 strings as examples. Try changing the value of the example string to explore how string method behavior depends on the string's value.

The string methods below modify whether alphabetical characters in a string are uppercase or lowercase.
```python
>>> x = 'hey, do penguins have DNA?'
>>> x.upper()       # all letters to uppercase
'HEY, DO PENGUINS HAVE DNA?'
>>> x.lower()       # all letters to lowercase
'hey, do penguins have dna?'
>>> x.title()       # 1st letter of each word to uppercase
'Hey, Do Penguins Have Dna?'
>>> x.capitalize()  # capitalize 1st letter, rest lowercase
'Hey, do penguins have dna?'
>>> x.swapcase()    # change upper to lowercase, and vice versa
'HEY, DO PENGUINS HAVE dna?'
```

These string methods either add or remove characters from the flanking regions of a string.
```python
>>> x = '  a long pause  '
>>> x
'  a long pause  '
>>> x.strip()          # remove all flanking whitespace
'a long pause'
>>> x.lstrip()         # remove all whitespace on left
'a long pause  '
>>> x.rstrip()         # remove all whitespace on right
'  a long pause'
>>> x.center(30,'.')   # create length-30 string, buffered with .
'.......  a long pause  .......'
>>> f = '7'
>>> f.zfill(3)         # create length-3 string, buffered on left with 0
'007'
```

This panel of string methods define boolean (`True` or `False`) that reflect the properties of the string's literal value.

```python
>>> x = 'Hello'               # create string
>>> x.isalpha()               # does x only contain alphabetical chars?
True
>>> 'Hello'.isalpha()         # call isalpha() method against string value
True
>>> 'hello'.islower()         # are all letters in string lowercase?
True
>>> 'HELLO'.isupper()         # are all letters in string uppercase?
True
>>> 'h3ll0'.isalnum()         # are all characters alphanumeric?
True
>>> '63110'.isdigit()         # are all characters numbers?
True
>>> ' \t\n'.isspace()         # are all characters whitespace?
True
>>> 'Hello'.startswith('He')  # does string start with supplied string?
True
>>> 'Hello'.endswith('lo')    # does string end with supplied string?
True
```

Python strings support various methods to count and find substrings within a given string.

```python
>>> x = 'Shelly sells seashells'
>>> x.count('ell')      # how many times does substring appear?
3
>>> x.find('ell')       # find index of first occurrence of substring
2
>>> x[2:]
'elly sells seashells'
>>> x.rfind('ell')      # find index of last occurrence of substring
18
>>> x[18:]
'ells'
>>> x.find('seashore')  # find returns -1 if substring not found
-1
```

These methods are useful for either splitting strings into substrings according to a delimiter, or joining multiple strings into a single character-delimited string

```python
>>> x = 'together forever'
>>> x.split(' ')          # tokenize string into list using delimter
['together', 'forever']
>>> x.replace('er','ah')  # replace all instances of substring
'togethah forevah'
>>> y = ['b','n','n','j','m']
>>> 'a'.join(y)           # use first string as "glue" to concatenate list
'bananajam'
>>> z = 'upstairs\ndownstairs'
>>> z.splitlines(keepends=True)  # split string using '\n' delimiter
['upstairs\n', 'downstairs']
```

Python also supports a wide range of string-formatting abilities, which make it easier to write complex and variable-dependent string values to stdout or to file. Here are several ways to seamlessly embed string values within another string.

```python
>>> mood = 'love'
>>> food = 'donuts'
>>> print('I ' + mood + ' to eat ' + food + '!')
I love to eat donuts!
>>> print(f'I {mood} to eat {food}')
I love to eat donuts!
>>> print('I {x} to eat {y}'.format(x='love', y='donuts')
I love to eat donuts!
```

Formatting numerical strings is especially tedious in many languages, but is relatively easy to do in Python
```python
>>> '{:.2f}'.format(3.141592653589793)
'3.14'
>>> '{:x<4d}'.format(5)
'5xxx'
>>> '{:.2%}'.format(0.25)
'25.00%'
>>> import datetime
>>> x = datetime.datetime(2020, 11, 7, 12, 39)
>>> '{:%Y-%m-%d %H:%M}'.format(x)
'2020-11-07 12:39'
```

---

## Filesystem

Python scripts may interact with the local filesystem in various ways, such as by listing files and directories, by reading files, and by writing files.

### Listing contents
 
Python functions that allow you to list filesystem objects (files and directories) generally belong external libraries that must be *imported* to the Python shell. Importing the relevant libraries is done with the `import` command, just as `import sys` was executed to gain access to the `sys.argv` argument vector.

Perhaps the most common approach to list all filesystem objects is with the function the `os.listdir()`. This function returns a list of strings that name the filesystem obejcts within the directory `path`.

```python
>>> import os
>>> path = '/home/data_analysis/netflix'
>>> os.listdir(path)
['file.txt', 'docs', 'data']
```

A similar function is `glob.glob()`, which returns a list of strings that describe all filesystem objects that match a filesystem search pattern; that pattern may include filesystem wildcard characters (e.g. `*`).

```python
>>> import glob
>>> glob.glob(path + "/*.txt")
['file.txt']
```

The third method is called `os.walk`, and it is the most powerful, but the most complex, of the three methods. As the name suggests, the function `os.walk()` will perforn a recursive "walk" through all of the directories and subdirectories located in the target directory. The walk returns a list of tuples, where each tuple contains three elements: the *root* in index 0, which gives the path to the current directory being listed in the walk; the list of all *directories* contained in the current root directory; and the list of all *files* in the current root directory. The root, directories, and files that are discovered during the walk can be assigned to separate iterators for each step in the for-loop.

```python
>>> import os
>>> path = '/home/data_analysis/netflix'
>>> for root, dirs, files in os.walk(path):
...	    for name in files:
...         print(os.path.join(root, name))
...     for name in dirs:
...         print(os.path.join(root, name))
```

We are now free to do as we please with the `root`, `dirs`, and `files` related to each iteration ("step") in the walk. The above example simply prints the content of those variables. (Note that `os.path.join` is here behaves similarly to `root + '/' + name`.)

### Reading

Reading files in Python will typically involve three steps. First the file must be opened for reading, using the `open()` function with the `'r'` "reading-mode" flag. Second, the content of the read-opened file must be read. Common practice is to use the idiom `for line in f:` to loop over all lines in an open and readable file `f`, processing each line as it is read. And, third, the file must (or should!) be closed once it is no longer in use, using the `f.close()` method.

To see how file reading works, first create a dummy file to read
```console
$ echo -e 'upstairs\ndownstairs' > test.txt
$ cat test.txt
upstairs
downstairs
```

then run the following Python code

```python
>>> dirname = '/home/mlandis/'
>>> filename = dirname + 'test.txt'
>>> s = ''
>>> # open the file for reading ('r')
>>> f = open(filename, 'r')
>>> for i,line in enumerate(f):
...     s += str(i) + ' : ' + line + '\n'
...
>>> f.close()
>>> print(s)
0 : upstairs
1 : downstairs
```

### Writing

Writing to file follows a procedure that's similar to how files are read. First, the file is opened using the `open()` function, but this time using the `'w'` "writing-mode" flag. Second, content is written to the write-enabled file using the method `f.write('example text')`. When all writing is complete, the file is closed with `f.close()`.

```python
>>> dirname = '/home/mlandis/'
>>> filename = dirname + 'test.txt'
>>> s = ''
>>> # open the file for writing ('w')
>>> f = open(filename, 'w')
>>> N = 3
>>> for i in range(N):
...     f.write(f'{i+1} of {N}\n')
...
>>> f.close()
>>> quit
```

then verify the script wrote to file
```console
$ cat /home/mlandis/test.txt
1 of 3
2 of 3
3 of 3
```

---
## Exercises

You will create a separate Python script for each of the following problems. Name the script after which problem it solves, e.g. `problem1.py`.

**Problem 1.** 
Write a Python script that accepts a list of words as arguments. The script then constructs a dictionary, that has each of the 26 letters of the alphabet as keys (`A`, `B`, ..., `Z`) and has the list of alphabetically sorted words that begin with each letter as values. For example, if the script was called as `./problem1.py avocado banana alligator` it would create a dictionary with the value

```python
{ 'A': ['alligator', 'avocado'], 'B': ['banana'], 'C': [], 'D': [], ..., 'Z': [] }
```

**Problem 2.**
Write a Python script that reads a csv file with numerical values, performs mathematical operations on each row, then writes the results to a new file. The script is called with `./problem2.py input_file.txt output_file.txt`. Once called, the script splits each line of `input_file.txt` into five separate fields, delimited by the `,` character. Then, those values are stored as floats into a temporary list named `x` and used to compute `y = x[0] + x[1] * x[2] + x[3] * x[4]^2`. Finally, the script writes the values of `y` and `x` for each row to the file `output_file.txt`.

**Problem 3.** 
Write a script that reorganizes the sequence data stored among fasta files within a directory. The script will process all files in a directory, then store their contents into a data array (list-of-lists). Each row in the array will correspond to one fasta sequence entry. The first column will give the species name, the second column will given the gene name, the third column will give the sequence length, and the fourth column will give the sequence identity itself. Assume that fasta headers for each sequence in each file follow the format `> species_name, gene_name`, for example `> Homo_sapiens, cytochrome B`, and that the lines immediately following the fasta header are valid sequences for that fasta entry.

For example, suppose the directory `data` contained two files, `data/rbcL.fasta`

```
> Viburnum_clemesiae, rbcL
ACGACT
> Viburnum_edule, rbcL
ACGCCT
```

and `data/matK.fasta`

```
> Viburnum_clemesiae, matK
CTTAGTA
> Viburnum_edule, matK
GTTAGTA
```

Running the script `./problem3.py data output.txt` should cause the script to internally create an array with the value
```
[ ['Viburnum_clemensiae', 'rbcL', 6, 'ACGACT'],
  ['Viburnum_dentatum', 'rbcL', 6, 'ACGACT'],
  ['Viburnum_clemensiae', 'rbcL', 7, 'CTTAGTA'],
  ['Viburnum_dentatum', 'rbcL', 7, 'GTTAGTA'] ]
```

that is then written in csv format to the file `output.txt`

```
$ cat output.txt
species_name,gene_name,gene_length,gene_content
Viburnum_clemensoae,rbcL,6,ACGACT
Viburnum_dentatum,rbcL,6,ACGACT
Viburnum_clemensoae,matK,7,CTTAGTA
Viburnum_dentatum,matK,7,GTTAGTA
```

To complete the lab, commit and push your three scripts to your GitHub repository.
