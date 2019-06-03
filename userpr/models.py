from django.contrib.auth.models import User
from django.dispatch import receiver
from allauth.account.signals import user_signed_up
from django.db import models


class Userpr(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE,primary_key=True)
    full_name = models.CharField(default=None, max_length=255)
    email = models.CharField(default=None, max_length=500)

    def __str__(self):
        return self.user.username

    #@receiver(user_signed_up)
    #def populate_profile(sociallogin, user, **kwargs):

        #user.profile = Userpr()
