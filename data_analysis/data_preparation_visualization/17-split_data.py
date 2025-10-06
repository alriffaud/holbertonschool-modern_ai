#!/usr/bin/env python3
"""
Split dataset into training and testing sets using stratified sampling
"""
from sklearn.model_selection import train_test_split


def split_data(df, target='Churn', test_size=0.2, random_state=42):
    """
    Splits data into training and test sets with stratified sampling.
    Args:
        df: pandas DataFrame
        target: name of target column (default: 'Churn')
        test_size: proportion of data for test set (default: 0.2)
        random_state: random seed (default: 42)
    Returns:
        tuple: (X_train, X_test, y_train, y_test)
    """
    # Separate features and target
    X = df.drop(columns=[target])
    y = df[target]

    # Stratified split to preserve class balance
    X_train, X_test, y_train, y_test = train_test_split(
        X, y,
        test_size=test_size,
        random_state=random_state,
        stratify=y
    )

    return X_train, X_test, y_train, y_test
