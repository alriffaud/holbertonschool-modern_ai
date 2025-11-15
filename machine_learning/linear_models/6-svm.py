#!/usr/bin/env python3
"""
This module provides a function to create untrained Support Vector Machine
(SVM) models with different kernel types.
"""
from sklearn import svm


def get_SVM_model(name, random_state):
    """
    Returns an untrained SVM classifier with the specified kernel.
    Args:
        name (str): kernel type ("linear", "poly", "rbf")
        random_state (int): seed for reproducibility
    Returns:
        svm.SVC: an untrained SVM model
    """
    if name == "linear":
        return svm.SVC(kernel="linear", random_state=random_state)

    if name == "poly":
        return svm.SVC(kernel="poly", random_state=random_state)

    if name == "rbf":
        return svm.SVC(kernel="rbf", random_state=random_state)

    raise ValueError("Invalid model name. Choose: 'linear', 'poly', 'rbf'.")
