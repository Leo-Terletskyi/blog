from django.contrib.auth import get_user_model
from django.db import models
from django.template.defaultfilters import slugify
from django.urls import reverse

from ckeditor.fields import RichTextField

user = get_user_model()


class Category(models.Model):
    name = models.CharField(max_length=32, unique=True)
    slug = models.SlugField(null=True, blank=True)

    def get_absolute_url(self):
        return reverse('category_list', kwargs={'slug': self.slug})

    def save(self, force_insert=False, force_update=False, using=None, update_fields=None):
        if not self.slug:
            self.slug = slugify(self.name)
        return super().save(force_insert=False, force_update=False, using=None, update_fields=None)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'
        ordering = ('name',)


class Article(models.Model):
    title = models.CharField(max_length=64, unique=True)
    slug = models.SlugField(null=True, blank=True)
    content = RichTextField()
    image = models.ImageField(upload_to='static/article_images')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    author = models.ForeignKey(user, on_delete=models.CASCADE)

    def get_absolute_url(self):
        return reverse('article_detail', kwargs={'slug': self.slug})

    def save(self, force_insert=False, force_update=False, using=None, update_fields=None):
        if not self.slug:
            self.slug = slugify(self.title)
        return super().save(force_insert=False, force_update=False, using=None, update_fields=None)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Article'
        verbose_name_plural = 'Articles'
        ordering = ('-updated_at', '-created_at')


