from django.shortcuts import get_object_or_404, render
from .calendrier import RandosCalendrier
from .animateur import RandosAnimateur
from .commandement import RandosCommandement
from .cartotheque import RandosCartotheque


def calendrier(request):
    calendrier = get_object_or_404(RandosCalendrier)
    return render(request, 'blog/rando/calendrier.html', {'calendrier':calendrier})


def animateurs(request):
    animateurs = get_object_or_404(RandosAnimateur)
    return render(request, 'blog/rando/animateurs.html', {'animateurs':animateurs})


def commandement(request):
    commandement = get_object_or_404(RandosCommandement)
    return render(request, 'blog/rando/commandement.html', {'commandement': commandement})


def cartotheque(request):
    cartotheque = get_object_or_404(RandosCartotheque)
    return render(request, 'blog/rando/cartotheque.html', {'cartotheque': cartotheque})