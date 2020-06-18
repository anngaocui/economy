#!/usr/bin/env python2.7
# -*- coding: utf-8 -*-
# author: Ann

from django.db import models
from django_extensions.db.fields import CreationDateTimeField, ModificationDateTimeField


class BaseModel(models.Model):
    updated_on = ModificationDateTimeField(db_index=True)
    created_on = CreationDateTimeField(db_index=True)
    year = models.IntegerField(blank=True, null=True)
    month = models.IntegerField(blank=True, null=True)

    class Meta:
        abstract = True
