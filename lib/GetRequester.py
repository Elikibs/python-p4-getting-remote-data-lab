import requests
import json

# General class for getting nd working with API data
class GetRequester:
    def __init__(self, url):
        self.url = url

    def get_response_body(self):
        response = requests.get(self.url)
        return response.content

    def load_json(self):
        workers_list = []
        workers = json.loads(self.get_response_body())
        
        for worker in workers:
            workers_list.append(f'Name; {worker["name"]} Occupation; {worker["occupation"]}')
        
        return workers_list

get_requester = GetRequester("https://learn-co-curriculum.github.io/json-site-example/endpoints/people.json")
workers_list_output = get_requester.load_json()

for worker in workers_list_output:
    print(worker)