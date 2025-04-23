import json
import requests

ico = input('Dobrý den! O kterém subjektu chcete získat informace? Zadejte jeho IČO: ')

response = requests.get(f'https://ares.gov.cz/ekonomicke-subjekty-v-be/rest/ekonomicke-subjekty/{ico}')
data = response.json()

informace_z_OR = data.get('ekonomickeSubjekty', {})

jmeno_subjektu = data['obchodniJmeno']
adresa_subjektu = data['sidlo']['textovaAdresa']

print(jmeno_subjektu)
print(adresa_subjektu)