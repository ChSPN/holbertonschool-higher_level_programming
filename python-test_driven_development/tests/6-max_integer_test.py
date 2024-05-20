#!/usr/bin/python3
"""Unittest for max_integer([..])"""
import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):
    def test_empty_list(self):
        """Test with an empty list"""
        self.assertIsNone(max_integer([]))

    def test_single_element_list(self):
        """Test with a list of one element"""
        self.assertEqual(max_integer([1]), 1)

    def test_same_element_list(self):
        """Test with a list of identical elements"""
        self.assertEqual(max_integer([1, 1, 1, 1]), 1)

    def test_sorted_list(self):
        """Test with a list sorted in ascending order"""
        self.assertEqual(max_integer([1, 2, 3, 4]), 4)

    def test_reverse_sorted_list(self):
        """Test with a list sorted in descending order"""
        self.assertEqual(max_integer([4, 3, 2, 1]), 4)


if __name__ == '__main__':
    unittest.main()
