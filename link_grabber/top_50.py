import requests
from spotify import authenticate

token = authenticate()

query_url = 'https://api.spotify.com/v1/playlists/37i9dQZEVXbMDoHDwVN2tF'

response = requests.get(query_url, headers={
    'Authorization': f'Bearer {token}'
})

response = response.json()

# for i in range(50):
#     print(response['tracks']['items'][i]['track']['external_urls']['spotify'])

# Exploring the response object's structure

# print(response)
# print(len(response))
#print(response.keys())
#print(response['tracks'])
#print(response['tracks'].keys())
#print(response['tracks']['limit'])
#print(len(response['tracks']))
#print(response['tracks']['items'])
#print(len(response['tracks']['items']))
#print(response['tracks']['items'][5].keys())
#print(response['tracks']['items'][5]['track'].keys())
# print(response['tracks']['items'][5]['track']['album'].keys())
# # print(response['tracks']['items'][5]['track']['album']['artists'])
# print('Song Name: ', response['tracks']['items'][11]['track']['name'])
# print('Artist: ', response['tracks']['items'][11]['track']['album']['artists'][0]['name'])
# print('Album: ', response['tracks']['items'][11]['track']['album']['name'])

def get_top_50_links():
    song_links = [song['track']['external_urls']['spotify']
                  for song in response['tracks']['items']]

    return song_links


for i in range(50):
    print('Song Name: ', response['tracks']['items'][i]['track']['name'])
    print('Artist: ', response['tracks']['items'][i]['track']['album']['artists'][0]['name'])
    print('Album: ', response['tracks']['items'][i]['track']['album']['name'])
    print('Song Link: ', response['tracks']['items'][i]['track']['external_urls']['spotify'])
    print('\n')

# if __name__ == '__main__':
#     print(get_top_50_links())