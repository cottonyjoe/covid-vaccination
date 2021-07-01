#!/usr/bin/env python3
# -*- coding: utf8 -*-

import json
from math import sin, cos, sqrt, atan2, asin, radians

# This script will read a list of patients from a JSON file and split them into
# groups according to their nearest vaccination center and sorted by age.

# Global variables
input_file = 'People.txt'
center_list = 'centerList.txt'


# Read data from file.
# @param string File name; optional, default is input_file global var value.
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


# Computes distance between 2 GPS coordinates at the surface og the Earth.
# Formula taken from https://en.wikipedia.org/wiki/Great-circle_distance
# @param float GPS latitude of the source.
# @param float GPS longitude of the source.
# @param float GPS latitude of the destination.
# @param float GPS longitude of the destination.
# @return float Distance in km.
def compute_distance(lat1, lon1, lat2, lon2):
    # Rough estimation of Earth's radius
    R = 6373.0

    # Converts all coodinates to radians
    r_lat1 = radians(lat1)
    r_lon1 = radians(lon1)
    r_lat2 = radians(lat2)
    r_lon2 = radians(lon2)

    # Calculate deltas
    dlon = r_lon2 - r_lon1
    dlat = r_lat2 - r_lat1

    # Implement actual formula
    a = sin(dlat / 2)**2 + cos(r_lat1) * cos(r_lat2) * sin(dlon / 2)**2
    c = 2 * asin(sqrt(a))
    distance = R * c

    return distance


# Gets the closest vaccination center from a customer.
# @param dict Customer object with Name, Age, Latitude and Longitude data.
# @param dict Vaccination centers list of dict with Name, Latitude and
#             Longitude data.
# @return string Name of the closest vaccination center from the customer.
def get_closest_center(customer, center_data):
    # Initiates few parameters
    nearest = 40000  # Very far center
    name = ''
    # Customer coordinates
    lat1 = customer['Latitude']
    if isinstance(lat1, str):
        lat1 = float(lat1)
    lon1 = customer['Longitude']
    if isinstance(lon1, str):
        lon1 = float(lon1)

    # For each vaccination center, find the closest from the customer
    for center in center_data:
        # Gets latitude and longitude from obj and convert them to float
        # if necessary.
        lat2 = center['Latitude']
        if isinstance(lat2, str):
            lat2 = float(lat2)
        lon2 = center['Longitude']
        if isinstance(lon2, str):
            lon2 = float(lon2)

        # Compute distance between GPS locations
        distance = compute_distance(lat1, lon1, lat2, lon2)

        # If closer, store it
        if distance < nearest:
            nearest = distance
            name = center['Name']

    return name


# Fills the result array with customers. Adds customer to its relevant
# vaccination center.
# @param dict Customer to add.
# @param string Vaccination to link with customer.
# @param list List of center and ordered customer.
def dispatch_customer(customer, vacc_center, grouped_result_list):
    center_index = next((
        index for (index, d) in enumerate(grouped_result_list)
        if d["Name"] == vacc_center), None)
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
        grouped_result_list = dispatch_customer(
            customer, vacc_center, grouped_result_list)

    # Returns result as JSON
    return json.dumps(grouped_result_list)

if __name__ == "__main__":
    # execute only if run as a script
    main()
