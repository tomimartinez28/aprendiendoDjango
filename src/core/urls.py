from django.urls import path, include
from core import views  

#app_name = 'core'


urlpatterns = [
    path('', views.indexView, name = 'index'),

    # includes
    path('publicaciones/', include('publicaciones.urls')),
    path('usuarios/', include('usuarios.urls')),
    path('contacto/', include('contacto.urls'))
]  
