import requests


# Function to check for recent earthquakes near a given location
def check_earthquakes_near_location(latitude, longitude, radius_km=100, min_magnitude=4.0):
    base_url = "https://earthquake.usgs.gov/fdsnws/event/1/query"

    # Define parameters for the API request
    params = {
        "format": "geojson",
        "latitude": latitude,
        "longitude": longitude,
        "maxradius": radius_km,
        "minmagnitude": min_magnitude,
    }

    try:
        response = requests.get(base_url, params=params)
        response.raise_for_status()
        earthquake_data = response.json()

        if earthquake_data.get("features"):
            print("Recent earthquakes near the specified location:")
            for earthquake in earthquake_data["features"]:
                properties = earthquake["properties"]
                mag = properties["mag"]
                place = properties["place"]
                time = properties["time"]
                print(f"Magnitude {mag} - {place} - {time}")
        else:
            print("No recent earthquakes found near the specified location.")

    except requests.exceptions.RequestException as e:
        print(f"Error fetching earthquake data: {e}")


# Get user input for latitude and longitude
try:
    latitude = float(input("Enter latitude: "))
    longitude = float(input("Enter longitude: "))
    check_earthquakes_near_location(latitude, longitude)
except ValueError:
    print("Invalid latitude or longitude input. Please enter numeric values.")