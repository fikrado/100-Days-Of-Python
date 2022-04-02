import requests
from datetime import datetime

today = datetime.now()
pixela_endpoint = "https://pixe.la/v1/users"
username = "fikrado2"
token = "ldhfakfda8f97a9d237a99ad9a7"

user_params = {
    "token": username,
    "username": token,
    "agreeTermsOfService": "yes",
    "notMinor": "yes"

}

# this for creating new user
# r = requests.post(url=pixela_endpoint, json=user_params)
# print(r.text)

#
# graph = f"{pixela_endpoint}/{username}/graphs"
# graph_config = {
#     "id": "super1",
#     "name": "Cycling Graph",
#     "unit": "Km",
#     "type": "float",
#     "color": "ajisai"
#
#
# }
#
headers = {
    "X-USER-TOKEN": token

}
#
# r = requests.post(url=graph, json=graph_config, headers=headers)
# print(r.text)

graph_edit = f"https://pixe.la/v1/users/fikrado2/graphs/super1/{today}"
graph = f"{pixela_endpoint}/{username}/graphs"
gra = {
    "quantity": "87",
}

r = requests.post(url=graph_edit, json=gra, headers=headers)
print(r.text)
