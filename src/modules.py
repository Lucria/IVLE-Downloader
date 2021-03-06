import config
import requests


def getModules(token):
    url = config.hosturl + "Modules"
    payload = {'APIKey': config.APIKey, 'AuthToken': token, 'Duration': '0', 'output': 'json'}
    response = requests.get(url, params=payload)
    return response.json()['Results']
