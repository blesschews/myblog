# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-12-03 14:31
from __future__ import unicode_literals

import ckeditor_uploader.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myblog', '0004_auto_20171202_1935'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='content',
            field=ckeditor_uploader.fields.RichTextUploadingField(null=True),
        ),
    ]
