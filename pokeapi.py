import requests
import textwrap


def format_text(text):
    return text.replace("-", " ").title()


def clean_flavor_text(text):
    # Remove unnecessary line breaks and fix spacing
    cleaned_text = text.replace("\n", " ").replace("\f", " ").strip()
    # Wrap the cleaned text at 80 characters
    return textwrap.fill(cleaned_text, width=80)


def fetch_pokemon(name_or_id):
    url = f"https://pokeapi.co/api/v2/pokemon/{name_or_id.lower()}"
    response = requests.get(url)

    if response.status_code == 200:  # Success
        data = response.json()
        return {
            "name": data["name"],
            "id": data["id"],
            "type": [t["type"]["name"] for t in data["types"]],
            "ability": [format_text(a['ability']['name']) for a in data['abilities']],
            "hp": data["stats"][0]["base_stat"],
            "attack": data["stats"][1]["base_stat"],
            "defense": data["stats"][2]["base_stat"],
            "special-attack": data["stats"][3]["base_stat"],
            "special-defense": data["stats"][4]["base_stat"],
            "speed": data["stats"][5]["base_stat"]
        }
    elif response.status_code == 404:  # Pokémon not found
        return "Pokémon not found."
    else:  # Other errors
        return f"Error: Unable to fetch data (status code {response.status_code})."


def fetch_pokemon_data(name_or_id):
    species_url = f"https://pokeapi.co/api/v2/pokemon-species/{name_or_id.lower()}"
    pokemon_url = f"https://pokeapi.co/api/v2/pokemon/{name_or_id.lower()}"

    # Fetch species data
    species_response = requests.get(species_url)
    if species_response.status_code == 200:
        species_data = species_response.json()

        # Fetch Pokémon data for sprites
        pokemon_response = requests.get(pokemon_url)
        if pokemon_response.status_code == 200:
            pokemon_data = pokemon_response.json()

            return {
                "name": species_data["name"],
                "types": [t["type"]["name"] for t in pokemon_data["types"]],
                "generation": (lambda gen: "Generation " + gen["generation"]["name"].replace("generation-", "").upper())(species_data),
                "color": species_data["color"]["name"],
                "egg_groups": [group["name"] for group in species_data["egg_groups"]],
                "description": clean_flavor_text(next(
                    entry["flavor_text"] for entry in species_data["flavor_text_entries"]
                    if entry["language"]["name"] == "en"
                )),
                "default_sprite": pokemon_data["sprites"]["front_default"],
                "shiny_sprite": pokemon_data["sprites"]["front_shiny"],
                "stats": {
                    "hp": pokemon_data["stats"][0]["base_stat"],
                    "attack": pokemon_data["stats"][1]["base_stat"],
                    "defense": pokemon_data["stats"][2]["base_stat"],
                    "special-attack": pokemon_data["stats"][3]["base_stat"],
                    "special-defense": pokemon_data["stats"][4]["base_stat"],
                    "speed": pokemon_data["stats"][5]["base_stat"],
                }
            }
        else:
            return "Error: Unable to fetch Pokémon sprite data."

    elif species_response.status_code == 404:
        return "Pokémon data not found."
    else:
        return f"Error: Unable to fetch data (status code {species_response.status_code})."


def fetch_typing_data(type_name):
    url = f"https://pokeapi.co/api/v2/type/{type_name.lower()}"
    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()
        return {
            "name": data["name"],
            "generation": data["generation"]["name"].replace("generation-", "").upper(),  # Extract and format
            "double_damage_from": [t["name"] for t in data["damage_relations"]["double_damage_from"]],
            "double_damage_to": [t["name"] for t in data["damage_relations"]["double_damage_to"]]
        }
    else:
        return "Type data not found."


def fetch_ability_data(ability_name):
    url = f"https://pokeapi.co/api/v2/ability/{ability_name.lower()}"
    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()
        return {
            "name": data["name"],
            "description": next(
                entry["effect"] for entry in data["effect_entries"]
                if entry["language"]["name"] == "en"
            )
        }
    else:
        return "Ability data not found."


def fetch_pokemon_list():
    """
    Fetches the full list of Pokémon from the PokéAPI.
    :return: A list of Pokémon names or an error message.
    """
    url = "https://pokeapi.co/api/v2/pokemon?limit=10000"
    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()
        return [pokemon["name"] for pokemon in data["results"]]
    else:
        return f"Error: Unable to fetch Pokémon list (status code {response.status_code})."
