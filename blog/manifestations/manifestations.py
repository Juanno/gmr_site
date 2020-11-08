from django.db import models
from tinymce.models import HTMLField


class Manifestation(models.Model):
    name = models.CharField(max_length=500)
    contenu = HTMLField()

    class Meta:
        verbose_name = 'Manifestations'
        verbose_name_plural = 'Manifestations'

    def __str__(self):
        return self.name

# Ajouter 2-3 champs pdf en anticipations