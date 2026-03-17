"""
A module that adds numbers together.

You may want to delete this module or modify it for your package.
It's generally good practice to have a docstring
that explains the purpose of the module, at the top.
"""
import numpy as np


def add_numbers(a, b):
    """
    Add two numbers together and return the result.

    This is an example function with a numpy style docstring.
    We recommend using this style for consistency and readability.

    Parameters
    ----------
    a : float
        The first number to add.
    b : float
        The second number to add.

    Returns
    -------
    float
        The sum of the two numbers.

    Examples
    --------
    >>> add_numbers(3, 5)
    8
    >>> add_numbers(-2, 7)
    5

    """
    return a + b


def sqrt_array(values):
    """Compute the square root of a list of numbers using NumPy.

    Parameters
    ----------
    values : list or float
        A list of non-negative numbers or a single non-negative float.

    Returns
    -------
    numpy.ndarray
        An array with the square root of each input value.

    Raises
    ------
    ValueError
        If any value in the list is negative.

    Examples
    --------
    >>> sqrt_array([4, 9, 16])
    array([2., 3., 4.])

    >>> sqrt_array(9)
    np.float64(3.0)
    """
    arr = np.array(values)
    if np.any(arr < 0):
        raise ValueError("Input contains negative values.")
    return np.sqrt(arr)
