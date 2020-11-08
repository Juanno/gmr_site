from django.shortcuts import get_object_or_404, render
from .photos import PhotosArticle, PostImage

def photos(request):
    articles = PhotosArticle.objects.all()
    photos = PostImage.objects.all()
    return render(request, 'blog/photos/photos.html', {'articles':articles, 'photos':photos})