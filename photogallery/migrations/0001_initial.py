# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('cat_name', models.CharField(unique=True, max_length=250)),
                ('description', models.TextField()),
                ('slug', models.SlugField(unique=True)),
            ],
            options={
                'ordering': ['cat_name'],
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Photo',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=100)),
                ('image', models.ImageField(upload_to=b'photogallery')),
                ('caption', models.CharField(max_length=250, blank=True)),
                ('slug', models.SlugField(unique=True)),
                ('item', models.ForeignKey(to='photogallery.Category')),
            ],
            options={
                'ordering': ['title'],
            },
            bases=(models.Model,),
        ),
    ]
