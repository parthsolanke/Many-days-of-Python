import os
import requests
import datetime as dt

USERNAME = "parthsolanke"
GRAPHID = "graph1"
PIXELA_TOKEN = os.environ["PIXELA_TOKEN"]
current_date = dt.datetime.now().strftime("%Y%m%d") # strftime is used to format the date in the given format
pixela_endpoint = "https://pixe.la/v1/users"
graph_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs"
pixel_creation_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPHID}"
pixel_update_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPHID}/{current_date}"
delete_pixel_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPHID}/{current_date}"


user_params = {
    "token": PIXELA_TOKEN,
    "username": USERNAME,
    "agreeTermsOfService": "yes",
    "notMinor": "yes",
}

graph_config = {
    "id": GRAPHID,
    "name": "Habit Tracker",
    "unit": "hours",
    "type": "float",
    "color": "shibafu",
}

pixel_data = {
    "date": current_date,
    "quantity": input("How many hours did you code today? "),
    
}

pixel_update_data = {
    "quantity": "2",
}

# # creating user (POST)
# response = requests.post(url=pixela_endpoint, json=user_params)
# print(response.text)

# # creating graph (POST)
# # creating a header for X-USER-TOKEN
headers = {
    "X-USER-TOKEN": PIXELA_TOKEN,
}
# response = requests.post(url=graph_endpoint, json=graph_config, headers=headers)
# print(response.text)

# creating a pixel (POST)
response = requests.post(url=pixel_creation_endpoint, json=pixel_data, headers=headers)
print(response.text)

# # updating a pixel (PUT)
# response = requests.put(url=pixel_update_endpoint, json=pixel_update_data, headers=headers)
# print(response.text)

# # deleting a pixel (DELETE)
# response = requests.delete(url=delete_pixel_endpoint, headers=headers)
# print(response.text)
