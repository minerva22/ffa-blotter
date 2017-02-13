# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-02-13 09:43
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0012_auto_20170213_0907'),
    ]

    operations = [
        migrations.CreateModel(
            name='Asset',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('asset_sid', models.CharField(max_length=20)),
                ('asset_symbol', models.CharField(max_length=20)),
                ('asset_exchange', models.CharField(max_length=200)),
                ('asset_name', models.CharField(max_length=200)),
            ],
        ),
        migrations.RemoveField(
            model_name='fill',
            name='fill_symbol',
        ),
        migrations.RemoveField(
            model_name='order',
            name='order_symbol',
        ),
        migrations.AddField(
            model_name='fill',
            name='asset',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='polls.Asset'),
        ),
        migrations.AddField(
            model_name='order',
            name='asset',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='polls.Asset'),
        ),
    ]