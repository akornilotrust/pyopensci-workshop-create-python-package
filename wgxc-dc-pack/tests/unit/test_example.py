"""
A test module that tests your example module.

Some people prefer to write tests in a test file for each function or
method/ class. Others prefer to write tests for each module. That decision
is up to you. This test example provides a single test for the example.py
module.
"""

import numpy as np
import pytest
from ak_wgxc_dc.example import sqrt_array, add_numbers


def test_add_numbers():
    """
    Test that add_numbers works as expected.

    A single line docstring for tests is generally sufficient.
    """
    out = add_numbers(1, 2)
    expected_out = 3
    assert  out == expected_out, f"Expected {expected_out} but got {out}"

def test_sqrt_array_float():
    result = sqrt_array(9)
    assert result == np.float64(3.0)

def test_sqrt_array():
    result = sqrt_array([4, 9, 16])
    expected = np.array([2.0, 3.0, 4.0])
    np.testing.assert_array_equal(result, expected)


def test_sqrt_array_with_zero():
    result = sqrt_array([0, 1])
    expected = np.array([0.0, 1.0])
    np.testing.assert_array_equal(result, expected)


def test_sqrt_array_negative_raises():
    with pytest.raises(ValueError, match="negative"):
        sqrt_array([-1, 4, 9])