"""Desafio 114. Crie um código em Python para verificar se o site www.pudim.com.br está acessível na internet."""

import urllib
import urllib.request

try:
    site = urllib.request.urlopen('http://www.pudim.com.br')
except:
    print('Site não acessível')
else:
    print('Site disponível!')
    print(site.read())

