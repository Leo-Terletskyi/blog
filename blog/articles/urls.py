from django.urls import path

from . import views

urlpatterns = [
    path('', views.HomePage.as_view(), name='home_page'),
    path('articles/<slug:slug>/', views.ArticleDetail.as_view(), name='article_detail'),


]
