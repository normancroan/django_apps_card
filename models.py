from django.db import models
import datetime
from django.contrib.postgres.fields import ArrayField

# Create your models here.

class EternalCard(models.Model):
	set = models.CharField(max_length=100)
	name = models.CharField(max_length=100)
	text = models.CharField(max_length=500)
	cost = models.IntegerField(default=0)
	influence = models.CharField(max_length=200)
	colors = ArrayField(models.CharField(max_length=200))
	rarity = models.CharField(max_length=100)
	attack = models.IntegerField(default=0)
	health = models.IntegerField(default=0)
	type = models.CharField(max_length=200)
	subtypes = ArrayField(models.CharField(max_length=200))
	num = models.IntegerField(default=0)
	aliases = ArrayField(models.CharField(max_length=200))
	def __str__(self):
		return self.name

class Chatter(models.Model):
	eternalcard = models.ForeignKey(EternalCard, on_delete=models.CASCADE)
	chatter_type = models.CharField(max_length=100)
	chatter_parent = models.CharField(max_length=500)
	chatter_content = models.CharField(max_length=3000)
	chatter_source = models.CharField(max_length=200)
	pub_date = models.DateTimeField(default=datetime.datetime.now)
	def __str__(self):
		return self.chatter_content
