#!/usr/bin/env python3
"""
Scale numeric features using StandardScaler
"""
import pandas as pd
from sklearn import preprocessing


def scale_numeric(df):
    """
    Standardizes numeric columns (MonthlyCharges, TotalCharges)
    using StandardScaler (mean=0, std=1)
    Args:
        df: pandas DataFrame
    Returns:
        pandas DataFrame with scaled numeric columns
    """
    df = df.copy()

    # Instantiate the scaler
    scaler = preprocessing.StandardScaler()

    # Columns to scale
    cols_to_scale = ['MonthlyCharges', 'TotalCharges']

    # Fit and transform the selected columns
    df[cols_to_scale] = scaler.fit_transform(df[cols_to_scale])

    return df
