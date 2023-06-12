from django.shortcuts import render, get_object_or_404
from .models import Publicacion

def render_publicaciones(request):
    publicacion = Publicacion.objects.all()
    return render (request,'publicaciones.html', {'publicacion':publicacion} )
    
    
    
def publicacion_detalle (request,publicacion_id):
    posteo= get_object_or_404 (Publicacion, pk=publicacion_id)
    return render (request, 'publicacion_detalle.html',{"publicacion":posteo})    