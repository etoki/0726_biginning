# coding: utf-8
from __future__ import unicode_literals
from django.db import models
from django.contrib.auth.models import AbstractUser


class CustomUser(AbstractUser):
    image_url = models.URLField('画像URL', blank=True)
