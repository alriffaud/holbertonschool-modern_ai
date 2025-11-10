#!/usr/bin/env python3
"""Creates a SHAP explainer and computes SHAP values for regression models."""
import shap


def get_shap_explainer_and_values(model, X_train, X_test):
    """
    Creates a SHAP explainer and computes SHAP values for a regression model.
    Args:
        model: Trained regression model (e.g., Linear, Ridge, Lasso)
        X_train: Training data used as background for the explainer
        X_test: Test data to explain
    Returns:
        explainer: SHAP explainer object
        shap_values: SHAP values for predictions on X_test
    """
    # Create explainer using X_train as the background dataset
    explainer = shap.Explainer(model, X_train)

    # Compute SHAP values for X_test
    shap_values = explainer(X_test)

    return explainer, shap_values
