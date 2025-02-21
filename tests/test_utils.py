import unittest
from weather.utils import display_weather
from io import StringIO
import sys

class TestUtils(unittest.TestCase):
    def test_display_weather(self):
        weather_data = {
            'name': 'London',
            'main': {'temp': 15, 'humidity': 80},
            'weather': [{'description': 'clear sky'}],
            'wind': {'speed': 3.5}
        }
        expected_output = (
            "Weather in London:\n"
            "Temperature: 15°C\n"
            "Description: clear sky\n"
            "Humidity: 80%\n"
            "Wind Speed: 3.5 m/s\n"
        )
        
        captured_output = StringIO()
        sys.stdout = captured_output
        display_weather(weather_data)
        sys.stdout = sys.__stdout__
        
        self.assertEqual(captured_output.getvalue(), expected_output)

if __name__ == '__main__':
    unittest.main()