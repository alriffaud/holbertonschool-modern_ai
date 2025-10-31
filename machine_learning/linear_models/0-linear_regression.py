#!/usr/bin/env python3
"""Creates a Linear Regression model using Ordinary Least Squares."""
from sklearn import linear_model


def Linear_Regression():
    """
    Creates and returns an untrained LinearRegression model.
    Returns:
        model: sklearn.linear_model.LinearRegression instance
    """
    model = linear_model.LinearRegression()
    return model
