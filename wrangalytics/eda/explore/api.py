def debug(x):
    print(x)

def findStringColumns(df):
    display(df.select_dtypes(include='object'))

def displayColumnNamesByType(df, type='object'):
    df.select_dtypes(include=type).columns.values

def displayRowIndex(df):
    display(df.index)

def displayColumnIndex(df):
    display(df.columns)

def displayUniqueValsBySeries(series):
    display(series.name, series.unique())

def displayUniqueValsByListSeries(list):
    for col in list:
        display(col, df[col].unique())

def displayIndexes(df):
    display(df.index)
    display(df.columns)

def featureCardinality(df):
    """
    Check cardinality for each feature

    Notes 
    ------
    - Ensure cardinality makes sense for both continuous and categorical features
    - Watch out for cardinality equal to 1 or greater than 50
    - Remove feature if cardinality is equal to 1 since no predictive power
    """
    df.apply(pd.Series.nunique)

def analyzeMissingValues(df):
    return True

def analyzeCardinality(df):
    return True

def analyzeOutliers(df):
    return True

def checkType(x):
    # Use 'is a' syntax to return boolean
    return type(x)

def checkDfType(df):
    df.dtypes

def checkSeriesType(series):
    series.dtype