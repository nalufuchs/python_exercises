import requests


try:
    site = requests.get('http://www.pudim.com.br')
except requests.exceptions.HTTPError:
    print('Deu erro.')
else:
    print('Deu certo.')
