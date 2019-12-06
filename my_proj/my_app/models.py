from django.contrib.postgres.fields import JSONField, ArrayField
from django.db import models


class Gadget(models.Model):
	code = models.SlugField(max_length=10)
	category = models.CharField(max_length=50)
	link = models.URLField()
	price = models.PositiveIntegerField()
	cashback = models.PositiveIntegerField()
	full_desc = models.TextField()
	tech = JSONField()
	photo_links = ArrayField(models.URLField())
