#!/usr/bin/env python3
"""
Chi-square tests for categorical features against Churn
"""
import pandas as pd
from scipy import stats


def chi_square_tests(df):
    """
    Performs chi-square tests between categorical features and the target
    Churn.
    Args:
        df (pd.DataFrame): DataFrame with a Churn column and categorical
        features.
    Returns:
        dict: Mapping {feature_name: p_value}
    """
    results = {}
    categorical_cols = df.select_dtypes(
        include=['object']).columns.drop('Churn')

    for col in categorical_cols:
        contingency = pd.crosstab(df[col], df['Churn'])
        chi2, p, _, _ = stats.chi2_contingency(contingency)
        results[col] = p

    return results
