import math

class Locality:
    def __init__(self, name, locality_coefficient):
        self.name = name
        self.locality_coefficient = locality_coefficient

class Property:
    def __init__(self, locality):
        self.locality = locality
     
class Estate(Property):
    def __init__(self, locality, estate_type, area):
        super().__init__(locality)
        self.estate_type = estate_type
        self.area = area

    def calculate_tax(self):
        type_estate = {
    'land': 0.85,
    'building_site': 9,
    'forrest': 0.35,
    'garden': 2,
    }
        type_coefficient = type_estate.get(self.estate_type)
        tax = math.ceil(self.area * self.locality.locality_coefficient * type_coefficient)
        return tax
    
    def __str__(self):
       return f'Pozemek v lokalitě {self.locality.name} má koeficient {self.locality.locality_coefficient}.'

       
locality = Locality('Les', 0.8)
lesni_pozemek = Estate(locality, 'land', 900)
#print(lesni_pozemek.calculate_tax())  

class Residence(Property):
    def __init__(self, locality, area, commercial):
        super().__init__(locality)
        self.area = area
        self.commercial = commercial
    def calculate_tax(self):
        if self.commercial:
            return self.area * self.locality.locality_coefficient * 15 * 2
        else:
            return self.area * self.locality.locality_coefficient * 15
    def __str__(self):
        return f'Pozemek v lokalitě {self.locality.name} má koeficient {self.locality.locality_coefficient}.'
        
locality = Locality('Praha', 3)
byt = Residence(locality, 60, True)
#- Zemědělský pozemek o ploše 900 metrů čtverečních v lokalitě Manětín s koeficientem 0.8. 
# Daň z této nemovitosti je 900 * 0.85 * 0.8 = 612.
locality = Locality('Manětín', 0.8)
pole = Estate(locality, 'land', 900)
#- Dům s podlahovou plochou 120 metrů čtverečních v lokalitě Manětín s koeficientem 0.8. 
# Daň z této nemovitosti je 120 * 0.8 * 15 = 1440.
locality = Locality('Manětín', 0.8)
dum = Residence(locality, 120, False)
#- Kancelář (tj. komerční nemovitost) s podlahovou plochou 90 metrů čtverečních v lokalitě Brno s koeficientem 3.
#  Daň z této nemovitosti je 90 * 3 * 15 * 2 = 8100.
locality = Locality('Brno', 3)
kancelar = Residence(locality, 90, True)
print(byt, f'Daň z nemovistoti je {byt.calculate_tax()}.')
print(pole, f'Daň z nemovistoti je {pole.calculate_tax()}.')
print(dum, f'Daň z nemovistoti je {dum.calculate_tax()}.')
print(kancelar, f'Daň z nemovistoti je {kancelar.calculate_tax()}.')