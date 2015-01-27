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
                ('customer', models.CharField(max_length=100)),
                ('date', models.DateField(auto_now_add=True)),
                ('total_amount', models.DecimalField(max_digits=5, decimal_places=2)),
                ('total_quantity', models.IntegerField()),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Transaction',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('product', models.CharField(max_length=100)),
                ('quantity', models.IntegerField()),
                ('price', models.DecimalField(max_digits=5, decimal_places=2)),
                ('total', models.DecimalField(max_digits=5, decimal_places=2)),
                ('invoice', models.ForeignKey(to='invoices.Invoice')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
