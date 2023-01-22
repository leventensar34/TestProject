import sys

import requests

url = "http://api.fixer.io/latest?base="

birinci_doviz = input("Birinci Döviz:")
ikinci_doviz = input("Ikinci Döviz:")
miktar = float(input("Miktar:"))

response = requests.get(url + birinci_doviz)

json_verisi = response.json()

try:
    print(json_verisi["rates"][ikinci_doviz] * miktar)
except KeyError:
    sys.stderr.write("Lütfen para birimini dogru giriniz")
    sys.stderr.flush()
