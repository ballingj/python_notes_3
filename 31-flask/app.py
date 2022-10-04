"""
pip install flask -U

in the command line:
export FLASK_APP=app.py
flask run --host 0.0.0.0 --port 3000 --reload

or add the following and run via CLI:

if __name__ == "__main__":
    app.run()
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
# consults the umbrella module and checks if umbrella is needed or not

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

# version 3 with query parameters: add  "/?city=<anycity>""
# http://127.0.0.1:5000/?city=omaha

app = Flask(__name__)

# custom location using argument parser
@app.route('/')
def home():
    city = request.args.get('city')
    if city is None:
        city = 'new york'
    if makeUmbrellaDecision(city, 'US'):
        return f'<h1>Bring an umbrella in {city}, USA!!!</h1>'
    else:
        return f'<h1>No need for an umbrella in {city}, USA.</h1>'


# preset locations for New York
@app.route('/ny')
def newyork():
    city = 'New York'
    country = 'US'
    if(makeUmbrellaDecision(city, country)):
        return f'<h1>You need an umbrella today in {city}, {country}</h1>'
    else:
        return f'<h1>You do NOT need an umbrella today in {city}, {country}</h1>'


# preset locations for Los Angeles
@app.route('/la')
def losangeles():
    city = 'Los Angeles'
    country = 'US'
    if(makeUmbrellaDecision(city, country)):
        return f'<h1>You need an umbrella today in {city}, {country}</h1>'
    else:
        return f'<h1>You do NOT need an umbrella today in {city}, {country}</h1>'


if __name__ == "__main__":
    app.run()
