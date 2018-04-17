import json
from pprint import pprint



#print (data['results'][0]["name"]["last"])
#print (data['results'][0]["login"]["password"])




def get_some_details():

    data = json.load(open('lazyduck.json'))
    result = data["results"][0]
    return {"lastName":       result["name"]["last"],
            "password":       result["login"]["password"],
            "postcodePlusID": result["location"]["postcode"] +
            int(result["id"]["value"])
            }

print (get_some_details())