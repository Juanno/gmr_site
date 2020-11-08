from django.db import models
from tinymce.models import HTMLField


class ReglementInterieur(models.Model):
    name = models.CharField(max_length=50)
    contenu = HTMLField()

    class Meta:
        verbose_name = 'Règlement intérieur'
        verbose_name_plural = 'Règlement intérieur'

    def __str__(self):
        return self.name
