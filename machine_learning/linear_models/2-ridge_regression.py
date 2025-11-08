#!/usr/bin/env python3
"""Creates a Ridge Regression model using Scikit-learn."""
from sklearn import linear_model


def ridge_regression(random_state):
    """
    Creates and returns a Ridge Regression model using Scikit-learn.
    Args:
        random_state (int): Seed for reproducibility.
    Returns:
        model: An untrained Ridge regression model instance.
    """
    model = linear_model.Ridge(alpha=1.0, random_state=random_state)
    return model
