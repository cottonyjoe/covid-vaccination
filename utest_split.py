#!/usr/bin/env python3
# -*- coding: utf8 -*-

import unittest
import split_patients as sp

class TestStringMethods(unittest.TestCase):

    # Test input file reading function
    def test_read_file(self):
        pass

    # Test not JSON file raises an error
    def test_get_json(self):
        pass

    # Test list is sorted by age descreasing
    def test_sort_by_age(self):
        pass

    # Test distance calculation between 2 GPS coordinates
    def test_distance_calculation(self):
        pass

    # Test customers are grouped with relevant center
    def test_center_filtering(self):
        pass

    # Test output is in JSON
    def test_output(self):
        pass

if __name__ == '__main__':
    unittest.main()