# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('yuekao', '0002_auto_20180528_0613'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='uaddress',
            field=models.CharField(default=None, max_length=40),
        ),
        migrations.AlterField(
            model_name='user',
            name='uemail',
            field=models.CharField(default=None, max_length=20),
        ),
        migrations.AlterField(
            model_name='user',
            name='utext',
            field=models.CharField(default=None, max_length=50),
        ),
    ]
