# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-03-27 12:14
from __future__ import unicode_literals

import django.core.validators
from django.db import migrations, models
import zipline_app.models.zipline_app.side


class Migration(migrations.Migration):

    dependencies = [
        ('zipline_app', '0003_account_account_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='limit_price',
            field=zipline_app.models.zipline_app.side.PositiveFloatFieldModel(default=0, validators=[django.core.validators.MaxValueValidator(1000000), django.core.validators.MinValueValidator(0), zipline_app.models.zipline_app.side.validate_nonzero]),
        ),
        migrations.AddField(
            model_name='order',
            name='order_type',
            field=models.CharField(choices=[('M', 'Market'), ('L', 'Limit')], default='L', max_length=1, verbose_name='Type'),
        ),
    ]