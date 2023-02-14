from flask import Flask, render_template, request
import requests
import json

# API Key for OpenWeatherMap
api_key = '21857ebedc19b88ac028582686871f7a'

# Function to get current weather conditions and 5-day forecast
def get_weather(location):
    # API endpoint for current weather
    current_weather_url = f'http://api.openweathermap.org/data/2.5/weather?q={location}&appid={api_key}&units=metric'
    # API endpoint for 5-day forecast
    forecast_url = f'http://api.openweathermap.org/data/2.5/forecast?q={location}&appid={api_key}&units=metric'

    # Make GET request to API
    current_weather_response = requests.get(current_weather_url)
    forecast_response = requests.get(forecast_url)

    # Parse JSON response
    current_weather_data = json.loads(current_weather_response.text)
    forecast_data = json.loads(forecast_response.text)

    # Extract current weather conditions
    current_temp = current_weather_data['main']['temp']
    current_weather = current_weather_data['weather'][0]['description']

    # Extract forecast for next 5 days
    forecast_list = forecast_data['list']
    forecast = {}
    for f in forecast_list:
        date = f['dt_txt'][:10]
        if date not in forecast:
            forecast[date] = {
                'temp': f['main']['temp'],
                'weather': f['weather'][0]['description']
            }

    return current_temp, current_weather, forecast

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index2.html')

@app.route('/weather', methods=['POST'])
def weather():
    location = request.form['location']
    current_temp, current_weather, forecast = get_weather(location)
    return render_template('weather.html', location=location, current_temp=current_temp, current_weather=current_weather, forecast=forecast)

if __name__ == '__main__':
    app.run(debug=True)
