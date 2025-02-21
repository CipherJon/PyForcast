from weather.api import get_weather
from weather.utils import display_weather

def main():
    city = input("Enter city name: ")
    weather_data = get_weather(city)
    if weather_data:
        display_weather(weather_data)
    else:
        print("Failed to retrieve weather data.")

if __name__ == "__main__":
    main()