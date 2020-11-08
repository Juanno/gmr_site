from django.db import models
from tinymce.models import HTMLField


class Bureau(models.Model):
    name = models.CharField(max_length=500)
    contenu = HTMLField()

    class Meta:
        verbose_name = 'Bureau'
        verbose_name_plural = 'Bureau'

    def __str__(self):
        return self.name