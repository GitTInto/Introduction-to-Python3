import requests
import json
from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    # return 'This is the homepage'
    url = "https://api.chucknorris.io/jokes/random"
    response = requests.get(url).json()
    # print(response['value'])
    return(response['value'])


@app.route('/tuna')
def tuna():
    return '<h2>Tuna is good</h2>'
if __name__ == '__main__':
    app.run(debug=True)



