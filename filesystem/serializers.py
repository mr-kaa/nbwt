from rest_framework import serializers
from filesystem.models import File, Hash


class FileSerializer(serializers.HyperlinkedModelSerializer):
    # class FileSerializer(serializers.ModelSerializer):
    # author = serializers.ReadOnlyField(source='author.username')

    # url = serializers.HyperlinkedIdentityField(
    #     view_name='files',
    #     lookup_field='slug'
    # )
    # author = serializers.HyperlinkedRelatedField(
    #     view_name='author-detail',
    #     lookup_field='id',
    #     many=True,
    #     read_only=True
    # )

    # author = serializers.RelatedField(many=False)

    class Meta:
        model = File
        fields = [
            'id',
            'name',
            'url',
            'slug',
            # 'author'
        ]
        depth = 1
        # exclude = [
        #     'author'
        # ]
        lookup_field = 'slug'

        extra_kwargs = {
            'slug': {'read_only': True},
            'url': {'lookup_field': 'slug'},
            # 'author': {'lookup_field': 'author.pk'},
            # 'tags':  {'lookup_field': 'tags.slug'},
        }


class HashSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Hash
        fields = '__all__'
