import requests

API_KEY = "2c5274dcfbc419fed8e7064b7af02422"  # Replace with your OpenWeatherMap API key

def get_europe_regions():
    lat_north = 71.0  # Northernmost latitude for Europe
    lat_south = 35.0  # Southernmost latitude for Europe
    lon_west = -23.0  # Westernmost longitude for Europe
    lon_east = 45.0  # Easternmost longitude for Europe

    url = f"http://api.openweathermap.org/data/2.5/box/city?bbox={lon_west},{lat_south},{lon_east},{lat_north},10&appid={API_KEY}&units=metric"
    response = requests.get(url)
    data = response.json()
    if data["count"] > 0:
        regions = [item["name"] for item in data["list"]]
        print("Regions in Europe:")
        for region in regions:
            print(region)
    else:
        print("No regions found in Europe.")

def main():
    get_europe_regions()

if __name__ == "__main__":
    main()


