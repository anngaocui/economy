#!/usr/bin/env python2.7
# -*- coding: utf-8 -*-
# author: Ann

from base import BaseModel
from django.db import models


class Expenditure(BaseModel):  # 支出
    money = models.DecimalField(null=True, blank=True, max_digits=20, decimal_places=2)  # 金额
    type = models.CharField(max_length=64, blank=True, null=True, db_index=True)  # 类型  吃穿住行
    catalog = models.CharField(max_length=64, blank=True, null=True, db_index=True)  # 具体名录
    quantity = models.IntegerField(blank=True, null=True)  # 数量

    class Meta:
        ordering = ['-id']
        db_table = 'app_expenditure'