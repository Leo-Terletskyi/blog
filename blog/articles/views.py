from django.contrib.auth import login, logout, authenticate
from django.db.models import Count, Q
from django.shortcuts import render, get_object_or_404, redirect
from django.views import generic

from .forms import UserRegister, UserLogin, AddArticleForm
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


def register_user(request):
    if request.method == 'POST':
        form = UserRegister(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('home_page')
        return render(request, template_name='auth/register.html', context={'form': form})
    form = UserRegister()
    return render(request, template_name='auth/register.html', context={'form': form})


def login_user(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            form = login(request, user)
            return redirect('home_page')
    form = UserLogin()
    return render(request, 'auth/login.html', {'form': form})


def logout_user(request):
    logout(request)
    return redirect('login')


class ArticleCreateView(generic.CreateView):
    form_class = AddArticleForm
    template_name = 'articles/add_article.html'

    def form_valid(self, form):
        article = form.save(commit=False)
        article.author = self.request.user
        article.save()
        return redirect('home_page')


class SearchListView(generic.ListView):
    model = Article
    template_name = 'articles/search.html'
    context_object_name = 'articles'

    def get_queryset(self):
        q = self.request.GET.get('q')
        qs = Article.objects.filter(Q(title__icontains=q) | Q(content__icontains=q)).select_related('category', 'author')
        return qs

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(object_list=None, **kwargs)
        context['categories'] = Category.objects.all().annotate(count_articles=Count('article'))
        return context



