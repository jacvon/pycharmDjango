from django.db import models


class User(models.Model):
    username = models.TextField()
    nickname = models.TextField()