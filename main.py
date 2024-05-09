#importações
import requests
import random

# obtendo os dados
url = 'https://raw.githubusercontent.com/guilhermeonrails/api-imersao-ia/main/words.json'
resposta = requests.get(url)
data = resposta.json()

# organizando os dados
valor_secreto = random.choice(data)
palavra_secreta = valor_secreto['palavra']
dica = valor_secreto['dica']

# apresenta as informações
print(f'Esta palavra tem {len(palavra_secreta)} letras. A dica é: {dica}')