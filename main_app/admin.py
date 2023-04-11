from django.contrib import admin

# Register your models here.
from .models import Rock, Observation

admin.site.register(Rock)
admin.site.register(Observation)
