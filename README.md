# 11SDD_WeatherApp

## This is a base project for you to TINKER with. It uses and API and Flask which is a wrapper used to create a local webserver and run an application. This is as hard as it needs to get for the HSC in Year 12, so lets start at the top and work backwards. The goal here is to learn 'just in time' and 'what you need' rather than plodding through un-connected exercises.

## This is a collaboration

You need to work with 1-2 other people

This task assumes you have the core skills or input, output, basic loops, using a dictionary to store data, know libraries exist to make your life easier, and that we can save files in a format called JSON which we use to import and dump data. I'm giving you the code because you can learn by copying it.

* I strongly suggest you don't copy and paste it as you'll learn nothing *

Begin with the file called lists.py

## lists.py

The code you provided demonstrates three different ways to loop through a list of names, and to print each name.

The first loop is a for loop that uses a variable called "name" to iterate through each element of the "names" list. For each iteration, the "name" variable takes on the value of the current element in the list, and the "print" function is used to display that value.

The second loop is a while loop that uses an index variable to keep track of the current position in the "names" list. The loop continues as long as the index variable is less than the number of elements in the list. At each iteration, the "print" function is used to display the element at the current index, and the index variable is incremented by 1.

The third loop uses the built-in "enumerate" function, which returns both the index and the value of each element in a list. The loop iterates through each element in the "names" list, and for each iteration, the index and name are assigned to the variables "index" and "name", respectively. The "print" function is used to display both the index and the name, with the index incremented by 1 to start counting from 1 instead of 0.

All three loops achieve the same result of printing each name in the "names" list, but they use different syntax and logic to do so.

## lists_flask.py

    The first two lines import two modules: "sys" and "Flask". "sys" is a standard Python module used to access system-specific functionality, while "Flask" is a third-party module that provides tools for building web applications.

    The next line imports the "render_template" function from the "flask" module. This function is used to render HTML templates for web pages.

    The next line creates a new Flask app and assigns it to the variable "app". The "name" parameter is passed to the app constructor to tell Flask the name of the current module. This is necessary for Flask to determine the location of other files, such as templates and static files.

    The "names" list contains a set of names that will be displayed on the home page of the web application.
    The "@app.route" decorator is used to specify a URL route for the home page of the web application. In this case, the route is simply "/", which represents the root of the web application.

    The "def index()" function is defined to handle the request for the home page. When a user visits the URL specified in the "@app.route" decorator, Flask will call this function to generate the response for that page.
    The "return render_template()" statement renders an HTML template called "index.html", passing the "names" list as a parameter. This template is used to generate the content of the home page, and the "names" list is used to display a list of names on the page.

    The final "if name == 'main':" block checks whether the current module is being run directly, as opposed to being imported as a module in another file. If it is being run directly, the "app.run()" method is called to start the Flask application in debug mode. This method will run the web application on the local host at port 5000.

## openWeather.py

This is a Python script that uses the OpenWeatherMap API to get the current weather conditions and 5-day forecast for a specified location. Here's a breakdown of what it does in a step by step kind of way

You need to get an API key from open weather dot com. This is a direct data-pipe to pull a ton of information into your program. What I want you to think about is - what data is in open weather and how can I change the program to do different things. This is a TINKERING exercise. This is also AS HARD AS IT GETS in terms of the HSC. It is WAY harder than the HSC exam questions. What I'm showing you is a data science project that could be the base for an web application - which could indeed be an major work.

## so we are going to start on HARD mode. I have given you links to the resources needed to get to the core-level and then you can use this to pick over to see how to make an app.

    The script imports the requests and json modules.
    The API key for OpenWeatherMap is defined and stored in a variable called api_key.
    The get_weather function is defined, which takes a location as its input and returns the current temperature, current weather conditions, and 5-day forecast for that location.
    Within the get_weather function, API endpoints for the current weather and 5-day forecast are constructed using the specified location and API key.
    The requests.get function is used to send GET requests to the API endpoints.
    The JSON response from the API is parsed into a Python dictionary using the json.loads function.
    The relevant data (current temperature, current weather conditions, and forecast for the next 5 days) is extracted from the Python dictionary and stored in variables.
    The current_temp, current_weather, and forecast variables are returned by the get_weather function.
    The user is prompted to enter a location.
    The get_weather function is called with the location as its input, and the results are stored in the current_temp, current_weather, and forecast variables.
    The current temperature and weather conditions for the specified location are printed to the console.
    The 5-day forecast for the specified location is printed to the console, with the date, temperature, and weather conditions for each day.

## openWeatherFlask.py

This code defines a web application that uses the Flask framework to provide weather information to users. The application takes a user's location input and returns the current temperature, current weather conditions, and a 5-day weather forecast for that location using the OpenWeatherMap API.

The Flask module is imported and an instance of the Flask class is created. The render_template and request modules are also imported.

The api_key variable is set to the API key for the OpenWeatherMap service.

The get_weather function takes a location parameter, constructs URLs for the current weather and 5-day forecast endpoints, and uses the requests module to make a GET request to each endpoint. The JSON response from each request is parsed into a Python dictionary. The function then extracts the current temperature and weather conditions from the current weather dictionary, and extracts the forecasted temperature and weather conditions for the next 5 days from the forecast dictionary.

The Flask instance is configured with two routes: the home page and the weather page. The index function handles the home page and renders an HTML template called index2.html. The weather function handles the weather page and takes the user's location input, calls the get_weather function to get the weather information, and renders an HTML template called weather.html, passing the weather information as arguments.

Finally, the application is started by calling the run method on the app instance, with debug mode set to True.





