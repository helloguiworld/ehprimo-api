from django.db import models
from django.conf import settings

class Player(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    record = models.PositiveSmallIntegerField(default=0)
    last_update = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.user.username