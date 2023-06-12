from django.urls import path

from .views import render_publicaciones , publicacion_detalle

app_name = 'blog' 

urlpatterns =[
    
    path('',render_publicaciones,name='publicaciones'),
    path('<int:publicacion_id>', publicacion_detalle, name='publicacion_detalle')
]