"""
freeCodeCamp Certification Project - Mean, Variance & Standard Deviation Calculator
Boilerplate: https://github.com/freeCodeCamp/boilerplate-mean-variance-standard-deviation-calculator/

This script implements the `calculate()` function that satisfies the exact unit test
cases defined in `test_module.py` for the freeCodeCamp certification. It reshapes a
9-element list into a 3×3 NumPy matrix and computes mean, variance, standard deviation,
max, min, and sum along columns (axis 0), rows (axis 1), and the flattened array.

The Jupyter Notebook (`mean_var_std.ipynb`) goes beyond passing the tests - driven by
curiosity to explore the computations further with interactive heatmap and bar chart
visualizations for each statistical measure.
"""
import numpy as np


def calculate(list: np.array) -> dict:
    """
    Calculate the mean, variance, standard deviation, max, min, and sum of a 1D list of numbers.

    Args:
        list (np.ndarray): A 1D numpy array of numbers.

    Returns:
        dict: A dictionary containing the mean, variance, standard deviation, max, min, and sum.
    """
    if len(list) != 9:
        raise ValueError("List must contain nine numbers.")

    matrix = np.array(list).reshape(3, 3)  # Reshape the list into a 3x3 matrix
    print("Matrix:\n", matrix)  # Debugging line to check the matrix
    print("Matrix shape:", matrix.shape)  # Debugging line to check the shape of the matrix 

    mean = [matrix.mean(axis=0).tolist(), matrix.mean(axis=1).tolist(), matrix.mean().tolist()] # axis=0 for columns, axis=1 for rows, and no axis for the entire matrix
    variance = [matrix.var(axis=0).tolist(), matrix.var(axis=1).tolist(), matrix.var().tolist()]
    std_dev = [matrix.std(axis=0).tolist(), matrix.std(axis=1).tolist(), matrix.std().tolist()]
    max_val = [matrix.max(axis=0).tolist(), matrix.max(axis=1).tolist(), matrix.max().tolist()]
    min_val = [matrix.min(axis=0).tolist(), matrix.min(axis=1).tolist(), matrix.min().tolist()]
    sum_val = [matrix.sum(axis=0).tolist(), matrix.sum(axis=1).tolist(), matrix.sum().tolist()]

    # Create a dictionary to hold the results
    calculations = {
        'mean': mean,
        'variance': variance,
        'standard deviation': std_dev,
        'max': max_val,
        'min': min_val,
        'sum': sum_val
    }

    return calculations

calculate([0, 1, 2, 3, 4, 5, 6, 7, 8])