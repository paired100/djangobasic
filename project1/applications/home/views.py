from django.shortcuts import render
from django.views.generic import TemplateView, ListView

from .models import Prueba
# Create your views here.
class IndexView(TemplateView):
    template_name = 'home/home.html'
    
class pruebaListView(ListView):
    template_name = 'home/lista.html'
    queryset = ['a','b','c']
    context_object_name = 'lista_prueba'
    

class ModelPruebaListView(ListView):
    model = Prueba
    template_name='home/prueba.html'
    context_object_name = 'lita_prueba'