#Pokemon Project
import requests
from ascii_magic import AsciiArt, Back

# Pokemon API URL and prompt the user for the name of the pokemon
pokeAPI = "https://pokeapi.co/api/v2/pokemon/"
pokemon = input("Enter the name of the pokemon:").lower()

# Function to obtain pokemon data
def get_pokemon(pokemon):
    response = requests.get(pokeAPI + pokemon)
    if response.status_code == 200:
        return response.json()
    else:
        return None

# Assigns all pokemon data to the variable data.
data = get_pokemon(pokemon)

# Print pokemon data
if data:
    # Gets the pokemon image and converts it to ASCII.
    image_url = data["sprites"]["front_default"]
    poke_art = AsciiArt.from_url(image_url).to_ascii(columns=60, width_ratio=2.5)    
    print(poke_art + '\n')

    # Print pokemon data
    print("Pokemon Data:")
    print("Name:", data["name"].capitalize())
    print("ID:", data["id"])
    print("Height:", data["height"] * 0.1, "metros")
    print("Weight:", data["weight"] * 0.1 , "Kg")
    print('Type:', ', '.join([t['type']['name'].capitalize() for t in data['types']]), '\n')
    
else:
    print("Pokemon not found")





