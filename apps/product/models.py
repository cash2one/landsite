# -*- coding: UTF-8 -*-
import os
from django.utils import six
from datetime import datetime, date
import logging

from django.utils.html import strip_tags
from django.utils.safestring import mark_safe
from django.conf import settings
from django.contrib.staticfiles.finders import find
from django.core.cache import cache
from django.core.exceptions import ValidationError, ImproperlyConfigured
from django.core.files.base import File
from django.core.urlresolvers import reverse
from django.core.validators import RegexValidator
from django.db import models
from django.db.models import Sum, Count
from django.utils.encoding import python_2_unicode_compatible
from django.utils.translation import ugettext_lazy as _, pgettext_lazy
from django.utils.functional import cached_property
from django.contrib.contenttypes.generic import GenericForeignKey
from django.contrib.contenttypes.models import ContentType

@python_2_unicode_compatible
class Category(models.Model):
    name = models.CharField(_('种类名'), max_length=255, db_index=True)
    description = models.TextField(_('描述'), blank=True)
    image = models.ImageField(_('图片'), upload_to='categories', blank=True,
                              null=True, max_length=255)

    def __str__(self):
        return self.name

    class Meta:
        app_label = 'product'
        ordering = ['id']
        verbose_name = _('种类')
        verbose_name_plural = _('种类')

@python_2_unicode_compatible
class Product(models.Model):
    name = models.CharField(_('名称'), max_length=128)
    description = models.TextField(_('描述'), blank=True)
    category = models.ForeignKey('Category', verbose_name=_("种类"))
    date_created = models.DateTimeField(_("Date created"), auto_now_add=True)
    date_updated = models.DateTimeField(_("Date updated"), auto_now=True, db_index=True)

    class Meta:
        app_label = 'product'
        ordering = ['-date_created']
        verbose_name = _('产品')
        verbose_name_plural = _('产品')

    def __str__(self):
        return self.name

    def get_primary_image_url(self):
        try:
            url = self.images.get(display_order=0).original.url
        except: 
            url = None
        return url

    def get_all_image_url(self):
        image_urls = []
        images = self.images.all()[1:]
        for i in images:
            image_urls.append(i.original.url)
        return image_urls

@python_2_unicode_compatible
class ProductImage(models.Model):
    """
    An image of a product
    """
    product = models.ForeignKey(
        'Product', related_name='images', verbose_name=_("产品"))
    original = models.ImageField(
        _("图片"), upload_to='products', max_length=255)

    #: Use display_order to determine which is the "primary" image
    display_order = models.PositiveIntegerField(
        _("显示顺序"), default=0,
        help_text=_("0代表主图"))
    date_created = models.DateTimeField(_("Date created"), auto_now_add=True)

    class Meta:
        app_label = 'product'
        ordering = ["display_order"]
        unique_together = ("product", "display_order")
        verbose_name = _('产品图片')
        verbose_name_plural = _('产品图片')

    def __str__(self):
        return u"Image of '%s'" % self.product

    def is_primary(self):
        """
        Return bool if image display order is 0
        """
        return self.display_order == 0

    def delete(self, *args, **kwargs):
        """
        Always keep the display_order as consecutive integers. This avoids
        issue #855.
        """
        super(ProductImage, self).delete(*args, **kwargs)
        for idx, image in enumerate(self.product.images.all()):
            image.display_order = idx
            image.save()

class IndexProduct(models.Model):
    index_image = models.ImageField(_('首页图片'), upload_to='index_image', blank=True,
                              null=True, max_length=255)
    product = models.ForeignKey("Product", verbose_name=_("产品"))
    description = models.TextField(_('描述'), blank=True)

    def __str__(self):
        return self.product.name

    class Meta:
        app_label = "product"
        ordering = ["id"]
        verbose_name = _("首页产品")
        verbose_name_plural = _("首页产品")

from tinymce import models as tinymce_models

class Mine(models.Model):
    name = models.CharField(_('名称'), max_length=128)
    image = models.ImageField(_('Image'), upload_to='矿区', max_length=255)
    description = tinymce_models.HTMLField()

    def __str__(self):
        return self.name

    class Meta:
        app_label = "product"
        ordering = ["id"]
        verbose_name = _("矿区")
        verbose_name_plural = _("矿区")