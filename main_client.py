import requests
import json

page = 'http://127.0.0.1:5000'

def auto_request(message:str, page:str = "",*, data = dict()):
    r = requests.get(page, data=json.dumps(data))
    _dict = r.json()

    print(message)
    print("%i results" % (len(_dict)))
    print("")

    return _dict

print("")

_search_results = auto_request("Blank GET request:", page)
_valid_id = _search_results[0]["id"]

auto_request("GET request with blank id:", page, data={"id": ""})

auto_request("GET request with invalid id:", page, data={"id": "-1"})

auto_request("GET request with valid id:", page, data={"id": _valid_id})

auto_request("Search Calories = 120:", page + '/results?calories=120')

auto_request("Search Fiber >= 6:", page + '/results?min_fiber=6')

auto_request("Search Fiber >= 6:", page + '/results?min_fiber=6')

auto_request("Search Sodium = 0 && Calories = 100:", page + '/results?sodium=0&calories=100')
