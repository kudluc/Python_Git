import requests
import json

subjekt = input('Dobrý den! Jaký je název subjektu, který chcete vyhledat? Zadejte jeho jméno:')

headers = {
    'accept': 'application/json',
    'Content-Type': 'application/json',
}

data = {'obchodniJmeno': subjekt}

response = requests.post('https://ares.gov.cz/ekonomicke-subjekty-v-be/rest/ekonomicke-subjekty/vyhledat', headers=headers, json=data)

data = response.json()

with open('subj.json', 'w', encoding='utf-8') as file:
    json.dump(data, file, indent=2, ensure_ascii=False)

with open('subj.json', encoding='utf-8') as file:
    subj_list = json.load(file)

subj_celkem = int(subj_list['pocetCelkem'])

print(f'Nalezeno subjektů: {subj_celkem}')

ekonomicke_subjekty = subj_list['ekonomickeSubjekty']

for subjekt in ekonomicke_subjekty:
    obchodni_jmeno = subjekt['obchodniJmeno']
    ico = subjekt['ico']
    
    print(obchodni_jmeno,', ', ico, sep='')