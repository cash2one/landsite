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

from tinymce import models as tinymce_models

class News(models.Model):
    title = models.CharField(_('title'), max_length=256)
    image = models.ImageField(_('Image'), upload_to='news', max_length=255)
    introduction = models.TextField(_('Introduction'))
    content = tinymce_models.HTMLField()
    date_created = models.DateTimeField(_("Date created"), auto_now_add=True)
    date_updated = models.DateTimeField(_("Date updated"), auto_now=True, db_index=True)

    def __str__(self):
        return self.title

    class Meta:
        app_label = "civilization"
        ordering = ["id"]
        verbose_name = _("News")
        verbose_name_plural = _("News")