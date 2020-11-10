from rest_framework import serializers
from tags.models import Tag


class TagSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Tag
        fields = '__all__'

        extra_kwargs = {
            'slug': {'read_only': True},
            'url': {'lookup_field': 'slug'}
        }
