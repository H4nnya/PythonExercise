import urllib
import urllib.request

try:
    site = urllib.request.urlopen('https://www.google.com')
except:
    print('Erro')
else:
    print('Deu certo')
