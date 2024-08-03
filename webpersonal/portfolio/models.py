from django.db import models

# Create your models here.
class Project(models.Model):
    title=models.CharField(max_length=200,verbose_name="Título")
    description=models.TextField(verbose_name="Descripción")
    image=models.ImageField(verbose_name="Imagen", upload_to="projects")
    created=models.DateTimeField(auto_now_add=True,verbose_name="Fecha de creación") #este se ejecuta una sola vez
    updated=models.DateTimeField(auto_now=True,verbose_name="Fecha de la última edición") #este cada vez que se modifique
    url=models.URLField(max_length=200, null=True, blank=True, verbose_name="Link para más informacion")

    class Meta:
        verbose_name="proyecto"
        verbose_name_plural="proyectos"
        ordering=["-created"]

    def __str__(self):
        return self.title