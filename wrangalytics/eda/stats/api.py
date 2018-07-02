def debug(x):
    print(x)

def featurePercMissing(df):
    df.isnull().sum()/df.shape[0]
    
def featurePercNotMissing(df):
    df.count()/df.shape[0]

# TODO
# - Categorical feature mode, mode frequency, and mode percentage

def analyzeDfCovarianceAndCorrelation(df):
    """
    Analyze covarariance and correlation of dataframe features

    Notes 
    ------
    - Covariance in range -inf to inf, with sign indicating positive or negative relationships
    - Correlation is normalized in range -1 to 1, with -1 indicating a very strong negative correlation and vice versa. 0 indicates no correlation (independent).
    - Correlation does not necessarily imply causation, and often other hidden related features are not accounted for (confounding)
    """

def summarizeDataFrame(df):
    display(df.describe(include='all'))
    display(df.info())