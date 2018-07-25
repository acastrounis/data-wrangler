## Potential Steps

- Import packages
- Configure notebook and environment
- Define functions
- Define vars
- Create mappings for converting input data
- Import data using mappings on import
- Create a copy of original data frame for modifications
    + df = df_orig.copy()
- Initial DF overview
    + All at once
        * df.info() gives df shape, col names and types, col type counts, memory usage, etc.
    + Individually
        * DF sample rows (head, tail)
            - Visually inspect missing values, bad values, sentinel values (None, null, NaN, or NA), outliers, etc.
        * DF col data types (info or dtypes)
        * DF size (shape)
        * Series counts for each data type (get_dtype_counts)
        * Indexes
            - Row: df.index
            - Col: df.columns
- Unique values and values by type
    + Num unique values per col: df.nunique()
    + Check string cols and unique string values per column
        * Convert string values to the desired unique set (use series replace function with map)
        * Convert string cols to category cols as needed
    + Check category cols and unique category values per column, convert if needed
- Explore missing values
    + CLI
        * isnull()
        * notnull()
    + List cols and number of rows in each with missing values
        * Cols: df.columns[df.isnull().any()]
        * Num rows per col: df.isnull().sum()
    + Masked df
        * df: df.isnull()
        * Rows with missing values: df.isnull().any(axis=1)
    + Filtered df
        * Rows with missing values: df[df.isnull().any(axis=1)]
        * Number of rows with missing values: df[df.isnull().any(axis=1)].shape
- Explore outliers
    + Find outliers using a common method
- Clean data
    + CLI
        * isnull()
        * notnull()
        * drop()
    + Drop columns that are not needed, contain no useful information (only 1 unique value), or contain excessive missing values (e.g., > 60%)
        * df.drop(columns=<colNameArray>, inplace=True)
    + Drop rows containing a certain amount of missing values, if desired
    + Drop all rows containing any missing values, if desired
        * df.dropna()
    + Impute and/or replace missing values
    + Remove outliers
- Save cleaned data as separate dataset
- Feature engineering
    + Encode categorical features
    + Convert text to numeric values where needed
    + Encode other data types, e.g., images
- Save engineered data as separate dataset
- Initial stats
    + df.describe() OR df.describe(include='all')
    + Cov and Corr
    + data visualizations
