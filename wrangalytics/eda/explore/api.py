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