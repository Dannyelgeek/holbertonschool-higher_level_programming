#!/usr/bin/python3
'''creates an Object from a “JSON file”'''
import json


def load_from_json_file(filename):
    '''Returns the created object.'''
    with open(filename) as readFile:
        return json.load(readFile)
