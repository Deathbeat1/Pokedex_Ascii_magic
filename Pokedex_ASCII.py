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
while data:
    print("Name:", data["name"].capitalize())
    print("Height:", data["height"])
    print("Weight:", data["weight"])
    print("Abilities:")
    for ability in data["abilities"]:
        print(ability["ability"]["name"])
    print("Types:")
    for types in data["types"]:
        print(types["type"]["name"])
    




