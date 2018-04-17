import json
import requests


def get_some_details():

    json_data = open("/lazyduck.json").read()

    data = json.loads(json_data)
    print (data)



