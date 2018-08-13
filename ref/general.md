## Potential Steps

Note: APIs given for pandas and scikit-learn

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
- Handle missing values
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
        * scikit-learn: Imputer()
- Save cleaned data as separate dataset
- Initial EDA
    + df.describe() OR df.describe(include='all')
    + Cov and Corr
    + data visualizations
    + Find and visualize outliers
- Handle outliers
    + Find outliers using a common method
    + Remove outliers where needed
- Preprocessing for ML and AI
    + Scaling and transformation
        * [Scikit-learn Comparisons](http://scikit-learn.org/stable/auto_examples/preprocessing/plot_all_scaling.html)
        * StandardScaler # zero mean and unit variance
            - Very useful for scaling the target / response variables used for regression
        * MinMaxScaler # Scale features to lie between a given minimum and maximum value, often 0 and one
        * MaxAbsScaler # Scale so that the maximum absolute value of each feature is scaled to unit size
        * RobustScaler # For data containing many outliers
        * QuantileTransformer # Less influenced by outliers than scaling methods
            - output_distribution='uniform'
            - output_distribution='normal'
    + Normalization
        * Normalizer # scale individual samples to have unit norm
    + Binarization
        * Binarizer # Threshold numerical features to get boolean values
    + Encoding categorical features
        * OneHotEncoder # Transform each categorical feature with m possible values into m binary features, with only one active
    + Polynomial features
        * PolynomialFeatures # Get features high-order and interaction terms
    + Custom transformations
        * FunctionTransformer # Convert an existing Python function into a transformer to assist in data cleaning or processing
    + Target/label transformation
        * LabelBinarizer # Create a label indicator matrix from a list of multi-class labels
        * MultiLabelBinarizer # For multiple labels per instance
        * LabelEncoder# Help normalize labels such that they contain only values between 0 and n_classes-1, OR transform non-numerical labels (as long as they are hashable and comparable) to numerical labels
- Feature engineering
    + Convert text to numeric values where needed
    + Encode other data types, e.g., images
    + Create aggregation features
    + Create new calculated features
- Free-form text
    + Remove free form text from dataset unless performing text analytics, NL*, etc.
- Save cleaned and transformed data as separate dataset
- Perform analytics tasks!
    + Descriptive, predictive, prescriptive, and advanced
