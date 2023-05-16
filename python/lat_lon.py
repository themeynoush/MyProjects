import requests

API_KEY = "2c5274dcfbc419fed8e7064b7af02422"  # Replace with your OpenWeatherMap API key

def get_city_names(lat, lon):
    url = f"http://api.openweathermap.org/data/2.5/find?lat={lat}&lon={lon}&cnt=10&appid={API_KEY}&units=metric"
    response = requests.get(url)
    data = response.json()
    if data["count"] > 0:
        cities = [item["name"] for item in data["list"]]
        print(f"City names near the coordinates ({lat}, {lon}):")
        for city in cities:
            print(city)
    else:
        print("No cities found for the specified coordinates.")

def main():
    lat = float(input("Enter latitude value: "))
    lon = float(input("Enter longitude value: "))
    get_city_names(lat, lon)

if __name__ == "__main__":
    main()
