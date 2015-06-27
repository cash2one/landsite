# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ProductImage',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('original', models.ImageField(upload_to=b'products', max_length=255, verbose_name='Original')),
                ('caption', models.CharField(max_length=200, verbose_name='Caption', blank=True)),
                ('display_order', models.PositiveIntegerField(default=0, help_text='An image with a display order of zero will be the primary image for a product', verbose_name='Display order')),
                ('date_created', models.DateTimeField(auto_now_add=True, verbose_name='Date created')),
                ('product', models.ForeignKey(related_name='images', verbose_name='Product', to='product.Product')),
            ],
            options={
                'ordering': ['display_order'],
                'verbose_name': 'Product image',
                'verbose_name_plural': 'Product images',
            },
        ),
        migrations.AlterUniqueTogether(
            name='productimage',
            unique_together=set([('product', 'display_order')]),
        ),
    ]
