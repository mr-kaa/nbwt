from django.db import models

# Create your models here.


class Tag(models.Model):
    name = models.CharField(
        max_length=255,
        verbose_name='Tag',
        unique=True,
        db_index=True
    )
    slug = models.SlugField(
        default='_',
        max_length=32,
        verbose_name='Tag slug',
        unique=True,
        db_index=True
    )
