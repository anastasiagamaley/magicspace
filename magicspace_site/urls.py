from django.contrib import admin
from django.urls import path
from pages import views as pages_views
from pages.views import index, contact_submit

urlpatterns = [
    path('admin/', admin.site.urls),

    # HOME
    path('', pages_views.index, name='home'),

    # DULA
    path('dula/', pages_views.dula, name='dula'),
    path('dula/kontrakcie/', pages_views.kontrakcie, name='kontrakcie'),
    path('dula/cerrada/', pages_views.cerrada, name='cerrada'),
    path('dula/porodny-kurz/', pages_views.porodny_kurz, name='porodny_kurz'),

    # JOGA – твои новые короткие ссылки
    path('jogamartin/', pages_views.joga_martin, name='joga_martin'),
    path('korp/', pages_views.korp, name='korp'),

    # ABOUT & CONTACT
    path('o-mne/', pages_views.o_mne, name='o_mne'),
    path('kontakt/', pages_views.kontakt, name='kontakt'),
]


