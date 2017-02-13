# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-02-12 21:40
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='booking',
            name='FoodId',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='user.Food'),
        ),
        migrations.AlterField(
            model_name='booking',
            name='Reason',
            field=models.CharField(blank=True, max_length=1000),
        ),
        migrations.AlterField(
            model_name='booking',
            name='Status',
            field=models.IntegerField(choices=[(1, 'CNF'), (2, 'WL'), (3, 'CANCEL'), (4, 'REJECTED'), (0, 'NIL')], default=1),
        ),
    ]
