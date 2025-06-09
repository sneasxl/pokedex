import textwrap
from pokeapi import fetch_pokemon, fetch_pokemon_data, fetch_typing_data, fetch_ability_data, fetch_pokemon_list
from search import search_pokemon_list


def format_pokemon_stat_output(data):
    if isinstance(data, dict):
        return (
            f"{data['name'].capitalize()} (ID: {data['id']})\n"
            f"Type: {', '.join(data['type']).title()}\n"
            f"Ability: {', '.join(data['ability']).title()}\n"
            f"HP: {data['hp']}\n"
            f"Attack: {data['attack']}\n"
            f"Defense: {data['defense']}\n"
            f"Special Attack: {data['special-attack']}\n"
            f"Special Defense: {data['special-defense']}\n"
            f"Speed: {data['speed']}\n"
        )
    return data  # Return error messages as-is


def format_pokemon_data_output(data):
    if isinstance(data, dict):
        return (
            f"Name: {data['name'].capitalize()}\n"
            f"Generation: {data['generation']}\n"
            f"Color: {data['color'].capitalize()}\n"
            f"Egg Group(s): {', '.join(data['egg_groups']).title()}\n"
            f"Description: {data['description']}\n"
            f"Sprite URL: {data['default_sprite']}\n"
        )
    return data  # Return the error message as-is


def format_typing_output(data):
    if isinstance(data, dict):
        return (
            f"Type: {data['name'].capitalize()}\n"
            f"Generation: Generation {data['generation']}\n"
            f"Weak To: {', '.join([t.capitalize() for t in data['double_damage_from']]) or 'None'}\n"
            f"Strong Against: {', '.join([t.capitalize() for t in data['double_damage_to']]) or 'None'}\n"
        )
    return data  # Return error message as-is


def format_ability_output(data):
    if isinstance(data, dict):
        description = data['description']
        # Wrap text at 80 characters for better readability
        wrapped_description = "\n".join(textwrap.fill(line, width=100) for line in description.split("\n"))
        return (
            f"Ability: {data['name'].capitalize()}\n"
            f"Description:\n{wrapped_description}\n"
        )
    return data


if __name__ == "__main__":
    print("Welcome to the Pokédex!")

    current_menu = "main"
    while True:
        if current_menu == "main":
            action = input("Choose an action: 'Dex', 'Search', or 'Exit': ").lower()

            if action == "dex":
                current_menu = "dex"
            elif action == "search":
                current_menu = "search"
            elif action == "exit":
                print("Goodbye!")
                break
            else:
                print("Invalid action. Please choose 'Dex', 'Search', or 'Exit'.")

        elif current_menu == "dex":
            choice = input("Choose 'stats', 'data', or 'back': ").lower()

            if choice == "stats":
                name_or_id = input("Enter Pokémon name or ID: ")
                print(f"Displaying data...\n==========")
                result = fetch_pokemon(name_or_id)
                print(format_pokemon_stat_output(result))
            elif choice == "data":
                current_menu = "data"
            elif choice == "back":
                current_menu = "main"
            else:
                print("Invalid option. Choose 'stats', 'data', or 'back'.")

        elif current_menu == "data":
            print("If you want to know a Specific Pokémon's data or know about a Type or Ability: ")
            choice = input("Choose Pokémon, type, ability, back, or main menu: ").lower()

            if choice == "pokemon":
                name_or_id = input("Enter Pokémon name or ID: ")
                print(f"Displaying data...\n==========")
                result = fetch_pokemon_data(name_or_id)
                print(format_pokemon_data_output(result))
            elif choice == "type":
                name_or_id = input("Enter Pokémon type: ")
                print(f"Displaying data...\n==========")
                result = fetch_typing_data(name_or_id)
                print(format_typing_output(result))
            elif choice == "ability":
                name_or_id = input("Enter Pokémon ability: ")
                print(f"Displaying data...\n==========")
                result = fetch_ability_data(name_or_id)
                print(format_ability_output(result))
            elif choice == "back":
                current_menu = "dex"
            elif choice == "main menu":
                current_menu = "main"
            else:
                print("Invalid option. Choose 'Pokémon', 'type', 'ability', 'back', or 'main menu'.")

        elif current_menu == "search":
            pokemon_list = fetch_pokemon_list()
            if isinstance(pokemon_list, list):  # Ensure list was fetched successfully
                query = input("Enter partial Pokémon name to search: ")
                matches = search_pokemon_list(query, pokemon_list)
                if isinstance(matches, list):
                    print("\n".join(matches))
                else:
                    print(matches)  # "No Pokémon match your search."
            else:
                print(pokemon_list)  # Display error message
            print()
            current_menu = "main"

""" My While Loop

    while True:  # Main loop
        action = input("Choose an action: 'Dex', 'Search', or 'Exit': ").lower()

        if action.lower() == "dex":
            return_to_main = False  # Flag to control exiting nested loops
            while not return_to_main:  # Sub-loop for 'Dex'
                choice = input("Choose 'stats', 'data', or 'back': ").lower()

                if choice.lower() == "stats":
                    name_or_id = input("Enter Pokémon name or ID: ")
                    print(f"Displaying data...\n"
                          f"==========")
                    # Add logic to show stats here
                    result = fetch_pokemon(name_or_id)
                    print(format_pokemon_stat_output(result))

                elif choice.lower() == "data":
                    while True:
                        print("If you want to know a Specific Pokemon's data or know about a Type or Ability: ")
                        choice = input("Choose Pokémon, type, ability, back, or main menu: ").lower()
                        if choice.lower() == "pokemon":
                            name_or_id = input("Enter Pokémon name or ID: ")
                            print(f"Displaying data...\n"
                                  f"==========")
                            # Add logic to show data here
                            result = fetch_pokemon_data(name_or_id)
                            print(format_pokemon_data_output(result))

                        elif choice.lower() == "type":
                            name_or_id = input("Enter Pokémon type: ")
                            print(f"Displaying data...\n"
                                  f"==========")
                            # Add logic to show data here
                            result = fetch_typing_data(name_or_id)
                            print(format_typing_output(result))

                        elif choice.lower() == "ability":
                            name_or_id = input("Enter Pokémon ability: ")
                            print(f"Displaying data...\n"
                                  f"==========")
                            # Add logic to show data here
                            result = fetch_ability_data(name_or_id)
                            print(format_ability_output(result))

                        elif choice == "back":
                            print("Returning to the previous menu...\n")
                            break  # Exit 'data' sub-loop

                        elif choice == "main menu":
                            print("Returning to the main menu...\n")
                            return_to_main = True  # Set the flag to exit all loops
                            break  # Break out of the 'data' sub-loop

                        else:
                            print("Invalid option. Choose 'Pokémon', 'type', 'ability', 'back', or 'main menu'.")

                elif choice.lower() == "back":
                    print("Returning to the main menu...\n"
                          f"==========")
                    break  # Exit the sub-loop and go back to the main loop

                else:
                    print("Invalid option. Choose 'stats', 'data', or 'back'.")

        elif action.lower() == "search":
            pokemon_list = fetch_pokemon_list()
            if isinstance(pokemon_list, list):  # Ensure list was fetched successfully
                query = input("Enter partial Pokémon name to search: ")
                matches = search_pokemon_list(query, pokemon_list)
                if isinstance(matches, list):
                    print("\n".join(matches))
                else:
                    print(matches)  # "No Pokémon match your search."
            else:
                print(pokemon_list)  # Display error message
            print()

        elif action.lower() == "exit":
            print("Goodbye!")
            break
        else:
            print("Invalid action. Please choose 'Dex', 'Search', or 'Exit'.")

"""