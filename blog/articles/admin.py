from django.contrib import admin

from .models import Category, Article


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    exclude = ('slug',)


@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    exclude = ('slug',)


