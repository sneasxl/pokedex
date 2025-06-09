import os

from flask import Flask, render_template, request
from pokeapi import fetch_pokemon_data

app = Flask(__name__)


@app.route('/')
def home():
    return render_template('index.html')


@app.route('/pokemon')
def pokemon():
    name_or_id = request.args.get('name_or_id')
    if not name_or_id:
        return "Error: Missing Pokémon name or ID.", 400

    data = fetch_pokemon_data(name_or_id)

    # Check if data contains an error
    if isinstance(data, str):
        return render_template('pokemon.html', pokemon=None, error=data)

    # Pass Pokémon data to the template
    return render_template('pokemon.html', pokemon=data, error=None)



if __name__ == '__main__':
    app.run(debug=True)
