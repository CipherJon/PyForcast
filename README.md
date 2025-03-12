# Weather Dashboard 🌦️

[![MIT License](https://img.shields.io/badge/License-MIT-green.svg)](https://opensource.org/licenses/MIT)
[![Python 3.8+](https://img.shields.io/badge/Python-3.8%2B-blue.svg)](https://www.python.org/)

A Python-based weather application that provides real-time weather information for your city through OpenWeatherMap API integration.

## Features ✨

- **Current Weather Data**: Retrieve temperature, humidity, wind speed, and weather conditions
- **API Integration**: Secure API key management using environment variables
- **Command-line Interface**: Simple CLI for quick weather lookups
- **Error Handling**: Robust error handling for API failures and invalid inputs
- **Unit Testing**: Comprehensive test suite with 90%+ coverage
- **Modular Architecture**: Separated concerns between data models, API client, and UI

## Installation 📦

```sh
git clone https://github.com/CipherJon/PyForcast
cd weather_app
```

### Virtual Environment Setup

<details>
<summary>Windows</summary>

```powershell
python -m venv env
env\Scripts\activate
```
</details>

<details>
<summary>Linux/macOS</summary>

```bash
python3 -m venv env
source env/bin/activate
```
</details>

Install dependencies:
```sh
pip install -r requirements.txt
```

## Configuration ⚙️

Create `.env` file with your API key:
```plaintext
WEATHER_API_KEY=your_actual_api_key_here
```

## Usage 🚀

Run the dashboard:
```sh
python app.py
```

Command-line options:
```sh
python app.py --city "London" --units metric
```

## Testing ✅

Run test suite:
```sh
python -m pytest tests/ -v
```

## Project Structure 📂

```
weather_app/
├── weather/          # Core application modules
│   ├── api.py        # API client implementation
│   ├── models.py     # Data models and schemas
│   └── utils.py      # Helper functions
├── tests/            # Unit tests
├── app.py            # Main application entrypoint
└── requirements.txt  # Dependency list
```

## Contributing 🤝

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/your-feature`)
3. Write tests for new functionality
4. Commit your changes (`git commit -am 'Add some feature'`)
5. Push to the branch (`git push origin feature/your-feature`)
6. Open a Pull Request

Please ensure your code passes all tests and follows PEP8 guidelines.

## License 📄

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
