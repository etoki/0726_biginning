# coding: utf-8
from __future__ import unicode_literals
from django.db import models


class Category(models.Model):
	name = models.CharField(max_length=200,unique=True)

	class Meta():
		verbose_name = verbose_name_plural = u'カテゴリ'

	def __unicode__(self):
		return self.name

PRIORITY_CHOICES = (('N','new'),('S','soon'),('L','later'))
class Todo(models.Model):
	title            = models.CharField(max_length = 200)
	description      = models.TextField(blank = True)
	datetime_created = models.DateTimeField(auto_now_add = True)
	is_finished      = models.BooleanField(default = False)
	priority         = models.CharField(max_length = 1, choices = PRIORITY_CHOICES, default = 'L')
	category         = models.ForeignKey(Category)
	
	class Meta():
		verbose_name = verbose_name_plural = u'Todo'

	def __unicode__(self):
		return self.title[:20]+u'...'