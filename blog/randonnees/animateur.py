from django.db import models
from tinymce.models import HTMLField

class RandosAnimateur(models.Model):

    class Meta:
        verbose_name = 'Animateurs rando'
        verbose_name_plural = 'Animateurs rando'

    name = models.CharField(max_length=50)
    contenu = HTMLField()

    def __str__(self):
        return self.name