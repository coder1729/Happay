# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Invoice',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('customer', models.CharField(max_length=200)),
                ('date', models.DateTimeField(verbose_name=b'date published')),
                ('total_quantity', models.IntegerField(default=0)),
                ('total_amount', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='Transaction',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('product', models.CharField(max_length=200)),
                ('quantity', models.IntegerField(default=0)),
                ('price', models.DecimalField(max_digits=20, decimal_places=4)),
                ('line_total', models.DecimalField(max_digits=20, decimal_places=4)),
                ('invoice_id', models.ForeignKey(to='invoice.Invoice')),
            ],
        ),
    ]
