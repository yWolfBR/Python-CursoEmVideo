import urllib.request

try:
    pudim = urllib.request.urlopen('http://pudim.com.br')
except Exception:
    print('O site Pudim não está acessível :(')
else:
    print('O site Pudim está acessível :)')
