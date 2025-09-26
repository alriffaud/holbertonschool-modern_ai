#!/usr/bin/env python3
"""
Plot Correlation Heatmap
"""
import seaborn as sns
import matplotlib.pyplot as plt


def plot_correlation_heatmap(df):
    """
    Visualizes correlations between continuous numeric features using seaborn
    heatmap.
    Args:
        df: pandas DataFrame
    """
    plt.figure(figsize=(6, 5))

    # Compute the correlation matrix
    numeric_cols = df.select_dtypes(include=['number']).columns.tolist()
    corr = df[numeric_cols].corr()

    # Generate a heatmap
    sns.heatmap(corr, annot=True, fmt=".2f", cmap="coolwarm", square=True,
                vmin=-1, vmax=1)
    plt.title("Correlation Matrix")
    plt.show()
