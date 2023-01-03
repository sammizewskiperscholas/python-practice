import json
import requests
#from pprint import pp

data={ "user"} : {
    "name" :    "William Williams",
     "age" : 98
}
with open ("data_file.json","w")as write_file:
    json.dump(data,write_file,indent=4)


