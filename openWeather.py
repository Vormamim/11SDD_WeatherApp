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

# Get weather for a location
location = input("Enter a location: ")
current_temp, current_weather, forecast = get_weather(location)

# Print current weather conditions
print(f'Current temperature in {location}: {current_temp}')
print(f'Current weather in {location}: {current_weather}')

# Print forecast for next 5 days
print("\n5-day forecast:")
for date, weather in forecast.items():
    print(f'{date}: Temperature: {weather["temp"]}, Weather: {weather["weather"]}')
