from django.shortcuts import get_object_or_404, render
from .manifestations import Manifestation

def manifestations(request):
    manifestations = Manifestation.objects.all()
    return render(request, 'blog/manifestations/manifestations.html', {'manifestations':manifestations})