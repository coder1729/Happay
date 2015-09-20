# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('invoice', '0002_invoice_invoice_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='transaction',
            name='invoice_id',
            field=models.IntegerField(default=0),
        ),
    ]
