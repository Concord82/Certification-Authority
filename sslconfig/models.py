# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.utils.translation import ugettext_lazy as _
from django.db import models
from django.forms import widgets
# Create your models here.

class Cert_Parameters(models.Model):
    SSL_CA = (
        ('CA:TRUE','Шаблон сертификата УЦ'),
        ('CA:FALSE','Шаблон другого типа')
    )
    NS_CERT_TYPE = (
        ('client', 'Сертифкат пользователя'),
        ('email', 'Защита элктронной почты'),
        ('server', 'Сертификат сервера')
    )
    title = models.CharField(verbose_name='Имя сертификата', max_length=64)
    mash_name = models.CharField(verbose_name='Машино понятное имя ', max_length=64)
    ca_type = models.CharField(verbose_name='Сертификат УЦ', choices=SSL_CA, default='CA:FALSE', max_length=10)
    nsCertType = models.CharField(verbose_name='тип сертификата', choices=NS_CERT_TYPE, max_length=255, default='server' )



