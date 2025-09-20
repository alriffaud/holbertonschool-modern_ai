#!/usr/bin/env python3
"""
Module for visualizing missing values in a DataFrame.
"""
import matplotlib.pyplot as plt
import numpy as np


def plot_missingness(df):
    """
    Visualizes missing values in a DataFrame using a scatter plot.
    Args:
        df (pd.DataFrame): DataFrame to analyze.
    Returns:
        None
    """
    plt.figure(figsize=(12, 8))

    for col in df.columns:
        missing_idx = df.index[df[col].isnull()]
        plt.scatter(
            missing_idx,
            [col] * len(missing_idx),
            marker='|',
            color='blue'
        )

    plt.title("Missingness Plot")
    plt.yticks(range(len(df.columns)), df.columns)
    plt.tight_layout()
    plt.show()
