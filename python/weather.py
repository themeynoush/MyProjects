import requests

API_KEY = "2c5274dcfbc419fed8e7064b7af02422"  # Replace with your OpenWeatherMap API key

def get_weather(city):
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric"
    response = requests.get(url)
    data = response.json()
    if data["cod"] == 200:
        feels_like = data["main"]["feels_like"]
        print(f"The 'feels like' temperature in {city} is {feels_like}°C.")
    else:
        print("Error retrieving weather information.")

def main():
    city = input("Enter the name of a city: ")
    get_weather(city)

if __name__ == "__main__":
    main()


