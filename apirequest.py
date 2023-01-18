import requests

baseurl = 'https://rickandmortyapi.com/api/'

endpoint = 'character'

def main_request(baseurl, endpoint):
    r = requests.get(baseurl + endpoint)
    return r.json()

def get_pages(response):
    return response['info']['pages']

def parse_json(response):
    charlist = []
    for item in response['results']:
        char = {
            'name': item['name'],
            'no_ep': len(item['episode']),
        }
        charlist.append(char)
    return charlist
 
data = main_request(baseurl, endpoint)
print(get_pages(data))
print(parse_json(data))

