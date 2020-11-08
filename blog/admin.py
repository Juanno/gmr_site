from django.contrib import admin
from .association import Bureau, Adhesion, Formation, ReglementInterieur
from .manifestations import Manifestation
from .photos import PhotosArticle, PostImage
from .randonnees import RandosCartotheque, RandosCommandement, RandosCalendrier, RandosAnimateur
from .sejour import DetailSejour
from .actualites import Actualites
from .accueil import Accueil


admin.site.register(Bureau)
admin.site.register(Adhesion)
admin.site.register(Formation)
admin.site.register(ReglementInterieur)

admin.site.register(Manifestation)

class PostImageAdmin(admin.StackedInline):
    model = PostImage

@admin.register(PhotosArticle)
class PostAdmin(admin.ModelAdmin):
    inlines = [PostImageAdmin]

    class Meta:
       model = PhotosArticle

@admin.register(PostImage)
class PostImageAdmin(admin.ModelAdmin):
    pass

admin.site.register(RandosCartotheque)
admin.site.register(RandosCommandement)
admin.site.register(RandosCalendrier)
admin.site.register(RandosAnimateur)

admin.site.register(DetailSejour)

admin.site.register(Actualites)

admin.site.register(Accueil)






