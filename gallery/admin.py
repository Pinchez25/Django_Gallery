from django.contrib import admin
from django.contrib.admin import ModelAdmin

from .models import Category, Photo


# Register your models here.
@admin.register(Category)
class CategoryAdmin(ModelAdmin):
    pass


@admin.register(Photo)
class PhotoAdmin(ModelAdmin):
    pass
