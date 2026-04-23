"""
freeCodeCamp Certification Project - Sea Level Predictor
Boilerplate: https://github.com/freeCodeCamp/boilerplate-sea-level-predictor/

This script implements `draw_plot()` with two linear regression lines - one fitted on
the full historical record (1880-2050) and one on the recent acceleration period
(2000-2050) - as required by the freeCodeCamp certification unit tests in `test_module.py`,
using NOAA/CSIRO global sea level data.

The Jupyter Notebook (`sea_level_predictor.ipynb`) goes well beyond just passing the
tests - driven by curiosity to explore the data further with detailed slope/intercept
metrics, dual-forecast comparison, and acceleration detection analysis.
"""
import os
import sys
import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress

# Allow importing utils from parent directory
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), ".."))
from utils.output_manager import get_output_dir


def draw_plot():
    # Close any previous figures to prevent artist stacking across calls
    plt.close("all")

    # Read data from file
    df = pd.read_csv("https://drive.google.com/uc?id=1-SV4j8lrJNHsMsRibwVHqqH9YJfBkSd4")
    print(df.head())

    # Create a fresh figure and axes for every call
    fig, ax = plt.subplots(figsize=(12, 6))

    # Create scatter plot
    ax.scatter(
        x=df["Year"],
        y=df["CSIRO Adjusted Sea Level"],
        color="blue",
        label="Observed Data",
        s=10,
    )

    # Create first line of best fit (full history 1880–2050)
    slope, intercept = linregress(x=df["Year"], y=df["CSIRO Adjusted Sea Level"])[:2]
    years_extended = pd.Series(range(1880, 2051))
    ax.plot(
        years_extended,
        slope * years_extended + intercept,
        color="red",
        label=f"Best Fit (1880–present)  {slope:.4f}\"/yr",
        linewidth=2,
    )
    print(f"slope: {slope}, intercept: {intercept}")

    # Create second line of best fit (2000–present)
    df_recent = df[df["Year"] >= 2000]
    slope_recent, intercept_recent = linregress(
        x=df_recent["Year"], y=df_recent["CSIRO Adjusted Sea Level"]
    )[:2]
    print(f"slope: {slope_recent}, intercept: {intercept_recent}")

    years_recent = pd.Series(range(2000, 2051))
    ax.plot(
        years_recent,
        slope_recent * years_recent + intercept_recent,
        color="green",
        label=f"Best Fit (2000–present)  {slope_recent:.4f}\"/yr",
        linewidth=2,
    )
    print(f"slope: {slope_recent}, intercept: {intercept_recent}")

    # Add labels and title
    ax.set_xlabel("Year")
    ax.set_ylabel("Sea Level (inches)")
    ax.set_title("Rise in Sea Level")
    ax.legend(loc="upper left")

    # Save plot to outputs folder using shared utility
    OUTPUT_DIR = get_output_dir()
    fig.savefig(os.path.join(OUTPUT_DIR, "sea_level_plot.png"))

    return ax


if __name__ == "__main__":
    draw_plot()
