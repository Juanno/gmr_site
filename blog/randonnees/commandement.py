from django.db import models
from tinymce.models import HTMLField


class RandosCommandement(models.Model):

    class Meta:
        verbose_name = 'Commandement du Randonneur'
        verbose_name_plural = 'Commandement du Randonneur'

    name = models.CharField(max_length=500)
    contenu = HTMLField()

    def __str__(self):
        return self.name