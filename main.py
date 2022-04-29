from operator import truediv
import pokebase as pb
import random
# check if user passed in a pokemon ID or name
# if ID or name--get that pokemon
# if not -- random

user_pokemon = input("Type the name of a pokemon, or press enter to continue! ")
while True:
    if user_pokemon != "":
        try:
            pokemon = pb.pokemon(user_pokemon)
            pokemon_id = pokemon.id
        except AttributeError:
            user_pokemon = input("We couldn't find a pokemon with that name. please try again. ")
            continue
    else:
        pokemon = pb.pokemon(random.randrange(1, 899))
    poke = pb.pokemon(898)

    # If pokemon has evolutions, link or suggest those
    # Create a UI
    break
print(pokemon.id)
print(pokemon.name)
    
# Handle typos or nonexistant pokemon
# figure out how to get sprites
