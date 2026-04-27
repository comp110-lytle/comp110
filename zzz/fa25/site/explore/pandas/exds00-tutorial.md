---
title: Pandas Tutorial
author:
- Kyle Sorensen
page: explore
template: overview
---

## exds_00: Getting Started

### Introduction:
Now more than ever, data has a unique ability to describe the many facets of our reality. Thanks to relatively recent (and accelerating) advances in computing,those with proper motivation can use data to affect change in any realm they so choose, from ones more directly related to computer science such as machine learning to others with not so obvious connections such as biology and economics!

You have likely heard a lot of talk recently about *data science*, but what exactly is data science? A quick search gives this definition: "an inter-disciplinary field that uses scientific methods, processes, algorithms and systems to extract knowledge and insights from structured and unstructured data, and apply knowledge from data across a broad range of application domains". Now, this is a mouthful, but essentially, data science pulls from the best of computer science, statistics, and mathematics to **make data understandable and actionable**. This is the key, because what worth does data have if we can not interpret it and make decisions based on it?

### `pandas` and Data Science in Python:
Learning Python in this class has already given you a headstart in data science, since Python is incredibly well-equipped for handling large datasets with many specialized third-party libraries. The industry standard for this type of work is a library called `pandas`. There are other libraries that work well with data science in Python that we may explore later, but `pandas` is all you need for now! :)

Below, you will see the usual convention for importing pandas:

## Importing pandas
~~~ {.python .numberLines startFrom="1"}
import pandas as pd
~~~

Now, that was not so bad! :) but we have a ways to go...

### The End-all Be-all of `pandas`: the `DataFrame`
In `pandas`, the primary data type that you will work is known as a `DataFrame`. Those who have worked in R may know this by the same name, and those who have in the SAS programming lanaguage may know this as a data set! Here, you will see a declaration of a `DataFrame` in `pandas`:

~~~{.python .numberLines startFrom="1"}
# Setting up the dictionary with str keys and list[int] values
d: dict[str, list[int]] = {'col1': [1, 2], 'col2': [3, 4]}

# Creating the DataFrame from the above structure
df = pd.DataFrame(data=d)

# We do not have to use df.head() (more info to come) here because the DataFrame is quite small (this will not be true going forward)
print(df)
~~~
~~~plaintext
   col1  col2
0     1     3
1     2     4
~~~

You might have noticed something very interesting, a marked similarity between this declaration and something you have worked with before, perhaps in EX04! Full disclosure, this is entirely purposeful. EX04 was meant to help you understand the underlying functionality of a `DataFrame` in `pandas`! Many things work similarly in pandas to how you implemented them in EX04. But, more on that later!

### Importing Data with `pandas`
It stands to reason that, to work with data, we need data! In `pandas`, we can read in many kinds of files, but the most common for datasets is the csv or "comma-separated value" file. The dataset imported below contains information about some Pokemon! To view your data, you should use a command of the form `print(dataframe.head(n))`, where n is the number of top rows you wish to display. If left blank, this will default to 5. 

Additionally, if we choose to modify the `DataFrame`, we can actually `write` to a new csv that will include the modifications using a similar command to the one you will see below. Do NOT worry if the code for modification seems foreign, we will get to that in time, but the gist of it is that we are ordering or sorting the pokemon `DataFrame` by ascending values of HP! It is worth noting that we could write back to the original csv, but in some cases it may be worth preserving the original dataset.

~~~{.python .numberLines startFrom="1"}
# Reading in the CSV
pokemon = pd.read_csv("pokemon.csv")

# Sorting the values rows and resetting their indices
pokemon_sorted = pokemon.sort_values("HP",ascending=True)
pokemon_sorted = pokemon_sorted.reset_index(drop=True)

# Writing the new DataFrame to the new csv
pokemon_sorted.to_csv("pokemon_new.csv",index=False)
~~~

### Summarizing the data in your `DataFrame`
After we load the data, the structure of our `DataFrame` may not be immediately obvious, and usually using a command such as `df.head()` works totally fine. But, sometimes we need a bit more information to understand our data before we attempt to analyze it. See the code below for some commands that may be useful in interpreting the structure of your `DataFrame`.

~~~{.python .numberLines startFrom="1"}
# Getting the number of rows in your DataFrame
print(len(pokemon))

# Getting the dimensions of your DataFrame (rows, columns)
pokemon.shape

# Getting a list of the column names in your DataFrame
pokemon.columns

# Provides the most comprehensive overview of the columns in your DataFrame
# also provides the name, count of non-null values and datatype of each column
# as well as some information about memory usage!
pokemon.info()
~~~
~~~plaintext
800
<class 'pandas.core.frame.DataFrame'>
RangeIndex: 800 entries, 0 to 799
Data columns (total 14 columns):
 #   Column      Non-Null Count  Dtype 
---  ------      --------------  ----- 
 0   Unnamed: 0  800 non-null    int64 
 1   #           800 non-null    int64 
 2   Name        800 non-null    object
 3   Type 1      800 non-null    object
 4   Type 2      414 non-null    object
 5   Total       800 non-null    int64 
 6   HP          800 non-null    int64 
 7   Attack      800 non-null    int64 
 8   Defense     800 non-null    int64 
 9   Sp. Atk     800 non-null    int64 
 10  Sp. Def     800 non-null    int64 
 11  Speed       800 non-null    int64 
 12  Generation  800 non-null    int64 
 13  Legendary   800 non-null    bool  
dtypes: bool(1), int64(10), object(3)
memory usage: 82.2+ KB
~~~

### Subsetting by variable (column) in a `DataFrame`
Of course, having the csv loaded is great, but there is not much use in a `DataFrame` if we can not actually get to the data and perform meaningful analyses. So, we will start by selecting columns! In `pandas`, there several ways to do this. See the code below and read the comments for insight into the action of each command and note the addition of another library called `numpy`, which will help us perform some basic analysis on the data we collect. 

Something of note is that the very last command uses something called a *regular expression*. We do not cover this topic in COMP 110, but they are quite useful and something you will learn more about in later COMP courses if you so choose to take them! :)

~~~{.python .numberLines startFrom="1"}
# Importing numpy
import numpy as np

# Selecting a column using . notation and find the mean HP of the pokemon in our dataset
hp = pokemon.HP
print(np.mean(hp))

# Selecting a column using subscription notation (should be more familiar), also finding the standard deviation using numpy
defense = pokemon["Defense"]
print(np.std(defense))

# Selecting multiple columns, can be useful to "declutter" your data or more directly compare columns
narrowed_pokemon = pokemon[["Name","HP","Attack","Defense"]]
print(narrowed_pokemon.head())

# Selecting columns in a range using .loc() and columns at certian indices using .iloc()
names_and_types = pokemon.loc[:,'Name':'Type 2']
narrowed_pokemon = pokemon.iloc[:,[2,6,7,8]] # note that this achieves the same thing as the subscription notation above!
print(names_and_types.head())
print(narrowed_pokemon.head())

# Filtering columns using .filter(), getting only the columns that start with T
types_and_total = pokemon.filter(regex="^T")
print(types_and_total.head())

# Selecting columns based on data type, only columns of a numeric types
numbers_only = pokemon.select_dtypes(include='number')
print(numbers_only.head())
~~~

~~~plaintext
69.25875
31.164004777146342
                    Name  HP  Attack  Defense
0              Bulbasaur  45      49       49
1                Ivysaur  60      62       63
2               Venusaur  80      82       83
3  VenusaurMega Venusaur  80     100      123
4             Charmander  39      52       43
                    Name Type 1  Type 2
0              Bulbasaur  Grass  Poison
1                Ivysaur  Grass  Poison
2               Venusaur  Grass  Poison
3  VenusaurMega Venusaur  Grass  Poison
4             Charmander   Fire     NaN
                    Name  HP  Attack  Defense
0              Bulbasaur  45      49       49
1                Ivysaur  60      62       63
2               Venusaur  80      82       83
3  VenusaurMega Venusaur  80     100      123
4             Charmander  39      52       43
  Type 1  Type 2  Total
0  Grass  Poison    318
1  Grass  Poison    405
2  Grass  Poison    525
3  Grass  Poison    625
4   Fire     NaN    309
   Unnamed: 0  #  Total  HP  Attack  Defense  Sp. Atk  Sp. Def  Speed  \
0           0  1    318  45      49       49       65       65     45   
1           1  2    405  60      62       63       80       80     60   
2           2  3    525  80      82       83      100      100     80   
3           3  3    625  80     100      123      122      120     80   
4           4  4    309  39      52       43       60       50     65   

   Generation  
0           1  
1           1  
2           1  
3           1  
4           1  
~~~

### Subsetting by observation (row) in a `DataFrame`
Next, we will focus on how to subset data by row. This is where Boolean expressions come into play since we typically want the rows we filter to meet a specific requirement such as one of its values falling within a range of numbers or being equal to some particular string. In this section, you will see how to generate a *sample* from larger dataset. However, pay particular attention to the use of Boolean conditions to filter rows of the `DataFrame`, as this is the most common and readable method in `pandas`.

~~~{.python .numberLines startFrom="1"}
# Using .head() and tail() to select the first and last 'n' rows respectively (n defaults to 5)
first_5 = pokemon.head(5)
last_5 = pokemon.tail(5)
print(first_5)
print(last_5)

# Filtering rows for a specific Boolean condition, all Pokemon with HP greater than 100
healthy_pokemon = pokemon[pokemon.HP > 100]
print(healthy_pokemon.head())

# Dropping duplicate observations from a DataFrame
no_repeats = pokemon.drop_duplicates()
print(no_repeats.head())

# Randomly sample (select) (1-frac)100% of the rows in the DataFrame
sample_frac = pokemon.sample(frac=0.25)
print(sample_frac.head())

# Randomly sample (select) n of the rows in the DataFrame
sample_n = pokemon.sample(n=10)
print(sample_n)
~~~

~~~plaintext
   Unnamed: 0  #                   Name Type 1  Type 2  Total  HP  Attack  \
0           0  1              Bulbasaur  Grass  Poison    318  45      49   
1           1  2                Ivysaur  Grass  Poison    405  60      62   
2           2  3               Venusaur  Grass  Poison    525  80      82   
3           3  3  VenusaurMega Venusaur  Grass  Poison    625  80     100   
4           4  4             Charmander   Fire     NaN    309  39      52   

   Defense  Sp. Atk  Sp. Def  Speed  Generation  Legendary  
0       49       65       65     45           1      False  
1       63       80       80     60           1      False  
2       83      100      100     80           1      False  
3      123      122      120     80           1      False  
4       43       60       50     65           1      False  
     Unnamed: 0    #                 Name   Type 1 Type 2  Total  HP  Attack  \
795         795  719              Diancie     Rock  Fairy    600  50     100   
796         796  719  DiancieMega Diancie     Rock  Fairy    700  50     160   
797         797  720  HoopaHoopa Confined  Psychic  Ghost    600  80     110   
798         798  720   HoopaHoopa Unbound  Psychic   Dark    680  80     160   
799         799  721            Volcanion     Fire  Water    600  80     110   

     Defense  Sp. Atk  Sp. Def  Speed  Generation  Legendary  
795      150      100      150     50           6       True  
796      110      160      110    110           6       True  
797       60      150      130     70           6       True  
798       60      170      130     80           6       True  
799      120      130       90     70           6       True  
     Unnamed: 0    #        Name  Type 1 Type 2  Total   HP  Attack  Defense  \
44           44   39  Jigglypuff  Normal  Fairy    270  115      45       20   
45           45   40  Wigglytuff  Normal  Fairy    435  140      70       45   
96           96   89         Muk  Poison    NaN    500  105     105       75   
120         120  112      Rhydon  Ground   Rock    485  105     130      120   
121         121  113     Chansey  Normal    NaN    450  250       5        5   

     Sp. Atk  Sp. Def  Speed  Generation  Legendary  
44        45       25     20           1      False  
45        85       50     45           1      False  
96        65      100     50           1      False  
120       45       45     40           1      False  
121       35      105     50           1      False  
   Unnamed: 0  #                   Name Type 1  Type 2  Total  HP  Attack  \
0           0  1              Bulbasaur  Grass  Poison    318  45      49   
1           1  2                Ivysaur  Grass  Poison    405  60      62   
2           2  3               Venusaur  Grass  Poison    525  80      82   
3           3  3  VenusaurMega Venusaur  Grass  Poison    625  80     100   
4           4  4             Charmander   Fire     NaN    309  39      52   

   Defense  Sp. Atk  Sp. Def  Speed  Generation  Legendary  
0       49       65       65     45           1      False  
1       63       80       80     60           1      False  
2       83      100      100     80           1      False  
3      123      122      120     80           1      False  
4       43       60       50     65           1      False  
     Unnamed: 0    #        Name  Type 1    Type 2  Total  HP  Attack  \
720         720  652  Chesnaught   Grass  Fighting    530  88     107   
249         249  230     Kingdra   Water    Dragon    540  75      95   
160         160  148   Dragonair  Dragon       NaN    420  61      84   
659         659  598  Ferrothorn   Grass     Steel    489  74      94   
461         461  414      Mothim     Bug    Flying    424  70      94   

     Defense  Sp. Atk  Sp. Def  Speed  Generation  Legendary  
720      122       74       75     64           6      False  
249       95       95       95     85           2      False  
160       65       70       70     70           1      False  
659      131       54      116     20           5      False  
461       50       94       50     66           4      False  
     Unnamed: 0    #                 Name  Type 1    Type 2  Total   HP  \
529         529  477             Dusknoir   Ghost       NaN    525   45   
585         585  526             Gigalith    Rock       NaN    515   85   
787         787  711  GourgeistSuper Size   Ghost     Grass    494   85   
777         777  707               Klefki   Steel     Fairy    470   57   
363         363  332             Cacturne   Grass      Dark    475   70   
398         398  363               Spheal     Ice     Water    290   70   
313         313  289              Slaking  Normal       NaN    670  150   
401         401  366             Clamperl   Water       NaN    345   35   
277         277  256            Combusken    Fire  Fighting    405   60   
254         254  235             Smeargle  Normal       NaN    250   55   

     Attack  Defense  Sp. Atk  Sp. Def  Speed  Generation  Legendary  
529     100      135       65      135     45           4      False  
585     135      130       60       80     25           5      False  
787     100      122       58       75     54           6      False  
777      80       91       80       87     75           6      False  
363     115       60      115       60     55           3      False  
398      40       50       55       50     25           3      False  
313     160      100       95       65    100           3      False  
401      64       85       74       55     32           3      False  
277      85       60       85       60     55           3      False  
254      20       35       20       45     75           2      False  
~~~

### Conclusion of Tutorial:
To wrap things up, let's recall what we have learned so far:

* importing `pandas`
* creating a `DataFrame`, underlying structure
* reading from and writing to .csv files
* observing the structure of a specific `DataFrame`
* selecting data by column and by row
* some basic analysis using `numpy`

Congratulations on taking the first step in your data science journey. If you so choose, you can try out the Data Science Challenge in this folder which will push you to apply the skills you learned in this tutorial and do some of your own analysis on a dataset! Great work and good luck to all of you future data scientists! :)
