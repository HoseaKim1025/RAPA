import requests

url = 'https://api.tvmaze.com/singlesearch/shows?q=narcos&embed=episodes'
r = requests.get(url)
print(r.text)