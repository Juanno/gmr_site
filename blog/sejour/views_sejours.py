from django.shortcuts import get_object_or_404, render
from .sejour import DetailSejour

def sejours(request, sejour_id):
    sejours = DetailSejour.objects.filter(pk=sejour_id)
    return render(request, 'blog/sejours/sejours.html', {'sejours': sejours})