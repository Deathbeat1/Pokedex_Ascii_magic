#Pokemon Project
import requests
from ascii_magic import AsciiArt, Back

# URL de la API de Pokemon y solicita al usuario el nombre del pokemon
pokeAPI = "https://pokeapi.co/api/v2/pokemon/"
pokemon = input("Ingrese el nombre del pokemon:")

# Función para obtener los datos del pokemon
def get_pokemon(pokemon):
    response = requests.get(pokeAPI + pokemon)
    if response.status_code == 200:
        return response.json()
    else:
        return None

# Asigna todos los datos del pokemon a la variable data
data = get_pokemon(pokemon)

# Imprime los datos del pokemon
if data:
    # Obtiene la imagen del pokemon y la convierte a ASCII
    image_url = data["sprites"]["front_default"]
    poke_art = AsciiArt.from_url(image_url).to_ascii(columns=110, width_ratio=2.5)    
    print(poke_art + '\n')

    # Imprime los datos del pokemon
    print("Datos del Pokemon:")
    print("Nombre:", data["name"].capitalize())
    print("ID:", data["id"])
    print("Altura:", data["height"] * 0.1, "metros")
    print("Peso:", data["weight"] * 0.1 , "Kg")
    print('Tipo:', ', '.join([t['type']['name'].capitalize() for t in data['types']]), '\n')
    
else:
    print("Pokemon no encontrado")


def search_pokemon():
    data = get_pokemon(pokemon)
    if data:
        image_url = data["sprites"]["front_default"]
        poke_art = AsciiArt.from_url(image_url).to_ascii(columns=70, width_ratio=2.5)
        print(poke_art + '\n')
        print("Datos del Pokemon:")
        print("Nombre:", data["name"].capitalize())
        print("ID:", data["id"])
        print("Altura:", data["height"], "inches")
        print("Peso:", data["weight"], "libras")
        print('Tipo:', ', '.join([t['type']['name'].capitalize() for t in data['types']]), '\n')
    else:
        print("Pokemon no encontrado")




