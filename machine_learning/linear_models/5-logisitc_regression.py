#!/usr/bin/env python3
"""Implements a simple logistic regression model using Scikit-learn."""
from sklearn import linear_model


def Logistic_Regression_Model(random_state):
    """
    Creates and returns an untrained Logistic Regression model
    using Scikit-learn.
    Args:
        random_state (int): Random seed for reproducibility.
    Returns:
        model: An untrained LogisticRegression instance.
    """
    model = linear_model.LogisticRegression(
        random_state=random_state,
        max_iter=1000  # Ensures convergence for most datasets
    )
    return model
