def debug(x):
    print(x)

def getStringColumns(df, display=True):
    df = df.select_dtypes(include='object')
    if display:
        display(df)
    return df

def columnNamesByType(df, type='object', display=True):
    colNames = df.select_dtypes(include=type).columns.values
    if display:
        display(colNames)
    return colNames

def getRowIndex(df, display=True):
    idx = df.index
    if display:
        display(df.index)
    return idx

def getColumnIndex(df, display=True):
    idx = df.index
    if display:
        display(df.columns)
    return idx

def getUniqueValsBySeries(series, display=True):
    unique = series.unique()
    if display:
        display(series.name, unique)
    return unique

def displayUniqueValsByListSeries(list):
    for col in list:
        display(col, df[col].unique())

def getIndexes(df, display=True):
    d = dict();
    d['row_idx'] = df.index
    d['col_idx'] = df.columns
    if display:
        display(d['row_idx'])
        display(d['col_idx'])
    return d

def displayDfFeatureCardinality(df):
    """
    Check cardinality for each feature

    Notes 
    ------
    - Ensure cardinality makes sense for both continuous and categorical features
    - Watch out for cardinality equal to 1 or greater than 50
    - Remove feature if cardinality is equal to 1 since no predictive power
    """
    df.apply(pd.Series.nunique)

def getFeatureCardinality(series, display=True):
    card = series.nunique
    if display:
        display(card)
    return card

def analyzeMissingValues(df):
    return True

def analyzeCardinality(df):
    return True

def analyzeOutliers(df):
    return True

def getType(x, display=True):
    # Use 'is a' syntax to return boolean
    input_type = type(x)
    if display:
        display(input_type)
    return input_type

def getDfType(df, display=True):
    df_types = df.dtypes
    if display:
        display(df_types)
    return df_types

def getSeriesType(series, display=True):
    s_type = series.dtype
    if display:
        display(s_type)
    return  s_type