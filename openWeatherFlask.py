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
    current_weather_response = requests.get(current_weather_url) # <-- make GET request to API
    forecast_response = requests.get(forecast_url) # <-- make GET request to API

    # Parse JSON response
    current_weather_data = json.loads(current_weather_response.text) # <-- convert JSON response to Python dictionary
    forecast_data = json.loads(forecast_response.text) # 

    # Extract current weather conditions
    current_temp = current_weather_data['main']['temp'] # <-- extract temperature from dictionary
    current_weather = current_weather_data['weather'][0]['description'] # <-- extract weather description from dictionary

    # Extract forecast for next 5 days
    forecast_list = forecast_data['list'] # <-- extract list of forecasts from dictionary
    forecast = {} # <-- create empty dictionary to store forecast
    for f in forecast_list: # <-- loop through list of forecasts
        date = f['dt_txt'][:10] # <-- extract date from forecast
        if date not in forecast: #  <-- check if date is already in forecast dictionary
            forecast[date] = { 
                'temp': f['main']['temp'],
                'weather': f['weather'][0]['description']
            } # <-- add date, temperature, and weather to forecast dictionary

    return current_temp, current_weather, forecast # <-- return current weather conditions and 5-day forecast

app = Flask(__name__) # create a Flask app

@app.route('/') # route for home page
def index(): # function to handle home page
    return render_template('index2.html') # render index.html template

@app.route('/weather', methods=['POST']) # route for weather page
def weather(): # function to handle weather page
    location = request.form['location'] # get location from form
    current_temp, current_weather, forecast = get_weather(location) # call get_weather function
    return render_template('weather.html', location=location, current_temp=current_temp, current_weather=current_weather, forecast=forecast) #  render weather.html template

if __name__ == '__main__': # run Flask app
    app.run(debug=True) #   run Flask app in debug mode
