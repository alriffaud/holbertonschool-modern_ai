#!/usr/bin/env python3
"""
Performs Welch's t-tests for numeric features vs Churn
"""
import pandas as pd
from scipy import stats


def ttest_numeric(df):
    """
    Performs Welch's t-test for each numeric feature in df,
    comparing distributions between Churn=Yes and Churn=No.
    Returns a dictionary {feature: p_value}.
    """

    numeric_cols = df.select_dtypes(include=['int64', 'float64']).columns
    results = {}

    for col in numeric_cols:
        group_yes = df[df["Churn"] == "Yes"][col].dropna()
        group_no = df[df["Churn"] == "No"][col].dropna()

        if len(group_yes) > 1 and len(group_no) > 1:
            _, pval = stats.ttest_ind(group_yes, group_no, equal_var=False)
            results[col] = pval

    return results
