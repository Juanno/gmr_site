from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from django.shortcuts import get_object_or_404, render
from .accueil import Accueil
from .models import Articles, Infos, Calendrier, QuiSommmesNous
from django.shortcuts import render, redirect
from .sejour import DetailSejour

def index(request):
    all_accueil = Accueil.objects.all()
    print(all_accueil)
    template = loader.get_template('blog/index.html')
    context = {
        'all_accueil': all_accueil
    }
    return HttpResponse(template.render(context, request))

def article(request, article_id):
    article = get_object_or_404(Articles, pk=article_id)
    return render(request, 'blog/article.html', {'article':article})
