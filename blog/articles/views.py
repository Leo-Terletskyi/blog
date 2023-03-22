from django.db.models import Count
from django.shortcuts import render, get_object_or_404
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


class ArticleDetail(generic.DetailView):
    model = Article
    slug_url_kwarg = 'slug'
    context_object_name = 'article'
    template_name = 'articles/article_detail.html'

    def get_object(self, queryset=None):
        return get_object_or_404(Article.objects.select_related('category', 'author'), slug=self.kwargs.get('slug'))

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(object_list=None, **kwargs)
        context['categories'] = Category.objects.all().annotate(count_articles=Count('article'))
        return context


class CategoryList(generic.ListView):
    model = Article
    context_object_name = 'articles'
    template_name = 'articles/category.html'

    def get_queryset(self):
        return Article.objects.filter(category__slug=self.kwargs.get('slug')).select_related('category', 'author')

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(object_list=None, **kwargs)
        context['categories'] = Category.objects.all().annotate(count_articles=Count('article'))
        context['title'] = self.kwargs.get('slug')
        return context


