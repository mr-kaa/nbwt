from extra.functions import make_unique_slug
from django.db import models

from slugify import slugify

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
        max_length=64,
        verbose_name='Tag slug',
        unique=True,
        db_index=True
    )

    class Meta:
        ordering = ['name']

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs) -> None:
        if not self.id:
            self.slug = make_unique_slug(Tag, slugify(self.name)[:60])
        super().save(*args, **kwargs)
