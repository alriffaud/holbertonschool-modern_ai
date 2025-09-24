#!/usr/bin/env python3
"""
Module for plotting churn distribution.
"""
import matplotlib.pyplot as plt


def plot_churn_distribution(df):
    """
    Visualizes churn class distribution.
    Args:
        df (pd.DataFrame): DataFrame with a 'Churn' column.
    Returns:
        None
    """
    plt.figure(figsize=(12, 8))

    colors = ['blue', 'orange']
    counts = df['Churn'].value_counts()[['No', 'Yes']]
    plt.bar(counts.index, counts.values, color=colors)

    plt.title("Churn Distribution")
    plt.xlabel("Churn")
    plt.ylabel("Count")
    plt.show()
