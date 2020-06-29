from django.db import models
from django.core import validators

# Create your models here.
class User(models.Model):
    name = models.CharField('Name', max_length=50)
    last_login = models.DateTimeField('Last Login', auto_now=True)
    email = models.EmailField('E-mail', max_length=254)
    password = models.CharField('Password', max_length=50)


class Agent(models.Model):
    name=models.CharField(max_length=50)
    status=models.BooleanField()
    env=models.CharField(max_length=20)
    version=models.CharField(max_length=5)
    address=models.CharField(max_length=39)


class Event(models.Model):
    level=models.CharField(['CRITICAL', 'DEBUG', 'ERROR', 'INFO'], max_length=20)
    data=models.TextField()
    arquivado=models.BooleanField()
    date=models.DateField(auto_now_add=True)
    agent=models.ForeignKey(
        Agent,
        on_delete=models.deletion.DO_NOTHING)
    user=models.ForeignKey(
        User,
        on_delete=models.deletion.DO_NOTHING,
    )


class Group(models.Model):
    name=models.CharField(max_length=50)


class GroupUser(models.Model):
    group=models.ForeignKey(
        Group,
        on_delete=models.deletion.DO_NOTHING,
    )
    user=models.ForeignKey(
        User,
        on_delete=models.deletion.DO_NOTHING,
    )