import pokebase as pb
import random
# check if user passed in a pokemon ID or name
# if ID or name--get that pokemon
# if not -- random
user_pokemon = input()
if input != "":
    pokemon = pb.pokemon(user_pokemon)
#else:
#     pokemon = pb.pokemon(random.range(899))
poke = pb.pokemon(898)

# If pokemon has evolutions, link or suggest those
# Create a UI