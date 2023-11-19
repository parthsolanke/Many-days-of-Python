import requests

# requesting data from the API
response = requests.get(url="http://api.open-notify.org/iss-now.json")
# using method raise_for_status() to check for errors
response.raise_for_status()

# getting the data in json format
original_response = response.json()
print(f"Original response: {original_response}")

position_data = response.json()["iss_position"]
print(f"Position data: {position_data}")

latitude = position_data["latitude"]
longitude = position_data["longitude"]
print(f"Latitude: {latitude}")
print(f"Longitude: {longitude}")
