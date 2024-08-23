from rest_framework import viewsets, permissions
from .models import User
from .serializers import UserSerializer


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]
    #  параметры доступа не указаны в тз, прикрыл авторизацией, предполагая,
    #  что программа написана не для общественного доступа, а внутри организации
