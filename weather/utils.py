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

    # Print weather data to console (for test compatibility)
    print(f"Weather in {city}:")
    print(f"Temperature: {temperature}°C")
    print(f"Description: {description}")
    print(f"Humidity: {humidity}%")
    print(f"Wind Speed: {wind_speed} m/s")

    # Create dashboard with increased spacing
    fig = make_subplots(
        rows=2, cols=2,
        specs=[[{"type": "indicator"}, {"type": "indicator"}],
               [{"type": "indicator"}, {"type": "bar"}]],
        subplot_titles=('', '', 'Humidity', 'Weather'),  # Removed "Temperature" and "Wind Speed"
        horizontal_spacing=0.1,
        vertical_spacing=0.2
    )

    # Temperature gauge with enhanced styling
    fig.add_trace(go.Indicator(
        mode="gauge+number",
        value=temperature,
        title={'text': "Temperature (°C)", 'font': {'size': 14, 'color': '#2c3e50'}},
        gauge={
            'axis': {'range': [0, 40], 'tickcolor': '#bdc3c7', 'ticklen': 10, 'tickwidth': 2},
            'steps': [
                {'range': [0, 10], 'color': '#3498db'},
                {'range': [10, 25], 'color': '#2980b9'},
                {'range': [25, 40], 'color': '#1f618d'}
            ],
            'threshold': {'line': {'color': '#e74c3c', 'width': 3}, 'thickness': 0.8, 'value': temperature},
            'bar': {'color': '#e74c3c'},
            'bgcolor': '#ffffff',
            'borderwidth': 2,
            'bordercolor': '#bdc3c7'
        },
        number={'suffix': "°C", 'font': {'size': 20, 'color': '#2c3e50'}}
    ), row=1, col=1)

    # Wind speed gauge with enhanced styling
    fig.add_trace(go.Indicator(
        mode="gauge+number",
        value=wind_speed,
        title={'text': "Wind Speed (m/s)", 'font': {'size': 14, 'color': '#2c3e50'}},
        gauge={
            'axis': {'range': [0, 15], 'tickcolor': '#bdc3c7', 'ticklen': 10, 'tickwidth': 2},
            'steps': [
                {'range': [0, 5], 'color': '#3498db'},
                {'range': [5, 10], 'color': '#2980b9'},
                {'range': [10, 15], 'color': '#1f618d'}
            ],
            'threshold': {'line': {'color': '#e74c3c', 'width': 3}, 'thickness': 0.8, 'value': wind_speed},
            'bar': {'color': '#e74c3c'},
            'bgcolor': '#ffffff',
            'borderwidth': 2,
            'bordercolor': '#bdc3c7'
        },
        number={'suffix': " m/s", 'font': {'size': 20, 'color': '#2c3e50'}}
    ), row=1, col=2)

    # Humidity gauge with enhanced styling
    fig.add_trace(go.Indicator(
        mode="gauge+number",
        value=humidity,
        title={'text': "Humidity (%)", 'font': {'size': 14, 'color': '#2c3e50'}},
        gauge={
            'axis': {'range': [0, 100], 'tickcolor': '#bdc3c7', 'ticklen': 10, 'tickwidth': 2},
            'steps': [
                {'range': [0, 30], 'color': '#f1c40f'},
                {'range': [30, 70], 'color': '#f39c12'},
                {'range': [70, 100], 'color': '#d35400'}
            ],
            'threshold': {'line': {'color': '#e74c3c', 'width': 3}, 'thickness': 0.8, 'value': humidity},
            'bar': {'color': '#e74c3c'},
            'bgcolor': '#ffffff',
            'borderwidth': 2,
            'bordercolor': '#bdc3c7'
        },
        number={'suffix': "%", 'font': {'size': 20, 'color': '#2c3e50'}}
    ), row=2, col=1)

    # Weather visualization as an enhanced bar chart
    fig.add_trace(go.Bar(
        x=['Current Weather'],
        y=[3],
        text=[f"Current: {description.capitalize()}"],
        marker_color='#3498db',
        marker_line_color='darkblue',
        marker_line_width=2,
        textposition='inside',
        textfont=dict(size=20, color="white", family="Arial"),
        width=0.6,
    ), row=2, col=2)

    # Update layout with improved separation and styling
    fig.update_layout(
        height=900,
        width=1100,
        title_text=f"Weather Dashboard for {city}",
        title_font=dict(size=32, family="Arial", color="#2c3e50"),
        title_x=0.5,
        title_y=0.95,  # Lowered main title to create space
        paper_bgcolor="#e8ecef",
        plot_bgcolor="#ffffff",
        font=dict(family="Helvetica, Arial", size=14, color="#2c3e50"),
        margin=dict(l=50, r=50, t=150, b=50),  # Increased top margin for more space
        showlegend=False,
        autosize=True,
        # Enable zooming and panning for interactivity
        dragmode='zoom'
    )

    # Style and reposition subplot titles to avoid overlap with main title
    for i, annotation in enumerate(fig['layout']['annotations']):
        if annotation['text'] in ['Humidity', 'Weather']:
            annotation['font'] = dict(size=16, color="#2c3e50", family="Arial")
            annotation['y'] = annotation['y'] + 0.15  # Move titles higher within their subplots

    # Remove y-axis ticks for the weather bar graph (bottom-right subplot)
    fig.update_yaxes(
        showticklabels=False,  # Hide y-axis ticks and labels
        showgrid=False,       # Hide grid lines
        row=2, col=2
    )

    # Save and open with custom CSS to center the dashboard
    filename = "weather_dashboard.html"
    fig.write_html(filename, config={'scrollZoom': True, 'displayModeBar': True})
    
    # Add custom CSS for centering and polished look
    with open(filename, 'a') as f:
        f.write("""
        <style>
            body {
                background: linear-gradient(to bottom, #e8ecef, #ffffff);
                margin: 0;
                display: flex;
                justify-content: center;
                align-items: center;
                min-height: 100vh;
                font-family: Helvetica, Arial;
            }
            .js-plotly-plot {
                border: 2px solid #bdc3c7;
                border-radius: 12px;
                box-shadow: 0 6px 12px rgba(0,0,0,0.1);
                padding: 15px;
                max-width: 1100px;
                width: 80%;
                height: auto;
            }
            .plotly .modebar {
                display: block;  /* Show modebar for zooming */
            }
        </style>
        """)
    
    webbrowser.open(f'file://{os.path.abspath(filename)}')

# Example weather data (for testing)
if __name__ == "__main__":
    sample_data = {
        'name': 'Las Vegas',
        'main': {'temp': 18.64, 'humidity': 20},
        'weather': [{'description': 'clear sky'}],
        'wind': {'speed': 11.83}
    }
    display_weather(sample_data)