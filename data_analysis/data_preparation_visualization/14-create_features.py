#!/usr/bin/env python3
"""
Feature engineering: create NumServices and TenureGroup
"""
import pandas as pd


def create_features(df):
    """
    Engineers new features from the dataset:
    - NumServices: counts the number of subscribed services (Yes).
    - TenureGroup: bins tenure into categorical intervals.
    Returns the modified DataFrame with new features and drops originals used.
    """
    service_cols = [
        'MultipleLines',
        'InternetService',
        'OnlineSecurity',
        'OnlineBackup',
        'DeviceProtection',
        'TechSupport',
        'StreamingTV',
        'StreamingMovies'
    ]

    # Count "Yes" for each service, treating InternetService separately
    df['NumServices'] = (
        df[service_cols]
        .apply(lambda row: sum(
            ((val == 'Yes') or
             (col == 'InternetService' and val in ['DSL', 'Fiber optic']))
            for col, val in row.items()
        ), axis=1)
    )

    # Bin tenure into groups
    bins = [0, 12, 24, 48, 60, float("inf")]
    labels = ['0-12', '13-24', '25-48', '49-60', '60+']
    df['TenureGroup'] = pd.cut(
        df['tenure'], bins=bins, labels=labels, right=True)

    # Drop the original columns used
    df = df.drop(columns=service_cols + ['tenure'])

    return df
