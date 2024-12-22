import requests 
url = "https://pokeapi.co/api/v2/pokemon/646"
x = requests.get (url)
data = x.json()
print(data['cries']['legacy'])