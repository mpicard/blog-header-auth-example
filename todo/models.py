# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models


class Todo(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    text = models.CharField(max_length=64, unique=True)
    done = models.BooleanField(default=False)

    class Meta:
        get_latest_by = 'created'
        indexes = [models.Index(fields=['text'])]

    def __str__(self):
        return self.text
