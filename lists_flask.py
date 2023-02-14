import sys
# py -m pip install Flask
from flask import Flask, render_template # pip install Flask
app = Flask(__name__) # create a Flask app

names = ["Alice", "Bob", "Charlie", "David", "Eve"] # a list of names

@app.route('/') # route for the home page
def index(): # function to handle the request
    return render_template('index.html', names=names) # render the template

if __name__ == '__main__': # if this file is run directly
    app.run(debug=True) # run the Flask app
