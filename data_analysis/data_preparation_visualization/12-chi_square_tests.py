#!/usr/bin/env python3
"""
Chi-square tests for categorical features against Churn
"""
import pandas as pd


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
    categorical_cols = df.select_dtypes(include=['object']).columns.tolist()
    if 'Churn' in categorical_cols:
        categorical_cols.remove('Churn')

    stats = __import__('scipy.stats', fromlist=['stats'])
    chi2_contingency = stats.chi2_contingency

    for col in categorical_cols:
        contingency = pd.crosstab(df[col], df['Churn'])
        _, p, _, _ = chi2_contingency(contingency.values)
        results[col] = p

    return results
