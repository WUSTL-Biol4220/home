# Lab 20

*Lab 20 GitHub Classroom link:* https://classroom.github.com/a/tCW3glX5

This lab will introduce to the numerical analysis library, NumPy, with an emphasis on how to create, access, manipulate, and compute with `numpy.array` data structures. To complete this assignment, finish the exercises in a Jupyter notebook (`lab-20.ipynb`), then submit the notebook through GitHub Classroom. See [Lab 19](https://github.com/WUSTL-Biol4220/home/blob/master/labs/lab_19.md) for instructions to connect to a Jupyter Notebook server hosted through your virtual machine.

---

## NumPy

[NumPy]() is a Python library that specializes in providing data types and functions that enable rapid processing of numerical data. The NumPy library is at the center of scientific computing ecosystem in Python, and as such, many other scientific libraries depend on NumPy data structures and/or functions. (We saw that the Matplotlib gallery examples from Lab 12A used NumPy random number generators to produce "toy" datasets.)

Place each of the following code-blocks into its own Jupyter cell.

The convention is to import the Numpy library, `numpy`, under the alias `np`.
```python
>>> # import NumPy library
>>> import numpy as np
```

The crown jewel of NumPy features is the NumPy `ndarray` type: a matrix-like container that allows for arbitrary numbers of dimensions. From the Python programmer's perspective, they behave much like a list-of-lists(-of-lists-of-lists...) where all elements share a common type, and all lists of a given dimension are equal in length. Although this may seem restrictive at first, it comes with benefits. NumPy `ndarray` objects are implemented in C using Python's C interface, making then highly efficient in terms of speed and space. By enforcing constraints on types and on dimension-sizes, `ndarray` elements can be accessed rapidly using pointer arithmetic.

Much of this technical background is useful to know, on some level, but for now let's practice using `ndarray` variables. First, create a simple 2x3 `ndarray` in a new Jupyter cell.

```python
>>> # create simple 2D array
>>> x = np.array( [[1,2,3], [4,5,6]] )
>>> # list-of-lists converted to array
>>> x
array([[1, 2, 3],
       [4, 5, 6]])
```       

Before we explore features of NumPy and its `ndarray` class, let us first observe the type of `x` and its elements. Most importantly, notice that `x.dtype` gives the datatype of its elements, while `type(x)` simply reports that the object is a `numpy.ndarray`.
    
```python
>>> type(x)                 # container type is numpy.ndarray
<class 'numpy.ndarray'>
>>> x.dtype                 # container dtype is 64-bit integer
dtype('int64')
>>> type(x[0])              # element type is 64-bit integer
<class 'numpy.int64'>
>>> x.tolist()              # convert to standard list-of-lists
[[1, 2, 3], [4, 5, 6]]
>>> type(x.tolist())        # container type of list(-of-lists)
<class 'list'>
```

We previously created the `ndarray` object, `x`, initialized to the value defined by a standard list-of-lists. There are many ways to create `ndarray` objects, depending on how you intend to use them, including initialized with all-zeroes, all-ones, cell-wise values, a structured pattern of values, or left uninitialized.

```python
>>> np.array( [[1,2],[3,4]] )  # from list-of-lists, 2D
array([[1, 2],
       [3, 4]])
>>> np.zeros([4])              # all zeroes, 1D
array([0., 0., 0., 0.])
>>> np.ones( [2,2,2] )         # all ones, 3D
array([[[1., 1.],
        [1., 1.]],
       [[1., 1.],
        [1., 1.]]])
>>> np.eye(2)                  # identity matrix, 2D
array([[1., 0.],
       [0., 1.]])
>>> np.empty( [2,3] )          # uninitialized values, 2D
array([[4.9e-324, 9.9e-324, 1.5e-323],
       [2.0e-323, 2.5e-323, 3.0e-323]])
>>> np.random.rand(2,3)        # random numbers, 0 to 1, 2D
array([[0.03675717, 0.28691042, 0.34546637],
       [0.95096269, 0.78970958, 0.00432774]])
>>> np.arange(0,6,2)           # from 0 to 6, every 2nd value, 1D
array([0, 2, 4])
>>> np.linspace(0,10,5)        # 5 spaced values, from 0 to 10, 1D
array([ 0. ,  2.5,  5. ,  7.5, 10. ])
```

Once created, `ndarray` objects may be manipulated in a variety of ways. Below, we'll explore ways to transform the dimensionality of the `ndarray` object.

```python
>>> x = np.array( [[1,2,3,4],[5,6,7,8]] )
>>> x                    # array
array([[1, 2, 3, 4],
       [5, 6, 7, 8]])
>>> x.T                  # array-transpose
array([[1, 5],
       [2, 6],
       [3, 7],
       [4, 8]])
>>> x.ndim               # two dimensions
2
>>> x.shape              # shape is 2x4 elements
(2, 4)
>>> x.shape = (2,2,2)    # change shape to 2x2x2
>>> x
array([[[1, 2],
        [3, 4]],
       [[5, 6],
        [7, 8]]])
>>> x.flatten()          # return 1D array
array([1, 2, 3, 4, 5, 6, 7, 8])
```

Python lists provide methods to access ranges of container elements using index-slicing. NumPy `ndarray` objects support slice-indexing, along with methods to select container elements that do *not* have adjacent indices.

```python
>>> x = np.array([[1,2,3],[4,5,6],[7,8,9]])
>>> x
array([[1, 2, 3],
       [4, 5, 6],
       [7, 8, 9]])
>>> x[ 0:2, 1:3 ]         # values by array slicing
array([[2, 3],
       [5, 6]])
>>> x[ [1,2], [0,2] ]     # values by index lists
array([4, 9])
>>> x > 2                 # does element pass test?
array([[False, False,  True],
       [ True,  True,  True],
       [ True,  True,  True]])
>>> np.where(x > 2)       # elem. indices that pass test
(array([0, 1, 1, 1, 2, 2, 2]), array([2, 0, 1, 2, 0, 1, 2]))
>>> x[x>2]                # boolean values to index
array([3, 4, 5, 6, 7, 8, 9])
>>> x[ np.where(x > 2) ]  # index tuple to index
array([3, 4, 5, 6, 7, 8, 9])
```

Standard Python lists can be concatenated and split along the outermost-dimension. NumPy `ndarray` objects extend this functionality to allow concatenation and split operations against any dimension in the array.

```python
>>> a = [[1,2],[3,4]]
>>> b = [[5,6],[7,8]]
>>> x = np.concatenate([a,b], axis=0) # concatenate by row (axis-0)
>>> x
array([[1, 2],
       [3, 4],
       [5, 6],
       [7, 8]])
>>> y = np.concatenate([a,b], axis=1) # concatenate by column (axis-1)
>>> y
array([[1, 2, 5, 6],
       [3, 4, 7, 8]])

>>> np.split(x, 2, axis=0)            # split between rows 1,2 (axis-0)
[array([[1, 2],
       [3, 4]]), array([[5, 6],
       [7, 8]])]
>>> np.split(x, 2, axis=1)            # split betwen cols 1,2 (axis-1)
[array([[1],
       [3],
       [5],
       [7]]), array([[2],
       [4],
       [6],
       [8]])]
```

When copying `ndarray` objects, it is important to know that when Python assigns one object to another object, e.g. `y = x`, `y` is only a *shallow copy* of `x`. A shallow copy sets `y` to share the value stored in memory by variable `x` (i.e. both variables reference the same value in memory). What that means is when the value of `x` changes, so does the value of `y`.


```python
>>> x = np.arange(8)  # create variable
>>> x
array([0, 1, 2, 3, 4, 5, 6, 7])
>>> y = x             # shallow copy of x into y
>>> x.shape = (2,4)   # change shape of x
>>> y                 # ... reflected in y
array([[0, 1, 2, 3],
       [4, 5, 6, 7]])
```

In contrast, a *deep copy* will create a new value for `y` with its own memory allocation. In this case, changing the value of `x` does not change the value of `y`. In NumPy, you can create a deep copy of an `ndarray` object with `numpy.copy`. (NB: Python also provides the `copy.deepcopy()` function in the `copy` module for deep-copies.)

```python
>>> x = np.arange(8)  # create variable
>>> x
array([0, 1, 2, 3, 4, 5, 6, 7])
>>> y = np.copy(x)    # deep copy of x into y
>>> x.shape = (2,4)   # change shape of x
>>> y                 # ... y is unchanged
array([0, 1, 2, 3, 4, 5, 6, 7])
```

Standard Python mathematical operators generally apply to a single-valued variable at a time (e.g. `2 * 3` works, but not `[1,2] * [3,4]`). NumPy provides an arsenal of standard mathematical operations for analyzing `ndarray` objects. These operations apply to each element in the `ndarray` container in a predictable manner. First, let's consider standard array-wise arithmetic operations.

```python
>>> a = [1, 2]
>>> b = [3, 4]
>>> np.add(a, b)             # addition
array([4, 6])
>>> np.subtract(a,b)         # substraction
array([-2, -2])
>>> np.multiply(a,b)         # multiplication
array([3, 8])
>>> np.divide(a, b)          # division (exact)
array([0.33333333, 0.5])
>>> np.power(a, b)           # raise-to-power
array([ 1, 16])
>>> np.power(a, 2)           # raise-to-power
array([1, 4])
>>> np.mod(a, b)             # remainder
array([1, 2])
```

NumPy also supports several forms of array-wise rounding.


```python
>>> np.around( [1.023, 3.948], 2 )   # round up/down to digit
array([1.02, 3.95])
>>> np.ceil( [1.023, 3.948] )        # round up to next whole number
array([2., 4.])
>>> np.floor(  [1.023, 3.948] )      # round down to next whole number
array([1., 3.])
```

Functions for simple statistical operations are provided by NumPy. [SciPy](https://scipy.org), NumPy's sister project, greatly expands the statistical functionality of `ndarray` objects through its `scipy.stats` module. (We'll learn about SciPy in the next lab.)

```python
>>> a = [ 1.9, 2.8, 5.7, 6.6, 8.5 ]
>>> np.sum(a)            # sum
25.5
>>> np.amin(a)           # minimum value
1.9
>>> np.amax(a)           # maximum value
8.5
>>> np.percentile(a, 20) # 20th percentile
2.6199999999999997
>>> np.median(a)         # 50th percentile
5.7
>>> np.mean(a)           # mean
5.1
>>> np.var(a)            # variance
5.94
>>> np.std(a)            # standard deviation
2.4372115213907883
```

NumPy also supports modest set of linear algebra operations through the `numpy.linalg` module; SciPy offers more, even though many of its linear algebra functions are simply wrappers for `numpy.linalg` functions.

```python
>>> a = np.array( [[1,2],[3,4]] )
>>> b = np.array( [[5,6],[7,8]] )
>>> np.matmul(a,b)                   # matrix-multiply
array([[19, 22],
       [43, 50]])
>>> np.linalg.det(a)                 # matrix determinant
-2.0000000000000004 
>>> np.linalg.inv(a)                 # matrix inverse
array([[-2. ,  1. ],
       [ 1.5, -0.5]])
>>> np.linalg.solve(a, np.eye(2))    # solves Ax = B
array([[-3., -4.],
       [ 4.,  5.]])
>>> np.linalg.eig(a)                 # get eigensystem
(array([-0.37228132,  5.37228132]),  # ... eigenvalues
 array([[-0.82456484, -0.41597356],  # ... eigenvectors
       [ 0.56576746, -0.90937671]]))
>>> np.kron(a,b)                     # Kronecker product
array([[ 5,  6, 10, 12],
       [ 7,  8, 14, 16],
       [15, 18, 20, 24],
       [21, 24, 28, 32]])
```

Now you should be familiar enough with NumPy's basic features to judge whether or not it would be useful to incorporate into your future (or ongoing!) projects. Submit `lab-20.ipynb' to your assignment repository to receive credit.
