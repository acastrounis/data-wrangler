def analyzeMissingValues(df):
    """
    Analyze missing values in dataframe

    Args
    -----
    - 
    
    Useful Methods
    -----
    - isnull()
    - notnull()
    - dropna()
    - fillna()

    Notes 
    ------
    - Sentinal values used by Pandas
        + None (dtype = object)
        + NaN (not a number, dtype = float64, np.nan)
    """
    return True

def getColsWithMissingValues(df):
    return df.columns[df.isnull().any()]

def getDfMissingValues(df):
    return df.isnull()

def getRowsWithMissingValues(df):
    return df.isnull().any(axis=1)

def getMissingValueCountsPerCol(df):
    return df.isnull().sum()

def getNumberOfRowsWithMissingValues(df):
    return df[df.isnull().any(axis=1)]