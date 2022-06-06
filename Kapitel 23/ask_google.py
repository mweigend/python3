# ask_google.py
from urllib.request import urlopen
from urllib.parse import urlencode
from re import findall


GOOGLE = 'https://www.google.de?search?'

with urlopen(GOOGLE)as f:
    htmltext=(str(f.read()))

print(htmltext[:100])
