# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from ..login_app.models import User

# Create your models here.
class Poke(models.Model):
    # pokes = models.IntegerField(default=0)
    # poker = models.ForeignKey(User, related_name='ipoked')
    # poked = models.ForeignKey(User, related_name='gotpoke')
    pokes = models.ManyToManyField(User, related_name='poker')
