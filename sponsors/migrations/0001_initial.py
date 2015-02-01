# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Sponsor',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, serialize=False, primary_key=True)),
                ('name', models.CharField(max_length=200, verbose_name='Name')),
                ('url', models.URLField(verbose_name='URL')),
                ('thumbnail', models.ImageField(upload_to='/sponsors/thumbnail/', verbose_name='Thumbnail')),
                ('picture', models.ImageField(upload_to='/sponsors/', verbose_name='Picture')),
                ('tsponsor', models.CharField(choices=[('diamond', 'Diamond'), ('platinum', 'Platinum'), ('gold', 'Gold'), ('silver', 'Silver')], max_length=10, verbose_name='Type of sponsor')),
            ],
            options={
                'verbose_name': 'Sponsor',
                'verbose_name_plural': 'Sponsors',
            },
            bases=(models.Model,),
        ),
    ]
