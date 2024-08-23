from rest_framework import serializers
from .models import Document


class DocumentSerializer(serializers.ModelSerializer):
    """ Сериализатор для загружаемых документов. """

    class Meta:
        model = Document
        fields = ('id', 'user', 'file', 'uploaded_at', 'is_approved', 'is_rejected')
