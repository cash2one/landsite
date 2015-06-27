# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0002_auto_20150624_0018'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='productimage',
            name='caption',
        ),
        migrations.AddField(
            model_name='product',
            name='description',
            field=models.TextField(verbose_name='Description', blank=True),
        ),
    ]
