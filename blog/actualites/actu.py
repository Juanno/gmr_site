from django.db import models
from tinymce.models import HTMLField

class Actualites(models.Model):
    name = models.CharField(max_length=50)
    contenu = HTMLField()

    class Meta:
        verbose_name = 'Actualités'
        verbose_name_plural = 'Actualités'

    def __str__(self):
        return self.name
