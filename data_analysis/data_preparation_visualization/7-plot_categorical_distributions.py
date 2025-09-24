#!/usr/bin/env python3
"""
Plot categorical feature distributions
"""
import matplotlib.pyplot as plt


def plot_categorical_distributions(df, columns_to_plot=None):
    """
    Visualizes the distributions of categorical features in a grid layout.
    Args:
        df: pandas DataFrame
        columns_to_plot: Optional list of categorical columns (default: all
        object dtype columns)
    Returns:
        None
    """
    if columns_to_plot is None:
        columns_to_plot = df.select_dtypes(
            include=['object']).columns.drop('Churn')
    else:
        columns_to_plot = [col for col in columns_to_plot if col in df.columns]

    n_cols, n_rows = 3, (len(columns_to_plot) + 2) // 3

    fig, axes = plt.subplots(n_rows, n_cols, figsize=(15, 5 * n_rows))
    axes = axes.flatten()

    for i, col in enumerate(columns_to_plot):
        counts = df[col].value_counts()
        axes[i].bar(counts.index, counts.values)
        axes[i].set_title(col)
        axes[i].tick_params(axis="x", rotation=45)

    # Removing any unused subplots
    for j in range(i + 1, len(axes)):
        axes[j].axis('off')

    plt.tight_layout()
    plt.savefig("Task_7.png")
    plt.show()
