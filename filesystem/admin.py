from django.contrib import admin

# Register your models here.

from filesystem import models


@admin.register(models.File)
class FileAdmin(admin.ModelAdmin):
    list_per_page = 20


@admin.register(models.Hash)
class HashAdmin(admin.ModelAdmin):
    list_per_page = 20
