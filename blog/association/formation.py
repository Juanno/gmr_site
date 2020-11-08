from django.db import models
from tinymce.models import HTMLField


class Formation(models.Model):
    name = models.CharField(max_length=500)
    contenu = HTMLField()

    class Meta:
        verbose_name = 'Formations'
        verbose_name_plural = 'Formations'

    def __str__(self):
        return self.name