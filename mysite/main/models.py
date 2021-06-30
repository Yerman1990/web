from django.db import models

class Curso(models.Model):
    titulo=models.CharField(max_length=200)
    contenido=models.TextField()
    publicado=models.DateField("fecha de publicacion")

    def  _str_(self):
        return self.titulo
        
    
