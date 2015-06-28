# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0004_indexproduct'),
    ]

    operations = [
        migrations.AddField(
            model_name='indexproduct',
            name='index_image',
            field=models.ImageField(max_length=255, upload_to=b'index_image', null=True, verbose_name='IndexImage', blank=True),
        ),
    ]
