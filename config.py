from dotenv import load_dotenv
import os

# Load environment variables from .env file
load_dotenv()

API_KEY = os.getenv('WEATHER_API_KEY')
BASE_URL = 'http://api.openweathermap.org/data/2.5/weather'

if not API_KEY:
    raise ValueError("No API key set for the weather service. Please set the WEATHER_API_KEY environment variable.")