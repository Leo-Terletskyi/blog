from django.urls import path

from . import views

urlpatterns = [
    path('', views.HomePage.as_view(), name='home_page'),
    path('articles/<slug:slug>/', views.ArticleDetail.as_view(), name='article_detail'),
    path('categories/<slug:slug>/', views.CategoryList.as_view(), name='category_list'),
    path('register/', views.register_user, name='register'),
    path('login/', views.login_user, name='login'),
    path('logout/', views.logout_user, name='logout'),
    path('add-new-article/', views.ArticleCreateView.as_view(), name='add_new_article'),
    path('search/', views.SearchListView.as_view(), name='search'),


]
