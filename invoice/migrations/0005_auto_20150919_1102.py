# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('invoice', '0004_auto_20150919_0950'),
    ]

    operations = [
        migrations.AlterField(
            model_name='transaction',
            name='invoice_id',
            field=models.IntegerField(default=0),
        ),
    ]
