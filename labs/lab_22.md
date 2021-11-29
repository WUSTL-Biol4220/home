# Lab 22

*Lab 22 GitHub Classroom link:* https://classroom.github.com/a/CVwZ17I1

This lab will explore how to work with data tables through the Python package, Pandas. To complete this assignment, complete the exercises in a Jupyter notebook (`lab-22.ipynb`), then submit the notebook through GitHub Classroom. See [Lab 19](https://github.com/WUSTL-Biol4220/home/blob/master/labs/lab_19.md) for instructions to connect to a Jupyter Notebook server hosted through your virtual machine.

---

## Pandas

[Pandas](https://pandas.pydata.org/) is an open source Python package that provides user-friendly and computationally efficient methods and objects for working with 1D and 2D data tables or spreadsheets. Pandas provides extensive [documentation](https://pandas.pydata.org/docs/) explaining how its code works, through guided [tutorials](https://pandas.pydata.org/docs/getting_started/index.html#getting-started), [cheat sheets](https://pandas.pydata.org/Pandas_Cheat_Sheet.pdf), and technical [developer guides](https://pandas.pydata.org/docs/reference/index.html).

In this lab, we will practice using some of the basic features of Pandas.

Enter the cloned repository for Lab 22 in your file system. It will contain the example data tables `codons.csv` and `amino_acids.csv`, both of which are in a comma-separated value format.

View the contents of `codons.csv`:

```bash
$ cat codons.csv
codon,abbr,code
AAA,Lys,K
AAC,Asn,N
AAG,Lys,K
AAT,Asn,N
ACA,Thr,T
ACC,Thr,T
ACG,Thr,T
ACT,Thr,T
AGA,Arg,R
...
TTG,Leu,L
TTT,Phe,F
```

Pandas should already be installed on your virtual machines. Regardless, installing it is easy:
```bash
$ pip install pandas
```

In your notebook, create a `pd.DataFrame` object from `codon.csv` using Pandas:

```python
>>> import pandas as pd
>>> fn = 'codons.csv'
>>> codon = pd.read_table(fn, sep=',')
>>> codon

   codon abbr code
0    AAA  Lys    K
1    AAC  Asn    N
2    AAG  Lys    K
3    AAT  Asn    N
4    ACA  Thr    T
..   ...  ...  ...
59   TGT  Cys    C
60   TTA  Leu    L
61   TTC  Phe    F
62   TTG  Leu    L
63   TTT  Phe    F

[64 rows x 3 columns]
```

Pandas will display larger data tables in an abbreviated format. (Notice `codon` only displays the first and last five rows out of all 64.)

Part of what makes Pandas so useful is that it allows programmers to easily import/export data tables across a wide variety of formats. In effect, this makes it easy to explore datasets using Python without needing to write custom data parsers.

```python
>>> # read data into new DataFrame
>>> pd.read_<PRESS TAB>
pd.read_clipboard(  pd.read_gbq(        pd.read_parquet(    pd.read_sql_query(
pd.read_csv(        pd.read_hdf(        pd.read_pickle(     pd.read_sql_table(
pd.read_excel(      pd.read_html(       pd.read_sas(        pd.read_stata(
pd.read_feather(    pd.read_json(       pd.read_spss(       pd.read_table(
pd.read_fwf(        pd.read_orc(        pd.read_sql(

>>> df = pd.DataFrame() # create empty DataFrame to explore methods
>>> # return values of DataFrame as new type
>>> df.to_<PRESS TAB>
df.to_clipboard(  df.to_gbq(        df.to_markdown(   df.to_records(    df.to_xarray(
df.to_csv(        df.to_hdf(        df.to_numpy(      df.to_sql(
df.to_dict(       df.to_html(       df.to_parquet(    df.to_stata(
df.to_excel(      df.to_json(       df.to_period(     df.to_string(
df.to_feather(    df.to_latex(      df.to_pickle(     df.to_timestamp(

>>> # example: read csv, then write to excel
>>> df = pd.read_csv(‘amino_acids.csv')
>>> df.to_excel(‘amino_acids.xlsx')
```

Once a Pandas container is created from a data table in the filesystem, it helps to know the size and dimensions of the new container, and how its rows and columns (axes) are named.

```python
>>> codon = pd.read_csv('codons.csv', sep=',')
>>> # shape returns ordered sizes of dimensions
>>> codon.shape
(64, 3)
>>> # total size is the product of all dimension sizes
>>> codon.size
192
>>> # labeled column names
>>> codon.columns
Index(['codon', 'abbr', 'code'], dtype='object’)
>>> # unlabeled row (index) names
>>> codon.index
RangeIndex(start=0, stop=64, step=1)
>>> # row and column info
>>> codon.axes
[RangeIndex(start=0, stop=64, step=1), Index(['codon', 'abbr', 'code’],
 dtype='object')]
```

It is also useful to review the contents of a dataframe after it is loaded. Use the `.head()` and `.tail()` method for the new dataframe to view only its first/last rows.

```python
>>> codon # partial view of data frame
   codon abbr code
0    AAA  Lys    K
1    AAC  Asn    N
2    AAG  Lys    K
3    AAT  Asn    N
4    ACA  Thr    T
..   ...  ...  ...
59   TGT  Cys    C
60   TTA  Leu    L
61   TTC  Phe    F
62   TTG  Leu    L
63   TTT  Phe    F

[64 rows x 3 columns]
>>> codon.head(3) # first three rows
  codon abbr code
0   AAA  Lys    K
1   AAC  Asn    N
2   AAG  Lys    K
>>> codon.tail(3) # last three rows
   codon abbr code
61   TTC  Phe    F
62   TTG  Leu    L
63   TTT  Phe    F
>>>
```

Information about the dimensions, size, column datatypes and memory usage are summarized with `.info()`. Pandas represents strings using the `object` `Dtype`.

```python
>>> codon.info() # overview of DataFrame properties
<class 'pandas.core.frame.DataFrame'>
RangeIndex: 64 entries, 0 to 63
Data columns (total 3 columns):
 #   Column  Non-Null Count  Dtype
---  ------  --------------  -----
 0   codon   64 non-null     object
 1   abbr    64 non-null     object
 2   code    64 non-null     object
dtypes: object(3)
memory usage: 1.6+ KB
```

The `.describe()` method will print a summary of the range of values for each column.

```python
>>> # summary of DataFrame contents
>>> codon.describe()
       codon abbr code
count     64   64   64
unique    64   21   21
top      AGC  Arg    L
freq       1    6    6
```

Of course, applying the same commands to a different data table will produce different output. View the head and tail of a new amino acid dataframe.

```python
>>> aa = pd.read_csv('amino_acids.csv', sep=',')
>>> aa.head(3)
            name abbr mol_formula  mol_weight  hydrophob
code
A        alanine  Ala     C3H7NO2       89.10         41
R       arginine  Arg   C6H14N4O2      174.20        -14
N     asparagine  Asn    C4H8N2O3      132.12        -28
>>> aa.tail(3)
            name abbr mol_formula  mol_weight  hydrophob
code
W     tryptophan  Trp  C11H12N2O2      204.23         97
Y       tyrosine  Tyr    C9H11NO3      181.19         63
V         valine  Val    C5H11NO2      117.15         76
```

Notice that the datatype (`Dtype`) differs across columns. The `aa` dataframe has a column of floating point numbers (`mol_weight`) and a column of integers (`hydrophob`).

```python
>>> aa.info()
<class 'pandas.core.frame.DataFrame'>
Index: 20 entries, A to V
Data columns (total 5 columns):
 #   Column       Non-Null Count  Dtype
---  ------       --------------  -----
 0   name         20 non-null     object
 1   abbr         20 non-null     object
 2   mol_formula  20 non-null     object
 3   mol_weight   20 non-null     float64
 4   hydrophob    20 non-null     int64
dtypes: float64(1), int64(1), object(3)
memory usage: 1.5+ KB
```

Applying `aa.describe()` summarizes the numerical columns using various quantitative summary statistics (`mean`, `std`, `min`, `max`, quantiles, etc.):

```python
>>> aa.describe()
       mol_weight   hydrophob
count   20.000000   20.000000
mean   136.903000   25.250000
std     30.863209   52.885054
min     75.070000  -55.000000
25%    118.627500  -16.250000
50%    132.615000   10.500000
75%    150.697500   74.500000
max    204.230000  100.000000
```

Pandas defines a 1D-container class (`pandas.Series`) and a 2D-container class (`pandas.DataFrame`). So far, we have only been explicitly working with `pandas.DataFrame` objects. That said, the columns of a `pandas.DataFrame` object are in fact `pandas.Series` object. Importantly, all elements in a `pandas.Series` object have the same datatype (`dtype`) -- e.g. `int64`, `float64`, `object`. Columns in `pandas.DataFrame`, however, may differ in `dtype`.

To understand this better, create a 1D `pandas.Series` object.

```python
>>> data_1d = ['Homo','Pan','Gorilla', 'Pongo']
>>> df_1d = pd.Series(data_1d, name='Genus')
>>> df_1d
0       Homo
1        Pan
2    Gorilla
3      Pongo
Name: Genus, dtype: object
```

Now create a 2D `pandas.DataFrame` object for the same genera.

```python
>>> data_2d = [['Homo', 60], ['Pan', 45], ['Gorilla', 125], ['Pongo', 50]]
>>> df_2d = pd.DataFrame(data_2d, columns=['Genus', 'Mass_kg'])
>>> df_2d
     Genus  Mass_kg
0     Homo       60
1      Pan       45
2  Gorilla      125
3    Pongo       50
```

Notice that the returned column `df_2d['Genus']` closely resembles the returned value for `df_1d`. (We will show how to access rows, columns, and elements soon.)

```python
>>> df_2d['Genus']
0       Homo
1        Pan
2    Gorilla
3      Pongo
Name: Genus, dtype: object
```

Comparing the `type` of the containers and the `dtype` and `dtypes` of the containers reveals that `df_1d` and `df_2d['Genus']` are in fact both `pandas.Series` with the same `dtype` (`'O'` for `object`).

```python
>>> type(df_1d)
<class 'pandas.core.series.Series'>
>>> type(df_2d)
<class 'pandas.core.frame.DataFrame'>
>>> type(df_2d['Genus'])
<class 'pandas.core.series.Series'>
>>> df_1d.dtype
dtype('O')
>>> df_2d.dtypes
Genus      object
Mass_kg     int64
dtype: object
>>> df_2d['Genus'].dtype
dtype('O')
```

Next, we'll explore how to access rows, columns, and elements from a dataframe. For this, we'll load a csv that contains information about 20 commonly used amino acids. By calling `.read_csv` while using the argument `index_col='code'`, our new `aa` data frame will label its rows according to the column named `code` (the single-letter character that represents each amino acid). 

```python
>>> aa = pd.read_csv('amino_acids.csv', index_col='code')
>>> aa.columns
Index(['name', 'abbr', 'mol_formula', 'mol_weight', 'hydrophob'], dtype='object')
>>> aa.index
Index(['A', 'R', 'N', 'D', 'C', 'E', 'Q', 'G', 'H', 'I', 'L', 'K', 'M', 'F',
       'P', 'S', 'T', 'W', 'Y', 'V'],
      dtype='object', name='code')
```

The safest way to extract rows, columns, and elements from a `pandas.DataFrame` is by using `.loc[a,b]` and `.iloc[a,b]` notation. This notation behaves similarly to that for `np.ndarray` from Numpy. The letter `a` (before the comma) is a placeholder for the subset of rows to extract from the dataframe, and `b` (after the comma) represents the subset of columns to extract. Using `.loc` uses the labeled location for each row/column, while `.iloc` uses the base-0 integer-indexed location.

For example, to extract the `panda.Series` row labeled `A` from `aa`:

```python
>>> aa.loc['A',:]
name           alanine
abbr               Ala
mol_formula    C3H7NO2
mol_weight        89.1
hydrophob           41
Name: A, dtype: object
```

To extract the `pandas.Series` column labeled `mol_weight` from `aa`:

```python
>>> aa.loc[:,'mol_weight']
code
A     89.10
R    174.20
N    132.12
D    133.11
C    121.16
E    147.13
Q    146.15
G     75.07
H    155.16
I    131.18
L    131.18
K    146.19
M    149.21
F    165.19
P    115.13
S    105.09
T    119.12
W    204.23
Y    181.19
V    117.15
Name: mol_weight, dtype: float64
```

There are many equivalent ways to access an element using the `.loc` and `.iloc`, either by visiting the element in the dataframe directly, or by extracting a `pandas.Series` first, then accessing an element in that series. This allows the programmer to interact with the dataframe in whatever way is most convenient for processing.

```python
>>> aa.loc['A','mol_weight']
89.1
>>> aa.iloc[0,3]
89.1
>>> aa.loc['A',:]['mol_weight']
89.1
>>> aa.loc[:,'mol_weight']['A']
89.1
>>> aa.iloc[0,:]['mol_weight']
89.1
>>> aa.iloc[:,3]['A']
89.1
>>> aa.loc['A',:][3]
89.1
```

Note that slice indexing can be used for label-based locations (`.loc`) and fro integer-based locations (`.iloc`; shown later).

```python
>>> aa.loc['A':'C','name':'abbr']
               name abbr
code
A           alanine  Ala
R          arginine  Arg
N        asparagine  Asn
D     aspartic acid  Asp
C          cysteine  Cys
```

Use lists of locations to extract non-contiguous subsets of rows and columns from the dataframe.

```python
>>> aa.loc[['A','R'],:]
          name abbr mol_formula  mol_weight  hydrophob
code
A      alanine  Ala     C3H7NO2        89.1         41
R     arginine  Arg   C6H14N4O2       174.2        -14
>>> aa.loc[['A','R'],['mol_weight','hydrophob']]
      mol_weight  hydrophob
code
A           89.1         41
R          174.2        -14
>>> aa.iloc[[0,1],:]
          name abbr mol_formula  mol_weight  hydrophob
code
A      alanine  Ala     C3H7NO2        89.1         41
R     arginine  Arg   C6H14N4O2       174.2        -14
>>> aa.iloc[[0,1],[3,4]]
      mol_weight  hydrophob
code
A           89.1         41
R          174.2        -14
>>> aa.iloc[0:2,3:5]
      mol_weight  hydrophob
code
A           89.1         41
R          174.2        -14
```

You can also construct series of boolean values from row/column data.

```python
>>> aa['mol_weight'] > 150
code
A    False
R     True
N    False
D    False
C    False
E    False
Q    False
G    False
H     True
I    False
L    False
K    False
M    False
F     True
P    False
S    False
T    False
W     True
Y     True
V    False
Name: mol_weight, dtype: bool
```

Boolean series can then be used to subset the dataframe. For example, the following command only displays rows whose `mol_weight` values are greater than 150.

```python
>>> aa[ aa['mol_weight'] > 150 ]
               name abbr mol_formula  mol_weight  hydrophob
code
R          arginine  Arg   C6H14N4O2      174.20        -14
H         histidine  His    C6H9N3O2      155.16        -31
F     phenylalanine  Phe    C9H11NO2      165.19         97
W        tryptophan  Trp  C11H12N2O2      204.23         97
Y          tyrosine  Tyr    C9H11NO3      181.19         63
```

The `.isin` method returns a boolean series that records which entries "match" within a set of targets. In this example, we want to locate only those rows that encode alanine (code `A`) and cysteine (code `C`):

```python
>>> codon = pd.read_csv('codons.csv')
>>> codon
   codon abbr code
0    AAA  Lys    K
1    AAC  Asn    N
2    AAG  Lys    K
3    AAT  Asn    N
4    ACA  Thr    T
..   ...  ...  ...
59   TGT  Cys    C
60   TTA  Leu    L
61   TTC  Phe    F
62   TTG  Leu    L
63   TTT  Phe    F

[64 rows x 3 columns]
>>> codon[ codon['code'].isin(['A','C']) ]
   codon abbr code
36   GCA  Ala    A
37   GCC  Ala    A
38   GCG  Ala    A
39   GCT  Ala    A
57   TGC  Cys    C
59   TGT  Cys    C
```

Data tables often need to be sorted for viewing or processing. Pandas dataframes can be sorted according to the location (index) for rows (`axis=0`) or columns (`axis=1`) using `.sort_index`. They can also be sorted according the the values of a given column using `.sort_values`.

```python
>>> aa.head(3)
            name abbr mol_formula  mol_weight  hydrophob
code
A        alanine  Ala     C3H7NO2       89.10         41
R       arginine  Arg   C6H14N4O2      174.20        -14
N     asparagine  Asn    C4H8N2O3      132.12        -28
>>> aa.sort_index(axis=0).head(3)
               name abbr mol_formula  mol_weight  hydrophob
code
A           alanine  Ala     C3H7NO2       89.10         41
C          cysteine  Cys    C3H7NO2S      121.16         49
D     aspartic acid  Asp     C4H7NO4      133.11        -55
>>> aa.sort_index(axis=0, ascending=False).head(3)
            name abbr mol_formula  mol_weight  hydrophob
code
Y       tyrosine  Tyr    C9H11NO3      181.19         63
W     tryptophan  Trp  C11H12N2O2      204.23         97
V         valine  Val    C5H11NO2      117.15         76
>>> aa.sort_values('mol_weight').head(3)
         name abbr mol_formula  mol_weight  hydrophob
code
G     glycine  Gly     C2H5NO2       75.07          0
A     alanine  Ala     C3H7NO2       89.10         41
S      serine  Ser     C3H7NO3      105.09         -5
>>> aa.sort_values('hydrophob').head(3)
               name abbr mol_formula  mol_weight  hydrophob
code
D     aspartic acid  Asp     C4H7NO4      133.11        -55
P           proline  Pro     C5H9NO2      115.13        -46
H         histidine  His    C6H9N3O2      155.16        -31
```

Especially with large data tables, it often helps to summarize the data to comprehend what information the table contains. We saw this earlier with the `.describe` method. Pandas offers a variety of other summary methods, which can be found in the [developer guide](https://pandas.pydata.org/docs/reference/frame.html).

For example, quantiles bin data such that some percent of the data are less than or equal to a quantile's value -- e.g. 20% of molecular weights are less than or equal to 117.7460.

```python
>>> aa.quantile([0.05, 0.20, 0.5, 0.80, 0.95])
      mol_weight  hydrophob
0.05     88.3985     -46.45
0.20    116.7460     -24.00
0.50    132.6150      10.50
0.80    157.1660      80.20
0.95    182.3420      99.05
```

Rank displays the order of values, from smallest to largest, with tied values receiving the average rank.

```python
>>> aa.loc[:,'mol_weight':'hydrophob'].rank()
      mol_weight  hydrophob
code
A            2.0       12.0
R           18.0        6.0
N           10.0        4.0
D           11.0        1.0
C            7.0       13.0
E           14.0       10.0
Q           12.0        7.0
G            1.0        9.0
H           16.0        3.0
I            8.5       19.0
L            8.5       20.0
K           13.0        5.0
M           15.0       15.0
F           17.0       17.5
P            4.0        2.0
S            3.0        8.0
T            6.0       11.0
W           20.0       17.5
Y           19.0       14.0
V            5.0       16.0
```

Pandas also allows you to apply custom functions to dataframes against either rows or columns.

```python
>>> df = pd.DataFrame(np.random.randn(3, 2),index=list('ABC'), columns=list('XY'))
>>> df
          X         Y
A  0.326329 -2.125083
B  0.936576 -1.519868
C -0.518834  1.306870
>>> df.apply(lambda x: x+10)
           X          Y
A  10.326329   7.874917
B  10.936576   8.480132
C   9.481166  11.306870
>>> df.apply(lambda x: sum(x), axis=0)
X    0.744071
Y   -2.338081
dtype: float64
>>> df.apply(lambda x: sum(x), axis=1)
A   -1.798753
B   -0.583292
C    0.788036
dtype: float64
```

Reshaping standard data tables into a "melted" format is easy in Pandas. Melted tables generally treat one (or sometimes more) variables as the identifying variable, then creates a separate row for each other variable and value associated with that identifying variable in the new melted table. For example, if we melt `aa` while using `abbr` as the identifying variable, each of the 20 amino acids has 4 entries (`name`, `mol_formula`, `mol_weight`, `hydrophob`) in a newly melted table with 80 rows and 3 columns. (This format is commonly used in data science packages, such as `dplyr` in the `tidyverse` from `R`).

```python
>>> aa.head(3)
            name abbr mol_formula  mol_weight  hydrophob
code
A        alanine  Ala     C3H7NO2       89.10         41
R       arginine  Arg   C6H14N4O2      174.20        -14
N     asparagine  Asn    C4H8N2O3      132.12        -28
>>> pd.melt(aa, id_vars='abbr')
   abbr   variable          value
0   Ala       name        alanine
1   Arg       name       arginine
2   Asn       name     asparagine
3   Asp       name  aspartic acid
4   Cys       name       cysteine
..  ...        ...            ...
75  Ser  hydrophob             -5
76  Thr  hydrophob             13
77  Trp  hydrophob             97
78  Tyr  hydrophob             63
79  Val  hydrophob             76

[80 rows x 3 columns]
```

Melted datasets can also be restored to a standard format using pivot tables. To appreciate this, first create a melted table:

```python
>>> df = pd.DataFrame({"A": ["foo", "foo", "foo", "foo", "foo",
...                          "bar", "bar", "bar", "bar"],
...                    "B": ["one", "one", "one", "two", "two",
...                          "one", "one", "two", "two"],
...                    "C": ["small", "large", "large", "small",
...                          "small", "large", "small", "small",
...                          "large"],
...                    "D": [1, 2, 2, 3, 3, 4, 5, 6, 7],
...                    "E": [2, 4, 5, 5, 6, 6, 8, 9, 9]})
>>> df
     A    B      C  D  E
0  foo  one  small  1  2
1  foo  one  large  2  4
2  foo  one  large  2  5
3  foo  two  small  3  5
4  foo  two  small  3  6
5  bar  one  large  4  6
6  bar  one  small  5  8
7  bar  two  small  6  9
8  bar  two  large  7  9
```

Then create a pivot table, where the values associated with `A` (`foo` and `bar`) and `C` (`small` and `large`) are used to index rows, and the values associated with `D` and `E` are summarized using different sets of aggregation functions (mean, min, max):

```python
>>> table = pd.pivot_table(df, values=['D', 'E'],
...                        index=['A','C'],
...                        aggfunc={'D': np.mean,
...                                 'E': [min, max, np.mean]})
>>> table
                  D    E
               mean  max      mean  min
A   C
bar large  5.500000  9.0  7.500000  6.0
    small  5.500000  9.0  8.500000  8.0
foo large  2.000000  5.0  4.500000  4.0
    small  2.333333  6.0  4.333333  2.0
```

Lastly, data tables that share values for a given dimension can be merged. For example, we can merge `aa` and `codon` using their shared abbreviated amino acid names (`abbr`) to construct a comprehensive table containing information about the genetic code and the properties of resulting translated amino acids

```python
>>> aa.head(3)
            name abbr mol_formula  mol_weight  hydrophob
code
A        alanine  Ala     C3H7NO2       89.10         41
R       arginine  Arg   C6H14N4O2      174.20        -14
N     asparagine  Asn    C4H8N2O3      132.12        -28
>>> codon.head(3)
  codon abbr code
0   AAA  Lys    K
1   AAC  Asn    N
2   AAG  Lys    K
>>> codon_aa = pd.merge(aa, codon, on='abbr')
>>> codon_aa
        name abbr mol_formula  mol_weight  hydrophob codon code
0    alanine  Ala     C3H7NO2       89.10         41   GCA    A
1    alanine  Ala     C3H7NO2       89.10         41   GCC    A
2    alanine  Ala     C3H7NO2       89.10         41   GCG    A
3    alanine  Ala     C3H7NO2       89.10         41   GCT    A
4   arginine  Arg   C6H14N4O2      174.20        -14   AGA    R
..       ...  ...         ...         ...        ...   ...  ...
56  tyrosine  Tyr    C9H11NO3      181.19         63   TAT    Y
57    valine  Val    C5H11NO2      117.15         76   GTA    V
58    valine  Val    C5H11NO2      117.15         76   GTC    V
59    valine  Val    C5H11NO2      117.15         76   GTG    V
60    valine  Val    C5H11NO2      117.15         76   GTT    V

[61 rows x 7 columns]
```

Once you have executed all of the above code through the Jupyter notebook, save and close the notebook, then commit and push the notebook to your GitHub classroom assignment repository. Also submit a log of your history (`history.txt`).
