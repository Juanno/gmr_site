from django.db import models
from tinymce.models import HTMLField


class RandosCalendrier(models.Model):

    name = models.CharField(max_length=50)
    contenu = HTMLField()
    calendrier_pdf = models.FileField(upload_to='media/')

    class Meta:
        verbose_name = 'Calendrier Semestriel'
        verbose_name_plural = 'Calendrier Semestriel'

    def __str__(self):
        return self.name