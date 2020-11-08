from django.shortcuts import get_object_or_404, render
from .actu import Actualites


def actu(request):
    adhesion = get_object_or_404(Actualites)
    return render(request, 'blog/actu/adhesion.html', {'adhesion': adhesion})
