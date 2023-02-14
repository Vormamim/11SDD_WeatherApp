import sys
# py -m pip install Flask
from flask import Flask, render_template
app = Flask(__name__)

names = ["Alice", "Bob", "Charlie", "David", "Eve"]

@app.route('/')
def index():
    return render_template('index.html', names=names)

if __name__ == '__main__':
    app.run(debug=True)
