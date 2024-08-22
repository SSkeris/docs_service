from rest_framework import serializers
from django.contrib.auth.hashers import make_password
from django.contrib.auth import get_user_model

User = get_user_model()


class UserSerializer(serializers.ModelSerializer):
    """ Сериализатор для пользователя. """

    class Meta:
        model = User
        fields = ('id', 'email', 'password')
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        """ Создание пользователя с хэшированным паролем для хранения в БД. """

        validated_data['password'] = make_password(validated_data['password'])
        user = User.objects.create(**validated_data)
        return user
