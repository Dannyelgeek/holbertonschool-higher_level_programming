#!/usr/bin/python3
'''Writes an Object to a text file.'''
import json


def save_to_json_file(my_obj, filename):
    '''Using a JSON representation'''
    with open(filename, mode="w", encoding="UFT-8") as saveFile:
        json.dump(my_obj, saveFile)
