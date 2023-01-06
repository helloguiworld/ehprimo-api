from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework import status

from api.models import Player
from api.serializers import PlayerSerializer, ReadPlayerSerializer, CustomUserSerializer
from api.permissions import IsUserDataOrAdminUserOrReadOnly

class PlayerPermission(IsUserDataOrAdminUserOrReadOnly):
    def has_permission(self, request, view):
        return True if view.action == "register" else super().has_permission(request, view)


class PlayerViewSet(viewsets.ModelViewSet):
    queryset = Player.objects.all()
    permission_classes = (PlayerPermission,)

    # serializer_class = PlayerSerializer
    def get_serializer_class(self):
        method = self.request.method
        return ReadPlayerSerializer if method == 'GET' else PlayerSerializer

    @action(methods=['post'], detail=False)
    def register(self, request):
        print(request)
        userSerializer = CustomUserSerializer(data=request.data)
        if userSerializer.is_valid():
            user = userSerializer.save()
            playerSerializer = PlayerSerializer(data={"user": user.pk})
            if playerSerializer.is_valid():
                playerSerializer.save()
                return Response(playerSerializer.data, status.HTTP_201_CREATED)
            return Response(playerSerializer.errors, status.HTTP_400_BAD_REQUEST)
        return Response(userSerializer.errors, status.HTTP_400_BAD_REQUEST)
