import numpy as np
import pandas as pd

def adapt_datatype(df:pd.DataFrame)->pd.DataFrame:
    """ adapt data type in dataframe df i.e. the type of column "TotalCharges" """
    df['TotalCharges'] = df['TotalCharges'].replace(' ', np.nan)# convert to float64
    df['TotalCharges'] = df['TotalCharges'].astype('float64')
    return df

def get_numeric_features(df:pd.DataFrame)->list:
    """Return list of all numeric features in dataframe df """
    numeric_features = list(df.dtypes[(df.dtypes == 'int64') | (df.dtypes == 'float64')].index)
    return numeric_features

def get_categorical_features(df:pd.DataFrame)->list:
    """Return list of all categorical features in dataframe df """
    categorical_features = list(df.dtypes[df.dtypes == 'object'].index)
    return categorical_features