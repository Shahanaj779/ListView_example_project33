from django.shortcuts import render

# Create your views here.
from django.views.generic import ListView
from app.models import *
    
class Trainer_List(ListView):
    model=Trainer

    template_name='Trainer_List.html'

    context_object_name='tl'
    #queryset=Trainer.objects.filter(trainer_name='Rakesh')
    ordering=['trainer_name']

