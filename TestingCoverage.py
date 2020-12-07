
# Importing required libraries

import pandas as pd
import matplotlib.pyplot as plt
import os
import seaborn as sns
import numpy as np
import datetime
from datetime import date
from dateutil.relativedelta import relativedelta


# Changing the working directory
os.chdir('D:/Downloads/')


# This function generates a series to denote age group distribution
def age_distribution(row, colname) -> pd.core.series.Series:
    """
        This function is used to return a pandas series that denotes the race percentage value
        of the different races present in NYC.

        Age data retrieved from: https://www.statista.com/statistics/911456/new-york-population-share-age-group/
        Total NYC population (2019) = 8,323,340
        This function was retrieved from one of the project's from the Spring 2020 semester.
        Link: https://github.com/rahulrohri/final_project_2020Sp

        Age Groups and their respective percentages:
        <18 : 23.2%
        18-24 : 6.5%
        25-44 : 27.2%
        45-64 : 26.1%
        65+ : 17%

        :param row: Denotes that the operation has to be performed across rows
        :param colname: Column name on which operation has to be performed
        :return : Numeric value if a row match is found from specified values in the function

        >>> df_dummy = pd.DataFrame({'Age':  ['25-44', '18-24', '45-64', '<18', '65+']})
        >>> df_dummy.apply(lambda row: age_distribution(row,'Age'), axis=1)
        0    0.272
        1    0.065
        2    0.261
        3    0.232
        4    0.170
        dtype: float64

        """

    if row[colname] == '25-44':
        return 0.272
    if row[colname] == '18-24':
        return 0.065
    if row[colname] == '45-64':
        return 0.261
    if row[colname] == '<18':
        return 0.232
    if row[colname] == '65+':
        return 0.17


# This function adds the age percentage column to a dataframe that has the 'AGE_GROUP' column
def age_pct_col(df):
    """
    This function allows us to add the age percentage column to an existing
    dataframe that contains the 'AGE_GROUP' column. Addition of this new column
    is an intermediate step to allow normalizing the values. Within this function
    another function - age_distribution is used.

    :param df: Dataframe to which the age percentage column has to be appended
    :return: Dataframe with the added column - age percentage distribution

    >>> df = pd.DataFrame({'AGE_GROUP': ['25-44', '18-24', '45-64', '<18', '65+']})
    >>> age_pct_col(df)
      AGE_GROUP  POP_BY_AGE_PCT
    0     25-44           0.272
    1     18-24           0.065
    2     45-64           0.261
    3       <18           0.232
    4       65+           0.170
    """
    age_pct = pd.DataFrame(df.apply(lambda row: age_distribution(row, 'AGE_GROUP'), axis=1))
    age_pct.rename(columns={0: 'POP_BY_AGE_PCT'}, inplace=True)
    df = pd.concat([df, age_pct], axis=1)
    return df


# This function allows selection of specific/required column(s) from a dataframe
def select_columns(df, *args):
    """

    This function is used to select particular columns from dataframes.
    The datasets loaded initially consist of multiple columns, all of
    which would not be required for analysis for one hypothesis. The
    user may use this function to extract relevant columns.

    :param df: The dataframe from which the columns are to be extracted
    :param args: Name of columns which can have to be extracted, pass as strings
    :return: A new dataframe consisting of the extracted columns

    >>> dummy_df = pd.DataFrame({'col1': [1, 2], 'col2': [3, 4]})
    >>> select_columns(dummy_df, 'col1')
       col1
    0     1
    1     2


    """

    new_df = df[[*args]]
    new_df = new_df.dropna()
    return new_df


# This function helps to perform preliminary data exploration
def preliminary_analysis(df):
    """

    This functions allows us to determine the shape of the dataset i.e. the number
    of rows and columns. It also helps to determine the number of null counts for
    a particular column within the dataset. Lastly, it prints the first 5 rows of
    the dataset to give an idea about the structure.

    :param df:  The dataframe that has to be analyzed

    >>> dummy_df = pd.DataFrame({'col1': [1, 2, 3, 4, 5], 'col2': [6, 7, 8, 9, 10]})
    >>> preliminary_analysis(dummy_df)
    *** Rows and Columns in the Dataframe ***
    Number of Instances (rows) : 5
    Number of Columns :  2
    *** Column Names, Non-Null Count and Column Data Types***
    <class 'pandas.core.frame.DataFrame'>
    RangeIndex: 5 entries, 0 to 4
    Data columns (total 2 columns):
     #   Column  Non-Null Count  Dtype
    ---  ------  --------------  -----
     0   col1    5 non-null      int64
     1   col2    5 non-null      int64
    dtypes: int64(2)
    memory usage: 208.0 bytes
    None
    *** First 5 rows to give an idea about the dataset ***
    <BLANKLINE>
        col1  col2
    0     1     6
    1     2     7
    2     3     8
    3     4     9
    4     5    10

    """
    rows, columns = df.shape
    print('*** Rows and Columns in the Dataframe ***')
    print('Number of Instances (rows) :', rows)
    print('Number of Columns : ', columns)

    print('*** Column Names, Non-Null Count and Column Data Types***')
    print(df.info())

    print('*** First 5 rows to give an idea about the dataset ***')
    print('\n', df.head())


def race_percentage(row, colname):
    """
    This function is used to return a pandas series that denotes the race percentage value
    of the different races present in NYC.

    Population data retrieved from: https://worldpopulationreview.com/us-cities/new-york-city-ny-population
    Total NYC population (2019) = 8,323,340
    This function was retrieved from one of the project's from the Spring 2020 semester.
    Link: https://github.com/rahulrohri/final_project_2020Sp

    :param row: Denotes that the operation has to be performed across rows
    :param colname: Column name on which operation has to be performed
    :return : Numeric value if a row match is found from specified values in the function

    >>> df_dummy = pd.DataFrame({'Race':  ['AMERICAN INDIAN/ALASKAN NATIVE', 'ASIAN / PACIFIC ISLANDER', 'BLACK', 'BLACK HISPANIC', 'WHITE', 'WHITE HISPANIC', 'UNKNOWN', '(null)']})
    >>> df_dummy.apply(lambda row: race_percentage(row,'Race'), axis=1)
    0    0.0043
    1    0.1400
    2    0.2195
    3    0.0233
    4    0.3214
    5    0.1053
    6    0.1862
    7    0.1862
    dtype: float64

    """

    if row[colname] == 'AMERICAN INDIAN/ALASKAN NATIVE':
        return 0.0043
    if row[colname] == 'ASIAN / PACIFIC ISLANDER':
        return 0.14
    if row[colname] == 'BLACK':
        return 0.2195
    if row[colname] == 'BLACK HISPANIC':
        return 0.0233
    if row[colname] == 'WHITE':
        return 0.3214
    if row[colname] == 'WHITE HISPANIC':
        return 0.1053
    if row[colname] == '(null)':
        return 0.1862
    if row[colname] == 'UNKNOWN':
        return 0.1862


def race_pct_col(df, col):
    """

    This function allows us to add the racial percentage column to an existing
    dataframe that contains the race column. Addition of this new column
    is an intermediate step to allow normalizing the values. Within this function
    another function - race_percentage is used.

    :param df: Dataframe to which the racial percentage column has to be appended
    :param col: Column used for calculating the race percentage
    :return: Dataframe with the added column - racial percentage distribution

    >>> df = pd.DataFrame({'col1': [1, 2, 3, 4, 5, 6, 7, 8], 'SUSPECT_RACE_DESCRIPTION': ['AMERICAN INDIAN/ALASKAN NATIVE', 'ASIAN / PACIFIC ISLANDER', 'BLACK', 'BLACK HISPANIC', 'WHITE', 'WHITE HISPANIC', '(null)', 'UNKNOWN']})
    >>> race_pct_col(df)
       col1        SUSPECT_RACE_DESCRIPTION  POP_BY_RACE_PCT
    0     1  AMERICAN INDIAN/ALASKAN NATIVE           0.0043
    1     2        ASIAN / PACIFIC ISLANDER           0.1400
    2     3                           BLACK           0.2195
    3     4                  BLACK HISPANIC           0.0233
    4     5                           WHITE           0.3214
    5     6                  WHITE HISPANIC           0.1053
    6     7                          (null)           0.1862
    7     8                         UNKNOWN           0.1862


    """
    race_pct = pd.DataFrame(df.apply(lambda row: race_percentage(row, col), axis=1))
    race_pct.rename(columns={0: 'POP_BY_RACE_PCT'}, inplace=True)
    df = pd.concat([df, race_pct], axis=1)
    return df


# This function allows grouping the dataframe based on same values in particular column(s). This helps to determine
# the count of the values through the aforementioned columns.
def grouping_for_count(df, col_to_groupby1, col_to_groupby2, col_for_count):
    """
    This function allows grouping the dataframe based on same values in particular column(s). This helps to determine
    the count of the values through the aforementioned columns.

    :param df: The dataframe on which the pd.groupby() function will be applied
    :param col_to_groupby1: The first column by which the grouping will be done
    :param col_to_groupby2: The second column by which the grouping will be done
    :param col_for_count: Column whose count values are to be determined
    :return: The grouped dataframe is returned with the index being reset and appropriate column names

    >>> dummy_df = pd.DataFrame({'AGE_GROUP': ['25-44', '18-24', '45-64', '<18', '65+', '65+'], 'POP_BY_AGE_PCT': [0.272, 0.065, 0.261, 0.232, 0.170, 0.170]})
    >>> grouping_for_count(dummy_df, 'AGE_GROUP', 'POP_BY_AGE_PCT', 'AGE_GROUP')
      AGE_GROUP  POP_BY_AGE_PCT  COUNT
    0     18-24           0.065      1
    1     25-44           0.272      1
    2     45-64           0.261      1
    3       65+           0.170      2
    4       <18           0.232      1

    """
    grouped_df = df.groupby([col_to_groupby1, col_to_groupby2])[col_for_count].count()
    grouped_df = pd.DataFrame(grouped_df)
    grouped_df.rename(columns={col_for_count: 'COUNT'}, inplace=True)
    grouped_df = grouped_df.reset_index()
    return grouped_df


# This function helps to normalize the values in the dataset to supplement appropriate analysis. Normalizing
# helps to scale the values to the entire population. Without normalization, a highly inaccurate analysis would be presented
def normalized_values(df, count_values, pct_dist_values):
    """

    This function helps to normalize the values in the dataset to supplement appropriate analysis. Normalizing
    helps to scale the values to the entire population. Without normalization, a highly inaccurate analysis would be presented

    :param df: The dataframe to which the normalized values must be added
    :param count_values: The count column which is the numerator for normalizing
    :param pct_dist_values: The percentage distribution within total population column which is the denominator
    :return: Returns the dataframe consisting of normalized values in the new 'NORM_VALUES' column

    >>> dummy_df = pd.DataFrame({'COUNT': [750822, 356689, 25012, 45899, 12221], 'POP_BY_AGE_PCT': [0.272, 0.065, 0.261, 0.232, 0.170]})
    >>> normalized_values(dummy_df, 'COUNT', 'POP_BY_AGE_PCT')
        COUNT  POP_BY_AGE_PCT  NORM_VALUES
    0  750822           0.272      2760375
    1  356689           0.065      5487523
    2   25012           0.261        95831
    3   45899           0.232       197840
    4   12221           0.170        71888
    """
    df['NORM_VALUES'] = (df[count_values] / df[pct_dist_values]).astype('int')
    return df


# This function helps to transform the normalized values to a ratio/proportion. This helps to conclude the analysis and
# thus, accept/reject the hypothesis
def proportional_values(df):
    """

    This function helps to transform the normalized values to a ratio/proportion. This helps to conclude the analysis and
    thus, accept/reject the hypothesis

    :param df: The dataframe to which the proportional values must be added
    :return: Returns the dataframe consisting of proportional values in the new 'PROP_VALUES' column

    >>> dummy_df = pd.DataFrame({'NORM_VALUES': [750822, 356689, 25012, 45899, 12221]})
    >>> proportional_values(dummy_df)
       NORM_VALUES  PROP_VALUES
    0       750822        63.06
    1       356689        29.96
    2        25012         2.10
    3        45899         3.85
    4        12221         1.03
    """
    df['PROP_VALUES'] = ((df['NORM_VALUES'] / df['NORM_VALUES'].sum()) * 100).round(2)
    return df


# Creating a function to return the sex percentage value in NYC
def sex_distribution(row, colname) -> pd.core.series.Series:
    # Population data retrieved from: https://worldpopulationreview.com/us-cities/new-york-city-ny-population

    # Total NYC population = 8,323,340

    # Credit to Rahul + Megha (Link their github notebook)

    #     """
    #     This function is used to return a pandas series that has the sex percentage value of all the sexes present in NYC.

    #     :param row: denotes that the operation has to be performed across rows
    #     :param colname: Column name on which operation has to be done
    #     :return : a specific numeric value if a row match is found
    #     >>> data_dummy = {'Sex':  ['MALE','FEMALE'],'Offense': ['FRAUDS', 'FRAUDS'],'Comp_no':[1,2]}
    #     >>> df_dummy = pd.DataFrame (data_dummy, columns = ['Sex','Offense','Comp_no'])
    #     >>> df_dummy.apply (lambda row: sex_percentage(row,'Sex'), axis=1)
    #     0    0.4767
    #     1    0.5233
    #     dtype: float64

    #     """

    if row[colname] == 'MALE':
        return 0.4767
    if row[colname] == 'FEMALE':
        return 0.5233


# This function adds the age percentage column to a dataframe that has the 'AGE_GROUP' column
def sex_pct_col(df, col):
    """
    This function allows us to add the sex percentage column to an existing
    dataframe that contains the sex column. Addition of this new column
    is an intermediate step to allow normalizing the values. Within this function
    another function - sex_distribution is used.

    :param df: Dataframe to which the sex percentage column has to be appended
    :param col: Column used for calculating the sex percentage
    :return: Dataframe with the added column - sex percentage distribution

    >>> df = pd.DataFrame({'SEX': ['MALE', 'FEMALE', 'FEMALE']})
    >>> sex_pct_col(df)
            SEX  POP_BY_SEX_PCT
    0      MALE          0.4767
    1    FEMALE          0.5233
    2    FEMALE          0.5233
    """
    sex_pct = pd.DataFrame(df.apply(lambda row: sex_distribution(row, col), axis=1))
    sex_pct.rename(columns={0: 'POP_BY_SEX_PCT'}, inplace=True)
    df = pd.concat([df, sex_pct], axis=1)
    return df



# Hypothesis 1

## Majority of the crimes are commited by individuals in the age-group of 25-44


# Reading the dataset 'NYPD_Arrests_Data_2019.csv' into a dataframe
arrests_2019 = pd.read_csv('NYPD_Arrests_Data_2019.csv')


# Performing Preliminary Exploration
arrests_2019


# Checking count of the age groups in the dataset
arrests_2019.AGE_GROUP.value_counts()

# Selecting only the AGE_GROUP column from the dataset for this hypothesis
age_df = select_columns(arrests_2019, 'AGE_GROUP')

age_df


# Using the age_pct_col() function to determine what percentage of the population the age groups represent

age_group_pct = age_pct_col(age_df)

age_group_pct


# Using the grouping_for_count() function to create a new dataframe 'age_grouped_df' which consists of the count
# of the age groups

age_grouped_df = grouping_for_count(age_group_pct, col_to_groupby1='AGE_GROUP', col_to_groupby2='POP_BY_AGE_PCT',
                                    col_for_count='AGE_GROUP')

age_grouped_df


# Using the normalized_values() function to generate normalized value for the age_grouped_df

normalized_values(age_grouped_df, 'COUNT', 'POP_BY_AGE_PCT')


# Using the proportional_values() function on age_grouped_df to determine ratios

proportional_values(age_grouped_df)


# Creating a plot to visualize the distribution of data (normalized values)

fig, ax = plt.subplots(1,1, figsize = (15,9))

x = age_grouped_df['AGE_GROUP']
y = age_grouped_df['NORM_VALUES']

ax.bar(x, y)
ax.set_title('Hypothesis 1 - [Majority of the crimes are commited by individuals in the age-group of 25-44]')
plt.xlabel('Age Group')
plt.ylabel('Normalized Values')
plt.show()


# Creating a plot to visualize the distribution of data by proportional analysis (proportional values)

fig, ax = plt.subplots(1,1, figsize = (15,9))

x = age_grouped_df['AGE_GROUP']
y = age_grouped_df['PROP_VALUES']

ax.bar(x, y)
ax.set_title('Hypothesis 1 - [Majority of the crimes are commited by individuals in the age-group of 25-44]')
plt.xlabel('Age Group')
plt.ylabel('Proportional Values')
plt.show()

# A better representation of the above graph would be a pie chart.
# Creating a pie-chart to conclude our analysis for this hypothesis. A pie-chart is a better representation for
# proportion of a whole

labels = age_grouped_df['AGE_GROUP']
sizes = age_grouped_df['PROP_VALUES']
explode = (0.1, 0.1, 0.1, 0.2, 0.3)

fig1, ax1 = plt.subplots(figsize=(15, 9))

wedges, texts, autotexts = ax1.pie(sizes, explode=explode, labels=labels, autopct='%1.1f%%',
                                   shadow=True, startangle=90)

ax1.axis('equal')

ax1.legend(wedges, labels,
           title="Age Groups",
           loc="center left")

plt.setp(autotexts, size=15, weight="bold")
ax1.set_title("Hypothesis 1 - [Majority of the crimes are commited by individuals in the age-group of 25-44]\n")

plt.show()


# Hypothesis 2

## Males are more likely to be frisked and arrested than females


### Frisking Data


# Reading the frisking data

stop_question_frisk = pd.read_excel('sqf-2019.xlsx')


# Preliminary analysis for stop_question_frisk data

preliminary_analysis(stop_question_frisk)


# Identifying frisking distribution of individuals by sex

stop_question_frisk.SUSPECT_SEX.value_counts()


# Creating a copy of the data

sqf = stop_question_frisk.copy()


# Selecting only the required columns from the sqf dataset for this hypothesis

sqf_frisk = sqf[sqf['FRISKED_FLAG'] == 'Y']
sqf_df = select_columns(sqf_frisk, 'SUSPECT_SEX')
sqf_df


# Using the sex_pct_col() function to determine what percentage of the population the sex groups represent in sqf dataset

sqf_sex_group_pct = sex_pct_col(sqf_df, 'SUSPECT_SEX')

sqf_sex_group_pct


# Using the grouping_for_count() function to create a new dataframe 'sqf_sex_grouped_df' which consists of the count
# of the sex groups

sqf_sex_grouped_df = grouping_for_count(sqf_sex_group_pct, col_to_groupby1='SUSPECT_SEX', col_to_groupby2='POP_BY_SEX_PCT',
                                    col_for_count='SUSPECT_SEX')

sqf_sex_grouped_df


# Using the normalized_values() function to generate normalized value for the sqf_sex_grouped_df

normalized_values(sqf_sex_grouped_df, 'COUNT', 'POP_BY_SEX_PCT')



# Using the proportional_values() function on sqf_sex_grouped_df to determine ratios

proportional_values(sqf_sex_grouped_df)


# Creating a plot to visualize the distribution of sqf data (normalized values)

fig, ax = plt.subplots(1,1, figsize = (15,9))

x = sqf_sex_grouped_df['SUSPECT_SEX']
y = sqf_sex_grouped_df['NORM_VALUES']

ax.bar(x, y)
ax.set_title('Hypothesis 2 - [Males are more likely to be frisked than females]')
plt.xlabel('Sex')
plt.ylabel('Normalized Values')
plt.show()


# Creating a plot to visualize the distribution of sqf data by proportional analysis (proportional values)

fig, ax = plt.subplots(1,1, figsize = (15,9))

x = sqf_sex_grouped_df['SUSPECT_SEX']
y = sqf_sex_grouped_df['PROP_VALUES']

ax.bar(x, y)
ax.set_title('Hypothesis 2 - [Males are more likely to be frisked than females]')
plt.xlabel('Sex')
plt.ylabel('Proportional Values')
plt.show()

# A better representation of the above graph would be a pie chart.
# Creating a pie-chart to conclude our analysis for on sqf data. A pie-chart is a better representation for
# proportion of a whole

labels = sqf_sex_grouped_df['SUSPECT_SEX']
sizes = sqf_sex_grouped_df['PROP_VALUES']
explode = (0.1, 0.2)

fig1, ax1 = plt.subplots(figsize=(15, 9))

wedges, texts, autotexts = ax1.pie(sizes, explode=explode, labels=labels, autopct='%1.1f%%',
                                   shadow=True, startangle=90)

ax1.axis('equal')

ax1.legend(wedges, labels,
           title="Sex",
           loc="center left")

plt.setp(autotexts, size=15, weight="bold")
ax1.set_title("Hypothesis 2 - [Males are more likely to be frisked than females]\n")

plt.show()


# Reading the arresting data

arrest = pd.read_csv('NYPD_Arrests_Data_2019.csv')


# Preliminary analysis for arrest data

preliminary_analysis(arrest)


# Identifying arrest distribution of individuals by sex

arrest.PERP_SEX.value_counts()


# Creating a copy of the data

arr = arrest.copy()


# Changing the value of 'M' to 'MALE' and 'F' to 'FEMALE' in 'PERP_SEX' column in the arrest data

arr["PERP_SEX"].replace({"M": "MALE", "F": "FEMALE"}, inplace=True)


# Selecting only the required columns from the arrest dataset for this hypothesis

arr_df = select_columns(arr, 'PERP_SEX')
arr_df


# Using the sex_pct_col() function to determine what percentage of the population the sex groups represent in arrest dataset

arr_sex_group_pct = sex_pct_col(arr_df, 'PERP_SEX')

arr_sex_group_pct


# Using the grouping_for_count() function to create a new dataframe 'arr_sex_grouped_df' which consists of the count
# of the sex groups

arr_sex_grouped_df = grouping_for_count(arr_sex_group_pct, col_to_groupby1='PERP_SEX', col_to_groupby2='POP_BY_SEX_PCT',
                                    col_for_count='PERP_SEX')

arr_sex_grouped_df

# Using the normalized_values() function to generate normalized value for the arr_sex_grouped_df

normalized_values(arr_sex_grouped_df, 'COUNT', 'POP_BY_SEX_PCT')

# %%

# Using the proportional_values() function on arr_sex_grouped_df to determine ratios

proportional_values(arr_sex_grouped_df)

# %%

# Creating a plot to visualize the distribution of arrest data (normalized values)

fig, ax = plt.subplots(1, 1, figsize=(15, 9))

x = arr_sex_grouped_df['PERP_SEX']
y = arr_sex_grouped_df['NORM_VALUES']

ax.bar(x, y)
ax.set_title('Hypothesis 2 - [Males are more likely to be arrested than females]')
plt.xlabel('Sex')
plt.ylabel('Normalized Values')
plt.show()

# %%

# Creating a plot to visualize the distribution of arrest data by proportional analysis (proportional values)

fig, ax = plt.subplots(1, 1, figsize=(15, 9))

x = arr_sex_grouped_df['PERP_SEX']
y = arr_sex_grouped_df['PROP_VALUES']

ax.bar(x, y)
ax.set_title('Hypothesis 2 - [Males are more likely to be arrested than females]')
plt.xlabel('Sex')
plt.ylabel('Proportional Values')
plt.show()

# %%

# A better representation of the above graph would be a pie chart.
# Creating a pie-chart to conclude our analysis for on arrest data. A pie-chart is a better representation for
# proportion of a whole

labels = arr_sex_grouped_df['PERP_SEX']
sizes = arr_sex_grouped_df['PROP_VALUES']
explode = (0.1, 0.1)

fig1, ax1 = plt.subplots(figsize=(15, 9))

wedges, texts, autotexts = ax1.pie(sizes, explode=explode, labels=labels, autopct='%1.1f%%',
                                   shadow=True, startangle=90)

ax1.axis('equal')

ax1.legend(wedges, labels,
           title="Sex",
           loc="center left")

plt.setp(autotexts, size=15, weight="bold")
ax1.set_title("Hypothesis 2 - [Males are more likely to be arrested than females]\n")

plt.show()

# %% md

# Hypothesis 3

## Individuals of a particular race are more likely to be frisked and arrested than any other race

# %% md

### Frisking Data

# %%

# Identifying distribution of individuals by race

stop_question_frisk.SUSPECT_RACE_DESCRIPTION.value_counts()

# %%

# Creating a copy of the data

sqf = stop_question_frisk.copy()

# %%

# Selecting only the required columns from the sqf dataset for this hypothesis

sqf_frisk = sqf[sqf['FRISKED_FLAG'] == 'Y']
sqf_race_df = select_columns(sqf_frisk, 'SUSPECT_RACE_DESCRIPTION')
sqf_race_df

# %%

# Using the race_pct_col() function to determine what percentage of the population the race groups represent

sqf_race_group_pct = race_pct_col(sqf_race_df, 'SUSPECT_RACE_DESCRIPTION')

sqf_race_group_pct

# %%

# Using the grouping_for_count() function to create a new dataframe 'sqf_race_grouped_df' which consists of the count
# of the racial groups

sqf_race_grouped_df = grouping_for_count(sqf_race_group_pct, col_to_groupby1='SUSPECT_RACE_DESCRIPTION',
                                         col_to_groupby2='POP_BY_RACE_PCT',
                                         col_for_count='SUSPECT_RACE_DESCRIPTION')

sqf_race_grouped_df

# %%

# Using the normalized_values() function to generate normalized value for the race_grouped_df

normalized_values(sqf_race_grouped_df, 'COUNT', 'POP_BY_RACE_PCT')

# %%

# Using the proportional_values() function on sqf_race_grouped_df to determine ratios

proportional_values(sqf_race_grouped_df)

# %%

# Creating a plot to visualize the distribution of sqf data (normalized values)

fig, ax = plt.subplots(1, 1, figsize=(15, 9))

x = sqf_race_grouped_df['SUSPECT_RACE_DESCRIPTION']
y = sqf_race_grouped_df['NORM_VALUES']

ax.bar(x, y)
ax.set_title('Hypothesis 3 - [Individuals of a particular race are more likely to be frisked than any other race]')
plt.xlabel('Racial Group')
plt.ylabel('Normalized Values')
plt.show()

# %%

# Creating a plot to visualize the distribution of sqf data by proportional analysis (proportional values)

fig, ax = plt.subplots(1, 1, figsize=(15, 9))

x = sqf_race_grouped_df['SUSPECT_RACE_DESCRIPTION']
y = sqf_race_grouped_df['PROP_VALUES']

ax.bar(x, y)
ax.set_title('Hypothesis 3 - [Individuals of a particular race are more likely to be frisked than any other race]')
plt.xlabel('Racial Group')
plt.ylabel('Proportional Values')
plt.show()

# %%

# A better representation of the above graph would be a pie chart.
# Creating a pie-chart to conclude our analysis for this hypothesis. A pie-chart is a better representation for
# proportion of a whole

labels = sqf_race_grouped_df['SUSPECT_RACE_DESCRIPTION']
sizes = sqf_race_grouped_df['PROP_VALUES']
explode = (0.3, 0.1, 0.1, 0.1, 0.1, 0.1)

fig1, ax1 = plt.subplots(figsize=(15, 9))

wedges, texts, autotexts = ax1.pie(sizes, explode=explode, labels=labels, autopct='%1.1f%%',
                                   shadow=True, startangle=90)

ax1.axis('equal')

ax1.legend(wedges, labels,
           title="Racial Groups",
           loc="center left")

plt.setp(autotexts, size=15, weight="bold")
ax1.set_title("Hypothesis 3 - [Individuals of a particular race are more likely to be frisked than any other race]\n")

plt.show()

# %% md

## Arrests Data

# %%

arrest.PERP_RACE.value_counts()

# %%

# Creating a copy of the data

arr = arrest.copy()

# %%

# Selecting only the required columns from the arrest dataset for this hypothesis

arr_race_df = select_columns(arr, 'PERP_RACE')
arr_race_df

# %%

# Using the race_pct_col() function to determine what percentage of the population the race groups represent

arr_race_group_pct = race_pct_col(arr_race_df, 'PERP_RACE')

arr_race_group_pct

# %%

# Using the grouping_for_count() function to create a new dataframe 'arr_race_grouped_df' which consists of the count
# of the racial groups

arr_race_grouped_df = grouping_for_count(arr_race_group_pct, col_to_groupby1='PERP_RACE',
                                         col_to_groupby2='POP_BY_RACE_PCT',
                                         col_for_count='PERP_RACE')

arr_race_grouped_df

# %%

# Using the normalized_values() function to generate normalized value for the race_grouped_df

normalized_values(arr_race_grouped_df, 'COUNT', 'POP_BY_RACE_PCT')

# %%

# Using the proportional_values() function on arr_race_grouped_df to determine ratios

proportional_values(arr_race_grouped_df)

# %%

# Creating a plot to visualize the distribution of arrest data (normalized values)

fig, ax = plt.subplots(1, 1, figsize=(15, 9))

x = arr_race_grouped_df['PERP_RACE']
y = arr_race_grouped_df['NORM_VALUES']

ax.bar(x, y)
ax.set_title('Hypothesis 3 - [Individuals of a particular race are more likely to be arrested than any other race]')
plt.xlabel('Racial Group')
plt.ylabel('Normalized Values')
plt.xticks(rotation=90)
plt.show()

# %%

# Creating a plot to visualize the distribution of arrest data by proportional analysis (proportional values)

fig, ax = plt.subplots(1, 1, figsize=(15, 9))

x = arr_race_grouped_df['PERP_RACE']
y = arr_race_grouped_df['PROP_VALUES']

ax.bar(x, y)
ax.set_title('Hypothesis 3 - [Individuals of a particular race are more likely to be arrested than any other race]')
plt.xlabel('Racial Group')
plt.ylabel('Proportional Values')
plt.xticks(rotation=90)
plt.show()

# %%

# A better representation of the above graph would be a pie chart.
# Creating a pie-chart to conclude our analysis for this hypothesis. A pie-chart is a better representation for
# proportion of a whole

labels = arr_race_grouped_df['PERP_RACE']
sizes = arr_race_grouped_df['PROP_VALUES']
explode = (0.1, 0.1, 0.1, 0.1, 0.3, 0.2, 0.1)

fig1, ax1 = plt.subplots(figsize=(15, 9))

wedges, texts, autotexts = ax1.pie(sizes, explode=explode, labels=labels, autopct='%1.1f%%',
                                   shadow=True, startangle=90)

ax1.axis('equal')

ax1.legend(wedges, labels,
           title="Racial Groups",
           loc="lower left")

plt.setp(autotexts, size=15, weight="bold")
ax1.set_title("Hypothesis 3 - [Individuals of a particular race are more likely to be arrested than any other race]\n")

plt.show()

# %% md

# Hypothesis 4

##

# %%

# Reading the complaint data

complaint = pd.read_csv('NYPD_Complaint_Data_Historic_2019.csv')

# %%

# Preliminary analysis for complaint data

preliminary_analysis(complaint)

# %%

# Creating a copy of the data

comp = complaint.copy()

# %%

# Changing the date columns into datetime object

comp['CMPLNT_FR_DT'] = pd.to_datetime(comp['CMPLNT_FR_DT'], format='%m/%d/%Y')
comp['CMPLNT_TO_DT'] = pd.to_datetime(comp['CMPLNT_TO_DT'], format='%m/%d/%Y')
comp['RPT_DT'] = pd.to_datetime(comp['RPT_DT'], format='%m/%d/%Y')

comp.head()

# %%

# Selecting the required columns

comp_req = comp[['CMPLNT_NUM', 'CMPLNT_FR_DT', 'RPT_DT']]

# %%

# Selecting only the required columns from the complaint dataset for this hypothesis

comp_req = select_columns(comp, 'CMPLNT_NUM', 'CMPLNT_FR_DT', 'RPT_DT')
comp_req

# %%

# Calculating the difference between the date of crime occurence and date when the event was reported to the police

# Days
comp_req['DIFF_DAYS'] = comp_req['RPT_DT'] - comp_req['CMPLNT_FR_DT']

# Weeks
comp_req['DIFF_WEEKS'] = round(comp_req['DIFF_DAYS'] / np.timedelta64(1, 'W'))

# Months
comp_req['DIFF_MONTHS'] = round(comp_req['DIFF_DAYS'] / np.timedelta64(1, 'M'))

# %%

# Changing the data type of some columns

comp_req.DIFF_WEEKS = comp_req.DIFF_WEEKS.astype(int)
comp_req.DIFF_MONTHS = comp_req.DIFF_MONTHS.astype(int)

comp_req.head()

# %%

# Identifying distribution of number of crimes reported weeks after the crime occured

comp_req.DIFF_WEEKS.value_counts()

# %%

# Plotting the number of crimes reported vs weeks after the crime occured

fig, ax = plt.subplots(1, 1, figsize=(15, 9))

comp_req['DIFF_WEEKS'].value_counts().sort_index(ascending=True).plot(kind='bar', rot=0)

ax.set_title('Hypothesis 4 - []')
plt.xlabel('Number of weeks after the crime')
plt.ylabel('Number of Complaints reported')
plt.show()

# %%

# Identifying distribution of number of crimes reported months after the crime occured

comp_req.DIFF_MONTHS.value_counts()

# %%

# Plotting the number of crimes reported vs months after the crime occured

fig, ax = plt.subplots(1, 1, figsize=(15, 9))

comp_req['DIFF_MONTHS'].value_counts().sort_index(ascending=True).plot(kind='bar', rot=0)

ax.set_title('Hypothesis 4 - []')
plt.xlabel('Number of months after the crime')
plt.ylabel('Number of Complaints reported')
plt.show()


