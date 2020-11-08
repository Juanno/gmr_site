from django.shortcuts import get_object_or_404, render
from .adhesion import Adhesion
from .bureau import Bureau
from .formation import Formation
from .reglement import ReglementInterieur


def adhesion(request):
    adhesion = get_object_or_404(Adhesion)
    return render(request, 'blog/asso/adhesion.html', {'adhesion':adhesion})


def bureau(request):
    bureau = get_object_or_404(Bureau)
    return render(request, 'blog/asso/bureau.html', {'bureau':bureau})


def formation(request):
    formation = get_object_or_404(Formation)
    return render(request, 'blog/asso/formation.html', {'formation': formation})


def reglement(request):
    reglement = get_object_or_404(ReglementInterieur)
    return render(request, 'blog/asso/reglement.html', {'reglement': reglement})