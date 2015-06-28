# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0003_auto_20150625_0025'),
    ]

    operations = [
        migrations.CreateModel(
            name='IndexProduct',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('description', models.TextField(verbose_name='Description', blank=True)),
                ('product', models.ForeignKey(verbose_name='product', to='product.Product')),
            ],
            options={
                'ordering': ['id'],
                'verbose_name': 'Index Product',
                'verbose_name_plural': 'Index Products',
            },
        ),
    ]
