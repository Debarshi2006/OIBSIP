import os
import requests
from dotenv import load_dotenv

load_dotenv()

def get_weather(city_name):
    
    api_key = os.getenv("WEATHER_API_KEY")
    base_url = "http://api.openweathermap.org/data/2.5/weather"
    
    params = {
        "q": city_name,
        "appid": api_key,
        "units": "metric"
    }

    try:
        response = requests.get(base_url, params=params)
        response.raise_for_status()
        
        data = response.json()

        temp = data['main']['temp']
        humidity = data['main']['humidity']
        desc = data['weather'][0]['description']
        city = data['name']
        country = data['sys']['country']

        print("-" * 30)
        print(f"Weather in {city_name}, {country}:")
        print(f"Temperature: {temp}°C")
        print(f"Humidity:    {humidity}%")
        print(f"Conditions:  {desc.capitalize()}")
        print("-" * 30)

    except requests.exceptions.HTTPError:
        print("Error: City not found. Please check the spelling.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    print("--- Python Command-Line Weather App ---")
    user_city = input("Enter a city name or ZIP code: ")
    get_weather(user_city)