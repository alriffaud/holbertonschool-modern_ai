#!/usr/bin/env python3
"""
Module for converting column types in a DataFrame.
"""
import pandas as pd


def convert_columns(df):
    """
    Converts specific columns in a DataFrame:
    - TotalCharges: converted to numeric (invalid values become NaN).
    - SeniorCitizen: mapped from 0/1 to "No"/"Yes".
    Args:
        df (pd.DataFrame): DataFrame containing the columns TotalCharges and
        SeniorCitizen.
    Returns:
        pd.DataFrame: Modified DataFrame with updated column types.
    """
    # Convert TotalCharges to numeric, coercing errors to NaN
    df["TotalCharges"] = pd.to_numeric(df["TotalCharges"], errors="coerce")

    # Map SeniorCitizen values 0 -> "No", 1 -> "Yes"
    df["SeniorCitizen"] = df["SeniorCitizen"].map({0: "No", 1: "Yes"})

    return df
