from django.db import models
from tinymce.models import HTMLField

class DetailSejour(models.Model):
    name = models.CharField(max_length=50)
    contenu = HTMLField()
    sejours_pdf = models.FileField(upload_to='media/')

    class Meta:
        verbose_name = 'Séjours'
        verbose_name_plural = 'Séjours'

    def __str__(self):
        return self.name

#Ajouter un champs photos !