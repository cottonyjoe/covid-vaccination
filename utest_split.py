#!/usr/bin/env python3
# -*- coding: utf8 -*-

import os
import unittest
import split_patients as sp
import json


class TestStringMethods(unittest.TestCase):

    people = []
    people.append({"Name": "Neoma Leong", "Age": 56, "Latitude": "54.88775482346", "Longitude": "-8.167787110571897"})
    people.append({"Name": "Ezequiel Hepfer", "Age": 69, "Latitude": "54.04308476487112", "Longitude": "-7.63487375893224"})
    people.append({"Name": "Lorri Currey", "Age": 25, "Latitude": "54.13644761914938", "Longitude": "-9.48968906074299"})

    # Tests data is read from JSON file
    def test_get_data(self):
        with open('test.txt', 'w') as outfile:
            json.dump(self.people, outfile)
        res = sp.get_data(file='test.txt')
        self.assertEqual(res, self.people)
        os.remove("test.txt")

    # Test result initialization
    def test_initiate_response(self):
        centers = []
        centers.append({"Name": "City Hall Cork", "Latitude": "51.89742637092438", "Longitude": "-8.465763459121026"})
        centers.append({"Name": "Citywest Convention Centre Dublin", "Latitude": "53.28603418885669", "Longitude": "-6.4444477725802285"})
        centers.append({"Name": "Galway Racecourse", "Latitude": "53.298810877564875", "Longitude": "-8.997003657335881"})
        expected_result_list = [\
{"Name": "City Hall Cork", "Customers":[]},\
{"Name": "Citywest Convention Centre Dublin", "Customers":[]},\
{"Name": "Galway Racecourse", "Customers":[]}\
]
        res = sp.initiate_response(centers)
        self.assertEqual(res, expected_result_list)

    # Tests list is sorted by age decreasing (default)
    def test_sort_by_age_default(self):
        res = sp.sort_by_key(self.people)
        sorted_people = []
        sorted_people.append({"Name": "Ezequiel Hepfer", "Age": 69, "Latitude": "54.04308476487112", "Longitude": "-7.63487375893224"})
        sorted_people.append({"Name": "Neoma Leong", "Age": 56, "Latitude": "54.88775482346", "Longitude": "-8.167787110571897"})
        sorted_people.append({"Name": "Lorri Currey", "Age": 25, "Latitude": "54.13644761914938", "Longitude": "-9.48968906074299"})
        self.assertEqual(res, sorted_people)
        self.assertNotEqual(res, self.people)

    # Tests list is sorted by age increasing
    def test_sort_by_age_increasing(self):
        res = sp.sort_by_key(self.people, is_reversed=False)
        sorted_people = []
        sorted_people.append({"Name": "Lorri Currey", "Age": 25, "Latitude": "54.13644761914938", "Longitude": "-9.48968906074299"})
        sorted_people.append({"Name": "Neoma Leong", "Age": 56, "Latitude": "54.88775482346", "Longitude": "-8.167787110571897"})
        sorted_people.append({"Name": "Ezequiel Hepfer", "Age": 69, "Latitude": "54.04308476487112", "Longitude": "-7.63487375893224"})
        self.assertEqual(res, sorted_people)
        self.assertNotEqual(res, self.people)

    # Tests list is sorted by name decreasing
    def test_sort_by_name(self):
        res = sp.sort_by_key(self.people, sorting_key='Name')
        sorted_people = []
        sorted_people.append({"Name": "Neoma Leong", "Age": 56, "Latitude": "54.88775482346", "Longitude": "-8.167787110571897"})
        sorted_people.append({"Name": "Lorri Currey", "Age": 25, "Latitude": "54.13644761914938", "Longitude": "-9.48968906074299"})
        sorted_people.append({"Name": "Ezequiel Hepfer", "Age": 69, "Latitude": "54.04308476487112", "Longitude": "-7.63487375893224"})
        self.assertEqual(res, sorted_people)
        self.assertNotEqual(res, self.people)

    # Tests distance calculation between 2 GPS coordinates
    def test_distance_calculation(self):
        lat1 = 53.297810877564875
        lon1 = -8.997003657335881
        lat2 = 53.09402405506328
        lon2 = -8.020019531250002
        res = round(sp.compute_distance(lat1, lon1, lat2, lon2), 3)
        self.assertEqual(res, 68.935)

    # Test closest center is defined
    def test_get_closest_center(self):
        centers = []
        centers.append({"Name": "City Hall Cork", "Latitude": "51.89742637092438", "Longitude": "-8.465763459121026"})
        centers.append({"Name": "Citywest Convention Centre Dublin", "Latitude": "53.28603418885669", "Longitude": "-6.4444477725802285"})
        centers.append({"Name": "Galway Racecourse", "Latitude": "53.298810877564875", "Longitude": "-8.997003657335881"})
        customer = {"Name": "Neoma Leong", "Age": 56, "Latitude": "54.88775482346", "Longitude": "-8.167787110571897"}
        res = sp.get_closest_center(customer, centers)
        self.assertEqual(res, "Galway Racecourse")

    # Tests customers are grouped with relevant center
    def test_center_filtering(self):
        pass

    # Tests output is in JSON
    def test_output(self):
        pass

if __name__ == '__main__':
    unittest.main()
