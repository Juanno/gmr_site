from django.db import models
from tinymce.models import HTMLField

class Accueil(models.Model):
    name = models.CharField(max_length=50)
    contenu = HTMLField()
    image = models.ImageField(upload_to='media/')

    class Meta:
        verbose_name = 'Accueil'
        verbose_name_plural = 'Accueil'

    def __str__(self):
        return self.name
