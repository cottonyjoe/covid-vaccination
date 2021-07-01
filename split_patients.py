#!/usr/bin/env python3
# -*- coding: utf8 -*-

import json
import math

# This script will read a list of patients from a JSON file and split them into
# groups according to their nearest vaccination center and sorted by age.

# Global variables
input_file = 'People.txt'
center_list = 'centerList.txt'


# Read data from file
# @param string File name; optional, default is input_file global var value
# @return list The list of customers as a list of dict objects.
def get_data(file=input_file):
    # Opening JSON file
    f = open(file)

    # Returns JSON object as a dictionary
    data = json.load(f)

    # Closing file and returns
    f.close()
    return data


# Sorts a list of dict objects according to an optional key; this can be
# reversed.
# @param list A list of dict objects to sort.
# @param string The key to sort on; optional, default value is 'Age'.
# @param boolean Sets if sort must be reversed or not; optional, default is
#                True.
# @return list Sorted list of dict objects
def sort_by_key(data, sorting_key='Age', is_reversed=True):
    return sorted(data, key=lambda k: k[sorting_key], reverse=is_reversed)


def computation_formula(lat1, long1, lat2, long2):
    res = 2 * math.asin(math.sqrt(math.pow(, 2)))
    return


# Gets the closest vaccination center from a customer
# @param dict Customer object with Name, Age, Latitude and Longitude data.
# @param dict Vaccination centers list of dict with Name, Latitude and
#             Longitude data.
def get_closest_center(customer, center_data):
    pass


# Main function
def main():
    # Gets customer data
    data = get_data(file=input_file)
    # Gets center list
    center_data = get_data(file=center_list)

    # Sorts data by priority
    sorted_data = sort_by_key(data, sorting_key='Age', is_reversed=True)

    # Splits individuals by center
    grouped_result_list = []
    # for each customer
    for customer in sorted_data:
        # get closest center
        vacc_center = get_closest_center(customer, center_data)
        # adds him/her to relevant group

    # Changes to JSON

    # Returns result
    return json.dumps(grouped_result_list)

if __name__ == "__main__":
    # execute only if run as a script
    main()
