from django.contrib import admin
from . import models


class ContentInline(admin.TabularInline):
    model = models.Content


@admin.register(models.Content)
class AdminContent(admin.ModelAdmin):
    pass


@admin.register(models.Page)
class AdminPage(admin.ModelAdmin):
    inlines = [ContentInline, ]
