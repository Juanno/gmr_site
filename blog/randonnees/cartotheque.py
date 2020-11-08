from django.db import models
from tinymce.models import HTMLField


class RandosCartotheque(models.Model):

    class Meta:
        verbose_name = 'Cartothèque IGN'
        verbose_name_plural = 'Cartothèque IGN'

    name = models.CharField(max_length=50)
    contenu = HTMLField()
    fichier_cartotheque = models.FileField(upload_to='media/')


    def __str__(self):
        return self.name