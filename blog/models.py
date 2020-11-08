from django.db import models
from tinymce.models import HTMLField


class Articles(models.Model):
    titre = models.CharField(max_length=200)
    pub_date = models.DateField('date published')
    content = HTMLField()

    def __str__(self):
        return self.titre

class Infos(models.Model):
    titre = models.CharField(max_length=200)
    pub_date = models.DateField('date published')
    content = HTMLField()
    INFO_TYPE = [
        ('gr', 'general'),
        ('ra', 'randonnees'),
        ('ma', 'materiel'),
    ]
    type_infos = models.CharField(max_length=30, choices=INFO_TYPE, default='gr')

    def __str__(self):
        return self.titre

class QuiSommmesNous(models.Model):
    titre = models.CharField(max_length=200)
    pub_date = models.DateField('date published')
    content = HTMLField()

    def __str__(self):
        return self.titre

class Calendrier(models.Model):
    titre = models.CharField(max_length=200)
    pub_date = models.DateField('date published')
    image = models.ImageField(upload_to="media", null=False)
    content = HTMLField()

    # trois fichiers un par groupe :
    #     chamoix - marmotte - rando santé

    def __str__(self):
        return self.titre


#Séjours unique pour été et pour hiver.
#Galerie photos à prévoir  X photos.