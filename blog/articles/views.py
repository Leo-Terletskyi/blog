from django.shortcuts import render
from django.views import generic

from .models import Category, Article


class HomePage(generic.ListView):
    model = Article
    context_object_name = 'articles'
    template_name = 'articles/home_page.html'
