import pandas as pd
import matplotlib.pyplot as plt
import os
import numpy as np

# Change directory by uncommenting and passing the appropriate directory path
# os.chdir('D:/Downloads/')

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

    >>> df = pd.read_csv('dummy_doctest_files/Age_group.csv')
    >>> age_pct_col(df)
      AGE_GROUP  POP_BY_AGE_PCT
    0     25-44           0.272
    1     18-24           0.065
    2     45-64           0.261
    3     45-64           0.261
    4       <18           0.232
    5     25-44           0.272
    6     18-24           0.065
    7     45-64           0.261
    8       <18           0.232
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
    >>> race_pct_col(df, 'SUSPECT_RACE_DESCRIPTION')
       col1        SUSPECT_RACE_DESCRIPTION  POP_BY_RACE_PCT
    0     1  AMERICAN INDIAN/ALASKAN NATIVE           0.0043
    1     2        ASIAN / PACIFIC ISLANDER           0.1400
    2     3                           BLACK           0.2195
    3     4                  BLACK HISPANIC           0.0233
    4     5                           WHITE           0.3214
    5     6                  WHITE HISPANIC           0.1053
    6     7                          (null)           0.1862
    7     8                         UNKNOWN           0.1862

    >>> df = pd.read_csv('dummy_doctest_files/Race_group.csv')
    >>> race_pct_col(df, 'SUSPECT_RACE_DESCRIPTION')
       SUSPECT_RACE_DESCRIPTION  POP_BY_RACE_PCT
    0                    (null)           0.1862
    1  ASIAN / PACIFIC ISLANDER           0.1400
    2                     BLACK           0.2195
    3            BLACK HISPANIC           0.0233
    4                     WHITE           0.3214
    5            WHITE HISPANIC           0.1053
    6            BLACK HISPANIC           0.0233
    7                    (null)           0.1862
    8  ASIAN / PACIFIC ISLANDER           0.1400
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
    
    """
    This function is used to return a pandas series that has the sex percentage value of all the sexes present in NYC.

    :param row: denotes that the operation has to be performed across rows
    :param colname: Column name on which operation has to be done
    :return : a specific numeric value if a row match is found
    >>> data_dummy = {'Sex':  ['MALE','FEMALE'],'Offense': ['FRAUDS', 'FRAUDS'],'Comp_no':[1,2]}
    >>> df_dummy = pd.DataFrame (data_dummy, columns = ['Sex','Offense','Comp_no'])
    >>> df_dummy.apply (lambda row: sex_percentage(row,'Sex'), axis=1)
    0    0.4767
    1    0.5233
    dtype: float64
    """

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
    >>> sex_pct_col(df, 'SEX')
          SEX  POP_BY_SEX_PCT
    0    MALE          0.4767
    1  FEMALE          0.5233
    2  FEMALE          0.5233

    >>> df = pd.read_csv('dummy_doctest_files/Gender_group.csv')
    >>> sex_pct_col(df, 'SUSPECT_SEX')
      SUSPECT_SEX  POP_BY_SEX_PCT
    0        MALE          0.4767
    1        MALE          0.4767
    2      FEMALE          0.5233
    3      FEMALE          0.5233
    4      FEMALE          0.5233
    5        MALE          0.4767
    6      FEMALE          0.5233
    7        MALE          0.4767
    8        MALE          0.4767

    """
    sex_pct = pd.DataFrame(df.apply(lambda row: sex_distribution(row, col), axis=1))
    sex_pct.rename(columns={0: 'POP_BY_SEX_PCT'}, inplace=True)
    df = pd.concat([df, sex_pct], axis=1)
    return df
