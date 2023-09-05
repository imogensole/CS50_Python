import requests 
import sys 
import json

# GOAL: use the itunes API to gain info about a given artist 

# error checking 
# Checks if the input length is correct 
if len(sys.argv) != 2:
    # if not exits the programme 
    sys.exit()

# Gets the data from the itunes API
# Allows user to input desired artist in the command line 
response = requests.get("https://itunes.apple.com/search?entity=song&limit=50&term=" + sys.argv[1])

# prints the response in json format 
# dumps function formats the json nicely
#print(json.dumps(response.json(), indent=2))

# GOAL: get the songs by a specified artist 

# store the response in the variable
o = response.json()

# iterate over each result found
for result in o["results"]:
    # prints the track name for that result 
    print(result["trackName"])


