#!/usr/bin/env python3
"""Creates and returns a Lasso Regression model using Scikit-learn."""
from sklearn import linear_model


def lasso_regression(random_state):
    """
    Creates and returns a Lasso Regression model using Scikit-learn.
    Args:
        random_state (int): Seed for reproducibility.
    Returns:
        model: An untrained Lasso regression model instance.
    """
    model = linear_model.Lasso(alpha=1.0,
                               random_state=random_state,
                               max_iter=1000)
    return model
