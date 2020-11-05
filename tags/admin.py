from django.contrib import admin

# Register your models here.

from tags import models

@admin.register(models.Tag)
class TagAdmin(admin.ModelAdmin):
    list_per_page = 20
