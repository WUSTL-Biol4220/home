# Lab 13A

*Lab 13A GitHub Classroom link:* https://classroom.github.com/a/Gjy6fm47

In this lab, we will explore several of SciPy's many features for processing quantitative data. To complete this assignment, complete the exercises in a Jupyter notebook (`lab-13a.ipynb`), then submit the notebook through GitHub Classroom. See [Lab 12A](https://github.com/WUSTL-Biol4220/home/blob/master/labs/lab_12A.md) for instructions to connect to a Jupyter Notebook server hosted through your virtual machine.

---

## SciPy

[SciPy](https://www.scipy.org/) is an open source ecosystem that supports scientific computing in Python. The SciPy project is best known for developing and maintaining the SciPy Python library. The SciPy library is fully [documented](https://docs.scipy.org/doc/scipy/reference/), and is accompanied by [tutorials](https://docs.scipy.org/doc/scipy/reference/tutorial/index.html) that demonstrate what the library offers. Library features include:

| Package             | Features |
| ---                 | --- |
| `scipy.cluster`     | clustering methods |
| `scipy.constants`   | numerical constants |
| `scipy.fft`         | discrete Fourier transforms |
| `scipy.integrate`   | integration and ODEs |
| `scipy.interpolate` | interpolation |
| `scipy.io`          | input and output |
| `scipy.linalg`      | linear algebra |
| `scipy.misc`        | miscellaneous routines |
| `scipy.ndimage`     | multidimensional image processing |
| `scipy.odr`         | orthogonal distance regression |
| `scipy.optimize`    | optimization and root-finding |
| `scipy.signal`      | signal processing |
| `scipy.sparse`      | sparse matrices |
| `scipy.special`     | special functions |
| `scipy.stats`       | statistical functions |

In this lab, we will explore several SciPy packages that are useful for analyzing biological datasets: `scipy.constants`, `scipy.stats`, `scipy.optimize`, `scipy.integrate`, and `scipy.cluster`.

You will need to install the SciPy library on your virtual machine, which may be done with the command `pip install scipy`.

### `scipy.constants`

The `scipy.constants` provides a dictionary of nearly 400 mathematical and physical constants. The value for a constant may be referenced by name directly (e.g. `scipy.constants.pi`). Any constant -- along with its value, unit, and precision -- can also be extracted from the dictionary, `scipy.constants.physical_constants`.

```python
>>> from scipy import constants
>>> constants.pi                               # pi
3.141592653589793
>>> constants.golden                           # golden ratio, (1+5^.5)/2
1.618033988749895
>>> constants.Avogadro                         # Avogadro's number
6.022140857e+23
>>> constants.speed_of_light                   # speed of light in vacuum
299792458.0
>>> constants.electron_mass                    # mass of electron
9.10938356e-31
>>> constants.proton_mass                      # mass of proton
1.672621898e-27
>>> constants.neutron_mass                     # mass of neutron
1.674927471e-27
>>> scipy.constants.physical_constants.keys()  # returns (values, units, precision)
>>> scipy.constants.physical_constants         # ... contains 100's of items
{'Wien displacement law constant': (0.0028977685, 'm K', 5.1e-09),
 'atomic unit of 1st hyperpolarizablity': (3.20636151e-53, 'C^3 m^3 J^-2', 2.8e-60),
 'atomic unit of 2nd hyperpolarizablity': (6.2353808e-65, 'C^4 m^4 J^-3', 1.1e-71),
 'atomic unit of electric dipole moment': (8.47835309e-30, 'C m', 7.3e-37),
 'atomic unit of electric polarizablity': (1.648777274e-41, 'C^2 m^2 J^-1', 1.6e-49),
 'atomic unit of electric quadrupole moment': (4.48655124e-40, 'C m^2', 3.9e-47),
 ...
```

### `scipy.stats`

Python developers generally rely on `scipy.stats` for standard statistical operations. Although we will only explore a few of `scipy.stats` many features, the package defines functions and classes for probability distributions, statistical tests, frequency statistics, summary statistics, statistical distances, contingency tables, correlation tests, and kernel density estimators.

Let's begin with probability distributions. `scipy.stats` provides a large number of probability distributions for both continuous and discrete values. All distributions in `scipy.stats` share similar methods with similar arguments, making it easy to "plug-and-play" with different distributions, once the interface is mastered. For example, suppose one wanted to work with a [normal distribution](https://en.wikipedia.org/wiki/Normal_distribution). With the SciPy normal distribution, one could simulate new data (`scipy.stats.norm.rvs()`); compute the probability density for a set of points (`scipy.stats.norm.pdf()`); determine the mean, variance, and other expectations of the distribution (`scipy.stats.norm.stats()`); and fit the distribution's parameters to a given dataset (`scipy.stats.norm.fit()`).

```python
>>> from scipy import stats
>>> # distribution object
>>> stats.norm
<scipy.stats._continuous_distns.norm_gen object at 0x7fdf98b67d68>
>>> # generate 4 normal RVs
>>> x = stats.norm.rvs(loc=10,scale=2,size=4)
array([10.11179033, 10.10902411, 10.65111753, 10.32368948])
>>> stats.norm.pdf(x=x, loc=10, scale=2 )
array([0.19915978, 0.19917499, 0.18917553, 0.19687573])
>>> # return mean, variance, skewness, kurtosis (mvsk)
>>> stats.norm.stats(loc=10, scale=2, \     
                     moments='mvsk')
(array(10.), array(4.), array(0.), array(0.))
>>> # generate 1000 normal RVs with mean=10, scale=2
>>> y = stats.norm.rvs(loc=10,scale=2,size=1000)
>>> # estimate mean and scale from simulated data
>>> stats.norm.fit( data=y, loc=50, scale=9 
(9.939835173664239, 2.004585580838588)
```

Simulated data can be especially helpful for generating test datasets, e.g. for use with Matplotlib.

```python
>>> from scipy import stats
>>> import matplotlib
>>> import matplotlib.pyplot as plt
>>> # simulate 10000 RVs, mean=10, scale=2
>>> y = stats.norm.rvs(loc=10,scale=2,size=10000)
>>> y
array([13.23832222, 13.05731999,  7.30259037, ...,  9.8595785,
        9.46715211,  9.98579946])
>>> fig,ax = plt.subplots()
>>> p = ax.hist(y,bins=50)
>>> fig.show()
```

The `scipy.stats` package defines functions for several summary statistics that are not available in the `numpy` or `math` packages, including functions for harmonic and geometric means, functions to compute higher moments, and methods to describe sample data.

```python
>>> from scipy import stats
>>> import numpy as np
>>> x = stats.norm.rvs(loc=10, scale=2, size=1000)
>>> np.mean(x)         # sample mean
9.907750191507521
>>> stats.hmean(x)     # harmonic mean
9.4599529015089185
>>> stats.gmean(x)     # geometric mean
9.6924828402578722
>>> stats.sem(x)       # standard error of sample mean
0.06353084579162438
>>> stats.skew(x)      # sample skew (asymmetry)
0.011612124738411802
>>> stats.kurtosis(x)  # sample kurtosis (fat-tailedness)
-0.0055425614273967305
>>> stats.describe(x)  # give summary of sample data
DescribeResult(nobs=1000,
               minmax=(3.7313631618255805, 16.221776607589973),
               mean=9.907750191507521,
               variance=4.0361683669991582,
               skewness=0.011612124738411802,
               kurtosis=-0.0055425614273967305)
```

Last among the `scipy.stats` features we'll consider are kernel densitory estimators (KDEs). KDEs estimate the probability density function for a sample of data by using a non-parametric mixture of weighted distributions, called kernels. In essence, this means that one could compute the relative probability for new data points based on previously sampled data points. `scipy.stats` provides a function for kernels based on the Gaussian (i.e. normal) distribution. Below, we see that the distribution estimated with the KDE (orange line) fits the underlying dataset (blue histogram) quite nicely.


```python
>>> from scipy import stats
>>> import matplotlib
>>> import matplotlib.pyplot as plt
>>> a = stats.norm.rvs(loc=12,scale=2,size=10000)  # create samples, a
>>> b = stats.norm.rvs(loc=6,scale=1,size=10000)   # create samples, b
>>> z = np.append(a, b)                  # mix samples a and b
>>> f = stats.gaussian_kde(z)            # fit KDE object to data, z
>>> x = np.arange(0,20,0.1)              # range of input values for f()
>>> f(x)                                 # density for each value, f(pos)
array([1.33471717e-11, 4.45526152e-11, 1.42288247e-10, 4.34870069e-10,
       1.27215449e-09, 3.56303164e-09, 9.55708453e-09, 2.45585700e-08,
       6.04813171e-08, 1.42815299e-07, 3.23510616e-07, 7.03432155e-07,
       ...
>>> fig,ax = plt.subplots()              # create empty plot
>>> h = ax.hist(z,bins=50,density=True)  # plot histogram (normalized)
>>> ax.plot(x, f(x))                     # plot KDE curve
>>> plt.show()                           # show plot
```

### `scipy.optimize`

Optimization methods attempt to find the arguments that optimize the value of a given function. In the below example, we will define a Python function for the Rosenbrock function. The Rosenbrock function was designed to test the performance of optimization methods, and has the form `f(x,y) = (1-x)^2 + 100*(y-x^2)^2` with a minimum value of `f(1,1)=0`. We will apply the `scipy.optimize.minimize` method below to numerically estimate what parameters minimize `f(x,y)` using the [Nelder-Mead](https://en.wikipedia.org/wiki/Nelder%E2%80%93Mead_method) method. Although we are considering a simple function with two parameters in the below example, Nelder-Mead works reasonably well with larger numbers of parameters. Note, `scipy.optimize.minimize` can be used for maximization when the user-defined function returns the negative value of function's true value.

```python
>>> import numpy as np
>>> from scipy.optimize import minimize
>>> def rosen(x):
...     # Rosenbrock function, for a=1 and b=100
...     # f(x,y) = (1-x)^2 + 100*(y-x^2)^2
...     return (1.0-x[0])**2 + 100.0*(x[1]-x[0]**2.0)**2.0
>>>
>>> rosen( [1.0, 1.0] )         # optimal value, f(1,1) = 0.0
0.0
>>> rosen( [1.01, 1.01] )       # worse value
0.010300999999999994
>>> rosen( [1.05, 1.05] )       # worse value
0.2781249999999999
>>> x0 = np.array([1.3, 0.7])   # initial guess
>>> # find the optimal value for x
>>> res = minimize(rosen, x0, method='nelder-mead',
                   options={'xatol': 1e-8, 'disp': True})
Optimization terminated successfully.
         Current function value: 0.000000
         Iterations: 79
         Function evaluations: 150
>>> print(res.x)                # estimate for x
[1. 1.]               
>>> print(res.fun)              # minimum, approx 0.0
3.3736077629532093e-18
```

### `scipy.integrate`

The `scipy.integrate` package allows programmers to integrate using adaptive quadrature (`scipy.integrate.quad`), at fixed points using trapezoidal or Simpson's integration (`scipy.integrate.simps` or `scipy.integrate.trapz`), or to integrate ordinary differential equations (`scipy.integrate.solve_ivp`). Below, we will consider the simple example, comparing numerical results under adaptive quadrature to the analytical result.

```python
>>> from scipy import integrate
>>> # define function to integrate
>>> def x2(x):
...     return x**2
...
>>> # numerical integration using quadrature
>>> y, err = integrate.quad(x2, 0, 4)
>>> y
21.333333333333336      # numerical integrand
>>> err
2.368475785867001e-13   # numerical error
>>> 
>>> print(4**3 / 3.)    # analytical result
21.3333333333
```

### `scipy.cluster`

SciPy offers several methods for clustering data, including vector quantization, hierarchical clustering, and k-means. The [k-means](https://en.wikipedia.org/wiki/K-means_clustering) method is a procedure that labels each input data point as belonging to any one of *k* possible clusters. The procedure works by iteratively optimizing the mean and variance for the data assigned to each of the $k$ clusters, while simultaneously reassigning which datapoints belong to which clusters. For illustrative purposes, below is a simple example of k-means for a two-dimensional dataset. However, k-means is a useful tool for detecting hidden structures in higher dimensional datasets that are often encountered in large genomic datasets.

```python
>>> import numpy as np
>>> from scipy.cluster.vq import vq, kmeans, whiten
>>> import matplotlib.pyplot as plt
>>> # 50 pts at (0,0)
>>> a = np.random.multivariate_normal([ 0,  0],
...                                   [[ 4, 1], [1, 4]],
...                                   size=50)
...
>>> # 50 pts at (30,10)
>>> b = np.random.multivariate_normal([30, 10],
...                                   [[10, 2], [2, 1]],
...                                   size=50) 
...
>>> features = np.concatenate((a, b))    # x = [ a, b ]
>>> x = whiten(features)                 # normalize data
>>> y, e = kmeans(whitened, 2)           # infer k=2 means
>>> plt.scatter(x[:, 0], x[:, 1])        # plot data, x
>>> plt.scatter(y[:, 0], y[:, 1], c='r') # plot means, y
>>> plt.show()
```

Once you have executed all of the above code through the Jupyter notebook, save and close the notebook, then commit and push the notebook to your GitHub classroom assignment repository.
