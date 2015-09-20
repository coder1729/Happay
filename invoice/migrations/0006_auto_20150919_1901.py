# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('invoice', '0005_auto_20150919_1102'),
    ]

    operations = [
        migrations.AlterField(
            model_name='transaction',
            name='invoice_id',
            field=models.ForeignKey(related_name='transactions', to='invoice.Invoice'),
        ),
    ]
