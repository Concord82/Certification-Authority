# -*- coding: utf-8 -*-
# Generated by Django 1.9.13 on 2017-04-07 08:37
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('sslconfig', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='cert_parameters',
            old_name='nCertType',
            new_name='nsCertType',
        ),
    ]
