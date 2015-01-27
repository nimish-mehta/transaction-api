# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('invoices', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='transaction',
            name='invoice',
            field=models.ForeignKey(related_name='transactions', to='invoices.Invoice'),
            preserve_default=True,
        ),
    ]
