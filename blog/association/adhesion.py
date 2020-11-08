from django.db import models
from tinymce.models import HTMLField


class Adhesion(models.Model):
    name = models.CharField(max_length=500)
    contenu = HTMLField()
    adhesion_pdf = models.FileField(upload_to='media/')

    class Meta:
        verbose_name = 'Adhésion'
        verbose_name_plural = 'Adhésion'

    def __str__(self):
        return self.name
