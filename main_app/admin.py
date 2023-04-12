from django.contrib import admin

# Register your models here.
from .models import Rock, Observation, Mineral

admin.site.register(Rock)
admin.site.register(Observation)
admin.site.register(Mineral)

