#from django.shortcuts import render
from django.http import HttpResponse
import pokebase as pb
import random

def index(request):
    pokemon = pb.pokemon(random.randrange(1, 899))
    return HttpResponse(f"Hello, world. Your pokemon is {pokemon.name}.")
# Create your views here.
