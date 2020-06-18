#!/usr/bin/env python2.7
# -*- coding: utf-8 -*-
# author: Ann
from base import BaseModel
from django.db import models


class Consumption(BaseModel):  # 收入
    wage = models.DecimalField(null=True, blank=True, max_digits=20, decimal_places=2)  # 收入
    type = models.CharField(max_length=64, blank=True, null=True, db_index=True)  # 类型
