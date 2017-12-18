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
	post=models.ForeignKey(Post, related_name='comments', null=True)
	comment_text=models.TextField()
	created_date = models.DateTimeField(default=timezone.now)
	approved_comment = models.BooleanField(default=True)

	def approve(self):
		self.approved_comment = True
		self.save()

	def __str__(self):
		return self.comment_text

class Project(models.Model):
	name=models.CharField(max_length=30)
	description=models.TextField()
	link=models.URLField()

	def __unicode__(self):
		return self.name

	

	

