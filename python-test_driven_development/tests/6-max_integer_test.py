#!/usr/bin/python3
"""Unittest for max_integer([..])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):
    """Test cases for the max_integer function"""

    def test_ordered_list(self):
        """Test an ordered list"""
        self.assertEqual(max_integer([1, 2, 3, 4]), 4)

    def test_unordered_list(self):
        """Test an unordered list"""
        self.assertEqual(max_integer([1, 3, 4, 2]), 4)

    def test_max_at_start(self):
        """Test when max is at the start"""
        self.assertEqual(max_integer([5, 1, 2]), 5)

    def test_max_at_end(self):
        """Test when max is at the end"""
        self.assertEqual(max_integer([1, 2, 6]), 6)

    def test_empty_list(self):
        """Test empty list returns None"""
        self.assertIsNone(max_integer([]))

    def test_single_element(self):
        """Test list with single element"""
        self.assertEqual(max_integer([7]), 7)

    def test_floats(self):
        """Test list with floats"""
        self.assertEqual(max_integer([1.5, 2.5, 0.5]), 2.5)

    def test_mixed_int_float(self):
        """Test list with ints and floats"""
        self.assertEqual(max_integer([1, 2.5, 3]), 3)

    def test_negative_numbers(self):
        """Test list with negative numbers"""
        self.assertEqual(max_integer([-1, -2, -3, -4]), -1)

    def test_all_equal(self):
        """Test list with all equal numbers"""
        self.assertEqual(max_integer([2, 2, 2]), 2)
