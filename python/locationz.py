import requests

API_KEY = "2c5274dcfbc419fed8e7064b7af02422"  # Replace with your OpenWeatherMap API key

def get_cities_with_temperature(temp_min, temp_max):
    url = f"http://api.openweathermap.org/data/2.5/find?lat=55.5&lon=37.5&cnt=10&appid={API_KEY}&units=metric"
    response = requests.get(url)
    data = response.json()
    if data["count"] > 0:
        cities = []
        for item in data["list"]:
            temp = item["main"]["temp"]
            if temp_min <= temp <= temp_max:
                city = item["name"]
                cities.append(city)
        if cities:
            print(f"Cities with temperatures between {temp_min}°C and {temp_max}°C:")
            for city in cities:
                print(f"{city}: {temp}°C")
        else:
            print("No cities found within the specified temperature range.")
    else:
        print("Error retrieving weather information.")

def main():
    temp_min = float(input("Enter the minimum temperature (in °C): "))
    temp_max = float(input("Enter the maximum temperature (in °C): "))
    get_cities_with_temperature(temp_min, temp_max)

if __name__ == "__main__":
    main()