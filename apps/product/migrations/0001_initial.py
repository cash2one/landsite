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
                ('name', models.CharField(max_length=255, verbose_name='Name', db_index=True)),
                ('description', models.TextField(verbose_name='Description', blank=True)),
                ('image', models.ImageField(max_length=255, upload_to=b'categories', null=True, verbose_name='Image', blank=True)),
            ],
            options={
                'ordering': ['id'],
                'verbose_name': 'Category',
                'verbose_name_plural': 'Categories',
            },
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=128, verbose_name='Name')),
                ('date_created', models.DateTimeField(auto_now_add=True, verbose_name='Date created')),
                ('date_updated', models.DateTimeField(auto_now=True, verbose_name='Date updated', db_index=True)),
                ('category', models.ForeignKey(verbose_name='Category', to='product.Category')),
            ],
            options={
                'ordering': ['-date_created'],
                'verbose_name': 'Product',
                'verbose_name_plural': 'Products',
            },
        ),
    ]
