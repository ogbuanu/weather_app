import requests
from flask import current_app
def api_caller(location):
    api_key = current_app.config['API_KEY']
    url = f'http://api.weatherapi.com/v1/forecast.json?key={api_key}&q={location}&days=2&aqi=no&alerts=no'
    response = requests.get(url)
    # return response.json() if response.status_code != 400 else 'please enter a valid location'
    return response
    # try:

    #     response = requests.get(url)
    # except:
    #     pass
    # if response :
    #     data = response.json()
    #     return data
    # return 'poor network connection'