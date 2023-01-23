from django.urls import path

from neo_geotat.views import get_regions

urlpatterns = [
    path('', get_regions, name='main_regions'),
]