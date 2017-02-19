# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-02-19 06:43
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Booking',
            fields=[
                ('GNR', models.AutoField(primary_key=True, serialize=False)),
                ('StartTime', models.DateField()),
                ('EndTime', models.DateField()),
                ('AmountReq', models.CharField(max_length=100)),
                ('AmountPaid', models.CharField(max_length=100)),
                ('Status', models.IntegerField(choices=[(1, 'CNF'), (2, 'WL'), (3, 'CANCEL'), (4, 'REJECTED'), (0, 'NIL')], default=1)),
                ('Reason', models.CharField(blank=True, max_length=1000)),
                ('BookingTime', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'ordering': ['GNR'],
            },
        ),
        migrations.CreateModel(
            name='Food',
            fields=[
                ('Id', models.AutoField(primary_key=True, serialize=False)),
                ('Name', models.CharField(max_length=40)),
                ('Status', models.CharField(max_length=10)),
            ],
            options={
                'ordering': ['Id'],
            },
        ),
        migrations.CreateModel(
            name='Person',
            fields=[
                ('Id', models.AutoField(primary_key=True, serialize=False)),
                ('Name', models.CharField(max_length=30)),
                ('Password', models.CharField(max_length=50)),
                ('Email', models.EmailField(blank=True, max_length=254)),
                ('type', models.CharField(max_length=30)),
            ],
            options={
                'ordering': ['Id'],
            },
        ),
        migrations.CreateModel(
            name='Room',
            fields=[
                ('Id', models.AutoField(primary_key=True, serialize=False)),
                ('Cost', models.CharField(max_length=40)),
                ('type', models.IntegerField(choices=[(1, 'Unreserved'), (2, 'reserved'), (3, 'Not Available')], default=1)),
            ],
            options={
                'ordering': ['Id'],
            },
        ),
        migrations.CreateModel(
            name='Administrator',
            fields=[
                ('person_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='basic.Person')),
            ],
            bases=('basic.person',),
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('person_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='basic.Person')),
            ],
            bases=('basic.person',),
        ),
        migrations.AddField(
            model_name='booking',
            name='FoodId',
            field=models.ForeignKey(default=1.0, on_delete=django.db.models.deletion.CASCADE, to='basic.Food'),
        ),
        migrations.AddField(
            model_name='booking',
            name='RoomId',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='basic.Room'),
        ),
        migrations.AddField(
            model_name='booking',
            name='UserId',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='basic.User'),
        ),
    ]