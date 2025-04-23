import requests
import json

subjekt = input('Dobrý den! Jaký je název subjektu, který chcete vyhledat? Zadejte jeho jméno: ')

headers = {
    'accept': 'application/json',
    'Content-Type': 'application/json',
}


data = {'obchodniJmeno': subjekt}

response = requests.post('https://ares.gov.cz/ekonomicke-subjekty-v-be/rest/ekonomicke-subjekty/vyhledat', headers=headers, json=data)

odpoved = response.json()
pocet = odpoved.get('pocetCelkem', 0)
subj_list = odpoved.get('ekonomickeSubjekty', {})

print(f'Nalezeno subjektů: {pocet}')

for subjekt in subj_list:
    obchodni_jmeno = subjekt['obchodniJmeno']
    ico = subjekt['ico']
    
    print(obchodni_jmeno,', ', ico, sep='')