#!/usr/bin/env python3
"""
Plot churn rate per category of a given categorical feature.
"""
import matplotlib.pyplot as plt
import pandas as pd


def plot_categorical_vs_churn(df, col):
    """
    Visualize churn rates per category for a given categorical column.
    Args:
        df (pd.DataFrame): DataFrame with a 'Churn' column.
        col (str): Name of categorical column to analyze.
    Returns:
        None
    """
    # Convert Churn to numeric (1 for Yes, 0 for No) if necessary
    churn_numeric = df["Churn"].apply(lambda x: 1 if x == "Yes" else 0)

    # Compute churn rate per category
    churn_rate = churn_numeric.groupby(df[col]).mean()

    # Plot
    plt.figure(figsize=(12, 8))
    plt.bar(churn_rate.index, churn_rate)

    plt.ylabel("Churn Rate")
    plt.title(f"Churn Rate by {col}")
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()
