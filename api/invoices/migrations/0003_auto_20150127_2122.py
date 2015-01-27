# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('invoices', '0002_auto_20150127_1904'),
    ]

    operations = [
        migrations.AlterField(
            model_name='invoice',
            name='total_amount',
            field=models.DecimalField(max_digits=13, decimal_places=2),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='transaction',
            name='price',
            field=models.DecimalField(max_digits=11, decimal_places=2),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='transaction',
            name='total',
            field=models.DecimalField(max_digits=11, decimal_places=2),
            preserve_default=True,
        ),
    ]
