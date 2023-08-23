import requests

API_KEY = "2c5274dcfbc419fed8e7064b7af02422"  # Replace with your OpenWeatherMap API key

def get_locations(lat_min, lat_max, lon_min, lon_max):
    url = f"http://api.openweathermap.org/data/2.5/box/city?bbox={lon_min},{lat_min},{lon_max},{lat_max},10&appid={API_KEY}&units=metric"
    response = requests.get(url)
    data = response.json()
    if "list" in data:
        locations = [item["name"] for item in data["list"]]
        print("Locations within the specified bounding box:")
        for location in locations:
            print(location)
    else:
        print("No locations found within the specified bounding box.")

def main():
    lat_min = float(input("Enter the latitude minimum: "))
    lat_max = float(input("Enter the latitude maximum: "))
    lon_min = float(input("Enter the longitude minimum: "))
    lon_max = float(input("Enter the longitude maximum: "))
    get_locations(lat_min, lat_max, lon_min, lon_max)

if __name__ == "__main__":
    main()
