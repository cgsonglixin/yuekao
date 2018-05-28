# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('yuekao', '0003_auto_20180528_0628'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='uaddress',
            field=models.CharField(max_length=40, default='  '),
        ),
        migrations.AlterField(
            model_name='user',
            name='uemail',
            field=models.CharField(max_length=20, default='  '),
        ),
        migrations.AlterField(
            model_name='user',
            name='utext',
            field=models.CharField(max_length=50, default='  '),
        ),
    ]
