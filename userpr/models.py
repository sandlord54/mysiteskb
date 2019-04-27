from django.db import models
from django.contrib.auth.models import AbstractBaseUser


class Userpr(models.Model):
    username = models.CharField('username',max_length=150,unique=True,db_index=True)
    password = models.CharField('password',db_index=True,max_length=120)
    email = models.EmailField('Email',unique=True,max_length=150)

    def __str__(self):
        return self.username
