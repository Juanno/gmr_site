from .sejour import DetailSejour
from .actualites import Actualites

def all_sejours(request):
    all_sejours = DetailSejour.objects.all()
    return {'all_sejours': all_sejours}


def all_actu(reqest):
    all_actu = Actualites.objects.all()
    return {'all_actu': all_actu }