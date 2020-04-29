import json
import os

def write_config(fName, data):
    if os.path.exists(fName):
        with open(fName, 'w') as jsonfile:
            try:
                json.dump(data, jsonfile)
            except IOError:
                print("Error")
            finally:
                jsonfile.close()

def read_config(fName):
    if os.path.exists(fName):
        with open(fName, 'r') as jsonfile:
            try:
                data = json.load(jsonfile)
                return data
            except IOError:
                print("Error")
            finally:
                jsonfile.close()

def change_global_rules():
    pass