from django.urls import path, include
from publicaciones import views

app_name = 'publicaciones'


urlpatterns = [
    path('publicaciones/', views.publicacionesView, name = 'publicaciones'),
]

