# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('invoice', '0003_auto_20150919_0918'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='invoice',
            name='invoice_id',
        ),
        migrations.AlterField(
            model_name='transaction',
            name='invoice_id',
            field=models.ForeignKey(to='invoice.Invoice'),
        ),
    ]
