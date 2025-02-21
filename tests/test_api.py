import unittest
from unittest.mock import patch
from weather.api import get_weather

class TestApi(unittest.TestCase):
    @patch('weather.api.requests.get')
    def test_get_weather(self, mock_get):
        mock_response = {
            'name': 'London',
            'main': {'temp': 15, 'humidity': 80},
            'weather': [{'description': 'clear sky'}],
            'wind': {'speed': 3.5}
        }
        mock_get.return_value.status_code = 200
        mock_get.return_value.json.return_value = mock_response
        
        city = 'London'
        weather_data = get_weather(city)
        
        self.assertIsNotNone(weather_data)
        self.assertIn('name', weather_data)
        self.assertIn('main', weather_data)
        self.assertIn('weather', weather_data)
        self.assertEqual(weather_data['name'], 'London')
        self.assertEqual(weather_data['main']['temp'], 15)
        self.assertEqual(weather_data['main']['humidity'], 80)
        self.assertEqual(weather_data['weather'][0]['description'], 'clear sky')
        self.assertEqual(weather_data['wind']['speed'], 3.5)

if __name__ == '__main__':
    unittest.main()