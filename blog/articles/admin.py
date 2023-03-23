from django.contrib import admin
from django.utils.safestring import mark_safe

from .models import Category, Article


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    exclude = ('slug',)


@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'category', 'author', 'updated_at', 'get_image')
    list_display_links = ('title',)
    exclude = ('author', 'slug')
    readonly_fields = ('get_image',)
    search_fields = ('title', 'content')
    list_filter = ('author',)
    list_per_page = 5

    def get_image(self, obj):
        if obj.image:
            return mark_safe(f"<img src={obj.image.url} width=100>")
        else:
            return '-'

    get_image.short_description = 'image'

    def save_model(self, request, obj, form, change):
        if not change:
            obj.author = request.user
        super().save_model(request, obj, form, change)
