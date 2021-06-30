#!/usr/bin/env python3
# -*- coding: utf8 -*-

import json

# This script will read a list of patients from a JSON file and split them into
# groups according to their nearest vaccination center and sorted by age.

# Global variables
input_file = 'People.txt'

# Sorts a list of dict according to an optional key; this can be reversed.
# @param list A list of dict objects to sort.
# @param string The key to sort on. Default value is 'Age'.
# @param boolean Set if sort must be reversed or not. Default is True.
def sort_by_key(data, sorting_key='Age', is_reversed=True):
    return sorted(data, key=lambda k: k[sorting_key], reverse=is_reversed) 

# Main function
def main():
    # Opening JSON file
    f = open(input_file)
      
    # Returns JSON object as a dictionary
    data = json.load(f)

    # Closing file
    f.close()

    # Sorts data by priority

    # Splits individuals by center
    # for each customer
    # get closest center

    # adds him/her to relevant group

    # Changes to JSON

    # Returns result
    pass

if __name__ == "__main__":
    # execute only if run as a script
    main()