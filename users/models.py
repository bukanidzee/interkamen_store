from django.contrib.auth.models import AbstractUser


class CustomUser(AbstractUser):

    class Meta(AbstractUser.Meta):
        ordering = ['username']

    def __str__(self):
        return self.username
