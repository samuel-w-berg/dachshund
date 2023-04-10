from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.


#Temporary Model
class Rock:  # Note that parens are optional if not inheriting from another class
  def __init__(self, name, type, description):
    self.name = name
    self.type = type
    self.description = description

rocks = [
  Rock('Granite', 'igneous', 'cooled magma with large rock crystals'),
  Rock('Sandstone', 'sedimentary', 'sand is accumulated and packed together over time'),
  Rock('Schist', 'metamorphic', 'foliated layers that are easily flaked off')
]

def home(request):
  return HttpResponse('<h1>Hello World!</h1>')