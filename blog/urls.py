from django.urls import path
from . import views
from .randonnees import views_rando
from .sejour import views_sejours
from .photos import views_photo
from .association import views_asso
from .manifestations import views_manif
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.index, name='index'),
    path('calendrier/', views_rando.calendrier, name='calendrier'),
    path('animateurs/', views_rando.animateurs, name='animateurs'),
    path('commandement/', views_rando.commandement, name='commandement'),
    path('cartotheque/', views_rando.cartotheque, name='cartotheque'),
    path('sejours/<int:sejour_id>', views_sejours.sejours, name='sejours'),
    path('photos/', views_photo.photos, name='photos'),
    path('adhesion/', views_asso.adhesion, name='adhesion'),
    path('bureau/', views_asso.bureau, name='bureau'),
    path('formation/', views_asso.formation, name='formation'),
    path('reglement/', views_asso.reglement, name='reglement'),
    path('manifestations/', views_manif.manifestations, name='manifestations'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)