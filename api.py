# se importa la biblioteca request
import requests

api_rym = 'https://rickandmortyapi.com/api'
characters = 'https://rickandmortyapi.com/api/character/'
locations = 'https://rickandmortyapi.com/api/location'

pj = input("Ingrese un número: ") 

# se realiza la petición
api = requests.get(api_rym)
character = requests.get(characters + pj)
# responde con un código de estado 200
print(api)

# se obtiene los datos en formato json
datos = character.json()
# se imprimen datos especificos del obj
print(f"Nombre: "+datos["name"])
print(f"Estado: "+datos["status"])
print(f"Especie: "+datos["species"])
print(f"Género: "+datos["gender"])
print(f"Locación: "+datos["location"]["name"])