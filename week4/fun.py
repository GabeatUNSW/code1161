import json
config = json.loads(open("lazyduck.json").read())

print (type (config))
print (config['results'])

#last name
#password
#and the number you get when you add the postcode to the id-value.
