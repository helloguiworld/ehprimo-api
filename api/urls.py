from rest_framework import routers
from django.urls import path, include
from api.viewsets import PlayerViewSet, AuthenticatedUserView

router = routers.DefaultRouter()
router.register(r'players', PlayerViewSet)

urlpatterns = [
    path('api/auth-user/', AuthenticatedUserView.as_view(), name='authenticated-user'),
    path("api/v1/", include(router.urls)),
]