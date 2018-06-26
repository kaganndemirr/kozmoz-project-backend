# Standart Library
import datetime

# Django
from django.db import models
from django.utils.translation import ugettext_lazy as _

# Local
from .formatChecker import ContentTypeRestrictedFileField

class Post(models.Model):
    description = models.TextField(
        verbose_name='Description', max_length=1000, blank=True
        )
    publishing_date = models.DateTimeField(verbose_name=_('Date'))
    media = ContentTypeRestrictedFileField(
        upload_to='uploads/', content_types=['video/mp4'],
        max_upload_size=5242880, blank=False, null=False
        )
    user = models.ForeignKey(
        verbose_name=_('User'), to='users.User', related_name='posts',
        on_delete=models.CASCADE
    )

    class Meta:
        verbose_name = _('Post')
        verbose_name_plural = ('Posts')
        ordering = ('user',)

    def __str__(self):
        return '{title}'.format(title=self.title)
