import requests

API_KEY = "2c5274dcfbc419fed8e7064b7af02422"  # Replace with your OpenWeatherMap API key

def get_cities_with_temperature(temp_min, temp_max):
    lat_min = 36.0  # Latitude minimum for Europe
    lat_max = 71.0  # Latitude maximum for Europe
    lon_min = -11.0  # Longitude minimum for Europe
    lon_max = 42.0  # Longitude maximum for Europe
    
    url = f"http://api.openweathermap.org/data/2.5/box/city?bbox={lon_min},{lat_min},{lon_max},{lat_max},50&appid={API_KEY}&units=metric"
    url = f"http://api.openweathermap.org/data/2.5/box/city?bbox={lon_min},36,{lon_max},{lat_max},50&appid={API_KEY}&units=metric"

    response = requests.get(url)
    data = response.json()
    if data["cod"] == 200 and data["cnt"] > 0:
        cities = []
        for item in data["list"]:
            temp = item["main"]["temp"]
            if temp_min <= temp <= temp_max:
                city = item["name"]
                cities.append(city)
        if cities:
            print(f"Cities with temperatures between {temp_min}°C and {temp_max}°C in the world:")
            for city in cities:
                print(city)
        else:
            print("No cities found within the specified temperature range in the world.")
    else:
        print("Error retrieving weather information.")

def main():
    temp_min = float(input("Enter the minimum temperature (in °C): "))
    temp_max = float(input("Enter the maximum temperature (in °C): "))
    get_cities_with_temperature(temp_min, temp_max)

if __name__ == "__main__":
    main()
