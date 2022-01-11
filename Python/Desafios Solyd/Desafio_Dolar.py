import re
import requests

requisicao = requests.get('https://economia.awesomeapi.com.br/last/USD-BRL')

padrao = re.findall(r'(\w\.\w+)', requisicao.text)

if padrao:
    print("O valor do Dolar está de R$", padrao[0])

else:
    print('Padrão não encontrado')