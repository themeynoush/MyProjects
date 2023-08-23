import requests

API_KEY = "2c5274dcfbc419fed8e7064b7af02422"  # Replace with your OpenWeatherMap API key

def get_region_name(lat, lon):
    url = f"http://api.openweathermap.org/geo/1.0/reverse?lat={lat}&lon={lon}&limit=1&appid={API_KEY}"
    response = requests.get(url)
    data = response.json()
    if data:
        region_name = data[0]["name"]
        print("Region name:")
        print(region_name)
    else:
        print("No region found for the specified coordinates.")

def main():
    lat = float(input("Enter latitude value: "))
    lon = float(input("Enter longitude value: "))
    get_region_name(lat, lon)

if __name__ == "__main__":
    main()
