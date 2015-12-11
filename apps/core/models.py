from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Menu(models.Model):
	title = models.CharField(max_length=100)


class SubMenu(models.Model):
	title = models.CharField(max_length=100)
	url = models.CharField(max_length=100)
	menu = models.ForeignKey(Menu)
