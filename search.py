# Search function to look for Pokémon's name, dex number, type(s), or stat
def search_pokemon(query, pokedex):
    results = []  # To store multiple matches
    for number, details in pokedex.items():
        # Convert query to string to handle numbers
        if (query.lower() in details["name"].lower() or
                query == number or
                query.capitalize() in details["type"] or
                query == str(details["hp"]) or
                query == str(details["attack"])):
            results.append(
                f"{details['name']} (#{number})\nType: {', '.join(details['type'])}\nHP: {details['hp']}\nAttack: {details['attack']}")
    # Return all results, or "not found" if none
    return "\n\n".join(results) if results else "Pokemon not found."


def search_pokemon_list(query, pokemon_list):
    """
    Searches for Pokémon names in the list that contain the query.
    :param query: Partial name to search for.
    :param pokemon_list: The list of Pokémon names.
    :return: A list of matching Pokémon names or a 'not found' message.
    """
    matches = [f"{name.capitalize()}" for name in pokemon_list if query.lower() in name.lower()]
    return matches if matches else "No Pokémon match your search."
