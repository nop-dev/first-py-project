import requests

url = 'https://raw.githubusercontent.com/guilhermeonrails/api-imersao-ia/main/words.json'

resposta = requests.get(url)
data = resposta.json()

print(len(data))

print(data[0])