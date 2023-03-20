from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework import status
from rest_framework.exceptions import NotAuthenticated, ValidationError

from api.models import Player
from api.serializers import \
    PlayerSerializer, \
    PlayerRecordSerializer, \
    ReadPlayerSerializer, \
    PlayerUserSerializer, \
    CustomUserSerializer
from api.permissions import IsUserDataOrAdminUserOrReadOnly

class PlayerPermission(IsUserDataOrAdminUserOrReadOnly):
    def has_permission(self, request, view):
        return True if view.action == "register" else super().has_permission(request, view)


class PlayerViewSet(viewsets.ModelViewSet):
    queryset = Player.objects.all()
    permission_classes = (PlayerPermission,)

    # serializer_class = PlayerSerializer
    def get_serializer_class(self):
        if(self.request.method == 'GET'):
            return ReadPlayerSerializer
        elif(self.action == 'new_record'):
            return PlayerRecordSerializer
        else:
            return PlayerSerializer

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

    @action(methods=['get'], detail=False, name='Auth Player User')
    def auth_user(self, request):
        print(request)
        if request.user and request.user.is_authenticated:
            playerUserSerializer = PlayerUserSerializer(request.user)
            return Response(playerUserSerializer.data)
        raise NotAuthenticated()

    @action(methods=['post'], detail=False, url_path='auth_user/new_record')
    def new_record(self, request):
        print(request)
        new_record = request.data['record']
        if(new_record.isdigit()):
            if request.user and request.user.is_authenticated:
                player = Player.objects.get(user=request.user)
                player.record = new_record
                player.save()
                playerSerializer = PlayerSerializer(player)
                return Response(playerSerializer.data)
            raise NotAuthenticated()
        raise ValidationError("New record must be a positive integer value.")
        
