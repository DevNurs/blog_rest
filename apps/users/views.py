from rest_framework import viewsets

from apps.users.models import User
from apps.users.serializers import UserSerializer, UserSerializerList
from rest_framework.permissions import IsAuthenticated


class UserAPIViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [
        IsAuthenticated,
    ]

    def get_serializer_class(self):
        if self.action in ['list', 'retrieve']:
            return UserSerializerList
        return self.serializer_class
