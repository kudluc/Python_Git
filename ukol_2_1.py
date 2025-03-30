import json
import requests

ICO = int(input('Dobrý den! O kterém subjektu chcete získat informace? Zadejte jeho IČO:'))

response = requests.get(f'https://ares.gov.cz/ekonomicke-subjekty-v-be/rest/ekonomicke-subjekty/{ICO}')
data = response.json()

with open('ICO.json', 'w', encoding='utf-8') as file:
    json.dump(data, file, indent=2, ensure_ascii=False)

with open('ICO.json', encoding='utf-8') as file:
    informace_z_OR = json.load(file)
    
jmeno_subjektu = informace_z_OR['obchodniJmeno']
adresa_subjeku = informace_z_OR['sidlo']['textovaAdresa']

print(jmeno_subjektu)
print(adresa_subjeku)