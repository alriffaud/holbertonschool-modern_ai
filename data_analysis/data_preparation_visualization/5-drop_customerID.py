#!/usr/bin/env python3
"""
Module for dropping the customerID column from a DataFrame.
"""


def drop_customerID(df):
    """
    Drops the customerID column from a DataFrame.
    Args:
        df (pd.DataFrame): DataFrame containing a customerID column.
    Returns:
        pd.DataFrame: DataFrame without the customerID column.
    """
    df = df.copy()
    df = df.drop(columns=['customerID'])
    return df
