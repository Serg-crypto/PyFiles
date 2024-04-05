import requests



url = 'https://api.kanye.rest'


response = requests.get(url)
if response.status_code == 200:
    data = response.json()
    print(data['quote'])