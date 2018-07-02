def groupByDtype(df):
    agg = df.columns.to_series().groupby(df.dtypes).groups
    return agg
