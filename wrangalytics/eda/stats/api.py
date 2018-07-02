def debug(x):
    print(x)

def featurePercMissing(df):
    df.isnull().sum()/df.shape[0]
    
def featurePercNotMissing(df):
    df.count()/df.shape[0]

# TODO
# - Categorical feature mode, mode frequency, and mode percentage