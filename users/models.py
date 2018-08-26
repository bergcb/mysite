from django.db import models
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.models import User


class MyUser(AbstractUser):
    nickname = models.CharField(max_length=50, blank=True)
    test = models.PositiveIntegerField(default=0)
    # user = models.OneToOneField(User)

    class Meta(AbstractUser.Meta):
        pass