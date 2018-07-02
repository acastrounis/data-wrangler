def debug(x):
    print(x)

def findStringColumns(df):
    display(df.select_dtypes(include='object'))

def displayRowIndex(df):
    display(df.index)

def displayColumnIndex(df):
    display(df.columns)

def displayUniqueVals(series):
    display(series.name, series.unique())

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