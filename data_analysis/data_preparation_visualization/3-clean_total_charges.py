#!/usr/bin/env python3
"""
Module for cleaning missing values in TotalCharges.
"""


def clean_total_charges(df, method='drop'):
    """
    Handles missing values in the 'TotalCharges' column.
    Args:
        df (pd.DataFrame): DataFrame with missing values in TotalCharges
        method (str): Strategy to handle missing values:
            - 'drop': Remove rows with missing TotalCharges
            - 'median': Fill with column median
            - 'impute': Replace with MonthlyCharges * tenure
    Returns:
        pd.DataFrame: Modified DataFrame
    """
    df = df.copy()

    if method == 'drop':
        df = df.dropna(subset=['TotalCharges'])
    elif method == 'median':
        median_val = df['TotalCharges'].median()
        df['TotalCharges'] = df['TotalCharges'].fillna(median_val)
    elif method == 'impute':
        missing_mask = df['TotalCharges'].isna()
        df.loc[missing_mask, 'TotalCharges'] = (
            df.loc[missing_mask, 'MonthlyCharges'] * df.loc[missing_mask,
                                                            'tenure']
        )
    else:
        raise ValueError(
            "Invalid method. Choose from 'drop', 'median', or 'impute'.")

    return df
