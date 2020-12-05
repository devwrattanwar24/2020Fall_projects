import pandas as pd
import matplotlib.pyplot as plt
import os
import seaborn as sns

os.chdir('D:/Downloads/')

arrests_2019 = pd.read_csv('NYPD_Arrests_Data_2019.csv')


# Function for selecting columns from a dataframe
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
    return new_df


# Creating a function for preliminary analysis - rows, columns, null counts etc.
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


def race_pct_col(df):
    """

    This function allows us to add the racial percentage column to an existing
    dataframe that contains the 'PERP_RACE' column. Addition of this new column
    is an intermediate step to allow normalizing the values. Within this function
    another function - race_percentage is used.

    :param df: Dataframe to which the racial percentage column has to be appended
    :return: Dataframe with the added column - racial percentage distribution

    >>> df = pd.DataFrame({'col1': [1, 2, 3, 4, 5, 6, 7, 8], 'PERP_RACE': ['AMERICAN INDIAN/ALASKAN NATIVE', 'ASIAN / PACIFIC ISLANDER', 'BLACK', 'BLACK HISPANIC', 'WHITE', 'WHITE HISPANIC', '(null)', 'UNKNOWN']})
    >>> race_pct_col(df)
       col1                       PERP_RACE  POP_BY_RACE_PCT
    0     1  AMERICAN INDIAN/ALASKAN NATIVE           0.0043
    1     2        ASIAN / PACIFIC ISLANDER           0.1400
    2     3                           BLACK           0.2195
    3     4                  BLACK HISPANIC           0.0233
    4     5                           WHITE           0.3214
    5     6                  WHITE HISPANIC           0.1053
    6     7                          (null)           0.1862
    7     8                         UNKNOWN           0.1862


    """
    race_pct = pd.DataFrame(df.apply(lambda row: race_percentage(row, 'PERP_RACE'), axis=1))
    race_pct.rename(columns={0 : 'POP_BY_RACE_PCT'}, inplace=True)
    df = pd.concat([df, race_pct], axis=1)
    return df


def race_percentage(row, colname) -> pd.core.series.Series:
    # Population data retrieved from: https://worldpopulationreview.com/us-cities/new-york-city-ny-population

    # Total NYC population = 8,323,340

    # Credit to Rahul + Megha (Link their github notebook)

    #     """
    #     This function is used to return a pandas series that has the race percentage value of all the different
    #     races present in NYC.

    #     :param row: denotes that the operation has to be performed across rows
    #     :param colname: Column name on which operation has to be done
    #     :return : a specific numeric value if a row match is found
    #     >>> data_dummy = {'Race':  ['AMERICAN INDIAN/ALASKAN NATIVE','ASIAN / PACIFIC ISLANDER', 'BLACK','BLACK HISPANIC','WHITE','WHITE HISPANIC','UNKNOWN/OTHER'],'Offense': ['FRAUDS', 'BURGLARY','HARRASSMENT 2','FORGERY','FRAUDS','FRAUDS','FRAUDS'],'Comp_no':[1,2,3,4,5,6,7]}
    #     >>> df_dummy = pd.DataFrame (data_dummy, columns = ['Race','Offense','Comp_no'])
    #     >>> df_dummy.apply (lambda row: race_percentage(row,'Race'), axis=1)
    #     0    0.0043
    #     1    0.1400
    #     2    0.2195
    #     3    0.0233
    #     4    0.3214
    #     5    0.1053
    #     6    0.1862
    #     dtype: float64

    #     """

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