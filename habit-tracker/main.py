

import requests
from datetime import datetime
pixela_endpoint = "https://pixe.la/v1/users"
USERNAME = "xxxxxxxxx"
TOKEN = "xxxxxxx"
GRAPH_ID = "graph1"
user_params = {
    "token": "xxxxxxx",
    "username": "xxxxxxx",
    "agreeTermsOfService": "yes",
    "notMinor": "yes",

}

# response = requests.post(url=pixela_endpoint,json=user_params)
# response.raise_for_status()
# print(response.text)


graph_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs"

graph_config = {
    "id": "graph1",
    "name": "Coding graph",
    "unit": "hours",
    "type": "int",
    "color": "sora",
}

headers = {
    "X-USER-TOKEN": TOKEN
}

# response_graph = requests.post(url=graph_endpoint, json=graph_config, headers=headers)
# print(response_graph.text)

dot_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}"
today = datetime.now()
TODAY = today.strftime("%Y%m%d")

dot_config = {
    "date": TODAY,
    "quantity": input("How long did you code? "),
}





dot_response = requests.post(url=dot_endpoint, json=dot_config, headers=headers)
print(dot_response.text)

update_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}/{TODAY}"

# update_response = requests.delete(url=update_endpoint,headers=headers)
# print(update_response.text)
