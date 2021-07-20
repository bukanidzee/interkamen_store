from django.contrib.auth.models import AbstractUser


class CustomUser(AbstractUser):

    class Meta(AbstractUser.Meta):
        ordering = ['username']
