# Lab 18

*Lab 18 GitHub Classroom link:* https://classroom.github.com/a/LDp-UZQK

We'll learn how to access a Jupyter session that is hosted on a remote computer, and how to produce Matplotlib visualizations using Jupyter notebooks.

This lab will cover the following topics

1. Installing Jupyter
2. Using Jupyter
3. Matplotlib

Follow the instructions in this lab to generate five standard Matplotlib plots in a Jupyter notebook. To complete this assignment, submit your Jupyter notebook file (`lab-18.ipynb`) through GitHub Classroom.

---

## Using Jupyter

Jupyter is a platform for hosting interactive and web-accessible programming notebooks. Jupyter notebooks act as a programming environment, playing a role similar to a standard `python` or `ipython` shell session. Jupyter notebooks also allow the programmer to enter commands, have access to local filesystem objects, and report output to the programmer. Rather than entering commands through a terminal session, Jupyter notebooks are accessed through a standard webpage browser and edited through a GUI.

By default, `jupyter` is not installed on most operating systems, including the Ubuntu installation on the virtual machines. To install the Python `jupyter` package on your virtual machine, type:
```console
$ sudo apt-get install jupyter
... installing ...
```

Next, navigate to your lab assignment repository, then call the following command to begin hosting Jupyter notebook services

```console
$ jupyter notebook --no-browser --port=8080
[I 14:49:32.666 NotebookApp] Serving notebooks from local directory: /home/mlandis/labs/lab-11b-mlandis
[I 14:49:32.666 NotebookApp] Jupyter Notebook 6.1.5 is running at:
[I 14:49:32.666 NotebookApp] http://localhost:8080/?token=2d5d02d2deaf55cfe84c63697aa27c662ab3250c482e8956
[I 14:49:32.666 NotebookApp]  or http://127.0.0.1:8080/?token=2d5d02d2deaf55cfe84c63697aa27c662ab3250c482e8956
[I 14:49:32.666 NotebookApp] Use Control-C to stop this server and shut down all kernels (twice to skip confirmation).
[C 14:49:32.671 NotebookApp]

    To access the notebook, open this file in a browser:
        file:///home/mlandis/.local/share/jupyter/runtime/nbserver-408002-open.html
    Or copy and paste one of these URLs:
        http://localhost:8080/?token=2d5d02d2deaf55cfe84c63697aa27c662ab3250c482e8956
     or http://127.0.0.1:8080/?token=2d5d02d2deaf55cfe84c63697aa27c662ab3250c482e8956
```

Once Jupyter is running on your virtual machine, return to your laptop. You will now open an SSH session that routes web traffic directed to the local computer on port 8080 towards the port 8080 on the virtual machine. In essence, this means that when `https://localhost:8080` is opened on your local computer, it will send and receive information hosted by the Jupyter notebook webpage running on the virtual machine through port 8080 over the secure shell (SSH) protocol.

If your personal computer runs a Unix-based operating system, such as Mac OS X or Linux, do the following. Open a new Terminal session, then run the following `ssh` command.

```console
$ ssh -N -L localhost:8080:localhost:8080 mlandis@128.252.89.47
mlandis@128.252.89.47's password:

... now the session hangs, which you can
    cancel eventually with ctrl-C ...
```

If your personal computer runs Windows 10, then you will instead need to open Powershell. Press Windows-R (Run), enter the command `powershell`, then strike enter. This will open a command line interface called Powershell. In Powershell, then type the command

```console
$ ssh -N -L localhost:8080:localhost:8080 mlandis@128.252.89.47
mlandis@128.252.89.47's password:

... now the session hangs, which you can
    cancel eventually with ctrl-C ...
```
On either system, the SSH session will "hang" and appear unresponsive once you correctly enter the password. Don't worry. Do not cancel the session. This is expected behavior.

Once your SSH session is established, open your preferred web browser on your workstation, then enter the website published by your virtual machine after you launched the Jupyter server. This will open a webpage to a Jupyter notebook. The web interface will display the filesystem of your virtual machine. For example, after starting the `jupyter notebook` service on my virtual machine, the program published the URL `http://localhost:8080/?token=b469720c401039446614120787cd21a970628537a6f0fc5d`. Each time `jupyter notebook` is run, the server using a different unique token for access. I only need to enter this URL with the correct token into my web browser to open the Jupyter interface.

---

## Using Jupyter

[Jupyter]() is an open source project that develops tools and resources for writing code using online development environments. Although Jupyter was originally designed for use with Python, it's been extended to support development environments for a large number of languages. Nonetheless, we will assume that we are using Jupyter with Python for this lab and beyond. As a tool, Jupyter is very popular, especially as an introductory tool for students learning how to program. Features for Jupyter can be explored through its high-quality [documentation](https://jupyter.org/documentation). The documentation for the [Jupyter notebook interface](https://jupyter-notebook.readthedocs.io/en/stable/notebook.html) is particularly useful.

Perhaps the most defining feature of Jupyter is its use of *notebooks*. A notebook is a special file, identified by the extension `.ipynb`, that describes a Python shell session. What is different about a notebook is that (1) it stores the code and the output of Python commands, (2) blocks of code are entered into *cells*, which can be re-run in any order and at any time through the Jupyter interface, and (3) it allows code, text, and graphics to be written into the same document, side-by-side.

This third feature will allow us to produce images using Matplotlib through our virtual machines, and seamlessly display the figures through the Jupyter notebook. We'll explore this more in the next section.

For now, let's create a Python notebook, and perform a simple programming task.  Click on "New" in the upper-right corner, then select "Python 3" from the dropdown menu. This will create a new notebook in the local directory named `Untitled.ipynb`.

Click on the name "Untitled" at the top of the screen, and rename the notebook as "Example".

Jupyter notebooks organizes content through cells. Each cell has a different "type". In the first cell, enter the code `x = 'GATTACA'`. Then press enter, and enter the code `print(x)`. Notice that when you press enter, it adds a new line of unexecuted code to edit, but does not execute the previous code. To execute the code for a cell, click the "Run" button or press Command-Enter (on Mac). Now, modify `x = 'GATTACA'` to instead read `x = 'a'.join(['b','n','n','p','j','m','s'])`. That cell should now print new text when executed.

To add more cells to the notebook, first click a cell to select it, then press `A` to add a new cell **a**bove the current cell, or `B` to add the cell **b**elow the current cell.

Press `A` to add a second cell to the notebook. Now, find the dropdown menu that reads "Code" and select "Markdown". Instead of entering Python code, type in the lines
```
# My glorious notebook
I do hope you enjoy reading it.
```
then "Run" the cell. The above Markdown code will be reformatted and published to the first cell of the notebook. But perhaps that cell is a little excessive. To delete the first cell, click on it, then press `D` once and `D` again.

Finally, once any cell creates a variable, any other cell can make use of that variable as well. Create new Python cell that contains the code `x.split('a')` and run it.

Now, create one final cell that contains the code
```python
import matplotlib.pyplot as plt
plt.plot([1,2,3,4])
plt.ylabel('some numbers')
plt.show()
```
then execute that cell. When complete, the cell will display a simple line-plot to your Jupyter interface.

Jupyter notebooks save automatically. When in doubt, you can always force Jupyter to save your notebook. To share your work, you may also export the notebook by clicking "File -> Download as" then choosing whichever output format you prefer. Some formats are more easily modifiable (`.py`) than others (`.pdf`).

When you are done editing your notebook, click Logout in the upper-right corner of the notebook editing interface. To shut down the Jupyter session, you can either press Quit from your local workstation, or you can press Ctrl-C from the virtual machine that's hosting Jupyter services.

---

## Intro to Matplotlib

[Matplotlib](https://matplotlib.org/) is an open source Python library for visualizations. The library comes with a superb [User's Guide](https://matplotlib.org/users/index.html) to help new Matplotlib programmers become familiar with the library's features. Matplotlib also publishes a [gallery](https://matplotlib.org/gallery/index.html) of attractive figures, along with the code that was used to produce the images. When browsing the online documentation, note that most Matplotlib functions are encoded as hyperlinks; clicking those links will provide you with more information about what the function does, what arguments it accepts, and what output to expect.

As we'd done in the previous section, we'll continue to use Jupyter notebooks to generate Matplotlib visualizations through our remote virtual machines that we can view from our personal computers. 

First, create a new notebook called `lab-18.ipynb` through the Jupyter Notebook interface. In the first cell, we will import all the libraries we'll use in the remaining cells, and set the random seed for the analysis. What is the random seed? When computers generate "random" numbers, the random numbers are in fact a sequence of pseudorandom numbers, where each value in the sequence is perfectly determined by a starting value, known as the *random number seed*.

```python
# Import libraries
import matplotlib
import matplotlib.pyplot as plt
import numpy as np

# Fixing random state for reproducibility
np.random.seed(19680801)
```

Each of the next five sections will provide code to create a new plot of each type. To run the below code, create five new cells at the end of your Jupyter notebok by pressing the 'B' key five times. In each cell, add the code for one plot type.


### Line plots

Line plots display how the value of one continuous-valued variable (y-axis) changes as a function of a second continuous-valued variable (x-axis). Line plots are used to represent how the value of a process (y-axis) varies over time (x-axis), how a genomic feature (y-axis) varies against sequence position (x-axis), or how the probability density (y-axis) of random variable changes with the variable's value (x-axis).


```python
# Data for plotting
t = np.arange(0.0, 2.0, 0.01)  # [ 0.00, 0.01, ..., 1.99, 2.00 ]
s = 1 + np.sin(2 * np.pi * t)  # sinusoidal wave

fig, ax = plt.subplots()       # create empty plot, save figure and axes
ax.plot(t, s)                  # plot x=t, y=s

# set x/y labels and title
ax.set(xlabel='time (s)', ylabel='voltage (mV)',
       title='About as simple as it gets, folks')
ax.grid()                      # add grid to plot background

fig.savefig("test.png")        # save plot to file
plt.show()                     # display plot to screen (Jupyter)
```



### Scatter plots

Like line plots, scatter plots display how two continuous-valued variables are related to one another. Whereas line plots generally assume that the data have an inherent order, e.g. that x[i-1] < x[i] < x[i+1], the data for scatter plots are unordered. One use of scatter plots is to quickly visualize whether two variables are correlated. Correlated variables tend to "slant" from lower left to upper right in scatterplots, in the sense that large values for variable 1 predict large values for variable 2, and vice verse. Scatter plots with an "anti-slant" from upper left to lower right have a negative correlation.

```python
# generate random data points for x-axis
x = np.arange(0.0, 50.0, 2.0)
# transform y = f(x)
y = x ** 1.3 + np.random.rand(*x.shape) * 30.0
# random sizes for points
s = np.random.rand(*x.shape) * 800 + 500
# generate scatter plot
plt.scatter(x, y, s, c="g",             # set color as green
            alpha=0.5,                  # transparent markers
            marker=r'$\clubsuit$',      # change marker symbol
            label="Luck")               # figure title
plt.xlabel("Leprechauns")               # x-axis label
plt.ylabel("Gold")                      # y-axis label
plt.legend(loc='upper left')            # figure legend
plt.show()                              # print to screen
```

### Bar plots

Barplots are used to compare continuous values across different categorical values. Standard barplots show the categories on the x-axis and the values for each category on the y-axis. Stacked barplots can be used to condense information; for example, the stacked barplots below both present the number of male and female score datapoints, along with the total number of score datapoints per "stack".

```python
N = 5                                  # five datapoints (hardcoded example)
menMeans = (20, 35, 30, 35, 27)        # tuple for men's means
womenMeans = (25, 32, 34, 20, 25)      # tuple for women's means
menStd = (2, 3, 4, 1, 2)               # tuple for men's standard deviations
womenStd = (3, 5, 2, 3, 3)             # tuple for women's standard deviations
ind = np.arange(N)                     # x-locations for groups
width = 0.35                           # the width of the bars

# plot men's values
p1 = plt.bar(ind, menMeans, width, yerr=menStd)
# plot women's values (bottom argument creates "stack")
p2 = plt.bar(ind, womenMeans, width,
             bottom=menMeans, yerr=womenStd)

plt.ylabel('Scores')                              # y-axis label
plt.title('Scores by group and gender')           # figure title
plt.xticks(ind, ('G1', 'G2', 'G3', 'G4', 'G5'))   # x-tick labels
plt.yticks(np.arange(0, 81, 10))                  # y-tick labels
plt.legend((p1[0], p2[0]), ('Men', 'Women'))      # color legend
                                                  # first arg (p1[0],p2[0]) sets color

plt.show()                                        # show plot
```

### Histogram

Histograms are used to report the relative frequencies of binned data points. These plots are particularly useful for comparing how a sample of data (which is finite in number, by definition) to a theoretical distribution of data (which can assume infinite data). Below, we compare a histogram of data simulated under a normal distribution to relative proportions of data expected under the normal distribution itself.

```python
# example data
mu = 100                               # mean of distribution
sigma = 15                             # standard deviation of distribution
x = mu + sigma * np.random.randn(437)  # generate 437 normal variates
num_bins = 50                          # bin values into 50 intervals

# generate empty plot; save figure + axis objects
fig, ax = plt.subplots()

# the histogram of the data
n, bins, patches = ax.hist(x, num_bins, density=1)

# add a 'best fit' line
y = ((1 / (np.sqrt(2 * np.pi) * sigma)) *
     np.exp(-0.5 * (1 / sigma * (bins - mu))**2))
ax.plot(bins, y, '--')                            # plot line
ax.set_xlabel('Smarts')                           # set x-axis label
ax.set_ylabel('Probability density')              # set y-axis label
title=r'Histogram of IQ: $\mu=100$, $\sigma=15$'  # this is LaTeX (math) formatted string
ax.set_title(title)                               # set figure title

# Tweak spacing to prevent clipping of ylabel
fig.tight_layout()                                # figure formatting
plt.show()                                        # displays figure in session
```

### Heat maps

Heat maps are useful for revealing relationships in three-dimensional datasets, and in particular, how a third variable reponds to the values of the two other variables. The first two dimensions (x, y) often have continuous values (e.g. -100 to 100) or categorical values (e.g. red, blue, yellow, ...), while the third dimension (z) is continuous. For example, heat maps can be used to visualize how gene expression levels (z) differ acrosss species (x) and genes (y).

```python
# Define numbers of data points and bins per axis.
N_numbers = 100000         # how many data points, in total
N_bins = 100               # how many bins per x,y axis

# Generate 2D normally distributed numbers.
x, y = np.random.multivariate_normal(
        mean=[0.0, 0.0],   # mean
        cov=[[1.0, 0.4],
             [0.4, 0.25]], # covariance matrix
        size=N_numbers
        ).T                # transpose into columns


# Construct 2D histogram using the 'plasma' colormap
plt.hist2d(x, y, bins=N_bins, cmap='plasma')

# Plot a colorbar with label.
cb = plt.colorbar()
cb.set_label('Number of entries')

# Add title and labels to plot.
title='Heatmap of 2D normally distributed data points'
plt.title(title)
plt.xlabel('x axis')
plt.ylabel('y axis')

# Show the plot.
plt.show()
```

---

Save and close the Jupyter notebook after you have generated each of the above plots. Once closed, commit and push the `lab-18.ipynb` file that you saved to your GitHub repository.
