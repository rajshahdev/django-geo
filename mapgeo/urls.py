from django.urls import path
from .views import mapview, download
urlpatterns = [
    path('home/',mapview),
    path('img/',download,name='download')
]