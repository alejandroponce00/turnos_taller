from django.db import models

class Member(models.Model):
  nombre = models.CharField(max_length=255)
  vehiculo = models.CharField(max_length=255)
  reparacion = models.CharField(max_length=255,null=True )
  
  joined_date = models.DateField(null=True)

  def __str__(self):
    return f"{self.nombre} {self.vehiculo} {self.reparacion}"