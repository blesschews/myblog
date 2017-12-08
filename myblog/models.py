# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.utils import timezone
from ckeditor_uploader.fields import RichTextUploadingField

# Create your models here.
class Post(models.Model):
	title=models.CharField(max_length=100)
	tags=models.ManyToManyField('Tag')
	body=models.TextField()
	content = RichTextUploadingField(null=True)
	date_created=models.DateTimeField(default=timezone.now)
	date_published=models.DateTimeField(null=True, blank=True)

	def __unicode__(self):
		return self.title



class Tag(models.Model):
	name=models.CharField(max_length=30)
	description=models.TextField()

	def __unicode__(self):
		return self.name


class Comment(models.Model):
	name=models.CharField(max_length=32)
	email=models.EmailField()
	comment_text=models.TextField()


	

	

