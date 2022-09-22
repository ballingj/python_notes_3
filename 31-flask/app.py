"""
pip install flask -U

in the command line:
export FLASK_APP=app.py
flask run --host 0.0.0.0 --port 3000 --reload

"""

from flask import Flask, request
from umbrella import makeUmbrellaDecision

'''
# version 1 -- simple text message

from flask import Flask  
app = Flask(__name__)


@app.route('/')
def home():
    return 'helloworld'


@app.route('/about')
def about():
    return 'about'


@app.route('/contact')
def contact():
    return 'contact'

'''

'''
# version 2 -- using other modules to perform actions

from flask import Flask
from umbrella import makeUmbrellaDecision


app = Flask(__name__)


@app.route('/')
def home():
    if(makeUmbrellaDecision('omaha', 'us')):
        return f'You need an umbrella today!!!'
    else:
        return f'You do NOT need an umbrella today.'

'''

# version 3 with query parameters
app = Flask(__name__)


@app.route('/')
def home():
    city = request.args.get('city')
    if city is None:
        city = 'new york'
    if makeUmbrellaDecision(city, 'us'):
        return f'Bring an umbrella in {city}!!!'
    else:
        return f'No need for an umbrella in {city}.'
