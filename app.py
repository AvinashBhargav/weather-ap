import requests
import json

def get_weather(city):
    api_key = 'YOUR_API_KEY'  # Replace with your OpenWeatherMap API key
    base_url = 'http://api.openweathermap.org/data/2.5/weather'
    params = {'q': city, 'appid': api_key, 'units': 'metric'}

    response = requests.get(base_url, params=params)
    weather_data = json.loads(response.text)

    if weather_data['cod'] == '404':
        print("City not found.")
        return

    temperature = weather_data['main']['temp']
    description = weather_data['weather'][0]['description']
    humidity = weather_data['main']['humidity']
    wind_speed = weather_data['wind']['speed']

    print(f"Weather in {city}:")
    print(f"Temperature: {temperature}°C")
    print(f"Description: {description}")
    print(f"Humidity: {humidity}%")
    print(f"Wind Speed: {wind_speed} m/s")

# User input
city_name = input("Enter the city name: ")

# Get weather information
get_weather(city_name)
