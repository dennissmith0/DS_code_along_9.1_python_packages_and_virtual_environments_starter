import requests
from spotify import authenticate

token = authenticate()

query_url = 'https://api.spotify.com/v1/playlists/37i9dQZEVXbMDoHDwVN2tF'

response = requests.get(query_url, headers={
    'Authorization': f'Bearer {token}'
})

response = response.json()

for i in range(50):
    print(response['tracks']['items'][i]['track']['external_urls']['spotify'])