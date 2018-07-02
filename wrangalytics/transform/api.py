def debug(x):
    print(x)

def percent2float(x):
    """
    Convert percent to float
    """
    return float(x.strip('%'))/100

def str2float(x):
    """
    Convert string to float
    """
    return float(x.replace(',',''))

def str2int(x):
    """
    Convert string to integer
    """
    return int(str(x))

def series2cat(series):
    """
    Convert continous feature to categorical
    """
    return series = series.astype('category')

def remapColVals(series, map):
    """
    Map series values to values defined in map
    """
    series.replace(map, inplace=True)

def handleMissingValues():
    # TODO: Remove feature if >60% missing values
    return True

def handleCardinality():
    # TODO: Remove feature if cardinality is equal to 1
    return True

def handleOutliers():
    return True