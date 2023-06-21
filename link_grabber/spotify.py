import requests
from os import getenv

def authenticate():
    AUTH_URL = 'https://accounts.spotify.com/api/token'

    response = requests.post(AUTH_URL, {
        'grant_type': 'client_credentials',
        'client_id': getenv('CLIENT_ID'),
        'client_secret': getenv('CLIENT_SECRET')
    })

    resp_json = response.json()

    return resp_json['access_token']

print(authenticate())