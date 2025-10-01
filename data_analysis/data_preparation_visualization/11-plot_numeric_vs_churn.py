#!/usr/bin/env python3
"""
Plot numeric feature distributions vs Churn
"""
import matplotlib.pyplot as plt
import numpy as np


def plot_numeric_vs_churn(df, col):
    """
    Compares numeric feature distributions by churn using side-by-side
    histograms.
    Args:
        df: pandas DataFrame with Churn column
        col: Numeric column name
    Returns:
        None
    """
    plt.figure(figsize=(12, 8))

    churn_values = ['No', 'Yes']

    bins = 30
    bin_edges = np.histogram_bin_edges(df[col], bins=bins)

    width = (bin_edges[1] - bin_edges[0]) / 3

    for i, churn_value in enumerate(churn_values):
        subset = df[df['Churn'] == churn_value][col]
        counts, _ = np.histogram(subset, bins=bin_edges)
        plt.bar(
            bin_edges[:-1] + i * width,
            counts,
            width=width,
            label=churn_value,
            align='edge'
        )

    plt.xlabel(col)
    plt.title(f"{col} Distribution by Churn")
    plt.legend(title="Churn")
    plt.tight_layout()
    plt.savefig("Task_11.png")
    plt.show()
