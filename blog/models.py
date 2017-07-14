# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.

class UbtVIP(models.Model):
	class Meta:
		db_table = 'ubt_vip'

	cguid = models.IntegerField()
	gdlc_cd = models.IntegerField()
	brand_no = models.IntegerField()
	vip_cnt = models.IntegerField()

	def __str__(self):
		return self.headline
