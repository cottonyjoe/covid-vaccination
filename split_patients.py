#!/usr/bin/env python3
# -*- coding: utf8 -*-

import json

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

# Sorts a list of dict objects according to an optional key; this can be reversed.
# @param list A list of dict objects to sort.
# @param string The key to sort on; optional, default value is 'Age'.
# @param boolean Set if sort must be reversed or not; optional, default is True.
# @return list Sorted list of dict objects
def sort_by_key(data, sorting_key='Age', is_reversed=True):
    return sorted(data, key=lambda k: k[sorting_key], reverse=is_reversed) 

def get_closest_center(customer, center_data):
    pass

# Main function
def main():
    # Gets customer data
    data = get_data(input_file)
    # Gets center list
    center_data = get_data(center_list)

    # Sorts data by priority
    sorted_data = sort_by_key(data, sorting_key='Age', is_reversed=True)

    # Splits individuals by center
    # for each customer
    for customer in sorted_data:
        # get closest center
        vacc_center = get_closest_center(customer, center_data)
        # adds him/her to relevant group

    # Changes to JSON

    # Returns result
    return

if __name__ == "__main__":
    # execute only if run as a script
    main()