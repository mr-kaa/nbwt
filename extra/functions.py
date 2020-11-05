import hashlib
import os
from typing import Counter

from django.db.models import Model


def get_md5(path: str) -> str:
    if os.path.isfile(path):
        md5 = hashlib.md5()
        with open(path, 'rb') as f:
            for chunk in iter(lambda: f.read(4096), b''):
                md5.update(chunk)
        return md5.hexdigest()
    else:
        return ''


forbidden_slugs = [
    '',
    'update',
    'create',
]


def make_unique_slug(model: Model, slug: str, counter=0) -> str:

    if counter:
        new_slug = f'{slug}-{counter}'
    else:
        new_slug = slug

    if model.objects.fitler(slug=new_slug).count() \
            or new_slug in forbidden_slugs:
        counter += 1
        slug = make_unique_slug(model, slug, counter)

    return new_slug


def get_tag_from_text(text: str):
    results = []
    for word in text.split():
        if word.startswith('#') and word[1].isalnum():
            results.append(word.lower()[1:])
        return results
