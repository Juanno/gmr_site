from django.db import models
from tinymce.models import HTMLField


class PhotosArticle(models.Model):

    name = models.CharField(max_length=50)
    contenu = HTMLField()
    default = models.BooleanField(default=False)

    class Meta:
        verbose_name = 'Galerie de photos'
        verbose_name_plural = 'Galerie de photos'

    def __str__(self):
        return self.name

class PostImage(models.Model):
    post = models.ForeignKey(PhotosArticle, default=None, on_delete=models.CASCADE)
    images = models.FileField(upload_to = 'images/')

    class Meta:
        verbose_name = 'Article à ne pas toucher !'
        verbose_name_plural = 'Article à ne pas toucher !'

    def __str__(self):
        return self.post.name

