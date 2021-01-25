from rest_framework.fields import SerializerMethodField
from rest_framework.serializers import ModelSerializer

from sharing.models import ShareableFile


class ShareableFileListSerializer(ModelSerializer):
    url = SerializerMethodField('get_raw_url')

    def get_raw_url(self, obj):
        return obj.get_raw_url()

    class Meta:
        model = ShareableFile
        fields = [
            'name',
            'hash',
            'url',
            'public',
        ]


class ShareableFileDetailSerializer(ModelSerializer):
    url = SerializerMethodField('get_raw_url')

    def get_raw_url(self, obj):
        return obj.get_raw_url()

    class Meta:
        model = ShareableFile
        read_only_fields = (
            'hash',
            'url',
        )
        fields = [
            'name',
            'hash',
            'url',
            'public',
        ]


class ShareableFileCreateSerializer(ModelSerializer):
    class Meta:
        model = ShareableFile
        read_only_fields = (
            'user',
        )
        fields = [
            'file',
            'user',
            'public',
        ]
