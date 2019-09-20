import requests

params = {
    'uri': 'https://styleme.pixnet.net/post/223909533'
}

requests.get('https://api.hypothes.is/api/search', params=params)

