from django.db import models
from django.urls import reverse

# Create your models here.
class Rock(models.Model):
    name= models.CharField(max_length=100)
    type= models.CharField(max_length=100)
    description= models.CharField(max_length=250)

    def get_absolute_url(self):
        return reverse('detail', kwargs={'rock_id':self.id})
    
    def __str__(self):
        return f"Name: {self.name}, Type: {self.type}"
    

class Observation(models.Model):
    date= models.DateField()
    observation= models.CharField(max_length=250)
    rock = models.ForeignKey(Rock, on_delete=models.CASCADE)

    def __str__(self):
        return f"Date: {self.date}, Observation: {self.observation}"