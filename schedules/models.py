from django.db import models
from django.utils.translation import ugettext_lazy as i18n


class Speaker(models.Model):
    name = models.CharField(
        verbose_name=i18n('Name'),
        max_length=200
    )
    short_bio = models.TextField(
        verbose_name=i18n('Biografy')
    )
    email = models.EmailField(
        verbose_name=i18n('Email')
    )
    github = models.CharField(
        verbose_name=i18n('Github Nickname'),
        max_length=55,
        blank=True,
        null=True
    )
    twitter = models.CharField(
        verbose_name=i18n('Twitter Nickname'),
        max_length=55,
        blank=True,
        null=True
    )

    class Meta:
        verbose_name = i18n('Speaker')
        verbose_name_plural = i18n('Speakers')

    def __unicode__(self):
        return self.name

    def github_url(self):
        return 'http://github.com/%s' % self.github

    def twitter_url(self):
        return 'http://twitter.com/%s' % self.twitter


class Slot(models.Model):
    TYPE_CHOICES = (
        ('talk', i18n('Talks')),
        ('other', i18n('Other')),
    )
    title = models.CharField(
        verbose_name=i18n('Title'),
        max_length=280
    )
    time = models.DateTimeField(
        verbose_name=i18n('Schedule hour')
    )
    abstract = models.TextField(
        verbose_name=i18n('Abstract'),
        blank=True,
        null=True
    )
    tslot = models.CharField(
        verbose_name=i18n('Type of slot'),
        choices=TYPE_CHOICES,
        max_length=10
    )
    speaker = models.ForeignKey(
        Speaker,
        verbose_name=i18n('Speaker'),
        null=True
    )

    class Meta:
        verbose_name = i18n('Slot')
        verbose_name_plural = i18n('Slots')
        ordering = ['-time']

    def __unicode__(self):
        return u'{} - {}'.format(self.time, self.title)
