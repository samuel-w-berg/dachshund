from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
from .models import Rock



def home(request):
  return HttpResponse('<h1>Hello World!</h1>')

def rocks_index(request):
    rocks = Rock.objects.all()
    return render(request, 'rocks/index.html', {'rocks':rocks})