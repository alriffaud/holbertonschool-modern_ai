#!/usr/bin/env python3
"""
Module for removing duplicate rows from a DataFrame.
"""


def remove_duplicates(df):
    """
    Removes duplicate rows from a DataFrame.
    Args:
        df (pd.DataFrame): DataFrame to process.
    Returns:
        pd.DataFrame: DataFrame without duplicate rows.
    """
    df = df.copy()

    df = df.drop_duplicates()

    return df
