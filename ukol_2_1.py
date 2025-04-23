import json
import requests

ico = input('Dobrý den! O kterém subjektu chcete získat informace? Zadejte jeho IČO: ')

response = requests.get(f'https://ares.gov.cz/ekonomicke-subjekty-v-be/rest/ekonomicke-subjekty/{ico}')
data = response.json()

informace_z_OR = data.get('ekonomickeSubjekty', {})

  
jmeno_subjektu = data.get('obchodniJmeno', 'Neznámý subjekt')
adresa_subjektu = data.get('sidlo', {}).get('textovaAdresa', 'Neznámá adresa')