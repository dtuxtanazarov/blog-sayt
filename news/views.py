from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Model2

# Create your views here.

class News_view(ListView):
    model = Model2
    template_name = 'home.html'

class Post_detail(DetailView):
    model = Model2
    template_name = 'detail.html'
    context_object_name = 'post'