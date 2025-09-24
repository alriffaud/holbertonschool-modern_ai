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

    churn_counts = df['Churn'].value_counts()

    plt.bar(churn_counts.index, churn_counts.values,
            color=['skyblue', 'salmon'])

    plt.title("Churn Distribution")
    plt.xlabel("Churn")
    plt.ylabel("Count")
    plt.show()
