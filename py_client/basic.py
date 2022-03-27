import requests

endpoint = "https://httpbin.org"
endpoint_status = "https://httpbin.org/status/200"
endpoint_anything = "https://httpbin.org/anything"

get_response = requests.get(endpoint_anything, json={
                            "query": "Hello World"})  # API -> Method

print(get_response.json())  # Print whatever the Rest API returns
