# COVID-19 vaccination challenge

This (small) project contains a python script to spread a list of individuals per age priority (assuming elders have higher priority) and grouped by vaccination center, each customer attached to its closest center.

## Prerequisites

To work fine, the script requires 2 files:
 - People.txt: JSON file containing a list of individuals details, such as name, age and GPS coordinates; it must have the following format:
    [
        {"Name": <str>, "Age": <int>, "Latitude": <str>,"Longitude": <str> },
    ]

   Example:
    [
        {"Name": "John Doe","Age": 59,"Latitude": "53.09402405506328","Longitude": "-8.020019531250002" },
        {"Name": "Jane Dah","Age": 47,"Latitude": "52.53627304145948","Longitude": "-6.822509765625001" }
    ]

 - centerList.txt: JSON file containing a list of vaccination center details, such as name and GPS coordinates; it must have the following format:
    [
        {"Name": <str>, "Latitude": <str>,"Longitude": <str> },
    ]

   Example:
    [
        {"Name": "Galway Racecourse", "Latitude": "53.298810877564875", "Longitude": "-8.997003657335881"},
        {"Name": "City Hall Cork", "Latitude": "51.89742637092438", "Longitude": "-8.465763459121026"}
    ]

These files must be put at the same place than split_patients.py

## Execute

To have the list of customers ordered and grouped by vaccination center, simply run split_patients.py.
This file can also be used as a module from another Python and method split_patients() will return a list of customers grouped by center, in JSON format.

`$ python ./split_patients.py`

## Output

The output is a JSON data with following format:
[
    {"Name": <str>, "Customers":[
        {"Name": <str>, "Age": <int>, "Latitude": <str>, "Longitude": <str>},
        ...
    ]}
]

## Unit tests

The script is covered by unit tests.
Those tests can be run:

`$ python ./utest_split.py`

## Disclaimer

This script can widely be improved in term of error management. Any issue in input files will cause the script to crash with ugly error message.