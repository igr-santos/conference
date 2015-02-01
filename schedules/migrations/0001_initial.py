# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Slot',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=280, verbose_name='Title')),
                ('time', models.DateTimeField(verbose_name='Schedule hour')),
                ('abstract', models.TextField(verbose_name='Abstract', blank=True, null=True)),
                ('tslot', models.CharField(max_length=10, verbose_name='Type of slot', choices=[('talk', 'Talks'), ('other', 'Other')])),
            ],
            options={
                'verbose_name': 'Slot',
                'ordering': ['-time'],
                'verbose_name_plural': 'Slots',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Speaker',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=200, verbose_name='Name')),
                ('short_bio', models.TextField(verbose_name='Biografy')),
                ('email', models.EmailField(max_length=75, verbose_name='Email')),
                ('github', models.CharField(max_length=55, verbose_name='Github Nickname', blank=True, null=True)),
                ('twitter', models.CharField(max_length=55, verbose_name='Twitter Nickname', blank=True, null=True)),
            ],
            options={
                'verbose_name': 'Speaker',
                'verbose_name_plural': 'Speakers',
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='slot',
            name='speaker',
            field=models.ForeignKey(verbose_name='Speaker', to='schedules.Speaker', null=True),
            preserve_default=True,
        ),
    ]
