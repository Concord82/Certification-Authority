# -*- coding: utf-8 -*-
# Generated by Django 1.9.13 on 2017-04-07 08:35
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Cert_Parameters',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=64, verbose_name='\u0418\u043c\u044f \u0441\u0435\u0440\u0442\u0438\u0444\u0438\u043a\u0430\u0442\u0430')),
                ('mash_name', models.CharField(max_length=64, verbose_name='\u041c\u0430\u0448\u0438\u043d\u043e \u043f\u043e\u043d\u044f\u0442\u043d\u043e\u0435 \u0438\u043c\u044f ')),
                ('ca_type', models.CharField(choices=[('CA:TRUE', '\u0428\u0430\u0431\u043b\u043e\u043d \u0441\u0435\u0440\u0442\u0438\u0444\u0438\u043a\u0430\u0442\u0430 \u0423\u0426'), ('CA:FALSE', '\u0428\u0430\u0431\u043b\u043e\u043d \u0434\u0440\u0443\u0433\u043e\u0433\u043e \u0442\u0438\u043f\u0430')], default='CA:FALSE', max_length=10, verbose_name='\u0421\u0435\u0440\u0442\u0438\u0444\u0438\u043a\u0430\u0442 \u0423\u0426')),
                ('nCertType', models.CharField(choices=[('client', '\u0421\u0435\u0440\u0442\u0438\u0444\u043a\u0430\u0442 \u043f\u043e\u043b\u044c\u0437\u043e\u0432\u0430\u0442\u0435\u043b\u044f'), ('email', '\u0417\u0430\u0449\u0438\u0442\u0430 \u044d\u043b\u043a\u0442\u0440\u043e\u043d\u043d\u043e\u0439 \u043f\u043e\u0447\u0442\u044b'), ('server', '\u0421\u0435\u0440\u0442\u0438\u0444\u0438\u043a\u0430\u0442 \u0441\u0435\u0440\u0432\u0435\u0440\u0430')], default='server', max_length=255, verbose_name='\u0442\u0438\u043f \u0441\u0435\u0440\u0442\u0438\u0444\u0438\u043a\u0430\u0442\u0430')),
            ],
        ),
    ]