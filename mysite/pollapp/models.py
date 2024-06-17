from django.db import models

class Lenguaje(models.Model):
    id = models.AutoField(primary_key=True)  # Cambiar a AutoField
    nombre = models.CharField(max_length=50, unique=True)
    code = models.CharField(max_length=50, unique=True, blank=False)
    votos = models.PositiveIntegerField(default=0)

    def __str__(self):
        return self.nombre