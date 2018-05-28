# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('yuekao', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='uaddress',
            field=models.CharField(default=1, max_length=40),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='user',
            name='uemail',
            field=models.CharField(default=11, max_length=20),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='user',
            name='utext',
            field=models.CharField(default=' ', max_length=50),
        ),
    ]
