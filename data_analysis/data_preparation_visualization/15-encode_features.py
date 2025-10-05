#!/usr/bin/env python3
"""
Encode categorical and binary features for modeling
"""
import pandas as pd
from sklearn import preprocessing


def encode_features(df):
    """
    Encodes categorical features for modeling using Scikit-learn.
    Args:
        df: pandas DataFrame
    Returns:
        tuple: (encoded DataFrame, LabelEncoder for Churn,
                OrdinalEncoder for binary columns,
                OrdinalEncoder for TenureGroup)
    """
    df = df.copy()

    # Label encode Churn (No→0, Yes→1)
    churn_le = preprocessing.LabelEncoder()
    df['Churn'] = churn_le.fit_transform(df['Churn'])

    # Binary columns (No→0, Yes→1)
    binary_cols = ['Partner', 'Dependents', 'PaperlessBilling',
                   'SeniorCitizen']
    binary_oe = preprocessing.OrdinalEncoder(categories=[['No', 'Yes']])
    for col in binary_cols:
        df[[col]] = binary_oe.fit_transform(df[[col]]).astype(int)

    # TenureGroup: alphabetical order
    tenure_oe = preprocessing.OrdinalEncoder()
    df[['TenureGroup']] = tenure_oe.fit_transform(
        df[['TenureGroup']]).astype(int)

    # One-hot encoding for Contract and PaymentMethod (drop_first=True)
    df = pd.get_dummies(df, columns=['Contract', 'PaymentMethod'],
                        drop_first=True)

    # Convert dummy columns to int (instead of bool)
    dummy_cols = [col for col in df.columns
                  if 'Contract_' in col or 'PaymentMethod_' in col]
    df[dummy_cols] = df[dummy_cols].astype(int)

    return df, churn_le, binary_oe, tenure_oe
