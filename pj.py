import requests

characters = 'https://rickandmortyapi.com/api/character/'

# se realiza la petición
data = requests.get(characters)
# responde con un código de estado 200
print(data,"\n")

# se obtiene los datos en formato json
pjs = data.json()

# bucle para imprimir datos de todos los personajes
for datos in pjs["results"]:
    print(f"Nombre: "+datos["name"])
    print(f"Estado: "+datos["status"])
    print(f"Especie: "+datos["species"])
    print(f"Género: "+datos["gender"])
    print(f"Locación: "+datos["location"]["name"])
    print("\n")