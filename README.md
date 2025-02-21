# Weather App

A simple Python weather app that fetches weather data from an API and displays it to the user.

## Features

- Fetch current weather data
- Display weather information
- Simple and easy-to-use interface

## Installation

1. Clone the repository:
   ```sh
   git clone https://github.com/CipherJon/weather_app.git
   cd weather_app
   ```

2. Create a virtual environment and activate it:
   ```sh
   python -m venv env
   source env/bin/activate  # On Windows use `env\Scripts\activate`
   ```

3. Install the required dependencies:
   ```sh
   pip install -r requirements.txt
   ```

4. Set up your API key:
   - Create a `.env` file in the root directory of your project and add your API key:
     ```plaintext
     WEATHER_API_KEY=your_actual_api_key_here
     ```

## Usage

Run the app:
```sh
python app.py
```

## Configuration

The API key is set using an environment variable. You can add it to a `.env` file in the root directory of the project:
```plaintext
WEATHER_API_KEY=your_actual_api_key_here
```

## Contributing

Contributions are welcome! Please open an issue or submit a pull request.

## License

This project is licensed under the MIT License.
