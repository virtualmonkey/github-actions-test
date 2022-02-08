from ast import Raise
import sys
import json

percentage = 0
threshold = 0

path = (sys.argv)[1]
threshold = (sys.argv)[2]

try: 
    file = open(path)
    data = json.load(file)
    percentage = data['total']['lines']['pct']
except:
    raise Exception("Couldn't parse JSON file")

if (float(percentage) < float(threshold)):
    raise Exception

print("Everything worked properly")
 
file.close()