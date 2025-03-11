import plotly.graph_objects as go
from plotly.subplots import make_subplots
import webbrowser
import os

def display_weather(weather_data):
    city = weather_data['name']
    temperature = weather_data['main']['temp']
    description = weather_data['weather'][0]['description']
    humidity = weather_data['main']['humidity']
    wind_speed = weather_data['wind']['speed']

    # Create dashboard layout
    fig = make_subplots(
        rows=2, cols=2,
        specs=[[{"type": "indicator"}, {"type": "indicator"}],
               [{"type": "indicator"}, {"type": "bar"}]],
        subplot_titles=('Temperature', 'Wind Speed', 'Humidity', 'Weather Conditions')
    )

    # Temperature gauge
    fig.add_trace(go.Indicator(
        mode="gauge+number",
        value=temperature,
        title={'text': "Temperature (°C)"},
        gauge={'axis': {'range': [None, 40]},
               'steps': [
                   {'range': [0, 10], 'color': "lightblue"},
                   {'range': [10, 20], 'color': "blue"},
                   {'range': [20, 40], 'color': "royalblue"}],
               'threshold': {'line': {'color': "red", 'width': 4},
                             'thickness': 0.75, 'value': temperature}},
        number={'suffix': "°C"}
    ), row=1, col=1)

    # Wind speed indicator
    fig.add_trace(go.Indicator(
        mode="number+delta",
        value=wind_speed,
        title={"text": "Wind Speed (m/s)"},
        number={'suffix': " m/s"}
    ), row=1, col=2)

    # Humidity gauge
    fig.add_trace(go.Indicator(
        mode="gauge+number",
        value=humidity,
        title={'text': "Humidity (%)"},
        gauge={'axis': {'range': [None, 100]},
               'steps': [
                   {'range': [0, 30], 'color': "yellow"},
                   {'range': [30, 70], 'color': "goldenrod"},
                   {'range': [70, 100], 'color': "darkgoldenrod"}],
               'threshold': {'line': {'color': "red", 'width': 4},
                             'thickness': 0.75, 'value': humidity}},
        number={'suffix': "%"}
    ), row=2, col=1)

    # Weather conditions bar
    fig.add_trace(go.Bar(
        x=['Current Weather'],
        y=[1],
        text=[description.capitalize()],
        marker_color='skyblue',
        textposition='auto'
    ), row=2, col=2)

    # Update layout
    fig.update_layout(
        height=600,
        width=800,
        title_text=f"Weather Dashboard for {city}",
        showlegend=False
    )

    # Save and open in browser
    filename = "weather_dashboard.html"
    fig.write_html(filename)
    webbrowser.open(f'file://{os.path.abspath(filename)}')