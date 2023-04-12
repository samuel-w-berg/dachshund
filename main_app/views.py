from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import DetailView, ListView
# Create your views here.
from .models import Rock, Mineral
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
   # find all minerals that are not in the rock, then get just their ids
   minerals_rock_lacks = Mineral.objects.exclude(id__in = rock.minerals.all().values_list('id'))
   observation_form = ObservationForm()
   return render(request, 'rocks/detail.html', {'rock': rock, 'observation_form': observation_form, 'minerals': minerals_rock_lacks})


# Minerals functions

class MineralList(ListView):
  model = Mineral

class MineralDetail(DetailView):
  model = Mineral

class MineralCreate(CreateView):
  model = Mineral
  fields = '__all__'

class MineralUpdate(UpdateView):
  model = Mineral
  fields = ['name']

class MineralDelete(DeleteView):
  model = Mineral
  success_url = '/minerals/'


def assoc_mineral(request, rock_id, mineral_id):
  Rock.objects.get(id=rock_id).minerals.add(mineral_id)
  return redirect('detail', rock_id=rock_id)