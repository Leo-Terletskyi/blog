from django.db.models import Count
from django.shortcuts import render
from django.views import generic

from .models import Category, Article


class HomePage(generic.ListView):
    model = Article
    context_object_name = 'articles'
    template_name = 'articles/home_page.html'
    queryset = Article.objects.all().select_related('category', 'author')

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(object_list=None, **kwargs)
        context['categories'] = Category.objects.all().annotate(count_articles=Count('article'))
        return context
