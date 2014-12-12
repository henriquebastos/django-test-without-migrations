# coding: utf-8
from django.db import models


class Person(models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField()

    def __unicode__(self):
        return self.name
