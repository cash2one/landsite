# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Case',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=128, verbose_name='Name')),
                ('description', models.TextField(verbose_name='Description', blank=True)),
                ('date_created', models.DateTimeField(auto_now_add=True, verbose_name='Date created')),
                ('date_updated', models.DateTimeField(auto_now=True, verbose_name='Date updated', db_index=True)),
            ],
            options={
                'ordering': ['-date_created'],
                'verbose_name': 'Case',
                'verbose_name_plural': 'Cases',
            },
        ),
        migrations.CreateModel(
            name='CaseImage',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('original', models.ImageField(upload_to=b'cases', max_length=255, verbose_name='Original')),
                ('display_order', models.PositiveIntegerField(default=0, help_text='An image with a display order of zero will be the primary image for a case', verbose_name='Display order')),
                ('date_created', models.DateTimeField(auto_now_add=True, verbose_name='Date created')),
                ('case', models.ForeignKey(related_name='images', verbose_name='Case', to='case.Case')),
            ],
            options={
                'ordering': ['display_order'],
                'verbose_name': 'Case image',
                'verbose_name_plural': 'Case images',
            },
        ),
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
        migrations.AddField(
            model_name='case',
            name='category',
            field=models.ForeignKey(verbose_name='Category', to='case.Category'),
        ),
        migrations.AlterUniqueTogether(
            name='caseimage',
            unique_together=set([('case', 'display_order')]),
        ),
    ]
