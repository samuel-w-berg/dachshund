from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.views.generic.edit import CreateView, UpdateView, DeleteView
# Create your views here.
from .models import Rock
from .forms import ObservationForm


def add_observation(request, rock_id):
  form = ObservationForm(request.POST)
  if form.is_valid():
    new_observation = form.save(commit=False)
    new_observation.rock_id = rock_id
    new_observation.save()
  return redirect('detail', rock_id=rock_id)


class RockCreate(CreateView):
  model = Rock
  fields = '__all__'


class RockUpdate(UpdateView):
  model = Rock
  fields = ['type', 'description']


class RockDelete(DeleteView):
  model = Rock
  success_url = '/rocks/'


def home(request):
  return render(request, 'home.html')

def rocks_index(request):
  rocks = Rock.objects.all()
  return render(request, 'rocks/index.html', {'rocks':rocks})

def rocks_detail(request, rock_id):
   rock = Rock.objects.get(id=rock_id)
   observation_form = ObservationForm()
   return render(request, 'rocks/detail.html', {'rock': rock, 'observation_form': observation_form})