from django.db import models
from django.utils.translation import ugettext_lazy as i18n


class Sponsor(models.Model):
    TYPE_CHOICES = (
        ('diamond', i18n('Diamond')),
        ('platinum', i18n('Platinum')),
        ('gold', i18n('Gold')),
        ('silver', i18n('Silver')),
    )

    name = models.CharField(
        verbose_name=i18n('Name'),
        max_length=200
    )
    url = models.URLField(
        verbose_name=i18n('URL'),
        blank=True,
        null=True
    )
    thumbnail = models.ImageField(
        verbose_name=i18n('Thumbnail'),
        upload_to='/sponsors/thumbnail/'
    )
    picture = models.ImageField(
        verbose_name=i18n('Picture'),
        upload_to='/sponsors/'
    )
    tsponsor = models.CharField(
        verbose_name=i18n('Type of sponsor'),
        choices=TYPE_CHOICES,
        max_length=10
    )

    class Meta:
        verbose_name = i18n('Sponsor')
        verbose_name_plural = i18n('Sponsors')

    def __unicode__(self):
        return '%s - %s' % (self.tsponsor, self.name)
