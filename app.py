import flask import Flash, render_template
import requests


app=Flask(__name__)


@app.route('/')
def home():
    return render_template('index.html')

if__name__=='__main__':
    app.run(debug='True')

@app.route('/weather')
def weather():
    api_key='1a02df4eb451c73c5d41662d94e9d886'
    city= 'maple ridge'
    url='https://api.openweathermap.org/data/3.0/onecall?lat=33.44&lon=-94.04&appid={1a02df4eb451c73c5d41662d94e9d886}'
    response = requests.get(url)
    data=response.json
    return render_template('weather.html', data-data)

    