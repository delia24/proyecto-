from django.db import models

# Create your models here.
class jugador (models.Model):
	nombre=models.CharField(max_length=200)
	apellidos=models.CharField(max_length=200)
	direccion=models.CharField(max_length=200)
	telefono=models.IntegerFiel()
	email=models.EmailField(max_length=75)
	ci=models.IntegerFiel(unique=True)
	fecha=models.DateTimeField(auto_now=True)
	def __unicode__(self):
		return "%s "%(self.nombre) 

