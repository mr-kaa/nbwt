import uuid

from django.db import models
from django.contrib.auth.models import User

from tags.models import Tag
from extra.functions import \
    get_md5, \
    make_unique_slug, \
    get_tag_from_text

# Create your models here.


class Hash(models.Model):
    md5 = models.CharField(
        max_length=255,
        verbose_name='File hash (md5)',
        unique=True
    )


class File(models.Model):
    author = models.ForeignKey(
        User,
        on_delete=models.PROTECT,
        related_name='file_author',
        verbose_name='Author'
    )
    name = models.CharField(
        max_length=255,
        verbose_name='Name',
        null=True,
        blank=True,
        default=None
    )
    file_type = models.CharField(
        max_length=255,
        verbose_name='Type',
        null=True,
        blank=True,
        default=None
    )
    md5 = models.ForeignKey(
        Hash,
        null=True,
        blank=True,
        default=None,
        on_delete=models.PROTECT,
        related_name='files',
        verbose_name='Hash'
    )
    slug = models.SlugField(
        default='_',
        max_length=64,
        verbose_name='Slug',
        unique=True,
        db_index=True
    )
    descriptions = models.TextField(
        verbose_name='Descriptions',
        blank=True,
        default=None
    )
    add_time = models.DateTimeField(
        verbose_name='Add time',
        auto_now_add=True,

    )
    tags = models.ManyToManyField(
        Tag,
        blank=True,
        default=None,
        related_name='files',
        verbose_name='Tags'
    )
    file = models.FileField(
        upload_to='files/%Y/%m/%d',
        blank=True,
        verbose_name='File'
    )
    is_deleted = models.BooleanField(
        default=False,
        verbose_name='Hide file'
    )
    identical_file = models.ForeignKey(
        'self',
        on_delete=models.PROTECT,
        blank=True,
        default=None,
        related_name='clones',
        verbose_name='Previously created identical file'
    )
    path = models.FilePathField(
        path='/home/usr/media/files',
        null=True,
        blank=True,
        default=None
    )

    @property
    def __path(self) -> str:
        if not self.is_clone:
            return './media/' + self.file.name
        else:
            return self.identical_file.path

    def get_hash(self) -> None:
        md5 = get_md5(self.path)
        try:
            self.hash = Hash.objects.get(md5=md5)
        except Exception:
            hash = Hash(md5=md5)
            hash.save()
            self.md5 = hash

    def get_tags_from_descriptions(self) -> None:
        tags_name_list = get_tag_from_text(self.descriptions)

    def save(self, *args, **kwargs) -> None:
        no_id_flag = False
        if not self.id:
            no_id_flag = True
            if not self.name:
                self.name = uuid.uuid1().__str__()
                self.slug = self.name
        else:
            self.get_tags_from_descriptions()

        super().save(*args, **kwargs)
        if no_id_flag:
            if self.file:
                pass

            pass
