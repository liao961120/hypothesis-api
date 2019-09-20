import requests, json

params = {
    'uri': 'https://styleme.pixnet.net/post/223909533'
}

rq = requests.get('https://api.hypothes.is/api/search', params=params)

annotations = json.loads(rq.text)
