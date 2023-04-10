from django.db import models
from django.urls import reverse

# Create your models here.
class Rock(models.Model):
    name= models.CharField(max_length=100)
    type= models.CharField(max_length=100)
    description= models.CharField(max_length=250)

    def get_absolute_url(self):
        return reverse('detail', kwargs={'rock_id':self.id})