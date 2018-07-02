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
    Convert string feature series to categorical
    """

    series = series.astype('category')
    return series

def seriesList2cat(list):
    """
    Convert series list to categorical
    """
    for series in list:
        df[series] = df[series].astype('category')
        display(df[series].dtype)

def cont2cat(series):
    """
    Convert continous feature to categorical (aka binning)

    Notes
    -----
    Binning Methods
    - Equal-width
    - Equal-frequency
    """

def remapColVals(series, map):
    """
    Map series values to values defined in map

    Notes
    -----
    - This function should be used to map categorical values to a standard set of levels
    """
    series.replace(map, inplace=True)

def handleMissingValues():
    # TODO: Remove feature if >60% missing values
    return True

def imputeMissingValues():
    """
    Impute missing values

    Notes
    -----
    - Common methods: use median or mean for continuos values and mode for categorical values
    - Kelleher, John D., et al. recommend considering not using imputation on features missing more than 30% of values, and strongly recommend against for features missing greater than 50% of values
    """
    return True

def removeMissingTargetRows():
    """
    Remove rows with missing target values
    """
    return True

def handleCardinality():
    # TODO: Remove feature if cardinality is equal to 1
    return True

def handleOutliers():
    """
    Handle features with outliers

    TODO
    -----
    - Add methods for outlier removal

    Notes
    -----
    Outlier Threshold Methods
    - Feature min and max combined with domain expertise
    - Upper and lower set to mean value plus or minus 2 times the std dev (assumes underlying normal distribution)
    - Clamp transformation (only apply if suspected model performing poorly due to outliers)
        - Lower threshold: 1st quartile minus 1.5 times the IQR
        - Upper threshold: 3rd quartile plus 1.5 times the IQR
    """
    return True

def standardizeSeries(series):
     """
    Standardize series values

    Notes
    -----
    Standardization and normalization methods
    - Range normalization
    - Standard scores (assumes normal distribution): (x - x_mean)/x_std_dev
    """