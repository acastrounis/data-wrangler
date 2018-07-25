def debug(x):
    print(x)

### Conversions

## Use case: converters argument in pandas data read functions (e.g., read_csv). Use dtypes argument for converting string to category.

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

def str2datetime(x):
    """
    Convert string to datetime
    """
    return pd.to_datetime

def series2cat(series):
    """
    Convert string feature series to categorical
    """
    return series.astype('category')

def seriesList2cat(df, list):
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

### Mapping

def remapColVals(series, map):
    """
    Map series values to values defined in map

    EX:

    map = {
        "itemName1": "newItemName1",
        "itemName2": "newItemName2",
        ...
        "itemNameN": "newItemNameN",
    }

    Notes
    -----
    - This function should be used to map categorical values to a standard set of levels
    """
    series.replace(map, inplace=True)

### Wrangling

def dropColsByList(df, list):
    df.drop(columns=list, inplace=True)

### Missing Values

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

### Outliers

def handleOutliers():
    """
    Handle features with outliers

    TODO
    -----
    - Add methods for outlier removal

    Notes
    -----
    Outlier Threshold Methods
    - Feature min and max combined with domain expertise (e.g., 0.5/0.95 rule)
    - Upper and lower set to mean value plus or minus 2 times the std dev (assumes underlying normal distribution, and could be a diff. multiple)
    - Clamp transformation (only apply if suspected model performing poorly due to outliers)
        - Lower threshold: 1st quartile minus 1.5 times the IQR
        - Upper threshold: 3rd quartile plus 1.5 times the IQR
    """
    return True

### Standardization and Normalization

def standardizeSeries(series):
     """
    Standardize series values

    Notes
    -----
    Standardization and normalization methods
    - Range normalization
    - Standard scores (assumes normal distribution): (x - x_mean)/x_std_dev
    """