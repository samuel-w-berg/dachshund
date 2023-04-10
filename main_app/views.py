from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
from .models import Rock



def home(request):
  return render(request, 'home.html')

def rocks_index(request):
  rocks = Rock.objects.all()
  return render(request, 'rocks/index.html', {'rocks':rocks})

def rocks_detail(request, rock_id):
   rock = Rock.objects.get(id=rock_id)
   return render(request, 'rocks/detail.html', {'rock': rock})