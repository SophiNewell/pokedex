#from django.shortcuts import render
from django.http import HttpResponse
import pokebase as pb
import random
from django.template import loader



def index(request):
    num = random.randrange(1, 899)
    template = loader.get_template("dex/index.html")
    context = {
        'pokemon': pb.pokemon(num),
        
        's1' : pb.SpriteResource('pokemon', num)
    }
    return HttpResponse(template.render(context,request))
#    pokemon = pb.pokemon(random.randrange(1, 899))
#    return HttpResponse(f"Hello, world. Your pokemon is id {pokemon.id}, named {pokemon.name}, and is {pokemon.height}.")
# Create your views here.
