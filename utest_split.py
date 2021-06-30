#!/usr/bin/env python3
# -*- coding: utf8 -*-

import unittest
import split_patients as sp
import json

class TestStringMethods(unittest.TestCase):

    people = []
    people.append({"Name": "Neoma Leong","Age": 56,"Latitude": "54.88775482346","Longitude": "-8.167787110571897" })
    people.append({"Name": "Ezequiel Hepfer","Age": 69,"Latitude": "54.04308476487112","Longitude": "-7.63487375893224" })
    people.append({"Name": "Lorri Currey","Age": 25,"Latitude": "54.13644761914938","Longitude": "-9.48968906074299" })

    # Tests data is read from JSON file
    def test_get_data(self):
        with open('test.txt', 'w') as outfile:
            json.dump(self.people, outfile)
        res = sp.get_data(file='test.txt')
        self.assertEqual(res, self.people)

    # Tests list is sorted by age decreasing (default)
    def test_sort_by_age_default(self):
        res = sp.sort_by_key(self.people)
        sorted_people = []
        sorted_people.append({"Name": "Ezequiel Hepfer","Age": 69,"Latitude": "54.04308476487112","Longitude": "-7.63487375893224" })
        sorted_people.append({"Name": "Neoma Leong","Age": 56,"Latitude": "54.88775482346","Longitude": "-8.167787110571897" })
        sorted_people.append({"Name": "Lorri Currey","Age": 25,"Latitude": "54.13644761914938","Longitude": "-9.48968906074299" })
        self.assertEqual(res, sorted_people)
        self.assertNotEqual(res, self.people)

    # Tests list is sorted by age increasing
    def test_sort_by_age_increasing(self):
        res = sp.sort_by_key(self.people, is_reversed=False)
        sorted_people = []
        sorted_people.append({"Name": "Lorri Currey","Age": 25,"Latitude": "54.13644761914938","Longitude": "-9.48968906074299" })
        sorted_people.append({"Name": "Neoma Leong","Age": 56,"Latitude": "54.88775482346","Longitude": "-8.167787110571897" })
        sorted_people.append({"Name": "Ezequiel Hepfer","Age": 69,"Latitude": "54.04308476487112","Longitude": "-7.63487375893224" })
        self.assertEqual(res, sorted_people)
        self.assertNotEqual(res, self.people)

    # Tests list is sorted by name decreasing
    def test_sort_by_name(self):
        res = sp.sort_by_key(self.people, sorting_key='Name')
        sorted_people = []
        sorted_people.append({"Name": "Neoma Leong","Age": 56,"Latitude": "54.88775482346","Longitude": "-8.167787110571897" })
        sorted_people.append({"Name": "Lorri Currey","Age": 25,"Latitude": "54.13644761914938","Longitude": "-9.48968906074299" })
        sorted_people.append({"Name": "Ezequiel Hepfer","Age": 69,"Latitude": "54.04308476487112","Longitude": "-7.63487375893224" })
        self.assertEqual(res, sorted_people)
        self.assertNotEqual(res, self.people)


    # Tests distance calculation between 2 GPS coordinates
    def test_distance_calculation(self):
        pass

    # Tests customers are grouped with relevant center
    def test_center_filtering(self):
        pass

    # Tests output is in JSON
    def test_output(self):
        pass

if __name__ == '__main__':
    unittest.main()