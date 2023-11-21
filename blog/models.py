from django.db import models
from django.urls import reverse

# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=200)
    author = models.ForeignKey(
    #CASCADE permite la actualización para todos los registros relacionados en una tabla
    #permitiendo la consistencia para todos los usuarios
      'auth.User',
       on_delete=models.CASCADE, 
    )
    body = models.TextField(default='Escribe aqui')

    def __str__(self):
      return self.title

    def get_absolute_url(self):
      return reverse('post_detail', args =[str(self.id)])

