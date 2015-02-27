# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import photogallery.models


class Migration(migrations.Migration):

    dependencies = [
        ('photogallery', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='photo',
            options={'ordering': ['title', 'image']},
        ),
        migrations.RemoveField(
            model_name='category',
            name='slug',
        ),
        migrations.RemoveField(
            model_name='photo',
            name='slug',
        ),
        migrations.AlterField(
            model_name='photo',
            name='image',
            field=photogallery.models.ThumbnailImageField(upload_to=b'photogallery'),
            preserve_default=True,
        ),
    ]
