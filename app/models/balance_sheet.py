#!/usr/bin/env python2.7
# -*- coding: utf-8 -*-
# author: Ann

from base import BaseModel
from django.db import models


class BalanceSheet(BaseModel):  # 资产负债表
    funds = models.DecimalField(null=True, blank=True, max_digits=20, decimal_places=2)  # 金额
    type = models.CharField(max_length=64, blank=True, null=True, db_index=True)  # 类型 存款,微信,支付宝,投资,借出,欠债
    is_debt = models.BooleanField(default=False, db_index=True)
    note = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        ordering = ['-id']
        db_table = 'app_balance_sheet'