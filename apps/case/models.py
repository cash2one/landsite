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
    name = models.CharField(_('Name'), max_length=255, db_index=True)
    description = models.TextField(_('Description'), blank=True)
    image = models.ImageField(_('Image'), upload_to='categories', blank=True,
                              null=True, max_length=255)

    def __str__(self):
        return self.name

    class Meta:
        app_label = 'case'
        ordering = ['id']
        verbose_name = _('Category')
        verbose_name_plural = _('Categories')

@python_2_unicode_compatible
class Case(models.Model):
    name = models.CharField(_('Name'), max_length=128)
    description = models.TextField(_('Description'), blank=True)
    category = models.ForeignKey('Category', verbose_name=_("Category"))
    date_created = models.DateTimeField(_("Date created"), auto_now_add=True)
    date_updated = models.DateTimeField(_("Date updated"), auto_now=True, db_index=True)

    class Meta:
        app_label = 'case'
        ordering = ['-date_created']
        verbose_name = _('Case')
        verbose_name_plural = _('Cases')

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
class CaseImage(models.Model):
    """
    An image of a Case
    """
    case = models.ForeignKey(
        'Case', related_name='images', verbose_name=_("Case"))
    original = models.ImageField(
        _("Original"), upload_to='cases', max_length=255)

    #: Use display_order to determine which is the "primary" image
    display_order = models.PositiveIntegerField(
        _("Display order"), default=0,
        help_text=_("An image with a display order of zero will be the primary"
                    " image for a case"))
    date_created = models.DateTimeField(_("Date created"), auto_now_add=True)

    class Meta:
        app_label = 'case'
        ordering = ["display_order"]
        unique_together = ("case", "display_order")
        verbose_name = _('Case image')
        verbose_name_plural = _('Case images')

    def __str__(self):
        return u"Image of '%s'" % self.case

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
        super(CaseImage, self).delete(*args, **kwargs)
        for idx, image in enumerate(self.case.images.all()):
            image.display_order = idx
            image.save()